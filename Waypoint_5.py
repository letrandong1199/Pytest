def filter_integers_greater_than(list,n):
    if list==[]:
        result=None
    else:
        result=[]
        for i in list:
            if i>n:
                result.append(i)
        if len(result)==0:
            result=None
    return result
l=([0,3,5,-2,9,8])
filter_integers_greater_than(l,4)