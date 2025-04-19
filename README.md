# 📡 SonicImage – Transmissão de Imagens via Áudio (FM)

Este projeto permite **transmitir uma imagem por som** usando modulação por frequência (FM). Uma imagem é convertida em tons sonoros, transmitida via alto-falante e reconstruída em tempo real com o microfone.

---

## 🎯 Objetivo

Explorar formas de **comunicação acústica** (Data over Sound) simulando um protocolo simples de envio de imagens via ondas sonoras. Isso pode ser útil para:
- Comunicação sem rede
- Transmissão de dados entre dispositivos simples
- Educação em sinais, áudio digital e codificação

---

## 🧠 Como funciona

1. **Transmissor:**
   - Carrega uma imagem RGB.
   - Converte os valores de cor (0–255) em frequências entre `F0` e `F1`.
   - Emite essas frequências em sequência via áudio.

2. **Receptor:**
   - Grava o som recebido pelo microfone.
   - Para cada segmento, usa FFT para extrair a frequência dominante.
   - Reconstrói os canais RGB e monta a imagem ao vivo.

---

## 🛠️ Requisitos

- Python 3.x
- Bibliotecas:
  - `numpy`
  - `sounddevice`
  - `Pillow`
  - `matplotlib`

Instale com:

```bash
pip install numpy sounddevice pillow matplotlib
