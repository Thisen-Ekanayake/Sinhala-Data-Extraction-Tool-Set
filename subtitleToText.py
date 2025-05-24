import re
import os
from tkinter import Tk, filedialog

def is_sinhala(text):
    return bool(re.search(r'[\u0D80-\u0DFF]', text))

def clean_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

def read_file_with_fallback(file_path):
    encodings = ['utf-8', 'utf-16', 'windows-1252']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as file:
                return file.readlines()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Failed to decode file with known encodings: {file_path}")

def extract_sinhala_text_from_srt(file_path):
    lines = read_file_with_fallback(file_path)

    sinhala_lines = []
    for line in lines:
        line = line.strip()
        if re.match(r'^\d+$', line) or re.match(r'^\d{2}:\d{2}:\d{2},\d{3}', line):
            continue
        if is_sinhala(line):
            cleaned = clean_whitespace(line)
            sinhala_lines.append(cleaned)

    return '\n'.join(sinhala_lines)

def save_to_txt(content, original_path):
    base = os.path.splitext(original_path)[0]
    new_path = base + '_sinhala.txt'
    with open(new_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    Tk().withdraw()
    file_paths = filedialog.askopenfilenames(
        title="Select .srt files",
        filetypes=[("SRT files", "*.srt")]
    )

    for path in file_paths:
        try:
            sinhala_text = extract_sinhala_text_from_srt(path)
            if sinhala_text:
                save_to_txt(sinhala_text, path)
                print(f"Saved: {os.path.basename(path)} → UTF-8 .txt")
            else:
                print(f"No Sinhala text found in: {os.path.basename(path)}")
        except Exception as e:
            print(f"Error processing {os.path.basename(path)}: {e}")

if __name__ == "__main__":
    main()
