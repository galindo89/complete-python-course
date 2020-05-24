my_file=open("file.txt","r")

file_content=my_file.read()

file_edit=input("Name: ")

file_content.write(file_edit)

print(file_content)