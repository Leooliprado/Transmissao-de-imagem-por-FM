import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from PIL import Image

IMG_SIZE = (128, 128)
NUM_PIXELS = IMG_SIZE[0] * IMG_SIZE[1]
FS = 44100
DURATION_PER_PIXEL = 0.002
SAMPLES_PER_PIXEL = int(FS * DURATION_PER_PIXEL)
F0 = 400
F1 = 2000

# Buffers para armazenar os dados RGB
r = np.zeros(NUM_PIXELS)
g = np.zeros(NUM_PIXELS)
b = np.zeros(NUM_PIXELS)
data = []
i = 0  # contador global de pixels

# Inicializa figura
plt.ion()
fig, ax = plt.subplots()
image_array = np.zeros((IMG_SIZE[0], IMG_SIZE[1], 3), dtype=np.uint8)
im = ax.imshow(image_array)
plt.title("Imagem sendo reconstruída...")
plt.show()

def audio_callback(indata, frames, time, status):
    global i, data, r, g, b

    if status:
        print(status)

    # Divide o sinal em segmentos de pixels
    samples = indata[:, 0]
    while len(samples) >= SAMPLES_PER_PIXEL:
        segment = samples[:SAMPLES_PER_PIXEL]
        samples = samples[SAMPLES_PER_PIXEL:]

        # FFT com janela de Hamming
        windowed = segment * np.hamming(len(segment))
        fft = np.abs(np.fft.rfft(windowed))
        freqs = np.fft.rfftfreq(len(segment), 1 / FS)
        dominant_freq = freqs[np.argmax(fft)]
        value = int(255 * (dominant_freq - F0) / (F1 - F0))
        value = np.clip(value, 0, 255)
        data.append(value)

        # Atualiza pixel
        if i < NUM_PIXELS:
            r[i] = value
        elif i < 2 * NUM_PIXELS:
            g[i - NUM_PIXELS] = value
        elif i < 3 * NUM_PIXELS:
            b[i - 2 * NUM_PIXELS] = value

        i += 1

        # Atualiza imagem a cada 500 pixels
        if i % 500 == 0 or i == NUM_PIXELS * 3:
            image_array[:, :, 0] = r.reshape(IMG_SIZE)
            image_array[:, :, 1] = g.reshape(IMG_SIZE)
            image_array[:, :, 2] = b.reshape(IMG_SIZE)
            im.set_data(image_array)
            plt.draw()
            plt.pause(0.001)

        if i >= NUM_PIXELS * 3:
            raise sd.CallbackStop  # Para a gravação quando a imagem estiver completa

def main():
    duration = NUM_PIXELS * 3 * DURATION_PER_PIXEL
    print("Gravando e reconstruindo ao vivo...")

    with sd.InputStream(callback=audio_callback, channels=1, samplerate=FS, blocksize=SAMPLES_PER_PIXEL):
        sd.sleep(int(duration * 1000))  # tempo total em milissegundos

    plt.ioff()
    plt.show()

    print("Reconstrução finalizando...")

    # Salva imagem final
    img = Image.merge("RGB", [
        Image.fromarray(r.reshape(IMG_SIZE).astype(np.uint8)),
        Image.fromarray(g.reshape(IMG_SIZE).astype(np.uint8)),
        Image.fromarray(b.reshape(IMG_SIZE).astype(np.uint8)),
    ])
    img.save("imagem_recebida.png")
    print("Imagem salva como 'imagem_recebida.png'.")
    img.show()

if __name__ == "__main__":
    main()
