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


def bt_dang41_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến ký hiệu cho Sympy
            x, y = symbols('x y')

            # Hàm định dạng phương trình đường thẳng ax + by + c = 0 cho đẹp
            def format_line(a, b, c):
                expr = a*x + b*y + c
                return latex(expr) + " = 0"

            # Bắt đầu chọn dạng bài
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Tạo điểm M(x0, y0) là trung điểm của AB (là giao của d2 và d3)
                x0 = random.randint(-5, 5)
                y0 = random.randint(-5, 5)

                # Bước 2: Tạo các hệ số cho d2 và d3 đi qua M
                # d2: a2*x + b2*y + c2 = 0
                a2, b2 = random.randint(-3, 3), random.randint(-3, 3)
                while a2 == 0 and b2 == 0: a2, b2 = random.randint(-3, 3), random.randint(-3, 3)
                c2 = -(a2*x0 + b2*y0)

                # d3: a3*x + b3*y + c3 = 0 (đảm bảo không song song d2)
                a3, b3 = random.randint(-3, 3), random.randint(-3, 3)
                while (a3 == 0 and b3 == 0) or (a2*b3 - a3*b2 == 0):
                    a3, b3 = random.randint(-3, 3), random.randint(-3, 3)
                c3 = -(a3*x0 + b3*y0)

                # Bước 3: Tạo d1 (song song với AB)
                a1, b1 = random.randint(-3, 3), random.randint(-3, 3)
                while (a1 == 0 and b1 == 0) or (a1*b2 - a2*b1 == 0) or (a1*b3 - a3*b1 == 0):
                    a1, b1 = random.randint(-3, 3), random.randint(-3, 3)
                c1 = random.randint(-10, 10)
                while c1 == -(a1*x0 + b1*y0): # Đảm bảo d1 không đi qua M
                    c1 = random.randint(-10, 10)

                # Bước 4: Tính phương trình cạnh AB: a1(x - x0) + b1(y - y0) = 0
                c_ab = -(a1*x0 + b1*y0)

                # Các chuỗi LaTeX cho phương trình
                str_d1 = format_line(a1, b1, c1)
                str_d2 = format_line(a2, b2, c2)
                str_d3 = format_line(a3, b3, c3)
                str_ab = format_line(a1, b1, c_ab)

                # Đáp án đúng
                da = '$' + str_ab + '$'

                # Tạo các đáp án sai bằng cách thay đổi hệ số tự do hoặc tráo hệ số
                s = [
                    '$' + format_line(a1, b1, c_ab + random.choice([-2, 2, 5])) + '$',
                    '$' + format_line(a2, b2, -(a2*x0 + b2*y0) + 3) + '$',
                    '$' + format_line(b1, a1, -(b1*x0 + a1*y0)) + '$',
                    '$' + format_line(a1, b1, -c_ab) + '$'
                ]

                # Đảm bảo không trùng đáp án đúng
                s = list(set(s))
                if da in s: s.remove(da)
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có các đường trung bình nằm trên các đường thẳng có phương trình '
                    '$d_1: %s, d_2: %s, d_3: %s$. Lập phương trình cạnh $AB$.'
                    % (latex(a1*x + b1*y + c1) + "=0", latex(a2*x + b2*y + c2) + "=0", latex(a3*x + b3*y + c3) + "=0")
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (
                    'Giả sử $d_1$ song song với $AB$, $d_2$ song song với $BC$, $d_3$ song song với $CA$.\\\\ '
                    'Gọi $M$ là trung điểm của $AB$. Khi đó $M = d_2 \\cap d_3$, nên tọa độ $M(x;y)$ thỏa mãn hệ \\\\'
                    '$\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$, ta được $M(%s; %s)$.\\\\ '
                    'Đường thẳng $AB$ đi qua $M$ và song song với $d_1$ nên có phương trình \\\\'
                    '$%s(x - %s) + %s(y - %s) = 0 \\Leftrightarrow %s$.'
                    % (latex(a2*x + b2*y + c2) + "=0", latex(a3*x + b3*y + c3) + "=0", 
                       latex(x0), latex(y0), latex(x0), latex(y0),
                       latex(a1), latex(x0), latex(b1), latex(y0), str_ab)
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content 

