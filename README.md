# pdf_highlight_extractor

Extracts highlights from PDF documents as a summary

Access the tool at <https://aravindgopala.github.io/pdf_highlight_extractor/>

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/aravinddatla)

## ✨ Why this exists

Extracting highlights from PDFs is surprisingly difficult without paid software or privacy-compromising online converters. This tool solves that by:

- **100% Privacy:** All processing happens in your browser. No files are uploaded to a server.
- **Zero Cost:** MIT Licensed and open-source.
- **Note-Taking Ready:** Export highlights directly to Markdown for apps like Obsidian, Notion, or Roam Research.

## 🚀 How to Use

1. Visit the live tool: **<https://aravindgopala.github.io/pdf_highlight_extractor>**
2. Drag and drop your PDF into the upload zone.
3. Review your highlights on the screen.
4. Click **Download .MD** or **Download .TXT** to save your notes.

## 🛠 Technical Details

- Built with **HTML5/CSS3** and **Vanilla JavaScript**.
- Powered by **PDF.js** (Mozilla) for high-performance PDF parsing.
- Handles common PDF "hiccups" like broken line breaks and coordinate mapping.

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The pdf can be highlighted using any of the popular tools like Adobe Acrobat, Foxit reader etc

The summary is saved in the same directory as the pdf file named as `<filename>_summary.txt`

## If you want to run the tool locally, below are the steps

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
