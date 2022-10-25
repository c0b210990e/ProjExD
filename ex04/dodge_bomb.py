import pygame as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct):
    """
    #obj_rct : こうかとんrctまたは爆弾rct
    src_rct : スクリーンrct
    領域内 : +1 /領域外 : -1
    """
    yoko, take = 1, 1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        take = -1

    return yoko, take


def main():
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに「逃げろ！こうかとん」と表示
    scrn_sfc = pg.display.set_mode((1600,900)) #800×600の画面Surfaceを生成
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10) #半径10の赤い円
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    vx, vy = 1, 1

    clock = pg.time.Clock()

    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]: tori_rct.centery -= 1
        if key_states[pg.K_DOWN]: tori_rct.centery += 1
        if key_states[pg.K_LEFT]: tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1
        yoko, take = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if take == -1:
            if key_states[pg.K_UP]:
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1
        scrn_sfc.blit(tori_sfc, tori_rct)

        yoko, take = check_bound(bomb_rct,scrn_rct)
        vx *= yoko
        vy *= take
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)

        if tori_rct.colliderect(bomb_rct): 
            fonto = pg.font.Font(None, 200)
            moji = "Game Over"
            txt = fonto.render(str(moji),True,(255,0,0))
            scrn_sfc.blit(txt, (400,450))
            pg.display.update()
            clock.tick(1)
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()