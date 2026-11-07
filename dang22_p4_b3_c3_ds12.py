import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang22_p4_b3_c3_ds12(self):
                # Khai báo biến
                lisdang=['1']
                dang=random.choice(lisdang)
                if dang=='1':
                    h=randint(26,35)
                    l0=randint(22,27)
                    lh=20
                    lmin=randint(13,14)
                    
                    xe=h
                    ye=lh*sqrt(2)/2
                    
                    ym=lmin*sqrt(2)/2
                    
                    xa=0 
                    ya=l0*sqrt(2)/2
                    
                    a=ya-ye
                    b=-(2*xe*(ya-ym))
                    c=(ya-ym)*xe**2
                    delta=b**2-4*a*c
                    x1=round((-b+sqrt(delta))/(2*a),4)
                    x2=round((-b-sqrt(delta))/(2*a),4)
                    a1=round((ya-ym)/(x2**2),4)
                    
                    x22=((-b-sqrt(delta))/(2*a))
                    a11=((ya-ym)/(x22**2))
                    
                    x = symbols('x')
                    f=(a11*sqrt(2)*(x-x22)**2+ym*sqrt(2))**2
                    integral = integrate(f, (x, 0, h))
                    
                    h1=integral   
                    number = Decimal(float(h1))  # Số cần làm tròn
                    kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    
                    # Nội dung câu hỏi
                    noidungcauhoi = ('''\\immini{Một kiến trúc sư chịu trách nhiệm thiết kế một tòa nhà cao $%s$ m. Mặt cắt ngang tại mọi độ cao, vuông góc với trục thẳng đứng, luôn là một hình vuông (xem hình vẽ). Mặt đáy tòa nhà là hình vuông có cạnh $L_0=%s$ m, mặt đỉnh là hình vuông có cạnh $L_{%s}=%s$ m. Mặt cắt ngang tại vị trí hẹp nhất của tòa nhà là hình vuông có cạnh nhỏ nhất $L_{min}=%s$ m. Mặt cắt của tòa nhà theo mặt phẳng đứng chứa đường chéo đáy có dạng là hình phẳng giới hạn bởi hai đường cong parabol đối xứng nhau qua trục thẳng đứng đi qua tâm đáy của tòa nhà. Tính thể tích của tòa nhà đó (làm tròn đến hàng đơn vị, đơn vị tính: mét khối).}
                                    {\\definecolor{myColor}{HTML}{0FA19E}
\\tdplotsetmaincoords{70}{120}
\\begin{tikzpicture}[scale=0.08]
	\\begin{scope}[tdplot_main_coords]
		\\def\\L(#1){0.041*(#1-18)^2+13.75}
		\\draw[dashed, myColor] (0,0,0) -- (0,0,30);
		\\foreach \\z in {0,1,...,30}
		{
			\\pgfmathsetmacro{\\a}{\\L(\\z)/2}
			\\draw[myColor!60] 
			(-\\a,-\\a,\\z) -- (\\a,-\\a,\\z) -- (\\a,\\a,\\z) -- (-\\a,\\a,\\z) -- cycle;
		}
		\\foreach \\sx/\\sy in {1/1,1/-1,-1/1}
		{
			\\draw[thick, myColor]
			plot[domain=0:30,samples=80]
			({\\sx*\\L(\\x)/2 + (\\sx-1)*7},
			{\\sy*\\L(\\x)/2 + (\\sy-1)*7},
			{\\x});
		}
		\\draw[dashed, thick, myColor]
		plot[domain=0:30,samples=80]
		({-\\L(\\x)/2 -14},
		{-\\L(\\x)/2 -14},
		{\\x});
		\\def\\z{30}
		\\pgfmathsetmacro{\\a}{\\L(\\z)/2}
		\\draw[thick, myColor]
		(-\\a,-\\a,\\z) -- (\\a,-\\a,\\z) -- (\\a,\\a,\\z) -- (-\\a,\\a,\\z) -- cycle;
		\\def\\z{0}
		\\pgfmathsetmacro{\\a}{\\L(\\z)/2}
		\\draw[dashed, myColor]
		(-\\a,\\a,\\z)--(-\\a,-\\a,\\z) -- (\\a,-\\a,\\z);
		\\draw[thick, myColor] (\\a,-\\a,\\z) -- (\\a,\\a,\\z) -- (-\\a,\\a,\\z);
	\\end{scope}
\\end{tikzpicture}}'''
                                    %(latex(h),latex(l0),latex(h),latex(lh),latex(lmin)
                                    ))
                    
                    # Nội dung lời giải
                    loigiai = ('''Gắn hệ trục tọa độ như hình vẽ
                            \\begin{center}
                    \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                        \\clip(-0.35754288479221297,-4.888406469107392) rectangle (6.669867377236902,0.6080702411332669);
                        \\draw [line width=1.pt] (0.9773112488059941,-0.42892996611831796)-- (0.22058350072674074,-3.0504510933928737);
                        \\draw [line width=1.pt] (0.22058350072674074,-3.0504510933928737)-- (1.487490747233617,-4.458949898298273);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.487490747233617,-4.458949898298273)-- (2.15294185742912,-1.9964374442824853);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.15294185742912,-1.9964374442824853)-- (0.9773112488059941,-0.42892996611831796);
                        \\draw [line width=1.pt] (5.396060777768778,-0.9018848086678513)-- (6.12584881324675,-2.086041105209007);
                        \\draw [line width=1.pt] (6.12584881324675,-2.086041105209007)-- (5.712891923798839,-4.040703715262452);
                        \\draw [line width=1.pt] (5.712891923798839,-4.040703715262452)-- (4.9603927030270905,-2.911954884104829);
                        \\draw [line width=1.pt] (4.9603927030270905,-2.911954884104829)-- (5.396060777768778,-0.9018848086678513);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.9773112488059941,-0.42892996611831796)-- (1.487490747233617,-4.458949898298273);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.22058350072674074,-3.0504510933928737)-- (2.15294185742912,-1.9964374442824853);
                        \\draw [line width=1.pt] (5.396060777768778,-0.9018848086678513)-- (5.712891923798839,-4.040703715262452);
                        \\draw [line width=1.pt] (4.9603927030270905,-2.911954884104829)-- (6.12584881324675,-2.086041105209007);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.2388678795932886,-2.4950232503747567)-- (5.556328013232212,-2.489638522542143);
                        \\draw [line width=1.pt] (3.1351419979715867,-1.3825046750885592)-- (2.823899147866072,-2.7830975005633753);
                        \\draw [line width=1.pt] (2.823899147866072,-2.7830975005633753)-- (3.4074794918139117,-3.561204625827162);
                        \\draw [line width=1.pt] (4.9603927030270905,-2.911954884104829)-- (5.712891923798839,-4.040703715262452);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.1351419979715867,-1.3825046750885592)-- (3.679816985656237,-2.189790817549738);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.679816985656237,-2.189790817549738)-- (3.4074794918139117,-3.561204625827162);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.1351419979715867,-1.3825046750885592)-- (3.4074794918139117,-3.561204625827162);
                        \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.823899147866072,-2.7830975005633753)-- (3.679816985656237,-2.189790817549738);
                        \\draw [shift={(3.5301260681081335,2.509530908439193)},line width=1.pt]  plot[domain=3.9968962050907177:5.208021153636945,variable=\\t]({1.*3.893708087751821*cos(\\t r)+0.*3.893708087751821*sin(\\t r)},{0.*3.893708087751821*cos(\\t r)+1.*3.893708087751821*sin(\\t r)});
                        \\draw [shift={(3.877604860778423,-7.099118817805685)},line width=1.pt]  plot[domain=1.0195574641289467:2.3064109570379183,variable=\\t]({1.*3.559371768723372*cos(\\t r)+0.*3.559371768723372*sin(\\t r)},{0.*3.559371768723372*cos(\\t r)+1.*3.559371768723372*sin(\\t r)});
                        \\draw [shift={(4.4029947275819135,9.64640661122084)},line width=1.pt,dash pattern=on 2pt off 2pt]  plot[domain=4.521486084184426:4.858192168130107,variable=\\t]({1.*11.858269503568046*cos(\\t r)+0.*11.858269503568046*sin(\\t r)},{0.*11.858269503568046*cos(\\t r)+1.*11.858269503568046*sin(\\t r)});
                        \\draw [shift={(3.0613017001496714,-19.094038402317025)},line width=1.pt]  plot[domain=1.4539730673909295:1.7460425343502426,variable=\\t]({1.*16.293138851295804*cos(\\t r)+0.*16.293138851295804*sin(\\t r)},{0.*16.293138851295804*cos(\\t r)+1.*16.293138851295804*sin(\\t r)});
                        \\draw [->,line width=1.pt] (0.9769364188087277,-0.4302284843231333) -- (0.8757091430374055,0.3210202001729231);
                        \\draw [->,line width=1.pt] (5.556328013232212,-2.489638522542143) -- (6.499763649260406,-2.4856913114393278);
                        \\draw (0.7,-2.1) node[anchor=north west] {$O$};
                        \\draw (6.2,-2.5) node[anchor=north west] {$x$};
                        \\draw (0.4,0.3316516831714543) node[anchor=north west] {$y$};
                        \\draw (0.4,-0.1892909837565771) node[anchor=north west] {$A$};
                        \\draw (-0.3,-2.910950631380578) node[anchor=north west] {$B$};
                        \\draw (1.4072832929639643,-4.378095285177891) node[anchor=north west] {$C$};
                        \\draw (2.130224136864085,-1.5820152565641714) node[anchor=north west] {$D$};
                        \\draw (3.002005742743642,-0.8803373786611086) node[anchor=north west] {$M$};
                        \\draw (2.4,-2.730215420405547) node[anchor=north west] {$N$};
                        \\draw (3.289055783703984,-3.5063136792983287) node[anchor=north west] {$P$};
                        \\draw (3.6,-1.7) node[anchor=north west] {$Q$};
                        \\draw (5.2984060704263785,-0.45507805871985846) node[anchor=north west] {$E$};
                        \\draw (4.5,-2.8365302503908594) node[anchor=north west] {$F$};
                        \\draw (5.627982043380846,-3.9740989312337036) node[anchor=north west] {$G$};
                        \\draw (6.1,-1.773381950537734) node[anchor=north west] {$H$};
                    \\end{tikzpicture}
                \\end{center}
                Gọi $f(x)$ là parabol phía trên với đỉnh $M(x_0;y_0)$ với $y_0=\\frac{L_{min} \\sqrt{2}}{2}=\\frac{%s \\sqrt{2}}{2}=%s$, ta có \\\\
                    $f(x)=a(x-x_0)^2+%s$. \\\\
                        $f(x)$ đi qua điểm $A \\left(0; %s \\right)$ và $E \\left(%s;%s \\right)$ nên ta có hệ phương trình \\\\
                            $\\heva{& %s=a(-x_0)^2+%s \\\\ & %s=a(%s-x_0)^2+%s} \\Leftrightarrow \\heva{&a x_0^2=%s \\\\ & a \\left( %s x_0-%s \\right)=%s}$ \\\\
                                $\\Leftrightarrow \\heva{&a=\\frac{%s}{x_0^2} \\\\ & %s x_0^2-%s x_0+%s=0}$. \\\\
                Giải hệ ta được $x_0=%s$ và $a=%s$. \\\\
                    Suy ra $f(x)=%s(x-%s)^2+%s$. \\\\
                    Khi đó diện tích mặt cắt là $S(x)=\\left( f(x) \\sqrt{2} \\right)^2=\\left[ %s(x-%s)^2+%s \\right]^2$. \\\\
                Vậy thể tích của tòa nhà là \\\\
                    $V=\\int \\limits_0^{%s} \\left[ %s(x-%s)^2+%s \\right]^2 \\text{d}x \\approx %s$ m$^3$.'''
                            %(latex(lmin),latex(ym),latex(ym),
                                latex(ya),latex(xe),latex(ye),
                                latex(ya),latex(ym),
                                latex(ye),latex(xe),latex(ym),
                                latex(ya-ym),
                                latex(2*xe),latex(xe**2),latex(ya-ye),
                                latex(ya-ym),
                                latex(ya-ye),latex(2*xe*(ya-ym)),latex((ya-ym)*xe**2),
                                latex(x2),latex(a1),
                                latex(a1),latex(x2),latex(ym),
                                latex(a1*sqrt(2)),latex(x2),latex(ym*sqrt(2)),
                                latex(h),
                                latex(a1*sqrt(2)),latex(x2),latex(ym*sqrt(2)),
                                latex(kq)
                            ))
                    

                # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+
                    '\\loigiai{ \n'
                    +str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-')
                return content