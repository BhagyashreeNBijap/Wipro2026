from models.rating_model import ratings

def create_rating(data):
    data["id"]=len(ratings)+1
    ratings.append(data)
    return data

