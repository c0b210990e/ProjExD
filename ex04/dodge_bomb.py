import pygame as pg
import sys


def main():
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに「初めてのPyGame」と表示
    scrn_sfc = pg.display.set_mode((1600,900)) #800×600の画面Surfaceを生成

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    scrn_sfc.blit(bg_sfc,bg_rct)
    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(0.2)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()