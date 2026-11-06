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


def bt_dang75_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo các biến toán học
            x, y = symbols('x y')

            # Chọn dạng toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Tạo bộ số Pythagorean để mẫu số (độ dài BC) là số nguyên đẹp
                py_triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20)]
                a_tri, b_tri, c_tri = random.choice(py_triples)

                # Chọn ngẫu nhiên vị trí B trên Oy và C trên Ox (để phương trình đẹp như mẫu)
                if random.choice([True, False]):
                    xC, yB = a_tri, b_tri
                else:
                    xC, yB = b_tri, a_tri

                # Tọa độ điểm A ngẫu nhiên
                xA = randint(-3, 6)
                yA = randint(-3, 6)

                # Đảm bảo A không thuộc BC
                while yB * xA + xC * yA - xC * yB == 0:
                    xA += 1

                # Các thông số tính toán
                # Phương trình BC theo đoạn chắn: x/xC + y/yB = 1 <=> yB*x + xC*y - xC*yB = 0
                val_a = yB
                val_b = xC
                val_c = -xC * yB

                # Tử số: |axA + byA + c|
                tu_so_val = val_a * xA + val_b * yA + val_c
                tu_so_abs = abs(tu_so_val)
                mau_so = c_tri 

                # Đáp án đúng
                kq = Rational(tu_so_abs, mau_so)
                da = '$%s$' % latex(kq)

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                potential_wrongs = [
                    Rational(tu_so_abs, mau_so**2), 
                    Rational(tu_so_abs, 1), 
                    Rational(abs(tu_so_val + 5), mau_so),
                    Rational(tu_so_abs, mau_so + 2)
                ]
                for p in potential_wrongs:
                    if p != kq:
                        s.add('$%s$' % latex(p))

                wrong_list = random.sample(list(s), 3)
                das1, das2, das3 = wrong_list[0], wrong_list[1], wrong_list[2]

                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có $A(%s;%s)$, $B(0;%s)$ và $C(%s;0)$. Chiều cao của tam giác kẻ từ đỉnh $A$ bằng'
                                 % (latex(xA), latex(yA), latex(yB), latex(xC)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # NỘI DUNG LỜI GIẢI THEO 3 BƯỚC
                # Bước 1: Lập phương trình BC
                phtrinh_bc = '%sx + %sy %s = 0' % (val_a, val_b, val_c if val_c < 0 else '+ ' + str(val_c))

                # Bước 2: Tính khoảng cách
                expr_tu = '%s \\cdot %s + %s \\cdot %s %s' % (val_a, xA, val_b, yA, val_c if val_c < 0 else '+ ' + str(val_c))

                loigiai = ('''Phương trình đường thẳng $BC$ đi qua $B(0; %s)$ và $C(%s; 0)$ là:
                                $\\frac{x}{%s} + \\frac{y}{%s} = 1 \\Leftrightarrow %s$.
                                Chiều cao của tam giác kẻ từ đỉnh $A$ chính là khoảng cách từ điểm $A(%s; %s)$ đến đường thẳng $BC$:
                                $h_A = d(A; BC) = \\frac{|%s|}{\\sqrt{%s^2 + %s^2}} = \\frac{|%s|}{%s} = %s$.\\\\
                                Vậy chiều cao cần tìm là $%s$.'''
                           % (latex(yB), latex(xC), latex(xC), latex(yB), phtrinh_bc,
                              latex(xA), latex(yA), expr_tu, val_a, val_b, tu_so_val, mau_so, latex(kq),
                              latex(kq)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

