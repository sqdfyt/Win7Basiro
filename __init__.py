
#All English annotations in this file are machine translated.

import tkinter
import pyautogui
import os
from random import randint
from platform import release
from PIL import Image,ImageTk,ImageFilter
from .packs import *             #需要作为库使用，否则需要改成“from packs import *”   It needs to be used as a library, otherwise it should be changed to "from packs import *"

__name__ = "Win7Basiro"
__version__ = "1.4"
__author__ = "Fyuter"
__all__ = ["wcd_path","Window","Messagebox","all_stop","main",
           "Button","ProgressBar","Entry","Text","ListBox","TabPage","Frame","Selection","MainMenu","MDIWindow"]

main_window = tkinter.Tk()
main_window.withdraw()

window_num = 0
dpi = main_window.winfo_screenwidth() / (main_window.winfo_screenmmwidth() / 25.4) / 96.0
int_dpi = round(dpi,1)
lib_bar = int(int_dpi*40)
if release() == "11":
    lib_bar = int(int_dpi*60)
_setting = {
    "BORADCOLORFOCUSIN":"#94C2EB",
    "BORADCOLORFOCUSOUT":"#E6E6E6",
    "CONTRASTCOLOR":"#000000",
    "ROOTCOLOR":"white"
}
if not os.path.isfile(".\\config.ops"):
    with open(".\\config.ops","w",encoding="utf-8") as file:
        file.write("BORADCOLORFOCUSIN=#BAD9FF\nBORADCOLORFOCUSOUT=#E6E6E6\nCONTRASTCOLOR=#000000\nROOTCOLOR=white\n")

with open(".\\config.ops","r",encoding="utf-8") as file:
    ops = file.readlines()
    for s in ops:
        key,value = s.split('=')
        _setting[key] = str(value).strip()
_icon = {
    "border_0":Image.open(f"{wcd_path}assets/BACKICO.png").convert("RGBA").resize((pyautogui.size()[0],pyautogui.size()[1]),Image.Resampling.LANCZOS),
    "light_7":Image.open(f"{wcd_path}assets/LIGHT.png").convert("RGBA").resize([int(int_dpi*7),int(int_dpi*6)]),
    "trans_parent_552":Image.open(f"{wcd_path}assets/TRANSPARENT.png").resize([int(int_dpi*552),int(int_dpi*116)]),
    "trans_parent":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/TRANSPARENT.png").resize([int(int_dpi*552),int(int_dpi*116)])),
    "leftup_bac":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/BAC.png")),
    "rightup_bac":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/BAC.png").transpose(Image.Transpose.FLIP_LEFT_RIGHT)),
    "leftbottom_bac":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/BAC.png").transpose(Image.Transpose.FLIP_TOP_BOTTOM)),
    "rightbottom_bac":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/BAC.png").transpose(Image.Transpose.FLIP_LEFT_RIGHT).transpose(Image.Transpose.FLIP_TOP_BOTTOM)),
    "close_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/CLOSENORMAL.png").resize([int(int_dpi*49),int(int_dpi*20)])),
    "close_focusout":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/CLOSEFOCUSOUT.png").resize([int(int_dpi*49),int(int_dpi*20)])),
    "close_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/CLOSECORE.png").resize([int(int_dpi*49),int(int_dpi*20)])),
    "close_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/CLOSEON.png").resize([int(int_dpi*49),int(int_dpi*20)])),
    "full_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/FULLNORMAL.png").resize([int(int_dpi*31),int(int_dpi*20)])),
    "full_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/FULLCORE.png").resize([int(int_dpi*31),int(int_dpi*20)])),
    "full_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/FULLON.png").resize([int(int_dpi*31),int(int_dpi*20)])),
    "pist_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/PISTNORMAL.png").resize([int(int_dpi*31),int(int_dpi*20)])),
    "pist_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/PISTCORE.png").resize([int(int_dpi*31),int(int_dpi*20)])),
    "pist_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/PISTON.png").resize([int(int_dpi*31),int(int_dpi*20)])),
    "why_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/WHYNORMAL.png").resize([int(int_dpi*29),int(int_dpi*20)])),
    "why_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/WHYCORE.png").resize([int(int_dpi*29),int(int_dpi*20)])),
    "why_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/WHYON.png").resize([int(int_dpi*29),int(int_dpi*20)])),
    "iconic_normal":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/ICONICNORMAL.png").resize([int(int_dpi*29),int(int_dpi*20)])),
    "iconic_core":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/ICONICCORE.png").resize([int(int_dpi*29),int(int_dpi*20)])),
    "iconic_on":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/ICONICON.png").resize([int(int_dpi*29),int(int_dpi*20)])),
    "both_normal":ImageTk.PhotoImage(Image.open(F"{wcd_path}assets/BOTHSCREENNORMAL.png").resize([int(int_dpi*16),int(int_dpi*16)])),
    "both_core":ImageTk.PhotoImage(Image.open(F"{wcd_path}assets/BOTHSCREENCORE.png").resize([int(int_dpi*16),int(int_dpi*16)])),
    "both_on":ImageTk.PhotoImage(Image.open(F"{wcd_path}assets/BOTHSCREENON.png").resize([int(int_dpi*17),int(int_dpi*17)])),
    "curson_duang":ImageTk.PhotoImage(Image.open(F"{wcd_path}assets/CURSONDUANG.png").resize([int(int_dpi*47),int(int_dpi*47)])),
    "curson_duang_big":ImageTk.PhotoImage(Image.open(F"{wcd_path}assets/CURSONDUANG.png").resize([int(int_dpi*70),int(int_dpi*70)])),
    "icon":Image.open(f"{wcd_path}assets/ICON.ico")
}
main_window.image = _icon

INFO = f"{wcd_path}assets/INFO.ico"
WARNING = f"{wcd_path}assets/WARNING.ico"
ERROR = f"{wcd_path}assets/ERROR.ico"
QUESTION = f"{wcd_path}assets/QUESTION.ico"

