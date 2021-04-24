import pygame
import socket
import time
import threading
import pickle

# clientttttt code info
FORMAT = "utf-8"
HEADER = 64
PORT = 6000
SERVER = input("enter ip of host - ")
DISCONNECT_MESSAGE = "/DISCONNECT"
ADDR = (SERVER, PORT)
try :
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
except Exception as e:
    print(e)
    time.sleep(120)



# ends here


def getcord():
    a=client.recv(1024)
    if a:
     coordstr = pickle.loads(a)
     return coordstr

def sendcord(xs, ys):
    cord = (xs,ys)
    client.send(pickle.dumps(cord))


white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

x = 100
y = 100
playery_change = 0
playerx_change = 0

reddot = pygame.image.load("playerdot   red.png")

pygame.init()
gameDisplay = pygame.display.set_mode((1500, 700))
gameDisplay.fill(white)


class game:

    def __init__(self):
        global x
        global y
        playery_change = 0
        playerx_change = 0
        # sendthread=threading.Thread(target=sendcord)
        # sendthread.start()

        running = True
        while running:
            time.sleep(0.009)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        playerx_change = -2
                    if event.key == pygame.K_RIGHT:
                        playerx_change = 2
                    if event.key == pygame.K_UP:
                        playery_change = -2
                    if event.key == pygame.K_DOWN:
                        playery_change = +2

                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerx_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        playery_change = 0

            x = x + playerx_change
            y = y + playery_change

            if running:
                gameDisplay.fill(white)
                pygame.draw.circle(gameDisplay, red, (x, y), 15)
                sendcord(x, y)

                pygame.draw.circle(gameDisplay, blue, getcord(), 15)
                pygame.display.update()


print("strating")
try :
 a = game()
except Exception as e:
    print(e)
    time.sleep(120)

print("enfing")
#time.sleep(5)
