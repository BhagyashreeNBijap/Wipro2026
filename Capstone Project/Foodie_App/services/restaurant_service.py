from models.restaurant_model import restaurants

def create_restaurant(data):
    data["id"]=len(restaurants)+1
    data["approved"]=False
    data["disabled"]=False
    restaurants.append(data)
    return data

def get_restaurant(rid):
    return next((r for r in restaurants if r["id"]==rid),None)

def update_restaurant(rid,data):
    restaurant=get_restaurant(rid)
    if restaurant:
        restaurant.update(data)
    return restaurant

