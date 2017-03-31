from gamelib import *
game = Game(1400, 700, "my gmae")
bk = Animation("images\\newbk2.png",8,game,994,243,10)
bk.resizeTo(game.width, game.height)
game.setBackground(bk)
sword=Image("images\\sword.png",game)
sword.resizeBy(-50)
c= Animation("images\\sc.png",2,game,328.5,364,3)
c.resizeBy(-75)
c_cooldown=30
c_energy=0
c.moveTo(300,600)
wing = Image("images\\wing.png",game)
wing.resizeBy(-50)
boss=Image("images//boss.gif",game)
boss.setSpeed(15,29.314526)
boss_2 =0
boss_hp =3
boss_tl = 180
boss1=Image("images//boss.gif",game)
boss1.setSpeed(15,29.314526)
boss1_2 =0
boss1_hp =20
boss1_tl = 180
boss2=Animation("images//gboss2.png",4,game,260,275,3)
boss2_hp =20
boss2_as = 0
boss2_dash_timer =0
arrow =[]
c_ArrowAmount = 20
potion=[]
game.setMusic("sound\\gbk.wav")
game.playMusic()
jumping = False
landed = False
factor = 1
fms=[]
fms2=[]
obj_web =[]
obj_fireball =[]
boss2_cd = 0;
sword_angle =190
boss_cd =0;
gi_1 = 0
for num in range(15):
    potion.append( Image("images//potion1.png",game))
for a in potion:
    a.resizeBy(-80)
    x=game.width+randint(100,10500)
    y=randint(550,575)
    s=randint(4,7)
    a.moveTo(x,y)
    a.setSpeed(s,90)
for times in range(50):
    fms2.append( Image("images\\m22.png",game))
for fm2 in fms2:
    x = game.width+randint(100,10500)
    y = randint(250,575)
    s = randint (4 , 7 )
    fm2.moveTo(x,y)
    fm2.setSpeed(s,90)        
for times in range(15):
    fms.append( Image("images\\m2.png",game))    
for fm in fms:
    x = game.width+randint(100,10500)
    y = randint(250,575)
    s = randint (4 , 7 )
    fm.moveTo(x,y)
    fm.setSpeed(s,90)
bar = Image("images\\paddle.png",game)
bar.setSpeed(4,90)
game.drawBackground()
game.drawText("Kill Or Be Killed",500,200,Font(black,100,red))
game.drawText("Press [SPACE] to Start",500,500,Font(black,50,red))
gi = Image("images\\pp.png",game)
game.update()
game.wait(K_SPACE)
gi.resizeTo(game.width,game.height)
gi.draw()
game.update()
game.wait(K_SPACE)
if keys.Pressed[K_SPACE]:
    gi_1+=1
if gi_1>+1:
    gi.draw()    
