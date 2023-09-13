import pygame
import sys
from tkinter import messagebox, Tk

pygame.init()
display_height = 500
display_width = 500
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Path Finding Game!")
clock = pygame.time.Clock()

rows = 25
col = 25
box_width = display_width // col
box_height = display_height // rows

matrix = []
queue = []
path = []

class boxes:

    def __init__(self,i,j):
        self.x = i# the position of the box w.r.t its coordinates
        self.y = j
        #set the flags for start, obstruction and end
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False
        self.neighbours = []
        self.prior = None

    def draw(self, display, color): # rec= #(x coordinate, y-coordinate(where to start), widht, height)
        pygame.draw.rect(display, color, (self.x*box_width, self.y*box_height,box_width-2, box_height-2))

    def set_neighbours(self):
        if self.x > 0:
            self.neighbours.append(matrix[self.x -1][self.y])
        if self.x < col -1:
            self.neighbours.append(matrix[self.x +1][self.y])

        if self.y > 0:
            self.neighbours.append(matrix[self.x][self.y -1])
        if self.y < rows -1:
            self.neighbours.append(matrix[self.x][self.y +1])


#make grid
for i in range(col):
    arr = []
    for j in range(rows):
        arr.append(boxes(i, j))
    matrix.append(arr)
matrix[10][0].wall=True
#set neighbours 
for i in range(col):
    for j in range(rows):
        matrix[i][j].set_neighbours()

start_box = matrix[col-1][0]
start_box.start = True
start_box.visited = True
queue.append(start_box)

def main():
    running = True
    begin_search = False
    target_box_set = False
    searching = True
    target_box = None

    while running:
        for events in pygame.event.get():
            # quit the screen
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # mouse controls
            elif events.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # print(x,y)
                # now for wall/ obstruction
                if events.buttons[0]:
                    i = x // box_width
                    j = y // box_height
                    matrix[i][j].wall=True
                # set the target
                if events.buttons[2] and not target_box_set:  #right mouse button is pressed AND target cannot be changed
                    i = x // box_width
                    j = y // box_height
                    # print(i, j)
                    target_box = matrix[i][j]
                    target_box.target = True
                    target_box_set = True
                    #start the algorithm
            if events.type == pygame.KEYDOWN and target_box_set: # any button & the game will start!
                begin_search = True

        if begin_search: # djikstra here!
            if len(queue) > 0 and searching:
                current_box = queue.pop(0)
                current_box.visited = True # put current in visited state
                if current_box == target_box:
                    searching = False
                    while current_box != start_box:
                        path.append(current_box.prior)
                        current_box = current_box.prior
                else:
                    for neighbour in current_box.neighbours:
                        if not neighbour.queued and not neighbour.wall:
                            neighbour.queued = True
                            neighbour.prior = current_box
                            queue.append(neighbour)
            else:
                if searching:
                    Tk().wm_withdraw()
                    messagebox.showinfo("THERE IS NO SOLUTION !!! ")
                    searching = False
        # colours
        for i in range(col):
            for j in range(rows):
                boxes=matrix[i][j]
                boxes.draw(display, (255,255,255))#(R,B,G)

                #select the colors of target, start and wall boxex
                if boxes.wall:# grey
                    boxes.draw(display,(50,50,50))
                if boxes.start:#yellow
                    boxes.draw(display, (255,255,0) )
                if boxes.target: #red
                    boxes.draw(display, (200, 0,0))

                #set visited box and queued boxes colors:
                if boxes.queued:#red
                    boxes.draw(display, (255, 0, 0))
                if boxes.visited:#green
                    boxes.draw(display, (0,200,0))
                #color the path with orange
                if boxes in path:
                    boxes.draw(display, (150,0,150))

        pygame.display.update()
        clock.tick(500) # making it run faster!

main()