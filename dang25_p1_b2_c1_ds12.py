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


def bt_dang25_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                a = random.randint(1, 5)

                # Tính M (giá trị lớn nhất) và m (giá trị nhỏ nhất)
                # M = 2*sqrt(a)
                # m = sqrt(2a)

                # Hàm để chuyển giá trị thành chuỗi latex
                def format_sqrt(val):
                    import math
                    root = math.sqrt(val)
                    if root.is_integer():
                        return str(int(root))

                    # Đơn giản hóa căn thức
                    for i in range(int(root), 1, -1):
                        if val % (i**2) == 0:
                            outside = i
                            inside = val // (i**2)
                            if outside == 1:
                                return "\\sqrt{%s}" % inside
                            return "%s\\sqrt{%s}" % (outside, inside)

                    return "\\sqrt{%s}" % val

                str_M = format_sqrt(4 * a) # 2*sqrt(a) = sqrt(4a)
                str_m = format_sqrt(2 * a)

                # Đề bài
                noidungcauhoi = "Hàm số $y = \\sqrt{%s + x} + \\sqrt{%s - x}$ có giá trị lớn nhất, giá trị nhỏ nhất lần lượt là" % (a, a)

                # Các đáp án
                da = "$%s; %s$" % (str_M, str_m)

                # Các đáp án nhiễu
                # Ta có thể tạo các bộ số nhiễu dựa trên các giá trị dễ nhầm lẫn
                # Ví dụ: m; M (ngược), M; a, m; a

                str_a = str(a)
                str_2a = str(2 * a)

                s = [
                    "$%s; %s$" % (str_m, str_M),
                    "$%s; %s$" % (str_M, format_sqrt(a)),
                    "$%s; %s$" % (format_sqrt(2*a), format_sqrt(a)),
                    "$%s; %s$" % (str_a, str_m),
                    "$%s; %s$" % (str_M, str_a),
                    "$%s; %s$" % (str_2a, str_M)
                ]

                # Loại bỏ đáp án đúng khỏi danh sách nhiễu nếu vô tình trùng
                if da in s:
                    s.remove(da)

                s = list(set(s)) # Đảm bảo unique
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tập xác định: $D = [-%s; %s]$. \\\\
            Ta có: $y' = \\frac{1}{2\\sqrt{%s + x}} - \\frac{1}{2\\sqrt{%s - x}}$. \\\\
            Cho $y' = 0 \\Leftrightarrow \\frac{1}{2\\sqrt{%s + x}} = \\frac{1}{2\\sqrt{%s - x}} \\Leftrightarrow \\sqrt{%s + x} = \\sqrt{%s - x} \\Leftrightarrow %s + x = %s - x \\Leftrightarrow 2x = 0 \\Leftrightarrow x = 0 \\in [-%s; %s]$. \\\\
            Tính các giá trị: \\\\
            $y(-%s) = \\sqrt{%s - %s} + \\sqrt{%s + %s} = %s$. \\\\
            $y(0) = \\sqrt{%s + 0} + \\sqrt{%s - 0} = %s$. \\\\
            $y(%s) = \\sqrt{%s + %s} + \\sqrt{%s - %s} = %s$. \\\\
            So sánh các giá trị, ta được giá trị lớn nhất là $%s$ và giá trị nhỏ nhất là $%s$.''' % 
                           (a, a, a, a, a, a, a, a, a, a, a, a,
                            a, a, a, a, a, str_m,
                            a, a, str_M,
                            a, a, a, a, a, str_m,
                            str_M, str_m))

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

