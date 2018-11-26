from tkinter import *
from tkinter import filedialog, Frame
from matplotlib import pyplot as plt
from random import randint

ALGORITHMS = ['InsertionSort', 'MergeSort', 'QuickSort', 'StoogeSort']


class MainLayout(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.setFrames()

    def setFrames(self):
        self.fileFrame = FileFrame(self)
        self.algorithmsFrame = AlgorithmsFrame(self)
        self.fileFrame.pack()
        self.fileFrame.pack()
        self.cretateRunButton()
        self.runButton.pack()

    def cretateRunButton(self):
        self.runButton = Button(self, width=10, height=2)
        self.runButton["text"] = "Run"
        self.runButton["command"] = self.runVisualization

    def runVisualization(self):
        # plot test
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
        plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
        plt.show()


class FileFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.createPathField()
        self.createPathButton()
        self.createGenerateButton()

    def createPathField(self):
        self.pathField = Text(self, state='disable', width=50, height=2)
        self.pathField.grid(row=0)
        self.pathField.grid(column=0)

    def createPathButton(self):
        self.pathButton = Button(self, width=10, height=2)
        self.pathButton["text"] = "Add file"
        self.pathButton["command"] = self.askForFile
        self.pathButton.grid(row=0)
        self.pathButton.grid(column=1)

    def askForFile(self):
        self.filePath = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        self.pathField['state'] = 'normal'
        self.pathField.delete(INSERT, END)
        self.pathField.insert(INSERT, self.filePath)
        self.pathField['state'] = 'disable'

    def createGenerateButton(self):
        self.pathButton = Button(self, width=10, height=2)
        self.pathButton["text"] = "Generate File"
        self.pathButton["command"] = self.generateFile
        self.pathButton.grid(row=0)
        self.pathButton.grid(column=2)

    def generateFile(self):
        with open('generated.txt', 'w', encoding='utf-8') as file:
            for i in range(100):
                file.write("%d\n" % randint(-100,100))


class AlgorithmsFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.createCheckBoxes()

    def createCheckBoxes(self):
        self.checkboxes = []

        for i, algorithm in enumerate(ALGORITHMS):
            check = Checkbutton(self, text=algorithm)
            check.grid(row=0)
            check.grid(column=i)
            self.checkboxes.append(check)


window = Tk()
app = MainLayout(master=window)
app.mainloop()