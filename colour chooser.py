import pygame as pg

t = True
f = False

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600))
running = t

red = 0
green = 0
blue = 0

hue = 0.0
sat = 0.0
value = 0.0

hsvchange = f

irep = t
rrep = t

textfont = pg.font.SysFont("centurygothic", 20)

print("""Use keys to change colour. y, u, h, j, n and m to increase or decrease red, green or blue respectively. 
Hold shift during this to use hsv instead. e is to enter you own rgb values, i inverts the colour""")

try:
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = f

        screen.fill("white")

        keys = pg.key.get_pressed()

        if keys[pg.K_y]:
            if keys[pg.K_LSHIFT]:
                hue -= 1
                if hue < 0:
                    hue = 359
            elif red > 0:
                red -= 1
        if keys[pg.K_u]:
            if keys[pg.K_LSHIFT]:
                hue += 1
                if hue > 359:
                    hue = 0
            elif red < 255:
                red += 1
        if keys[pg.K_h]:
            if keys[pg.K_LSHIFT]:
                sat -= 0.01
                if sat < 0:
                    sat = 0
            elif green > 0:
                green -= 1
        if keys[pg.K_j]:
            if keys[pg.K_LSHIFT]:
                sat += 0.01
                if sat > 1:
                    sat = 1
            elif green < 255:
                green += 1
        if keys[pg.K_n]:
            if keys[pg.K_LSHIFT]:
                value -= 0.01
                if value < 0:
                    value = 0
            elif blue > 0:
                blue -= 1
        if keys[pg.K_m]:
            if keys[pg.K_LSHIFT]:
                value += 0.01
                if value > 1:
                    value = 1
            elif blue < 255:
                blue += 1

        if keys[pg.K_LSHIFT]:
            hsvchange = t

        if keys[pg.K_i]:
            if irep:
                red = 255 - red
                green = 255 - green
                blue = 255 - blue
            irep = f
        else:
            irep = t

        if keys[pg.K_r]:
            if rrep:
                redcopy = red
                red = green
                green = blue
                blue = redcopy
            rrep = f
        else:
            rrep = t
        

        if keys[pg.K_e]:
            red = int(input("Red value?"))
            green = int(input("Green value?"))
            blue = int(input("Blue value?"))

        if hsvchange:
            cvar = value * sat
            xvar = cvar * (1 - abs((hue/60) % 2 - 1))
            mag = value - cvar

            #sorry, there is definetely a better way to do this
            if 0<=hue<60:  
                ured = cvar
                ugreen = xvar
                ublue = 0
            elif 60<=hue<120:
                ured = xvar
                ugreen = cvar
                ublue = 0
            elif 120<=hue<180:
                ured = 0
                ugreen = cvar
                ublue = xvar
            elif 180<=hue<240:
                ured = 0
                ugreen = xvar
                ublue = cvar
            elif 240<=hue<300:
                ured = xvar
                ugreen = 0
                ublue = cvar
            elif 300<=hue<360:
                ured = cvar
                ugreen = 0
                ublue = xvar

            red = int((ured + mag)*255)
            green = int((ugreen + mag)*255)
            blue = int((ublue + mag)*255)
            
        else:
            ured = red/255
            ugreen = green/255
            ublue = blue/255
            cmax = max(ured, ugreen, ublue)
            cmin = min(ured, ugreen, ublue)
            delta = cmax - cmin
            if delta == 0:
                hue = 0
            elif cmax == ured:
                    hue = 60 * ((ugreen - ublue)/delta % 6)
            elif cmax == ugreen:
                    hue = 60 * ((ublue - ured)/delta + 2)
            elif cmax == ublue:
                    hue = 60 * ((ured - ugreen)/delta + 4)
            
            if cmax == 0:
                sat = 0
            else:
                sat = delta/cmax
            
            value = cmax
            

        hsvchange = f
            
        
        pg.draw.rect(screen,(red,green,blue),(0,0,600,400))

        redtext = "Red: " + str(red)
        greentext = "Green: " + str(green)
        bluetext = "Blue: " + str(blue)
        huetext = "Hue: " + str(round(hue)) + "°"
        sattext = "Saturation: " + str(round(sat * 100)) + "%"
        valuetext = "Value: " + str(round(value * 100)) + "%"

        screen.blit(textfont.render(redtext, t, "black"),(5,405))
        screen.blit(textfont.render(greentext, t, "black"),(115,405))
        screen.blit(textfont.render(bluetext, t, "black"),(225,405))
        screen.blit(textfont.render(huetext, t, "black"),(5,455))
        screen.blit(textfont.render(sattext, t, "black"),(115,455))
        screen.blit(textfont.render(valuetext, t, "black"),(280,455))

        pg.display.flip()

        clock.tick(60)

finally:
    pg.quit()
