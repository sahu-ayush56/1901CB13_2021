def get_memory_score(input_nums):
    damaged_list = []
    flag = True
    for x in input_nums :
        ifdig = isinstance(x,int)
        if ifdig == False :
            flag = False
            damaged_list.append(x)
    
    if flag == False :
        return damaged_list
    else :
        five_list = []
        Score = 0
        for x in input_nums :
            if x in five_list :
                Score += 1
            else :
                if len(five_list) == 5 :
                    five_list.pop(0)
                    five_list.append(x)
                else :
                    five_list.append(x)
    return Score

input_nums = [3, 4, 5, 3, 2, 1]

ans = get_memory_score(input_nums)
x = isinstance(ans,int);
if x :
    print('Score:', ans)
else :
    print('Please enter a valid input list, Invalid inputs detected : ',ans)
