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


def bt_dang49_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp tìm các tham số đảm bảo nghiệm luôn nguyên và hợp lý
                while True:
                    m1 = random.randint(-5, 5)
                    m2 = random.randint(-5, 5)
                    if m1 == m2: continue

                    c1 = random.randint(-4, 4)
                    x0 = random.randint(-3, 3)
                    # Để M1, M2 cách đều I thì I phải thuộc trung trực của M1M2
                    y0 = x0 - (m1 + m2 + c1)

                    # Bình phương khoảng cách MI
                    mi2 = (m1 - x0)**2 + (-m1 - c1 - y0)**2

                    # Chọn R sao cho MA^2 = MI^2 - R^2 > 0 và R là số nguyên
                    valid_R_sq = [r2 for r2 in range(1, mi2) if int(math.sqrt(r2))**2 == r2]
                    if not valid_R_sq: continue
                    R = int(math.sqrt(random.choice(valid_R_sq)))

                    ma2 = mi2 - R**2
                    if ma2 <= 0: continue
                    break

                # Tính tọa độ y của M
                y1 = -m1 - c1
                y2 = -m2 - c1

                # Phương trình đường tròn (C)
                c_c = x0**2 + y0**2 - R**2
                def format_circle(x0, y0, c_c):
                    s = "x^2 + y^2"
                    if x0 != 0: s += f" - {2*x0}x" if x0 > 0 else f" + {-2*x0}x"
                    if y0 != 0: s += f" - {2*y0}y" if y0 > 0 else f" + {-2*y0}y"
                    if c_c > 0: s += f" + {c_c}"
                    elif c_c < 0: s += f" - {-c_c}"
                    return s + " = 0"
                circ_eq = format_circle(x0, y0, c_c)

                # Phương trình đường thẳng d
                def format_line(c1):
                    if c1 > 0: return f"x + y + {c1} = 0"
                    elif c1 < 0: return f"x + y - {-c1} = 0"
                    else: return "x + y = 0"
                line_eq = format_line(c1)

                # Chu vi và cạnh
                MA_sym = sp.sqrt(ma2)
                peri_sym = 2*(R + MA_sym)
                latex_peri = latex(peri_sym)
                latex_half_peri = latex(R + MA_sym)
                latex_MA = latex(MA_sym)

                # Xử lý format cho chuỗi phương trình
                def format_coord_y(c1):
                    if c1 > 0: return f"-{c1}-m"
                    elif c1 < 0: return f"{-c1}-m"
                    else: return "-m"
                y_m_str = format_coord_y(c1)

                def format_x0_minus_m(x0):
                    return f"{x0}-m" if x0 != 0 else "-m"

                yc = y0 + c1
                def format_m_plus(A):
                    if A > 0: return f"m+{A}"
                    elif A < 0: return f"m-{-A}"
                    else: return "m"

                # Tạo phương trình bậc 2 theo m
                m_var = symbols('m')
                A_eq = 2
                B_eq = 2*yc - 2*x0
                C_eq = x0**2 + yc**2 - mi2
                eq_expr = A_eq*m_var**2 + B_eq*m_var + C_eq
                latex_eq = latex(eq_expr) + " = 0"

                # Các đáp án trắc nghiệm
                def pt(x_val, y_val): return f"M({x_val}; {y_val})"
                da = f"${pt(m1, y1)}$ hoặc ${pt(m2, y2)}$"

                # Chế tạo đáp án nhiễu (sai)
                fakes = set()
                fakes.add(f"${pt(-m1, y1)}$ hoặc ${pt(-m2, y2)}$")
                fakes.add(f"${pt(m1, -y1)}$ hoặc ${pt(m2, -y2)}$")
                fakes.add(f"${pt(y1, m1)}$ hoặc ${pt(y2, m2)}$")
                fakes.add(f"${pt(m1+1, y1-1)}$ hoặc ${pt(m2+1, y2-1)}$")
                fakes.add(f"${pt(m1-1, y1+1)}$ hoặc ${pt(m2-1, y2+1)}$")
                fakes.discard(da)
                fakes_list = list(fakes)
                random.shuffle(fakes_list)

                das1 = fakes_list[0]
                das2 = fakes_list[1]
                das3 = fakes_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = f'''Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho đường tròn $(C): {circ_eq}$. Gọi $I$ là tâm và $R$ là bán kính của $(C)$. Tìm tọa độ điểm $M$ thuộc đường thẳng $d: {line_eq}$ sao cho từ $M$ kẻ được hai tiếp tuyến $MA,MB$ đến $(C)$ ($A, B$ là các tiếp điểm) thỏa mãn tứ giác $MAIB$ có chu vi bằng ${latex_peri}$.'''

                # Gán True cho đáp án đúng
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                               \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.6cm,y=0.6cm]
                	\\clip(-3,-1) rectangle (9,6);
                	\\draw (3.,2.)-- (3.,5.);
                	\\draw (6.,2.)-- (3.,2.);
                	\\draw(3.,2.) circle (1.8cm);
                	\\draw (0.,5.)-- (6.,5.);
                	\\draw (6.,5.)-- (6.,0.);
                	\\draw (3.,2.)-- (6.,5.);
                	\\draw (4.,6.)-- (9.35,3.289);
                	\\draw (8.3,4.9) node[anchor=north west] {$d$};
                	\\draw (2.6,2) node[anchor=north west] {$I$};
                	\\draw (6.,6.) node[anchor=north west] {$M$};
                	\\draw (4,3.3) node[anchor=north west] {$H$};
                	\\draw (2.66,6) node[anchor=north west] {$A$};
                	\\draw (6,2.7) node[anchor=north west] {$B$};
                	\\draw (3.,5.)-- (6.,2.);
                \\end{tikzpicture}
                \\end{center}'''
                    f'''Ta có $C_{{MAIB}} = MA + AI + IB + BM = 2(MA + AI) = {latex_peri}$. \\\\
            Suy ra $MA + AI = {latex_half_peri} \\Leftrightarrow MA = {latex_half_peri} - AI = {latex_MA}$. \\\\
            Do đó $MI = \\sqrt{{AM^2 + AI^2}} = \\sqrt{{{mi2}}}$. \\\\
            Do $M \\in d$ nên $M(m; {y_m_str})$. Ta có \\\\
            $MI = \\sqrt{{{mi2}}} \\Leftrightarrow \\sqrt{{({format_x0_minus_m(x0)})^2 + ({format_m_plus(yc)})^2}} = \\sqrt{{{mi2}}}$ \\\\
            $\\Leftrightarrow {latex_eq}$ \\\\
            $\\Leftrightarrow \\left[ \\begin{{matrix}} m = {m1} \\\\ m = {m2} \\end{{matrix}} \\right.$ \\\\
            Vậy {da}.''')

                # Xử lý hiển thị - - thành + và + - thành - để LaTeX đẹp nhất
                noidungcauhoi = noidungcauhoi.replace('+ -', '-').replace('- -', '+').replace('+-', '-')
                loigiai = loigiai.replace('+ -', '-').replace('- -', '+').replace('+-', '-')


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

