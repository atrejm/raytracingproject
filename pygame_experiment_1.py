import pygame
from pygame import Color

SCREEN_WIDTH, SCREEN_HEIGHT = 360, 360
GRID_SIZE = 8
DEFAULT_BOX_COLOR = Color(100, 100, 100)
boxes = {}

def create_display(height, width):
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    return pygame.display.set_mode((height,width))

def gridify(grid_subdivisions, screen):
    # subdivisions are a factor based on the screen size
    screen_width, screen_heigth = pygame.display.get_window_size()

    x_gridwidth = screen_width/grid_subdivisions
    y_gridwidth = screen_heigth/grid_subdivisions

    for i in range(grid_subdivisions):
        for j in range(grid_subdivisions):
            boxes[(i,j)] = Box(x_gridwidth*i, y_gridwidth*j, x_gridwidth, y_gridwidth, DEFAULT_BOX_COLOR, (i,j))

    return boxes

def main():
     
    screen = create_display(SCREEN_WIDTH, SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    screen.fill(Color(200,200,200))
    boxes = gridify(GRID_SIZE, screen) #all boxes drawn to screen

    for id, box in boxes.items():
        box.draw_self(screen)
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        
        for id, box in boxes.items():
            box.draw_self(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                toggle_box(pygame.mouse.get_pos())
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

def toggle_box(mousepos):
    # math to find which grid coord we're in
    x = int(mousepos[0]/SCREEN_WIDTH * GRID_SIZE)
    y = int(mousepos[1]/SCREEN_HEIGHT * GRID_SIZE)
    print(x,y)

    boxes[(x,y)].toggle_selected()    

    # find box with matching gridid
    return

class Box():
    grid_id = (0,0)
    color_when_selected = Color(40, 40, 40)
    border_color = Color(0,0,0)
    selected = False

    def __init__(self, left, top, width, height, color, id):
        self.rect = pygame.Rect(left, top, width, height)
        self.color_when_unselected = color
        self.color = self.color_when_unselected
        self.grid_id = id

    def draw_self(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, self.border_color, self.rect, width=2)

    def toggle_selected(self):
        self.selected = not self.selected
        
        print(self.color)

        if self.selected:
            self.color = self.color_when_selected
        else:
            self.color = self.color_when_unselected

if __name__ == "__main__":
    main()