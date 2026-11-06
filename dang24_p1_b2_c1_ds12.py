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


def bt_dang24_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3-Suy nghĩ tìm cách random bài toán
                # Hàm số dạng y = x * sqrt(a - x^2). Vì đây là hàm số lẻ trên tập đối xứng nên M + m luôn bằng 0.
                # Ta chuẩn bị sẵn các trường hợp của a để nghiệm và giá trị cực trị hiển thị đẹp mắt (dưới dạng phân số/căn thức chuẩn).
                list_cases = [
                    {
                        'a': 1,
                        'func': "x\\sqrt{1 - x^2}",
                        'domain': "[-1; 1]",
                        'y_prime': "\\frac{1 - 2x^2}{\\sqrt{1 - x^2}}",
                        'eq_y_prime': "1 - 2x^2 = 0 \\Leftrightarrow x^2 = \\frac{1}{2} \\Leftrightarrow x = \\pm \\frac{\\sqrt{2}}{2}",
                        'x_pos': "\\frac{\\sqrt{2}}{2}",
                        'x_neg': "-\\frac{\\sqrt{2}}{2}",
                        'M': "\\frac{1}{2}",
                        'm': "-\\frac{1}{2}",
                        'ends': "y(1) = 0; y(-1) = 0"
                    },
                    {
                        'a': 2,
                        'func': "x\\sqrt{2 - x^2}",
                        'domain': "[-\\sqrt{2}; \\sqrt{2}]",
                        'y_prime': "\\frac{2 - 2x^2}{\\sqrt{2 - x^2}}",
                        'eq_y_prime': "2 - 2x^2 = 0 \\Leftrightarrow x^2 = 1 \\Leftrightarrow x = \\pm 1",
                        'x_pos': "1",
                        'x_neg': "-1",
                        'M': "1",
                        'm': "-1",
                        'ends': "y(\\sqrt{2}) = 0; y(-\\sqrt{2}) = 0"
                    },
                    {
                        'a': 3,
                        'func': "x\\sqrt{3 - x^2}",
                        'domain': "[-\\sqrt{3}; \\sqrt{3}]",
                        'y_prime': "\\frac{3 - 2x^2}{\\sqrt{3 - x^2}}",
                        'eq_y_prime': "3 - 2x^2 = 0 \\Leftrightarrow x^2 = \\frac{3}{2} \\Leftrightarrow x = \\pm \\frac{\\sqrt{6}}{2}",
                        'x_pos': "\\frac{\\sqrt{6}}{2}",
                        'x_neg': "-\\frac{\\sqrt{6}}{2}",
                        'M': "\\frac{3}{2}",
                        'm': "-\\frac{3}{2}",
                        'ends': "y(\\sqrt{3}) = 0; y(-\\sqrt{3}) = 0"
                    },
                    {
                        'a': 4,
                        'func': "x\\sqrt{4 - x^2}",
                        'domain': "[-2; 2]",
                        'y_prime': "\\frac{4 - 2x^2}{\\sqrt{4 - x^2}}",
                        'eq_y_prime': "4 - 2x^2 = 0 \\Leftrightarrow x^2 = 2 \\Leftrightarrow x = \\pm \\sqrt{2}",
                        'x_pos': "\\sqrt{2}",
                        'x_neg': "-\\sqrt{2}",
                        'M': "2",
                        'm': "-2",
                        'ends': "y(2) = 0; y(-2) = 0"
                    }
                ]

                # Random chọn một trường hợp
                case = random.choice(list_cases)
                a = case['a']

                # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng (0)
                s = [a, -a, a*2, -a*2, 1, 2, 3, -1, -2, -3]
                s = [x for x in s if x != 0] # Lọc bỏ giá trị 0
                s = list(set(s)) # Đảm bảo các phần tử không trùng nhau
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Gọi $M$ là giá trị lớn nhất và $m$ là giá trị nhỏ nhất của hàm số $y = %s$. Khi đó $M + m$ bằng''' % case['func'])

                # Đưa các đáp án vào danh sách
                da_d = ('\\True $0$')
                da_s1 = ('$%s$' % das1)
                da_s2 = ('$%s$' % das2)
                da_s3 = ('$%s$' % das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Tập xác định của hàm số là $D = %s$. \\\\
            Đạo hàm $y' = \\sqrt{%s - x^2} + x \\cdot \\frac{-2x}{2\\sqrt{%s - x^2}} = %s$. \\\\
            Cho $y' = 0 \\Leftrightarrow %s$. \\\\
            Ta có: \\\\
            $y\\left(%s\\right) = %s$. \\\\
            $y\\left(%s\\right) = %s$. \\\\
            $%s$. \\\\
            Suy ra giá trị lớn nhất của hàm số là $M = %s$ và giá trị nhỏ nhất là $m = %s$. \\\\
            Vậy $M + m = %s + \\left(%s\\right) = 0$.''' % (
                    case['domain'],
                    a, a, case['y_prime'],
                    case['eq_y_prime'],
                    case['x_pos'], case['M'],
                    case['x_neg'], case['m'],
                    case['ends'],
                    case['M'], case['m'],
                    case['M'], case['m']
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{\n' + str(loigiai) + '\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

