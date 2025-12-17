def calculate_grade(score):

    if score >= 85:
        return "A"  
    elif score >= 70:
        return "B"  
    elif score >= 55:
        return "C"  
    else:
        return "D"  

scores = [90, 76, 60, 40]  

for s in scores:
    print("Score:", s, "Grade:", calculate_grade(s))  
