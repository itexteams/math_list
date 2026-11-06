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


def bt_dang41_p3_b1_c1_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random số nguyên k khác 0 để thiết lập hệ số a = 2k
        # Đảm bảo nghiệm cực trị luôn là x = 1 và x = -1 (là các số nguyên)
        k = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        a = 2 * k

        # Biểu thức tử số của hàm số y = (x^2 + ax + 1) / (x^2 + 1)
        expr_tu = x**2 + a*x + 1
        expr_tu_str = latex(expr_tu)

        # Random tọa độ điểm I(x_I; y_I) là các số nguyên sao cho tam giác IAB tồn tại (S > 0)
        while True:
            x_I = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            y_I = random.choice([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
            S_val = abs(1 - y_I + k * x_I)
            if S_val > 0:
                break

        kq = latex(S_val)

        # Các đáp án trắc nghiệm
        du = ['$%s$' % kq]
        da = random.choice(du)

        # Sinh danh sách phương án sai (là các số nguyên dương không trùng với đáp án đúng)
        s_opts = []
        candidates = [S_val + 1, S_val + 2, S_val + 3, S_val + 4, S_val - 1, S_val - 2, S_val + 5]
        for c_val in candidates:
            if c_val > 0 and c_val != S_val and c_val not in s_opts:
                s_opts.append(c_val)

        das1 = '$%s$' % latex(s_opts[0])
        das2 = '$%s$' % latex(s_opts[1])
        das3 = '$%s$' % latex(s_opts[2])

        # Tính tọa độ cực trị (luôn là số nguyên)
        y_A = k + 1
        y_B = 1 - k

        # Tọa độ vectơ IA và IB
        u1 = 1 - x_I
        v1 = y_A - y_I
        u2 = -1 - x_I
        v2 = y_B - y_I

        I_str = 'I(%s; %s)' % (latex(x_I), latex(y_I))

        # Câu hỏi
        noidungcauhoi = ('''Biết rằng hai điểm cực trị của đồ thị hàm số $y = \\frac{%s}{x^2 + 1}$ cùng với điểm $%s$ tạo thành một tam giác. Diện tích tam giác đó bằng bao nhiêu?'''
                         % (expr_tu_str, I_str))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải chi tiết
        loigiai = ('''Tập xác định: $D = \\mathbb{R}$.\\\\
                     Ta có đạo hàm:\\\\
                     $y' = \\frac{(2x + %s)(x^2 + 1) - (%s)2x}{(x^2 + 1)^2} = \\frac{-%s x^2 + %s}{(x^2 + 1)^2} = \\frac{-%s(x^2 - 1)}{(x^2 + 1)^2}$.\\\\
                     $y' = 0 \\Leftrightarrow x^2 - 1 = 0 \\Leftrightarrow \\begin{cases} x_1 = 1 \\\\ x_2 = -1 \\end{cases}$.\\\\
                     Thay các giá trị $x$ vào hàm số, ta tìm được tung độ tương ứng của các điểm cực trị:\\\\
                     - Với $x_1 = 1 \\Rightarrow y_1 = \\frac{1 + %s + 1}{1^2 + 1} = %s \\Rightarrow A(1; %s)$.\\\\
                     - Với $x_2 = -1 \\Rightarrow y_2 = \\frac{1 - %s + 1}{(-1)^2 + 1} = %s \\Rightarrow B(-1; %s)$.\\\\
                     Với $%s$, ta tính tọa độ các vectơ:\\\\
                     $\\vec{IA} = \\left(%s; %s\\right)$,\\\\
                     $\\vec{IB} = \\left(%s; %s\\right)$.\\\\
                     Diện tích tam giác $IAB$ được tính theo công thức:\\\\
                     $S_{IAB} = \\frac{1}{2} \\left| x_{\\vec{IA}} y_{\\vec{IB}} - x_{\\vec{IB}} y_{\\vec{IA}} \\right| = \\frac{1}{2} \\left| (%s) \\cdot (%s) - (%s) \\cdot (%s) \\right| = \\frac{1}{2} \\left| %s \\right| = %s$.'''
                     % (latex(a), expr_tu_str, latex(a), latex(a), latex(a),
                        latex(a), latex(y_A), latex(y_A),
                        latex(a), latex(y_B), latex(y_B),
                        I_str,
                        latex(u1), latex(v1),
                        latex(u2), latex(v2),
                        latex(u1), latex(v2), latex(u2), latex(v1),
                        latex(2 * S_val), latex(S_val)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(S_val))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('--', '')
    return content  

