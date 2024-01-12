from graphics import *

win = GraphWin("Flags", 600, 600)


def btn():
    t = Text(Point(300, 345), "Please click on the button")
    t.draw(win)


def text():
    bk = Rectangle(Point(210, 335), Point(390, 355))
    bk.setFill("white")
    bk.setOutline("white")
    bk.draw(win)
    t = Text(Point(300, 345), "Please type Syria or Iraq")
    t.draw(win)


def syria():
    red = Rectangle(Point(60, 185), Point(540, 291))
    red.setFill("red")
    red.setOutline("red")
    red.draw(win)
    white = Rectangle(Point(60, 292), Point(540, 398))
    white.setFill("white")
    white.setOutline("white")
    white.draw(win)
    black = Rectangle(Point(60, 399), Point(540, 505))
    black.setFill("black")
    black.draw(win)

    star1 = Polygon(
        Point(180, 330),
        Point(220, 330),
        Point(232, 295),
        Point(245, 330),
        Point(285, 330),
        Point(255, 355),
        Point(265, 390),
        Point(232, 370),
        Point(200, 390),
        Point(210, 355)
    )
    star1.setFill("green")
    star1.setOutline("green")
    star1.draw(win)
    star2 = star1.clone()
    star2.draw(win)
    star1.move(-20, 0)
    star2.move(155, 0)

    t = Text(Point(300, 550), "Type another country or Click anywhere to close")
    t.draw(win)


def iraq():
    red = Rectangle(Point(60, 185), Point(540, 291))
    red.setFill("red")
    red.setOutline("red")
    red.draw(win)
    white = Rectangle(Point(60, 292), Point(540, 398))
    white.setFill("white")
    white.setOutline("white")
    white.draw(win)
    black = Rectangle(Point(60, 399), Point(540, 505))
    black.setFill("black")
    black.draw(win)

    t = Text(Point(300, 345), "الله أكبر")
    t.setSize(36)
    t.setTextColor("green")
    t.setStyle("bold")
    t.draw(win)

    tt = Text(Point(300, 550), "Type another country or Click anywhere to close")
    tt.draw(win)


def main():
    txt = Text(Point(300, 75), "Please enter Syria or Iraq : ")
    txt.draw(win)

    flg = Entry(Point(300, 100), 21)
    flg.setFill(color_rgb(170, 190, 200))
    flg.draw(win)

    bg = Rectangle(Point(250, 130), Point(350, 150))
    bg.setFill(color_rgb(0, 255, 255))
    bg.draw(win)

    txtt = Text(Point(300, 140), "Click Here!")
    txtt.draw(win)

    click = False
    try:
        while win.isOpen():
            x = win.getMouse()
            if 250 <= x.getX() <= 350 and 130 <= x.getY() <= 150:
                country = flg.getText()
                if country == "Syria" or country == "syria":
                    syria()
                elif country == "Iraq" or country == "iraq":
                    iraq()
                else:
                    text()
                click = True
            elif click is True:
                win.close()
                print(x)
                break
            else:
                btn()
    except GraphicsError as err:
        print(err)


if __name__ == '__main__':
    main()
