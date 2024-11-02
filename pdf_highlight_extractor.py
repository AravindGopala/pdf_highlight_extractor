#!/usr/bin/env python3

import fitz  # PyMuPDF

# Open the PDF file

# get input path from user
pdf_path = input("Enter the path to the PDF file: ")

# Check if the path is valid
try:
    doc = fitz.open(pdf_path)
except FileNotFoundError:
    print("File not found.")
    exit()

doc = fitz.open(pdf_path)
highlights = []

# Iterate through each page
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    for annot in page.annots():  # Iterate over annotations
        if annot.type[0] == 8:  # Check if annotation is a highlight
            text = page.get_text("text", clip=annot.rect)
            highlights.append((page_num + 1, text.strip()))  # Store page number and text

# Print the extracted highlights with page numbers and title of the book
print("\n" + "=" * 30)
print(f"\n**** 📖 Title: {doc.metadata['title']} 📖 ****")
print("\nExtracted Highlights:\n" + "=" * 30)
for page_number, highlight in highlights:
    print(f"\n📝 **Page {page_number}**")
    print("-" * 30)
    processed_text = highlight.replace('z\n', '\n\u2022 ')
    print(processed_text)
print("\n" + "=" * 30)

# Close the PDF file
doc.close()

# Save the highlights to a text file in the same directory as the PDF, use same print style as print above
output_file = pdf_path.replace(".pdf", "_highlights.txt")
with open(output_file, "w") as file:
    file.write("-" * 30 + " ")
    file.write(f" 📖 Title: {doc.metadata['title']} 📖 ")
    file.write("-" * 30 + "\n")
    for page_number, highlight in highlights:
        file.write(f"\nPage {page_number}\n")
        file.write("-" * 30 + "\n")
        processed_text = highlight.replace('z\n', '\n\u2022 ')
        file.write(processed_text + "\n\n")

print(f"*** Saved highlights successfully to \"{output_file}\" ***")
