import os
from tkinter import Tk, filedialog
from docx import Document

def count_words_and_size():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select a DOCX file",
        filetypes=[("Word Documents", "*.docx")]
    )

    if not file_path:
        print("No file selected.")
        return

    # Get file size in MB
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

    doc = Document(file_path)
    total_words = sum(len(p.text.strip().split()) for p in doc.paragraphs)

    print(f"\nFile: {file_path}")
    print(f"Size: {file_size_mb:.2f} MB")
    print(f"Word count: {total_words}")

if __name__ == "__main__":
    count_words_and_size()
