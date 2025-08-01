total = 0
FirstName = input("Enter your First Name: ")
LastName  = input("Enter your last Name: ")
Division = input("Enter your Class: ")



Maths = int(input("Enter Marks of Hindi: "))
Science = int(input("Enter Marks of Science: "))
English = int(input("Enter Marks of English: "))
Hindi = int(input("Enter Marks of Hindi: ")) 


Marks = [Maths,Science,English,Hindi]

total = Maths+Science+English+Hindi


if total < 0 or total > 400:
    print("Please enter Marks from 0 to 100")
else:
    percentage = total / 4
    print("Helloo..")
    print(FirstName.upper() +  LastName.upper())
    print(f"Your class is {Division}")
    print(f"Your Marks is {Marks}")
    print(f"Your Total Marks is {total}")
    print(f"Your percentage is {percentage}")

    if percentage >= 80 and percentage < 100:
        print("Distinction")
    elif percentage >=70 and percentage <79:
        print("First Class")
    elif percentage >= 60 and percentage < 69:
        print("Second Class")
    elif(percentage <=39):
        print("Try Agian...")    



