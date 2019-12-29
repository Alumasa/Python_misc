#This is a grade book for all my students. I am a teacher.
#this a dictionary containing a student's grades.
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}

#student2 dictionary
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}

#student3 dictionary
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Below are functions that are self-explanatory
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

students = [alice, lloyd, tyler]
print(get_class_average(students))

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80 and score <= 89:
    return "B"
  elif score >= 70 and score <= 79:
    return "C"
  elif score >= 60 and score <= 69:
    return "D"
  else:
    return "F"

print(get_letter_grade(get_class_average(students)))