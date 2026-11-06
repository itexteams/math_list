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


def bt_dang25_p4_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số a, b, c (tránh 0 để luôn cắt 2 trục và dễ xét điểm O)
                a = random.choice([-3, -2, -1, 1, 2, 3])
                b = random.choice([-3, -2, -1, 1, 2, 3])
                c = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])

                # Random dấu bất phương trình
                ops = ['>', '<', '\\ge', '\\le']
                op_str = random.choice(ops)

                # Hàm kiểm tra tính đúng sai của bất phương trình tại 1 điểm
                def check_ineq(x_val, y_val, a, b, c, op):
                    lhs = a * x_val + b * y_val
                    if op == '>': return lhs > c
                    elif op == '<': return lhs < c
                    elif op == '\\ge': return lhs >= c
                    elif op == '\\le': return lhs <= c
                    return False

                # Sử dụng Sympy để xử lý biểu thức ax + by đẹp (tự chuyển + - thành -, 1x thành x)
                x, y_sym = sp.symbols('x y')
                expr = a*x + b*y_sym
                str_expr = sp.latex(expr)

                # Tọa độ giao điểm A, B (dùng Rational để tối giản và latex để hiển thị phân số đẹp)
                xA = Rational(c, a)
                yB = Rational(c, b)
                str_xA = latex(xA)
                str_yB = latex(yB)
                xA_float = float(c/a)
                yB_float = float(c/b)

                # Xét gốc tọa độ O(0,0)
                is_solution = check_ineq(0, 0, a, b, c, op_str)

                # Logic text khi xét điểm O(0,0)
                if is_solution:
                    str_origin = f"$x = y = 0$ là nghiệm của bất phương trình."
                    str_contain = "chứa gốc tọa độ $O$"
                else:
                    str_origin = f"$x = y = 0$ không phải là nghiệm của bất phương trình."
                    str_contain = "không chứa gốc tọa độ $O$"

                # Logic text bờ d
                if op_str in ['>', '<']:
                    str_boundary = "không bao gồm đường thẳng $d$"
                else:
                    str_boundary = "bao gồm đường thẳng $d$"

                # XỬ LÝ TIKZ
                # Tính 2 điểm xa nhau trên đường thẳng để vẽ d
                x1_tikz, x2_tikz = -6, 6
                y1_tikz = (c - a * x1_tikz) / b
                y2_tikz = (c - a * x2_tikz) / b

                # Xác định miền cần gạch chéo (miền sai)
                # Thử điểm có toạ độ y rất lớn (đỉnh trên của đồ thị)
                top_is_solution = check_ineq(0, 100, a, b, c, op_str)
                if top_is_solution:
                    # Nếu phía trên là nghiệm -> Miền sai nằm ở phía dưới
                    y_corner = -6
                else:
                    # Nếu phía trên không là nghiệm -> Miền sai nằm ở phía trên
                    y_corner = 6

                # Cấu trúc chuỗi TikZ
                tikz_code = f'''\\begin{{center}}
            \\begin{{tikzpicture}}[>=stealth, scale=0.6]
                \\draw[help lines, color=gray!30, dashed] (-4,-4) grid (4,4);
                \\draw[->,line width=1pt] (-4.2,0) -- (4.2,0) node[below] {{$x$}};
                \\draw[->,line width=1pt] (0,-4.2) -- (0,4.2) node[right] {{$y$}};
                \\node at (0.2,-0.3) {{$O$}};
                \\clip (-4,-4) rectangle (4,4);
                \\fill[pattern=north west lines, pattern color=black] ({x1_tikz}, {y1_tikz}) -- ({x2_tikz}, {y2_tikz}) -- ({x2_tikz}, {y_corner}) -- ({x1_tikz}, {y_corner}) -- cycle;
                \\draw[line width=1pt, blue] ({x1_tikz}, {y1_tikz}) -- ({x2_tikz}, {y2_tikz}) node[pos=0.7, above, sloped, black] {{$d$}};
                \\fill (0, {yB_float}) circle (1.5pt) node[below right, fill=white, inner sep=1pt] {{${str_yB}$}};
                \\fill ({xA_float}, 0) circle (1.5pt) node[above left, fill=white, inner sep=1pt] {{${str_xA}$}};
            \\end{{tikzpicture}}
            \\end{{center}}'''

                # Đề bài
                noidungcauhoi = f"Biểu diễn hình học tập nghiệm của bất phương trình ${str_expr} {op_str} {c}$."

                # Nội dung lời giải
                loigiai = f'''+ Đường thẳng $d: {str_expr} = {c}$ đi qua hai điểm $A\\left({str_xA}; 0\\right)$ và $B\\left(0; {str_yB}\\right)$. \\\\
            + {str_origin} \\\\
            + Miền nghiệm của bất phương trình là nửa mặt phẳng bờ là đường thẳng $d: {str_expr} = {c}$, {str_contain}, {str_boundary} (là miền không gạch chéo trên hình vẽ).
            {tikz_code} '''

            # Xuất câu tự luận
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\n\\loigiai{ \n'
                +str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

