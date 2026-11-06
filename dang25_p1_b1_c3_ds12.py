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


def bt_dang25_p1_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Bước 1: Random các thông số cho bài toán
            # Hàm số có dạng f(x) = a^(x-m) * b^(x+n)
            a = random.choice([2, 3, 5, 7])
            b = random.choice([2, 3, 5, 7])
            while a == b: # Đảm bảo a và b khác nhau để bài toán phong phú
                b = random.choice([2, 3, 5, 7])

            m = random.randint(1, 3)
            n = random.randint(1, 3)

            # Tính toán hàm số
            # f(x) = a^x/a^m * b^x * b^n = (a*b)^x * (b^n / a^m)
            f = (a**(x - m)) * (b**(x + n))

            # Tính nguyên hàm chính xác
            # F(x) = [(a*b)^x / ln(a*b)] * (b^n / a^m)
            tich_ab = a * b
            he_so_tu = b**n
            he_so_mau = a**m

            nguyen_ham = (he_so_tu * (tich_ab**x)) / (he_so_mau * symbols(f'ln({tich_ab})'))

            # Đáp án đúng (Dạng chuỗi LaTeX)
            da_dung = f'$\\frac{{{he_so_tu} \\cdot {tich_ab}^x}}{{{he_so_mau} \\ln {tich_ab}}} + C$'

            # Tạo các đáp án nhiễu
            s = [
                f'$\\frac{{{a}^{{x-{m}}} \\cdot {b}^{{x+{n}}}}}{{\\ln {a} \\cdot \\ln {b}}} + C$',
                f'${a}^{{x-{m}}} \\cdot {b}^{{x+{n}}} + C$',
                f'$\\frac{{{he_so_tu} \\cdot {tich_ab}^x}}{{{he_so_mau}}} + C$',
                f'$\\frac{{{tich_ab}^x}}{{{he_so_mau} \\ln {tich_ab}}} + C$',
                f'$\\frac{{{he_so_tu} \\cdot {tich_ab}^x}}{{\\ln {tich_ab}}} + C$'
            ]

            random.shuffle(s)
            list_fake = s[:3] # Lấy 3 đáp án sai ngẫu nhiên

            # Câu hỏi
            noidungcauhoi = f'Nguyên hàm của hàm số $f(x) = {a}^{{x-{m}}} \\cdot {b}^{{x+{n}}}$ là'

            # Thiết lập danh sách đáp án cho mẫu \choice
            da_d = '\\True ' + da_dung
            list_1 = [da_d] + list_fake
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = (f'Ta có: $\\int {a}^{{x-{m}}} \\cdot {b}^{{x+{n}}} dx = \\int \\frac{{{a}^x}}{{{a}^{m}}} \\cdot {b}^{n} \\cdot {b}^x dx '
                       f'= \\int \\frac{{{he_so_tu} \\cdot ({a} \\cdot {b})^x}}{{{he_so_mau}}} dx '
                       f'= \\frac{{{he_so_tu}}}{{{he_so_mau}}} \\int {tich_ab}^x dx '
                       f'= \\frac{{{he_so_tu} \\cdot {tich_ab}^x}}{{{he_so_mau} \\ln {tich_ab}}} + C$.')

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