game.wait(K_SPACE)    
game.update(50)
while not game.over:    
    game.processInput()
    game.scrollBackground("left",3)    
    c.move()
    c.x-=1.5   
    c_cooldown -=2   
    c_energy +=1
    if c_cooldown<=1:
        c_cooldown+=1        
    boss.move(True)
    if game.score > 49:
        for n in range(100):
            n +=1
            if boss_cd ==60 *n:
                obj_web.append(     Image("images\\bossweapon.png",game))
                obj_web[len(obj_web)-1].resizeBy(-75);
                obj_web[len(obj_web)-1].moveTo(boss.x,boss.y)
                obj_web[len(obj_web)-1].move()
                obj_web[len(obj_web)-1].setSpeed(50,90);
        for b_w in obj_web:
            b_w.move();
            if c.collidedWith(b_w):
                c.health=0
    wing.moveTo(c.x-55,c.y)
    sword.moveTo(c.x+10,c.y)
    sword.rotateTo(sword_angle)
    for a in potion:
        a.move()
        if a.isOffScreen("left"):
            x = game.width+randint(100,10500)
            y = randint(550,575)
            a.moveTo(x,y)
        if c.collidedWith(a):
            c.health+=10
            a.makeVisible(False)           
    for fm in fms:
        fm.move()
        if sword.collidedWith(fm):
            fm.makeVisible(False)
            x = game.width+randint(100,10500)
            y = randint(250,575)
            fm.moveTo(x,y)
            game.score+=10
        if fm.collidedWith(boss):
            boss_hp += 0.5
            fm.makeVisible(False) 
        if fm.isOffScreen("left"):
            x = game.width+randint(100,10500)
            y = randint(250,575)
            fm.moveTo(x,y)
            s=randint(4,7)
            fm.setSpeed(s,90)
            fm.makeVisible(True)
    if keys.Pressed[K_k]:
            sword_angle -=20
    else:
        sword_angle =190
    if sword_angle <=21:
        sword_angle =20        
    if keys.Pressed[K_w]:        
        c.y-=8       
    if keys.Pressed[K_d]:        
        c.x+=8      
    if keys.Pressed[K_a]:        
        c.x-=8
    if c_energy>=100:        
        c_energy-=1        
    if keys.Pressed[K_SPACE]:        
        c_energy-=5        
        c.x+=8        
        if c_energy<=0:            
            c.x-=5            
            c_energy=0
    if c.y>=game.height-95:        
        landed=True    
    if jumping:
        c.y-=25 * factor
        factor *=.95
        landed =False
        if factor<.18:
            jumping =False
            factor =1            
    if keys.Pressed[K_SPACE] and landed and not jumping:        
        jumping = True        
    if not landed:        
        c.y+=11        
    if c_cooldown<=-1:        
        c_cooldown+=1        
    if c_cooldown <=1: 
        if keys.Pressed[K_j]:            
            arrow.append( Image("Images\\arrow.png",game))
            arrow[len(arrow)-1].resizeBy(-70)
            arrow[len(arrow)-1].moveTo(c.x,c.y)                       
            c_cooldown =50
            c_ArrowAmount -=1
    for fm in fms:
        if keys.Pressed[K_k]:
            if sword.collidedWith(fm):
                fm.makeVisible(False)
                x = game.width+randint(100,10500)
                y = randint(250,575)
                fm.moveTo(x,y)
                game.score+=10
    for a in arrow:       
        a.move()        
        a.setSpeed(65,-90)
        if a.isOffScreen("right"):
            a.makeVisible(False)
        for fm in fms:
            if a.collidedWith(fm):
                fm.makeVisible(False)
                x = game.width+randint(100,10500)
                y = randint(250,575)
                fm.moveTo(x,y)
                a.makeVisible(False)
                game.score+=10
                c_ArrowAmount +=5
    if c.collidedWith(boss):
        c.health =0
    if c.health<=0:
        game.over= True
    if game.score <50:
        boss_hp = 3
    if game.score >=50:
        game.drawText("time left:"+str(boss_tl),690,35)
        boss_tl-=0.1
        if boss_2 ==0:
            boss.rotateTo(-90)
            boss.moveTo(game.width -150,400)
            boss.setSpeed(10,180)
            boss_2=1
    for a in arrow:
        if a.collidedWith(boss):
            boss_hp -=1
            a.makeVisible(False)            
    if c.isOffScreen("left"):
        game.over= True
    if c.isOffScreen("right"):
        game.over= True
    if c.isOffScreen("up"):
        game.over= True
    if c.isOffScreen("down"):
        game.over= True
    if boss_hp <=0:
        game.over= True
    boss_cd +=1;        
    game.drawText("Arrow Cooldown: " + str(c_cooldown),90,5,Font(red,25,black))    
    game.drawText("Energy: " + str(c_energy),290,5,Font(red,25,black)) 
    game.drawText("health:"+str(c.health),490,5,Font(red,25,black)) 
    game.drawText("boss hp:"+str(boss_hp),690,5,Font(red,25,black)) 
    game.drawText("Arrow amount:"+str(c_ArrowAmount),90,35,Font(red,25,black))
    game.displayScore()
    game.update(60)
