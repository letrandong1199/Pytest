import math
def calculate_euclidean_distance_between_2_point(point_1,point_2):
    result=math.sqrt((point_2[0]-point_1[0])**2+(point_2[1]-point_1[1])**2)
    return result
def calculate_euclidean_distance_between_points(list_point):
    result=0
    # i = 0
    # while i<len(list_point)-1:
    #     result+=calculate_euclidean_distance_between_2_point(list_point[i],list_point[i+1])
    #     i+=1
    # return result
    for i in range(len(list_point)-1):
        result+=calculate_euclidean_distance_between_2_point(list_point[i],list_point[i+1])
    return result
print(calculate_euclidean_distance_between_points([(0,0),(3,4),(-1,-1)]))