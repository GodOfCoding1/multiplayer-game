import socket
import threading
import sys
import pickle
PORT = 6000
SERVER = socket.gethostbyname(socket.gethostname())
global playernumber
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
clients, names, players = [], [], []
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind(ADDRESS)
DISCONNECT_MESSAGE = "/DISCONNECT"
DISCONNECT_MESSAGE2 = "/disconnect"
DISCONNECT_MESSAGE3 = "/quit"
playerdata = {}
playernumber = 0

def closedconnection(conn):
    global playernumber
    global clients
    playernumber-=1
    clients.remove(conn)
    conn.close()



def playersdatastore(cordtup, playernumber):
    global playerdata

    playerdata[playernumber] = cordtup


def getplayerdata(conn):

    return playerdata[conn]


def getcord(conn):
    coordstr = pickle.loads(conn.recv(500))
    return coordstr


'''def sendcord(conn, cordtup):
    cordstr = str(cordtup[0]) + ',' + str(cordtup[1])
    conn.send(cordstr.encode(FORMAT))'''
def sendcord(conn, cordtup):
    conn.send(pickle.dumps(cordtup))


# function to start the connection
def startcooention():
    global playernumber
    global clients
    print("server is working on " + SERVER)

    server.listen()


    while True:
        conn, addr = server.accept()
        # conn.send("?NAME?".encode(FORMAT))

        players.append(playernumber)
        clients.append(conn)

        print(f"player {playernumber} joined")

        # broadcastMessage("{name} has joined.".encode(FORMAT))

        # conn.send('Connection successful'.encode(FORMAT))

        thread = threading.Thread(target=handle,
                                  args=(conn, addr, playernumber))
        thread.start()
        playerdata[conn]=(-10,-10)


        playernumber += 1
        print(f"active connections {threading.activeCount() - 1}")


def handle(conn, addr, playernumber):
    print(f"new connection {addr}")
    clients.append(conn)
    connected = True
    while connected:
      try:
          playersdatastore(getcord(conn), conn)
          try:
           sendtoplayers(conn)
          except Exception as e:
             print(e)
             print(f"a player has disconnected")
      except:
          print(f"closing : {addr}")
          closedconnection(conn)
          break
    sys.exit()
    print(f"active connections {threading.activeCount() - 1}")




def sendtoplayers(conn):

    for i in clients:
        if i == conn:
            pass
        else:
            sendcord(i,getplayerdata(conn))



try:
    startcooention()
except Exception as e:
    print(e)
    #time.sleep(120)
