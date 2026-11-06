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


def bt_dang5_p4_b1_c2_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random tần số các nhóm
        f1 = random.randint(10, 20)
        f2 = random.randint(25, 40)
        f3 = random.randint(20, 35)
        f4 = random.randint(10, 25)
        f5 = random.randint(3, 10)

        n = f1 + f2 + f3 + f4 + f5

        # Tính Q1
        vt_Q1 = n / 4
        if vt_Q1 <= f1:
            nhom_Q1 = 1
            L_Q1 = 1
            w_Q1 = 5
            cf_Q1 = 0
            f_Q1 = f1
        elif vt_Q1 <= f1 + f2:
            nhom_Q1 = 2
            L_Q1 = 6
            w_Q1 = 5
            cf_Q1 = f1
            f_Q1 = f2
        elif vt_Q1 <= f1 + f2 + f3:
            nhom_Q1 = 3
            L_Q1 = 11
            w_Q1 = 5
            cf_Q1 = f1 + f2
            f_Q1 = f3
        else:
            nhom_Q1 = 4
            L_Q1 = 16
            w_Q1 = 5
            cf_Q1 = f1 + f2 + f3
            f_Q1 = f4

        Q1 = L_Q1 + ((n/4 - cf_Q1) / f_Q1) * w_Q1

        # Tính Q3
        vt_Q3 = 3 * n / 4
        if vt_Q3 <= f1 + f2 + f3:
            nhom_Q3 = 3
            L_Q3 = 11
            w_Q3 = 5
            cf_Q3 = f1 + f2
            f_Q3 = f3
        elif vt_Q3 <= f1 + f2 + f3 + f4:
            nhom_Q3 = 4
            L_Q3 = 16
            w_Q3 = 5
            cf_Q3 = f1 + f2 + f3
            f_Q3 = f4
        else:
            nhom_Q3 = 5
            L_Q3 = 21
            w_Q3 = 5
            cf_Q3 = f1 + f2 + f3 + f4
            f_Q3 = f5

        Q3 = L_Q3 + ((3*n/4 - cf_Q3) / f_Q3) * w_Q3

        delta_Q = Q3 - Q1

        # Định dạng kết quả
        kq = str(Decimal(float(delta_Q)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        Q1_str = str(Decimal(float(Q1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        Q3_str = str(Decimal(float(Q3)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        # Câu hỏi
        noidungcauhoi = ('''Biểu đồ dưới đây biểu diễn số lượng khách hàng đặt bàn qua hình thức trực tuyến mỗi ngày trong quý $III$ năm $2022$ của một nhà hàng. Cột thứ nhất biểu diễn số ngày có từ $1$ đến $6$ lượt đặt bàn, cột thứ hai biểu diễn số ngày có từ $6$ đến $11$ lượt đặt bàn;...
        \\begin{center}
        \\begin{tikzpicture}[font=\\footnotesize,>=stealth,x=1cm,y=0.15cm]
        \\draw[->] (0,0) -- (6.5,0) node[below] {Số lượt đặt bàn};
        \\draw[->] (0,0) -- (0,37) node[above] {Số ngày};
        \\foreach \\x/\\xtext in {1/1, 2/6, 3/11, 4/16, 5/21, 6/26}
            \\draw (\\x,0.1) -- (\\x,-0.1) node[below] {\\xtext};
        \\foreach \\y in {5,10,15,20,25,30,35}
            \\draw (0.1,\\y) -- (-0.1,\\y) node[left] {\\y};
        \\draw[dashed,gray] (0,5) -- (6,5);
        \\draw[dashed,gray] (0,10) -- (6,10);
        \\draw[dashed,gray] (0,15) -- (6,15);
        \\draw[dashed,gray] (0,20) -- (6,20);
        \\draw[dashed,gray] (0,25) -- (6,25);
        \\draw[dashed,gray] (0,30) -- (6,30);
        \\draw[dashed,gray] (0,35) -- (6,35);
        \\draw[fill=gray!50] (1,0) rectangle (2,%s);
        \\node at (1.5,%s+1.5) {\\textbf{%s}};
        \\draw[fill=gray!50] (2,0) rectangle (3,%s);
        \\node at (2.5,%s+1.5) {\\textbf{%s}};
        \\draw[fill=gray!50] (3,0) rectangle (4,%s);
        \\node at (3.5,%s+1.5) {\\textbf{%s}};
        \\draw[fill=gray!50] (4,0) rectangle (5,%s);
        \\node at (4.5,%s+1.5) {\\textbf{%s}};
        \\draw[fill=gray!50] (5,0) rectangle (6,%s);
        \\node at (5.5,%s+1.5) {\\textbf{%s}};
        \\end{tikzpicture}
        \\end{center}
        Tìm khoảng tứ phân vị của mẫu số liệu ghép nhóm cho bởi biểu đồ trên'''
                         %(f1, f1, f1, f2, f2, f2, f3, f3, f3, f4, f4, f4, f5, f5, f5))

        # Tìm khoảng chứa các tứ phân vị để viết lời giải
        khoang_Q1 = f"[{L_Q1};{L_Q1+5})"
        khoang_Q3 = f"[{L_Q3};{L_Q3+5})"

        # Nội dung lời giải
        loigiai=('''Dựa vào biểu đồ ta lập được bảng ghép nhóm như sau:
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|c|}
        \\hline
        Lượt đặt bàn & $[1;6)$ & $[6;11)$ & $[11;16)$ & $[16;21)$ & $[21;26)$ \\\\
        \\hline
        Số ngày & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        Cỡ mẫu $n = %s$ và gọi $x_1, x_2, \\dots, x_{%s}$ là mẫu số liệu đã cho.\\\\
        Tứ phân vị thứ nhất của mẫu số liệu thuộc nhóm $%s$. Do đó tứ phân vị thứ nhất của mẫu số liệu là:
        $$Q_1 = %s + \\frac{\\frac{%s}{4} - %s}{%s} \\cdot 5 = %s$$
        Tứ phân vị thứ ba của mẫu số liệu thuộc nhóm $%s$. Do đó tứ phân vị thứ ba của mẫu số liệu là:
        $$Q_3 = %s + \\frac{\\frac{3 \\cdot %s}{4} - %s}{%s} \\cdot 5 = %s$$
        Vậy khoảng tứ phân vị của mẫu số liệu là: $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$.'''
                 %(f1, f2, f3, f4, f5, 
                   n, n, 
                   khoang_Q1, L_Q1, n, cf_Q1, f_Q1, Q1_str,
                   khoang_Q3, L_Q3, n, cf_Q3, f_Q3, Q3_str,
                   Q3_str, Q1_str, kq))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content

