if __name__ == '__main__':
    grades = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades[name] = score
    
    # print("grades", grades)
    # print("grades names sorted", sorted(grades))
    # l_scores = []
    # for s in sorted(grades.values()): # clean duplicates
    #     if s not in l_scores:
    #         l_scores.append(s)
    l_scores = list(dict.fromkeys(sorted(grades.values()))) # clean and remove duplicates
    # print("grades values sorted", l_scores)
    
    score = l_scores[1] # seleccionar el penultimo
    # print("l_score", l_score)
    l_students = []
    for k,v in grades.items():
        # print("k", k)
        # print("v", v)
        if v==score:
            l_students.append(k)
    l_students.sort()
    for s in l_students:
        print(s)

