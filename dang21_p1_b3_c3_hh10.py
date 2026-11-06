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


def bt_dang21_p1_b3_c3_hh10(self):
            # Khai báo biến
            def generate_problem():
                x, y, t = symbols('x y t', real=True)

                # Bước 1: Chọn tâm I và bán kính R trước để đảm bảo số đẹp
                xI_val = random.randint(-4, 4)
                yI_val = random.randint(-4, 4)
                R_val = random.choice([3, 4, 5, 10])

                # Bước 2: Tạo đường thẳng d1 đi qua I
                while True:
                    a1 = random.randint(-3, 3)
                    b1 = random.randint(-3, 3)
                    if a1 != 0 or b1 != 0: break
                c1 = -(a1 * xI_val + b1 * yI_val)
                d1_expr = a1*x + b1*y + c1

                # Bước 3: Tạo đường thẳng d2 tiếp xúc (C)
                pythagorean_triples = [(3, 4), (4, 3), (5, 12), (12, 5), (8, 15), (15, 8)]
                a2, b2 = random.choice(pythagorean_triples)
                if random.random() > 0.5: a2 = -a2
                if random.random() > 0.5: b2 = -b2

                dist_val = R_val * int(sp.sqrt(a2**2 + b2**2))
                c2 = random.choice([dist_val - (a2 * xI_val + b2 * yI_val), -dist_val - (a2 * xI_val + b2 * yI_val)])
                d2_expr = a2*x + b2*y + c2

                # Bước 4: Chọn điểm A sao cho IA = R
                A_val = (xI_val + R_val, yI_val) if random.random() > 0.5 else (xI_val, yI_val + R_val)

                return d1_expr, d2_expr, A_val, xI_val, yI_val, R_val

            # Khởi tạo dữ liệu
            d1, d2, A, xI, yI, R = generate_problem()
            x, y, t = symbols('x y t', real=True)

            # Lấy hệ số d1 và tham số hóa
            coeffs1 = d1.as_coefficients_dict()
            a1, b1, c1 = coeffs1.get(x, 0), coeffs1.get(y, 0), coeffs1.get(1, 0)

            if a1 != 0:
                I_ts = (Rational(-b1, a1)*t + Rational(-c1, a1), t)
            else:
                I_ts = (t, Rational(-c1, b1))

            # Lấy hệ số d2
            coeffs2 = d2.as_coefficients_dict()
            a2, b2, c2 = coeffs2.get(x, 0), coeffs2.get(y, 0), coeffs2.get(1, 0)
            mau_so_sq = a2**2 + b2**2

            # Phương trình d(I, d2)^2 = IA^2
            tu_so_dist_sq = (a2*I_ts[0] + b2*I_ts[1] + c2)**2
            IA_sq = (I_ts[0] - A[0])**2 + (I_ts[1] - A[1])**2
            eq = sp.Eq(tu_so_dist_sq / mau_so_sq, IA_sq)
            solutions = solve(eq, t)

            t_fix = solutions[0]
            for sol in solutions:
                if simplify(I_ts[0].subs(t, sol)) == xI and simplify(I_ts[1].subs(t, sol)) == yI:
                    t_fix = sol
                    break

            # --- Chuẩn bị hiển thị ---
            def fix_sign(expr):
                if isinstance(expr, str):
                    return expr.replace("+ -", "- ").replace("- -", "+ ").replace("- 0", "")
                return fix_sign(latex(expr))

            noidungcauhoi = (f"Trong mặt phẳng với hệ tọa độ $Oxy$, cho hai đường thẳng $d_1: {fix_sign(d1)} = 0$, "
                             f"$d_2: {fix_sign(d2)} = 0$ và điểm $A({A[0]}; {A[1]})$. "
                             f"Phương trình đường tròn $(C)$ có tâm thuộc $d_1$, đi qua điểm $A$ và tiếp xúc với $d_2$ là")

            pt_chuan = fix_sign(f"(x - {xI})^2 + (y - {yI})^2 = {R**2}")
            da_d = "\\True $" + pt_chuan + "$"
            list_1 = [da_d, 
                      f"$(x + {xI})^2 + (y + {yI})^2 = {R**2}$", 
                      f"$(x - {xI})^2 + (y - {yI})^2 = {R**2 + 5}$", 
                      f"$(x - {A[0]})^2 + (y - {A[1]})^2 = {R**2}$"]
            random.shuffle(list_1)

            # LỜI GIẢI CHI TIẾT (Bổ sung bước thay số cụ thể)
            loigiai = (f"Gọi $I$ là tâm của đường tròn $(C)$. Do $I \\in d_1$ nên tọa độ của $I$ có dạng $I({latex(I_ts[0])}; {latex(I_ts[1])})$. \\\\\n"
                       f"Đường tròn $(C)$ đi qua $A$ và tiếp xúc với $d_2$ nên ta có: $d(I, d_2) = IA$. \\\\\n"
                       f"$\\Leftrightarrow \\frac{{|{a2 if a2!=1 else ''}({latex(I_ts[0])}) {'+' if b2>0 else ''} {b2 if b2!=1 else ''}({latex(I_ts[1])}) {'+' if c2>0 else ''} {c2 if c2!=0 else ''}|}}{{\\sqrt{{{a2}^2 + ({b2})^2}}}} = \\sqrt{{({latex(I_ts[0])} - ({A[0]}))^2 + ({latex(I_ts[1])} - {A[1]})^2}}$ \\\\\n"
                       f"$\\Leftrightarrow \\frac{{|{latex(expand(a2*I_ts[0] + b2*I_ts[1] + c2))}|}}{{\\sqrt{{{mau_so_sq}}}}} = \\sqrt{{{latex(simplify(IA_sq))}}}$ \\\\\n"
                       f"Bình phương hai vế ta được: $\\frac{{({latex(expand(a2*I_ts[0] + b2*I_ts[1] + c2))})^2}}{{{mau_so_sq}}} = {latex(simplify(IA_sq))}$. \\\\\n"
                       f"Giải phương trình trên ta được $t = {latex(t_fix)}$. \\\\\n"
                       f"Với $t = {latex(t_fix)} \\Rightarrow I({xI}; {yI})$ và bán kính $R = IA = {R}$. \\\\\n"
                       f"Vậy phương trình đường tròn $(C)$ là: ${pt_chuan}$.")

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -','+').replace('+ -','-').replace('- +','-')
            return content

