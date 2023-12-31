
# File: Project1.py
# Student: Caroline Snell
# UT EID: crs4775
# Course Name: CS303E
# 
# Date: October 10th
# Description of Program: This is a program I created tom determine someone's grade at a particular point in time based on homework, project, and exam grades. 

def computeHomeworkAvg(): 
    print("HOMEWORKS:")
    hw1=0
    hw2=0
    hw3=0
    while True:
        hw1=int(input("  Enter HW1 grade: "))
        if (hw1 > 10 or hw1<0):
            print("  Grade must be in range [0..10]. Try again.")
        else:
            break
    while True:
        hw2=int(input("  Enter HW2 grade: "))
        if (hw2 > 10 or hw2<0):
            print("  Grade must be in range [0..10]. Try again.")
        else:
            break
    while True:
        hw3=int(input("  Enter HW3 grade: "))
        if (hw3 > 10 or hw3<0):
            print("  Grade must be in range [0..10]. Try again.")
        else:
            break
    return( (hw1+hw2+hw3)/3 )

def computeProjectAvg():
    print("PROJECTS")
    pr1=0
    pr2=0
    while True:
        pr1=int(input("  Enter Pr1 grade: "))
        if (pr1 > 100 or pr1<0):
            print("  Grade must be in range [0..100]. Try again.")
        else:
            break
    while True:
        pr2=int(input("  Enter Pr2 grade: "))
        if (pr2 > 100 or pr2<0):
            print("  Grade must be in range [0..100]. Try again.")
        else:
            break
    return( (pr1+pr2)/2 )
  
def computeExamAvg():
    print("EXAMS")
    ex1=0
    ex2=0
    while True:
        ex1=int(input("  Enter Ex1 grade: "))
        if (ex1 > 100 or ex1<0):
            print("  Grade must be in range [0..100]. Try again.")
        else:
            break
    while True:
        ex2=int(input("  Enter Ex2 grade: "))
        if (ex2 > 100 or ex2<0):
            print("  Grade must be in range [0..100]. Try again.")
        else:
            break
        
    return( (ex1+ex2)/2 )



def main():
    studentsname=input("Enter the student's name (or 'stop'): ")
    if (studentsname== 'stop'):
        print("Thanks for using the grade calculator! Goodbye.")
    else:
        print()
        hwavg= computeHomeworkAvg()
        print()
        pravg= computeProjectAvg()
        print()
        exavg= computeExamAvg()
        print()
        studentscourseaverage= ((hwavg/10)*0.3  +   (pravg/100)*0.3  +   (exavg/100)*.4)*100
        displayedhwaverage=format( (hwavg/10)*100, ".2f")
        displayedexaverage=format( exavg,".2f")
        displayedprojectaverage=format( pravg, ".2f" )
        displayedcourseaverage=format(studentscourseaverage, ".2f")
        lettergrade=0
        if studentscourseaverage>=90:
            lettergrade="A"
        elif (studentscourseaverage<90 and studentscourseaverage>= 80):
            lettergrade="B"
        elif (studentscourseaverage<80 and studentscourseaverage>= 70):
            lettergrade="C"
        elif(studentscourseaverage<70 and studentscourseaverage>= 60):
            lettergrade="D"
        else:
            lettergrade="F"
        
        
        print("Grade report for: ", studentsname)
        print("  Homework average: (30% of grade): ", displayedhwaverage)
        print("  Project average: (30% of grade): ", displayedprojectaverage)
        print("  Exam average: (40% of grade): ", displayedexaverage)
        print("  Student course average: ", displayedcourseaverage)
        print("  Course grade (CS303E: Fall, 2022): ", lettergrade) 
     
        
main()



