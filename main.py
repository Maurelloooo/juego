from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep_ms,sleep

ancho=128
alto=64

i2c = I2C(0, scl=Pin(22), sda=Pin(23)) 
oled = SSD1306_I2C(ancho, alto, i2c)
contadorx=0
contadory=0

posicion=0
pulsar=0
posO=[1,2,3,4,5,6,7,8,9]


sensorx= ADC(Pin(32))
sensorx.atten(ADC.ATTN_11DB)
sensorx.width(ADC.WIDTH_12BIT)

boton1=Pin(21,Pin.IN,Pin.PULL_UP)

sensory= ADC(Pin(33))
sensory.atten(ADC.ATTN_11DB)
sensory.width(ADC.WIDTH_12BIT)

def seleccionar(contadorx, contadory, posicion):
  
   # Fila 1
    if(contadorx==0 and contadory==0):
        oled.text("[ ]", 7, 10, 0)
        posicion=1
    else:
        oled.text(" ", 7, 10, 0)
    
    if(contadorx==1 and contadory==0):
        oled.text("[ ]", 52, 10, 0)
        posicion=2
    else:
        oled.text(" ", 52, 10, 0)
        
    if(contadorx==2 and contadory==0):
        oled.text("[ ]", 96, 10, 0)
        posicion=3
    else:
        oled.text(" ", 96, 10, 0)
        # fila 2
    
    if(contadorx==0 and contadory==1):
        oled.text("[ ]", 7, 30, 0)
        posicion=4
    else:
        oled.text(" ", 7, 30, 0)

    if(contadorx==1 and contadory==1):
        oled.text("[ ]", 52, 30, 0)
        posicion=5
    else:
        oled.text(" ", 52, 30, 0)
    
    if(contadorx==2 and contadory==1):
        oled.text("[ ]", 96, 30, 0)
        posicion=6
    else:
        oled.text(" ", 96, 30, 0)
      # fila 3
    
    if(contadorx==0 and contadory==2):
        oled.text("[ ]", 7, 51, 0)
        posicion=7
    else:
        oled.text(" ", 7, 51, 0)
    
    if(contadorx==1 and contadory==2):
        oled.text("[ ]", 52, 51, 0)
        posicion=8
    else:
        oled.text(" ", 52, 51, 0)
        
    if(contadorx==2 and contadory==2):
        oled.text("[ ]", 96, 51, 0)
        posicion=9
    else:
        oled.text(" ", 96, 51, 0)

matriz=[[2,2,2],[2,2,2],[2,2,2]]
matriztxt=[["","",""],["","",""],["","",""]]

def colocarXyO(posicion, pulsar,turno):
  
  contador= turno

  if(turno==0):
    #no me acuerdo que hacia
    if(pulsar==1 and matriz[0][0]==2):
        matriz[0][0]=1
        matriztxt[0][0]="x"
        contador=not contador
    if(pulsar==2 and matriz[0][1]==2):
        matriz[0][1]=1
        matriztxt[0][1]="x"
        contador=not contador
    if(pulsar==3 and matriz[0][2]==2):
        matriz[0][2]=1
        matriztxt[0][2]="x"
        contador=not contador
    if(pulsar==4 and matriz[1][0]==2):
        matriz[1][0]=1
        matriztxt[1][0]="x"
        contador=not contador
    if(pulsar==5 and matriz[1][1]==2):
        matriz[1][1]=1
        matriztxt[1][1]="x"
        contador=not contador
    if(pulsar==6 and matriz[1][2]==2):
        matriz[1][2]=1
        matriztxt[1][2]="x"
        contador=not contador
    if(pulsar==7 and matriz[2][0]==2):
        matriz[2][0]=1
        matriztxt[2][0]="x"
        contador=not contador
    if(pulsar==8 and matriz[2][1]==2):
        matriz[2][1]=1
        matriztxt[2][1]="x"
        contador=not contador
    if(pulsar==9 and matriz[2][2]==2):
        matriz[2][2]=1
        matriztxt[2][2]="x"
        contador=not contador
            
                    

  else:
    
    if(pulsar==1 and matriz[0][0]==2):
      matriz[0][0]=0
      matriztxt[0][0]="o"
      contador=not contador
    if(pulsar==2 and matriz[0][1]==2):
      matriz[0][1]=0
      matriztxt[0][1]="o"
      contador=not contador
    if(pulsar==3 and matriz[0][2]==2):
      matriz[0][2]=0
      matriztxt[0][2]="o"
      contador=not contador
    if(pulsar==4 and matriz[1][0]==2):
      matriz[1][0]=0
      matriztxt[1][0]="o"
      contador=not contador
    if(pulsar==5 and matriz[1][1]==2):
      matriz[1][1]=0
      matriztxt[1][1]="o"
      contador=not contador
    if(pulsar==6 and matriz[1][2]==2):
      matriz[1][2]=0
      matriztxt[1][2]="o"
      contador=not contador
    if(pulsar==7 and matriz[2][0]==2):
      matriz[2][0]=0
      matriztxt[2][0]="o"
      contador=not contador
    if(pulsar==8 and matriz[2][1]==2):
      matriz[2][1]=0
      matriztxt[2][1]="o"
      contador=not contador
    if(pulsar==9 and matriz[2][2]==2):
      matriz[2][2]=0
      matriztxt[2][2]="o"
      contador=not contador
            
   
  oled.text(matriztxt[0][0], 15, 10, 0)
  oled.text(matriztxt[0][1], 60, 10, 0)
  oled.text(matriztxt[0][2], 103, 10, 0) 

  oled.text(matriztxt[1][0], 15, 27, 0)
  oled.text(matriztxt[1][1], 60, 27, 0)
  oled.text(matriztxt[1][2], 103, 27, 0)   

  oled.text(matriztxt[2][0], 15, 51, 0)
  oled.text(matriztxt[2][1], 60, 51, 0)
  oled.text(matriztxt[2][2], 103, 51, 0)

  return contador
