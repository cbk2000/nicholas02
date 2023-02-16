file_input_location = "../output/DUMMY-REGISTRATION.csv"
file_output_location = "../output/OS_GH_USERNAME.txt"

username = []

with open(file_input_location, 'r') as file:
    file.readline()
    for line in file:
        username.append(line.split(",")[4])

with open(file_output_location, 'w') as output:
    for name in username:
        output.write(name + "\n")
