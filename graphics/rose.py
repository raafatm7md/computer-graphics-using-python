from graphics import *

win = GraphWin("Rose", 600, 600)
win.setBackground("white")
color1 = color_rgb(255, 0, 255)
bkk = Rectangle(Point(80, 175), Point(530, 535))
bkk.setFill("white")
bkk.setOutline("white")


r1 = Circle(Point(240, 350), 50)
r1.setFill(color1)
r2 = Circle(Point(300, 290), 50)
r2.setFill(color1)
r3 = Circle(Point(360, 350), 50)
r3.setFill(color1)
r4 = Circle(Point(300, 410), 50)
r4.setFill(color1)
r5 = Circle(Point(350, 300), 50)
r5.setFill(color1)
r6 = Circle(Point(250, 300), 50)
r6.setFill(color1)
r7 = Circle(Point(250, 400), 50)
r7.setFill(color1)
r8 = Circle(Point(350, 400), 50)
r8.setFill(color1)
c = Circle(Point(300, 350), 45)
c.setFill(color_rgb(255, 195, 0))
c.setOutline(color_rgb(255, 195, 0))

t = Text(Point(300, 345), "Please click on the button")

bk = Rectangle(Point(210, 335), Point(390, 355))
bk.setFill("white")
bk.setOutline("white")
tz = Text(Point(300, 345), "Please don't exceed 8")


def main():
    txt = Text(Point(300, 70), "Enter a number from 0 to 8 : ")
    txt.draw(win)

    num = Entry(Point(300, 100), 2)
    num.setFill(color_rgb(220, 220, 220))
    num.draw(win)

    bg = Rectangle(Point(250, 130), Point(350, 150))
    bg.setFill(color_rgb(0, 255, 255))
    bg.draw(win)

    buton = Text(Point(300, 140), "Click Here!")
    buton.draw(win)

    c.draw(win)

    click = False
    try:
        while win.isOpen():
            x = win.getMouse()
            if 250 <= x.getX() <= 350 and 130 <= x.getY() <= 150:
                n = num.getText()
                if n == '0':
                    bk.undraw()
                    tz.undraw()
                    t.undraw()
                    r1.undraw()
                    r2.undraw()
                    r3.undraw()
                    r4.undraw()
                    r5.undraw()
                    r6.undraw()
                    r7.undraw()
                    r8.undraw()
                    c.undraw()
                    c.draw(win)
                    click = True
                elif n == '1':
                    bk.undraw()
                    tz.undraw()
                    t.undraw()
                    r1.undraw()
                    r2.undraw()
                    r3.undraw()
                    r4.undraw()
                    r5.undraw()
                    r6.undraw()
                    r7.undraw()
                    r8.undraw()
                    c.undraw()
                    r3.draw(win)
                    c.draw(win)
                    click = True
                elif n == '2':
                    bk.undraw()
                    tz.undraw()
                    t.undraw()
                    r1.undraw()
                    r2.undraw()
                    r3.undraw()
                    r4.undraw()
                    r5.undraw()
                    r6.undraw()
                    r7.undraw()
                    r8.undraw()
                    c.undraw()
                    r3.draw(win)
                    r5.draw(win)
                    c.draw(win)
                    click = True
                elif n == '3':
                    bk.undraw()
                    tz.undraw()
                    t.undraw()
                    r1.undraw()
                    r2.undraw()
                    r3.undraw()
                    r4.undraw()
                    r5.undraw()
                    r6.undraw()
                    r7.undraw()
                    r8.undraw()
                    c.undraw()
                    r2.draw(win)
                    r3.draw(win)
                    r5.draw(win)
                    c.draw(win)
                    click = True
                elif n == '4':
                    bk.undraw()
                    tz.undraw()
                    t.undraw()
                    r1.undraw()
                    r2.undraw()
                    r3.undraw()
                    r4.undraw()
                    r5.undraw()
                    r6.undraw()
                    r7.undraw()
                    r8.undraw()
                    c.undraw()
                    r2.draw(win)
                    r3.draw(win)
                    r5.draw(win)
                    r6.draw(win)
                    c.draw(win)
                    click = True
                elif n == '5':
                    bk.undraw()
                    tz.undraw()
                    t.undraw()
                    r1.undraw()
                    r2.undraw()
                    r3.undraw()
                    r4.undraw()
                    r5.undraw()
                    r6.undraw()
                    r7.undraw()
                    r8.undraw()
                    c.undraw()
                    r1.draw(win)
                    r2.draw(win)
                    r3.draw(win)
                    r5.draw(win)
                    r6.draw(win)
                    c.draw(win)
                    click = True
                elif n == '6':
                    bk.undraw()
                    tz.undraw()
                    t.undraw()
                    r1.undraw()
                    r2.undraw()
                    r3.undraw()
                    r4.undraw()
                    r5.undraw()
                    r6.undraw()
                    r7.undraw()
                    r8.undraw()
                    c.undraw()
                    r1.draw(win)
                    r2.draw(win)
                    r3.draw(win)
                    r5.draw(win)
                    r6.draw(win)
                    r7.draw(win)
                    c.draw(win)
                    click = True
                elif n == '7':
                    bk.undraw()
                    tz.undraw()
                    t.undraw()
                    r1.undraw()
                    r2.undraw()
                    r3.undraw()
                    r4.undraw()
                    r5.undraw()
                    r6.undraw()
                    r7.undraw()
                    r8.undraw()
                    c.undraw()
                    r1.draw(win)
                    r2.draw(win)
                    r3.draw(win)
                    r4.draw(win)
                    r5.draw(win)
                    r6.draw(win)
                    r7.draw(win)
                    c.draw(win)
                    click = True
                elif n == '8':
                    bk.undraw()
                    tz.undraw()
                    t.undraw()
                    r1.undraw()
                    r2.undraw()
                    r3.undraw()
                    r4.undraw()
                    r5.undraw()
                    r6.undraw()
                    r7.undraw()
                    r8.undraw()
                    c.undraw()
                    r1.draw(win)
                    r2.draw(win)
                    r3.draw(win)
                    r4.draw(win)
                    r5.draw(win)
                    r6.draw(win)
                    r7.draw(win)
                    r8.draw(win)
                    c.draw(win)
                    click = True
                else:
                    bk.draw(win)
                    tz.draw(win)
                    click = True
            elif click is True:
                win.close()
                print(x)
                break
            else:
                t.draw(win)
    except GraphicsError as err:
        print(err)


if __name__ == '__main__':
    main()