import numpy as np
from PIL import Image
import sounddevice as sd

IMG_SIZE = (128, 128)
FS = 44100
DURATION_PER_PIXEL = 0.002 # 5ms por pixel
F0 = 400   # frequência mínima
F1 = 2000  # frequência máxima

def img_to_rgb_data(img_path):
    img = Image.open(img_path).convert("RGB").resize(IMG_SIZE)
    r, g, b = img.split()
    data = np.concatenate([
        np.array(r).flatten(),
        np.array(g).flatten(),
        np.array(b).flatten()
    ])
    return data

def data_to_fm_signal(data):
    signal = []
    t = np.linspace(0, DURATION_PER_PIXEL, int(FS * DURATION_PER_PIXEL), False)
    for value in data:
        freq = F0 + (F1 - F0) * (value / 255)
        tone = np.sin(2 * np.pi * freq * t)
        signal.extend(tone)
    return np.array(signal)

def main():
    print("Convertendo imagem...")
    data = img_to_rgb_data("imagem.png")
    print("Gerando sinal de áudio...")
    signal = data_to_fm_signal(data)
    print("Transmitindo imagem via som...")
    sd.play(signal, samplerate=FS)
    sd.wait()
    print("Transmissão concluída.")

if __name__ == "__main__":
    main()
