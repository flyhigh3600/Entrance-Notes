import base64

def ttf_to_base64(ttf_file):
    try:
        with open(ttf_file, 'rb') as f:
            ttf_data = f.read()
            base64_data = base64.b64encode(ttf_data)
            return base64_data.decode('utf-8')
    except FileNotFoundError:
        print(f"Error: File '{ttf_file}' not found.")
        return None

def main():
    ttf_file = input("Enter the path to the TrueType Font (.ttf) file: ")
    base64_data = ttf_to_base64(ttf_file)
    if base64_data:
        print("data recorded")
        open("gg.g","w").write(base64_data)

if __name__ == "__main__":
    main()
