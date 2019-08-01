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
hotels= [
    ('Majestic Saigon Hotel', 93),
    ('Hotel Grand Saigon', 80),
    ('Sofitel Saigon Plaza', 123),
    ('Hotel Continental', 62),
    ('Caravelle Hotel', 180),
    ('Sheraton Saigon Hotel', 216),
    ('Park Hyatt Saigon', 209)
]
print(find_cheapest_hotels(hotels,80))


