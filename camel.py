s = input("Верблюжий стиль: ")
sN = ""
for c in s:
    if c.islower():
        sN = sN + c
    else:
        sN = sN + " " + c. lower()

print(sN)