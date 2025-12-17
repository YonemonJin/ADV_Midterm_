print("=== STUDENT ENROLLMENT SYSTEM ===")


full_name = input("Enter Full Name: ")
address = input("Enter Address: ")
age = int(input("Insert Age Here: "))

print("\nAvailable Courses: ")
print("1. "BSIT")
print("2. "BSCS")
print("3. "BSEMC")

course_choice = input("Select course (1-3): ")

if course_choice == "1":
 course = "BSIT"

elif course_choice == "2":
 course = "BSCS"

elif course_choice == "3":
 course = "BSEMC"

else:
 course = "Invalid Course, please try again."


#SUBJECT SELECTION

num_subject = int(input("\nEnter number of Subjects: "))
rate_per_subject = 1500
total_payment = num_subject * rate_per_subject

#DISPLAY SUMMARY

print("\n=== ENROLLMENT SUMMARY ===")
print(f"Student Name: {full_name}")
print(f"Address: {address}")
print(f"Age: {age}")
print(f"Course: {course}")
print(f"Number of Subjects: {num_subject}")
print(f"Rate Per Subject: PHP {rate_per_subject}")
print(f"Total Payment PHP {total_payment}")