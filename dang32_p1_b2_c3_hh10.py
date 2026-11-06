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


def bt_dang32_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo các biến ký hiệu cho SymPy
            x, y = symbols('x y')

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Để bài toán "đẹp", ta chọn các bộ số (a, b) sao cho căn(a^2 + b^2) là số nguyên hoặc có tỉ lệ đẹp.
            # Ví dụ: (1, -7) có độ dài 5*sqrt(2), (1, 1) có độ dài sqrt(2). Tỉ lệ là 5.
            # Hoặc bộ số Py-ta-go: (3, 4) -> 5, (5, 12) -> 13.

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn điểm M ngẫu nhiên
                xm = random.randint(-5, 5)
                ym = random.randint(-5, 5)
                M = (xm, ym)

                # Tạo đường thẳng d1: a1x + b1y + c1 = 0
                # Chọn d1 có độ dài vector pháp tuyến là k1 * sqrt(p)
                # Ở đây chọn d1: x - 7y + c1 (độ dài 5*sqrt(2))
                a1, b1 = 1, -7
                c1 = random.randint(-20, 20)
                L1_sq = a1**2 + b1**2 # 50

                # Tạo đường thẳng d2: a2x + b2y + c2 = 0
                # Chọn d2: x + y + c2 (độ dài sqrt(2))
                a2, b2 = 1, 1
                c2 = random.randint(-15, 15)
                L2_sq = a2**2 + b2**2 # 2

                # Tỉ lệ k giữa hai mẫu số của phương trình phân giác
                # |d1|/sqrt(50) = |d2|/sqrt(2)  => |d1| = 5*|d2|
                k = int(math.sqrt(L1_sq / L2_sq)) 

                # Phương trình phân giác: d1 = k*d2 và d1 = -k*d2
                # Phan giac 1: (a1 - k*a2)x + (b1 - k*b2)y + (c1 - k*c2) = 0
                pg1_a, pg1_b, pg1_c = a1 - k*a2, b1 - k*b2, c1 - k*c2
                # Phan giac 2: (a1 + k*a2)x + (b1 + k*b2)y + (c1 + k*c2) = 0
                pg2_a, pg2_b, pg2_c = a1 + k*a2, b1 + k*b2, c1 + k*c2

                # Rút gọn hệ số phân giác bằng GCD
                def rut_gon(a, b, c):
                    common = math.gcd(math.gcd(a, b), c)
                    if a < 0 or (a == 0 and b < 0): common = -common
                    return a // common, b // common, c // common

                pg1_a, pg1_b, pg1_c = rut_gon(pg1_a, pg1_b, pg1_c)
                pg2_a, pg2_b, pg2_c = rut_gon(pg2_a, pg2_b, pg2_c)

                # Đường thẳng Delta song song với phân giác và qua M(xm, ym)
                # Delta: Ax + By - (A*xm + B*ym) = 0
                dt1_c = -(pg1_a * xm + pg1_b * ym)
                dt2_c = -(pg2_a * xm + pg2_b * ym)

                # Biểu thức SymPy để xuất Latex đẹp
                d1_expr = Eq(a1*x + b1*y + c1, 0)
                d2_expr = Eq(a2*x + b2*y + c2, 0)
                delta1 = Eq(pg1_a*x + pg1_b*y + dt1_c, 0)
                delta2 = Eq(pg2_a*x + pg2_b*y + dt2_c, 0)

                # Đáp án đúng
                da = f"{latex(delta1)}; {latex(delta2)}"

                # Các đáp án nhiễu (thay đổi hằng số tự do)
                s = [
                    f"{latex(Eq(pg1_a*x + pg1_b*y + dt1_c + 2, 0))}; {latex(Eq(pg2_a*x + pg2_b*y - 1, 0))}",
                    f"{latex(Eq(pg1_a*x + pg1_b*y - 5, 0))}; {latex(Eq(pg2_a*x + pg2_b*y + 3, 0))}",
                    f"{latex(Eq(pg1_a*x - pg1_b*y + dt1_c, 0))}; {latex(Eq(pg2_a*x + pg2_b*y, 0))}",
                    f"{latex(Eq(pg1_a*x + pg1_b*y + 1, 0))}; {latex(Eq(pg2_a*x - pg2_b*y + 1, 0))}"
                ]

                das1 = random.choice(s); s.remove(das1)
                das2 = random.choice(s); s.remove(das2)
                das3 = random.choice(s)

                # --- B2: Viết lại bài toán ---
                noidungcauhoi = (f"Trong mặt phẳng với hệ tọa độ $Oxy$, cho điểm $M({xm};{ym})$ và hai đường thẳng "
                                 f"$d_1: {latex(d1_expr.lhs)}=0$, $d_2: {latex(d2_expr.lhs)}=0$. "
                                 f"Phương trình đường thẳng $\\Delta$ đi qua điểm $M$ và tạo với $d_1, d_2$ một tam giác cân tại giao điểm của $d_1$ và $d_2$ là")

                da_d = ('\\True $' + da + '$')
                list_1 = [da_d, f"${das1}$", f"${das2}$", f"${das3}$"]
                random.shuffle(list_1)

            # Nội dung lời giải (Đã sửa lỗi ngoặc nhọn ở dòng begin{{aligned}})
                loigiai = (f"Phương trình đường phân giác của góc tạo bởi $d_1$ và $d_2$ là:\\\\"
                           f"$\\frac{{|{latex(d1_expr.lhs)}|}}{{\\sqrt{{{a1}^2 + ({b1})^2}}}} = \\frac{{|{latex(d2_expr.lhs)}|}}{{\\sqrt{{{a2}^2 + {b2}^2}}}} "
                           f"\\Leftrightarrow \\frac{{|{latex(d1_expr.lhs)}|}}{{{k}\\sqrt{{{L2_sq}}}}} = \\frac{{|{latex(d2_expr.lhs)}|}}{{\\sqrt{{{L2_sq}}}}} "
                           f"\\Leftrightarrow |{latex(d1_expr.lhs)}| = {k}|{latex(d2_expr.lhs)}|$\\\\"
                           f"$\\Leftrightarrow \\left[\\begin{{aligned}} & {latex(Eq(pg1_a*x + pg1_b*y + pg1_c, 0))} \\\\ & {latex(Eq(pg2_a*x + pg2_b*y + pg2_c, 0))} \\end{{aligned}}\\right.$.\\\\"
                           f"Đường thẳng $\\Delta$ cần tìm đi qua $M({xm};{ym})$ và song song với một trong hai đường phân giác trên.\\\\"
                           f"- Trường hợp 1: $\\Delta$ song song với phân giác thứ nhất thì $\\Delta$ có dạng: ${pg1_a}x + {pg1_b}y + C = 0$. "
                           f"Thay tọa độ $M$ vào ta được phương trình: ${latex(delta1)}$.\\\\"
                           f"- Trường hợp 2: $\\Delta$ song song với phân giác thứ hai thì $\\Delta$ có dạng: ${pg2_a}x + {pg2_b}y + C = 0$. "
                           f"Thay tọa độ $M$ vào ta được phương trình: ${latex(delta2)}$.\\\\"
                           f"Vậy có hai đường thẳng thỏa mãn: ${da}$.")
            # --- Xuất câu trắc nghiệm ---
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

