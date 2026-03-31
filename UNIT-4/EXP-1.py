def write_file(filename, content): 
    with open(filename, 'w') as file: 
        file.write(content) 
        print("Data written to file successfully.") 
 
def read_file(filename): 
    try: 
        with open(filename, 'r') as file: 
            content = file.read() 
            print("File Content:") 
            print(content) 
    except FileNotFoundError: 
        print("File not found.") 
 
def append_file(filename, content): 
    with open(filename, 'a') as file: 
        file.write(content) 
        print("Data appended to file successfully.") 
 
def main(): 
    filename = "sample.txt" 
     
    # Writing to file 
    write_file(filename, "Hello, this is the first line.\n") 
     
    # Reading the file 
    read_file(filename) 
     
    # Appending to file 
    append_file(filename, "This is an appended line.\n") 
     
    # Reading after appending 
    read_file(filename) 
 
if __name__ == "__main__": 
    main() 
