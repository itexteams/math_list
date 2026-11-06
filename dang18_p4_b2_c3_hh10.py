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


def bt_dang18_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # ---------------- B3: RANDOM BÀI TOÁN ----------------
                # 1. Random vector pháp tuyến d: (A1, B1)
                A1_list = [3, 2, 1, 4]
                B1_list = [-2, 3, -4, 1, -1, 2]
                A1 = random.choice(A1_list)
                # Rút ngẫu nhiên B1 sao cho hệ số a^2 - b^2 != 0 
                B1 = random.choice([b for b in B1_list if abs(b) != A1]) 

                C1 = random.randint(-5, 5)

                # 2. Random điểm M(x0, y0) sao cho M không thuộc d
                x0 = random.randint(-3, 3)
                y0 = random.randint(-3, 3)
                while A1*x0 + B1*y0 + C1 == 0:
                    y0 = random.randint(-3, 5)

                # Phương trình đường thẳng d
                d_expr = A1*x + B1*y + C1
                eq_d = latex(d_expr) + "=0"

                # Hàm hỗ trợ hiển thị nhân a(x - x0) + b(y - y0)
                def fmt_x(val):
                    if val == 0: return "x"
                    if val > 0: return f"(x-{val})"
                    return f"(x+{abs(val)})"

                def fmt_y(val):
                    if val == 0: return "y"
                    if val > 0: return f"(y-{val})"
                    return f"(y+{abs(val)})"

                # Hàm hỗ trợ hiển thị pt tổng quát dạng chữ: ax + by - ax0 - by0 = 0
                def get_general(x_val, y_val):
                    res = "ax+by"
                    if x_val == 1: res += "-a"
                    elif x_val == -1: res += "+a"
                    elif x_val > 0: res += f"-{x_val}a"
                    elif x_val < 0: res += f"+{-x_val}a"

                    if y_val == 1: res += "-b"
                    elif y_val == -1: res += "+b"
                    elif y_val > 0: res += f"-{y_val}b"
                    elif y_val < 0: res += f"+{-y_val}b"
                    return res + "=0"

                # 3. Tính toán cho phương trình bậc 2 theo a, b
                # A_coeff*a^2 + B_coeff*ab + C_coeff*b^2 = 0
                A_coeff = A1**2 - B1**2
                B_coeff = 4 * A1 * B1
                C_coeff = -(A1**2 - B1**2)

                # Công thức nghiệm tỷ lệ t = a/b
                T1 = -2 * A1 * B1 + (A1**2 + B1**2)
                T2 = -2 * A1 * B1 - (A1**2 + B1**2)
                M0 = A1**2 - B1**2

                # Dùng Sympy Rational để rút gọn phân số lấy a, b đẹp
                t1_val = Rational(T1, M0)
                t2_val = Rational(T2, M0)

                a1, b1 = t1_val.numerator, t1_val.denominator
                a2, b2 = t2_val.numerator, t2_val.denominator

                # Xử lý C cho đường thẳng Delta 1 và Delta 2
                C_delta1 = -a1*x0 - b1*y0
                C_delta2 = -a2*x0 - b2*y0

                delta1_expr = a1*x + b1*y + C_delta1
                delta2_expr = a2*x + b2*y + C_delta2

                eq_delta1 = latex(delta1_expr) + "=0"
                eq_delta2 = latex(delta2_expr) + "=0"

                # Các đáp án trắc nghiệm
                da = f"${eq_delta1}; {eq_delta2}$"

                # Tạo phương án nhiễu (distractors)
                s_set = set()
                while len(s_set) < 3:
                    s_a1, s_b1 = random.choice([(a1, -b1), (b1, a1), (a1, b1), (-b1, a1)])
                    s_a2, s_b2 = random.choice([(a2, -b2), (-b2, a2), (a2, b2), (b2, a2)])
                    s_c1 = C_delta1 + random.randint(-3, 3)
                    s_c2 = C_delta2 + random.randint(-3, 3)
                    s_eq1 = latex(s_a1*x + s_b1*y + s_c1) + "=0"
                    s_eq2 = latex(s_a2*x + s_b2*y + s_c2) + "=0"
                    s_ans = f"${s_eq1}; {s_eq2}$"
                    if s_ans != da:
                        s_set.add(s_ans)

                s = list(s_set)[:3]

                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(s[0]), str(s[1]), str(s[2])]
                random.shuffle(list_1)

                # ---------------- TẠO NỘI DUNG LỜI GIẢI ----------------
                noidungcauhoi = f"Cho đường thẳng $d: {eq_d}$ và $M({x0}; {y0})$. Lập phương trình đường thẳng $\\Delta$ đi qua $M$ và tạo với $d$ một góc $45^\\circ$."

                # Xử lý chuỗi in ra sao cho tử số / mẫu số giống hệt bài mẫu
                tu_so_1 = f"|{A1}a + ({B1}b)|" if B1 < 0 else f"|{A1}a + {B1}b|"
                mau_so_1 = f"\\sqrt{{{A1}^2+({B1})^2}} \\cdot \\sqrt{{a^2+b^2}}" if B1 < 0 else f"\\sqrt{{{A1}^2+{B1}^2}} \\cdot \\sqrt{{a^2+b^2}}"
                tu_so_2 = f"|{A1}a - {abs(B1)}b|" if B1 < 0 else f"|{A1}a + {B1}b|"
                sum_sq = A1**2 + B1**2
                mau_so_2 = f"\\sqrt{{{sum_sq}}} \\cdot \\sqrt{{a^2+b^2}}"
                ve_trai_3 = f"\\sqrt{{{sum_sq * 2}(a^2+b^2)}}"
                ve_phai_3 = f"2{tu_so_2}"

                # Xử lý in phương trình bậc 2 đẹp không bị lỗi cộng trừ
                term1 = f"{A_coeff}a^2" if A_coeff not in [1, -1] else ("a^2" if A_coeff == 1 else "-a^2")
                term2 = f"+ {B_coeff}ab" if B_coeff > 0 else (f"- {abs(B_coeff)}ab" if B_coeff < 0 else "")
                term3 = f"+ {C_coeff}b^2" if C_coeff > 0 else (f"- {abs(C_coeff)}b^2" if C_coeff < 0 else "")
                pt_bac_2 = f"{term1} {term2} {term3} = 0".strip()
                if pt_bac_2.startswith('+ '): pt_bac_2 = pt_bac_2[2:]

                # Hàm hiển thị mối liên hệ của a và b
                def nice_rel(num, den):
                    if den == 1: return f"a = {num}b"
                    if den == -1: return f"a = {-num}b"
                    if num == 1: return f"{den}a = b"
                    if num == -1: return f"{den}a = -b"
                    return f"{den}a = {num}b"

                rel1 = nice_rel(a1, b1)
                rel2 = nice_rel(a2, b2)

                str_kq1 = f"Nếu ${rel1}$, chọn $a={a1}; b={b1}$ ta được $\\Delta: {eq_delta1}$."
                str_kq2 = f"Nếu ${rel2}$, chọn $a={a2}; b={b2}$ ta được $\\Delta: {eq_delta2}$."

                loigiai = (
                    f"Đường thẳng $\\Delta$ đi qua $M$ có dạng $a{fmt_x(x0)}+b{fmt_y(y0)}=0, a^2+b^2 \\neq 0$ hay ${get_general(x0, y0)}$.\\\\\n"
                    f"Theo bài ra $\\Delta$ tạo với $d$ một góc $45^\\circ$ nên:\\\\\n"
                    f"$\\cos 45^\\circ = \\frac{{{tu_so_1}}}{{{mau_so_1}}} \\Leftrightarrow \\frac{{\\sqrt{{2}}}}{{2}} = \\frac{{{tu_so_2}}}{{{mau_so_2}}} \\Leftrightarrow {ve_trai_3} = {ve_phai_3}$\\\\\n"
                    f"$\\Leftrightarrow {pt_bac_2} \\Leftrightarrow \\left[ \\begin{{array}}{{l}} {rel1} \\\\ {rel2} \\end{{array}} \\right.$\\\\\n"
                    f"{str_kq1}\\\\\n"
                    f"{str_kq2}\\\\\n"
                    f"Vậy có hai đường thẳng thỏa mãn: ${eq_delta1}; {eq_delta2}$."
                )

                # Dùng hàm replace để CHẮC CHẮN loại bỏ lỗi dấu + -, - - theo nguyên tắc
                loigiai = loigiai.replace('+ -', '- ').replace('- -', '+ ')
                noidungcauhoi = noidungcauhoi.replace('+ -', '- ').replace('- -', '+ ')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

