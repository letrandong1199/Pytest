import math
#Wp1

def hello(text):
    text = text.strip()
    result='Hello '+text+'!'
    return result

#wp2

def calculate_hypotenuse(a,b):
    result=math.sqrt(a**2+b**2)
    return result

#wp3

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

#wp4

def is_a_condition_true(list):
    if list == [] :
        result=None
    else:
        result=False
        for i in list:
            if i==True:
                result=True
    return result

#wp5

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

#wp6

def find_cheapest_hotels(hotel_daily_rate,maximum_daily_rate):
    if hotel_daily_rate==[]:
        result_hotel=[]
    else:
        result_hotel = []
        for i in hotel_daily_rate:
            if i[1]<=maximum_daily_rate:
                result_hotel.append(i)
    result_hotel=sorted(result_hotel,key=lambda hotel: hotel[1])
    new_hotel = []
    for i in result_hotel:
        new_hotel.append(i[0])
    return new_hotel

#wp7

def calculate_euclidean_distance_between_2_points(point_1,point_2):
    result=math.sqrt((point_2[0]-point_1[0])**2+(point_2[1]-point_1[1])**2)
    return result

#wp8

def calculate_euclidean_distance_between_points(list_point):
    result=0
    # i = 0
    # while i<len(list_point)-1:
    #     result+=calculate_euclidean_distance_between_2_point(list_point[i],list_point[i+1])
    #     i+=1
    # return result
    for i in range(len(list_point)-1):
        result+=calculate_euclidean_distance_between_2_points(list_point[i],list_point[i+1])
    return result

#wp9

def capitalize_words(str):
    str=str.strip()
    while (str.find('  ')!=-1):
        str=str.replace('  ',' ')
    str=str.title()
    return str

#wp10

def uppercase_lowercase_words(str):
    str=capitalize_words(str)
    str=str.split(' ')
    for i in range(0,len(str)):
        if i%2!=0:
            str[i]=str[i].lower()
        else:
            str[i]=str[i].upper()
    str = ' '.join(str)
    return str

#wp11

def factorial(n):
    if type(n)!=int:
        return None
    if n==0 and n==1:
        return 1
    else:
        tmp=1
        for i in range(1,n+1):
            tmp*=i
    return tmp

#wp12

def char_to_int(ch):
    if len(ch)!=1:
        return False
    else:
        if ord(ch)<48 and ord(ch)>57:
            return False
    return ord(ch)-48

#wp13
def string_to_int(str):
    result=0
    for i in range(len(str)):
        result+=char_to_int(str[i])*10**(len(str)-i-1)
    return result

#wp14


