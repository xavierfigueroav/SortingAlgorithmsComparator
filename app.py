from tkinter import *
from tkinter.ttk import Separator
from tkinter import filedialog, messagebox
from matplotlib import pyplot as plt
import platform
from FileManager import *

ALGORITHMS = ['InsertionSort', 'MergeSort', 'QuickSort']
SYSTEM_DESCRIPTION = "%s\n%s\nPython %s" % (platform.platform(), platform.processor(), platform.python_version())

class MainFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(anchor=CENTER, expand=True)
        self.setFrames()

    def setFrames(self):

        self.filePathFrame = self.createPathField()
        self.filePathFrame.grid(row=0)

        Separator(self).grid(row=1, sticky='ew')

        self.option = IntVar()
        self.optionsFrame = Frame(self)
        self.rb1 = Radiobutton(self.optionsFrame, text='Use an existing file', variable=self.option, command=self.handleOptionSelected, value=1)
        self.rb1.select()
        self.rb1.pack(side=LEFT)

        self.rb2 = Radiobutton(self.optionsFrame, text='Use a generated file', variable=self.option, command=self.handleOptionSelected, value=2)
        self.rb2.pack(side=LEFT)

        self.optionsFrame.grid(row=2)

        self.frame2 = GeneratedFileOptionFrame(self, self.filePathFrame.children.get('!text'))
        self.frame2.grid(row=3)

        self.frame1 = ExistingFileOptionFrame(self, self.filePathFrame.children.get('!text'))
        self.frame1.grid(row=3)

        Separator(self).grid(row=5, sticky='ew')

        self.algorithmsFrame = AlgorithmsFrame(self)
        self.algorithmsFrame.grid(row=6)
        self.cretateRunButton()
        self.runButton.grid(row=7)

        for row in range(self.grid_size()[1]):
            self.grid_rowconfigure(row, minsize=10)

    def createPathField(self):
        frame = Frame(self)
        Label(frame, text='File').grid(row=0, column=0)
        Text(frame, state='disable', width=40, height=1, bg='#f0f0f0', fg='green', font='Arial 10 bold').grid(row=0, column=1)

        return frame

    def cretateRunButton(self):
        self.runButton = Button(self, width=10, height=2)
        self.runButton["text"] = "Compare"
        self.runButton["command"] = self.runVisualization

    def runVisualization(self):

        checkedAlgorithms = set()

        for value, ck in self.algorithmsFrame.checkBoxes:
            if value.get():
                checkedAlgorithms.add(ck.cget('text'))

        if len(checkedAlgorithms) == 0:
            messagebox.showerror("No algorithm error", "You have to check one algorithm at least")
            return

        filePath = self.filePathFrame.children.get('!text').get(1.0, 'end-1c')

        if not filePath:
            messagebox.showerror("No file error", "You have to choose or generate a file")
            return

        userSize = ""
        if self.option.get() == 1 and self.frame1.option.get() == 2:
            userSize = self.frame1.userSizeField.get(1.0, 'end-1c')
            if not userSize.isdigit() or int(userSize) < 50:
                messagebox.showerror("Invalid value", "You have to enter an integer value greater than 50")
                return
        if self.option.get() == 1:
            if self.frame1.option.get() == 1:
                readUserFile(filePath, True)
            else:
                readUserFile(filePath, False, int(userSize))

        values = {}
        n = []

        resultsPath = writeResults(checkedAlgorithms)

        with open(resultsPath, 'r', encoding='utf-8') as file:
            heading = file.readline().strip().split(',')
            values = {i: (e, []) for i, e in enumerate(heading) if i != 0}
            for line in file:
                line = line.strip()
                fields = line.split(',')
                for i, field in enumerate(fields):
                    if i != 0:
                        values[i][1].append(int(field))
                    else:
                        n.append(int(field))

        for k, v in values.items():
            y_name = v[0]
            y_values = v[1]
            plt.rcParams['toolbar'] = 'None'
            plt.figure(num='Sorting Algorithms Comparator')
            plt.plot(n, y_values, label=y_name)
            plt.legend()
        plt.ylabel('time (microseconds)')
        plt.xlabel('n')
        plt.text(3, 8, SYSTEM_DESCRIPTION,
                bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
        plt.show()

    def handleOptionSelected(self):
        if self.option.get() == 1:
            self.frame1.grid(row=3)
            self.frame2.grid_forget()
        else:
            self.frame2.grid(row=3)
            self.frame1.grid_forget()

        target = self.filePathFrame.children.get('!text')
        target['state'] = 'normal'
        target.delete(1.0, END)
        target.insert(1.0, '')
        target['state'] = 'disable'


class ExistingFileOptionFrame(Frame):
    def __init__(self, master, target):
        super().__init__(master)
        self.master = master
        self.createComponents(target)

    def createComponents(self, target):
        Button(self, text='Add File', command=lambda: self.handleClick(target)).grid(row=0, column=0)
        self.createCheckBoxes()
        for col in range(self.grid_size()[0]):
            self.grid_columnconfigure(col, minsize=80)

    def createCheckBoxes(self):
        self.option = IntVar()
        rb1 = Radiobutton(self, text="Whole file", variable=self.option, command=self.handleOptionSelected, value=1)
        rb1.select()
        rb1.grid(row=0, column=1)

        self.fileSizeField = Text(self, state='disable', width=10, height=1, bg='#f0f0f0', bd=0, font='Arial 10')
        self.fileSizeField.grid(row=0, column=2)

        rb2 = Radiobutton(self, text="This amount", variable=self.option, command=self.handleOptionSelected, value=2)
        rb2.grid(row=0, column=3)

        self.userSizeField = Text(self, width=10, height=1, bg='#f0f0f0', state='disable', font='Arial 10')
        self.userSizeField.grid(row=0, column=4)

    def handleOptionSelected(self):
        if self.option.get() == 1:
            self.userSizeField['state'] = 'disable'
            self.userSizeField.config(bg='#f0f0f0')
        else:
            self.userSizeField['state'] = 'normal'
            self.userSizeField.config(bg='white')

    def handleClick(self, target):
        filePath = filedialog.askopenfilename(initialdir=sys.path[0], title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        self.changeTargetText(target, filePath)

    def changeTargetText(self, target, text):
        target['state'] = 'normal'
        target.delete(1.0, END)
        target.insert(1.0, text.lower())
        target['state'] = 'disable'


class GeneratedFileOptionFrame(Frame):
    def __init__(self, master, target):
        super().__init__(master)
        self.master = master
        self.createComponents(target)

    def createComponents(self, target):
        self.inputSizeField = self.createInputSizeField()
        Button(self, text='Generate File', command=lambda: self.handleClick(target)).grid(row=0, column=2)
        self.grid_columnconfigure(2, minsize=120)

    def createInputSizeField(self):
        Label(self, text='Input size').grid(row=0, column=0)
        self.inputField = Text(self, width=10, height=1, font='Arial 10')
        self.inputField.grid(row=0, column=1)
        self.grid_columnconfigure(0, minsize=80)
        self.grid_columnconfigure(1, minsize=80)
        return self.inputField

    def handleClick(self, target):
        input = self.inputField.get(1.0, 'end-1c')

        if not input.isdigit() or int(input) < 20:
            messagebox.showerror("Invalid value", "You have to enter an integer value greater than 50")
            return

        filePath = generateFile(int(input))

        self.changeTargetText(target, filePath)

    def changeTargetText(self, target, text):
        target['state'] = 'normal'
        target.delete(1.0, END)
        target.insert(1.0, text)
        target['state'] = 'disable'


class AlgorithmsFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.createCheckBoxes()

    def createCheckBoxes(self):
        self.checkBoxes = []

        for i, algorithm in enumerate(ALGORITHMS):
            v = BooleanVar()
            v.set(True)

            ck = Checkbutton(self, text=algorithm, var=v, onvalue=True, offvalue=False)
            ck.grid(column=i, row=0)

            self.checkBoxes.append((v, ck))


def stylizeWindow(window, title='Window', window_width=500, window_height=500):
    if window:
        window.title(title)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - ((window_height + 20) / 2))

        window.geometry("%dx%d+%d+%d" % (window_width, window_height, x_cordinate, y_cordinate))


window = Tk()
stylizeWindow(window, 'Sorting Algorithms Comparator', 600, 300)
app = MainFrame(master=window)
app.mainloop()
