from models.user_model import users

def create_user(data):
    data["id"]=len(users)+1
    users.append(data)
    return data

