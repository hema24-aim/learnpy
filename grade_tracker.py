students = [{"name": "hema", "marks": [95,78,89]},
            {"name": "pavana", "marks": [97,79,88]}]  #storing the data
def add_student(name, marks):              #build functions
    return {"name": name, "marks": marks}
def calculate_avg(marks):
    return sum(marks) / len(marks)
def get_grade(avg):
    if avg >= 92:
        return "A"
    elif avg > 65:
        return "B"
    else:
        return "C"
def display_students(students):
    for student in students:
        avg = calculate_avg(student["marks"])
        grade = get_grade(avg)
        print(f"{student['name']} → Avg: {avg:.2f}, Grade: {grade}")
def main():
    students = []
    students.append(add_student("hema",[95,78,89]))
    students.append(add_student("pavana",[97,79,88]))
    display_students(students)
main()
    
    
    