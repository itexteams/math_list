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


def bt_dang23_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random tọa độ 2 điểm A và B
                # Giới hạn tọa độ trong khoảng từ -10 đến 10 để số không quá lớn
                xA = randint(-10, 10)
                yA = randint(-10, 10)
                xB = randint(-10, 10)
                yB = randint(-10, 10)

                # Đảm bảo A và B không trùng nhau
                while xA == xB and yA == yB:
                    xB = randint(-10, 10)
                    yB = randint(-10, 10)

                # Bước 2: Tính toán các thông số
                # Tọa độ trung điểm I
                xI = Rational(xA + xB, 2)
                yI = Rational(yA + yB, 2)

                # Vectơ pháp tuyến là vectơ AB = (xB - xA, yB - yA)
                va = xB - xA
                vb = yB - yA

                # Rút gọn vectơ pháp tuyến (chia cho GCD để phương trình đẹp hơn)
                common = math.gcd(va, vb)
                va = va // common
                vb = vb // common

                # Đảm bảo hệ số đầu tiên không âm để phương trình trông chuẩn hơn
                if va < 0 or (va == 0 and vb < 0):
                    va = -va
                    vb = -vb

                # Phương trình: va*(x - xI) + vb*(y - yI) = 0  => va*x + vb*y + c = 0
                # Trong đó c = -(va*xI + vb*yI)
                c = -(va * xI + vb * yI)

                # Tạo biểu thức Sympy để render latex cho đẹp
                x, y = symbols('x y')
                phuong_trinh_bieu_thuc = va*x + vb*y + c
                kq_final = latex(phuong_trinh_bieu_thuc) + " = 0"

                # Bước 3: Tạo các phương án sai (distractors)
                # Phương án sai 1: Nhầm dấu hệ số tự do
                s1 = latex(va*x + vb*y - c) + " = 0"
                # Phương án sai 2: Nhầm tọa độ (đảo vị trí x, y của vectơ pháp tuyến)
                s2 = latex(vb*x + va*y + c) + " = 0"
                # Phương án sai 3: Lấy nhầm điểm A làm điểm đi qua thay vì trung điểm I
                c_sai = -(va * xA + vb * yA)
                s3 = latex(va*x + vb*y + c_sai) + " = 0"

                # Đảm bảo không trùng với đáp án đúng
                wrong_answers = [s1, s2, s3]
                if kq_final in wrong_answers:
                    # Nếu trùng thì tạo đại 1 phương án khác
                    wrong_answers = [latex(va*x + vb*y + c + 1) + " = 0", 
                                     latex(va*x + vb*y + c - 2) + " = 0", 
                                     latex(vb*x - va*y + c) + " = 0"]

                da = '$' + kq_final + '$'
                das1 = '$' + wrong_answers[0] + '$'
                das2 = '$' + wrong_answers[1] + '$'
                das3 = '$' + wrong_answers[2] + '$'

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$ biết $A(%s; %s)$, $B(%s; %s)$. Phương trình tổng quát đường trung trực của đoạn thẳng $AB$ là'''
                                 % (latex(xA), latex(yA), latex(xB), latex(yB)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # va_nguyen, vb_nguyen dùng để hiển thị trong bước nhân phá ngoặc
                loigiai = ('''Gọi $I$ là trung điểm của $AB$, khi đó: \\\\
                             $x_I = \\frac{x_A + x_B}{2} = \\frac{%s + (%s)}{2} = %s$ \\\\
                             $y_I = \\frac{y_A + y_B}{2} = \\frac{%s + (%s)}{2} = %s$ \\\\
                             Suy ra $I\\left( %s; %s \\right)$. \\\\
                             Đường trung trực của đoạn thẳng $AB$ đi qua $I$ và nhận $\\vec{AB}(%s; %s)$ làm vectơ pháp tuyến. \\\\
                             Chọn vectơ pháp tuyến rút gọn là $\\vec{n}(%s; %s)$. \\\\
                             Phương trình tổng quát của đường trung trực là: \\\\
                             $%s \\left( x - %s \\right) + %s \\left( y - %s \\right) = 0$ \\\\
                             Hay $%s$.'''
                           % (latex(xA), latex(xB), latex(xI),
                              latex(yA), latex(yB), latex(yI),
                              latex(xI), latex(yI),
                              latex(xB - xA), latex(yB - yA),
                              latex(va), latex(vb),
                              latex(va), latex(xI), latex(vb), latex(yI),
                              kq_final
                              ))

            # Xuất câu trắc nghiệm
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

