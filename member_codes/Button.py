    def GravaCSV(self):
        '''Pega nome do cronometro e cria arquivo para guardar as laps'''
        arquivo = str(self.e.get()) + ' - '
        with open(arquivo + self.today + '.txt', 'wb') as lapfile:
            for lap in self.laps:
                lapfile.write((bytes(str(lap) + '\n', 'utf-8')))
            
def main():
    root = Tk()
    root.wm_attributes("-topmost", 1)      #always on top - might do a button for it
    sw = StopWatch(root)
    sw.pack(side=TOP)

    Button(root, text='Lap', command=sw.Lap).pack(side=LEFT)
    Button(root, text='Start', command=sw.Start).pack(side=LEFT)
    Button(root, text='Stop', command=sw.Stop).pack(side=LEFT)
    Button(root, text='Reset', command=sw.Reset).pack(side=LEFT)
    #Button(root, text='Save', command=sw.GravaCSV).pack(side=LEFT)
    #Button(root, text='Quit', command=root.quit).pack(side=LEFT)    
    
    root.mainloop()

if __name__ == '__main__':
    main()