def are_all_conditions_true(list):
    if list==[]:
        result=None
    else:
        result=True
        for i in list:
            if i==False:
                result=False
                break
    return result
are_all_conditions_true([])