from home import *
def Document(APP):
    def __init__(self, root, Tabs):
        super(Document, self).__init__(root, Tabs)

        self.DocumentTab_Label =  Label(self.DocumentTab, self.DocumentTab, text="Document Tab")
        self.DocumentTab_Label.pack(fill=tk.X, ipady=20, side=tk.TOP, anchor=tk.N)
        self.root.update()
        