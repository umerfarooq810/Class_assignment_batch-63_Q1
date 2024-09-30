

# Pattren 1
score = 91  

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"The grade for a score of {score} is: {grade}")



# Pattren 2
score = int(input("Enter the student's score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"The grade for a score of {score} is: {grade}")


# if "google.colab" in str(get_ipython()):
#     !pip install nb-mypy -qqq
# %load_ext nb_mypy