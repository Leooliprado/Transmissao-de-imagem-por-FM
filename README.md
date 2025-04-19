### 📌 **Visão Geral do Projeto**
- **Objetivo**: Transmitir imagens usando ondas sonoras (Data over Sound), útil para comunicação sem internet, transferência entre dispositivos simples ou fins educacionais.
- **Funcionamento**:
  - **Transmissor**: Converte valores de cor (RGB) de uma imagem em tons de áudio (frequências entre `400 Hz` e `2000 Hz`) e os emite via alto-falante.
  - **Receptor**: Capta o áudio via microfone, decodifica as frequências (usando FFT) e reconstrói a imagem em tempo real.

### 🛠️ **Configuração Necessária**
- **Python 3.x** + Bibliotecas:
  ```bash
  pip install numpy sounddevice pillow matplotlib
  ```
- **Passos para uso**:
  1. Coloque uma imagem chamada `imagem.png` na pasta do projeto.
  2. Execute o transmissor:  
     ```bash
     python transmissor.py
     ```
  3. Execute o receptor (em outro dispositivo/terminal):  
     ```bash
     python receptor.py
     ```
  - A imagem será reconstruída gradualmente e salva como `imagem_recebida.png`.

### ⚙️ **Parâmetros Ajustáveis**
| Parâmetro           | Valor Padrão   | Descrição                          |
|---------------------|---------------|-----------------------------------|
| `IMG_SIZE`          | `(128, 128)`  | Tamanho da imagem (redimensionada) |
| `FS`                | `44100 Hz`    | Taxa de amostragem do áudio        |
| `DURATION_PER_PIXEL`| `0.002 s`     | Duração de cada pixel no áudio     |
| `F0`, `F1`          | `400-2000 Hz` | Frequências para valores 0 e 255   |

### 🎨 **Exemplo de Saída**
- A imagem recebida será exibida em tempo real e salva no final do processo.

### 🔍 **Inspiração**
- Técnicas de comunicação acústica submarina, modems antigos (ex.: 300 baud) e troca de dados por som entre dispositivos móveis.

### 📜 **Licença**
- **MIT** (livre para uso, modificação e distribuição).

### 👨‍💻 **Autor**
- Projeto desenvolvido por **Leonardo** (GitHub: [@Leooliprado](https://github.com/Leooliprado)).

---

Se você quiser testar ou contribuir, clone o repositório:
```bash
git clone https://github.com/Leooliprado/Transmissao-de-imagem-por-FM.git
```

Alguma dúvida específica sobre o funcionamento ou implementação? 😊
