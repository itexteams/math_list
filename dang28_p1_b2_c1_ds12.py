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


def bt_dang28_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random đoạn [a; b] sao cho số e (xấp xỉ 2.718) luôn nằm trong đoạn để có sự biến thiên
                a = random.randint(1, 2)
                b = random.randint(3, 5)

                # Tránh trường hợp y(2) = y(4) = ln(2)/2 dẫn đến 2 giá trị giống hệt nhau
                while a == 2 and b == 4:
                    b = random.randint(3, 5)

                # Hàm tính giá trị y để so sánh
                def eval_y(x_val):
                    if x_val == 1: 
                        return 0
                    if x_val == 'e': 
                        return 1 / math.e
                    return math.log(x_val) / x_val

                # Hàm định dạng chuỗi LaTeX cho giá trị y
                def format_y(x_val):
                    if x_val == 1: 
                        return "0"
                    if x_val == 'e': 
                        return "\\frac{1}{e}"
                    return "\\frac{\\ln %s}{%s}" % (x_val, x_val)

                # Tính toán các giá trị tại biên và tại điểm cực trị x = e
                val_a = eval_y(a)
                val_b = eval_y(b)
                val_e = eval_y('e')

                str_a = format_y(a)
                str_b = format_y(b)
                str_e = format_y('e')

                # Tìm giá trị nhỏ nhất (min)
                min_val = min(val_a, val_b, val_e)
                if min_val == val_a:
                    kq_str = str_a
                elif min_val == val_b:
                    kq_str = str_b
                else:
                    kq_str = str_e

                # Đáp án đúng
                du = ['$%s$' % (kq_str)]
                da = random.choice(du)

                # Tạo các phương án nhiễu (kể cả giá trị lớn nhất và các biên khác)
                s = [
                    '$%s$' % (str_a),
                    '$%s$' % (str_b),
                    '$%s$' % (str_e),
                    '$\\frac{2}{e^2}$',
                    '$\\frac{3}{e^2}$',
                    '$\\frac{\\ln %s}{%s}$' % (b + 1, b + 1)
                ]

                # Loại bỏ các phương án trùng lặp và xóa đáp án đúng khỏi danh sách nhiễu
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Giá trị nhỏ nhất của hàm số $y = \\frac{\\ln x}{x}$ trên đoạn $[%s; %s]$ bằng''' % (a, b))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Hàm số đã cho xác định và liên tục trên đoạn $[%s; %s]$.\\\\
                           Ta có đạo hàm $y' = \\frac{(\\ln x)' \\cdot x - \\ln x \\cdot (x)'}{x^2} = \\frac{\\frac{1}{x} \\cdot x - \\ln x \\cdot 1}{x^2} = \\frac{1 - \\ln x}{x^2}$.\\\\
                           Cho $y' = 0 \\Leftrightarrow 1 - \\ln x = 0 \\Leftrightarrow \\ln x = 1 \\Leftrightarrow x = e \\in [%s; %s]$.\\\\
                           Ta có: $y(%s) = %s$; $y(%s) = %s$; $y(e) = %s$.\\\\
                           So sánh các giá trị, ta được $\\min\\limits_{[%s; %s]} y = %s$.'''
                           % (a, b,
                              a, b,
                              a, str_a, b, str_b, str_e,
                              a, b, kq_str))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

