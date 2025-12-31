#!/usr/bin/env python3
import fitz  # PyMuPDF
import os

# 1. Get input path from user
pdf_path = input("Enter the path to the PDF file: ").strip(
    '"'
)  # Strip quotes in case they drag-and-drop

# 2. Check if the path is valid and open document
if not os.path.exists(pdf_path):
    print(f"Error: The file '{pdf_path}' was not found.")
    exit()

try:
    doc = fitz.open(pdf_path)
except Exception as e:
    print(f"Failed to open PDF: {e}")
    exit()

# Extract Title safely
title = doc.metadata.get("title") or os.path.basename(pdf_path)
highlights = []

# 3. Iterate through each page
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    # Check if page has annotations before iterating
    annots = page.annots()
    if annots:
        for annot in annots:
            # Type 8 is the standard Highlight annotation
            if annot.type[0] == 8:
                # clip=annot.rect ensures we only grab text inside the highlighted box
                text = page.get_text("text", clip=annot.rect)
                highlights.append((page_num + 1, text.strip()))

# 4. Prepare the content for display and saving
output_content = []
header = f"\n**** 📖 Title: {title} 📖 ****\n" + "=" * 30

output_content.append(header)
for page_number, highlight in highlights:
    processed_text = highlight.replace(
        "z\n", "\n• "
    )  # Clean up common OCR/PDF artifacts
    entry = f"\n📝 Page {page_number}\n" + "-" * 20 + f"\n{processed_text}\n"
    output_content.append(entry)

# Print to console
print("\n".join(output_content))

# 5. Save the highlights to a text file
output_file = os.path.splitext(pdf_path)[0] + "_highlights.txt"

try:
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(output_content))
    print(
        f'\n✅ Saved {len(highlights)} highlights successfully to: \n   "{output_file}"'
    )
except IOError as e:
    print(f"Error saving file: {e}")

# Close the PDF file
doc.close()
