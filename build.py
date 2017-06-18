def solution(list_of_nums):
    x = y = 0
    for i in list_of_nums:
        if i%2==0:
            y+=1
        else:
            x+=1
    return {'ODD': x, 'EVEN': y}