class _TaskBar:
    def __init__(self,master=None,alpha=1.0,title="",image=None,width=800,x=0,y=0):
        global _icon

        self.var = {
            "x_tep":False,
            "y_tep":False,
            "end_drag":False
        }

        if master is None:
            self.tb = tkinter.Toplevel(main_window)
        else:
            self.tb = tkinter.Toplevel(master)
        self.tb.title(title)
        self.tb.attributes("-transparentcolor","#000001")
        self.tb.attributes("-alpha",alpha)
        self.tb.attributes("-topmost",True)
        self.tb.overrideredirect(True)
        self.tb.config(bg="#FFFFFF")
        self.tb.geometry(f"{width}x37+{x}+{y}")

        if not image is None:
            self.icon = {
                "icon_16x16":image
            }
        else:
            self.icon = {
                "icon_16x16":None
            }

        self.bar = tkinter.Label(self.tb,bg=_setting["BORADCOLORFOCUSOUT"],borderwidth=0,highlightthickness=0)
        self.bar.place(x=1,y=1,width=width-2,height=35)

        self.leftup_bac = tkinter.Label(self.tb,image=_icon["leftup_bac"],borderwidth=0,highlightthickness=0)
        self.leftup_bac.place(x=0,y=0)

        self.rightup_bac = tkinter.Label(self.tb,image=_icon["rightup_bac"],borderwidth=0,highlightthickness=0)
        self.rightup_bac.place(x=width-7,y=0)

        if not image is None:
            self.ico = tkinter.Label(self.tb,image=image,bg=_setting["BORADCOLORFOCUSOUT"],width=16,height=16)
            self.ico.place(x=6,y=6)

        if not title == "":
            self.title = tkinter.Label(self.tb,text=title,bg=_setting["BORADCOLORFOCUSOUT"],font=("Segoe UI",10))
            self.title.place(x=30,y=3)
        
        self.tb.update()
    
    def _config_packs(self):
        self.bar.place(x=1,y=1,width=self.tb.winfo_width()-2,height=28)
        self.leftup_bac.place(x=0,y=0)
        self.rightup_bac.place(x=self.tb.winfo_width()-7,y=0)

    def _set_tep(self,x,y):
        if x < self.tb.winfo_x():
            self.var["x_tep"] = tkinter.LEFT
        elif x == self.tb.winfo_x():
            self.var["x_tep"] = tkinter.NONE
        elif x > self.tb.winfo_x():
            self.var["x_tep"] = tkinter.RIGHT
        if y < self.tb.winfo_y():
            self.var["y_tep"] = tkinter.TOP
        elif y == self.tb.winfo_y():
            self.var["y_tep"] = tkinter.NONE
        elif y > self.tb.winfo_y():
            self.var["y_tep"] = tkinter.BOTTOM

    def _drag(self,x,y):
        new_x = 0
        new_y = 0
        if x != self.tb.winfo_x():
            if self.var["x_tep"] == tkinter.LEFT:
                new_x = 1
            elif self.var["x_tep"] == tkinter.NONE:
                new_x = 0
            elif self.var["x_tep"] == tkinter.RIGHT:
                new_x = -1

        if y != self.tb.winfo_y():
            if self.var["y_tep"] == tkinter.TOP:
                new_y = -1
            elif self.var["y_tep"] == tkinter.NONE:
                new_y = 0
            elif self.var["y_tep"] == tkinter.BOTTOM:
                new_y = 1
                
        try:
            self.tb.geometry(f"+{self.tb.winfo_x()+new_x}+{self.tb.winfo_y()+new_y}")
        except UnboundLocalError:
            pass
        
        if not self.var["end_drag"]:
            if x != self.tb.winfo_x() or y != self.tb.winfo_y():
                self.tb.after(5,lambda:self._drag(x,y))
                self.var["end_drag"] = False
    
    def _config_len(self,width,end_x,end_y,offset):
        if width > self.tb.winfo_width():
            if self.tb.winfo_width() < width:
                self.tb.geometry(f"{self.tb.winfo_width()+8}x37+{self.tb.winfo_x()-offset}+{self.tb.winfo_y()}")
                self._config_packs()
                self.tb.after(5,lambda:self._config_len(width,end_x,end_y,offset))
            else:
                self.tb.geometry(f"{width}x37+{end_x}+{end_y}")
                self.var["end_drag"] = True
        elif width < self.tb.winfo_width():
            if self.tb.winfo_width() > width:
                self.tb.geometry(f"{self.tb.winfo_width()-8}x37+{self.tb.winfo_x()+offset}+{self.tb.winfo_y()}")
                self._config_packs()
                self.tb.after(5,lambda:self._config_len(width,end_x,end_y,offset))
            else:
                self.tb.geometry(f"{width}x37+{end_x}+{end_y}")
                self.var["end_drag"] = True
        else:
            pass
    
    def _resize(self,w,h,x,y):
        self.tb.geometry(f"{w}x{h}+{x}+{y}")
        self.tb.after(50,lambda:self.tb.destroy())

class _Glass:
    def __init__(self,trank,width,height,x,y,master=None):
        global _icon
        if master is None:
            self.w = tkinter.Toplevel(main_window)
        else:
            self.w = tkinter.Toplevel(master)
        self.w.attributes("-alpha",0.2)
        self.w.attributes("-topmost",True)
        self.w.attributes("-transparentcolor","#000001")
        self.w.config(bg="#9E9E9E")
        self.w.overrideredirect(True)
        self.w.geometry(f"{width}x{height}+{x}+{y}")
        crop_region = (x,y,x+width,y+height)
        cropped_img = _icon[f"border_{trank}"].crop(crop_region)
        self.photo_img = ImageTk.PhotoImage(cropped_img)
        self.image = tkinter.Label(self.w,image=self.photo_img,bg="#FFFFFF")
        self.image.pack(fill=tkinter.BOTH,expand=True)
        self.image.image = self.photo_img

        self.leftup_bac = tkinter.Label(self.w,image=_icon["leftup_bac"],highlightthickness=0,borderwidth=0)
        self.leftup_bac.place(x=0,y=0)
        
        self.rightup_bac = tkinter.Label(self.w,image=_icon["rightup_bac"],highlightthickness=0,borderwidth=0)
        self.rightup_bac.place(x=width-7,y=0)
        
        self.leftbottom_bac = tkinter.Label(self.w,image=_icon["leftbottom_bac"],highlightthickness=0,borderwidth=0)
        self.leftbottom_bac.place(x=0,y=height-7)
        
        self.rightbottom_bac = tkinter.Label(self.w,image=_icon["rightbottom_bac"],highlightthickness=0,borderwidth=0)
        self.rightbottom_bac.place(x=width-7,y=height-7)
    
    def _resize(self,width,height,x,y):
        self.w.geometry(f"{width}x{height}+{x}+{y}")
        self.leftup_bac.place(x=0,y=0)
        self.rightup_bac.place(x=width-7,y=0)
        self.leftbottom_bac.place(x=0,y=height-7)
        self.rightbottom_bac.place(x=width-7,y=height-7)

    def _close(self):
        self.w.destroy()

class _Curson:
    def __init__(self,master,x,y):
        global _icon
        self.x = x
        self.y = y
        if master is None:
            self.c = tkinter.Toplevel(main_window)
        else:
            self.c = tkinter.Toplevel(master)
        self.c.geometry(f"70x70+{x-45}+{y-45}")
        self.c.attributes("-topmost",True)
        self.c.attributes("-alpha",0.9)
        self.c.attributes("-transparentcolor","#000001")
        self.c.config(bg="#000001")
        self.c.overrideredirect(True)
        self.icon = tkinter.Label(self.c,image=_icon["curson_duang"],bg="#000001",highlightthickness=0,borderwidth=0)
        self.icon.place(x=23,y=23)
        self.c.after(200,self._run)
    
    def _run(self):
        global _icon
        if not self.c.attributes("-alpha") <= 0:
            self.icon.place(x=0,y=0)
            self.c.attributes("-alpha",self.c.attributes("-alpha")-0.25)
            self.icon.config(image=_icon["curson_duang_big"])
            self.c.after(30,self._run)
        else:
            self.c.destroy()


