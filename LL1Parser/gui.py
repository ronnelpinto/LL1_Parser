from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as box
from firstfollow import *

fileptr = [False, 0]

class MainWIndow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='#eed')
        self.parent = parent
        self.initUI()
        self.initQuitButton()
        self.initFileButton()
        self.initInputText()
        self.initOutputText()
        self.initLabels()
        self.initGenerateButton()
        self.initInfoLabel()
        
    def initUI(self):        
        self.parent.title('LL1 PARSER')
        self.pack(fill=BOTH, expand=1)
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.parent.geometry('500x500+%d+%d' % ((sw - 500)/2, (sh - 500)/2))
        
    def initQuitButton(self):
        quitButton = Button(self, text = "Quit", command = self.quit)
        quitButton.place(relx = 0.8, rely = 0.93, relwidth = 0.1)
        
    def initGenerateButton(self):
        genButton = Button(self, text = "Generate table", command = self.invokeParser)
        genButton.place(relx = 0.32, rely = 0.93, relwidth = 0.2)
        
    def initFileButton(self):
        fileButton = Button(self, text = "Select Input", command = self.onOpen)
        fileButton.place(relx = 0.08, rely = 0.93, relwidth = 0.2)
        
    def initInputText(self, textParam=''):
        self.inputText = Text(self)
        self.inputText.place(relx = 0.08, rely = 0.07, relwidth = 0.7, relheight = 0.25)
        self.inputText.insert(index = INSERT, chars = textParam)
                
    def initLabels(self):
        l1 = Label(self, text = "Input Grammar", background='#eed')
        l2 = Label(self, text = "Output Parsing Table", background='#eed')        
        l1.place(relx = 0.2, rely = 0.02, relwidth = 0.3)
        l2.place(relx = 0.2, rely = 0.35, relwidth = 0.3)
                
    def initInfoLabel(self, textParam = "Information: ", flag = 1):
        if flag is 1:
            l3 = Label(self, text = textParam, background='#3f3')
        else:
            l3 = Label(self, text = textParam, background='#a77')
        l3.place(relx = 0.79, rely = 0.1, relwidth = 0.2)    
        
    def initOutputText(self, textParam=''):
        self.outputText = Text(self)
        self.outputText.place(relx = 0.08, rely = 0.4, relwidth = 0.7, relheight = 0.50)
        self.outputText.insert(index = INSERT, chars = textParam)
        
    def onOpen(self):      
        filename = filedialog.askopenfilename()
        if filename is '':
            box.showinfo("Info", "You did not select a file.")
        else:
            global fileptr
            fileptr[0] = True
            fileptr[1] = filename
            f = open(fileptr[1], 'r')
            self.text = f.read()
            self.text = self.text.split('\n')
            displayText = ''
            for i in range(len(self.text)):
                displayText += (self.text[i] + '\n')
            self.initInputText(displayText)    
            #print(displayText) #testing #success                 
            #for i in text: #testing #success
                #print(i)       #testing
        
    def invokeParser(self):
        #call to generateparser code module

        parsingtable = createparser(self.inputText.get( '0.0', END)) 
        
        outputText = ''
        
        #print("---"*40)
        outputText +="---"*35
        for i in parsingtable:
            outputText +="\n "
            for j in parsingtable[i]:
                for k in parsingtable[i][j]:
                
                    outputText += "[ "+i+ ","+j+ " ]" "::" +k+ ' '
            outputText +="\n " 
            outputText +="---"*35
            #print("")
            #print("---"*40)
            #outputText += (parsingtable[i] + '\n')                
        print('outputText:', outputText)
        self.initOutputText(outputText)
        infoString = 'Success!\nThe parsing\ntable has been\nsuccessfully\ncreated' 
        self.initInfoLabel(infoString, flag = 1)
                    
    
def main():
    root = Tk()
    app = MainWIndow(root)
    root.mainloop()
