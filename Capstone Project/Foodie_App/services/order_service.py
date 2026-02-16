from models.order_model import orders

def create_order(data):
    data["id"]=len(orders)+1
    orders.append(data)
    return data

