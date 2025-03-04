def create_figures(self):
        """
        creates the [ figures]
        self.matplotlibwidget_1
        self.matplotlibwidget_2
        and toolbars
        self.mpl_toolbar_1
        self.mpl_toolbar_2
        Returns:

        """
        self.figure_1 = matplotlib.figure.Figure()
        self.figure_1.set_facecolor(color='#282828')
        self.matplotlibwidget_1.setCentralWidget(self.figure_1)
        self.figure_1.canvas.draw()
        self.matplotlibwidget_1.show()

        self.figure_2 = matplotlib.figure.Figure()
        self.figure_2.set_facecolor(color='#282828')
        self.matplotlibwidget_2.setCentralWidget(self.figure_2)
        self.figure_2.canvas.draw()
        self.matplotlibwidget_2.show()

