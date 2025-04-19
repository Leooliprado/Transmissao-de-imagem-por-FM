
# 📡 SonicImage – Transmissão de Imagens via Áudio (FM)

Transmita imagens usando ondas sonoras! Projeto educativo para comunicação acústica entre dispositivos.

---

## 📌 **Visão Geral do Projeto**
- **Objetivo**:  
  Transmitir imagens usando ondas sonoras (*Data over Sound*), útil para:
  - Comunicação sem internet
  - Transferência entre dispositivos simples
  - Fins educacionais em processamento de sinais

- **Funcionamento**:
  - **Transmissor**:  
    Converte valores RGB (0-255) em tons de áudio (400Hz-2000Hz) e emite via alto-falante.
  - **Receptor**:  
    Capta áudio via microfone, decodifica frequências (usando FFT) e reconstrói a imagem em tempo real.

---

## 🚀 **Como Usar**

### 1️⃣ **Pré-requisitos**
- Python 3.x + Bibliotecas:
  ```bash
  pip install numpy sounddevice pillow matplotlib
  ```

### 2️⃣ **Preparação da Imagem**
- **Redimensione para 128x128 pixels** (obrigatório):  
  🔗 *Ferramenta online:* [safeimagekit.com/resize-image-to-128x128](https://safeimagekit.com/resize-image-to-128x128)
- Salve como `imagem.png` na pasta do projeto.

### 3️⃣ **Execução Automatizada**
```bash
chmod +x executar_transmissao.sh  # Dar permissão
./executar_transmissao.sh         # Roda transmissor e receptor
```

### ⚠️ Modo Manual (alternativo)
```bash
# Terminal 1 - Transmissor
python transmissor.py

# Terminal 2 - Receptor (outro dispositivo)
python receptor.py
```

---

## ⚙️ **Parâmetros Técnicos**
| Parâmetro           | Valor Padrão   | Descrição                          |
|---------------------|---------------|-----------------------------------|
| `IMG_SIZE`          | `(128, 128)`  | Dimensões da imagem                |
| `FS`                | `44100 Hz`    | Taxa de amostragem do áudio        |
| `DURATION_PER_PIXEL`| `0.002 s`     | Duração de cada pixel no áudio     |
| `F0`, `F1`          | `400-2000 Hz` | Frequências para valores 0 e 255   |

---

## 🎨 **Saída**
- Reconstrução em tempo real da imagem
- Salva automaticamente como `imagem_recebida.png`

---

## 🔧 **Código Útil**
```python
# Redimensionamento via Python
from PIL import Image
Image.open("imagem.png").resize((128, 128)).save("imagem_128x128.png")
```

---

## 🌟 **Inspiração**
- Comunicação acústica submarina
- Modems antigos (300 baud)
- Troca de dados por som entre smartphones

---

## 📜 **Licença**
MIT - Livre para uso e modificação

---

## 👨‍💻 **Autor**
Leonardo ([GitHub @Leooliprado](https://github.com/Leooliprado))

---

```bash
# Clone o repositório
git clone https://github.com/Leooliprado/Transmissao-de-imagem-por-FM.git
```


