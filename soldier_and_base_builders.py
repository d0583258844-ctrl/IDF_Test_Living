class Soldier:
    def __init__(self, num_id: int, first_name: str, last_name: str, gender: str, city: str, distance: int, status: str = "not placed"):
        self.num_id = num_id 
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender 
        self.city = city
        self.distance = distance
        self.status = status



class Room:
    def __init__(self):
        self.soldiers = []

    def add_soldier(self, soldiers:list[dict]):
        while len(soldiers) != 8:
            for row in soldiers:
                if row["status"] != "placed":
                    soldiers.append(Soldier(row["soder_nomber"],row["first_name"],row["last_name"],row["gender"],row["city"],row["distance"], row["status"]))
        return soldiers
    
class HomeBuilder:
    def __init__(self, rooms):
        self.rooms = list[Room]
        

class BaseBulder(HomeBuilder):
    def __init__(self):
        super().__init__()



