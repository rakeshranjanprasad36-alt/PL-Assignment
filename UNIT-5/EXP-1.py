def read_file():
  filename = input("Please enter the file name: ")
  try:
    with open(filename, 'r') as file:
        content = file.read()
        print("Contents of the file:")
        print(content)
  except FileNotFoundError:
    print("Error: File not found.")
  except PermissionError:
    print("Error: Access to this file is denied.")
  except Exception as e:
    print(f"Something went wrong: {e}")

if __name__ == "__main__":
 read_file()