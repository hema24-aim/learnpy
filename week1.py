import json
#file handling
FILE = "students.json"
def load_students():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []
def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent = 4)
#CRUD operations
def add_student(students):
    name = input("Enter name: ")
    marks = list(map(int, input("Enter marks: ").split()))
    students.append({"name": name, "marks": marks})
    print("Student added!")
def view_students(students):
    for s in students:
        avg = sum(s["marks"]) / len(s["marks"])
        print(f"{s['name']} → Avg: {avg:.2f}")
def update_student(students):
    name = input("Enter name to update: ")
    for s in students:
        if s["name"] == name:
            s["marks"] = list(map(int, input("Enter new marks: ").split()))
            print("Updated!")
            return
    print("Student not found!")
def delete_student(students):
    name = input("Enter name to delete: ")
    for s in students:
        if s["name"] == name:
            students.remove(s)
            print("Deleted!")
            return
    print("Student not found!")
#slicing
def show_top_two(students):
    print("Top 2 students:")
    sorted_list = sorted(students, key=lambda x: sum(x["marks"]), reverse=True)
    for s in sorted_list[:2]:
        print(s["name"])   
#sorting
def sort_students(students):
    students.sort(key=lambda x: sum(x["marks"]), reverse=True)
    print("Students sorted by marks!")
#set operations
def unique_marks(students):
    all_marks = []
    for s in students:
        all_marks.extend(s["marks"])

    unique = set(all_marks)
    print("Unique marks:", unique)
#dict comprehension
def average_dict(students):
    avg_dict = {
        s["name"]: sum(s["marks"]) / len(s["marks"])
        for s in students
    }
    print("Average dictionary:", avg_dict)   
#main
def main():
    students = load_students()

    while True:
        print("\n1.Add 2.View 3.Update 4.Delete")
        print("5.Sort 6.Top2 7.UniqueMarks 8.AvgDict 9.Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            update_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            sort_students(students)

        elif choice == "6":
            show_top_two(students)

        elif choice == "7":
            unique_marks(students)

        elif choice == "8":
            average_dict(students)

        elif choice == "9":
            save_students(students)
            print("Saved! Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()     