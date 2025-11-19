import curses

from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Hello World")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)