game.drawText("Press space to start to play next level",100,300,Font(black,100,red))
game.update(1)
game.wait(K_SPACE) 
game.over= False
bk = Image("images\\newbk3.jpg",game)
bk.resizeTo(game.width,game.height)
game.setBackground(bk)
game.score = 0
game.update(60)
boss2.moveTo(game.width -150,400)
boss2.setSpeed(10,180)
while not game.over:    
    game.processInput()
    game.scrollBackground("left",3)    
    c.move()
    c.x-=1.5
    c.y+=1.5
    c_cooldown -=2
    boss2_as +=1
    boss2_cd +=1;
    if boss2_as <=100:
        boss2.setSpeed(10,180)
        boss2.move(True)
    if boss2_as >=100:
        boss2.setSpeed(10,90)
        boss2.move(False)
    if boss2.isOffScreen("left"):
        boss2_as == 0
        jb = randint(150,350)
        boss2.moveTo(game.width -150 ,jb)
        boss2.setSpeed(10,180)
        boss2.move(True)            
    for q in range(100):
            q +=1
            if boss2_cd ==60 *q:
                obj_fireball.append(     Image("images\\fireball.png",game))
                obj_fireball[len(obj_web)-1].resizeBy(-50);
                obj_fireball[len(obj_web)-1].moveTo(boss2.x,boss2.y)
                obj_fireball[len(obj_web)-1].move()
                obj_fireball[len(obj_web)-1].setSpeed(50,90);
                if obj_fireball[len(obj_web)].isOffScreen("left"):
                        obj_fireball[len(obj_web)].makeVisible(False)
                        
    for b_b in obj_fireball:
        b_b.move();
        if c.collidedWith(b_b):
            game.over= True    
    if c_cooldown<=1:
        c_cooldown+=1
    for fm2 in fms2:
        if sword.collidedWith(fm):
            fm.makeVisible(False)
            x = game.width+randint(100,10500)
            y = randint(250,575)
            fm.moveTo(x,y)
            game.score+=5
    wing.moveTo(c.x-55,c.y)
    sword.moveTo(c.x+10,c.y)
    sword.rotateTo(sword_angle)
    for a in potion:
        a.move()
        if a.isOffScreen("left"):
            x = game.width+randint(100,10500)
            y = randint(550,575)
            a.moveTo(x,y)
        if c.collidedWith(a):
            c.health+=5
            a.makeVisible(False)           
    for fm2 in fms2:
        fm2.move()
        if sword.collidedWith(fm2):
            fm2.makeVisible(False)
            x = game.width+randint(100,10500)
            y = randint(250,575)
            fm2.moveTo(x,y)
            game.score+=5
        if fm2.isOffScreen("left"):
            x = game.width+randint(100,10500)
            y = randint(250,575)
            fm2.moveTo(x,y)
            s=randint(4,7)
            fm2.setSpeed(s,90)
            fm2.makeVisible(True)
    if keys.Pressed[K_k]:
            sword_angle -=20
    else:
        sword_angle =190
    if sword_angle <=21:
        sword_angle =20        
    if keys.Pressed[K_w]:        
        c.y-=8
    if keys.Pressed[K_s]:        
        c.y+=8
    if keys.Pressed[K_d]:        
        c.x+=8      
    if keys.Pressed[K_a]:        
        c.x-=8
    if c_cooldown<=-1:        
        c_cooldown+=1        
    if c_cooldown <=1: 
        if keys.Pressed[K_j]:            
            arrow.append( Image("Images\\arrow.png",game))
            arrow[len(arrow)-1].resizeBy(-70)
            arrow[len(arrow)-1].moveTo(c.x,c.y)
            c_cooldown =50
            c_ArrowAmount -=1
    for a in arrow: 
        a.move()        
        a.setSpeed(65,-90)
        if a.isOffScreen("right"):
            a.makeVisible(False)
        if a.collidedWith(boss2):
            boss2_hp-=1
            a.makeVisible(False)
        for fm2 in fms2:
            if a.collidedWith(fm2):
                fm2.makeVisible(False)
                x = game.width+randint(100,10500)
                y = randint(250,575)
                fm2.moveTo(x,y)
                a.makeVisible(False)
                game.score+=5
                c_ArrowAmount +=5                
    if c.collidedWith(boss2):
        game.over= True
    if c.health<=0:
        game.over= True
    if c.isOffScreen("left"):
        game.over= True
    if c.isOffScreen("right"):
        game.over= True
    if c.isOffScreen("up"):
        game.over= True
    if c.isOffScreen("down"):
        game.over= True
    if c.health<=0:
        game.over= True
    if game.score >=1000:
        game.over =True
    if boss2_hp<=0:
        game.over =True
    if c.collidedWith(boss2):
        c.health =0
    game.drawText("Arrow Cooldown: " + str(c_cooldown),90,5,Font(red,25,black))
    game.drawText("Arrow Cooldown: " + str(c_cooldown),90,5,Font(red,25,black))
    game.drawText("health:"+str(c.health),490,5,Font(red,25,black)) 
    game.drawText("boss hp:"+str(boss2_hp),690,5,Font(red,25,black)) 
    game.drawText("Arrow amount:"+str(c_ArrowAmount),90,35,Font(red,25,black))
    game.displayScore()
    game.update(30)
game.drawText("Game Over ",100,400,Font(blue,100,black))
game.drawText("Press Space To Exit",200,500,Font(red,100,black))
game.update(1)
game.wait(K_SPACE)
game.quit()

    
