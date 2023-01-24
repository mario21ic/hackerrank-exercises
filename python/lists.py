"""
input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

expected:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
import sys

if __name__ == '__main__':
    N = int(input())
    # print(N) # 12
    # get all inputs
    cmds = []
    # try:
    x=0
    while x<N:
        c = input()
        if not c:
            break
        cmds.append(c)
        x+=1
    # except EOFError as er:
        # print("err:", er)
    
    # print("cmds: ", cmds)

    l = []
    for c in cmds:
        c = c.split(" ")
        cmd = c[0]
        if cmd=="insert":
            l.insert(int(c[1]), int(c[2]))
        if cmd=="print":
            print(l)
        if cmd=="remove":
            l.remove(int(c[1]))
        if cmd=="append":
            l.append(int(c[1]))
        if cmd=="sort":
            l.sort()
        if cmd=="pop":
            l.pop()
        if cmd=="reverse":
            l.reverse()
    # l.append()
    

