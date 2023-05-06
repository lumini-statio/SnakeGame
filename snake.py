import turtle
import time
import random

posponer = 0.1

#puntaje
score = 0
high_score = 0

#configuración ventana
window = turtle.Screen()
window.title('snake')
window.bgcolor('black')
window.setup(width=600, height= 600)
window.tracer(0)


#conf cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.color('green')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction ='stop'

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(100,0)

#cuerpo
segmentos = []

#puntos
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write('Score: 0               High Score: 0', align='center', font='Courier')

#funciones
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def derecha():
    cabeza.direction = 'right'
def izquierda():
    cabeza.direction = 'left'

def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        
    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        
    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#teclado
window.listen()
window.onkey(arriba, "Up")
window.onkey(abajo, "Down")
window.onkey(derecha, "Right")
window.onkey(izquierda, "Left")

while True:
    window.update()    
    
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x, y)
        
        segmento = turtle.Turtle()
        segmento.speed(0)
        segmento.shape('square')
        segmento.color('green')
        segmento.penup()
        segmentos.append(segmento)
        
        #aumentar marcador
        
        score += 1
        
        if score > high_score:
            high_score = score

        texto.clear()
        texto.write(f'Score: {score}               High Score: {high_score}', align='center', font='Courier')
        
    totalSeg = len(segmentos)
    for i in range(totalSeg -1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)
        
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)
        
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 280 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = 'stop'
        
        #esconder segmentos
        for segmento in segmentos:
            segmento.goto(1000, 1000)
            
        #limpiar lista segmentos
        segmentos.clear()
        
        score = 0
        
        texto.clear()
        texto.write(f'Score: {score}               High Score: {high_score}', align='center', font='Courier')
        
    mov()
    
    #colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) <20:
            time.sleep(0)
            cabeza.goto(0,0)
            cabeza.direction='stop'
            
            #esconder segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
                
            segmentos.clear()

            score = 0
            
            texto.clear()
            texto.write(f'Score: {score}               High Score: {high_score}', align='center', font='Courier')
    
    time.sleep(posponer)
    
