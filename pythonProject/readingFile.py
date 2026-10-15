# Python reading files (.txt, .json, .csv)

file_path = "stuff/test.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)