def buildPWArray(listEntries):
    passwords = []

    # password index index: 0 => min, 1 => max, 2 => letter, 3 => pw
    for entry in listEntries:
        values = entry.split(':') # 0 => min,max,letter 1 => pw
        minMax = values[0].split('-') # 0 => min 1 => max,letter
        maxLetter = minMax[1].split(' ') # 0 => max 1 => letter

        pw = values[1]
        min = minMax[0]
        max = maxLetter[0]
        letter = maxLetter[1]

        passwordEntry = []
        passwordEntry.append(min)
        passwordEntry.append(max)
        passwordEntry.append(letter)
        passwordEntry.append(pw.rstrip()[1:])
        #6-12 p
        passwords.append(passwordEntry)
    return passwords

def buildRegEx(min, max, letter):
    

validPasswords = 0

listEntries = open("input.txt")
passwords = buildPWArray(listEntries) # [[min,max,letter,pw],[min,max,letter,pw], ..]

for password in passwords:
    print(password)
