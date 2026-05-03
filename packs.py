
#All English annotations in this file are machine translated.

import tkinter
import sys
import os
from PIL import Image,ImageTk

if getattr(sys,'frozen',False):
    wcd_path = sys.executable[:sys.executable.rfind('/')] + "/"
if hasattr(sys,"_MEIPASS"):
    wcd_path = f"{sys._MEIPASS}/"
else:
    wcd_path = f"{os.path.dirname(os.path.abspath(__file__))}/"

_icon = {}
_isloaded_image = False
font_size = 12
dpi = 1
int_dpi = 1

def _loadimage():
    global _icon,_isloaded_image,font_size,dpi,int_dpi
    dpi = tkinter._default_root.winfo_screenwidth() / (tkinter._default_root.winfo_screenmmwidth() / 25.4) / 96.0   #_default_root是tkinter隐藏方法，可以获取tkinter.Tk现有的实例   _default_root is a hidden tkinter method, that allows you to get an existing Tk instance
    int_dpi = round(dpi,1)
    _icon = {
        "leftup_bac":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/MDIBAC.png")),
        "rightup_bac":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/MDIBAC.png").transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "leftbottom_bac":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/MDIBAC.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)),
        "rightbottom_bac":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/MDIBAC.png").transpose(Image.Transpose.FLIP_LEFT_RIGHT).transpose(Image.Transpose.FLIP_TOP_BOTTOM)),
        "close_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/CLOSEFOCUSOUT.png")),
        "close_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/CLOSECORE.png")),
        "close_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/CLOSEON.png")),
        "why_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/WHYNORMAL.png")),
        "why_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/WHYCORE.png")),
        "why_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/WHYON.png")),
        "button_lefthead_normal_medium":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADNORMAL.png").resize([int(int_dpi*3),int(int_dpi*23)])),
        "button_righthead_normal_medium":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADNORMAL.png").resize([int(int_dpi*3),int(int_dpi*23)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "button_res_normal_medium":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONRESNORMAL.png").resize([int(int_dpi*1),int(int_dpi*23)])),
        "button_lefthead_core_medium":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADCORE.png").resize([int(int_dpi*3),int(int_dpi*23)])),
        "button_righthead_core_medium":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADCORE.png").resize([int(int_dpi*3),int(int_dpi*23)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "button_res_core_medium":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONRESCORE.png").resize([int(int_dpi*1),int(int_dpi*23)])),
        "button_lefthead_on_medium":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADON.png").resize([int(int_dpi*3),int(int_dpi*23)])),
        "button_righthead_on_medium":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADON.png").resize([int(int_dpi*3),int(int_dpi*23)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "button_res_on_medium":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONRESON.png").resize([int(int_dpi*1),int(int_dpi*23)])),
        "button_lefthead_normal_big":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADNORMAL.png").resize([int(int_dpi*3),int(int_dpi*28)])),
        "button_righthead_normal_big":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADNORMAL.png").resize([int(int_dpi*3),int(int_dpi*28)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "button_res_normal_big":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONRESNORMAL.png").resize([int(int_dpi*1),int(int_dpi*28)])),
        "button_lefthead_core_big":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADCORE.png").resize([int(int_dpi*3),int(int_dpi*28)])),
        "button_righthead_core_big":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADCORE.png").resize([int(int_dpi*3),int(int_dpi*28)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "button_res_core_big":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONRESCORE.png").resize([int(int_dpi*1),int(int_dpi*28)])),
        "button_lefthead_on_big":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADON.png").resize([int(int_dpi*3),int(int_dpi*28)])),
        "button_righthead_on_big":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADON.png").resize([int(int_dpi*3),int(int_dpi*28)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "button_res_on_big":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONRESON.png").resize([int(int_dpi*1),int(int_dpi*28)])),
        "button_lefthead_normal_small":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADNORMAL.png").resize([int(int_dpi*3),int(int_dpi*19)])),
        "button_righthead_normal_small":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADNORMAL.png").resize([int(int_dpi*3),int(int_dpi*19)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "button_res_normal_small":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONRESNORMAL.png").resize([int(int_dpi*1),int(int_dpi*19)])),
        "button_lefthead_core_small":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADCORE.png").resize([int(int_dpi*3),int(int_dpi*19)])),
        "button_righthead_core_small":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADCORE.png").resize([int(int_dpi*3),int(int_dpi*19)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "button_res_core_small":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONRESCORE.png").resize([int(int_dpi*1),int(int_dpi*19)])),
        "button_lefthead_on_small":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADON.png").resize([int(int_dpi*3),int(int_dpi*19)])),
        "button_righthead_on_small":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONHEADON.png").resize([int(int_dpi*3),int(int_dpi*19)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "button_res_on_small":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\BUTTONRESON.png").resize([int(int_dpi*1),int(int_dpi*19)])),
        "prc_lefthead":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\PRCHEAD.png").resize([int(int_dpi*2),int(int_dpi*28)])),
        "prc_righthead":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\PRCHEAD.png").resize([int(int_dpi*2),int(int_dpi*28)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "prc_res":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\PRCRES.png").resize([1,int(int_dpi*28)])),
        "prc_green":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\PRCG.png").resize([1,int(int_dpi*28)])),
        "prc_yellow":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\PRCY.png").resize([1,int(int_dpi*28)])),
        "prc_red":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\PRCR.png").resize([1,int(int_dpi*28)])),
        "prc_blue":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\PRCB.png").resize([1,int(int_dpi*28)])),
        "prc_light_top":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\PRCGR.png").resize([int(int_dpi*127),int(int_dpi*18)])),
        "prc_light_bottom":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\PRCGR.png").resize([int(int_dpi*127),int(int_dpi*18)]).transpose(Image.Transpose.FLIP_TOP_BOTTOM)),
        "tabpage_lefthead_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\TABPAGEHEADNORMAL.png").resize([int(int_dpi*2),int(int_dpi*18)])),
        "tabpage_righthead_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\TABPAGEHEADNORMAL.png").resize([int(int_dpi*2),int(int_dpi*18)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "tabpage_res_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\TABPAGERESNORMAL.png").resize([1,int(int_dpi*18)])),
        "tabpage_lefthead_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\TABPAGEHEADCORE.png").resize([int(int_dpi*2),int(int_dpi*18)])),
        "tabpage_righthead_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\TABPAGEHEADCORE.png").resize([int(int_dpi*2),int(int_dpi*18)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "tabpage_res_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\TABPAGERESCORE.png").resize([1,int(int_dpi*18)])),
        "tabpage_lefthead_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\TABPAGEHEADON.png").resize([int(int_dpi*4),int(int_dpi*20)])),
        "tabpage_righthead_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\TABPAGEHEADON.png").resize([int(int_dpi*4),int(int_dpi*20)]).transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
        "tabpage_res_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\TABPAGERESON.png").resize([1,int(int_dpi*20)])),
        "selection_normal_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\SELECTIONNORMALNORMAL.png").resize([int(int_dpi*13),int(int_dpi*13)])),
        "selection_normal_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\SELECTIONNORMALCORE.png").resize([int(int_dpi*13),int(int_dpi*13)])),
        "selection_normal_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\SELECTIONNORMALON.png").resize([int(int_dpi*13),int(int_dpi*13)])),
        "selection_on_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\SELECTIONONNORMAL.png").resize([int(int_dpi*13),int(int_dpi*13)])),
        "selection_on_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\SELECTIONONCORE.png").resize([int(int_dpi*13),int(int_dpi*13)])),
        "selection_on_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\SELECTIONONON.png").resize([int(int_dpi*13),int(int_dpi*13)])),
        "menu_small":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\MENU.png").resize([14,int(int_dpi*18)])),
        "menu_big":ImageTk.PhotoImage(Image.open(f"{wcd_path}\\assets\\MENU.png").resize([14,int(int_dpi*30)])),
    }
    tkinter._default_root.image = _icon
    _isloaded_image = True

