from models.dish_model import dishes


def create_dish(data):
    data["id"] = len(dishes) + 1
    data["enabled"] = True
    dishes.append(data)
    return data


def get_dish(did):
    return next((d for d in dishes if d["id"] == did), None)


def update_dish(did, data):
    dish = get_dish(did)
    if dish:
        dish.update(data)
    return dish


def delete_dish(did):
    dish = get_dish(did)
    if dish:
        dishes.remove(dish)
    return dish
