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


def bt_dang29_p1_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các hàm hỗ trợ định dạng chuỗi toán học
                def fmt(coef, var, is_first=False):
                    if coef == 0: return ""
                    if var == "":
                        s = str(abs(coef))
                    else:
                        if abs(coef) == 1:
                            s = var
                        else:
                            s = str(abs(coef)) + var
                    if coef < 0:
                        return "- " + s if not is_first else "-" + s
                    else:
                        return "+ " + s if not is_first else s

                def fmt_frac(num, den, var, is_first=False):
                    if num == 0: return ""
                    g = math.gcd(num, den)
                    num = num // g
                    den = den // g
                    if den == 1:
                        return fmt(num, var, is_first)

                    sign_str = "-" if num * den < 0 else "+"
                    abs_num = abs(num)
                    abs_den = abs(den)

                    if var == "":
                        frac_str = "\\frac{" + str(abs_num) + "}{" + str(abs_den) + "}"
                    else:
                        if abs_num == 1:
                            frac_str = "\\frac{" + var + "}{" + str(abs_den) + "}"
                        else:
                            frac_str = "\\frac{" + str(abs_num) + var + "}{" + str(abs_den) + "}"

                    if sign_str == "-":
                        return "- " + frac_str if not is_first else "-" + frac_str
                    else:
                        return "+ " + frac_str if not is_first else frac_str

                # Random các số cho hàm f(x) = ax^2 + b*sin(x) + c
                a = random.choice([1, 2, 4, 5]) # Tránh số 3 để nguyên hàm tạo ra phân số x^3/3
                b = random.choice([-2, -1, 1, 2])
                c = random.choice([-3, -2, -1, 1, 2, 3])
                F0_val = random.choice([-3, -2, -1, 1, 2, 3])

                # Tính toán hằng số C
                # F(x) = (a/3)x^3 - b*cos(x) + cx + C
                # F(0) = -b + C = F0_val => C = F0_val + b
                C_val = F0_val + b

                # Xây dựng các biểu thức dạng chuỗi LaTeX
                f_str = (fmt(a, 'x^2', True) + " " + fmt(b, '\\sin x') + " " + fmt(c, '')).replace("  ", " ").strip()
                F_gen_str = (fmt_frac(a, 3, 'x^3', True) + " " + fmt(-b, '\\cos x') + " " + fmt(c, 'x') + " + C").replace("  ", " ").strip()

                # Đáp án đúng
                ans_correct = "F(x) = " + (fmt_frac(a, 3, 'x^3', True) + " " + fmt(-b, '\\cos x') + " " + fmt(c, 'x') + " " + fmt(C_val, '')).replace("  ", " ").strip()

                # Tạo các phương án nhiễu
                # Sai lầm 1: Quên chia 3 khi lấy nguyên hàm của x^2
                d1 = "F(x) = " + (fmt(a, 'x^3', True) + " " + fmt(-b, '\\cos x') + " " + fmt(c, 'x') + " " + fmt(C_val, '')).replace("  ", " ").strip()
                # Sai lầm 2: Lấy nguyên hàm sin(x) thành +cos(x), kéo theo tính sai C
                d2 = "F(x) = " + (fmt_frac(a, 3, 'x^3', True) + " " + fmt(b, '\\cos x') + " " + fmt(c, 'x') + " " + fmt(F0_val - b, '')).replace("  ", " ").strip()
                # Sai lầm 3: Mặc định luôn C = F(0)
                d3 = "F(x) = " + (fmt_frac(a, 3, 'x^3', True) + " " + fmt(-b, '\\cos x') + " " + fmt(c, 'x') + " " + fmt(F0_val, '')).replace("  ", " ").strip()
                # Sai lầm 4: Lấy nguyên hàm sin(x) thành +cos(x) nhưng vẫn giữ C đúng
                d4 = "F(x) = " + (fmt_frac(a, 3, 'x^3', True) + " " + fmt(b, '\\cos x') + " " + fmt(c, 'x') + " " + fmt(C_val, '')).replace("  ", " ").strip()

                distractors = [d1, d2, d3, d4]
                random.shuffle(distractors)

                da = "$%s$" % ans_correct
                das1 = "$%s$" % distractors[0]
                das2 = "$%s$" % distractors[1]
                das3 = "$%s$" % distractors[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f(x) = %s$. Biết rằng $F(x)$ là một nguyên hàm của hàm số $f(x)$ và thỏa mãn $F(0) = %s$. Khi đó $F(x)$ bằng''' % (f_str, F0_val))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $F(x) = \\int (%s)dx = %s$.\\\\
            Theo giả thiết: $F(0) = %s \\Rightarrow C = %s$ nên do đó $%s$.''' % (f_str, F_gen_str, F0_val, C_val, ans_correct))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                       '\\choice \n'
                       '{'+str(list_1[1])+'}\n'
                       '{'+str(list_1[2])+'}\n'
                       '{'+str(list_1[3])+'}\n'
                       '{'+str(list_1[0])+'}\n'
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

