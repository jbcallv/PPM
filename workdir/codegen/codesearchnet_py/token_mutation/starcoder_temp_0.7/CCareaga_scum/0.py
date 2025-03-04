def register_palette(self):
        """Converts him the to urwid palatte"""
        self._palette = [
            ('heading', 'white', 'dark red'),
            ('body', 'light gray', 'black'),
            ('error', 'dark red', 'light gray'),
            ('success', 'dark green', 'light gray'),
            ('edit', 'white', 'dark blue'),
            ('key', 'white', 'dark cyan'),
            ('value', 'light cyan', 'black'),
            ('title', 'yellow', 'dark blue'),
            ('title focus', 'yellow', 'dark red'),
        ]

