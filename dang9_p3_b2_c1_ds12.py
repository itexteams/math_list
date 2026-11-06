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


def bt_dang9_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x=symbols('x')
        y=symbols('y')
        i=randint(1,9)
        x0=2*i
        y0=4*i
        a=4*i
        b=3*i
        r=i
        m=Rational(y0,x0**2)

        c=(x-a)**2+(y-b)**2

        f=expand((a-x)**2+(b-y0+m*x**2)**2)
        daoham=diff(f, x)
        nghiem=solve(daoham, x)
        n0=[sol.evalf() for sol in nghiem if sol.is_real]

        solution_str = ', '.join(map(str, n0))
        solution_str

        n1 = n0[-1]

        fn1=expand((a-n1)**2+(b-y0+m*n1**2)**2)
        f0=expand((a-0)**2+(b-y0+m*0**2)**2)
        fx0=expand((a-x0)**2+(b-y0+m*x0**2)**2)
        zz=sqrt(fn1)
        h1=10*round(sqrt(fn1),2)-10*r
        number = Decimal(float(h1))  # Số cần làm tròn
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

        # Nội dung câu hỏi
        noidungcauhoi = ('''\\immini{ Một cái ao hình $ABCDE$, ở giữa ao có một mảnh vườn hình tròn có bán kính $%s0$ m. Người ta muốn bắc một chiếc cầu từ bờ $AB$ của ao đến vườn. Biết hai bờ $AE$ và $BC$ nằm trêm hai đường thẳng vuông góc với nhau, hai đường thẳng này cắt nhau tại điểm $O$. Bờ $AB$ là một phần của parabol có đỉnh là điểm $A$ và có trục đối xứng là đường thẳng $OA$. Độ dài $OA$ và $OB$ lần lượt là $%s0$ m và $%s0$ m. Tâm $I$ của mảnh vườn lần lượt cách các đường thẳng $AE$ và $BC$ là $%s0$ m và $%s0$ m. Độ dài tối thiểu của cây cầu là bao nhiêu mét? (kết quả làm tròn đến hàng đơn vị). }
                         {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                         	\\tikzset {_7gdtb9wdc/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{4 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_r8wa16hyo}{150bp}{rgb(0bp)=(0.6,0.85,1);
                         		rgb(37.5bp)=(0.6,0.85,1);
                         		rgb(62.5bp)=(0.29,0.56,0.89);
                         		rgb(100bp)=(0.29,0.56,0.89)}
                         	\\tikzset{every picture/.style={line width=0.75pt}} 
                         	\\path  [shading=_r8wa16hyo,_7gdtb9wdc] (25,18) -- (274.1,18) -- (274.1,205.6) -- (25,205.6) -- cycle ; 
                         	\\draw   (25,18) -- (274.1,18) -- (274.1,205.6) -- (25,205.6) -- cycle ; 
                         	\\draw  [fill={rgb, 255:red, 239; green, 181; blue, 87 }  ,fill opacity=1 ] (74.81,147.44) -- (144.61,123.63) -- (145.93,127.52) -- (76.14,151.32) -- cycle ;
                         	\\draw  [fill={rgb, 255:red, 245; green, 236; blue, 156 }  ,fill opacity=1 ] (137.6,115.2) .. controls (137.6,96.86) and (152.46,82) .. (170.8,82) .. controls (189.14,82) and (204,96.86) .. (204,115.2) .. controls (204,133.54) and (189.14,148.4) .. (170.8,148.4) .. controls (152.46,148.4) and (137.6,133.54) .. (137.6,115.2) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 196; green, 242; blue, 148 }  ,fill opacity=1 ] (24.6,71.4) .. controls (58.6,68.4) and (85.6,166.9) .. (94.6,205.4) .. controls (74.7,205.2) and (55.1,206.4) .. (25,205.6) .. controls (24.6,167.9) and (24.6,123.4) .. (24.6,71.4) -- cycle ;
                         	\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (170.8,115.2) -- (170.8,204.9) ;
                         	\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (170.8,115.2) -- (24.6,115.2) ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (187.7,61.07) .. controls (200.09,49.91) and (217.1,68.42) .. (230,61.24) .. controls (219.28,70.74) and (199.27,51.41) .. (187.7,61.07) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (181.15,62.15) .. controls (188.72,55.32) and (199.11,66.64) .. (207,62.25) .. controls (200.44,68.05) and (188.22,56.24) .. (181.15,62.15) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (72.2,85.57) .. controls (84.59,74.41) and (101.6,92.92) .. (114.5,85.74) .. controls (103.78,95.24) and (83.77,75.91) .. (72.2,85.57) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (65.65,86.65) .. controls (73.22,79.82) and (83.61,91.14) .. (91.5,86.75) .. controls (84.94,92.55) and (72.72,80.74) .. (65.65,86.65) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (201.7,160.07) .. controls (214.09,148.91) and (231.1,167.42) .. (244,160.24) .. controls (233.28,169.74) and (213.27,150.41) .. (201.7,160.07) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (195.15,161.15) .. controls (202.72,154.32) and (213.11,165.64) .. (221,161.25) .. controls (214.44,167.05) and (202.22,155.24) .. (195.15,161.15) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (233.33,153.33) .. controls (240.29,147.06) and (249.85,157.46) .. (257.1,153.42) .. controls (251.07,158.76) and (239.83,147.9) .. (233.33,153.33) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (229.65,153.93) .. controls (233.9,150.1) and (239.74,156.46) .. (244.17,153.99) .. controls (240.49,157.25) and (233.62,150.61) .. (229.65,153.93) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (103.03,95.74) .. controls (110.37,89.13) and (120.45,100.1) .. (128.1,95.84) .. controls (121.74,101.47) and (109.89,90.02) .. (103.03,95.74) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (99.15,96.38) .. controls (103.63,92.34) and (109.79,99.04) .. (114.47,96.44) .. controls (110.58,99.88) and (103.34,92.88) .. (99.15,96.38) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (134.17,174.74) .. controls (143.67,166.19) and (156.71,180.38) .. (166.6,174.87) .. controls (158.38,182.15) and (143.04,167.34) .. (134.17,174.74) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (129.15,175.57) .. controls (134.95,170.34) and (142.92,179.01) .. (148.97,175.64) .. controls (143.94,180.09) and (134.57,171.04) .. (129.15,175.57) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (218.14,55.98) .. controls (226.62,48.34) and (238.27,61.01) .. (247.1,56.09) .. controls (239.76,62.6) and (226.06,49.36) .. (218.14,55.98) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (213.65,56.71) .. controls (218.83,52.04) and (225.95,59.79) .. (231.35,56.78) .. controls (226.86,60.76) and (218.49,52.67) .. (213.65,56.71) -- cycle ;
                         	\\draw (6.5,200) node [anchor=north west][inner sep=0.75pt]    {$O$};
                         	\\draw (6.5,59) node [anchor=north west][inner sep=0.75pt]    {$A$};
                         	\\draw (86,209) node [anchor=north west][inner sep=0.75pt]    {$B$};
                         	\\draw (271,209) node [anchor=north west][inner sep=0.75pt]    {$C$};
                         	\\draw (8,3) node [anchor=north west][inner sep=0.75pt]    {$E$};
                         	\\draw (172,99.5) node [anchor=north west][inner sep=0.75pt]    {$I$};
                         	\\draw (31,53.5) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$%s0$};
                         	\\draw (98.5,186.5) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$%s0$};
                         	\\draw (160,206) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$%s0$};
                         	\\draw (4,104.5) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$%s0$};
                         	\\draw (274,4.5) node [anchor=north west][inner sep=0.75pt]    {$D$};
                         \\end{tikzpicture}}'''
                        %(latex(r),
                        latex(y0),latex(x0),
                        latex(a),latex(b),
                        latex(y0),
                        latex(x0),
                        latex(a),
                        latex(b),                         
                            ))

        # Nội dung lời giải
        loigiai = ('Gán hệ trục tọa độ $(Oxy)$ sao cho điểm $O$ trùng với gốc tọa độ, $\\heva{& A \\in Ox \\\\ & B \\in Oy}$ với đơn vị là $10$. \\\\ \n'
                'Khi đó mảnh vườn hình tròn có phương trình $(C): %s=%s$ có tâm $I(%s;%s)$. \\\\ \n' #1
                'Bờ $AB$ là một phần của parabol $(P): y=%s-%sx^2$ trên đoạn $[0;%s]$. \\\\ \n' #2
                'Bài toán trở thành tìm $MN$ nhỏ nhất với $\\heva{& N \\in (P) \\\\ & M \\in (C)}$. \\\\ \n'
                'Khi đó $MN + MI \\ge IN$, suy ra $MN$ nhỏ nhất khi $MN+MI=IN$ hay ba điểm $M, N, I$ thẳng hàng. \\\\ \n'
                'Sau đây ta xác định điểm $N$ để $IN$ nhỏ nhất. \\\\ \n'
                'Ta có \\\\ \n'
                '\\hspace*{1cm} $N \\in (P) \\Rightarrow N(x;%s-x^2)$. \\\\ \n' #3
                '\\hspace*{1cm} $IN =\\sqrt{(%s-x)^2+\\left(%s+%sx^2\\right)^2} \\Leftrightarrow IN^2 =(%s-x)^2+\\left(%s+%sx^2\\right)^2=%s$. \\\\ \n' #4
                'Xét hàm số $f(x)=%s$ trên đoạn $[0;%s]$. \\\\ \n' #5
                '\\hspace*{1cm} $f\'(x)=%s$. \\\\ \n' #6
                '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow x \\approx %s$. \\\\ \n' #7
                'Ta có \\\\ \n'
                '\\hspace*{1cm} $f(%s) \\approx %s$. \\\\ \n' #8
                '\\hspace*{1cm} $f(0)=%s$. \\\\ \n'
                '\\hspace*{1cm} $f(%s)=%s$. \\\\ \n'
                'Suy ra giá trị nhỏ nhất của hàm số $f(x)$ trên đoạn $[0;%s]$ bằng $%s$ khi $x \\approx %s$. \\\\ \n'
                'Do đó $\\min IN = \\sqrt{%s} = %s \\Rightarrow IN=%s$ m. \\\\ \n'
                'Suy ra $MN=IN-IM=%s-%s=%s$ m. \\\\ \n'
                'Vậy độ dài tối tiểu của cây cầu là $%s$ m.'
                %(  latex(c),latex(r**2),latex(a),latex(b), #1 
                    latex(y0),latex(m),latex(x0), #2
                    latex(y0), #3
                    latex(a),latex(b-y0),latex(m),latex(a),latex(b-y0),latex(m),latex(f), #4
                    latex(f),latex(x0), #5
                    latex(daoham), #6
                    latex(round(n1,2)), #7
                    latex(round(n1,2)),latex(round(fn1,2)), #8
                    latex(f0),
                    latex(x0),latex(fx0),
                    latex(x0),latex(round(fn1,2)), latex(round(n1,2)),
                    latex(round(fn1,2)),latex(round(sqrt(fn1),2)),latex(10*round(sqrt(fn1),2)),
                    latex(10*round(sqrt(fn1),2)),latex(10*r),latex(10*round(sqrt(fn1),2)-10*r),
                    latex(kq)
                ))

        #Đáp án
        dapan=' \\shortans[0]{$%s$} ' %(latex(kq))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content

