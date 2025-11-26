class Soldier:
    def __init__(self, num_id: int, first_name: str, last_name: str, gender: str, city: str, distance_from_base_in_KM: int, status: str):
        self.num_id = num_id 
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender 
        self.city = city
        self.distance_from_base_in_KM = distance_from_base_in_KM
        self.status = status



class Room:
    def __init__(self):
        pass


class HomeBulder:
    def __init__(self, rooms):
        self.rooms=list[Room]
        

class BaseBulder(HomeBulder):
    def __init__(self):
        super().__init__()



