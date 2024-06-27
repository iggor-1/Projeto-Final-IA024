import re

input_txt_path = "IRPF2024.pdf.txt"

parentheses_txt_path = "IRPF2024.pdf_parentheses_filtered.txt"

with open(input_txt_path, "r", encoding="utf-8") as txt_file:
    content = txt_file.read()

pattern = r'\((.*?)\)'
all_parentheses_texts = re.findall(pattern, content, re.DOTALL)

keywords = ["Lei", "Regulamento", "Decreto", "Instrução", "Parecer"]
filtered_texts = [text for text in all_parentheses_texts if any(keyword in text for keyword in keywords)]

with open(parentheses_txt_path, "w", encoding="utf-8") as parentheses_file:
    for text in filtered_texts:
        parentheses_file.write(text.strip())
        parentheses_file.write("\n")

print(f"O texto dentro de parênteses contendo palavras específicas foi salvo em: {parentheses_txt_path}")
