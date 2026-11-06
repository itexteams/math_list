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


def bt_dang40_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Chọn ngẫu nhiên số tử số lẻ (ví dụ: 121, 141, 161, 181, 201) sao cho khi chia cho 60 và nhân 60 sẽ ra số lẻ lần pi
                # Số lẻ lần pi tức là van sẽ ở vị trí cao nhất (quay nửa vòng lẻ)
                tuso = random.choice([121, 141, 161, 181, 201])

                # Bán kính bánh xe (cm)
                R = random.choice([50, 55, 58, 60, 65])

                # Độ dày lốp xe (cm)
                d = random.choice([2, 3, 4])

                # Tính toán các giá trị lượng giác và vị trí cho lời giải
                goc_1s = Rational(tuso, 60) # tử số / 60 * pi
                goc_1phut = tuso # tuso * pi rad
                goc_do = goc_1phut * 180
                so_vong_float = float(goc_1phut) / 2
                so_vong_str = str(Decimal(str(so_vong_float)).normalize()).replace('.', ',')

                # Khoảng cách lúc cao nhất là 2 * R + d
                ans_val = 2 * R + d
                kq = '%s cm' % ans_val

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai (các vị trí đặc biệt khác: thấp nhất d, tại tâm R + d, hoặc tính sai)
                s = [
                    '$%s cm$' % (2 * R),
                    '$%s cm$' % (R + d),
                    '$%s cm$' % d,
                    '$%s cm$' % R,
                    '$%s cm$' % (R + 2 * d)
                ]

                # Lọc bỏ giá trị trùng đáp án đúng nếu có
                s = [item for item in s if item != da]
                s = list(set(s)) # loại bỏ trùng lặp trong s

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]
                hinhve=r'''	\scalebox{0.6}{ \begin{tikzpicture}[>=stealth]
            	\shade[shading=radial] (-1.5,-2) rectangle (1.5,-1.6);
            	\shade[shading=radial] (4.5,-2) rectangle (7.5,-1.6);
            	\def\Radius{1.5cm}
            	\draw[blue] (0, 0) circle[radius=\Radius];
            	\draw[line width=4pt] (0,0) circle[radius=\Radius+0.15cm];
            	\begin{scope}[opacity=0.35]
            		\foreach \a in {0, 15, ..., 350} {
            			\draw[color=gray!75!black] (0, 0) -- (\a:\Radius);
            			\draw[black] (0, 0) -- (\a+1.5:\Radius);
            			\draw[gray] (0, 0) -- (\a+3:\Radius);
            			\draw[gray!50] (0, 0) -- (\a+4.5:\Radius);
            		}
            	\end{scope}
            	\foreach \h in {0, 60, ..., 300} {
            		\draw[color=black,line width=0.5mm,rotate around={\h:(0,0)}] (0,0) edge[-,bend left=40] (0.2cm,0) edge[-,bend right=40] (0.2cm,0);
            	}
            	\draw[line width=1pt] (0,0) circle[radius=0.2cm];
            	\draw[line width=4pt,rounded corners=1pt,rotate=0] (1.68,0.6)--(1.94,0.54);
            	\draw[line width=0.3mm,yellow!60!black] (1.8,0) arc (0:150:1.8cm)--(0,0);
            	\draw[line width=0.5mm,yellow!60!black] (1.8,0) arc (0:160:1.8cm);
            	\begin{scope}[opacity=0.35]
            		\foreach \b in {0, 15, ..., 360} {
            			\draw[color=gray!75!black,rotate around={\b:(6,0)}] (6, 0) -- (7.5,0);
            			\draw[black,rotate around={\b+1.5:(6,0)}] (6, 0) -- (7.5,0);
            			\draw[gray,rotate around={\b+3:(6,0)}] (6, 0) -- (7.5,0);
            			\draw[gray!50,rotate around={\b+4.5:(6,0)}] (6, 0) -- (7.5,0);
            		}
            	\end{scope}
            	\draw[blue] (6, 0) circle[radius=\Radius];
            	\draw[line width=4pt] (6, 0) coordinate (A) circle[radius=\Radius+0.15cm];
            	draw[line width=0.5mm,yellow!60!black] (6,1. arc (90:200:1.8cm);
            	\draw[line width=1pt] (0,0.2cm)--(2.2,0.5cm) (0,-0.2cm)--(2.2,-0.5cm);
            	\draw[line width=2pt] (2.2,0)--(2.6,-0.6) (2.2,0)--(1.8,0.6);
            	\draw[line width=1mm,rounded corners=8pt,rotate around={25:(6,0)}] (6,0)--(6,1.3cm)--++(80:2.1cm);
            	\draw[line width=1mm,rounded corners=8pt,rotate around={27:(6,0)}] (6,0)--(6,1.3cm)--++(80:2.1cm);
            	\draw[line width=1mm,rounded corners=8pt,rotate around={26:(6,0)}] (6,0)--(6,1.3cm)--++(80:2.1cm) coordinate (a);
            	\draw[line width=1.5mm] (a)--++(-80:0.15cm)--++(0:0.5cm)--++(180:0.05cm) coordinate (b);
            	\draw[line width=1.1mm,rounded corners=4pt] (b)--++(-30:0.6cm) coordinate (c)--++(-160:0.4cm) (b)--++(150:0.6cm) coordinate (d)--++(200:0.4cm);
            	\draw[line width=0.4mm,rounded corners=0pt] (c)--++(-95:0.1cm)--++(-160:0.25cm) (d)--++(-95:0.1cm)--++(200:0.25cm);
            	\draw[line width=2mm,rotate around={35:(2.2,0)}] (2.2,0)--++(3.7,0)--++(75:0.4cm)--++(155:3.5) coordinate (e)--(2.2,0);
            	\draw[line width=1mm] (0,0)--(2.2,0) (0,0)--(45:2.5cm) (0,0)--(46.5:2.5) (0,0)--(2:2.2);
            	\draw[line width=1.2mm] (e)--++(106:0.9cm)--++(-74:0.1cm) coordinate (d);
            	\foreach \c in {0, 72, ..., 288} {\draw[color=red,line width=1.8mm,rotate around={\c:(2.2,0)}] (2.2,0) edge[-,bend left=30] (2.69,0);}
            	\draw[line width=2pt] (2.2,0) circle[radius=0.5cm];
            	\fill (2.2,0) circle[radius=0.1cm];
            	\draw[line width=4pt,rounded corners=1pt,rotate=0] (2.4,-0.58)--(2.68,-0.56);
            	\draw[line width=2pt] (2.2,0)--(2.6,-0.6);
            	\shade[top color=white,bottom color=black,rounded corners=2pt,rotate around={10:(d)}] (d)--++(220:2mm)--++(100:2mm)--++(180:3mm)--++(110:1.5mm)--++(160:2mm)--++(110:3.5mm) coordinate (i)--++(-15:10mm)--++(-5:5mm)--++(-20:3mm) coordinate (j)--++(-50:0.7mm)--++(180:4mm)--++(170:1mm)--++(-175:2mm)--(d);
            	\shade[top color=gray!50,bottom color=black,rounded corners=2pt,rotate around={10:(d)}] (d)--++(220:2mm)--++(100:2mm)--++(180:3mm)--++(110:1.5mm)--++(160:2mm)--++(110:3.5mm)--++(-50:4.5mm)--++(-3:13mm)--++(-10:2mm)--++(180:4mm)--++(170:1mm)--++(-175:2mm)--(d);
            	\filldraw[black] (0,0) circle (2pt) (6,0) circle (2pt);
            	\draw[line width=0.3mm] (0,0)--++(105:2cm)--++(-2:0.7cm) coordinate (g)--+(-10:1.5cm) (g)--(0,0);
            	\shade[top color=gray!10!white,bottom color=gray] (-0.8cm,1.9cm)--++(-3:1.4cm) arc (-90:90: 0.4mm)--++(174:1.4cm) arc (90:270: 0.65mm);
            	\shade[top color=gray!20,bottom color=black] (-0.8cm,1.9cm)--++(-3:1.4cm) arc (-90:90: 0.4mm)--++(177:1.4cm) arc (90:270: 0.4mm);
            \end{tikzpicture} }'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Khi xe đạp di chuyển, van của bánh xe quay quanh trục của bánh xe theo chiều kim đồng hồ với vận tốc không đổi là $\frac{%s}{60}\\pi$ rad/s. Ban đầu van nằm ở vị trí gần mặt đất nhất. Biết bán kính bánh xe là $%s$cm và độ dày của lốp xe $%s$cm. Hỏi sau một phút di chuyển, khoảng cách từ van đến mặt đất là bao nhiêu cm? (kết quả làm tròn đến hàng đơn vị).}{%s}'''
                                 % (latex(tuso), latex(R), latex(d),hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Bánh xe quay $1$ giây được $\\frac{%s}{60}\\pi$ rad. Do đó quay một phút được $%s\\pi$ rad. \\\\
                             Ta biết $\\pi \\text{(rad)} = 180^\\circ$, do đó $%s\\pi \\text{(rad)} = %s^\\circ$ \\\\
                             Do đó bánh xe quay được $%s$ (vòng) \\\\
                             Vậy lúc đó van xe đang ở vị trí cao nhất so với mặt đất, cách mặt đất là $%s \\cdot 2 + %s = %s$ (cm).'''
                           % (latex(tuso), latex(goc_1phut), latex(goc_1phut), latex(goc_do), so_vong_str, latex(R), latex(d), latex(ans_val)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(ans_val))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

