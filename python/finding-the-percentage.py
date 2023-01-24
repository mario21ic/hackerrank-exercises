if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Your code here
    # print(n, student_marks, query_name)
    result=0
    x=0
    for k,v in student_marks.items():
        # print(k)
        if query_name==k:
            for s in v:
                result += s
                x+=1
    # print("r", result)
    result = result/x
    print(f'{result:.2f}')

