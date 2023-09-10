def swap_case(s):
    result = []
    for x in s:
        if x.islower():
            result.append(x.upper())
        else:
            result.append(x.lower())
    return "".join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
