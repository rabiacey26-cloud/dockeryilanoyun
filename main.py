import curses
import random

def main(stdscr):
    # İmleci gizle ve giriş bekleme süresini ayarla
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100) # Yılanın hızı (Düşürdükçe hızlanır)

    # Ekran boyutlarını al
    sh, sw = stdscr.getmaxyx()

    # Yılanın başlangıç pozisyonu
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    # İlk yemi oluştur
    food = [sh // 2, sw // 2]
    stdscr.addch(food[0], food[1], curses.ACS_PI)

    # Başlangıç yönü
    key = curses.KEY_RIGHT

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        # Yılanın yeni baş pozisyonunu hesapla
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        # Yeni başı ekle
        snake.insert(0, new_head)

        # Duvara veya kendine çarpma kontrolü
        if (snake[0][0] in [0, sh] or 
            snake[0][1] in [0, sw] or 
            snake[0] in snake[1:]):
            curses.endwin()
            print("Oyun Bitti! Skorun:", len(snake) - 3)
            quit()

        # Yemi yeme kontrolü
        if snake[0] == food:
            food = None
            while food is None:
                # Yeni yem konumu belirle
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake else None
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            # Yem yenmediyse kuyruğun sonunu sil
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        # Yılanın yeni başını çiz
        try:
            stdscr.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
        except curses.error:
            pass

# Curses uygulamasını başlat
curses.wrapper(main)