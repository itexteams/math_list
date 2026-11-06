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


def bt_dang5_p3_b2_c2_ds10(self):
            # Khai báo biến
            x = symbols('x')
            y = symbols('y')
            #Điểm A
            lis_ya=[2,3,4,5]
            ya=random.choice(lis_ya)
            xa=0
            #Điểm B
            lis_xb=[1,2,3]
            xb=random.choice(lis_xb)
            yb=ya
            #Điểm C
            lis_xc=[1,2]
            d_xc=random.choice(lis_xc)
            xc=xb+d_xc
            yc=ya-1
            #Điểm D
            xd=xc+1
            yd=0



            lis2=[2,3,4,5,6,7,8,9]
            i=random.choice(lis2)
            k=random.choice(lis2)
            #while i<=k:
                #i=random.choice(lis2)
                #k=random.choice(lis2)
            #Rút gọn các BPT
            lis3=[2,3,4,5]
            m=random.choice(lis3)
            n=random.choice(lis3)
            o=random.choice(lis3)

            bpt1=simplify((yd-yc)*x+(xc-xd)*y>=yc*(xc-xd)-xc*(yc-yd))
            pt11=m*(yc-yd)*x+m*(xd-xc)*y<=m*yc*(xd-xc)-m*xc*(yd-yc)
            pt111=m*(yc-yd)*x+m*(xd-xc)*y
            pt1=simplify(Eq((yd-yc)*x+(xc-xd)*y,yc*(xc-xd)-xc*(yc-yd)))
            bpt2=simplify((yb-yc)*x+(xc-xb)*y<=yc*(xc-xb)-xc*(yc-yb))
            pt22=o*(yb-yc)*x+o*(xc-xb)*y<=o*yc*(xc-xb)-o*xc*(yc-yb)
            pt222=o*(yb-yc)*x+o*(xc-xb)*y
            pt2=simplify(Eq((yb-yc)*x+(xc-xb)*y,yc*(xc-xb)-xc*(yc-yb)))

            pt33=n*y<=n*yb
            pt333=n*y

            a=ya*m+2*xa*m
            b=n*yc*(xc-xd)-n*xc*(yc-yd)
            c=2*m
            d=n*(yd-yc)
            e=m
            f=n*(xc-xd)
            #Tiền
            tien=i*x+k*y
            tien_a=i*xa+k*ya
            tien_b=i*xb+k*yb
            tien_c=i*xc+k*yc
            tien_d=i*xd+k*yd
            #Tìm GTNN
            tien_max=max(tien_a,tien_b,tien_c,tien_d)
            # Khởi tạo biến để lưu trữ giá trị x và y tương ứng với tien_min
            x_tien_max = None
            y_tien_max = None
            # Tìm x và y tương ứng với tien_min
            if tien_max == tien_a:
                x_tien_max = xa
                y_tien_max = ya
            elif tien_max == tien_b:
                x_tien_max = xb
                y_tien_max = yb
            elif tien_max == tien_c:
                x_tien_max = xc
                y_tien_max = yc
            elif tien_max == tien_d:
                x_tien_max = xd
                y_tien_max = yd

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có ba nhóm máy $A, B, C$ dùng để sản xuất ra hai loại sản phẩm $I$ và $II$. Để sản xuất một đơn vị sản phẩm mỗi loại phải lần lượt dùng các máy thuộc các nhóm khác nhau. Số máy trong một nhóm và số máy của từng nhóm cần thiết để sản xuất ra một đơn vị sản phẩm thuộc mỗi loại được cho trong bảng sau:\\\\'''
                            #Bảng
                            '\\begin{tabular}{|c|c|p{5cm}|c|} \n'
                            '\\hline \n'
                            '\\multirow{2}{*}{Nhóm} & \\multirow{2}{*}{Số máy trong mỗi nhóm} & \\multicolumn{2}{c|}{Số máy trong từng nhóm để sản xuất ra một đơn vị sản phẩm} \\\\ \n'
                            '\\cline{3-4} \n'
                            '&  & \\centering Loại I & Loại II \\\\ \n'
                            '\\hline \n'
                            'A & %s & \\multicolumn{1}{c|}{%s} & \\multicolumn{1}{c|}{%s} \\\\ \n'
                            '\\hline \n'
                            'B & %s & \\centering 0 & %s \\\\ \n'
                            '\\hline \n'
                            'C & %s &\\centering %s & %s \\\\ \n'
                            '\\hline \n'
                            '\\end{tabular}  \\\\ \n'
                            'Một đơn vị sản phẩm loại $I$ lãi $%s$ nghìn đồng, một đơn vị sản phẩm loại $II$ lãi $%s$ nghìn đồng. Tổng số cả hai sản phẩm phải sản xuất để có lãi cao nhất là bao nhiêu?'
                            %(latex(m*yc*(xd-xc)-m*xc*(yd-yc)),latex(m*(yc-yd)),latex(m*(xd-xc)),
                                latex(n*yb),latex(n),
                                latex(o*yc*(xc-xb)-o*xc*(yc-yb)),latex(o*(yb-yc)),latex(o*(xc-xb)),latex(i),latex(k)
                            ))

                # Nội dung lời giải
            hinhve = f'''\\begin{{center}}
            \\begin{{tikzpicture}}[>=stealth, scale=0.8, line width=1pt]
            \\draw[->] (-1.5, 0) -- ({xd+2}, 0) node[below] {{$x$}};
            \\draw[->] (0, -1.5) -- (0, {ya+2}) node[left] {{$y$}};
            \\node at (0,0) [below left] {{$O$}};
            \\clip (-1.5,-1.5) rectangle ({xd+1.5},{ya+1.5});
            \\fill[pattern=north east lines, pattern color=black] (-1.5,-1.5) rectangle ({xd+1.5},{ya+1.5});
            \\fill[white] (0,0) -- (0,{ya}) -- ({xb},{yb}) -- ({xc},{yc}) -- ({xd},0) -- cycle;
            \\draw[black] (-1.5,0) -- ({xd+2},0);
            \\draw[black] (0,-1.5) -- (0,{ya+2});
            \\draw[black, smooth, domain=-1.5:{xd+1.5}] plot(\\x, {{{ya}}}); % Đường y = ya
            \\draw[black, smooth, domain=-1.5:{xd+1.5}] plot(\\x, {{(({yc}-{yb})/({xc}-{xb}))*\\x + ({yc}-{xc}*({yc}-{yb})/({xc}-{xb}))}}); % Đường BC
            \\draw[black, smooth, domain=-1.5:{xd+1.5}] plot(\\x, {{(({yd}-{yc})/({xd}-{xc}))*\\x + ({yd}-{xd}*({yd}-{yc})/({xd}-{xc}))}}); % Đường CD
            \\coordinate (A) at (0,{ya});
            \\coordinate (B) at ({xb},{yb});
            \\coordinate (C) at ({xc},{yc});
            \\coordinate (D) at ({xd},0);
            \\fill (0,0) circle (0.5pt);
            \\fill (A) circle (0.5pt) node[above left] {{$A$}};
            \\fill (B) circle (0.5pt) node[above right] {{$B$}};
            \\fill (C) circle (0.5pt) node[above right] {{$C$}};
            \\fill (D) circle (0.5pt) node[above right] {{$D$}};
            \\draw[dashed, thin] ({xb},0) node[below] {{${xb}$}} -- (B);
            \\draw[dashed, thin] ({xc},0) node[below] {{${xc}$}} -- (C) -- (0,{yc}) node[left] {{${yc}$}};
            \\node[left] at (A) {{${ya}$}};
            \\node[below] at (D) {{${xd}$}};
            \\end{{tikzpicture}}
            \\end{{center}}'''

            # Nội dung lời giải
            loigiai=('Gọi số sản phẩm loại $I$ cần sản xuất là $x$ tấn; Số sản phẩm loại $II$ cần sản xuất là $y$ tấn, với $x \\ge 0$ và $y \\ge 0$. \\\\ \n'
                    'Khi đó số máy nhóm $A$ cần sử dụng là $%s$. \\\\ \n' #1
                    'Số máy nhóm $B$ cần sử dụng là $%s$. \\\\ \n' #3
                    'Số máy nhóm $C$ cần sử dụng là $%s$. \\\\ \n' #2
                    'Ta có hệ phương trình: $\\heva{&x \\ge 0 \\\\& y \\ge 0 \\\\& %s\\\\& %s \\\\& %s} \\Leftrightarrow  \\heva{& x \\ge 0 \\\\& 0 \\le y \\le %s\\\\& %s\\\\& %s.}$\\\\ \n'
                    'Vẽ các đường thẳng sau trên cùng hệ trục tọa độ $(Oxy)$: \\\\ \n'
                    '$d_1: y=%s$.\\\\ \n'
                    '$d_2: %s$.\\\\ \n'
                    '$d_3: %s$.\\\\ \n'
                    'Ta được miền nghiệm của hệ bất phương trình là phần tô đậm trong hình vẽ sau: \\\\ \n'
                    '%s' #hinhve
                    'Miền nghiệm là đa giác $OABCD$ với $O(0;0), A \\left( %s;%s \\right), B \\left( %s;%s \\right), C \\left( %s;%s \\right)$ và $D \\left( %s;%s \\right)$. \\\\ \n'
                    'Số tiền lãi là $F(x;y)=%s$ nghìn đồng. Ta có \\\\ \n'
                    '$F \\left( 0;0 \\right) =0$. \\\\ \n'
                    '$F \\left( %s;%s \\right) =%s$. \\\\ \n'
                    '$F \\left( %s;%s \\right) =%s$. \\\\ \n'
                    '$F \\left( %s;%s \\right) =%s$. \\\\ \n'
                    '$F \\left( %s;%s \\right) =%s$. \\\\ \n'
                    'Ta thấy $F(x;y)$ đạt giá trị lớn nhất tại điểm $\\left( %s;%s \\right)$. \\\\ \n'
                    'Để lãi cao nhất thì cần sản xuất $%s$ sản phẩm loại $I$ và $%s$ sản phẩm loại $II$.'
                    ' Vậy để lãi cao nhất thì cần sản xuất tổng số sản phẩm loại $I$ và $II$ là $%s+%s=%s$ sản phấm.'
                    %(
                        latex(pt111), #1
                        latex(pt333), #3
                        latex(pt222), #2
                        latex(pt11),
                        latex(pt33),
                        latex(pt22),
                        latex(yb),
                        latex(bpt1),latex(bpt2),
                        latex(yb),
                        latex(pt1), #CD
                        latex(pt2), #BC
                        str(hinhve),
                        latex(xa),latex(ya),
                        latex(xb),latex(yb),
                        latex(xc),latex(yc),
                        latex(xd),latex(yd),
                        latex(tien),
                        latex(xa),latex(ya), latex(tien_a),
                        latex(xb),latex(yb), latex(tien_b),
                        latex(xc),latex(yc), latex(tien_c),
                        latex(xd),latex(yd), latex(tien_d),
                        latex(x_tien_max),latex(y_tien_max),
                        latex(x_tien_max),latex(y_tien_max),
                        latex(x_tien_max),latex(y_tien_max),latex(x_tien_max+y_tien_max),
                        ))

                #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(x_tien_max + y_tien_max))
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac'). replace('1x','x').replace('-1x','-x'). replace('1y','y'). replace('.0',''). replace('+-','-')
            return content

