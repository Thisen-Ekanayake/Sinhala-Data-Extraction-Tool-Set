import os
from tkinter import Tk, filedialog
from pathlib import Path

def add_txt_extension_to_files():
    # Hide the main Tkinter window
    root = Tk()
    root.withdraw()

    # File picker – allow multiple selections
    file_paths = filedialog.askopenfilenames(
        title="Select files without extensions",
        filetypes=[("All Files", "*.*")]
    )

    if not file_paths:
        print("No files selected.")
        return

    renamed_count = 0
    skipped_count = 0

    for file_path in file_paths:
        path = Path(file_path)

        # Skip if the file already has an extension
        if path.suffix != "":
            print(f"Skipped: {path.name} already has an extension.")
            skipped_count += 1
            continue

        # Add .txt
        new_path = path.with_suffix(".txt")
        os.rename(path, new_path)
        print(f"Renamed: {path.name} -> {new_path.name}")
        renamed_count += 1

    print(f"\nSummary: Renamed {renamed_count} file(s), Skipped {skipped_count} file(s).")

if __name__ == "__main__":
    add_txt_extension_to_files()
