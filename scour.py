from rw_processes import read_file


if __name__ == "__main__":
    abs_path = input("Path to the directory to index: ")
    
    a = read_file(abs_path, encoding="utf-8")
    print("Name: ", a["Filename"])
    print("Content: ", a["Content"])