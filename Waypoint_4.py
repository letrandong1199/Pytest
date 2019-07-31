def is_a_conditions_true(list):
    if list == [] :
        result=None
    else:
        result=False
        for i in list:
            if i==True:
                result=True
    return print(result)
is_a_conditions_true([True,True])
 
