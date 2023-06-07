flag = " "
tmp = " "

with open("/Users/anauroranon/Desktop/aiuto.txt", "r") as input:
    for line in input:
        if '(opcode' in line:

            for i in range(36,42):
                tmp = tmp + line[i]
            flag = flag + chr(int(tmp, base=16))
            tmp = " "
            
print(flag)



