import tkinter as tk
from tkinter.ttk import *
import sv_ttk
import darkdetect

import document_gui

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", foreground='grey'):
        super().__init__(master)

        self.default_fg_color = self['foreground']
        self.placeholder = placeholder
        self.placeholder_color = foreground

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(foreground=self.placeholder_color)

    def foc_in(self, *args):
        if str(self.cget('foreground')) == str(self.placeholder_color):
            self.delete('0', 'end')
            self.config(foreground=self.default_fg_color)

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


class APP:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Python Office")
        sv_ttk.set_theme(darkdetect.theme())

        self.Home()
        self.Tabs()
        self.DocumentFrame()

        self.root.mainloop()

    def Home(self):
        # 标题区
        self.Title_Label = tk.Label(self.root, text="Python Office", font=("Arial", 24), justify="center")
        self.Title_Label.pack(fill=tk.X, ipady=20, side=tk.TOP, anchor=tk.N)
        
    
    def Tabs(self):
        # 创建 Notebook 控件
        self.Tabs = Notebook(self.root)
        self.Files = Frame(self.Tabs)
        
        self.WechatTab = Frame(self.Tabs)

        self.AutoTab = Frame(self.Tabs)

        self.Tabs.add(self.Files, text="Files")
        self.Tabs.add(self.WechatTab, text="WeChat")
        self.Tabs.add(self.AutoTab, text="Auto")
        
        self.Tabs.pack(fill=tk.BOTH, pady = 5, side=tk.TOP, anchor=tk.N, expand=True)
        

    def DocumentFrame(self):
        self.MergeDoc_Frame = Frame(self.Files)

        self.MergeDoc_Input_Frame = Frame(self.MergeDoc_Frame)
        self.MergeDoc_Input_Entry = EntryWithPlaceholder(self.MergeDoc_Input_Frame, "Input Path or File")
        self.MergeDoc_Input_Button = Button(self.MergeDoc_Input_Frame, text="Open", style="Accent.TButton")

        self.MergeDoc_Output_Frame = Frame(self.MergeDoc_Frame)
        self.MergeDoc_Output_Entry = EntryWithPlaceholder(self.MergeDoc_Output_Frame, "Output Path or File")
        self.MergeDoc_Output_Button = Button(self.MergeDoc_Output_Frame, text="Open", style="Accent.TButton")

        self.MergeDoc_Input_Frame.pack(fill=tk.X, padx=10, pady=5, anchor=tk.N, side=tk.TOP)
        self.MergeDoc_Output_Frame.pack(fill=tk.X, padx=10, pady=5, anchor=tk.N, side=tk.TOP)

        self.MergeDoc_Input_Entry.pack(fill=tk.X, padx=10, pady=5, anchor=tk.CENTER, expand=True, side=tk.LEFT)
        self.MergeDoc_Input_Button.pack(fill=tk.X, padx=10, pady=5, anchor=tk.CENTER, expand=True, side=tk.LEFT)
        self.MergeDoc_Output_Entry.pack(fill=tk.X, padx=10, pady=5, anchor=tk.CENTER, expand=True, side=tk.LEFT)
        self.MergeDoc_Output_Button.pack(fill=tk.X, padx=10, pady=5, anchor=tk.CENTER, expand=True, side=tk.LEFT)
        self.MergeDoc_Frame.pack(fill=tk.BOTH, padx=20, pady=5, anchor=tk.CENTER, expand=True, side=tk.TOP)

    def Run(self):
        # 运行主循环
        self.root.mainloop()




if __name__ == "__main__":
    APP()
    document_gui.Document()