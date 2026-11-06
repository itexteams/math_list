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


def bt_dang39_p1_b1_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random vector chỉ phương (a, b, c) đảm bảo không có tọa độ nào bằng 0 để viết dạng chính tắc
                a, b, c = 0, 0, 0
                while a == 0 or b == 0 or c == 0:
                    a, b, c = random.sample(range(-5, 6), 3)

                # Random điểm thuộc đường thẳng d
                x0 = random.randint(-5, 5)
                y0 = random.randint(-5, 5)
                z0 = random.randint(-5, 5)

                # Random điểm A mà mặt phẳng (P) đi qua
                xA = random.randint(-5, 5)
                yA = random.randint(-5, 5)
                zA = random.randint(-5, 5)

                # Hàm định dạng tử số của phương trình đường thẳng
                def fmt_num(num, var):
                    if num > 0: return '%s-%s' % (var, num)
                    elif num < 0: return '%s+%s' % (var, abs(num))
                    else: return '%s' % var

                frac_x = '\\frac{%s}{%s}' % (fmt_num(x0, 'x'), a)
                frac_y = '\\frac{%s}{%s}' % (fmt_num(y0, 'y'), b)
                frac_z = '\\frac{%s}{%s}' % (fmt_num(z0, 'z'), c)

                vec_u = '(%s; %s; %s)' % (a, b, c)
                pt_A = '(%s; %s; %s)' % (xA, yA, zA)

                # Phương trình mặt phẳng: a(x - xA) + b(y - yA) + c(z - zA) = 0
                D_val = -(a*xA + b*yA + c*zA)
                eq_correct = a*x + b*y + c*z + D_val

                # Tạo các phương án nhiễu
                wrong_eqs = set()

                # Nhiễu 1: Sai hằng số tự do
                D_w1 = D_val + random.choice([1, -1, 2, -2])
                if D_w1 == D_val: D_w1 += 1
                wrong_eqs.add(a*x + b*y + c*z + D_w1)

                # Nhiễu 2: Đổi dấu 1 hệ số của vectơ pháp tuyến
                D_w2 = -(a*xA + b*yA - c*zA)
                wrong_eqs.add(a*x + b*y - c*z + D_w2)

                # Nhiễu 3: Đổi dấu 1 hệ số khác của vectơ pháp tuyến
                D_w3 = -(a*xA - b*yA + c*zA)
                wrong_eqs.add(a*x - b*y + c*z + D_w3)

                # Lấy đủ 3 phương án nhiễu (đảm bảo không trùng với đáp án đúng)
                while len(wrong_eqs) < 3 or eq_correct in wrong_eqs:
                    a_w, b_w, c_w = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
                    if a_w == 0 and b_w == 0 and c_w == 0: continue
                    D_w = -(a_w*xA + b_w*yA + c_w*zA) + random.randint(-3, 3)
                    eq_w = a_w*x + b_w*y + c_w*z + D_w
                    if eq_w != eq_correct:
                        wrong_eqs.add(eq_w)

                wrong_list = list(wrong_eqs)

                # Chuẩn bị đáp án trắc nghiệm
                da = '$%s=0$' % latex(eq_correct)
                das1 = '$%s=0$' % latex(wrong_list[0])
                das2 = '$%s=0$' % latex(wrong_list[1])
                das3 = '$%s=0$' % latex(wrong_list[2])

                # Câu hỏi
                noidungcauhoi = ('''Trong không gian $Oxyz$, cho đường thẳng $d: %s = %s = %s$. Mặt phẳng $(P)$ đi qua điểm $A%s$ và vuông góc với đường thẳng $d$ có phương trình là''' 
                                 % (frac_x, frac_y, frac_z, pt_A))

                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Hàm định dạng cho bước trung gian trong lời giải (giữ nguyên số 1 hoặc -0 theo như hình ảnh)
                def fmt_step_term(coeff, var, val):
                    sign = "+" if coeff > 0 else "-"
                    if val > 0: inner = '%s-%s' % (var, val)
                    elif val < 0: inner = '%s+%s' % (var, abs(val))
                    else: inner = '%s-0' % var
                    return '%s%s(%s)' % (sign, abs(coeff), inner)

                t1 = fmt_step_term(a, 'x', xA)
                if t1.startswith('+'): t1 = t1[1:] # Xóa dấu '+' ở số hạng đầu tiên nếu dương
                t2 = fmt_step_term(b, 'y', yA)
                t3 = fmt_step_term(c, 'z', zA)
                step_eq = '%s%s%s=0' % (t1, t2, t3)

                # Lời giải
                loigiai = ('''Đường thẳng $d$ có một vectơ chỉ phương là $\\vec{u}_d=%s$.\\\\
            Mặt phẳng $(P)$ vuông góc với đường thẳng $d$ nên $(P)$ nhận $\\vec{u}_d$ làm vectơ pháp tuyến.\\\\
            Phương trình mặt phẳng $(P)$ là: $%s \\Leftrightarrow %s=0$.''' 
                           % (vec_u, step_eq, latex(eq_correct)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

