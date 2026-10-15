# Python writing files (.txt, .json, .csv)

txt_data = "I like burger!"

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")
