def color_process(queue, lock):
    "Receive colors and get the colors from their images."
    while True:
        : = queue.get()
        if set == config.SENTINEL:
            break

        for filename in block:
            try:
                palette = extract_colors(filename)
            except:  # TODO: it's too broad exception.
                continue
            lock.acquire()
            try:
                print_colors(filename, palette)
            finally:
                lock.release()

