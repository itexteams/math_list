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


def bt_dang35_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Tạo các điểm ngẫu nhiên A và B (O cố định 0,0)
                # Để giải hệ ra số nguyên/hữu tỉ đẹp, ta chọn a, b trước rồi tính y
                a_val = random.choice([i for i in range(-5, 6) if i != 0])
                b_val = random.choice([i for i in range(-5, 6) if i != 0])
                c_val = 0

                # Chọn x1, x2 khác nhau và khác 0
                x1 = random.randint(1, 3)
                x2 = random.randint(-3, -1)

                # Tính y tương ứng
                y1 = a_val * x1**2 + b_val * x1
                y2 = a_val * x2**2 + b_val * x2

                # Biểu thức Parabol đúng
                f_x = a_val * x**2 + b_val * x
                kq = latex(f_x).replace('**2', '^2')

                # Các đáp án trắc nghiệm
                da_dung = f'$y = {kq}$'

                # Tạo các đáp án nhiễu (sai)
                s = [
                    f'$y = {latex(-a_val*x**2 + b_val*x)}$',
                    f'$y = {latex(a_val*x**2 - b_val*x)}$',
                    f'$y = {latex(b_val*x**2 + a_val*x)}$',
                    f'$y = {latex(a_val*x**2 + b_val*x + 1)}$',
                    f'$y = {latex(2*a_val*x**2 + b_val*x)}$'
                ]

                # Loại bỏ trùng lặp nếu có và lấy 3 đáp án sai
                s = list(set([i for i in s if i != da_dung]))
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = (f'Xác định parabol $y = ax^2 + bx + c$, biết rằng parabol đó đi qua ba điểm '
                                 f'$A({x1};{y1})$, $B({x2};{y2})$, $O(0;0)$.')

                # Các đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết y hệt cấu trúc trong ảnh)
                # Thiết lập hệ phương trình để trình bày lời giải
                eq1 = f"{x1**2}a + {x1}b + c = {y1}" if x1 > 0 else f"{x1**2}a - {abs(x1)}b + c = {y1}"
                eq2 = f"{x2**2}a - {abs(x2)}b + c = {y2}" if x2 < 0 else f"{x2**2}a + {x2}b + c = {y2}"

                loigiai = (f'Vì $(P)$ đi qua ba điểm $A({x1};{y1})$, $B({x2};{y2})$, $O(0;0)$ nên suy ra \\\\'
                           f'$\\begin{{cases}} {eq1} \\\\ {eq2} \\\\ c = 0 \\end{{cases}} '
                           f'\\Leftrightarrow \\begin{{cases}} a = {a_val} \\\\ b = {b_val} \\\\ c = 0 \\end{{cases}}$. \\\\'
                           f'Vậy $(P): y = {kq}$.')

            # Xuất câu trắc nghiệm theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

