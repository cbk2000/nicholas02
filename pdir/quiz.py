input_location = input().strip()
output_location = input().strip()

print("quiz.py: reading input file...")
with open(input_location.strip('"'), 'r') as file:    
    print("quiz.py: writting output file...")
    with open(output_location.strip('"'), 'w') as flush:
        header_hash = "# ############# XXXXX"
        header_ZCZC = ""
        ans = ""
        for line in file:
            if "ZCZC" in line:
                header_ZCZC = line
            else:
                if line.strip() == "":
                    continue
                if line.strip() == "T:":
                    ans = "ANSWER: A"
                elif line.strip() == "F:":
                    ans = "ANSWER: B"

                flush.write(f"{header_hash}\n{header_ZCZC}")
                flush.write(file.readline())
                while True:
                    next_read = file.readline().strip()
                    if next_read == "":
                        break
                    flush.write(next_read+"\n")

                flush.write("---\n")
                flush.write("A. true\n")
                flush.write("B. false\n")
                flush.write(f"{ans}\n\n")

print("quiz.py: process completed")
