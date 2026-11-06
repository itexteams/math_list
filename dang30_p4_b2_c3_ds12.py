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


def bt_dang30_p4_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Thiết lập các thông số random
            x_c = random.randint(0, 2) 
            dist_left = random.randint(2, 3)
            dist_right = random.randint(2, 3)

            x_1 = x_c - dist_left  # Cận dưới
            x_2 = x_c + dist_right # Cận trên

            y_1 = random.randint(2, 4) 
            y_2 = random.randint(2, 4) 

            # Tính phương trình đường thẳng f1, f2
            m1 = Rational(0 - y_1, x_c - x_1)
            f1 = simplify(m1 * (x - x_c))

            m2 = Rational(y_2 - 0, x_2 - x_c)
            f2 = simplify(m2 * (x - x_c))

            # B2: Tính tích phân
            int1 = integrate(f1, (x, x_1, x_c))
            int2 = integrate(f2, (x, x_c, x_2))
            kq_phan_so = int1 + int2
            kq_latex = latex(kq_phan_so)

            # B4: Tạo các đáp án nhiễu
            da_dung = f'\\True ${kq_latex}$'
            s = set()
            while len(s) < 3:
                sai_val = random.choice([kq_phan_so + Rational(1, 2), 
                                         kq_phan_so - Rational(1, 2), 
                                         kq_phan_so + 1, 
                                         Rational(random.randint(5, 19), 2)])
                if sai_val != kq_phan_so:
                    s.add(f'${latex(sai_val)}$')

            list_all = [da_dung] + list(s)
            random.shuffle(list_all)

            # --- Tạo mã TikZ cho đồ thị (Đã xóa số 0 ở gốc tọa độ) ---
            max_y = max(y_1, y_2)
            tikz_code = f"""\\begin{{center}}
            \\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick] 
                \\draw[->] ({x_1-1},0) -- ({x_2+1},0) node[below] {{$x$}};
                \\draw[->] (0,-1) -- (0,{max_y+1}) node[left] {{$y$}};
                \\draw[fill=black] (0,0) circle (1pt);
                \\draw[thick] ({x_1},{y_1}) -- ({x_c},0) -- ({x_2},{y_2});
                \\draw[dashed] ({x_1},0) node[below] {{${x_1}$}} -- ({x_1},{y_1}) -- (0,{y_1}) node[right] {{${y_1}$}};
                \\draw[dashed] ({x_2},0) node[below] {{${x_2}$}} -- ({x_2},{y_2}) -- (0,{y_2}) node[left] {{${y_2}$}};
                \\node[below] at ({x_c},0) {{${x_c}$}};
                \\node[below left] at (0,0) {{$O$}};
            \\end{{tikzpicture}}
            \\end{{center}}"""

            # Nội dung câu hỏi
            noidungcauhoi = f"Đường gấp khúc trong hình vẽ bên là đồ thị hàm số $y=f(x)$ trên đoạn $[{x_1};{x_2}]$. Tính $\\int_{{{x_1}}}^{{{x_2}}} f(x)dx$." + tikz_code

            # Nội dung lời giải (Đã thêm \left( và \right))
            # Sử dụng replace để đảm bảo các ngoặc đơn trong latex được bọc bởi \left \right
            f1_latex = latex(f1).replace("(", "\\left(").replace(")", "\\right)")
            f2_latex = latex(f2).replace("(", "\\left(").replace(")", "\\right)")

            loigiai = f"""Trên đoạn $[{x_1};{x_c}]$, đồ thị hàm số $y=f(x)$ là đường thẳng đi qua $\\left({x_1};{y_1}\\right)$ và $\\left({x_c};0\\right) \\Rightarrow y = {f1_latex}$. \\\\
            Trên đoạn $[{x_c};{x_2}]$, đồ thị hàm số $y=f(x)$ là đường thẳng đi qua $\\left({x_c};0\\right)$ và $\\left({x_2};{y_2}\\right) \\Rightarrow y = {f2_latex}$. \\\\
            Do đó:
            $\\int_{{{x_1}}}^{{{x_2}}} f(x) \\text{{d}}x = \\int_{{{x_1}}}^{{{x_c}}} \\left( {f1_latex} \\right) \\text{{d}}x + \\int_{{{x_c}}}^{{{x_2}}} \\left( {f2_latex} \\right) \\text{{d}}x = {latex(int1)} + {latex(int2)} = {kq_latex}$."""

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

