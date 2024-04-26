import argparse
from pdf2image import convert_from_path
import pytesseract

def ocr_pdf(pdf_path, num_pages):
    # Convertendo o PDF em uma lista de imagens para o pytesseract
    pages = convert_from_path(pdf_path)

    # Passa como argumento o numero de paginas que foram ser passadas
    pages = pages[:num_pages]

    for i, page in enumerate(pages):
        # Convertendo a imagem para texto usando OCR pytesseract
        text = pytesseract.image_to_string(page)  
        
        # Salvar os arquivos em txt com a numeração das paginas
        with open(f'page_{i+1}.txt', 'w', encoding='utf-8') as f:
            f.write(text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract text from a specified number of pages from a PDF file using OCR')
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
    parser.add_argument('num_pages', type=int, help='Number of pages to process')
    args = parser.parse_args()
    
    ocr_pdf(args.pdf_path, args.num_pages)
