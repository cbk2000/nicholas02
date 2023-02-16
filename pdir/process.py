file_input_location = input().strip()
file_output_location = input().strip()

username = []

print("process.py: reading input file...")
with open(file_input_location.strip('"'), 'r') as file:
    file.readline()
    for line in file:
        username.append(line.split(",")[4])

print("process.py: complete reading input file")
print("process.py: writting output file...")
with open(file_output_location.strip('"'), 'w') as output:
    for name in username:
        output.write(name + "\n")
print("process.py: complete writting output file")
