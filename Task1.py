total=0

for i in range(1,6):
    marks = int(input("Enter the marks"))
    if marks < 0 or marks >100:
        print("Invalid input")
        break
    total += marks
print(total)


# if valid:
percentage = total / 5
print("Total Marks",total)
print(percentage)


if percentage >= 80 and percentage < 100:
        print("Grade A")
elif percentage >=70 and percentage <79:
        print("Grade B")
elif percentage >= 60 and percentage < 69:
        print("Grade C")
elif(percentage <=39):
        print("Fail")
    