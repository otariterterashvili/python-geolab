import random
from resource import RELATIVE_NAME


file_name = "/Users/otarterterashvili/Desktop/geolab.txt"

number = int(input("How many random numbers ?"))

with open(RELATIVE_NAME, "w") as file_object:

  for i in range(number):
    rand_number = str(random.randint(10, 1000))
    file_object.writelines(f"Random number {i+1}: {rand_number}\n")

  file_object.close()

