#TODO получить из системных настроек масштаб разрешения дисплея(resolution<list>, value<%>),
# выставить size=[resolution[0]*100/value,resolution[1]*100/value]
SIZE = (1536,864) #value=125% resolution=[1920,1080]
size_smal_card = (70, 100)
size_board_cell = (100, 150)

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 200, 200)

move_direction = [26, 82, 22, 81, 4, 80, 7, 79] #event.scancode w, up, s, down, a, left, d, right
directions = ["up", "down", "left", "right", "stop"]
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
STOP = "stop"