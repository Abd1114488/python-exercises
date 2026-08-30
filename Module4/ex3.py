gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))
if gender == "female":
    if hemoglobin < 117:
        print("Low hemoglobin value")
    elif hemoglobin <= 155:
        print("Normal hemoglobin value")
    else:
        print("High hemoglobin value")
elif gender == "male":
    if hemoglobin < 134:
        print("Low hemoglobin value")
    elif hemoglobin <= 167:
        print("Normal hemoglobin value")
    else:
        print("High hemoglobin value")
else:
    print("Invalid gender entered")