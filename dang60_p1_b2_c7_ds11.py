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


def bt_dang60_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Nghiên cứu đề bài và lời giải
            # Đề bài: Cho f(x) = ax^3 + bx^2 + c, g(x) = dx^3 + ex^2 + f. Giải f'(x) > g'(x)
            # B3: Suy nghĩ cách random: Random các hệ số a, b, d, e sao cho biệt thức của bất phương trình bậc 2 có nghiệm đẹp.

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số để tạo bài toán mới
                # Đảm bảo f'(x) - g'(x) là một tam thức bậc 2 có 2 nghiệm phân biệt
                a = random.randint(2, 4)
                d = random.randint(1, a - 1) # Để hệ số x^2 của f'-g' luôn dương

                # b và e chọn sao cho nghiệm thường là số nguyên cho đẹp
                b = random.randint(-5, 5)
                e = random.randint(1, 5)

                # Các hằng số tự do (c, f) không ảnh hưởng đạo hàm nhưng làm đề phong phú
                c_val = random.choice([r'\sqrt{3}', r'\sqrt{2}', '5', '7'])
                f_val = random.choice([r'\sqrt{3}', r'\sqrt{5}', '1', '2'])

                f_expr = a*x**3 + b*x**2
                # g_expr sử dụng Rational cho các hệ số phân số như x^2/2 trong hình
                g_expr = d*x**3 + S(e)/2 * x**2

                # Tính đạo hàm
                df = diff(f_expr, x)
                dg = diff(g_expr, x)

                # Bất phương trình f'(x) > g'(x) <=> df - dg > 0
                diff_poly = df - dg
                roots = solve(diff_poly, x)
                roots.sort()

                x1, x2 = roots

                # Chuẩn bị hiển thị LaTeX
                f_tex = f"{a}x^3 {'+' if b > 0 else ''}{b if b != 0 else ''}x^2 + {c_val}".replace('+-', '-').replace('+ -', '-').replace('1x', 'x')
                g_tex = f"{d}x^3 + \\frac{{{e}x^2}}{{2}} - {f_val}".replace('+-', '-').replace('+ -', '-').replace('1x', 'x')

                noidungcauhoi = (f"Cho $f(x) = {f_tex}$, $g(x) = {g_tex}$. Tập nghiệm của bất phương trình $f'(x) > g'(x)$ là")

                # Đáp án đúng
                da_clean = f"x \\in (-\\infty ; {latex(x1)}) \\cup ({latex(x2)} ; +\\infty)"
                da = f"${da_clean}$"

                # Tạo các đáp án nhiễu
                s = [
                    f"$( {latex(x1)} ; {latex(x2)} )$ ",
                    f"$x \\in (-\\infty ; {latex(x1)}] \\cup [{latex(x2)} ; +\\infty)$",
                    f"$x \\in (-\\infty ; {latex(x2)}) \\cup ({latex(x1)} ; +\\infty)$", # Đảo số
                    f"$(-\\infty ; {latex(x1+1)}) \\cup ({latex(x2+1)} ; +\\infty)$"
                ]

                das1 = random.choice(s); s.remove(das1)
                das2 = random.choice(s); s.remove(das2)
                das3 = random.choice(s)

                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = (f"Ta có $f'(x) = ({f_tex})' = {latex(df)}$, $g'(x) = ({g_tex})' = {latex(dg)}$. \\\\\n"
                           f"Khi đó: $f'(x) > g'(x) \\Leftrightarrow {latex(df)} > {latex(dg)}$ \\\\\n"
                           f"$\\Leftrightarrow {latex(diff_poly)} > 0 \\Leftrightarrow {da_clean}$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

