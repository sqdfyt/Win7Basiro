# Win7Basiro
This repository uses Python to restore the opaque Microsoft Windows 7 Aero effect without ctypes.
About Files:
	1.init.py: Main file, includes Window, Messagebox, etc.
	2.packs.py: Component file, includes Button, Progress, etc.
	3.assets\*: Icon files, must not be missing.
What It Can Do:
	Experience Aero-style windows on Microsoft Windows 8 and above.
How It Works:
	1.Created with Tkinter.Tk/Toplevel windows using overrideredirect(True) (all functions reset due to no ctypes and WS_POPUP).
	2.Glass rendering: Repeatedly crop the area not blocked by Win7Basiro.Window.root and display the glass image at global positions.
Performance:
	1.Better performance than other similar windows. Uses only two components: Canvas (title bar drawing) and Frame (content area), instead of multiple components.
	2.Glass refresh (_config_glass) involves repeated image cropping, rendering, and calculation, so CPU usage may increase by about 10% (tested on my PC; set dwm=False when creating Win7Basiro.Window on low-end PCs).
Copyright:
	afytz/fyt/Fyuter reserves all rights.
	Not for demonstration only; you may use Win7Basiro to create windows (credit the author if possible).
(machine translated)

这个库使用Python，无ctypes的情况下复原了不透明的Microsoft Windows7 Aero效果
1.文件关于：
	1.__init__.py主文件 有Window、Messagebox等
	2.packs.py组件文件 有Button、Progress等
	3.assets\*图标文件 不可失
2.可以干什么：
	在Microsoft Windows 8及以上版本体验Aero式窗口
3.怎么做的：
	1.使用了overrideredirect(True)的Tkinter.Tk\Toplevel窗口制造（由于不使用ctypes加上WS_POPUP，所以重置了所有功能）
	2.关于玻璃渲染：反复裁剪不被Win7Basiro.Window.root阻挡的部分在玻璃图片在全局显示的位置
4.性能：
	1.相当于其他有同样特性的窗口，性能更佳。因为不使用多个组件装扮窗口，而是使用Canvas（标题栏绘制）和Frame（内容区）两个组件
	2.由于刷新玻璃效果（_config_glass）会反复裁切图片、渲染图片、运算，所以CPU也许会增加大约10%（在我的电脑上是这样的，低端电脑请在创建Win7Basiro.Window时设置dwm为False）
5.著作权：
	afytz/fyt/Fyuter保留所有权利
	非仅供演示，可使用Win7Basiro创建窗口（可以标注作者）
