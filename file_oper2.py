with open("empty.txt","w") as emp_file:
    emp_file.write("srit ")
    emp_file.write("is an atonamus ")
with open("empty.txt","a") as emp_file:
    emp_file.write("college")

with open("empty.txt","r") as emp_file:
    line=emp_file.read()
    print(line)