class Window:
    def __init__(self,have_root=True,can_resize=True,any_drag=False,topmost=False,can_bothscreen=False,win32_iconic=False,win32_drag=True,must_high_config=False,dwm=True,contrast=False,title="",image=None,main_win=None,boardfocusincolor=None,boardfocusoutcolor=None,contrastcolor=None,rootcolor=None,buttons=[False,True,True,True],width=800,height=600,min_width=400,min_height=300,alpha=0.6,trank=0.0,dragtime=200,borderwidth=7,borderheight=29,why_command=None):
        """
        any_drag: 任意地方都可以触发移动（适合borderwidth、borderheight都是7的情况下打开）You can trigger the move anywhere (suitable for enabling when borderwidth and borderheight are both 7)
        win32_iconic: 如果为True：Win32时的最小化，在任务栏没有图标，最小化为把窗口缩放为最小；如果为False：任务栏有图标，最小化消失，再次点击任务栏图标恢复（也许需要多点几次）If it's True: Minimizes in Win32 mode without an icon on the taskbar; minimizing just scales the window down to its smallest size. If it's False: There's an icon on the taskbar, and when minimized, the window disappears; you need to click the taskbar icon again to restore it (maybe multiple times)
        buttons: [问号按钮,最小化按钮,最大化按钮,关闭按钮]     [Why Button,Iconic Button,Fullscreen Button,Close Button]
        must_high_config: 强制高刷新率   Must user high reload(config)
        """
        global _icon,window_num
        window_num += 1
        self.hr = have_root
        self.can_resize = can_resize
        self.any_drag = any_drag
        self.can_fullscreen = can_bothscreen
        self.win32_iconic = win32_iconic
        self.mhc = must_high_config
        self.dwm = dwm
        self.contrast = contrast
        if self.contrast == True:
            self.mhc = False
            self.dwm = False
        self.boardfocusincolor = boardfocusincolor
        if self.boardfocusincolor == None:
            self.boardfocusincolor = _setting["BORADCOLORFOCUSIN"]
        self.boardfocusoutcolor = boardfocusoutcolor
        if self.boardfocusoutcolor == None:
            self.boardfocusoutcolor = _setting["BORADCOLORFOCUSOUT"]
        self.contrastcolor = contrastcolor
        if self.contrastcolor == None:
            self.contrastcolor = _setting["CONTRASTCOLOR"]
        self.rootcolor = rootcolor
        if self.rootcolor == None:
            self.rootcolor = _setting["ROOTCOLOR"]
        self.buttons = buttons
        self.alpha = alpha
        self.trank = trank
        self.dragtime = dragtime
        self.but_relen = 7
        if len(title) >= 25:
            title = title[:25] + "..."
        if title == "":
            title = " "
        self.title_str = title
        self.old_state = "normal"

        self.var = {
            "x":0,
            "y":0,
            "w":0,
            "h":0,
            "start_x":0,
            "start_y":0,
            "win_x":0,
            "win_y":0,
            "can_drag":False,
            "can_full_screen":True,
            "full_screen":False,
            "back_x":0,
            "back_y":0,
            "back_w":0,
            "back_h":0,
            "enter_iconic":False,
            "enter_full":False,
            "enter_close":False,
            "enter_why":False,
            "resize_mode":None,
            "resize_start_x":0,
            "resize_start_y":0,
            "resize_start_width":0,
            "resize_start_height":0,
            "resize_start_win_x":0,
            "resize_start_win_y":0,
            "bo_width":int(int_dpi*7),
            "font_size":int(int_dpi*10),
            "is_resizing":False,
            "is_iconic":False,
            "is_bothscreen":False,
            "is_configing_glass":False,
            "is_show_title":False,
            "have_cursor":False,
            "focus":True,
            "exit_alpha":0,
            "close_image":"normal",
            "full_image":"normal",
            "iconic_image":"normal",
            "why_image":"normal",
        }

        self.commands = []

        if not win32_iconic:
            if main_window is None:
                self.taskbaricon = tkinter.Toplevel(main_window)
            else:
                self.taskbaricon = tkinter.Toplevel(main_win)
            self.taskbaricon.withdraw()
            self.taskbaricon.protocol("WM_DELETE_WINDOW",self.destroy)
            self.taskbaricon.attributes("-alpha",0)
            self.taskbaricon.attributes("-transparentcolor","#000001")
            self.taskbaricon.title(self.title_str)
            if image:
                self.taskbaricon.iconbitmap(image)
            else:
                self.taskbaricon.iconbitmap(f"{wcd_path}assets\\DEFAULT.ico")
            self.taskbaricon.config(bg="#000001")
            self.taskbaricon.geometry(f"1x1+-114514137891+-114514137891")
            self.taskbaricon.deiconify()

        if win32_iconic:
            if main_window is None:
                self.w = tkinter.Toplevel(main_window)
            else:
                self.w = tkinter.Toplevel(main_win)
        else:
            self.w = tkinter.Toplevel(self.taskbaricon)
        self.w.withdraw()
        self.w.title(self.title_str)
        if image:
            self.w.iconbitmap(image)
        else:
            self.w.iconbitmap(f"{wcd_path}assets\\DEFAULT.ico")
        self.w.attributes("-alpha",alpha)
        self.w.attributes("-transparentcolor","#000001")
        self.w.attributes("-topmost",topmost)
        self.w.overrideredirect(True)
        self.w.config(bg="#000001")
        self.width = int(int_dpi * width)
        self.height = int(int_dpi * height)
        self.borderheight = int(int_dpi * borderheight)
        self.borderwidth = int(int_dpi * borderwidth)
        min_width = max(int(int_dpi*190),min_width)
        min_height = max(self.borderheight+self.borderwidth+1,min_height)
        self.w.geometry(f"{width}x{height}")
        self.w.deiconify()
        if not f"border_{self.trank}" in _icon:
            _icon[f"border_{self.trank}"] = _icon["border_0"].filter(ImageFilter.GaussianBlur(radius=self.trank))
        if not f"light_{self.borderwidth}" in _icon:
            _icon[f"light_{self.borderwidth}"] = _icon["border_0"].resize([self.borderwidth,6])
        if not f"trans_parent_{len(self.title_str)*24}" in _icon:
            _icon[f"trans_parent_{len(self.title_str)*24}"] = ImageTk.PhotoImage(_icon["trans_parent_552"].resize([int(int_dpi*len(self.title_str)*24),int(int_dpi*114)]))

        if not image is None:
            self.icon = {
                "icon":Image.open(image),
                "icon_16x16":ImageTk.PhotoImage(Image.open(image).resize([int(int_dpi*16),int(int_dpi*16)]))
            }
        else:
            self.icon = {
                "icon":Image.open(f"{wcd_path}assets/DEFAULT.ico"),
                "icon_16x16":ImageTk.PhotoImage(Image.open(f"{wcd_path}assets/DEFAULT.ico").resize([int(int_dpi*16),int(int_dpi*16)]))
            }
        
        self.glass = _Glass(self.trank,0,0,0,0,self.w)
        self.glass.w.withdraw()

        self.bar = tkinter.Canvas(self.w,bg="#000001",border=0,borderwidth=0,highlightthickness=0)
        
        self.menu = tkinter.Menu(self.w,tearoff=0,font=("新宋体",9))
        self.menu.add_command(label="还原",command=lambda:self._full_screen(None))
        self.menu.add_command(label="移动",command=lambda:[pyautogui.moveTo(self.w.winfo_x()+self.w.winfo_width()//2,self.w.winfo_y()+20)])
        self.menu.add_command(label="大小",command=lambda:[pyautogui.moveTo(self.w.winfo_x()+self.w.winfo_width()//2,self.w.winfo_y()+self.w.winfo_height()//2)])
        if not self.can_resize:
            self.menu.entryconfig(2,state=tkinter.DISABLED)
        self.menu.add_command(label="最小化",command=lambda:self._iconic(None))
        if not self.buttons[1]:
            self.menu.entryconfig(3,state=tkinter.NORMAL)
        self.menu.add_command(label="最大化",command=lambda:self._full_screen(None))
        if self.buttons[2]:
            self.menu.entryconfig(4,state=tkinter.NORMAL)
        self.menu.add_separator()
        self.menu.add_command(label="关闭",font=("新宋体",9,"bold"),command=self.destroy)
        if not self.buttons[3]:
            self.menu.entryconfig(6,state=tkinter.NORMAL)

        if have_root:
            self.root = tkinter.Frame(self.w,bg=self.rootcolor,width=width-self.borderwidth*2,height=height-self.borderheight)
        self.w.bind("<FocusIn>",lambda event:[
            self._set_var("focus",True),
            self._set_closeicon(),
            self._focus_inout()
            ])
        self.w.bind("<FocusOut>",lambda event:[
            self._set_var("focus",False),
            self._set_closeicon(),
            self._focus_inout()
            ])
        self.w.bind("<ButtonPress-1>",self._drag)
        self.w.bind("<B1-Motion>",self._drag)
        self.w.bind("<ButtonRelease-1>",self._drag)
        self.w.bind("<Alt-space>",lambda event:self._chick_icon(event,True))
        self.bar.bind("<ButtonPress-3>",self._right_menu)
        if can_bothscreen:
            self.w.bind("<F11>",lambda event:self._both_screen())
        self.bar.bind("<B1-Motion>",lambda event:self._show_glass(event,0),add="+")
        self.bar.bind("<ButtonRelease-1>",lambda event:self._show_glass(event,1),add="+")
        self.bar.bind("<ButtonPress-1>",lambda event:self._chick_icon(event,False))

        if self.buttons[3]:
            self.bar.tag_bind("close","<Enter>",lambda event:[self.bar.itemconfig("close",image=_icon["close_core"]),self._set_var("close",True)])
            self.bar.tag_bind("close","<Leave>",lambda event:[self.bar.itemconfig("close",image=self._set_closeicon()),self._set_var("close",False)])
            self.bar.tag_bind("close","<ButtonPress-1>",lambda event:[self.bar.itemconfig("close",image=_icon["close_on"])])
            self.bar.tag_bind("close","<ButtonRelease-1>",lambda event:[self.bar.itemconfig("close",image=_icon["close_core"]),self.destroy()])

        if self.buttons[2] and self.can_resize:
            self.bar.tag_bind("full","<Enter>",lambda event:[self._set_othericon("full","core"),self._set_var("full",True)])
            self.bar.tag_bind("full","<Leave>",lambda event:[self._set_othericon("full","normal"),self._clean_butenter()])
            self.bar.tag_bind("full","<ButtonPress-1>",lambda event:[self._set_othericon("full","on")])
            self.bar.tag_bind("full","<ButtonRelease-1>",lambda event:[self._set_othericon("full","core"),self._full_screen(event)])

        if self.buttons[1]:
            self.bar.tag_bind("iconic","<Enter>",lambda event:[self._set_othericon("iconic","core"),self._set_var("iconic",True)])
            self.bar.tag_bind("iconic","<Leave>",lambda event:[self._set_othericon("iconic","normal"),self._clean_butenter()])
            self.bar.tag_bind("iconic","<ButtonPress-1>",lambda event:[self._set_othericon("iconic","on")])
            self.bar.tag_bind("iconic","<ButtonRelease-1>",lambda event:[self._set_othericon("iconic","core"),self._iconic(event)])
        
        if self.buttons[0]:
            self.bar.tag_bind("why","<Enter>",lambda event:[self.bar.itemconfig("why",image=_icon["why_core"]),self._set_var("why",True)])
            self.bar.tag_bind("why","<Leave>",lambda event:[self.bar.itemconfig("why",image=_icon["why_normal"]),self._clean_butenter()])
            self.bar.tag_bind("why","<ButtonPress-1>",lambda event:[self.bar.itemconfig("why",image=_icon["why_on"])])
            self.bar.tag_bind("why","<ButtonRelease-1>",lambda event:[self.bar.itemconfig("why",image=_icon["why_core"]),why_command()])
        if can_bothscreen:
            self.bar.tag_bind("both","<Enter>",lambda event:[self.bar.itemconfig("both",image=_icon["both_core"])])
            self.bar.tag_bind("both","<Leave>",lambda event:[self.bar.itemconfig("both",image=_icon["both_normal"])])
            self.bar.tag_bind("both","<ButtonPress-1>",lambda event:[self.bar.itemconfig("both",image=_icon["both_on"]),self._both_screen()])
        if self.can_resize:
            self.bar.bind("<Double-Button-1>",self._double_title)
            self.bar.bind("<Motion>",self._set_cursor)
            self.bar.bind("<ButtonPress-1>",self._start_resize,add="+")
            self.bar.bind("<B1-Motion>",lambda event:self._do_resize(event,min_width,min_height),add="+")
            self.bar.bind("<ButtonRelease-1>",self._end_resize,add="+")
        
        self._start(self.width-20,self.height-20)
        self._config_glass(None)
        self._run_command()
        self.w.focus_force()

    def _run_command(self):
        if self.commands != []:
            for command in self.commands:
                try:
                    command()
                except Exception as error:
                    if command is None or hasattr(globals,str(command.__self__)):
                        print(error)
                    else:
                        self.commands.remove(command)
        self.w.after(25,self._run_command)

    def _focus_inout(self):
        if not self.var["is_bothscreen"]:
            if self.var["focus"]:
                if not self.contrast:
                    self.bar.config(bg=self.boardfocusincolor)
                else:
                    self.bar.config(bg=self.contrastcolor)
            else:
                self.bar.config(bg=self.boardfocusoutcolor)
        elif self.var["is_bothscreen"]:
            if self.var["focus"]:
                self.bar.config(bg="#000000")
            else:
                if not self.win32_iconic:
                    self._iconic(None)
                else:
                    self._both_screen()

    def _set_closeicon(self):
        if self.var["focus"]:
            self.bar.itemconfig("close",image=_icon["close_normal"])
        elif not self.var["focus"]:
            self.bar.itemconfig("close",image=_icon["close_focusout"])
    
    def _set_othericon(self,but,image):
        if but == "full":
            if not self.var["is_iconic"] and self.var["full_screen"]:
                self.bar.itemconfig("full",image=_icon[f"pist_{image}"])
            else:
                self.bar.itemconfig("full",image=_icon[f"full_{image}"])
        if but == "iconic":
            if self.var["is_iconic"] and self.var["full_screen"]:
                self.bar.itemconfig("iconic",image=_icon[f"pist_{image}"])
            else:
                self.bar.itemconfig("iconic",image=_icon[f"iconic_{image}"])
        
    def _clean_butenter(self):
        self.var["enter_close"] = False
        self.var["enter_full"] = False
        self.var["enter_iconic"] = False
        self.var["enter_why"] = False

    def _remove_window(self):
        global window_num
        window_num -= 1
        if not self.win32_iconic:
            self.w.after(75,self.taskbaricon.destroy())
        else:
            self.w.after(75,self.w.destroy())
        if window_num == 0:
            main_window.destroy()


    def _set_var(self,setvar,value):
        if setvar == "close":
            self.var["enter_close"] = value
        elif setvar == "full":
            self.var["enter_full"] = value
        elif setvar == "iconic":
            self.var["enter_iconic"] = value
        elif setvar == "why":
            self.var["enter_why"] = value
        elif setvar == "focus":
            self.var["focus"] = value

    def _config_glass(self,event):
        global _icon

        if self.var["is_configing_glass"]:
            return

        self.var["is_configing_glass"] = True
        
        if not self.var["is_bothscreen"]:
            if self.w.winfo_x() != self.var["x"] or self.w.winfo_y() != self.var["y"] or self.w.winfo_width() != self.var["w"] or self.w.winfo_height() != self.var["h"]:
                self.bar.place(x=0,y=0,width=self.w.winfo_width(),height=self.w.winfo_height())
                self.bar.delete(tkinter.ALL)
                if not self.contrast and self.hr:
                    lightimg = _icon[f"light_{self.borderwidth}"].resize([self.borderwidth,self.w.winfo_height()//3])
                    self.photo_lightimg = ImageTk.PhotoImage(lightimg)
                    self.bar.create_image(0,self.borderheight+6,image=self.photo_lightimg,anchor=tkinter.NW,tags="light")
                    self.bar.create_image(self.w.winfo_width(),self.borderheight+6,image=self.photo_lightimg,anchor=tkinter.NE,tags="light")
                if self.hr and self.dwm:
                    bordercrop_region = (self.w.winfo_x(),self.w.winfo_y(),self.w.winfo_x() + self.w.winfo_width(),self.w.winfo_y() + self.borderheight)
                else:
                    bordercrop_region = (self.w.winfo_x(),self.w.winfo_y(),self.w.winfo_x() + self.w.winfo_width(),self.w.winfo_y() + self.w.winfo_height())
                if self.dwm:
                    cropped_borderimg = _icon[f"border_{self.trank}"].crop(bordercrop_region)
                    self.photo_borderimg = ImageTk.PhotoImage(cropped_borderimg)
                    self.bar.create_image(1,1,image=self.photo_borderimg,anchor=tkinter.NW,tags="bg")
                self.bar.create_image(self.w.winfo_width(),0,image=_icon["trans_parent"],tags="wu")
                self.bar.create_image(0,0,image=_icon[f"trans_parent_{len(self.title_str)*24}"],tags="wu")
                
                if self.var["focus"]:
                    self.bar.config(bg=self.boardfocusincolor)
                    if self.contrast:
                        self.bar.config(bg=self.contrastcolor)
                else:
                    self.bar.config(bg=self.boardfocusoutcolor)

                self.bar.create_image(self.borderheight//2,self.borderheight//2,image=self.icon["icon_16x16"],tags="icon")
                if not self.contrast:
                    self.bar.create_text(self.borderheight,self.borderheight//2,text=self.title_str,fill="black",font=("Segoe UI",self.var["font_size"]),anchor=tkinter.W,tags="title")
                else:
                    self.bar.create_text(self.borderheight,self.borderheight//2,text=self.title_str,fill="white",font=("Segoe UI",self.var["font_size"]),anchor=tkinter.W,tags="title")

                if not self.contrast:
                    self.bar.create_image(0,0,image=_icon["leftup_bac"],anchor=tkinter.NW,tags="bac")
                    self.bar.create_image(self.w.winfo_width(),0,image=_icon["rightup_bac"],anchor=tkinter.NE,tags="bac")
                    self.bar.create_image(0,self.w.winfo_height(),image=_icon["leftbottom_bac"],anchor=tkinter.SW,tags="bac")
                    self.bar.create_image(self.w.winfo_width(),self.w.winfo_height(),image=_icon["rightbottom_bac"],anchor=tkinter.SE,tags="bac")

                self.but_relen = self.var["bo_width"]
                if self.buttons[3]:
                    self.bar.create_image(self.w.winfo_width()-self.but_relen,0,image=_icon["close_normal"],anchor=tkinter.NE,tags="close")
                    self.but_relen += int(int_dpi*49)
                if self.buttons[2]:
                    if not self.var["is_iconic"] and self.var["full_screen"]:
                        self.bar.create_image(self.w.winfo_width()-self.but_relen,0,image=_icon["pist_normal"],anchor=tkinter.NE,tags="full")
                    else:
                        self.bar.create_image(self.w.winfo_width()-self.but_relen,0,image=_icon["full_normal"],anchor=tkinter.NE,tags="full")
                    self.but_relen += int(int_dpi*31)
                if self.buttons[1]:
                    if self.var["is_iconic"] and self.var["full_screen"]:
                        self.bar.create_image(self.w.winfo_width()-self.but_relen,0,image=_icon["pist_normal"],anchor=tkinter.NE,tags="iconic")
                        self.but_relen += int(int_dpi*29)
                    else:
                        self.bar.create_image(self.w.winfo_width()-self.but_relen,0,image=_icon["iconic_normal"],anchor=tkinter.NE,tags="iconic")
                        self.but_relen += int(int_dpi*29)
                if self.buttons[0]:
                    self.bar.create_image(self.w.winfo_width()-self.but_relen,0,image=_icon["why_normal"],anchor=tkinter.NE,tags="why")
                    self.but_relen += int(int_dpi*29)
        else:
            self.bar.delete(tkinter.ALL)
            self.bar.config(bg="#000000")
            self.bar.place(x=0,y=0,width=self.w.winfo_width(),height=self.w.winfo_height())
            self.bar.create_image(self.borderheight//2,self.borderheight//2,image=self.icon["icon_16x16"],tags="icon")
            self.bar.create_text(self.borderheight,self.borderheight//2,text=self.title_str,fill="white",font=("Segoe UI",self.var["font_size"]),anchor=tkinter.W,tags="title")

            self.bar.create_image(self.w.winfo_screenwidth()-self.borderheight//2,6,image=_icon["both_normal"],anchor=tkinter.NW,tags="both")
            self.bar.tag_raise("both")

        self.bar.tag_raise("bg")
        if len(self.bar.find_withtag("bg")) != 0:
            self.bar.tag_raise("light","bg")
        self.bar.tag_raise("title")
        self.bar.tag_raise("icon")
        self.bar.tag_raise("close")
        self.bar.tag_raise("full")
        self.bar.tag_raise("iconic")
        self.bar.tag_raise("why")
        self.bar.tag_raise("bac")

        if hasattr(self,"root"):
            if not self.var["is_iconic"] and self.var["full_screen"]:
                self.root.pack(padx=(self.borderwidth,self.borderwidth),pady=(self.borderheight-6,0),fill=tkinter.BOTH,expand=True)
            elif self.var["is_bothscreen"]:
                if not self.var["is_show_title"]:
                    if self.w.winfo_pointery() <= 2:
                        self.root.pack(padx=(0,0),pady=(self.borderheight,0),fill=tkinter.BOTH,expand=True)
                        self.var["is_show_title"] = True
                    else:
                        self.root.pack(padx=(0,0),pady=(0,0),fill=tkinter.BOTH,expand=True)
                else:
                    if self.w.winfo_pointery() >= self.borderheight:
                        self.root.pack(padx=(0,0),pady=(0,0),fill=tkinter.BOTH,expand=True)
                        self.var["is_show_title"] = False
                    else:
                        self.root.pack(padx=(0,0),pady=(self.borderheight,0),fill=tkinter.BOTH,expand=True)
            else:
                self.root.pack(padx=(self.borderwidth,self.borderwidth),pady=(self.borderheight,self.borderwidth),fill=tkinter.BOTH,expand=True)

        if not self.win32_iconic:
            if self.taskbaricon.state() != self.old_state:
                self.old_state = self.taskbaricon.state()
                self._iconic(None)
                self.w.focus_force()
        
        if self.var["full_screen"] and self.var["is_resizing"] and self.glass.w.state() != "withdrawn":
            self._show_glass(event,1)

        self.var["x"] = self.w.winfo_x()
        self.var["y"] = self.w.winfo_y()
        self.var["w"] = self.w.winfo_width()
        self.var["h"] = self.w.winfo_height()

        self.var["is_configing_glass"] = False
        if not self.mhc:
            self.w.after(25,lambda event=None:self._config_glass(None))
        elif not self.dwm:
            self.w.after(50,lambda event=None:self._config_glass(None))
        else:
            self.w.after(200,lambda event=None:self._config_glass(None))

    def _drag(self,event):
        if not self.any_drag and event.widget != self.bar:
            return
        if self.var["is_resizing"] or self.var["is_bothscreen"]:
            return
        if not self.var["is_iconic"] and self.var["full_screen"]:
            return

        if event.type == tkinter.EventType.ButtonPress:
            if not self.var["is_resizing"] and self.var["resize_mode"] is None:
                if not self.any_drag:
                    if event.y > self.borderheight:
                        return
                self.var["start_x"] = event.x_root
                self.var["start_y"] = event.y_root
                self.var["win_x"] = self.w.winfo_x()
                self.var["win_y"] = self.w.winfo_y()
                self.var["can_drag"] = True
                self._show_glass(event,0)
                self._split_window(event)
            else:
                self.var["can_drag"] = False
        elif event.type == tkinter.EventType.Motion and self.var["can_drag"]:
            dx = event.x_root - self.var["start_x"]
            dy = event.y_root - self.var["start_y"]
            if self.var['win_y'] + dy >= self.w.winfo_screenheight() - lib_bar - self.borderheight:
                self.w.geometry(f"+{self.var['win_x'] + dx}+{self.w.winfo_y()}")
            else:
                self.w.geometry(f"+{self.var['win_x'] + dx}+{self.var['win_y'] + dy}")
        elif event.type == tkinter.EventType.ButtonRelease:
            self.var["can_drag"] = False
            if not self.var["full_screen"]:
                self.w.geometry(f"+{self.w.winfo_x()}+{max(0,self.w.winfo_y())}")
            self._split_window(event)
    
    def _post_menu(self,event,x,y):
        if self.var["is_bothscreen"]:
            self.menu.post(x,y)
            return
        if self.var["full_screen"]:
            self.menu.entryconfig(0,state=tkinter.NORMAL)
            self.menu.entryconfig(1,state=tkinter.DISABLED)
            self.menu.entryconfig(2,state=tkinter.DISABLED)
            if self.buttons[1]:
                self.menu.entryconfig(3,state=tkinter.DISABLED)
            if self.buttons[2] and self.can_resize:
                self.menu.entryconfig(4,state=tkinter.DISABLED)
        elif not self.var["full_screen"]:
            self.menu.entryconfig(0,state=tkinter.DISABLED)
            self.menu.entryconfig(1,state=tkinter.NORMAL)
            if self.can_resize:
                self.menu.entryconfig(2,state=tkinter.NORMAL)
            else:
                self.menu.entryconfig(2,state=tkinter.DISABLED)
            if self.buttons[1]:
                self.menu.entryconfig(3,state=tkinter.NORMAL)
            else:
                self.menu.entryconfig(3,state=tkinter.DISABLED)
            if self.buttons[2] and self.can_resize:
                self.menu.entryconfig(4,state=tkinter.NORMAL)
            else:
                self.menu.entryconfig(4,state=tkinter.DISABLED)
        if self.buttons[3]:
            self.menu.entryconfig(6,state=tkinter.NORMAL)
        else:
            self.menu.entryconfig(6,state=tkinter.DISABLED)
        self.menu.post(x,y)

    def _right_menu(self,event):
        if event.y <= self.borderheight and event.widget == self.bar:
            self._post_menu(event,event.x_root,event.y_root)
    
    def _chick_icon(self,event,must):
        if self.var["can_drag"] or self.var["is_resizing"]:
            return
        if (event.y < self.borderheight and event.x < self.borderheight and event.y > self.var["bo_width"] and event.x > self.var["bo_width"] and not self.var["is_iconic"] and event.widget == self.bar) or must:
            if not self.var["is_bothscreen"]:
                self._post_menu(event,self.w.winfo_x()+self.borderwidth,self.w.winfo_y()+self.borderheight)
            else:
                self._post_menu(event,0,self.w.winfo_y()+self.borderheight)

    def _double_title(self,event):
        if self.var["is_bothscreen"]:
            return
        if not self.any_drag:
            if event.y < self.borderheight and event.x < self.borderheight and event.y > self.var["bo_width"] and event.x > self.var["bo_width"]:
                self.destroy()
            elif event.y <= self.borderheight and event.y > self.var["bo_width"] and not self.var["enter_full"] and not self.var["enter_close"] and not self.var["enter_iconic"] and not self.var["enter_why"]:
                self._full_screen(None)
        else:
            self._full_screen(None)
        self._show_glass(event,1)

    def _full_screen(self,event):
        global lib_bar
        if self.var["is_bothscreen"] or self.any_drag:
            return
        self._clean_butenter()
        if not self.var["full_screen"]:
            if self.var["can_full_screen"]:
                self.var["can_full_screen"] = False
                self.w.title(f"{self.title_str}")
                self.bar.delete("title")
                self.bar.create_text(self.borderheight,3,text=self.w.title(),font=("Segoe UI",10),anchor=tkinter.NW,tags="title")
                self.var["back_x"] = self.w.winfo_x()
                self.var["back_y"] = self.w.winfo_y()
                self.var["back_w"] = self.w.winfo_width()
                self.var["back_h"] = self.w.winfo_height()
                taskbar = _TaskBar(self.w,alpha=self.alpha,title=self.title_str,image=self.icon["icon_16x16"],width=self.w.winfo_width(),x=self.w.winfo_x(),y=self.w.winfo_y())
                taskbar._set_tep(self.w.winfo_screenwidth(),0)
                taskbar._drag(self.w.winfo_screenwidth(),0)
                taskbar._config_len(self.w.winfo_screenwidth(),0,0,4)
                self.w.after(self.dragtime,lambda:taskbar._resize(self.w.winfo_screenwidth(),self.borderheight,0,0))
                self.w.wait_window(taskbar.tb)
                self.w.geometry(f"{self.w.winfo_screenwidth()+14}x{self.w.winfo_screenheight() - lib_bar+2}+-7+-2")
                self.var["full_screen"] = True
                self.var["can_full_screen"] = True
                self.var["is_iconic"] = False
        else:
            if self.var["can_full_screen"]:
                self.var["can_full_screen"] = False
                self.w.title(f"{self.title_str}")
                self.bar.delete("title")
                self.bar.create_text(self.borderheight,3,text=self.w.title(),font=("Segoe UI",10),anchor=tkinter.NW,tags="title")
                taskbar = _TaskBar(self.w,alpha=self.alpha,title=self.title_str,image=self.icon["icon_16x16"],width=self.w.winfo_width(),x=self.w.winfo_x(),y=self.w.winfo_y())
                taskbar._set_tep(self.var["back_x"],self.var["back_y"])
                taskbar._drag(self.var["back_x"],self.var["back_y"])
                taskbar._config_len(self.var["back_w"],self.var["back_x"],self.var["back_y"],4)
                self.w.after(self.dragtime,lambda:taskbar._resize(self.var["back_w"],self.var["back_h"],self.var["back_x"],self.var["back_y"]))
                self.w.wait_window(taskbar.tb)
                self.w.geometry(f'{self.var["back_w"]}x{self.var["back_h"]}+{self.var["back_x"]}+{self.var["back_y"]}')
                self._show_glass(event,1)
                self.var["full_screen"] = False
                self.var["can_full_screen"] = True

    def _show_glass(self,event,mod):
        if not self.can_resize or self.var["is_bothscreen"] or self.var["enter_close"] or self.var["enter_full"] or self.var["enter_iconic"] or self.var["enter_why"]:
            return
        if mod == 0:
            if event.x_root <= 10 and not self.var["full_screen"] and not self.var["is_resizing"]:
                self.glass._resize((self.w.winfo_screenwidth() // 2) - 7,self.w.winfo_screenheight() - lib_bar - 7,7,7)
                self.glass.w.deiconify()
                if not self.var["have_cursor"]:
                    cursor = _Curson(self.w,event.x_root,event.y_root)
                    self.var["have_cursor"] = True
            elif event.x_root >= self.w.winfo_screenwidth() - 10 and not self.var["full_screen"] and not self.var["is_resizing"]:
                self.glass._resize((self.w.winfo_screenwidth() // 2),self.w.winfo_screenheight() - lib_bar - 7,(self.w.winfo_screenwidth() // 2),7)
                self.glass.w.deiconify()
                if not self.var["have_cursor"]:
                    cursor = _Curson(self.w,event.x_root,event.y_root)
                    self.var["have_cursor"] = True
            elif event.y_root <= 10 and not self.var["full_screen"] and not self.var["is_resizing"]:
                self.glass._resize(self.w.winfo_screenwidth() - 7,self.w.winfo_screenheight() - lib_bar - 7,7,7)
                self.glass.w.deiconify()
                if not self.var["have_cursor"]:
                    cursor = _Curson(self.w,event.x_root,event.y_root)
                    self.var["have_cursor"] = True
            elif not event.x_root >= self.w.winfo_screenwidth() - 10 and not event.x_root <= 10 and not event.y_root <= 10 and not self.var["full_screen"]:
                self._show_glass (event,1)
                self.var["have_cursor"] = False
        if mod == 1:
            self.glass.w.withdraw()

    def _split_window(self,event):
        global lib_bar
        if not self.can_resize or self.var["is_bothscreen"] or self.var["enter_close"] or self.var["enter_full"] or self.var["enter_iconic"] or self.var["enter_why"] or self.any_drag:
            return
        def _set_var(sid):
            if sid == 1:
                self.var["back_x"] = self.w.winfo_x()
                self.var["back_y"] = self.w.winfo_y()
                self.var["back_w"] = self.w.winfo_width()
                self.var["back_h"] = self.w.winfo_height()
            elif sid == 2:
                self.var["full_screen"] = True
                self.var["can_drag"] = False

        if event.x_root <= 10 and not self.var["full_screen"] and not self.var["can_drag"]:
            _set_var(1)
            taskbar = _TaskBar(self.w,alpha=self.alpha,title=self.title_str,image=self.icon["icon_16x16"],width=self.w.winfo_width(),x=self.w.winfo_x(),y=self.w.winfo_y())
            taskbar._set_tep(self.w.winfo_screenwidth() // 2,0)
            taskbar._drag(self.w.winfo_screenwidth() // 2,0)
            taskbar._config_len(self.w.winfo_screenwidth() // 2,0,0,4)
            self.w.after(self.dragtime,lambda:taskbar._resize(self.w.winfo_screenwidth() // 2,self.borderheight,0,0))
            self.w.wait_window(taskbar.tb)
            self.w.geometry(f"{self.w.winfo_screenwidth() // 2 + 7}x{self.w.winfo_screenheight() - lib_bar}+-7+0")
            _set_var(2)
        elif event.x_root >= self.w.winfo_screenwidth() - 10 and not self.var["full_screen"] and not self.var["can_drag"]:
            _set_var(1)
            taskbar = _TaskBar(self.w,alpha=self.alpha,title=self.title_str,image=self.icon["icon_16x16"],width=self.w.winfo_width(),x=self.w.winfo_x(),y=self.w.winfo_y())
            taskbar._set_tep(self.w.winfo_screenwidth(),0)
            taskbar._drag(self.w.winfo_screenwidth(),0)
            taskbar._config_len(self.w.winfo_screenwidth() // 2,0,0,4)
            self.w.after(self.dragtime,lambda:taskbar._resize(self.w.winfo_screenwidth() // 2,self.borderheight,self.w.winfo_screenwidth() // 2,0))
            self.w.wait_window(taskbar.tb)
            self.w.geometry(f"{self.w.winfo_screenwidth() // 2 + 7}x{self.w.winfo_screenheight() - lib_bar}+{self.w.winfo_screenwidth() // 2}+0")
            _set_var(2)
        elif event.y_root <= 10 and not self.var["full_screen"] and not self.var["can_drag"]:
            _set_var(1)
            self._full_screen(None)
            _set_var(2)
        self._clean_butenter()

    def _iconic(self,event):
        if self.any_drag:
            return
        if self.win32_iconic:
            if self.var["is_iconic"]:
                self.var["is_iconic"] = False
                self.var["full_screen"] = False
                taskbar = _TaskBar(self.w,alpha=self.alpha,title=self.title_str,image=self.icon["icon_16x16"],width=self.w.winfo_width(),x=self.w.winfo_x(),y=self.w.winfo_y())
                taskbar._set_tep(self.var["back_x"],self.var["back_y"])
                taskbar._drag(self.var["back_x"],self.var["back_y"])
                taskbar._config_len(self.var["back_w"],self.var["back_x"],self.var["back_y"],0)
                self.w.after(self.dragtime,lambda:taskbar._resize(self.var["back_w"],self.var["back_h"],self.var["back_x"],self.var["back_y"]))
                self.w.wait_window(taskbar.tb)

                if not self.title_str == "":
                    self.w.title(f"{self.title_str}")
                    self.bar.delete("title")
                    self.bar.create_text(self.borderheight,3,text=self.w.title(),font=("Segoe UI",10),anchor=tkinter.NW,tags="title")
                self.w.geometry(f'{self.var["back_w"]}x{self.var["back_h"]}+{self.var["back_x"]}+{self.var["back_y"]}')
            elif not self.var["is_iconic"]:
                self.var["full_screen"] = True
                self.var["is_iconic"] = True
                self.var["back_x"] = self.w.winfo_x()
                self.var["back_y"] = self.w.winfo_y()
                self.var["back_w"] = self.w.winfo_width()
                self.var["back_h"] = self.w.winfo_height()
                taskbar = _TaskBar(self.w,alpha=self.alpha,title=self.title_str,image=self.icon["icon_16x16"],width=self.w.winfo_width(),x=self.w.winfo_x(),y=self.w.winfo_y())
                taskbar._set_tep(self.w.winfo_x(),self.w.winfo_y()-self.borderheight)
                taskbar.tb.update()
                taskbar._drag(self.w.winfo_x(),self.w.winfo_y()-self.borderheight)
                taskbar._config_len(170,self.w.winfo_x(),self.w.winfo_y()-self.borderheight,0)
                self.w.after(self.dragtime,lambda:taskbar._resize(170,self.borderheight,self.w.winfo_x(),self.w.winfo_y()-self.borderheight))
                self.w.wait_window(taskbar.tb)
                if not self.title_str == "":
                    self.w.title(f"{self.title_str[0]}...")
                    self.bar.delete("title")
                    self.bar.create_text(self.borderheight,3,text=self.w.title(),font=("Segoe UI",10),anchor=tkinter.NW,tags="title")
                self.w.geometry(f"170x{self.borderheight}+{self.w.winfo_x()}+{self.w.winfo_y()-self.borderheight}")
        else:
            if self.var["is_iconic"]:
                self.var["is_iconic"] = False
                self.old_state = "iconic"
                self.taskbaricon.iconify()
                self.w.deiconify()
                self.w.focus_force()
            elif not self.var["is_iconic"]:
                self.var["is_iconic"] = True
                self.old_state = "normal"
                self.taskbaricon.deiconify()
                self.w.withdraw()
        
    def _both_screen(self):
        if not self.var["is_bothscreen"]:
            if self.var["is_iconic"]:
                return
            self.var["is_bothscreen"] = True
            self.var["is_show_title"] = False
            if not self.var["full_screen"] or not self.var["is_iconic"]:
                self.var["back_w"] = self.w.winfo_width()
                self.var["back_h"] = self.w.winfo_height()
                self.var["back_x"] = self.w.winfo_x()
                self.var["back_y"] = self.w.winfo_y()
            self.menu.entryconfig(0,state=tkinter.DISABLED)
            self.menu.entryconfig(1,state=tkinter.DISABLED)
            self.menu.entryconfig(2,state=tkinter.DISABLED)
            self.menu.entryconfig(3,state=tkinter.DISABLED)
            self.menu.entryconfig(4,state=tkinter.DISABLED)
            self.w.geometry(f"{self.w.winfo_screenwidth()}x{self.w.winfo_screenheight()}+0+0")
            self.w.focus_force()
        elif self.var["is_bothscreen"]:
            self.var["is_bothscreen"] = False
            self.var["is_show_title"] = False
            self.w.geometry(f"{self.var['back_w']}x{self.var['back_h']}+{self.var['back_x']}+{self.var['back_y']}")
        self._clean_butenter()
    
    def _set_cursor(self,event):
        if not self.any_drag and event.widget != self.bar:
            return
        if self.var["is_bothscreen"]:
            self.var["resize_mode"] = None
            self.w.config(cursor="arrow")
            return
        if not self.var["full_screen"]:
            if self.var["is_resizing"]:
                self.w.config(cursor="arrow")
                return

            self.var["resize_mode"] = None
            self.w.config(cursor="arrow")

            width = self.w.winfo_width()
            height = self.w.winfo_height()
            x,y = event.x,event.y
            bo_width = self.var["bo_width"]
        
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
            elif x > bo_width and x < width - bo_width and y > bo_width and y < height - bo_width:
                self.w.config(cursor="arrow")
        elif self.var["full_screen"]:
            self.var["resize_mode"] = None
            self.w.config(cursor="arrow")

    def _start_resize(self,event):
        if not self.var["full_screen"]:
            if self.var["resize_mode"] is not None:
                self.var["is_resizing"] = True
                self.var["resize_start_x"] = event.x_root
                self.var["resize_start_y"] = event.y_root
                self.var["resize_start_width"] = self.w.winfo_width()
                self.var["resize_start_height"] = self.w.winfo_height()
                self.var["resize_start_win_x"] = self.w.winfo_x()
                self.var["resize_start_win_y"] = self.w.winfo_y()

    def _do_resize(self,event,min_width,min_height):
        if not self.any_drag and event.widget != self.bar:
            return
        if not self.var["full_screen"]:
            if self.var["resize_mode"] is None or not self.var["is_resizing"] or self.var["is_bothscreen"] or self.w.cget("cursor") == "arrow":
                self.w.config(cursor="arrow")
                return
        
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
            self.w.geometry(f"{min(self.w.winfo_screenwidth(),max(min_width,new_width))}x{min(self.w.winfo_screenheight(),max(min_height,new_height))}+{new_x}+{new_y}")

    def _end_resize(self,event):
        self.var["is_resizing"] = False
        self.w.config(cursor="arrow")
        
    def _start(self,width,height):
        if self.var["exit_alpha"] < 1:
            self.var["exit_alpha"] += 0.2
            self.w.attributes("-alpha",self.var["exit_alpha"])
            width = width + 2
            height = height + 2
            self.w.geometry(f"{width}x{height}+{((self.w.winfo_screenwidth() - width) // 2)+1}+{((self.w.winfo_screenheight() - height) // 2) + 1}")
            if self.mhc:
                self.w.after(5,lambda:self._start(width,height))
            else:
                self.w.after(15,lambda:self._start(width,height))
        elif self.var["exit_alpha"] >= 1:
            self.var["exit_alpha"] = self.alpha
            self.w.attributes("-alpha",self.var["exit_alpha"])
            self.w.geometry(f"{self.width}x{self.height}+{(self.w.winfo_screenwidth() - self.width) // 2}+{(self.w.winfo_screenheight() - self.height) // 2}")

    def destroy(self):
        if self.var["exit_alpha"] > 0:
            self.var["exit_alpha"] -= 0.2
            self.w.attributes("-alpha",self.var["exit_alpha"])
            self.w.geometry(f"{max(self.w.winfo_width() - 2,1)}x{max(self.w.winfo_height() - 2,0)}+{self.w.winfo_x() + 1}+{self.w.winfo_y() + 2}")
            if self.mhc:
                self.w.after(5,self.destroy)
            else:
                self.w.after(15,self.destroy)
        elif self.var["exit_alpha"] <= 0:
            self._remove_window()
    
    def move(self,x,y):
        self.w.geometry(f"+{x}+{y}")
    
    def resize(self,width,height):
        self.w.geometry(f"{width}x{height}")
    
    def reg_command(self,command):
        self.commands.append(command)

    def unreg_command(self,command):
        self.commands.remove(command)

def Messagebox(title,main_title,message,image=INFO,main_win=None,contrast=False,color=["default","default","default","default"],buttons=[False,True,False]):
    """
    buttons:[重试(R),确定(Y),取消(N)]
    return:[None(R),True(Y),False(N)]
    """
    rul = False
    def ret(res):
        nonlocal rul
        rul = res
    msgwin = Window(have_root=True,can_resize=False,any_drag=False,topmost=True,can_bothscreen=False,win32_iconic=True,win32_drag=False,must_high_config=False,dwm=True,contrast=contrast,title=title,image=image,main_win=main_win,boardfocusincolor=color[0],boardfocusoutcolor=color[1],contrastcolor=color[2],rootcolor=color[3],buttons=[False,False,False,False],width=350,height=160+(len(message)//12)*20+40,alpha=1.0,borderwidth=7,borderheight=29,dragtime=0)
    msgwin.w.protocol("WM_DELETE_WINDOW",lambda:[msgwin.destroy(),ret(False)])
    img = ImageTk.PhotoImage(Image.open(image).resize((int(int_dpi*64),int(int_dpi*64))))
    icon = tkinter.Label(msgwin.root,bg="white",image=img)
    icon.image = img
    icon.place(x=int(int_dpi*25),y=int(int_dpi*25))

    main_title = main_title[:int(int_dpi*10)]
    title_label = tkinter.Label(msgwin.root,bg="white",fg="#4498FF",text=main_title,font=("微软雅黑",18,"bold"),justify="left",wraplength=int(int_dpi*200))
    title_label.place(x=int(int_dpi*125),y=int(int_dpi*20))

    message_label = tkinter.Label(msgwin.root,bg="white",fg="#111111",text=message,font=("微软雅黑",12),justify="left",wraplength=int(int_dpi*200))
    message_label.place(x=int(int_dpi*125),y=int(int_dpi*55))

    but_frame = tkinter.Frame(msgwin.root,bg="#EEEEEE")
    but_frame.place(x=0,y=int(int_dpi*160+(len(message)//12)*20-int(int_dpi*50)),width=int(int_dpi*350),height=int(int_dpi*50))

    if buttons[2]:
        no_but = Button(but_frame,text="取 消",width=int(int_dpi*45),build="medium",command=lambda event:[msgwin.destroy(),ret(False)])
    if buttons[1]:
        yes_but = Button(but_frame,text="确 定",width=int(int_dpi*45),build="medium",command=lambda event:[msgwin.destroy(),ret(True)])
    if buttons[0]:
        retry_but = Button(but_frame,text="重 试",width=int(int_dpi*45),build="medium",command=lambda event:[msgwin.destroy(),ret(None)])

    for index in reversed(range(len(buttons))):
        if buttons[index] is True:
            if buttons[2]:
                no_but.frame.pack(side=tkinter.RIGHT,padx=(int(int_dpi*5),int(int_dpi*21)))
            if buttons[1]:
                yes_but.frame.pack(side=tkinter.RIGHT,padx=(int(int_dpi*5),int(int_dpi*21)))
            if buttons[0]:
                retry_but.frame.pack(side=tkinter.RIGHT,padx=(int(int_dpi*5),int(int_dpi*21)))
    msgwin.w.focus_force()
    msgwin.resize(int(int_dpi*350),int(int_dpi*160+(len(message)//12)*20))
    msgwin.w.wait_window()
    return rul

def all_stop():
    main_window.destroy()

def main():
    main_window.mainloop()


#已抛弃了设置窗口，但是仍保留    The setting window has been abandoned, but it's still there.
"""
if True:
    pid = 0
    window = {}
    def go_bool(res):
        if res == "True":
            return True
        elif res == "False":
            return False
        elif res == "None":
            return None
        else:
            return str(res)
    def run_window():
        try:
            global pid,window,window_num
            res = setting.get(1.0,"end-1c").split("\n")
            have_root = go_bool(res[0])
            can_resize = go_bool(res[1])
            topmost = go_bool(res[2])
            can_bothscreen = go_bool(res[3])
            must_high_config = go_bool(res[4])
            win32_iconic = go_bool(res[5])
            dwm = go_bool(res[6])
            title = res[7]
            image = go_bool(res[8])
            bgin = str(res[9])
            bgout = str(res[10])
            rg = str(res[11])
            close = go_bool(res[12])
            full = go_bool(res[13])
            iconic = go_bool(res[14])
            why = go_bool(res[15])
            width = int(res[16])
            height = int(res[17])
            min_width = int(res[18])
            min_height = int(res[19])
            alpha = float(res[20])
            trank = int(res[21])
            dragtime = int(res[22])
            borderwidth = int(res[23])
            borderheight = int(res[24])
            window[str(pid)] = Window(have_root=have_root,can_resize=can_resize,topmost=topmost,can_bothscreen=can_bothscreen,win32_iconic=win32_iconic,must_high_config=must_high_config,dwm=dwm,title=title,image=image,boardfocusincolor=bgin,boardfocusoutcolor=bgout,rootcolor=rg,buttons=[why,iconic,full,close],main_win=main_window,width=width,height=height,min_width=min_width,min_height=min_height,alpha=alpha,trank=trank,dragtime=dragtime,borderwidth=borderwidth,borderheight=borderheight,why_command=lambda:[Messagebox("提问","你是什么?","你是人",INFO,None,[False,True,True])])
            pid += 1
            win.destroy()
            window_num -= 1
        except Exception as error:
            Messagebox(title="撞大运了",main_title="",message=str(error),image=ERROR,buttons=[False,True,False])
    win = tkinter.Toplevel()
    window_num += 1
    win.protocol("WM_DELETE_WINDOW",lambda:[main_window.destroy()])
    win.title("设置")
    win.geometry(f"300x362+250+400")
    win.resizable(True,False)
    win.minsize(300,362)
    win.maxsize(500,362)
    tip = tkinter.Text(win,bg="#000000",fg="#FFFFFF",width=7,height=24)
    tip.pack(anchor=tkinter.N,side=tkinter.LEFT)
    tip.insert(1.0,"有内容:\n拉伸  :\n置顶  :\n能全屏:\nW32ic :\n高刷新:\ndwm   :\n标题  :\n图标  :\n聚背色:\n离背色:\n内容色:\n关闭  :\n最大化:\n最小化:\n提问  :\n宽    :\n长    :\n最小宽:\n最小长:\n透明度:\n模糊度:\n动画时:\n边框宽:\n边框高:")
    tip.config(state=tkinter.DISABLED)
    setting = tkinter.Text(win,bg="#000000",fg="#FFFFFF",height=24)
    setting.pack(anchor=tkinter.N,side=tkinter.RIGHT)
    setting.insert(1.0,"True\nTrue\nTrue\nTrue\nTrue\nFalse\nTrue\n\nNone\ndefault\ndefault\ndefault\nTrue\nTrue\nTrue\nFalse\n400\n300\n0\n0\n1.0\n5\n200\n7\n29")
    run = tkinter.Button(win,text=f"{' ' * 56}运 行{' ' * 56}",command=run_window)
    run.place(x=7,y=320)
    win.mainloop()
    """

