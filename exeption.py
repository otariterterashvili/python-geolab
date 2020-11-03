def read_file(filename):
  try:
    with open(filename, "r") as file_object:
      print(10/0)
      return file_object.readlines()
  except FileNotFoundError:
    return "File not found error"
    # print("File not found error")


print(read_file("temp.txt"))

print("end of the world")