def refrescar(oled):
   
    seleccionar(contadorx, contadory, posicion)


    oled.show()

def Comprobar_partida():

  victoria=False

  for i in range(len(matriz)):
    if matriz[i][0]!=2 and matriz[i][1]!=2 and matriz[i][2]!=2 and (matriz[i][0]==matriz[i][1] and matriz[i][1]==matriz[i][2]):
      if matriz[i][0]==0:
        return 0
      else:
        return 1
        victoria=True
  for i in range(len(matriz[0])):
    if matriz[0][i]!=2 and matriz[1][i]!=2 and matriz[2][i]!=2 and (matriz[0][i]==matriz[1][i] and matriz[1][0]==matriz[2][i]):
      if matriz[0][i]==0:
        return 0
        victoria=True
      else:
        return 1
        victoria=True

  if matriz[1][1]!=2 and ((matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2]) or (matriz[0][2]==matriz[1][1] and matriz[1][1]==matriz[2][0])):
    if matriz[1][1]==0:
      return 0
      victoria=True
    else:
      return 1
      victoria=True

  empate=True
  
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      if matriz[i][j]==2:
        empate=False
  
  if empate==True and victoria==False:
    return 2

  return 3
def vaciar_matrices():
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      matriz[i][j]=2
      matriztxt[i][j]=""

contador=0
end=False

while True:

  oled.text("PARTIDA: ",30, 1,0)

  estado=Comprobar_partida()

  if estado==0:
    pulsar=0
    oled.fill(1)
    vaciar_matrices()
    oled.text("JUGADOR 2 WINNER", 0, 27, 0)
    oled.show()
    sleep(3)
  if estado==1:
    pulsar=0
    oled.fill(1)
    vaciar_matrices()
    oled.text("JUGADOR 1 WINNER", 0, 27, 0)
    oled.show()
    sleep(3)
  if estado==2:
    pulsar=0
    oled.fill(1)
    vaciar_matrices()
    oled.text("EMPATE", 0, 65, 0)
    oled.show()
    sleep(3)
  #linea vertical
  oled.line(42,10,42,64,0)
  oled.line(85,10,85,64,0)
  #linea horizontal
  oled.line(0,23,128,23,0)
  oled.line(0,43,128,43,0)
  
  movimientoX=sensorx.read()
  movimientoY=sensory.read()
  
  if(movimientoX==0 and contadorx!=2):
      contadorx=contadorx+1
      sleep_ms(200)
  if(movimientoX==4095 and contadorx!=0):
      contadorx=contadorx-1
      sleep_ms(200)
  if(movimientoY==0 and contadory!=2):
      contadory=contadory+1
      sleep_ms(200)
  if(movimientoY==4095 and contadory!=0):
      contadory=contadory-1
      sleep_ms(200)

  if(contadorx==0 and contadory==0):
      posicion=1
  if(contadorx==1 and contadory==0):
      posicion=2
  if(contadorx==2 and contadory==0):
      posicion=3
  if(contadorx==0 and contadory==1):
      posicion=4
  if(contadorx==1 and contadory==1):
      posicion=5
  if(contadorx==2 and contadory==1):
      posicion=6
  if(contadorx==0 and contadory==2):
      posicion=7
  if(contadorx==1 and contadory==2):
      posicion=8
  if(contadorx==2 and contadory==2):
      posicion=9
  
  if(not boton1.value()):
      pulsar=posicion
      sleep_ms(200)

  contador=colocarXyO(posicion, pulsar, contador)
  refrescar(oled)

  oled.show()
  oled.fill(1)