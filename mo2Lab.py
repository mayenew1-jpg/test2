# Mahlet Ayenew
# Module2_CaseStudy.py
# This program accepts student names and GPAs and determines
# whether the student qualifies for the Dean's List or Honor Roll.


while True:
    
    # Get student's last name
    last_name = input("Enter student's last name (ZZZ to quit): ")
    # Exit program if user enters ZZZ
    if last_name == "ZZZ":
       print("Program ended.")
       break
     # Get student's first name
     first_name = input("Enter student's first name: ")
    # Get student's GPA
    gpa = float(input("Enter student's GPA: "))
# Display student name
print(f"\nStudent: {first_name} {last_name}")
# Check Dean's List
if gpa >= 3.5:
    # Check Honor Roll
    if gpa >= 3.25:
        print("Congratulations! The student has made the Honor Rol
           print()   
