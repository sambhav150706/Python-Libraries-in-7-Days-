import json
import csv


print("===== DAY 02: JSON & CSV =====")
print("\n--- JSON Section ---")

student_data = {
    "name": "Sambhav",
    "course": "Python Libraries",
    "marks": 95
}

json_string = json.dumps(student_data, indent=4)
print("\nJSON String:")
print(json_string)

with open("student.json", "w") as json_file:
    json.dump(student_data, json_file, indent=4)

print("\nData written to student.json")

with open("student.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("\nData read from student.json:")
print(loaded_data)
print("Student Name:", loaded_data["name"])

print("\n--- CSV Section ---")

with open("students.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Sambhav", 95])
    writer.writerow(["Rahul", 88])
    writer.writerow(["Aman", 91])

print("Data written to students.csv")

print("\nReading CSV File:")
with open("students.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)



print("\n--- Mini Project: Student Record Manager ---")

students = []

n = int(input("How many students do you want to add? "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append({"Name": name, "Marks": marks})

with open("student_records.csv", "w", newline="") as file:
    fieldnames = ["Name", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("Student records saved to student_records.csv")

with open("student_records.json", "w") as json_file:
    json.dump(students, json_file, indent=4)

print("Student records also saved to student_records.json")

print("\nProgram Completed Successfully 🚀")
