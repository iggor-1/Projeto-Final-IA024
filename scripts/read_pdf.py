import pdfplumber

pdf_path = "IRPF2024.pdf"

text_pages = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        text_pages.append(text)

output_txt_path = pdf_path + ".txt"

with open(output_txt_path, "w", encoding="utf-8") as txt_file:
    for page_number, text in enumerate(text_pages):
        txt_file.write(f"Página {page_number + 1}:\n")
        txt_file.write(text)
        txt_file.write("\n-----------------------------------------\n")

page_number_to_print = 8
page = text_pages[page_number_to_print-1]

print(f"Conteúdo da página {page_number_to_print}:\n")
print(page)