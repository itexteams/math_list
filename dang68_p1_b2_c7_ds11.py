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


def bt_dang68_p1_b2_c7_ds11(self):
            # Khai báo biến
            x = symbols('x')

            # B1: Nghiên cứu đề bài và lời giải
            # Hàm số có dạng: y = a*tan(x) + b*sqrt(x) + c*x^n

            # B3: Suy nghĩ cách random bài toán (bao gồm cả dấu)
            a_val = random.randint(2, 9) * random.choice([1, -1])
            b_val = random.randint(2, 9) * random.choice([1, -1])
            c_val = random.choice([1, -1]) # Hệ số của x^n
            n = random.randint(3, 7)

            # Hàm bổ trợ để xử lý dấu khi viết biểu thức y = ...
            def format_first_term(val, term_str):
                if val == 1: return term_str
                if val == -1: return "-" + term_str
                return f"{val}{term_str}"

            def format_next_term(val, term_str):
                if val == 1: return " + " + term_str
                if val == -1: return " - " + term_str
                if val > 0: return f" + {val}{term_str}"
                return f" - {abs(val)}{term_str}"

            # Tạo chuỗi hiển thị cho đề bài
            de_bai_y = format_first_term(a_val, r"\tan x")
            de_bai_y += format_next_term(b_val, r"\sqrt{x}")
            de_bai_y += format_next_term(c_val, r"x^{%s}" % n)

            # Thành phần đạo hàm chuẩn
            # 1. a/cos^2(x)
            p1_val = a_val
            # 2. b/(2*sqrt(x))
            p2_val = b_val
            # 3. c*n*x^(n-1)
            p3_val = c_val * n

            # Tạo chuỗi hiển thị cho đạo hàm đúng (y') (ĐÃ SỬA LỖI Ở ĐÂY)
            if p1_val == 1:
                da_dung_y = r"\frac{1}{\cos^2 x}"
            elif p1_val == -1:
                da_dung_y = r"-\frac{1}{\cos^2 x}"
            elif p1_val > 0:
                da_dung_y = r"\frac{%s}{\cos^2 x}" % p1_val
            else:
                da_dung_y = r"-\frac{%s}{\cos^2 x}" % abs(p1_val)

            if p2_val > 0:
                da_dung_y += r" + \frac{%s}{2\sqrt{x}}" % abs(p2_val)
            else:
                da_dung_y += r" - \frac{%s}{2\sqrt{x}}" % abs(p2_val)

            da_dung_y += format_next_term(p3_val, r"x^{%s}" % (n-1))

            # B2: Viết lại bài toán theo mẫu code
            noidungcauhoi = r'Đạo hàm của hàm số $y = %s$ là' % de_bai_y

            # Đáp án đúng
            da_d = r'''\True $y' = %s$''' % da_dung_y

            # Các đáp án nhiễu (Mô phỏng các lỗi sai trong ảnh)
            da_s1 = r'''$y' = %s$''' % da_dung_y.replace(r"\cos^2 x", r"\cos x")
            da_s2 = r'''$y' = -%s$''' % da_dung_y # Đổi dấu thành phần đầu
            da_s3 = r'''$y' = %s$''' % da_dung_y.replace(r"2\sqrt{x}", r"\sqrt{x}")

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = r'''Ta thực hiện đạo hàm từng thành phần của hàm số: \\
             $(%s \tan x)' = %s \cdot \frac{1}{\cos^2 x} = \frac{%s}{\cos^2 x}$. \\
             $(%s \sqrt{x})' = %s \cdot \frac{1}{2\sqrt{x}} = \frac{%s}{2\sqrt{x}}$. \\
             $(%s x^{%s})' = %s \cdot %s x^{%s} = %s x^{%s}$. \\
             Ghép các kết quả lại, ta được $y' = %s$.''' % (
                a_val, a_val, a_val, 
                b_val, b_val, b_val, 
                c_val, n, c_val, n, n-1, p3_val, n-1,
                da_dung_y
            )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','')
            return content

