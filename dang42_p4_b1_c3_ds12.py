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


def bt_dang42_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x = symbols('x')

                # Hàm hỗ trợ định dạng số hạng đa thức (không chứa phân số)
                def to_str(coef, var, is_first=False):
                    if coef == 0: return ""
                    sign = ""
                    if not is_first:
                        sign = " + " if coef > 0 else " - "
                    else:
                        sign = "-" if coef < 0 else ""

                    abs_c = abs(coef)
                    str_c = "" if (abs_c == 1 and var != "") else str(abs_c)
                    return sign + str_c + var

                # Hàm hỗ trợ định dạng số hạng có chứa hệ số phân số
                def to_str_frac(coef, var, is_first=False):
                    if coef == 0: return ""

                    # Đã Sửa Lỗi: Ép kiểu hệ số về dạng Rational của sympy để luôn có thuộc tính .p và .q
                    coef = Rational(coef)

                    sign = ""
                    if not is_first:
                        sign = " + " if coef > 0 else " - "
                    else:
                        sign = "-" if coef < 0 else ""

                    abs_c = abs(coef)
                    if abs_c == 1 and var != "":
                        str_c = ""
                    elif abs_c.q == 1: # Bây giờ abs_c luôn là Rational nên không bị lỗi thuộc tính .q
                        str_c = str(abs_c.p)
                    else:
                        str_c = "\\frac{" + str(abs_c.p) + "}{" + str(abs_c.q) + "}"

                    return sign + str_c + var

                # Random các hệ số của đề bài y = ax^3 + b\sqrt[3]{x^2} + c\sqrt{x} + d
                a_val = random.choice([4, 8, 12, 2, -2, -4, -8])
                b_val = random.choice([-6, -3, -9, 3, 6, 9])
                c_val = random.choice([8, 4, 6, 2, -2, -4, -6, -8])
                d_val = random.choice([-7, -5, -3, -2, 2, 3, 5, 7])

                # Tạo chuỗi cho đề bài y ở dạng căn thức
                y_tex = to_str(a_val, "x^3", True) + to_str(b_val, "\\sqrt[3]{x^2}") + to_str(c_val, "\\sqrt{x}") + to_str(d_val, "")

                # Tạo chuỗi dạng lũy thừa để đưa vào lời giải
                y_pow_tex = to_str(a_val, "x^3", True) + to_str(b_val, "x^{\\frac{2}{3}}") + to_str(c_val, "x^{\\frac{1}{2}}") + to_str(d_val, "")

                # Tính toán hệ số của nguyên hàm đúng
                A_val = Rational(a_val, 4)
                B_val = Rational(b_val * 3, 5)
                C_val = Rational(c_val * 2, 3)
                D_val = d_val

                # Chuỗi nguyên hàm đúng F(x)
                F_tex = to_str_frac(A_val, "x^4", True) + to_str_frac(B_val, "x^{\\frac{5}{3}}") + to_str_frac(C_val, "x^{\\frac{3}{2}}") + to_str_frac(D_val, "x")

                # CÁC PHƯƠNG ÁN NHIỄU (SAI)
                # Nhiễu 1: Tính nhầm sang đạo hàm
                dA_val = a_val * 3
                dB_val = Rational(b_val * 2, 3)
                dC_val = Rational(c_val * 1, 2)
                F_wrong1_tex = to_str_frac(dA_val, "x^2", True) + to_str_frac(dB_val, "x^{-\\frac{1}{3}}") + to_str_frac(dC_val, "x^{-\\frac{1}{2}}")

                # Nhiễu 2: Quên chia cho số mũ mới (chỉ tăng mũ, giữ nguyên hệ số)
                F_wrong2_tex = to_str_frac(a_val, "x^4", True) + to_str_frac(b_val, "x^{\\frac{5}{3}}") + to_str_frac(c_val, "x^{\\frac{3}{2}}") + to_str_frac(d_val, "x")

                # Nhiễu 3: Nhân nghịch đảo sai (ví dụ chia thay vì nhân nghịch đảo)
                W3_B_val = Rational(b_val * 5, 3)
                W3_C_val = Rational(c_val * 3, 2)
                F_wrong3_tex = to_str_frac(A_val, "x^4", True) + to_str_frac(W3_B_val, "x^{\\frac{5}{3}}") + to_str_frac(W3_C_val, "x^{\\frac{3}{2}}") + to_str_frac(D_val, "x")

                # Các đáp án trắc nghiệm
                du = ['$%s + C$' % (F_tex)]
                da = random.choice(du)

                s = [
                    '$%s$' % (F_tex), 
                    '$%s + C$' % (F_wrong1_tex),
                    '$%s + C$' % (F_wrong2_tex),
                    '$%s + C$' % (F_wrong3_tex),
                    '$%s - C$' % (F_tex)
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Tìm nguyên hàm của hàm số $y = %s$.' % (y_tex))

                # Đánh dấu đáp án đúng - sai
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Hướng dẫn: Đưa căn về lũy thừa rồi lấy nguyên hàm. \\\\ '
                           'Ta có $y = %s = %s$. \\\\ '
                           'Họ tất cả các nguyên hàm của hàm số đã cho là: \\\\ '
                           '$\\int \\left( %s \\right) \\mathrm{d}x = %s + C$.' 
                           % (y_tex, y_pow_tex, y_pow_tex, F_tex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

