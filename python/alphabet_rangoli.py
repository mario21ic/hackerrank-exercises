def print_rangoli(size):
    # your code goes here
    if size==1:
        print("a")
        return
    first_letter = 97
    last_letter = 122
    x = 0
    letters1 = []
    for n in range(size):
        letters1.append(chr(first_letter + x))
        x += 1
    #letters2 = letters1.copy()
    letters2 = letters1
    letters1.reverse()
    #print(letters1)
    #print(letters2)
    
    width = (size*4)-3
    #height = (size*2)-1
    height = size*2
    height_middle = height//2
    padding_left = (width//2)+1
    padding_right = (width//2)-1
    x = 1
    y = 0
    middle = False
    for l in range(1, height):
        #print(l)
        central_left = '-'.join(letters1[:x])
        letters3 = letters2[:y]
        letters3.reverse()
        central_right = '-'.join(letters3)
        print(central_left.rjust(padding_left, '-') + "-" + central_right.ljust(padding_right, '-'))
        
        if (x >= height_middle) or middle:
            #print("llegamos a la mitad")
            middle = True
            x-=1
            y-=1
            #print(central_left.rjust(padding_left, '-') + "-" + central_right.ljust(padding_right, '-'))
        else:
            #print(central_left.rjust(padding_left, '-') + "-" + central_right.ljust(padding_right, '-'))
            x+=1
            y+=1
    
    return

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
