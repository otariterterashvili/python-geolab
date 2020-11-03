from resource import RELATIVE_NAME

with open(RELATIVE_NAME, "r") as file_object:
  for line in file_object:
    print(line.rstrip())
