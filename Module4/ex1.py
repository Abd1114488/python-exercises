length = float(input("Enter the length of a zander in cm: "))
diff_length = 42 - length
if length < 42:
    print("Release the fish back into the lake.")
    print(f"The fish was {diff_length} cm below the size limit")
else:
    print("The zander meets the size limit.")