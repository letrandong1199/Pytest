def are_all_conditions_true(list):
    if list == [] :
        result=None
    else:
        result=True
        for i in list:
            if i!=True:
                result=False
    return print(result)
are_all_conditions_true([])
