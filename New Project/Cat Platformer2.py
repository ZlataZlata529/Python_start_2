import play
import pygame
from random import randint

play.set_backdrop("thistle")
pygame.display.set_caption('Cat Platformer')



icon=pygame.image.load("E:/Программирование/Python/New Project/cat.png")
pygame.display.set_icon(icon)

#счетчик монет
score_txt = play.new_text(words='Score:', x=play.screen.right-100, y=play.screen.top-30, size=70,color="white")
score = play.new_text(words='0', x=play.screen.right-30, y=play.screen.top-30, size=70,color="white")

#подсказки
text = play.new_text(words='Tap SPACE to jump, LEFT/RIGHT to move', x=0, y=play.screen.bottom+60, size=70, color="white")
lose= play.new_text(words='YOU LOSE! CAT HATES WATER! BRR!', x=0, y=play.screen.bottom+80, size=70, color="red")
win= play.new_text(words='YOU WON! NOW CAT IS HAPPY! YAY!', x=0, y=play.screen.bottom+80, size=70, color="green")

sea = play.new_box(
        color='dodgerblue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20
    )

character=play.new_image(image="E:/Программирование/Python/New Project/new/syobon2.png",x=-340,y=150,size=10)
finish=play.new_image(image="E:/Программирование/Python/New Project/finish.png",x=170,y=-120,size=7)

platforms=[]
coins=[]
cat_coins=0

def draw_platforms():
    platform1=play.new_box(color="olivedrab", x=-340,y=100,border_color="darkgreen",border_width=5, width=100,height=20)
    platforms.append(platform1)
    platform2=play.new_box(color="olivedrab", x=-200,y=100,border_color="darkgreen",border_width=5, width=100,height=20)
    platforms.append(platform2)
    platform3=play.new_box(color="olivedrab", x=100,y=150,border_color="darkgreen",border_width=5, width=300,height=20)
    platforms.append(platform3)
    platform4=play.new_box(color="olivedrab", x=400,y=50,border_color="darkgreen",border_width=5, width=300,height=20)
    platforms.append(platform4)
    platform5=play.new_box(color="olivedrab", x=150,y=-5,border_color="darkgreen",border_width=5, width=100,height=20)
    platforms.append(platform5)
    platform6=play.new_box(color="olivedrab", x=-150,y=-5,border_color="darkgreen",border_width=5, width=300,height=20)
    platforms.append(platform6)
    platform7=play.new_box(color="olivedrab", x=100,y=-150,border_color="darkgreen",border_width=5, width=800,height=20)
    platforms.append(platform7)
    for p in platforms:
        p.start_physics(can_move=False, stable=True, obeys_gravity=False,mass=10)

def draw_coins():
    coin1=play.new_circle(color="gold",x=-200,y=140, radius=10,border_color="darkorange", border_width=5)
    coins.append(coin1)
    coin2=play.new_circle(color="gold",x=150,y=190, radius=10,border_color="darkorange", border_width=5)
    coins.append(coin2)
    coin3=play.new_circle(color="gold",x=150,y=50, radius=10,border_color="darkorange", border_width=5)
    coins.append(coin3)
    coin4=play.new_circle(color="gold",x=-150,y=30, radius=10,border_color="darkorange", border_width=5)
    coins.append(coin4)
    coin5=play.new_circle(color="gold",x=30,y=-120, radius=10,border_color="darkorange", border_width=5)
    coins.append(coin5)

@play.when_program_starts  
def start():
    #подключи фоновую музыку
    character.start_physics(can_move=1,stable=1,obeys_gravity=1, bounciness=0.5)
    draw_platforms()
    draw_coins()
    lose.hide()
    win.hide()

@play.repeat_forever
async def game():
  


    #тут опиши процесс игры  
    global cat_coins
    for j in coins:
        if j.is_touching(character):
            pygame.mixer_music.load("E:/Программирование/Python/New Project/coin.wav")
            pygame.mixer_music.play()
            coins.remove(j)
            j.hide()  
            score.words=int(score.words)+1 
            cat_coins=cat_coins+1 
    
    if play.key_is_pressed("a") and character.x>play.screen.left+75:
        character.physics.x_speed=-10
    elif play.key_is_pressed("d") and character.x<play.screen.right-75:
        character.physics.x_speed=10
    else:
        character.physics.x_speed=0  

    for p in platforms:
        if play.key_is_pressed("space") and p.is_touching(character):
            pygame.mixer_music.load("E:/Программирование/Python/New Project/jump.mp3")
            pygame.mixer_music.play()
            character.physics.y_speed=40
    if character.physics.y_speed>0:
        character.physics.y_speed-=1  
    if character.is_touching(sea):
        pygame.mixer_music.load("E:/Программирование/Python/New Project/lose.mp3")
        pygame.mixer_music.play()
        lose.show()
        await play.timer(seconds=2)
        quit()
    if character.is_touching(finish) and cat_coins==5:
        pygame.mixer_music.load("E:/Программирование/Python/New Project/win.mp3")
        pygame.mixer_music.play()
        win.show()
        await play.timer(seconds=5)
        quit()
    await play.timer(seconds=1/48)

play.start_program()