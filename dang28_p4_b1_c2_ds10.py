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


def bt_dang28_p4_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp tìm a, b, c nguyên tố cùng nhau (chuẩn hóa dạng ax + by = c với a > 0)
                while True:
                    a = random.randint(1, 4)
                    b = random.randint(-4, 4)
                    c = random.randint(-4, 4)
                    if b == 0 or c == 0: continue
                    if math.gcd(math.gcd(abs(a), abs(b)), abs(c)) == 1:
                        break

                # Tọa độ giao điểm với trục tọa độ (Dùng Rational để hiển thị phân số LaTeX đẹp)
                xA = Rational(c, a)
                yB = Rational(c, b)

                # Tìm một điểm C nguyên (xC, yC) nằm trong miền nghiệm (thỏa mãn ax + by > c)
                xC, yC = 0, 0
                found = False
                for r in range(0, 10):
                    for i in range(-r, r+1):
                        for j in range(-r, r+1):
                            if a*i + b*j > c:
                                xC, yC = i, j
                                found = True
                                break
                        if found: break
                    if found: break

                # Hàm xử lý dấu + - chuẩn mực cho biểu thức ax + by
                def clean_expr(a, b):
                    term1 = f"{a}x" if a not in [1, -1] else ("x" if a == 1 else "-x")
                    term2 = f"+ {b}y" if b > 0 else f"- {abs(b)}y"
                    if b == 1: term2 = "+ y"
                    if b == -1: term2 = "- y"
                    return f"{term1} {term2}"

                # Hàm đóng ngoặc cho số âm khi thay số vào biểu thức tính toán
                def term_eval(val):
                    return f"({val})" if val < 0 else f"{val}"

                eq_str = clean_expr(a, b)
                val_C = a*xC + b*yC
                kq = a + b + c

                # Tạo mã TikZ để vẽ hình
                # Miền gạch chéo là miền KHÔNG PHẢI nghiệm (tức là ax + by < c)
                tikz_str = f"""\\begin{{center}}
            \\begin{{tikzpicture}}[>=stealth, scale=0.6]
            \\clip (-5.2,-5.2) rectangle (5.2,5.2);"""
                # Nếu b > 0, miền ax+by < c nằm bên dưới đường thẳng
                if b > 0:
                    tikz_str += f"\\fill[pattern=north west lines, pattern color=black!60] (-6,-6) -- (6,-6) -- (6, { (c-a*6)/b }) -- (-6, { (c-a*-6)/b }) -- cycle;\n"
                # Nếu b < 0, miền ax+by < c nằm bên trên đường thẳng
                else:
                    tikz_str += f"\\fill[pattern=north west lines, pattern color=black!60] (-6,6) -- (6,6) -- (6, { (c-a*6)/b }) -- (-6, { (c-a*-6)/b }) -- cycle;\n"

                # Định vị nhãn cho các điểm cắt
                pos_x = "below right" if c/a > 0 else "below left"
                pos_y = "above right" if c/b > 0 else "below right"

                tikz_str += f"""\\draw[->] (-5,0) -- (5,0) node[below] {{$x$}};
            \\draw[->] (0,-5) -- (0,5) node[left] {{$y$}};
            \\node at (0,0) [below left] {{$O$}};
            \\draw[thick, blue] (-6, { (c-a*-6)/b }) -- (6, { (c-a*6)/b });
            \\fill ({float(c/a)},0) circle (1.5pt) node[{pos_x}] {{\\footnotesize ${latex(xA)}$}};
            \\fill (0,{float(c/b)}) circle (1.5pt) node[{pos_y}] {{\\footnotesize ${latex(yB)}$}};
            \\end{{tikzpicture}}
            \\end{{center}}"""

                # Tạo các đáp án trắc nghiệm
                du = [f'${kq}$']
                da = random.choice(du)

                s = [f'${kq+1}$', f'${kq+2}$', f'${kq+3}$', f'${kq-1}$', f'${kq-2}$', f'${kq-3}$']
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Đề bài
                noidungcauhoi = f"Bất phương trình bậc nhất hai ẩn có miền nghiệm như hình dưới đây (phần không bị gạch chéo) là bất phương trình có dạng $ax + by \\ge c$ (với $a>0$, $a, b, c \\in \\mathbb{{Z}}$ và có ước chung lớn nhất bằng $1$). Tính $a+b+c$. {tikz_str}"

                # Cấu trúc chọn lựa A, B, C, D
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Lời giải
                loigiai = f'''Đường thẳng $(d)$ đi qua hai điểm $A\\left({latex(xA)}; 0\\right)$ và $B\\left(0; {latex(yB)}\\right)$ có phương trình: ${eq_str} = {c}$.\\\\
            Xét điểm $C({xC}; {yC})$ thuộc miền nghiệm của bất phương trình ta có: ${a} \\cdot {term_eval(xC)} + {term_eval(b)} \\cdot {term_eval(yC)} = {val_C} > {c}$ nên bất phương trình bậc nhất hai ẩn cần tìm là ${eq_str} \\ge {c}$.\\\\
            Vậy ta có $a={a}, b={b}, c={c} \\Rightarrow a+b+c = {a} + {term_eval(b)} + {term_eval(c)} = {kq}$.'''


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

