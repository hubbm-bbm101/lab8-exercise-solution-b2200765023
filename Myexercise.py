import sys

student_info =[]

f = open(sys.argv[1],"r",encoding = "utf-8")

for line in f:
    name = line.split(":")[0]
    student_info[name] = (line.split(":")[1]).split(",")

try:
    for item in sys.argv[2].split(","):
        university = student_info[item][0]
        depatment = student_info[item][1]
        print("Name: " + str(item) + "\nUniversity: " + str(unıversity) + "\nDepartment: " +str(depatment))
except KeyError:
    print("\nNo record of '{}' was found!".format(item))
except IndexError:
    print("\nCouldn't find {}'s university and/or department!".format(item))