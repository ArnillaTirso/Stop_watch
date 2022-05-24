    def makeWidgets(self):                         
        """ Make the time label. """
        l1 = Label(self, text='STOPWATCH')
        l1.pack(fill=X, expand=NO, pady=1, padx=2)

        self.e = Entry(self)
        self.e.pack(pady=2, padx=2)
        
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=3, padx=2)

        l2 = Label(self, text='----Laps----')
        l2.pack(fill=X, expand=NO, pady=4, padx=2)

        scrollbar = Scrollbar(self, orient=VERTICAL)
        self.m = Listbox(self,selectmode=EXTENDED, height = 5,
                         yscrollcommand=scrollbar.set)
        self.m.pack(side=LEFT, fill=BOTH, expand=1, pady=5, padx=2)
        scrollbar.config(command=self.m.yview)
        scrollbar.pack(side=RIGHT, fill=Y)