list_of_nums=[1, 2, 3, 5, 8, 9]
def solution(list_of_nums):
    x = y = 0
    for i in list_of_nums:
        if i%2==0:
            y+=1
        else:
            x+=1
    return {'ODD': x, 'EVEN': y}
solution(list_of_nums)
