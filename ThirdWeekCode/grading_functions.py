# assignment3 functions
#   Function to calculate the average of a list
#   a. the function called average() that has one argument, a list of numbers
#   b. Inside the function, it uses the built-in Python functions sum() and len() to calculate the averages

def average(grade):
    return sum(grade)/len(grade)
# example
#homework_steve = [90,97,75,92]
#print(average(homework_steve))

#   Function to calculate the weighted average score for a student
#   a. the function called get_weighted_average() takes one argument: student
#   b. using the average() function to calculate the average of the student's homework, quizzes, and test scores
#   d. Returns the weighted average score for each student (homework is 10%, quizzes are 30%, and tests are 60%  of the grade).

def get_weighted_average(score):
    return (average (score['homework'])*.1)+(average(score['quizzes'])*.3)+(average(score['tests'])*.6)

#   Function to convert a grade into a letter grade
#   a. the function called get_letter_grade() has one argument called score (a number)
#   b. the function uses if / elif /else to return the following letter grades:
#       - 90 or above: “A"
#       - 80 or above: “B"
#       - 70 or above: “C"
#       - 60 or above: “D"
#       - Below 60: “F"
#   
def get_letter_grade(score):
    if score >= 90:
        letter_grade = "A"
    elif score >= 80:
        letter_grade = "B"
    elif score >= 70:
        letter_grade = "C"
    elif score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade

#   Function to calculate the class average
#   a. The function called get_class_average() has one argument, students (a list of dictionaries)
#   b. Inside the function,  a temporary empty list called results is created to store each student's grade
#   c. Loops over the list of students, appending each student's grade into the results list
#   d. Finally, returns the average of the results

def get_class_average(students):
    temp_list =[]
    for student in students:
        temp_list.append(get_weighted_average(student))
    return average(temp_list)
