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


def bt_dang2_p2_b3_c1_ds12(self):
            # Khai báo biến
            x = symbols('x')

            while True:
                x1=randint(-3,-1)
                x2=randint(1,3)

                a = 1
                b=randint(-5,5)
                m=1
                #n=Rational(-x1-x2,2*a)
                n=(-x1-x2)/(2*a)
                #c=Rational(b*n-x1*x2,m)
                c=(b*n-x1*x2)/(m)

                f=(a*x**2+b*x+c)/(m*x+n)
                f1=(a*x1**2+b*x1+c)/(m*x1+n)
                y1=Rational(a*x1**2+b*x1+c,m*x1+n)
                f2=(a*x2**2+b*x2+c)/(m*x2+n)
                y2=Rational(a*x2**2+b*x2+c,m*x2+n)

                tcx=(a/m)*x+b/m-a*n/m**2
                tcd=-n/m
                hsa=Rational(a,m)
                hsb=Rational(b,m)-Rational(a*n,m**2)
                gox=Rational(-hsb,hsa)
                goy=hsb
                tcd1=Rational(-n,m)
                tcx1=hsa*x+hsb
                tcx1s=hsa*x+hsb+1
                if -4 <= f1 <= 4 and -4 <= f2 <= 4:
                    break
            while True:
                zx1=randint(-3,-1)
                zx2=randint(1,3)

                za = 1
                zb=randint(-5,5)
                zm=1
                #n=Rational(-x1-x2,2*a)
                zn=(-zx1-zx2)/(2*za)
                #c=Rational(b*n-x1*x2,m)
                zc=(zb*zn-zx1*zx2)/(zm)

                zf=(za*x**2+zb*x+zc)/(zm*x+zn)
                zf1=(za*zx1**2+zb*zx1+zc)/(zm*zx1+zn)
                zy1=Rational(za*zx1**2+zb*zx1+zc,zm*zx1+zn)
                zf2=(za*zx2**2+zb*zx2+zc)/(zm*zx2+zn)
                zy2=Rational(za*zx2**2+zb*zx2+zc,zm*zx2+zn)

                ztcx=(za/zm)*x+zb/zm-za*zn/zm**2
                ztcd=-zn/zm

                if -4 <= zf1 <= 4 and -4 <= zf2 <= 4:
                    break
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên  \n ''')
            hinhve = ('\\scalebox{0.6}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \\\\'
                        '\\tikzset{every node/.style={scale=0.9}} \\\\'
                                '\\draw[->] (-5.1,0)--(5.1,0) node[below left] {$x$}; \\\\'
                                '\\draw[->] (0,%s)--(0,%s) node[below left] {$y$}; \\\\' #11
                                '\\draw (0,0) node [below left] {$O$}; \\\\'
                                '\\draw (%s,0) node [below] {$%s$}; \\\\' #5
                                '\\draw (0,%s) node [left] {$%s$}; \\\\' #6
                                '\\draw (%s,0) node [below] {$%s$}; \\\\' #7
                                '\\draw (0,%s) node [left] {$%s$}; \\\\' #8

                                '\\draw (0,%s) node [left] {$%s$}; \\\\' #5
                                '\\draw (0,%s) node [left] {$%s$}; \\\\' #5

                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \\\\' #9
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \\\\' #10

                                '\\draw[dashed,thin](%s,%s)--(0,%s); \\\\' #
                                '\\draw[dashed,thin](0,%s)--(%s,%s); \\\\' #

                                '\\begin{scope} \\\\'
                                    '\\clip (-5,%s) rectangle (5,%s); \\\\' #12
                                    '\\draw[samples=200,domain=-5:%s,smooth,variable=\\x] plot (\\x,{(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \\\\' #1
                                    '\\draw[samples=200,domain=%s:5,smooth,variable=\\x] plot (\\x,{(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \\\\' #2
                                    '\\draw [line width=1.pt,domain=-5:5] plot(\\x,{%s*\\x+%s}); \\\\' #3
                                    '\\draw [line width=1.pt] (%s,%s) -- (%s,%s); \\\\'  #4
                                '\\end{scope}	 \\\\'
                                '\\draw (%s,0) node [below left] {$%s$}; \\\\' #13
                            '\\end{tikzpicture} \\\\}'

                                %(latex(f1-2),latex(f2+2), #11
                                latex(x2),latex(x2), #5
                                latex(f2),latex(y2), #6
                                latex(x1),latex(x1), #7
                                    latex(f1),latex(y1), #8

                                    latex(round(hsa*x1+hsb,1)),latex(hsa*x1+hsb),
                                    latex(round(hsa*x2+hsb,1)),latex(hsa*x2+hsb),

                                    latex(x2),latex(x2),latex(f2),latex(f2), #9
                                    latex(x1),latex(x1),latex(f1),latex(f1), #10

                                    latex(x1),latex(round(hsa*x1+hsb,1)),latex(round(hsa*x1+hsb,1)), #9
                                    latex(round(hsa*x2+hsb,1)),latex(x2),latex(round(hsa*x2+hsb,1)), #10

                                    latex(f1-2),latex(f2+2), #12
                                    latex(-n/m-0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #1
                                latex(-n/m+0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #2
                                latex(a/m),latex(b/m-a*n/m**2), #3
                                latex(-n/m),latex(f1-2), latex(-n/m),latex(f2+2), #4
                                latex(-n/m),latex(-Rational(n,m)), #13
                                ))
            # Các đáp án
            da_1_d = '\\True Đồ thị hàm số có đường tiệm cận đứng là $x=%s$'%(latex(tcd1))
            da_1_s = 'Đồ thị hàm số có đường tiệm cận đứng là  $x=%s$'%(latex(tcd1+1))
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Đồ thị hàm số có đường tiệm cận xiên là $y=%s$'%(latex(tcx1))
            da_2_s = 'Đồ thị hàm số có đường tiệm cận xiên là $y=%s$'%(latex(tcx1s))
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True Điểm cực đại của hàm số là $x=%s$'%(latex(x1))
            da_3_s = 'Điểm cực đại của hàm số là $x=%s$'%(latex(x2))
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Điểm cực tiểu của hàm số là $x=%s$'%(latex(x2))
            da_4_s = 'Điểm cực tiểu của hàm số là $x=%s$'%(latex(x1))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True Hàm số đồng biến trên các khoảng $\\left(-\\infty;%s\\right)$ và $\\left(%s;+\\infty\\right)$'%(latex(x1),latex(x2))
            da_5_s = 'Hàm số đồng biến trên các khoảng$\\left(-\\infty;%s\\right)$ và $\\left(%s;+\\infty\\right)$'%(latex(x2),latex(x1))
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True Hàm số nghịch biến trên các khoảng $\\left(%s;%s\\right)$ và $\\left(%s;%s\\right)$'%(latex(x1),latex(tcd1),latex(tcd1),latex(x2))
            da_6_s = 'Hàm số đồng biến trên khoảng$\\left(%s;%s\\right)$ '%(latex(x1),latex(x2))
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True Đồ thị hàm số không đi qua gốc tọa độ'
            da_7_s = 'Đồ thị hàm số đi qua gốc tọa độ'
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7]

            # Nội dung lời giải
            loigiai_1 = ('Dựa vào hình ta thấy đồ thị hàm số có đường tiệm cận đứng là $x=%s$.'%(latex(tcd1)))

            loigiai_2 = ('Tiệm cận xiên của đồ thị hàm số đi qua hai điểm $\\left(%s;%s\\right)$ và $\\left(%s;%s\\right)$ nên có phương trình là $y=%s$.'%(latex(x1),latex(hsa*x1+hsb),latex(x2),latex(hsa*x2+hsb),latex(tcx1)))

            loigiai_3 = ('Điểm cực đại của hàm số là $x=%s$.'%(latex(x1)))

            loigiai_4 = ('Điểm cực tiểu của hàm số là $x=%s$.'%(latex(x2)))

            loigiai_5 = ('Trên các khoảng $\\left(-\\infty;%s\\right)$ và $\\left(%s;+\\infty\\right)$ đồ thị đi lên từ trái sang phải nên hàm số đồng biến.'%(latex(x1),latex(x2)))

            loigiai_6 = ('Trên các khoảng $\\left(%s;%s\\right)$ và $\\left(%s;%s\\right)$ đồ thị đi xuống từ trái sang phải nên hàm số nghịch biến.'%(latex(x1),latex(tcd1),latex(tcd1),latex(x2)))

            loigiai_7 = ('Dựa vào đồ thị ta thấy đồ thị không đi qua gốc tọa độ $O(0;0)$.')

            # Đưa các lời giải vào danh sách lời giải
            list_2 = [loigiai_1, loigiai_2, loigiai_3, loigiai_4, loigiai_5, loigiai_6, loigiai_7]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined = list(zip(list_1, list_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers, shuffled_solutions = zip(*combined)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n\\immini{'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n} {'+hinhve+'} \n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n'). replace('\\dfrac','\\frac').replace('\\frac','\\dfrac').replace('.0','').replace('1 x','x')
            return content

