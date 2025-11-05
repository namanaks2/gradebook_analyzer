"""

Name: Naman Gupta 
Date: 5 November'25
Ttile: Gradebook Analyzer
Description: A menu-based Python program to input student marks,
             calculate statistics, assign grades, and display results.

"""

def show_welcome():
    print("\n===== Welcome to Gradebook Analyzer =====")
    
while True:
    print("\n1. Enter student data manually\n2. Exit")
    choice = input("Enter your choice: ")

    if choice == "2":
        print("Goodbye!")
        break
    elif choice != "1":
        print("Invalid choice, try again.")
        continue

    n = int(input("\nEnter number of students: "))
    marks = {}
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks[name] = float(input(f"Enter marks for {name}: "))

    scores = list(marks.values())
    avg = sum(scores) / len(scores)

    med = sorted(scores)[len(scores)//2] if len(scores)%2 else \
        (sorted(scores)[len(scores)//2-1] + sorted(scores)[len(scores)//2]) / 2
    
    print(f"\nAverage: {avg:.2f}, Median: {med:.2f}, Max: {max(scores)}, Min: {min(scores)}")

    grades = {}
    for name, m in marks.items():
        if m >= 90: g = "A"
        elif m >= 80: g = "B"
        elif m >= 70: g = "C"
        elif m >= 60: g = "D"
        else: g = "F"

        grades[name] = g

    print("\nGrade Distribution:")

    for grade in sorted(set(grades.values())):
        print(f"{grade}: {list(grades.values()).count(grade)}")

    passed = [n for n, m in marks.items() if m >= 40]
    failed = [n for n, m in marks.items() if m < 40]

    print(f"\nPassed ({len(passed)}): {', '.join(passed)}")
    print(f"Failed ({len(failed)}): {', '.join(failed)}")

    print("\nName\t\tMarks\tGrade")
    print("-" * 30)

    for name, m in marks.items():
        print(f"{name:<12}\t{m:<7}\t{grades[name]}")

    print("\nAnalysis complete!\n")    