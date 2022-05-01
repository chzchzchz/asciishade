from curses import wrapper
from curses import start_color
from curses import use_default_colors
from curses import init_pair
from curses import color_pair
import curses

x = 0
y = 0
current_color_pair = 1
max_color_pair_defined = -1
mode = 'normal'
max_x = -1
max_y = -1
current_character = -1
hud_color = 8
quit = False
movement_keys = ['KEY_LEFT', 'KEY_RIGHT', 'KEY_UP', 'KEY_DOWN']


def switch_mode():
    global mode
    if mode == 'normal':
        mode = 'text'
    elif mode == 'text':
        mode = 'normal'


def add_character(s, c):
    global x
    s.addstr(y, x, c, color_pair(current_color_pair))
    #s.addstr(y, x, '▀', color_pair(current_color_pair))
    x += 1


def reset_cursor(s, dy=0, dx=0):
    global y, x
    y = dy
    x = dx
    s.move(y, x)


def draw_hud(s):
    for j in range(max_y-2, max_y):
        for i in range(0, max_x):
            try:
                s.addstr(j, i, ' ', color_pair(hud_color))
            except:
                pass

    s.addstr(max_y-2, 0, f'y: {y:3} | ', color_pair(hud_color)) 
    s.addstr('█', color_pair(current_color_pair))
    s.addstr(f'{current_color_pair:3}', color_pair(hud_color))
    s.addstr(max_y-1, 0, f'x: {x:3} | ', color_pair(hud_color)) 
    s.addstr('#', color_pair(current_color_pair))
    s.addstr(f'{current_color_pair:3}', color_pair(hud_color))
    reset_cursor(s, y, x)


def handle_input(s, c):
    global y, x
    global mode
    global current_color_pair
    global current_character
    global hud_color
    global quit
    if not c in movement_keys:
        if mode == 'normal':
            if c == '`':
                switch_mode()
            elif c == ' ':
                s.addstr(y, x, c, color_pair(current_color_pair))
                x += 1
            elif c == 'c':
                current_color_pair -= 1
                if current_color_pair < 0:
                    current_color_pair = max_color_pair_defined-1
            elif c == 'v':
                current_color_pair += 1
                if current_color_pair >= max_color_pair_defined:
                    current_color_pair = 0
            elif c == 'q':
                quit = True
            elif c == 'i': #info
                attr = s.inch(y, x)
                char = chr(attr & curses.A_CHARTEXT)
                color = attr & curses.A_COLOR
                current_character = char
                my_attrs = f'{bin(attr)} {hex(attr)} {attr} {char} {bin(color)} {hex(color)} {color}'
                s.addstr(y, x+1, str(my_attrs))
        elif mode == 'text':
            if c == '`':
                switch_mode()
            else:
                add_character(s, c)
    elif c == movement_keys[0]:
        x -= 1
    elif c == movement_keys[1]:
        x += 1
    elif c == movement_keys[2]:
        y -= 1
    elif c == movement_keys[3]:
        y += 1
    check_cursor_bounds()
    s.move(y, x)

def check_cursor_bounds():
    global y, x
    if x <= 0:
        x = 0
    elif x > max_x - 2:
        x = max_x - 2
    if y <= 0:
        y = 0
    elif y > max_y - 3:
        y = max_y - 3


def define_color_pairs():
    global max_color_pair_defined
    x = 0
    for j in range(128):
        for i in range(256):
            init_pair(x, i, j)
            x += 1
    max_color_pair_defined = x


def draw_initial_ascii(s):
    lines = [ 'Welcome to shade v0.1',
        'by darkmage',
        'www.evildojo.com'
    ]
    y0 = 0
    for i in lines:
        s.addstr(y0, 0, i, color_pair(8))
        y0 += 1


def main(s):
    global mode
    global y, x
    global max_y, max_x
    s.clear()
    max_y, max_x = s.getmaxyx()
    start_color()
    use_default_colors()
    define_color_pairs()
    draw_initial_ascii(s)
    y, x = s.getyx()
    s.refresh()
    while quit != True:
        draw_hud(s)
        c = s.getkey()
        handle_input(s, c)
        s.refresh()


if __name__ == '__main__':
    wrapper(main)
