from os import path

'''width and height'''
WIDTH = 1000
HEIGHT = 700

'''environment data'''
FPS = 30
ceiling = 600
finish_line = 15000

'''color'''
BLACK = "#000000"
WHITE = "#ffffff"
RED = "#ff0000"
YELLOW = "#ffff00"
GREEN = "#00ff00"
GREY = "#8c8c8c"
BLUE = "#0000ff"
LIGHT_BLUE = "##21A1F1"

'''object size'''
car_size = (60, 30)
coin_size = (30,30)
lane_size = (20,3)

'''command'''
LEFT_cmd = "MOVE_LEFT"
RIGHT_cmd = "MOVE_RIGHT"
SPEED_cmd = "SPEED"
BRAKE_cmd = "BRAKE"

'''data path'''
ASSET_IMAGE_DIR = path.join(path.dirname(__file__), "../asset/image")
IMAGE_DIR = path.join(path.dirname(__file__), 'image')
SOUND_DIR = path.join(path.dirname(__file__), 'sound')
BACKGROUND_IMAGE = ["ground0.jpg"]
COIN_IMAGE = "coin.png"
RANKING_IMAGE = ["info_coin.png", "info_km.png"]

START_LINE_IMAGE = ["start.png", "finish.png"]
# FINISH_LINE_IMAGE =
USER_IMAGE = [["car-1.png","car1-bad.png"],["car-2.png","car2-bad.png"],
              ["car-3.png","car3-bad.png"], ["car-4.png","car4-bad.png"]]
COMPUTER_CAR_IMAGE = ["car-5.png","computer_die.png"]
USER_COLOR = [WHITE, YELLOW, BLUE, RED]

'''image url'''
COMPUTER_CAR_URL = "https://raw.githubusercontent.com/yen900611/RacingCar/master/asset/image/car-5.png"
USER_CAR_URL = ["https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/image/car-1.png",
                "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/image/car-2.png",
                "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/image/car-3.png",
                "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/image/car-4.png"]
BACKGROUND_URL = "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/image/ground0.jpg"
INFO_COIN_URL = "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/image/info_coin.png"
INFO_KM_URL = "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/image/info_km.png"
FINISH_URL = "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/image/finish.png"
START_URL = "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/image/start.png"
COIN_URL = "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/image/coin.png"

computerCar_init_position = [
    (650, 110), (650, 160), (650, 210), (650, 260), (650, 310), (650, 360), (650, 410), (650, 460), (650, 510),
    (-700, 110), (-700, 160), (-700, 210), (-700, 260), (-700, 310), (-700, 360), (-700, 410), (-700, 460), (-700, 510)
]
# computerCar_init_position = [
#     (650, 110), (650, 160), (650, 210), (650, 260), (650, 310), (650, 360), (650, 410), (650, 460), (650, 510),
#     (-700, 110), (-700, 160), (-700, 210), (-700, 260), (-700, 310), (-700, 360), (-700, 410), (-700, 460), (-700, 510)
# ]

userCar_init_position = [160, 260, 360, 460]
