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


def bt_dang6_p3_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # 1. Random tọa độ B' (giới hạn từ 2 đến 6 để hình vẽ không quá to)
        x0 = random.randint(2, 6)
        y0 = random.randint(2, 6)
        z0 = random.randint(2, 6)

        # 2. Định nghĩa tọa độ các đỉnh còn lại dựa vào B'
        vertices = {
            'A': (x0, 0, 0),
            'C': (0, y0, 0),
            'B': (x0, y0, 0),
            'A\'': (x0, 0, z0),
            'C\'': (0, y0, z0),
            'O\'': (0, 0, z0)
        }

        # Chọn ngẫu nhiên đỉnh để hỏi
        target_name = random.choice(list(vertices.keys()))
        a, b, c = vertices[target_name]

        # 3. Random hệ số biểu thức T = m*a + n*b + p*c
        m = random.randint(-3, 3)
        while m == 0: m = random.randint(-3, 3) # m khác 0

        n = random.randint(-3, 3)
        p = random.randint(-3, 3)

        kq = m*a + n*b + p*c

        # --- HÀM TẠO CHUỖI BIỂU THỨC T & XỬ LÝ DẤU ---
        def format_term(coef, var, is_first=False):
            if coef == 0: return ""
            abs_coef = abs(coef)
            coef_str = "" if abs_coef == 1 else str(abs_coef)

            if is_first:
                return f"-{coef_str}{var}" if coef < 0 else f"{coef_str}{var}"
            else:
                return f" - {coef_str}{var}" if coef < 0 else f" + {coef_str}{var}"

        expr_m = format_term(m, 'a', True)
        expr_n = format_term(n, 'b', False)
        expr_p = format_term(p, 'c', False)

        # Ghép chuỗi biểu thức và dọn dẹp các trường hợp sinh lỗi dấu (nếu có)
        expr_str = f"{expr_m}{expr_n}{expr_p}".replace("+ -", "- ").replace("- -", "+ ")

        # Chuỗi phép thế số
        def format_sub(coef, val):
            if coef == 0: return "0"
            if coef == 1: return f"{val}"
            if coef == -1: return f"(-{val})" if val > 0 else f"{val}"
            return f"{coef}\\cdot {val}"

        sub_str = f"{format_sub(m, a)} + {format_sub(n, b)} + {format_sub(p, c)}"
        # Fix triệt để dấu + - thành -
        sub_str = sub_str.replace("+ -", "- ").replace("- -", "+ ").replace("+ 0", "").replace("- 0", "").strip()

        # --- 4. TẠO HÌNH VẼ TIKZ ĐỘNG ---
        # Các trục tọa độ dài hơn cạnh hộp 1.5 đơn vị để vẽ mũi tên đẹp
        len_x = x0 + 1.5
        len_y = y0 + 1.5
        len_z = z0 + 1.5

        tikz_fig = f"""\\begin{{center}}
    \\begin{{tikzpicture}}[scale=0.7, >=stealth, x={{(-0.5cm,-0.4cm)}}, y={{(1cm,0cm)}}, z={{(0cm,1cm)}}, font=\\footnotesize]
        \\draw[->] (0,0,0) -- ({len_x},0,0) node[below] {{$x$}};
        \\draw[->] (0,0,0) -- (0,{len_y},0) node[right] {{$y$}};
        \\draw[->] (0,0,0) -- (0,0,{len_z}) node[above] {{$z$}};
        \\coordinate (O) at (0,0,0);
        \\coordinate (A) at ({x0},0,0);
        \\coordinate (C) at (0,{y0},0);
        \\coordinate (B) at ({x0},{y0},0);
        \\coordinate (O') at (0,0,{z0});
        \\coordinate (A') at ({x0},0,{z0});
        \\coordinate (C') at (0,{y0},{z0});
        \\coordinate (B') at ({x0},{y0},{z0});
        \\draw[red, thick] (O') -- (A') -- (B') -- (C') -- cycle;
        \\draw[red, thick] (A) -- (A');
        \\draw[red, thick] (B) -- (B');
        \\draw[red, thick] (C) -- (C');
        \\draw[red, thick] (A) -- (B) -- (C);
        \\node[left] at (O) {{$O$}};
        \\node[left] at (A) {{$A$}};
        \\node[right] at (C) {{$C$}};
        \\node[below] at (B) {{$B$}};
        \\node[left] at (O') {{$O'$}};
        \\node[left] at (A') {{$A'$}};
        \\node[right] at (C') {{$C'$}};
        \\node[right] at (B') {{$B'$}};
    \\end{{tikzpicture}}
    \\end{{center}}"""
        # Đề bài (chứa luôn mã TikZ)
        noidungcauhoi = f"Trong không gian $Oxyz$, cho hình hộp chữ nhật $OABC.O'A'B'C'$ như hình vẽ, biết $B'({x0}; {y0}; {z0})$. \n{tikz_fig}\nBiết tọa độ đỉnh ${target_name}$ là $(a;b;c)$. Giá trị $T = {expr_str}$ bằng bao nhiêu?"

        # Nội dung lời giải
        loigiai = f"Dựa vào hình vẽ và tọa độ $B'({x0}; {y0}; {z0})$, ta xác định được tọa độ đỉnh ${target_name}$ là $({a};{b};{c}) \\longrightarrow a = {a}; b = {b}; c = {c}$. \\\\\nThay vào biểu thức ta có: $T = {sub_str} = {kq}$."
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content

