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


def bt_dang34_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các giá trị ngẫu nhiên để đảm bảo x0 là số nguyên
                # Hàm số có dạng y = ax^2 + b
                a = randint(1, 3)
                x0_val = randint(1, 3)
                b = randint(-5, 5)

                # Tính tung độ y0
                y0_val = a * (x0_val**2) + b

                # Đạo hàm y' = 2ax
                # Tại x0: k1 = 2 * a * x0_val
                # Tại -x0: k2 = -2 * a * x0_val
                k1 = 2 * a * x0_val
                k2 = -2 * a * x0_val

                # Phương trình: y = k(x - x_0) + y_0
                # y = kx - k*x0 + y0
                m = y0_val - k1 * x0_val

                # Kết quả đúng
                # k1*x + m và k2*x + m
                if m >= 0:
                    da_str = "y = %sx + %s \\text{ và } y = %sx + %s" % (latex(k1), latex(m), latex(k2), latex(m))
                else:
                    da_str = "y = %sx %s \\text{ và } y = %sx %s" % (latex(k1), latex(m), latex(k2), latex(m))

                da_str = da_str.replace('.', ',')
                du = ["$%s$" % da_str]
                da = random.choice(du)

                # Tạo các phương án nhiễu (sai)
                s = []
                # Nhiễu 1: Sai hệ số m
                m_wrong = m + randint(1, 3)
                s.append("$y = %sx + %s \\text{ và } y = %sx + %s$" % (latex(k1), latex(m_wrong), latex(k2), latex(m_wrong)))

                # Nhiễu 2: Sai hệ số góc k
                k_wrong = k1 + 1
                s.append("$y = %sx + %s \\text{ và } y = %sx + %s$" % (latex(k_wrong), latex(m), latex(-k_wrong), latex(m)))

                # Nhiễu 3: Chỉ lấy 1 phương trình
                s.append("$y = %sx + %s$" % (latex(k1), latex(m)))

                # Nhiễu 4: Sai dấu m
                s.append("$y = %sx + %s \\text{ và } y = %sx + %s$" % (latex(k1), latex(-m), latex(k2), latex(-m)))

                random.shuffle(s)
                das1 = s[0].replace('.', ',')
                das2 = s[1].replace('.', ',')
                das3 = s[2].replace('.', ',')

                # Câu hỏi
                # y = ax^2 + b
                bieuthuc_y = "%sx^2" % (latex(a)) if b == 0 else ("%sx^2 + %s" % (latex(a), latex(b)) if b > 0 else "%sx^2 %s" % (latex(a), latex(b)))

                noidungcauhoi = ('''Viết phương trình tiếp tuyến của đồ thị hàm số $y = %s$ $(C)$ tại điểm có tung độ $y_0 = %s$.'''
                                 % (bieuthuc_y, latex(y0_val)))

                # Nội dung lời giải (Viết chi tiết giống trong ảnh)
                # f(x) - f(x0) = a*x^2 + b - (a*x0^2 + b) = a(x^2 - x0^2) = a(x-x0)(x+x0)
                loigiai = ('''Gọi $T\\left( x_0;y_0 \\right)$ là tiếp điểm.\\\\
            Tại $x_0 \\in \\mathbb{R}$ tùy ý, ta có: $f\\left( x \\right) - f\\left( x_0 \\right) = %sx^2 %s - \\left( %s x_0^2 %s \\right) = %s \\left( x - x_0 \\right) \\left( x + x_0 \\right)$.\\\\
            Ta có: $\\frac{f\\left( x \\right) - f\\left( x_0 \\right)}{x - x_0} = \\frac{%s \\left( x - x_0 \\right) \\left( x + x_0 \\right)}{x - x_0} = %s \\left( x + x_0 \\right)$.\\\\
            Suy ra: $\\lim_{x \\to x_0} \\frac{f\\left( x \\right) - f\\left( x_0 \\right)}{x - x_0} = \\lim_{x \\to x_0} \\left( %s \\left( x + x_0 \\right) \\right) = %s x_0 \\Rightarrow y' = %s x$.\\\\
            Ta có $y_0 = %s \\Rightarrow %sx^2 %s = %s \\Leftrightarrow %sx^2 = %s \\Leftrightarrow \\left[ \\begin{aligned} & x_0 = %s \\\\ & x_0 = %s \\end{aligned} \\right.$\\\\
            + Với $x_0 = %s$:\\\\
            Hệ số góc của tiếp tuyến của $(C)$ tại điểm có hoành độ $x_0 = %s$ là $k = y'\\left( %s \\right) = %s$.\\\\
            Phương trình tiếp tuyến cần tìm là $y = y'\\left( %s \\right) \\left( x - %s \\right) + y\\left( %s \\right) \\Leftrightarrow y = %sx %s$.\\\\
            + Với $x_0 = %s$:\\\\
            Hệ số góc của tiếp tuyến của $(C)$ tại điểm có hoành độ $x_0 = %s$ là $k = y'\\left( %s \\right) = %s$.\\\\
            Phương trình tiếp tuyến cần tìm là $y = y'\\left( %s \\right) \\left( x + %s \\right) + y\\left( %s \\right) \\Leftrightarrow y = %sx %s$.\\\\
            Vậy phương trình tiếp tuyến của đồ thị hàm số tại điểm có tung độ $y_0 = %s$ là\\\\
            $y = %sx %s$ và $y = %sx %s$.'''
                           % (latex(a), "" if b == 0 else ("+ " + latex(b) if b > 0 else latex(b)), 
                              latex(a), "" if b == 0 else ("+ " + latex(b) if b > 0 else latex(b)), 
                              latex(a),
                              latex(a), latex(a), latex(a), latex(2*a), latex(2*a),
                              latex(y0_val), latex(a), "" if b == 0 else ("+ " + latex(b) if b > 0 else latex(b)), latex(y0_val), 
                              latex(a), latex(a * x0_val**2),
                              latex(x0_val), latex(-x0_val),
                              latex(x0_val), latex(x0_val), latex(x0_val), latex(k1),
                              latex(x0_val), latex(x0_val), latex(x0_val), latex(k1), "+ " + latex(m) if m >= 0 else latex(m),
                              latex(-x0_val), latex(-x0_val), latex(-x0_val), latex(k2),
                              latex(-x0_val), latex(x0_val), latex(-x0_val), latex(k2), "+ " + latex(m) if m >= 0 else latex(m),
                              latex(y0_val),
                              latex(k1), "+ " + latex(m) if m >= 0 else latex(m),
                              latex(k2), "+ " + latex(m) if m >= 0 else latex(m)
                              ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + 
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '')
            return content

