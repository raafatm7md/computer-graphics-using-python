# note : after the emoji stops it will start laughing, and you click on the window to close it
# note : moving speed depends on your CPU

from graphics import *

win = GraphWin("Emoji", 650, 650)    # 650 x 650 pixel window
yellow = color_rgb(255, 240, 0)


def moving_tears(t1, t2):
    while win.checkMouse() is None:
        for _ in range(30):
            t1.move(0, 1)
            t2.move(0, 1)
            time.sleep(.02)
        t1.move(0, -30)
        t2.move(0, -30)


def move(shape, x, y, n):
    for i in range(n):
        for _ in shape:
            _.move(x, y)
        time.sleep(0.0000001)


def draw_rectangle(x1, y1, x2, y2, color):
    r = Rectangle(Point(x1, y1), Point(x2, y2))
    r.setFill(color)
    r.setOutline(color)
    r.draw(win)
    return r


def main():
    # Face
    shadow = Circle(Point(335, 330), 150)
    shadow.setFill(color_rgb(255, 215, 0))
    shadow.setOutline(color_rgb(255, 215, 0))
    shadow.draw(win)
    face = Circle(Point(325, 325), 150)
    face.setFill(yellow)
    face.setOutline(yellow)
    face.draw(win)

    # Mouth
    mouth = Circle(Point(325, 315), 120)
    mouth.setFill(color_rgb(40, 40, 40))
    mouth.setOutline(color_rgb(40, 40, 40))
    mouth.draw(win)
    r1 = draw_rectangle(228, 210, 420, 390, yellow)
    r2 = draw_rectangle(205, 240, 230, 390, yellow)
    r3 = draw_rectangle(410, 242, 447, 390, yellow)
    r4 = draw_rectangle(265, 215, 385, 190, yellow)
    tongue = Oval(Point(280, 410), Point(370, 460))
    tongue.setFill(color_rgb(255, 50, 50))
    tongue.setOutline(color_rgb(255, 50, 50))
    tongue.draw(win)
    t = Circle(Point(325, 325), 120)
    t.setOutline(yellow)
    t.setWidth(16)
    t.draw(win)
    tt = draw_rectangle(275, 440, 370, 460, yellow)

    # Eyebrows
    eb1 = Circle(Point(255, 270), 45)
    eb1.setFill(color_rgb(205, 180, 50))
    eb1.setOutline(color_rgb(205, 200, 100))
    eb1.draw(win)
    b1 = Circle(Point(265, 295), 60)
    b1.setFill(yellow)
    b1.setOutline(yellow)
    b1.draw(win)
    eb2 = eb1.clone()
    eb2.draw(win)
    b2 = b1.clone()
    b2.draw(win)
    eb2.move(140, 0)
    b2.move(120, 0)

    # Eyes
    i1 = Oval(Point(225, 270), Point(300, 350))
    i1.setFill(color_rgb(110, 50, 50))
    i1.setOutline(color_rgb(110, 50, 50))
    i1.draw(win)
    ii1 = Oval(Point(215, 270), Point(310, 350))
    ii1.setFill(yellow)
    ii1.setOutline(yellow)
    ii1.draw(win)
    i1.move(0, 5)
    ii1.move(0, 30)
    i2 = i1.clone()
    ii2 = ii1.clone()
    i2.draw(win)
    i2.move(125, 0)
    ii2.draw(win)
    ii2.move(125, 0)

    teeth = draw_rectangle(230, 365, 420, 390, "white")  # teeth

    # Tears
    tear1 = Polygon(Point(245, 320),
                    Point(245, 380),
                    Point(243, 382),
                    Point(240, 385),
                    Point(235, 386),
                    Point(230, 387),
                    Point(225, 386),
                    Point(220, 385),
                    Point(215, 382),
                    Point(210, 378),
                    Point(206, 370),
                    Point(205, 365))
    tear1.setFill("blue")
    tear1.setOutline("blue")
    tear2 = Polygon(Point(400, 320),
                    Point(400, 380),
                    Point(402, 382),
                    Point(405, 385),
                    Point(410, 386),
                    Point(415, 387),
                    Point(420, 386),
                    Point(425, 385),
                    Point(430, 382),
                    Point(435, 378),
                    Point(439, 370),
                    Point(440, 365))
    tear2.setFill("blue")
    tear2.setOutline("blue")
    tear1.draw(win)
    tear2.draw(win)

    emoji = [shadow, face,
             mouth, r1, r2, r3, r4,
             tongue, t, tt,
             eb1, eb2, b1, b2,
             i1, i2, ii1, ii2,
             teeth,
             tear1, tear2]

    try:

        move(emoji, -1, 0, 175)
        move(emoji, 1, 0, 340)
        move(emoji, -1, 0, 165)
        moving_tears(tear1, tear2)
        win.close()
    except GraphicsError as err:
        print("Error :", err)
    except KeyboardInterrupt:
        print("Closed by force")


if __name__ == '__main__':
    main()
