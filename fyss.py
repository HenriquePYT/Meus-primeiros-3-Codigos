print("FYSS ( Final Score of the Year from the State Schools)")
name = input("Before you start the system please, identify yourself with your name")
print(f"Person Identified, Welcome {name}!")
student_name = input("Insert the Student´s Name: ")
score_text = input("Now please, Insert the Final Score of the Student during the whole year:")
score_text = score_text.replace(",", ".")
student_score = float(score_text)
if student_score > 10 or 0 > student_score:
    print("Oh! It seems that it was a identified a mistake by the FYSS System, please check the final score of the student with the coordenation from your school!")
elif 10 >= student_score and  student_score >= 9:
     print("Congratulations, you passed to the next year!")
elif 8 >= student_score and  student_score >= 7:
     print("Congratulations, you passed to the next year!")
elif 7 >= student_score and  student_score >= 6:
    print("Congratulations, you passed to the next year!")    
elif student_score < 6:
     print("Oh! It seems that you didn´t pass to the next year :( In case of wrong final score please enter in contact with the Principal or the Orientation from your School")
summary_answer = input("Do you want to check the student´s summary?").strip().lower()
positive_answers = ["yes", "sure", "yep", "alright!", "alright", "why not?"]
if summary_answer.strip().lower() in positive_answers:
    print("-----SUMMARY-----")
    print(f"{student_name}")
    print(f"{student_score}")
else:
    print(f"Okay, thank you for use the FYSS System, Have a Nice day {name}!")
