import random
import curses
import os

def snake_game(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.timeout(100)

    snake = [[sh // 2, sw // 2 + 1], [sh // 2, sw // 2], [sh // 2, sw // 2 - 1]]
    food = [sh // 2, sw // 2 - 5]

    def print_snake():
        for s in snake:
            w.addch(s[0], s[1], curses.ACS_CKBOARD)

    def print_food():
        w.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        elif key == curses.KEY_UP:
            new_head[0] -= 1
        elif key == curses.KEY_LEFT:
            new_head[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                nf = [random.randint(1, sh - 1), random.randint(1, sw - 1)]
                food = nf if nf not in snake else None
            print_food()
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        if (
            new_head[0] in [0, sh] or
            new_head[1] in [0, sw] or
            new_head in snake[1:]
        ):
            break

        print_snake()

if __name__ == "__main__":
    # Use os.system('cls') for Windows or os.system('clear') for Unix-like systems to clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    curses.wrapper(snake_game)
