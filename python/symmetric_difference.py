# Enter your code here. Read input from STDIN. Print output to STDOUT
set1_size = input()
set1_items = input()
set2_size = input()
set2_items = input()

set1 = set()
for x in set1_items.split(" "):
    set1.add(int(x))
#print("set1", set1)

set2 = set()
for x in set2_items.split(" "):
    set2.add(int(x))
#print("set2", set2)

result1 = set1.difference(set2)
result2 = set2.difference(set1)
result3 = result1.union(result2)
milist = list(result3)
milist.sort()
for n in milist:
    print(n)
