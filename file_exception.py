import os

try:
    
    with open("example.txt", "w") as file:
        file.write("Hello! Welcome to File Handling in Python.\n")
        file.write("This file contains some example text.\n")
    print(" File written successfully.")

    with open("example.txt", "r") as file:
        content = file.read()
        print("\n File Content:\n" + content)

    with open("example.txt","a") as file:
        file.write("How are you??\n")  

    
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")    

   
    with open("/home", "w") as file: 
        file.write("Test")


except FileNotFoundError:
    
    print("Error: The file you are trying to read does not exist.")

except PermissionError:
   
    print("Error: You do not have permission to access this file.")

except Exception as e:
   
    print("An unexpected error occurred:",e)

finally:
   
    print("\n File operation completed.")
