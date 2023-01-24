if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    l_arr = list(arr)
    l_arr.sort()
    # l_new=[]
    # prev=None
    # for i in l_arr: # limpiar duplicados
    #     if i==prev:
    #         continue
    #     prev = i
    #     l_new.append(i)
    # print(l_new[len(l_new)-2]) # buscar al penultimo
    print(l_arr[l_arr.index(max(l_arr)) - 1]) # forma optimizada

