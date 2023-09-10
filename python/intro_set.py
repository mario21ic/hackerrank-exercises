def average(array):
    # your code goes here
    miset = set()
    for x in array:
        miset.add(x)
    return sum(miset)/len(miset)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
