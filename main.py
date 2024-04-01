# Built-in imports
import math

# Your code below
GRADE = {}
for score in range(101):
    grade = ''
    if 100 >= score >= 70:
        grade = 'A'
    elif 70 > score >= 60:
        grade = 'B'
    elif 60 > score >= 55:
        grade = 'C'
    elif 55 > score >= 50:
        grade = 'D'
    elif 50 > score >= 45:
        grade = 'E'
    elif 45 > score >= 40:
        grade = 'S'
    elif 40 > score >= 0:
        grade = 'U'
    GRADE[score] = grade

overall = 0
student_data = []
def read_testscores(filename):
    """
    Parameter
    ---------
    filename : str
        a string of the name of a csv file

    Return
    ------
    a list of dictionaries
    """
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            line = line.strip().split(',')
            class_ = line[0]
            name_ = line[1]
            p1 = int(line[2])
            p2 = int(line[3])
            p3 = int(line[4])
            p4 = int(line[5])
            overall = (p1/30 * 15) + (p2/40 * 30) + (p3/80 * 35) + (p4/30 * 20)
            overall = math.ceil(overall)
            grade = GRADE[overall]
            student_data.append({'class' : class_, 'name' : name_, 'overall' : overall, 'grade' : grade})
        return student_data


def analyze_grades(studentdata):
    """
    Parameter
    ---------
    studentdata : variable

    Return
    ------
    dictionaries inside a dictionary
    """
    analysis = {}
    for lin_ in student_data:
        class_s = lin_['class']
        grade_s = lin_['grade']
        if class_s not in analysis:
            analysis[class_s] = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'S':0, 'U':0}
        analysis[class_s][grade_s] += 1
    return analysis
    
        
    