class Button:
    def __init__(self,masterframe,text="",fg="black",font="default",build="medium",width=36,command=None):
        """
        build: 大小（small、medium、big）    build (small,medium or big)
        """
        if not _isloaded_image:
            _loadimage()
        self.master = masterframe
        self.width = width
        self.text = text.strip()
        self.font = font
        self.fg = fg
        self.build = build
        if build == "small":
            self.height = int(int_dpi*19)
        elif build == "medium":
            self.height = int(int_dpi*23)
        elif build == "big":
            self.height = int(int_dpi*28)
        self.frame = tkinter.Canvas(self.master,bg=masterframe.cget("bg"),cursor="hand2",width=self.width,height=self.height,highlightthickness=0,borderwidth=0,relief="flat")

        self.frame.bind("<Enter>",lambda event:self._config_image("core"))
        self.frame.bind("<Leave>",lambda event:self._config_image("normal"))
        self.frame.bind("<ButtonPress-1>",lambda event:self._config_image("on"))
        self.frame.bind("<ButtonRelease-1>",lambda event:self._config_image("core"))
        self.frame.bind("<ButtonRelease-1>",command,add="+")
        self._config_image("normal")
    def _config_image(self,text):
        self.frame.delete(tkinter.ALL)
        self.frame.create_image(0,0,image=_icon[f"button_lefthead_{text}_{self.build}"],anchor=tkinter.NW)
        for num in range(self.width-int(int_dpi*6)):
            self.frame.create_image(num+int(int_dpi*3),0,image=_icon[f"button_res_{text}_{self.build}"],anchor=tkinter.NW)
        self.frame.create_text(self.width//2,self.height//2,text=self.text,font=(self.font,12),fill=self.fg)
        self.frame.create_image(self.width-int(int_dpi*3),0,image=_icon[f"button_righthead_{text}_{self.build}"],anchor=tkinter.NW)


class ProgressBar():
    def __init__(self,masterframe,masterwindow,width=500,mode="green"):
        """
        mode: [绿:"green"、红: "red"、黄: "yellow"、蓝："blue"]
        """
        if not _isloaded_image:
            _loadimage()
        self.master = masterframe
        self.masterwindow = masterwindow
        self.progress = 0
        self.light_progress = -127
        self.mode = mode
        self.width = width
        self.frame = tkinter.Canvas(self.master,width=self.width,height=28,bg=masterframe.cget("bg"),highlightthickness=0,borderwidth=0,relief="flat")
        self.frame.create_image(0,0,image=_icon["prc_lefthead"],anchor=tkinter.NW,tags="head")
        self.frame.create_image(self.width-2,0,image=_icon["prc_righthead"],anchor=tkinter.NW,tags="head")

        self.config_progress(0)
        self.masterwindow.reg_command(self._show_progress_light)
    
    def config_progress(self,progress):
        """
        更改进度条的进度（Tip：不是百分比，而是每个像素）Improve the progress bar's progression (Tip: not as a percentage, but per pixel)
        """
        self.frame.delete("back")
        self.frame.delete("top")
        self.progress = progress
        for num in range(self.progress-4):
            self.frame.create_image(num+2,0,image=_icon[f"prc_{self.mode}"],anchor=tkinter.NW,tags="back")
        for num in range(self.width-4-self.progress):
            self.frame.create_image(self.progress+num+2,0,image=_icon[f"prc_res"],anchor=tkinter.NW,tags="top")
        self.frame.tag_raise("light")
        self.frame.tag_raise("head")

    def config_mode(self,mode):
        """
        更改颜色（只有绿色有滚动效果）Change the color (only green has a scrolling effect)
        ["green","yellow","red","blue"]
        """
        self.mode = mode
    
    def _show_progress_light(self):
        try:
            self.frame.delete("light")
        except:
            pass
        if self.mode != "green":
            self.master.after(15,self._show_progress_light)
            return
        if self.light_progress < self.progress + 127 and not self.progress == 0:
            self.frame.create_image(self.light_progress+2,0,image=_icon["prc_light_top"],anchor=tkinter.NE,tags="light")
            self.frame.create_image(self.light_progress+2,14,image=_icon["prc_light_bottom"],anchor=tkinter.NE,tags="light")
            self.light_progress += 2
            try:
                self.frame.tag_raise("light","back")
                self.frame.tag_lower("light","top")
            except:
                pass
        else:
            self.light_progress = -127

class Edit:
    def __init__(self,masterframe,font="default",fg="black",show_char="",charwidth=16):
        """
        charwidth: 可容纳的字符长度（是len不是width）Maximum character length (it's len, not width)
        """
        if not _isloaded_image:
            _loadimage()
        self.frame = tkinter.Canvas(masterframe,bg=masterframe.cget("bg"),width=charwidth*int(int_dpi*18)+4,height=int(int_dpi*18),highlightthickness=0,borderwidth=0,relief="flat")
        self.frame.create_rectangle(2,0,charwidth*int(int_dpi*18)+4,14,fill="#ABADB3",width=0)
        self.entry = tkinter.Entry(self.frame,font=(font,12),bg="white",width=charwidth,fg=fg,show=show_char,relief="flat")
        self.entry.pack(padx=(2,2),pady=(2,2))
    
    def get(self):
        return self.entry.get().strip()

    def delete(self,first,last):
        self.entry.delete(first,last)

    def insert(self,index,char):
        self.entry.insert(index,char)

class Text:
    def __init__(self,masterframe,font="default",fg="black",charwidth=16,charheight=10):
        """
        charwidth: 可容纳的字符长度（是len不是width） Maximum character length (it's len, not width)
        charheight: 同上        See up
        """
        if not _isloaded_image:
            _loadimage()
        self.frame = tkinter.Canvas(masterframe,bg=masterframe.cget("bg"),width=charwidth*int(int_dpi*18)+4,height=charheight*int(int_dpi*18)+4,highlightthickness=0,borderwidth=0,relief="flat")
        self.frame.create_rectangle(2,0,charwidth*int(int_dpi*18)+4,charheight*18-4,fill="#ABADB3",width=0)
        self.text = tkinter.Text(self.frame,font=(font,12),width=charwidth,height=charheight,bg="white",fg=fg,relief="flat")
        self.text.pack(padx=(2,2),pady=(2,2))
    
    def get(self):
        return self.text.get(1.0,tkinter.END).strip()

    def delete(self,first,last):
        self.text.delete(first,last)

    def insert(self,index,char):
        self.text.insert(index,char)

class ListBox:
    def __init__(self,masterframe,font="default",fg="black",select_many=False,width=16,height=10):
        """
        height: 列表的项目（依旧len不是width）Items in the list (still len, not width)
        select_many: 是否允许多选   Do multiple selections allow
        """
        if not _isloaded_image:
            _loadimage()
        if select_many:
            select_many = tkinter.SINGLE
        else:
            select_many = tkinter.EXTENDED
        self.frame = tkinter.Canvas(masterframe,bg=masterframe.cget("bg"),width=width*int(int_dpi*18)+4,height=height*int(int_dpi*18)+4,highlightthickness=0,borderwidth=0,relief="flat")
        self.frame.create_rectangle(2,0,width*int(int_dpi*18)+4,height*int(int_dpi*18)-4,fill="#ABADB3",width=0)
        self.list = tkinter.Listbox(self.frame,font=(font,12),width=width,height=height,selectmode=select_many,bg="white",fg=fg,relief="flat")
        self.list.pack(padx=(2,2),pady=(2,2))

    def delete_many(self,first,last):
        self.list.delete(first,last)

    def delete_one(self,len):
        self.list.delete(len)

    def insert(self,index,char):
        self.list.insert(index,char)    
        
    def get_select(self):   
        return self.list.curselection() 
    
    def get_text(self,cur): 
        return self.list.get(cur)   
    
class TabPage:  
    def __init__(self,masterframe,masterwindow,tabs=[],pags=[],width=350,height=250):   
        """
        tabs: 标签（文字）        Label (char)
        pags: 页（组件）         Pages (pack)
        Tip: tabs与pages的长度要对齐     The length of tabs and pages should be aligned
        """
        if not _isloaded_image: 
            _loadimage()    
        self.masterwindow = masterwindow    
        self.tabs = tabs    
        self.pages = pags   
        self.width = width  
        self.height = height    
        self.image = dict.fromkeys(tabs,"normal")
        self.frame = tkinter.Canvas(masterframe,bg=masterframe.cget("bg"),width=self.width,height=height,highlightthickness=0,borderwidth=0,relief="flat")
        calc = 2
        for tab in self.tabs:
            self.frame.create_image(calc,int(int_dpi*20),image=_icon[f"tabpage_lefthead_{self.image[tab]}"],anchor=tkinter.S,tags=f"{tab}_lefthead")
            for num in range(len(tab)*18):
                self.frame.create_image(int(int_dpi*(num+calc+2)),int(int_dpi*20),image=_icon[f"tabpage_res_{self.image[tab]}"],anchor=tkinter.S,tags=tab)
            self.frame.create_text(int(int_dpi*(num//2+calc)),int(int_dpi*10),text=tab,tags=f"{tab}_text")
            self.frame.create_image(int(int_dpi*(num+calc+2)),int(int_dpi*20),image=_icon[f"tabpage_righthead_{self.image[tab]}"],anchor=tkinter.S,tags=f"{tab}_righthead")
            calc += num + 2
        self.frame.create_rectangle(0,int(int_dpi*20),self.width-1,self.height-1,fill="",outline="#898C95",width=2)
        self._config_image(tabs[0],"on")
        self._tag_binds()
        self.masterwindow.reg_command(self._place)
    
    def _renden(self,item,image):
        for items in self.frame.find_withtag(item):
            self.frame.itemconfig(items,image=_icon[f"tabpage_res_{image}"])
        self.frame.itemconfig(f"{item}_lefthead",image=_icon[f"tabpage_lefthead_{image}"])
        self.frame.itemconfig(f"{item}_righthead",image=_icon[f"tabpage_righthead_{image}"])
    
    def _config_image(self,key,image):
        if self.image[key] == "on":
            return
        if image == "on":
            for page in self.pages:
                page.pack_forget()
                page.place_forget()
                page.grid_forget()
            for tab in self.tabs:
                self.image[tab] = "normal"
                self._renden(tab,"normal")
        self.image[key] = image
        self._renden(key,image)
        if image == "on":
            page = self.pages[self.tabs.index(key)]
            page.place(x=self.frame.winfo_x()+2,y=self.frame.winfo_y()+20)
            page.tk.call("raise",page)
    
    def _place(self):
        for key,value in self.image.items():
            if value == "on":
                page = self.pages[self.tabs.index(key)]
                page.place(x=self.frame.winfo_x()+2,y=self.frame.winfo_y()+18)
                page.tk.call("raise",page)
    
    def _raise(self,key):
        self.frame.tag_raise(key)
        self.frame.tag_raise(f"{key}_lefthead")
        self.frame.tag_raise(f"{key}_righthead")
        self.frame.tag_raise(f"{key}_text")

    def _tag_binds(self):
        for tag in self.tabs:
            self.frame.tag_bind(tag,"<Enter>",lambda event,ta=tag:self._config_image(str(ta),"core"))
            self.frame.tag_bind(tag,"<Leave>",lambda event,ta=tag:self._config_image(str(ta),"normal"))
            self.frame.tag_bind(tag,"<ButtonPress-1>",lambda event,ta=tag:[self._config_image(str(ta),"on"),self._raise(ta)])
            self.frame.tag_bind(f"{tag}_text","<Enter>",lambda event,ta=tag:self._config_image(str(ta),"core"))
            self.frame.tag_bind(f"{tag}_text","<Leave>",lambda event,ta=tag:self._config_image(str(ta),"normal"))
            self.frame.tag_bind(f"{tag}_text","<ButtonPress-1>",lambda event,ta=tag:self._config_image(str(ta),"on"))

class Frame:
    def __init__(self,masterframe,text,width=350,height=350):
        if not _isloaded_image:
            _loadimage()
        self.frame = tkinter.Canvas(masterframe,bg=masterframe.cget("bg"),width=width,height=height+15,highlightthickness=0,borderwidth=0)
        self.frame.create_rectangle(2,int(int_dpi*10),width,height,fill="",outline="#898C95",width=2)
        self.frame.create_rectangle(int(int_dpi*22),int(int_dpi*5),len(text)*int(int_dpi*14),int(int_dpi*20),fill="white",width=0,)
        self.frame.create_text(int(int_dpi*28),int(int_dpi*10),text=text,fill="black",anchor=tkinter.W)

        self.main = tkinter.Frame(self.frame,bg=masterframe.cget("bg"))
        self.frame.create_window(int(int_dpi*6),int(int_dpi*24),window=self.main,width=width-10,height=height-28,anchor=tkinter.NW)

class Selection:
    def __init__(self,masterframe,text,fg="black",default=False):
        if not _isloaded_image:
            _loadimage()
        self.state = default
        self.frame = tkinter.Canvas(masterframe,bg="white",width=len(text)*int(int_dpi*12),height=int(int_dpi*17),highlightthickness=0,borderwidth=0)
        if not default:
            self.frame.create_image(int(int_dpi*2),int(int_dpi*2),image=_icon["selection_normal_normal"],anchor=tkinter.NW,tags="selection")
        elif default:
            self.frame.create_image(int(int_dpi*2),int(int_dpi*2),image=_icon["selection_on_normal"],anchor=tkinter.NW,tags="selection")
        self.frame.create_text(15,1,text=text,fill=fg,anchor=tkinter.NW)
        self.frame.bind("<Enter>",lambda event:[self._config("core")])
        self.frame.bind("<Leave>",lambda event:[self._config("normal")])
        self.frame.bind("<ButtonPress-1>",lambda event:[self._config("on")])
        self.frame.bind("<ButtonRelease-1>",lambda event:[self._restate(),self._config("core")])
    def _config(self,image):
        if self.state:
            self.frame.itemconfig("selection",image=_icon[f"selection_on_{image}"])
        elif not self.state:
            self.frame.itemconfig("selection",image=_icon[f"selection_normal_{image}"])
        
    def _restate(self):
        if self.state:
            self.state = False
        elif not self.state:
            self.state = True

class MainMenu:
    def __init__(self,masterframe,masterwindow,build="small"):
        if not _isloaded_image:
            _loadimage()
        self.masterframe = masterframe
        self.build = build
        if self.build == "small":
            self.height = 9
        else:
            self.height = 15
        self.char = []
        self.command = []
        self.x = []
        self.frame = tkinter.Canvas(masterframe,bg=masterframe.cget("bg"),height=self.height*2,highlightthickness=0,borderwidth=0)
        self.frame.place(x=0,y=0)
        masterwindow.reg_command(self._renden)

    def add_menu(self,label,menu):
        """
        加入一个菜单到主菜单       Append a menu to main menu
        label: 显示的文字   Show the char.
        menu: 添加的菜单    Append the menu.
        """
        self.char.append(str(label))
        self.command.append(menu)
    
    def _renden(self):
        self.frame.delete(tkinter.ALL)
        self.frame.config(width=self.masterframe.winfo_width())
        for num in range(self.masterframe.winfo_width()//14+1):
            self.frame.create_image(num*14,0,image=_icon[f"menu_{self.build}"],anchor=tkinter.NW,tags="bg")
        textup = 0
        self.x = []
        for textnum in range(len(self.char)):
            self.frame.create_text(textup+int(int_dpi*len(self.char[textnum])*18)//2,self.height,text=self.char[textnum],fill="#000000",tag=f"text_{textnum}")
            self.x.append(textup)
            self.frame.tag_bind(f"text_{textnum}","<ButtonPress>",lambda event,textnum=textnum:self.command[textnum].post(self.masterframe.winfo_rootx()+self.x[textnum],self.masterframe.winfo_rooty()+self.height*2))
            textup += int(int_dpi*len(self.char[textnum])*18)
        

class MDIWindow:
    def __init__(self,masterframe,masterwindow,can_resize=True,whybut=False,image=None,title="",x=0,y=0,width=100,height=75,min_width=0,min_height=0,why_command=None):
        self.whybut = whybut
        self.can_resize = can_resize
        self.title_str = title
        self.masterwindow = masterwindow
        self.var = {
            "x":0,
            "y":0,
            "w":0,
            "h":0,
            "start_x":0,
            "start_y":0,
            "win_x":0,
            "win_y":0,
            "resize_start_x":0,
            "resize_start_y":0,
            "resize_start_width":0,
            "resize_start_height":0,
            "resize_start_win_x":0,
            "resize_start_win_y":0,
            "resize_mode":None,
            "can_drag":True,
            "is_resizing":False,
            "is_configing_glass":False,
            "enter_why":False,
            "enter_close":False
        }
        self.min_width = max(190,min_width)
        self.min_height = max(37,min_height)
        self.w = tkinter.Frame(masterframe,bg=masterframe.cget("bg"),highlightthickness=0,borderwidth=0)
        self.w.place(x=x,y=y,width=width,height=height)
        self.bar = tkinter.Canvas(self.w,bg="#C5D5E2",highlightthickness=0,borderwidth=0)
        if not image is None:
            self.icon = {
                "icon":Image.open(image),
                "icon_16x16":ImageTk.PhotoImage(Image.open(image).resize([16,16]))
            }
        else:
            self.icon = {
                "icon":Image.open(f"{wcd_path}assets/DEFAULT.ico"),
                "icon_16x16":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/DEFAULT.ico").resize([16,16]))
            }
        
        self.root = tkinter.Frame(self.w,bg="#FFFFFF")

        self.bar.create_image(6,6,image=self.icon["icon_16x16"],anchor=tkinter.NW)
        self.bar.create_text(12,6,text=self.title_str,anchor=tkinter.NW)
        self.bar.tag_bind("close","<Enter>",lambda event:[self.bar.itemconfig("close",image=_icon["close_core"]),self.set_var("close",True)])
        self.bar.tag_bind("close","<Leave>",lambda event:[self.bar.itemconfig("close",image=_icon["close_normal"]),self.set_var("close",False)])
        self.bar.tag_bind("close","<ButtonPress-1>",lambda event:[self.bar.itemconfig("close",image=_icon["close_on"]),self.masterwindow.unreg_command(self._config_glass),self.w.destroy()])
        
        self.bar.tag_bind("why","<Enter>",lambda event:[self.bar.itemconfig("why",image=_icon["why_core"]),self.set_var("why",True)])
        self.bar.tag_bind("why","<Leave>",lambda event:[self.bar.itemconfig("why",image=_icon["why_normal"]),self.set_var("why",False)])
        self.bar.tag_bind("why","<ButtonPress-1>",lambda event:[self.bar.itemconfig("why",image=_icon["why_on"]),why_command()])
         
        self.bar.bind("<ButtonPress-1>",self._drag)
        self.bar.bind("<B1-Motion>",self._drag)
        self.bar.bind("<ButtonRelease-1>",self._drag)

        if self.can_resize:
            self.bar.bind("<Motion>",self._set_cursor)
            self.bar.bind("<ButtonPress-1>",self._start_resize,add="+")
            self.bar.bind("<B1-Motion>",lambda event:self._do_resize(event,min_width,min_height),add="+")
            self.bar.bind("<ButtonRelease-1>",self._end_resize,add="+")

        self.masterwindow.reg_command(self._config_glass)
    
    def set_var(self,var,value):
        if var == "close":
            self.var["enter_close"] = value
        elif var == "why":
            self.var["enter_why"] = value

    def _config_glass(self):
        self.var["is_configing_glass"] = True
        if self.w.winfo_x() != self.var["x"] or self.w.winfo_y() != self.var["y"] or self.w.winfo_width() != self.var["w"] or self.w.winfo_height() != self.var["h"]:
            self.bar.delete(tkinter.ALL)
            self.bar.place(x=0,y=0,width=self.w.winfo_width(),height=self.w.winfo_height())
            self.root.place(x=7,y=29,width=self.w.winfo_width()-14,height=self.w.winfo_height()-36)
            self.bar.create_image(6,6,image=self.icon["icon_16x16"],anchor=tkinter.NW)
            self.bar.create_text(24,6,text=self.title_str,anchor=tkinter.NW)
            
            self.bar.create_image(0,0,image=_icon["leftup_bac"],anchor=tkinter.NW)
            self.bar.create_image(self.w.winfo_width()-7,0,image=_icon["rightup_bac"],anchor=tkinter.NW)
            self.bar.create_image(0,self.w.winfo_height()-7,image=_icon["leftbottom_bac"],anchor=tkinter.NW)
            self.bar.create_image(self.w.winfo_width()-7,self.w.winfo_height()-7,image=_icon["rightbottom_bac"],anchor=tkinter.NW)

            self.bar.create_image(self.w.winfo_width()-56,0,image=_icon["close_normal"],anchor=tkinter.NW,tags="close")
            if self.whybut:
                self.bar.create_image(self.w.winfo_width()-85,0,image=_icon["why_normal"],anchor=tkinter.NW,tags="why")
            
        self.var["is_configing_glass"] = False

    def _drag(self,event):
        if self.var["is_resizing"] or self.var["enter_close"] or self.var["enter_why"]:
            return
        self.w.lift()
        if event.type == tkinter.EventType.ButtonPress:
            if not self.var["is_resizing"] and self.var["resize_mode"] is None and event.y <= 29:
                self.var["start_x"] = event.x_root
                self.var["start_y"] = event.y_root
                self.var["win_x"] = self.w.winfo_x()
                self.var["win_y"] = self.w.winfo_y()
                self.var["can_drag"] = True
            else:
                self.var["can_drag"] = False
        elif event.type == tkinter.EventType.Motion and self.var["can_drag"]:
            dx = event.x_root - self.var["start_x"]
            dy = event.y_root - self.var["start_y"]
            self.w.place(x=self.var['win_x'] + dx,y=self.var['win_y'] + dy)
        elif event.type == tkinter.EventType.ButtonRelease:
            self.var["can_drag"] = False
    def _set_cursor(self,event):
        if event.widget != self.bar or self.var["enter_close"] or self.var["enter_why"]:
            self.var["resize_mode"] = None
            self.w.config(cursor="arrow")
            return
        if self.var["is_resizing"]:
            return

        self.var["resize_mode"] = None
        self.w.config(cursor="arrow")

        width = self.w.winfo_width()
        height = self.w.winfo_height()
        x,y = event.x,event.y
        bo_width = 7
        
        if x < bo_width and y < bo_width:
            self.var["resize_mode"] = "nw"
            self.w.config(cursor="size_nw_se")
        elif x > width - bo_width and y < bo_width and x < width and y >=0:
            self.var["resize_mode"] = "ne"
            self.w.config(cursor="size_ne_sw")
        elif x < bo_width and y > height - bo_width and x >=0 and y < height:
            self.var["resize_mode"] = "sw"
            self.w.config(cursor="size_ne_sw")
        elif x > width - bo_width and y > height - bo_width and x < width and y < height:
            self.var["resize_mode"] = "se"
            self.w.config(cursor="size_nw_se")
        elif x < bo_width and x >=0:
            self.var["resize_mode"] = "w"
            self.w.config(cursor="size_we")
        elif x > width - bo_width and x < width:
            self.var["resize_mode"] = "e"
            self.w.config(cursor="size_we")
        elif y < bo_width and y >=0:
            self.var["resize_mode"] = "n"
            self.w.config(cursor="size_ns")
        elif y > height - bo_width and y < height:
            self.var["resize_mode"] = "s"
            self.w.config(cursor="size_ns")

    def _start_resize(self,event):
        if self.var["resize_mode"] is not None:
            self.var["is_resizing"] = True
            self.var["resize_start_x"] = event.x_root
            self.var["resize_start_y"] = event.y_root
            self.var["resize_start_width"] = self.w.winfo_width()
            self.var["resize_start_height"] = self.w.winfo_height()
            self.var["resize_start_win_x"] = self.w.winfo_x()
            self.var["resize_start_win_y"] = self.w.winfo_y()

    def _do_resize(self,event,min_width,min_height):
        if not self.var["is_resizing"] or self.var["enter_close"] or self.var["enter_why"]:
            return
        self.w.lift()
        dx = event.x_root - self.var["resize_start_x"]
        dy = event.y_root - self.var["resize_start_y"]
        
        new_width = self.var["resize_start_width"]
        new_height = self.var["resize_start_height"]
        new_x = self.var["resize_start_win_x"]
        new_y = self.var["resize_start_win_y"]
        
        min_width,min_height = min_width,min_height

        if self.var["resize_mode"] == "e":
            new_width = max(min_width,self.var["resize_start_width"] + dx)
            new_x = self.var["resize_start_win_x"]
        elif self.var["resize_mode"] == "w":
            new_width = max(min_width,self.var["resize_start_width"] - dx)
            new_x = min(self.var["resize_start_win_x"] + dx,self.var["resize_start_win_x"] + (self.var["resize_start_width"] - min_width))
        elif self.var["resize_mode"] == "s":
            new_height = max(min_height,self.var["resize_start_height"] + dy)
            new_y = self.var["resize_start_win_y"]
        elif self.var["resize_mode"] == "n":
            new_height = max(min_height,self.var["resize_start_height"] - dy)
            new_y = min(self.var["resize_start_win_y"] + dy,self.var["resize_start_win_y"] + (self.var["resize_start_height"] - min_height))
        elif self.var["resize_mode"] == "ne":
            new_width = max(min_width,self.var["resize_start_width"] + dx)
            new_height = max(min_height,self.var["resize_start_height"] - dy)
            new_y = min(self.var["resize_start_win_y"] + dy,self.var["resize_start_win_y"] + (self.var["resize_start_height"] - min_height))
            new_x = self.var["resize_start_win_x"]
        elif self.var["resize_mode"] == "nw":
            new_width = max(min_width,self.var["resize_start_width"] - dx)
            new_height = max(min_height,self.var["resize_start_height"] - dy)
            new_x = min(self.var["resize_start_win_x"] + dx,self.var["resize_start_win_x"] + (self.var["resize_start_width"] - min_width))
            new_y = min(self.var["resize_start_win_y"] + dy,self.var["resize_start_win_y"] + (self.var["resize_start_height"] - min_height))
        elif self.var["resize_mode"] == "se":
            new_width = max(min_width,self.var["resize_start_width"] + dx)
            new_height = max(min_height,self.var["resize_start_height"] + dy)
            new_x = self.var["resize_start_win_x"]
            new_y = self.var["resize_start_win_y"]
        elif self.var["resize_mode"] == "sw":
            new_width = max(min_width,self.var["resize_start_width"] - dx)
            new_height = max(min_height,self.var["resize_start_height"] + dy)
            new_x = min(self.var["resize_start_win_x"] + dx,self.var["resize_start_win_x"] + (self.var["resize_start_width"] - min_width))
            new_y = self.var["resize_start_win_y"]
        self.w.place(x=new_x,y=new_y,width=max(max(min_width,new_width),self.min_width),height=max(max(min_height,new_height),self.min_height))

    def _end_resize(self,event):
        self.var["is_resizing"] = False