# pdf_highlight_extractor

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/aravinddatla)

Extracts highlights from PDF documents as a summary

The pdf can be highlighted using any of the popular tools like Adobe Acrobat, Foxit reader etc

The summary is saved in the same directory as the pdf file named as `<filename>_summary.txt`

## Dependencies

`pip install PyMuPDF`

Make it executable

`chmod +x pdf_highlight_extractor.py`

## How to run

`./pdf_highlight_extractor.py`

## Example Output

```c
Enter the path to the PDF file: c:\documents\example.pdf

==============================

****  Title: The Linux Programming Interface  *****

Extracted Highlights:
==============================

📝 **Page 55**
------------------------------
Portable Operating System Interface)

📝 **Page 66**
------------------------------
Process scheduling:

📝 **Page 66**
------------------------------
Memory management:

*** Saved highlights successfully to: c:\documents\example_summary.txt ***

```
