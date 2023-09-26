import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    kk_img = pg.image.load("fig/3.png")
    rot_kk_img = pg.transform.flip(kk_img,True, False)
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)
    lst = [kk_img, rot_kk_img]
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img, [0, 0])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()