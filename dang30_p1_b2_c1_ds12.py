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


def bt_dang30_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các tham số cho hàm số y = a + sqrt(x^2 - 2bx + c) với c = b^2 + k^2
                a = random.randint(1, 5)

                # Random b và dấu của b
                b_val = random.randint(1, 4)
                sign = random.choice([-1, 1])
                b = b_val * sign

                k = random.randint(1, 4)

                c = b**2 + k**2
                min_y = a + k

                # Các chuỗi định dạng
                a_str = str(a)
                b_str = str(b)
                c_str = str(c)
                k_str = str(k)
                k2_str = str(k**2)
                min_y_str = str(min_y)

                # Chuỗi cho hệ số bậc 1 của x
                B = -2 * b
                if B < 0:
                    str_B = "- %sx" % abs(B)
                    str_B_prime = "- %s" % abs(B)
                    str_B_coef_sub = "- %s" % abs(B)
                else:
                    str_B = "+ %sx" % B
                    str_B_prime = "+ %s" % B
                    str_B_coef_sub = "+ %s" % B

                str_c = "+ %s" % c

                # Chuỗi cho tử số đạo hàm và hằng đẳng thức
                if b > 0:
                    square_expr = "(x - %s)^2" % b
                    tu_so = "x - %s" % b
                else:
                    square_expr = "(x + %s)^2" % abs(b)
                    tu_so = "x + %s" % abs(b)

                # Chuỗi cho giá trị b khi thay vào biểu thức (đóng ngoặc nếu âm)
                if b < 0:
                    b_sub = "(%s)" % b
                else:
                    b_sub = str(b)

                # Câu hỏi
                ham_so = "%s + \\sqrt{x^2 %s %s}" % (a_str, str_B, str_c)
                noidungcauhoi = "Giá trị nhỏ nhất của hàm số $y = %s$ bằng" % ham_so

                # Đáp án đúng
                da_str = "\\min\\limits_{\\mathbb{R}} y = %s" % min_y_str
                du = ['$%s$' % da_str]
                da = random.choice(du)

                # Các phương án nhiễu
                s = [
                    "$\\min\\limits_{\\mathbb{R}} y = %s$" % a_str,
                    "$\\min\\limits_{\\mathbb{R}} y = %s$" % (a + c),
                    "$\\min\\limits_{\\mathbb{R}} y = %s + \\sqrt{%s}$" % (a_str, c_str),
                    "$\\min\\limits_{\\mathbb{R}} y = 0$",
                    "$\\min\\limits_{\\mathbb{R}} y = %s$" % k_str,
                    "$\\min\\limits_{\\mathbb{R}} y = %s$" % (min_y + 1)
                ]

                # Lọc trùng và xóa đáp án đúng
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Format phương án trả lời
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Sử dụng đạo hàm)
                loigiai = ('''Tập xác định $D = \\mathbb{R}$ (vì $x^2 %s %s = %s + %s > 0$ với mọi $x \\in \\mathbb{R}$).\\\\
                           Ta có đạo hàm $y' = \\frac{(x^2 %s %s)'}{2\\sqrt{x^2 %s %s}} = \\frac{2x %s}{2\\sqrt{x^2 %s %s}} = \\frac{%s}{\\sqrt{x^2 %s %s}}$.\\\\
                           Cho $y' = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow x = %s$.\\\\
                           Bảng biến thiên cho thấy qua $x = %s$, $y'$ đổi dấu từ âm sang dương nên hàm số đạt giá trị nhỏ nhất tại $x = %s$.\\\\
                           Ta có $y(%s) = %s + \\sqrt{%s^2 %s \\cdot %s %s} = %s$.\\\\
                           Vậy $\\min\\limits_{\\mathbb{R}} y = %s$.'''
                           % (str_B, str_c, square_expr, k2_str,
                              str_B, str_c, str_B, str_c, str_B_prime, str_B, str_c, tu_so, str_B, str_c,
                              tu_so, b_str,
                              b_str, b_str,
                              b_str, a_str, b_sub, str_B_coef_sub, b_sub, str_c, min_y_str,
                              min_y_str))

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

