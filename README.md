# OCR em PDF com pytesseract

#### Este é um script Python simples que extrai texto de um arquivo PDF usando OCR (Reconhecimento Óptico de Caracteres) com o pytesseract.

## Pré-requisitos

- Python 3.x

- pytesseract

- pdf2image

- Tesseract OCR

- Poppler

## Instalação

#### Tesseract OCR

```bash
  Baixe e instale o Tesseract OCR para Windows a partir do repositório oficial.
  Pode ser que precise por o caminho do path da pasta bin
  https://github.com/UB-Mannheim/tesseract/wiki
```
    
#### Poppler

```bash
  Baixe e instale o Poppler para Windows a partir do repositório oficial.
  Pode ser que precise por o caminho do path da pasta bin
  https://github.com/oschwartz10612/poppler-windows/releases
```

#### Instalar dependências Python

```bash
  pip install pytesseract pdf2image
```

## Uso/Exemplos
 No cmd use o comando:
```bash 
  python -h 
```
  ou

  Execute o script ocr_pdf.py fornecendo o caminho para o arquivo PDF como argumento. Por exemplo:
``` 
  python ocr_pdf.py caminho_do_seu_arquivo.pdf 8
```
O segundo argumento é opcional e representa o número de páginas a serem processadas. Se não for fornecido, todas as páginas serão processadas.

Os arquivos de texto resultantes serão salvos no diretório atual com o formato page_X.txt, onde X é o número da página.
