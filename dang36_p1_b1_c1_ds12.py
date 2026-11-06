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


def bt_dang36_p1_b1_c1_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng đa thức bậc 2: ax^2 + bx + c
            def format_poly2(a, b, c):
                res = ""
                if a == 1: res += "x^2"
                elif a == -1: res += "-x^2"
                else: res += str(a) + "x^2"

                if b == 1: res += " + x"
                elif b == -1: res += " - x"
                elif b > 0: res += " + " + str(b) + "x"
                elif b < 0: res += " - " + str(abs(b)) + "x"

                if c > 0: res += " + " + str(c)
                elif c < 0: res += " - " + str(abs(c))

                return res

            # Hàm hỗ trợ định dạng đa thức bậc 1: ax + b
            def format_poly1(a, b):
                res = ""
                if a == 1: res += "x"
                elif a == -1: res += "-x"
                else: res += str(a) + "x"

                if b > 0: res += " + " + str(b)
                elif b < 0: res += " - " + str(abs(b))

                return res

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                while True:
                    # Random các hệ số
                    x0 = random.choice([-3, -2, -1, 1, 2, 3])
                    k = random.choice([-3, -2, -1, 1, 2, 3])
                    if x0 == -k: # Đảm bảo nghiệm x_M không trùng với điều kiện xác định
                        continue

                    b = 2 * k
                    D = random.choice([2, 3, 5, 6, 7, 8, 10]) # Delta' dương và không phải số chính phương
                    c = D - x0**2 - b*x0
                    break

                x_M = -k
                B = -2*x0
                C = -(b*x0 + c)

                # Chuỗi hiển thị cho hàm số ban đầu
                tu_so_str = format_poly2(1, b, c)
                mau_so_str = format_poly1(1, -x0)

                # Chuỗi hiển thị cho đạo hàm và đường thẳng đi qua cực trị
                y_prime_num = format_poly2(1, B, C)
                y_prime_den = "(" + mau_so_str + ")^2"

                extrema_line_num = format_poly1(2, b)
                extrema_line = format_poly1(2, b)

                pt_b = "+ " + str(b) if b > 0 else "- " + str(abs(b))

                # Các đáp án trắc nghiệm
                da_d = ('\\True $x_M = %s$' % x_M)
                da_s1 = ('$x_M = %s - \\sqrt{%s}$' % (x0, D))
                da_s2 = ('$x_M = %s$' % x0)
                da_s3 = ('$x_M = %s + \\sqrt{%s}$' % (x0, D))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Câu hỏi
                noidungcauhoi = ('Biết đồ thị $(C)$ của hàm số $y = \\frac{%s}{%s}$ có hai điểm cực trị. Đường thẳng đi qua hai điểm cực trị của đồ thị $(C)$ cắt trục hoành tại điểm $M$ có hoành độ $x_M$ bằng' % (tu_so_str, mau_so_str))

                # Lời giải
                loigiai = ('Tập xác định hàm số $D = \\mathbb{R} \\setminus \\{%s\\}$.\\\\ \n'
                           'Ta có $y\' = \\frac{%s}{%s}$; $y\' = 0 \\Rightarrow %s = 0 \\Rightarrow x = %s \\pm \\sqrt{%s}$ (Hàm số có hai điểm cực trị).\\\\ \n'
                           'Đường thẳng đi qua hai điểm cực trị của $(C)$ là $d$: $y = \\frac{u\'(x)}{v\'(x)} = \\frac{%s}{1}$ hay $y = %s$.\\\\ \n'
                           'Gọi $M(x_M; 0) \\in Ox$; vì $M(x_M; 0) \\in d \\Rightarrow 0 = 2x_M %s \\Rightarrow x_M = %s$.'
                           % (x0, 
                              y_prime_num, y_prime_den, y_prime_num, x0, D,
                              extrema_line_num, extrema_line,
                              pt_b, x_M))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                       '\\choice \n'
                       '{'+str(list_1[1])+'}\n'
                       '{'+str(list_1[2])+'}\n'
                       '{'+str(list_1[3])+'}\n'
                       '{'+str(list_1[0])+'}\n'
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

