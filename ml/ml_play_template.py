import random


class MLPlay:
    def __init__(self,ai_name:str,*args,**kwargs):
        self.other_cars_position = []
        self.coins_pos = []
        self.ai_name = ai_name
        self.speed = random.randint(9,11)*10
        print("Initial ml script")
        print(ai_name)
        print(kwargs)

    def update(self, scene_info: dict,*args,**kwargs):
        """
        Generate the command according to the received scene information
        """
        # print(scene_info)
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if random.randint(1,100)<self.speed:
            return ["SPEED"]
        else:
            return []

    def reset(self):
        """
        Reset the status
        """
        self.speed = random.randint(7,11)*10

        # print("reset ml script")
        pass
