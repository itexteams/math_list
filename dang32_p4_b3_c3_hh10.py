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


def bt_dang32_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Hàm xử lý dấu thừa
            def clean_str(text):
                return str(text).replace('+ -', '-').replace('- -', '+').replace('+-', '-').replace('--', '+')

            # Hàm format phương trình đường tròn
            def format_circle(x0, y0, R2_val):
                term_x = f"(x - {x0})^2" if x0 > 0 else (f"(x + {-x0})^2" if x0 < 0 else "x^2")
                term_y = f"(y - {y0})^2" if y0 > 0 else (f"(y + {-y0})^2" if y0 < 0 else "y^2")
                return clean_str(f"{term_x} + {term_y} = {sp.latex(R2_val)}")

            # Hàm format trị tuyệt đối
            def format_abs(b_val):
                if b_val > 0: return f"|a + {b_val}|"
                elif b_val < 0: return f"|a - {-b_val}|"
                else: return "|a|"

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random hệ số m cho đường thẳng d
                m = random.choice([-3, -2, -1, 1, 2, 3])

                # Bước 2: Để nghiệm đẹp, set hệ số q của Delta sao cho q - m = 1 hoặc -1 (ở đây chọn 1)
                q = m + 1
                if q == 0:
                    q = random.choice([2, 3])
                    m = q - 1

                # Bước 3: Random 2 nghiệm a1, a2 (cùng tính chẵn lẻ để B nguyên)
                a1 = random.randint(-5, 5)
                k = random.randint(1, 4)
                a2 = a1 - 2*k

                # Bước 4: Tính B và K để thiết lập trị tuyệt đối |a + B| = K
                B = -(a1 + a2) // 2
                K = abs(a1 + B)

                # Bước 5: Random n cho đường thẳng d, từ đó suy ra c cho Delta
                n = random.randint(-5, 5)
                c = B + n

                # Tính R và R^2
                denom_sq = 1 + q**2
                R_expr = sp.Rational(K, 1) / sp.sqrt(denom_sq)
                R2_expr = sp.Rational(K**2, denom_sq)

                # Tọa độ tâm
                xI1 = -m*a1 - n
                yI1 = a1
                xI2 = -m*a2 - n
                yI2 = a2

                # Phương trình đúng
                eqC1 = format_circle(xI1, yI1, R2_expr)
                eqC2 = format_circle(xI2, yI2, R2_expr)
                da = f"${eqC1}$ và ${eqC2}$"

                # Các phương án sai (Nhiễu dấu tọa độ tâm)
                eqC1_w1 = format_circle(-xI1, -yI1, R2_expr)
                eqC2_w1 = format_circle(-xI2, -yI2, R2_expr)
                das1 = f"${eqC1_w1}$ và ${eqC2_w1}$"

                eqC1_w2 = format_circle(xI1, -yI1, R2_expr)
                eqC2_w2 = format_circle(xI2, -yI2, R2_expr)
                das2 = f"${eqC1_w2}$ và ${eqC2_w2}$"

                eqC1_w3 = format_circle(-xI1, yI1, R2_expr)
                eqC2_w3 = format_circle(-xI2, yI2, R2_expr)
                das3 = f"${eqC1_w3}$ và ${eqC2_w3}$"

                # Câu hỏi
                x_sym, y_sym = sp.symbols('x y')
                d_expr = x_sym + m*y_sym + n
                delta_expr = x_sym + q*y_sym + c

                d_str = clean_str(sp.latex(d_expr) + "=0")
                delta_str = clean_str(sp.latex(delta_expr) + "=0")

                noidungcauhoi = f"Trong mặt phẳng $Oxy$ cho $d: {d_str}$ và $\\Delta: {delta_str}$. Lập phương trình (C) có bán kính $R = {sp.latex(R_expr)}$, có tâm thuộc $d$ và tiếp xúc với $\\Delta$."

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                a_sym = sp.symbols('a')
                xI_expr = -m * a_sym - n
                xI_str = clean_str(sp.latex(xI_expr))

                loigiai = f"""Gọi $I({xI_str}; a) \\in d$ là tâm của (C). Ta có
                \\[ d(I, \\Delta) = R \\Leftrightarrow \\frac{{{format_abs(B)}}}{{\\sqrt{{{1 + q**2}}}}} = {sp.latex(R_expr)} \\Leftrightarrow \\left[ \\begin{{array}}{{l}} a = {a1} \\\\ a = {a2} \\end{{array}} \\right. \\]
                - Với $a = {a1}$ suy ra $I({xI1}; {yI1})$. Phương trình $(C): {eqC1}$. \\\\
                - Với $a = {a2}$ suy ra $I({xI2}; {yI2})$. Phương trình $(C): {eqC2}$.
                """

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

