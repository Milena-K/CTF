def recursion(answer, x, y):
    if(x == 525):
        return answer
    x += 1
    y += 1
    ans = x * y + answer + 3
    print((ans,x))
    recursion(ans, x, y)

recursion(1,0,0)
