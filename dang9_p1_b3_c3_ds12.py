import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang9_p1_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                a1=randint(-3,3)
                b1=randint(-3,3)
                a=-1
                b=a1-b1
                c=a1*b1
                f=a*x**2+b*x+c
                g=-x-b1
                k=[-b1,-1+a1]
                k1=sorted(k)
                x1=k1[0]
                x2=k1[1]
                x3=-b/2*a
                f1=f.subs(x,x1)
                f2=f.subs(x,x2)
                f3=f.subs(x,x3)
                yma=f3+1.5
                ymi=f1-3
                pt=Eq(a*x**2+b*x+c,ymi)
                sol1=solve(pt,x)
                so=sorted(sol1)
                d1=float(so[0])
                d2=float(so[1])
                d3=float(ymi-b1)
                d4=float(yma-b1)
                sol=[x1,x2]
                aa=sorted(sol)
                x11=aa[0]
                x22=aa[1]
                y=(-x**3)/3+((-1+b)/2)*x**2+(-b1+c)*x
                y1=y.subs(x,x11)
                y2=y.subs(x,x22)
                kq=nsimplify(y2-y1)
                xmi=float(x11-4)
                xma=float(x22+4)
                while kq<1.5 or x1==x2 or f1>5 or f1<-4 or f2>5 or f2<-4 or f3>5 or f3<-4 or b==0:
                    x=symbols('x')
                    a1=randint(-3,3)
                    b1=randint(-3,3)
                    a=-1
                    b=a1-b1
                    c=a1*b1
                    f=a*x**2+b*x+c
                    g=-x-b1
                    k=[-b1,-1+a1]
                    k1=sorted(k)
                    x1=k1[0]
                    x2=k1[1]
                    x3=-b/2*a
                    f1=f.subs(x,x1)
                    f2=f.subs(x,x2)
                    f3=f.subs(x,x3)
                    yma=f3+1.5
                    ymi=f1-3
                    pt=Eq(a*x**2+b*x+c,ymi)
                    sol1=solve(pt,x)
                    so=sorted(sol1)
                    d1=float(so[0])
                    d2=float(so[1])
                    d3=float(ymi-b1)
                    d4=float(yma-b1)
                    sol=[x1,x2]
                    aa=sorted(sol)
                    x11=aa[0]
                    x22=aa[1]
                    y=(-x**3)/3+((-1+b)/2)*x**2+(-b1+c)*x
                    y1=y.subs(x,x11)
                    y2=y.subs(x,x22)
                    kq=nsimplify(y2-y1)
                    xmi=float(x11-4)
                    xma=float(x22+4)

                du = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%( latex(x11),latex(x22),latex(b-1),latex(c-b1))
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(x^2+%sx+%s\\right)\\text{d}x$'%( latex(x11),latex(x22),latex(b-1),latex(c-b1)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%( latex(x11),latex(x22),latex(-b+1),latex(-c+b1)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%( latex(x11),latex(x22),latex(b-1+2),latex(c-b1+2)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%( latex(x11),latex(x22),latex(b-1+3),latex(c-b1+3))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình vẽ. Diện tích hình phẳng được gạch chéo bằng \n')
                hinhve=(
                    '\\begin{tikzpicture}[scale=0.6]\n'
                            '\\def\\xmin{%s} \\def\\xmax{%s}\n'
                            '\\def\\ymin{%s} \\def\\ymax{%s}\n'
                            '\\draw[->] (\\xmin,0)$zz$(\\xmax,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin)$zz$(0,\\ymax) node [right]{$y$};\n'
                            '\\draw[smooth,name path=hsf] plot[domain=%s:%s] (\\x,{-(\\x)^2+%s*(\\x)+%s}) node[above left,rotate =-80]{$y=-x^2+%sx+%s$};\n'
                            '\\draw[name path=hsg]  plot[domain=%s:%s] (\\x,{(\\x)+%s}) node[above right,rotate = 45]{$y=x+%s$};\n'
                            '\\fill[pattern=north west lines,intersection segments={of=hsf and hsg,sequence=L2}][intersection segments={of=hsf and hsg,sequence=R2}];\n'
                            '\\draw[fill=white] (0:0) circle (.03) node[below right]{$O$};\n'
                        '\\end{tikzpicture}\n'

                %(latex(xmi),latex(xma),latex(ymi),latex(yma),latex(d1),latex(d2),latex(b),latex(c),latex(b),latex(c),
                latex(d4),latex(d3),latex(b1),latex(b1)

                )

                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Phương trình hoành độ giao điểm của hai đồ thị hàm số là\\\\ \n'
                        '\\hspace*{1cm}$-x^2+%sx+%s=x+%s\\Leftrightarrow -x^2+%sx+%s=0\\Leftrightarrow\\hoac{&x=%s\\\\&x=%s}.$\\\\ \n'
                        'Trên đoạn $[%s;%s]$ đồ thị hàm số $y=x^2+%sx+%s$ ở phía trên đồ thị hàm số $y=x+%s$ nên diện tích hình phẳng được gạch chéo là\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle\\int\\limits_{%s}^{%s} \\left[(-x^2+%sx+%s)-(x+%s)\\right]\\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$.'
                        %(latex(b),latex(c),latex(b1),latex(b-1),latex(c-b1),latex(x11),latex(x22),
                        latex(x11),latex(x22),latex(b),latex(c),latex(b1),
                        latex(x11),latex(x22),latex(b),latex(c),latex(b1), latex(x11),latex(x22),latex(b-1),latex(c-b1))

                        )
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                a1=randint(-3,3)
                b1=randint(-3,3)
                a=1
                b=a1+b1
                c=a1*b1
                f=a*x**2+b*x+c
                g=x+b1
                k=[-b1,-1-a1]
                k1=sorted(k)
                x1=k1[0]
                x2=k1[1]
                x3=-b/2*a
                f1=f.subs(x,x1)
                f2=f.subs(x,x2)
                f3=f.subs(x,x3)
                yma=f1+3.5
                ymi=f3-1.5
                pt=Eq(a*x**2+b*x+c,yma)
                sol1=solve(pt,x)
                so=sorted(sol1)
                d1=float(so[0])
                d2=float(so[1])
                d3=float(-ymi-b1)
                d4=float(-yma-b1)
                sol=[x1,x2]
                aa=sorted(sol)
                x11=aa[0]
                x22=aa[1]
                y=(-x**3)/3-((1+b)/2)*x**2-(b1+c)*x
                y1=y.subs(x,x11)
                y2=y.subs(x,x22)
                kq=nsimplify(y2-y1)
                xmi=float(x11-4)
                xma=float(x22+4)
                while kq<1.5 or x1==x2 or f1>5 or f1<-2 or f2>5 or f2<-2 or f3>5 or f3<-2 or b==0:
                    x=symbols('x')
                    a1=randint(-3,3)
                    b1=randint(-3,3)
                    a=1
                    b=a1+b1
                    c=a1*b1
                    f=a*x**2+b*x+c
                    g=x+b1
                    k=[-b1,-1-a1]
                    k1=sorted(k)
                    x1=k1[0]
                    x2=k1[1]
                    x3=-b/2*a
                    f1=f.subs(x,x1)
                    f2=f.subs(x,x2)
                    f3=f.subs(x,x3)
                    yma=f1+3.5
                    ymi=f3-1.5
                    pt=Eq(a*x**2+b*x+c,yma)
                    sol1=solve(pt,x)
                    so=sorted(sol1)
                    d1=float(so[0])
                    d2=float(so[1])
                    d3=float(-ymi-b1)
                    d4=float(-yma-b1)
                    sol=[x1,x2]
                    aa=sorted(sol)
                    x11=aa[0]
                    x22=aa[1]
                    y=(-x**3)/3-((1+b)/2)*x**2-(b1+c)*x
                    y1=y.subs(x,x11)
                    y2=y.subs(x,x22)
                    kq=nsimplify(y2-y1)
                    xmi=float(x11-4)
                    xma=float(x22+4)

                du = ['$\\displaystyle\\int\\limits_{%s}^{%s}(-x^2+%sx+%s)\\text{d}x$'%(latex(x11),latex(x22),latex(-b-1),latex(-c-b1))
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s}(x^2+%sx+%s)\\text{d}x$'%(latex(x11),latex(x22),latex(-b-1),latex(-c-b1)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s}(-x^2+%sx+%s)\\text{d}x$'%(latex(x11),latex(x22),latex(-b-1+2),latex(-c-b1+1)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s}(-x^2+%sx+%s)\\text{d}x$'%(latex(x11),latex(x22),latex(-b-1+3),latex(-c-b1+2)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s}(-x^2+%sx+%s)\\text{d}x$'%(latex(x11),latex(x22),latex(b+1),latex(c+b1))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình vẽ. Diện tích hình phẳng được gạch chéo bằng\n')
                hinhve=(
                        '\\begin{tikzpicture}[scale=0.6]\n'
                            '\\def\\xmin{%s} \\def\\xmax{%s}\n'
                            '\\def\\ymin{%s} \\def\\ymax{%s}\n'
                            '\\draw[->] (\\xmin,0)$zz$(\\xmax,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin)$zz$(0,\\ymax) node [right]{$y$};\n'
                            '\\draw[smooth,name path=hsf] plot[domain=%s:%s] (\\x,{(\\x)^2+%s*(\\x)+%s}) node[below left,rotate = 75]{$y=x^2+%sx+%s$};\n'
                            '\\draw[name path=hsg]  plot[domain=%s:%s] (\\x,{-(\\x)-%s}) node[above right,rotate = -45]{$y=-x-%s$};\n'
                            '\\fill[pattern=north west lines,intersection segments={of=hsf and hsg,sequence=L2}][intersection segments={of=hsf and hsg,sequence=R2}];\n'
                            '\\draw[fill=white] (0:0) circle (.03) node[below right]{$O$};\n'
                        '\\end{tikzpicture}\n'

                %(latex(xmi),latex(xma),latex(ymi),latex(yma),latex(d1),latex(d2),latex(b),latex(c),latex(b),latex(c),
                latex(d3),latex(d4),latex(b1),latex(b1)

                )

                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Phương trình hoành độ giao điểm của hai đồ thị hàm số là\\\\ \n'
                        '\\hspace*{1cm}$x^2+%sx+%s=-x-%s\\Leftrightarrow x^2+%sx+%s=0\\Leftrightarrow\\hoac{&x=%s\\\\&x=%s}.$\\\\ \n'
                        'Trên đoạn $[%s;%s]$ đồ thị hàm số $y=-x-%s$ ở phía trên đồ thị hàm số $y=x^2+%sx+%s$ nên diện tích hình phẳng được gạch chéo là\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle\\int\\limits_{%s}^{%s}\\left[(-x-%s)-(x^2+%sx+%s)\\right]\\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s}(-x^2+%sx+%s)\\text{d}x$.'
                        %(latex(b),latex(c),latex(b1),latex(b+1),latex(c+b1),latex(x11),latex(x22),
                        latex(x11),latex(x22),latex(b1),latex(b),latex(c),
                        latex(x11),latex(x22),latex(b1),latex(b),latex(c), latex(x11),latex(x22),latex(-b-1),latex(-c-b1))

                        )
            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                a1=randint(-3,3)
                b1=randint(-3,3)
                a=-1
                b=a1-b1
                c=a1*b1
                f=a*x**2+b*x+c
                g=-x-b1
                k=[-b1,1+a1]
                k1=sorted(k)
                x1=k1[0]
                x2=k1[1]
                x3=-b/2*a
                f1=f.subs(x,x1)
                f2=f.subs(x,x2)
                f3=f.subs(x,x3)
                yma=f3+1.5
                ymi=f2-3
                pt=Eq(a*x**2+b*x+c,ymi)
                sol1=solve(pt,x)
                so=sorted(sol1)
                d1=float(so[0])
                d2=float(so[1])
                d3=float(-ymi-b1)
                d4=float(-yma-b1)
                sol=[x1,x2]
                aa=sorted(sol)
                x11=aa[0]
                x22=aa[1]
                y=(-x**3)/3+((1+b)/2)*x**2+(b1+c)*x
                y1=y.subs(x,x11)
                y2=y.subs(x,x22)
                kq=nsimplify(y2-y1)
                xmi=float(x11-4)
                xma=float(x22+4)

                while x1==x2 or kq<2 or f1>5 or f1<-4 or f2>5 or f2<-4 or f3>5 or f3<-4 or b==0:
                    x=symbols('x')
                    a1=randint(-3,3)
                    b1=randint(-3,3)
                    a=-1
                    b=a1-b1
                    c=a1*b1
                    f=a*x**2+b*x+c
                    g=-x-b1
                    k=[-b1,1+a1]
                    k1=sorted(k)
                    x1=k1[0]
                    x2=k1[1]
                    x3=-b/2*a
                    f1=f.subs(x,x1)
                    f2=f.subs(x,x2)
                    f3=f.subs(x,x3)
                    yma=f3+1.5
                    ymi=f2-3
                    pt=Eq(a*x**2+b*x+c,ymi)
                    sol1=solve(pt,x)
                    so=sorted(sol1)
                    d1=float(so[0])
                    d2=float(so[1])
                    d3=float(-ymi-b1)
                    d4=float(-yma-b1)
                    sol=[x1,x2]
                    aa=sorted(sol)
                    x11=aa[0]
                    x22=aa[1]
                    y=(-x**3)/3+((1+b)/2)*x**2+(b1+c)*x
                    y1=y.subs(x,x11)
                    y2=y.subs(x,x22)
                    kq=nsimplify(y2-y1)
                    xmi=float(x11-4)
                    xma=float(x22+4)

                du = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%(latex(x11),latex(x22),latex(b+1),latex(c+b1))
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(x^2+%sx+%s\\right)\\text{d}x$'%(latex(x11),latex(x22),latex(b+1),latex(c+b1)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%(latex(x11),latex(x22),latex(b+1+1),latex(c+b1+1)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%(latex(x11),latex(x22),latex(b+1+2),latex(c+b1)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%(latex(x11),latex(x22),latex(b+1+3),latex(c+b1+1))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = (
                    'Cho hình vẽ. '
                    'Diện tích hình phẳng được gạch chéo bằng'

                                )
                hinhve =('\\begin{tikzpicture}[scale=0.6]\n'
                '\\def\\xmin{%s} \\def\\xmax{%s}\n'
                '\\def\\ymin{%s} \\def\\ymax{%s}\n'
                '\\draw[->] (\\xmin,0)$zz$(\\xmax,0) node [below]{$x$};\n'
                '\\draw[->] (0,\\ymin)$zz$(0,\\ymax) node [right]{$y$};\n'
                '\\draw[smooth,name path=hsf] plot[domain=%s:%s] (\\x,{-(\\x)^2+%s*(\\x)+%s}) node[above right,rotate =80]{$y=-x^2+%sx+%s$};\n'
                '\\draw[name path=hsg]  plot[domain=%s:%s] (\\x,{-(\\x)-%s}) node[above left,rotate = -45]{$y=-x-%s$};\n'
                '\\fill[pattern=north west lines,intersection segments={of=hsf and hsg,sequence=L2}][intersection segments={of=hsf and hsg,sequence=R2}];\n'
                '\\draw[fill=white] (0:0) circle (.03) node[above left]{$O$};\n'
                '\\end{tikzpicture}\n'


            %(latex(xmi),latex(xma),latex(ymi),latex(yma),latex(d2),latex(d1),latex(b),latex(c),latex(b),latex(c),
            latex(d4),latex(d3),latex(b1),latex(b1)

            ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Phương trình hoành độ giao điểm của hai đồ thị hàm số là\\\\ \n'
                        '\\hspace*{1cm}$-x^2+%sx+%s=-x-%s\\Leftrightarrow -x^2+%sx+%s=0\\Leftrightarrow\\hoac{&x=%s\\\\&x=%s}.$\\\\ \n'
                        'Trên đoạn $[%s;%s]$ đồ thị hàm số $y=x^2+%sx+%s$ ở phía trên đồ thị hàm số $y=-x-%s$ nên diện tích hình phẳng được gạch chéo là\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle\\int\\limits_{%s}^{%s} \\left[(-x^2+%sx+%s)-(-x-%s)\\right]\\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$.'
                        %(latex(b),latex(c),latex(b1),latex(b+1),latex(c+b1),latex(x11),latex(x22),
                        latex(x11),latex(x22),latex(b),latex(c),latex(b1),
                        latex(x11),latex(x22),latex(b),latex(c),latex(b1), latex(x11),latex(x22),latex(b+1),latex(c+b1))

                        )
            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                a1=randint(-3,3)
                b1=randint(-3,3)
                a=1
                b=a1+b1
                c=a1*b1
                f=a*x**2+b*x+c
                g=x+b1
                k=[-b1,1-a1]
                k1=sorted(k)
                x1=k1[0]
                x2=k1[1]
                x3=-b/2*a
                f1=f.subs(x,x1)
                f2=f.subs(x,x2)
                f3=f.subs(x,x3)
                yma=f2+4
                ymi=f3-2
                pt=Eq(a*x**2+b*x+c,yma)
                sol1=solve(pt,x)
                so=sorted(sol1)
                d1=float(so[0])
                d2=float(so[1])
                d3=float(ymi-b1)
                d4=float(yma-b1)
                sol=[x1,x2]
                aa=sorted(sol)
                x11=aa[0]
                x22=aa[1]
                y=(-x**3)/3+((1-b)/2)*x**2+(b1-c)*x
                y1=y.subs(x,x11)
                y2=y.subs(x,x22)
                kq=nsimplify(y2-y1)
                xmi=float(x11-4)
                xma=float(x2+4)
                while x1==x2 or kq<1.5 or f1>5 or f1<-2 or f2>5 or f2<-2 or f3>5 or f3<-2 or b==0:
                    x=symbols('x')
                    a1=randint(-3,3)
                    b1=randint(-3,3)
                    a=1
                    b=a1+b1
                    c=a1*b1
                    f=a*x**2+b*x+c
                    g=x+b1
                    k=[-b1,1-a1]
                    k1=sorted(k)
                    x1=k1[0]
                    x2=k1[1]
                    x3=-b/2*a
                    f1=f.subs(x,x1)
                    f2=f.subs(x,x2)
                    f3=f.subs(x,x3)
                    yma=f2+4
                    ymi=f3-2
                    pt=Eq(a*x**2+b*x+c,yma)
                    sol1=solve(pt,x)
                    so=sorted(sol1)
                    d1=float(so[0])
                    d2=float(so[1])
                    d3=float(ymi-b1)
                    d4=float(yma-b1)
                    sol=[x1,x2]
                    aa=sorted(sol)
                    x11=aa[0]
                    x22=aa[1]
                    y=(-x**3)/3+((1-b)/2)*x**2+(b1-c)*x
                    y1=y.subs(x,x11)
                    y2=y.subs(x,x22)
                    kq=nsimplify(y2-y1)
                    xmi=float(x11-4)
                    xma=float(x2+4)

                du = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%(latex(x11),latex(x22),latex(-b+1),latex(-c+b1))
                    ]
                da= random.choice(du)
                s = ['$\\displaystyle\\int\\limits_{%s}^{%s} \\left(x^2+%sx+%s\\right)\\text{d}x$'%(latex(x11),latex(x22),latex(-b+1),latex(-c+b1)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%(latex(x11),latex(x22),latex(-b+1+1),latex(-c+b1+1)),
                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left(-x^2+%sx+%s\\right)\\text{d}x$'%(latex(x11),latex(x22),latex(-b+1+2),latex(-c+b1+2)),                                                                              
                    '$\\displaystyle\\int\\limits_{%s}^{%s} \\left(x^2+%sx+%s\\right)\\text{d}x$'%(latex(x11),latex(x22),latex(-b+1+3),latex(-c+b1+3))                                                                              
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hình vẽ. Diện tích hình phẳng được gạch chéo bằng \n')
                hinhve =('\\begin{tikzpicture}[scale=0.6]\n'
                            '\\def\\xmin{%s} \\def\\xmax{%s}\n'
                            '\\def\\ymin{%s} \\def\\ymax{%s}\n'
                            '\\draw[->] (\\xmin,0)$zz$(\\xmax,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin)$zz$(0,\\ymax) node [right]{$y$};\n'
                            '\\draw[smooth,name path=hsf] plot[domain=%s:%s] (\\x,{(\\x)^2+%s*(\\x)+%s}) node[below right,rotate = -80]{$y=x^2+%sx+%s$};\n'
                            '\\draw[name path=hsg]  plot[domain=%s:%s] (\\x,{(\\x)+%s}) node[above left,rotate = 45]{$y=x+%s$};\n'
                            '\\fill[pattern=north west lines,intersection segments={of=hsf and hsg,sequence=L2}][intersection segments={of=hsf and hsg,sequence=R2}];\n'
                            '\\draw[fill=white] (0:0) circle (.03) node[above left]{$O$};\n'
                        '\\end{tikzpicture}\n'

                %(latex(xmi),latex(xma),latex(ymi),latex(yma),latex(d2),latex(d1),latex(b),latex(c),latex(b),latex(c),
                latex(d3),latex(d4),latex(b1),latex(b1)

                )

                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Phương trình hoành độ giao điểm của hai đồ thị hàm số là\\\\ \n'
                        '\\hspace*{1cm}$x^2+%sx+%s=x+%s\\Leftrightarrow x^2+%sx+%s=0\\Leftrightarrow\\hoac{&x=%s\\\\&x=%s}.$\\\\ \n'
                        'Trên đoạn $[%s;%s]$ đồ thị hàm số $y=x+%s$ ở phía trên đồ thị hàm số $y=x^2+%sx+%s$ nên diện tích hình phẳng được gạch chéo là\\\\ \n'
                        '\\hspace*{1cm}$\\displaystyle\\int\\limits_{%s}^{%s}\\left[(x+%s)-(x^2+%sx+%s)\\right]\\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s}(-x^2+%sx+%s)\\text{d}x$.'
                        %(latex(b),latex(c),latex(b1),latex(b-1),latex(c-b1),latex(x11),latex(x22),
                        latex(x11),latex(x22),latex(b1),latex(b),latex(c),
                        latex(x11),latex(x22),latex(b1),latex(b),latex(c), latex(x11),latex(x22),latex(-b+1),latex(-c+b1))

                        )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n\\immini{'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n}{'+hinhve+ '} \n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-').replace('+0x+', '+').replace('+0x-', '-').replace('+0$', '$').replace('-0$', '$').replace('$zz$', '--').replace('-1x', '-x').replace('+1x', '+x').replace('+0=', '=').replace('-0=', '-').replace('+0)', ')').replace('-0)', ')').replace('+0}', '}').replace('-0}', '}').replace('+0\\right)', '\\right)').replace('+0\\Leftrightarrow', '\\Leftrightarrow').replace('-0\\right)', '\\right)').replace('-0\\Leftrightarrow', '\\Leftrightarrow')
            return content

