import textwrap

def wrap(string, max_width):
    # print("string", string)
    # print("max_width", max_width)
    
    # x=1
    # line=""
    # result = ""
    # for s in string:
    #     line += s
    #     # print("line:", line)
    #     # print("x:", x)
    #     # print("len:", len(string))
    #     if len(line)==max_width or x==len(string):
    #         # print(line)
    #         result += line + "\n"
    #         line=""
    #     x+=1
    
    w_string = textwrap.TextWrapper(width=max_width)
    s_dedent = textwrap.dedent(text=string)
    result = w_string.fill(text=s_dedent)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
