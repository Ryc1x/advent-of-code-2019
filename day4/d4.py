def check1(password):
    count = 0
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            count += 1
        if password[i] > password[i+1]:
            return 0
    return 1 if count > 0 else 0

def check2(password):
    count = 0
    valid = False
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            count += 1
        else:
            if count == 1:
                valid = True
            count = 0
        if password[i] > password[i+1]:
            return 0
    if count == 1:
        valid = True
    
    return 1 if valid else 0

# INPUTS: Number in range: 172851-675869
if __name__ == "__main__":
    count = 0
    for i in range(172851,675870):
        count += check2(str(i))
    print(count)