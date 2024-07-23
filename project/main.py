import datetime

# Define the student data
student_names = ["Amol", "Naina", "Chirag", "Deepa", "Eshaan", "Falguni", "Gaurav", "Heena", "Ishan", "Jaya"]
student_classes = ["10th Grade", "10th Grade", "10th Grade", "10th Grade", "10th Grade", "10th Grade", "10th Grade", "10th Grade", "10th Grade", "10th Grade"]
college_name = "ABC College of Engineering"
college_address = "123 College Road, Mumbai, Maharashtra, India"

math_marks = [85, 92, 78, 74, 88, 90, 67, 76, 83, 80]
science_marks = [89, 95, 82, 77, 91, 93, 72, 79, 85, 82]
english_marks = [90, 88, 85, 80, 87, 92, 75, 78, 84, 86]
history_marks = [88, 90, 84, 76, 89, 91, 70, 77, 81, 85]
geography_marks = [87, 89, 83, 75, 90, 92, 69, 78, 82, 84]

# Function to calculate total marks, percentage, and SGPA
def calculate_results(index):
    total = math_marks[index] + science_marks[index] + english_marks[index] + history_marks[index] + geography_marks[index]
    percentage = total / 5
    sgpa = percentage / 10  # Simple conversion for SGPA
    return total, percentage, sgpa

# Function to display the marksheet for a student
def display_marksheet(index):
    if 0 <= index < len(student_names):
        total, percentage, sgpa = calculate_results(index)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        print("\n" + "="*50)
        print(f"Marksheet for {student_names[index]}")
        print("="*50)
        print(f"College: {college_name}")
        print(f"Address: {college_address}")
        print(f"Class: {student_classes[index]}")
        print(f"Date: {current_date}")
        print("="*50)
        print(f"Math:       {math_marks[index]}")
        print(f"Science:    {science_marks[index]}")
        print(f"English:    {english_marks[index]}")
        print(f"History:    {history_marks[index]}")
        print(f"Geography:  {geography_marks[index]}")
        print("="*50)
        print(f"Total Marks:    {total}")
        print(f"Percentage:     {percentage:.2f}%")
        print(f"SGPA:           {sgpa:.2f}")
        print("="*50)
    else:
        print("Invalid index. Please enter a number between 0 and 9.")

def main():
    while True:
        print("\nStudent Marksheet System")
        print("1. Display Marksheet")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            index = int(input("Enter student index (0-9): "))
            display_marksheet(index)
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()