def total(marks):
    return sum(marks)

def average(marks):
    return total(marks) / len(marks)

def highest(marks):
    return max(marks)

def lowest(marks):
    return min(marks)

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

students = []

n = int(input("Enter number of students: "))
sub = int(input("Enter number of subjects: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = []

    for j in range(sub):
        marks.append(float(input(f"Enter mark for subject {j + 1}: ")))

    avg = average(marks)
    students.append({
        "name": name,
        "total": total(marks),
        "average": avg,
        "highest": highest(marks),
        "lowest": lowest(marks),
        "grade": grade(avg)
    })

students.sort(key=lambda x: x["average"], reverse=True)

print(f"{'Name':<10}{'Total':<8}{'Average':<8}{'Highest':<8}{'Lowest':<8}{'Grade':<6}")
for s in students:
    print(f"{s['name']:<10}{s['total']:<8.2f}{s['average']:<8.2f}{s['highest']:<8.2f}{s['lowest']:<8.2f}{s['grade']:<6}")