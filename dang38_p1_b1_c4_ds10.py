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


def bt_dang38_p1_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Để tập xác định luôn là R, ta cần a != 0 và a != -b
            b = random.randint(-5, 5)
            if b == 0: b = 2 # Tránh trường hợp suy biến x^2

            # Lấy danh sách các giá trị x làm mẫu số bằng 0 của từng cụm
            roots_g = [0, -b] 

            # Chọn a sao cho a không trùng với 0 và -b
            a_candidates = [i for i in range(-5, 6) if i not in roots_g and i != 0]
            a = random.choice(a_candidates)

            # Tạo các biểu thức sympy để dùng latex() cho chuẩn (xử lý dấu +/-)
            expr_numerator = Abs(x)
            expr_denom_part1 = Abs(x - a)
            expr_denom_part2 = Abs(x**2 + b*x)
            func = expr_numerator / (expr_denom_part1 + expr_denom_part2)

            # --- B4: Điều chỉnh các phương án sai ---
            # Đáp án đúng
            da_dung = r'$D = \mathbb{R}$'

            # Tạo các phương án sai dựa trên các nghiệm riêng lẻ
            # Lưu ý: Dùng set để tránh trùng lặp nếu ngẫu nhiên b hoặc a rơi vào các số đặc biệt
            sai1 = r'$D = \mathbb{R} \setminus \{ %s \}$' % latex(a)
            sai2 = r'$D = \mathbb{R} \setminus \{ %s; %s \}$' % (latex(min(0, -b)), latex(max(0, -b)))
            sai3 = r'$D = \mathbb{R} \setminus \{ %s; %s; %s \}$' % (latex(min(a, 0, -b)), 
                                                                    latex(sorted([a, 0, -b])[1]), 
                                                                    latex(max(a, 0, -b)))

            # --- B2: Viết lại bài toán theo mẫu ---
            noidungcauhoi = r'Tập xác định của hàm số $y = %s$ là' % latex(func)

            # Danh sách đáp án
            da_d = r'\True ' + da_dung
            list_1 = [da_d, sai1, sai2, sai3]
            random.shuffle(list_1)

            # Nội dung lời giải
            val_at_a = Abs(a**2 + b*a)
            loigiai = (r'Hàm số xác định khi $%s + %s \neq 0 \Leftrightarrow x \in \mathbb{R}$. Thật vậy: \\'
                       r'Nếu $x - %s = 0 \Leftrightarrow x = %s$ thì $%s = %s \neq 0$.\\'
                       r'Nếu $%s = 0 \Leftrightarrow \left[\begin{array}{l} x = 0 \\ x = %s \end{array}\right.$ '
                       r'thì $%s$ lần lượt bằng $%s$ và $%s$ (đều khác $0$).\\'
                       r'Vậy tập xác định của hàm số là $D = \mathbb{R}$.' 
                       % (latex(expr_denom_part1), latex(expr_denom_part2), 
                          latex(a), latex(a), latex(expr_denom_part2), latex(val_at_a),
                          latex(expr_denom_part2), latex(-b),
                          latex(expr_denom_part1), latex(Abs(0-a)), latex(Abs(-b-a))
                         ))

            # Xuất kết quả theo định dạng yêu cầu
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

