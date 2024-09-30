
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

students_data = [
    {
        'name': 'Umer Farooq',
        'marks': {
            'Math': 85,
            'English': 90,
            'Science': 78
        }
    },
    {
        'name': 'Umer Khalil',
        'marks': {
            'Math': 75,
            'English': 82,
            'Science': 89
        }
    },
    {
        'name': 'Qasim Akram',
        'marks': {
            'Math': 93,
            'English': 87,
            'Science': 85
        }
    },
    {
        'name': 'Muzhar Sab',
        'marks': {
            'Math': 65,
            'English': 70,
            'Science': 60
        }
    },
    {
        'name': 'Rehan Sab',
        'marks': {
            'Math': 88,
            'English': 85,
            'Science': 90
        }
    }
]

def calculate_average():
    total = sum(marks.values())
    count = len(marks)
    return total / count

student_grades = []
for student in students_data:
    name = student['name']
    marks = student['marks']
    subject_grades = {subject: calculate_grade(score) for subject, score in marks.items()} 
    average_marks = calculate_average()
    overall_grade = calculate_grade(average_marks)  
    student_grades.append({'name': name, 'average_marks': average_marks, 'overall_grade': overall_grade, 'subject_grades': subject_grades})


for student in student_grades:
    print(student)

