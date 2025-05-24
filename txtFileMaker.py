import os

def create_txt_files(start, end, directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for i in range(start, end + 1):
        filename = os.path.join(directory, f"{i}.txt")
        open(filename, 'w').close()
        print(f"Created: {filename}")

if __name__ == "__main__":
    try:
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))

        if start > end:
            print("Invalid range. Start should be less than or equal to end.")
        else:
            folder = r"C:\Users\user\Desktop\Sinhala Data Set\Facebook Articles"
            create_txt_files(start, end, folder)

    except ValueError:
        print("Please enter valid integers for the range.")
