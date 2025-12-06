try:
    n = int(input())
    s = input().split()
    a = []
    for x in s:
        a.append(int(x))

    max_count = 0 
    for i in range(n):
        count = 0
        for j in range(n):
            if a[i] == a[j]:
        if count > max_count:
        