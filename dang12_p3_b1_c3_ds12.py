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


def bt_dang12_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            def generate_data():
                while True:
                    # 1. Random hệ số f''(x) sao cho nguyên đẹp
                    a = random.choice([12, -12, 24, -24])
                    b = random.choice([6, -6, 12, -12])
                    c = random.choice([2, -2, 4, -4, 6, -6])
                    f_double_prime = a*x**2 + b*x + c

                    # 2. Random các giá trị x1, x2, x3 khác nhau
                    points = random.sample(range(-2, 4), 3)
                    x1, x2, x3 = points[0], points[1], points[2]

                    # 3. Random giá trị f(x1) và f(x2)
                    val_f_x1 = random.randint(-5, 10)
                    val_f_x2 = random.randint(-5, 10)

                    # 4. Tính toán tìm f(x)
                    f_prime_part = integrate(f_double_prime, x)
                    f_x_part = integrate(f_prime_part, x)

                    from sympy import solve
                    C1, C2 = symbols('C1 C2')
                    eq1 = f_x_part.subs(x, x1) + C1*x1 + C2 - val_f_x1
                    eq2 = f_x_part.subs(x, x2) + C1*x2 + C2 - val_f_x2
                    sol = solve((eq1, eq2), (C1, C2))

                    if not sol: continue

                    c1_val = sol[C1]
                    c2_val = sol[C2]

                    f_final = f_x_part + c1_val*x + c2_val
                    kq_final = f_final.subs(x, x3)

                    # 6. KIỂM TRA ĐIỀU KIỆN 4 KÝ TỰ
                    if kq_final.is_integer and len(str(int(kq_final))) <= 4:
                        return {
                            'f_dp': f_double_prime,
                            'x1': x1, 'x2': x2, 'x3': x3,
                            'v1': val_f_x1, 'v2': val_f_x2,
                            'f_p_p': f_prime_part, 'f_x_p': f_x_part,
                            'c1': c1_val, 'c2': c2_val,
                            'f_f': f_final, 'kq': int(kq_final)
                        }

            data = generate_data()

            # Tạo đáp án
            da_d = f"${data['kq']}$"
            s = set()
            while len(s) < 3:
                offset = random.choice([-10, 10, -5, 5, -2, 2, 15, -15])
                nhieu = data['kq'] + offset
                if nhieu != data['kq']:
                    s.add(f"${nhieu}$")
            list_ans = ['\\True ' + da_d] + list(s)
            random.shuffle(list_ans)

            # Hàm bổ trợ hiển thị hệ số C1 trong lời giải (để tránh 1C1 hoặc 0C1 kỳ cục)
            def format_c1(val):
                if val == 0: return "0"
                if val == 1: return "C_1"
                if val == -1: return "-C_1"
                return f"{val}C_1"

            # Nội dung câu hỏi
            noidungcauhoi = (f"Cho hàm số $y = f(x)$ có đạo hàm cấp hai trên $\\mathbb{{R}}$ thỏa mãn "
                             f"$f''(x) = {latex(data['f_dp'])}$, $f({data['x1']}) = {data['v1']}$ và $f({data['x2']}) = {data['v2']}$. "
                             f"Tính $f({data['x3']})$.")

            # Nội dung lời giải
            loigiai = (f"Ta có $f'(x) = \\int f''(x) \\text{{d}}x = \\int ({latex(data['f_dp'])}) \\text{{d}}x = {latex(data['f_p_p'])} + C_1$. \\\\\n"
                       f"$\\Rightarrow f(x) = \\int f'(x) \\text{{d}}x = \\int ({latex(data['f_p_p'])} + C_1) \\text{{d}}x = {latex(data['f_x_p'])} + C_1x + C_2$. \\\\\n"
                       f"Theo giả thiết: $\\begin{{cases}} f({data['x1']}) = {data['v1']} \\\\ f({data['x2']}) = {data['v2']} \\end{{cases}} "
                       f"\\Leftrightarrow \\begin{{cases}} {latex(data['f_x_p'].subs(x, data['x1']))} + {format_c1(data['x1'])} + C_2 = {data['v1']} \\\\ "
                       f"{latex(data['f_x_p'].subs(x, data['x2']))} + {format_c1(data['x2'])} + C_2 = {data['v2']} \\end{{cases}}$ \\\\\n"
                       f"Giải hệ ta được: $C_1 = {data['c1']}, C_2 = {data['c2']}$. \\\\\n"
                       f"Vậy $f(x) = {latex(data['f_f'])}$. \\\\\n"
                       f"$\\Rightarrow f({data['x3']}) = {data['kq']}$.")
            #Đáp án
            dapan=' \\shortans[0]{%s} '%(str(da_d))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

