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


def bt_dang76_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến loại câu hỏi
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Sinh dữ liệu ngẫu nhiên và kiểm tra điều kiện để tránh m/0
                found = False
                while not found:
                    xA = randint(-5, 5)
                    yA = randint(-5, 5)
                    xB = randint(-5, 5)
                    yB = randint(-5, 5)
                    c = randint(1, 5) # Delta: mx - y + c = 0

                    # Tính toán các giá trị trung gian
                    xI = Rational(xA + xB, 2)
                    yI = Rational(yA + yB, 2)
                    vecAB_x = xB - xA
                    vecAB_y = yB - yA

                    # nx_AB = vecAB_y, ny_AB = -vecAB_x
                    nx_AB = vecAB_y
                    ny_AB = -vecAB_x

                    # ĐIỀU KIỆN QUAN TRỌNG: 
                    # 1. xI != 0 để m1 không bị triệt tiêu hoành độ
                    # 2. nx_AB != 0 và ny_AB != 0 để tỉ số m/nx = -1/ny không có mẫu bằng 0
                    # 3. xA != xB và yA != yB để đường thẳng AB không thẳng đứng/nằm ngang
                    if xI != 0 and nx_AB != 0 and ny_AB != 0:
                        # m1: Delta đi qua trung điểm I
                        # m*xI - yI + c = 0 => m = (yI - c) / xI
                        m1 = (yI - c) / xI

                        # m2: Delta song song với AB
                        # n_delta = (m, -1) cùng phương với n_AB = (nx_AB, ny_AB)
                        # m/nx_AB = -1/ny_AB => m = -nx_AB / ny_AB
                        m2 = Rational(-nx_AB, ny_AB)

                        # Chỉ lấy kết quả nếu m1 khác m2 và phân số đẹp (mẫu số nhỏ hơn 10)
                        if m1 != m2 and m1.q < 10 and m2.q < 10:
                            found = True

                # Hàm định dạng ngoặc vuông bên trái cho kết quả m
                def format_m_result(val1, val2):
                    return r'\left[ \begin{aligned} & m = ' + latex(val1) + r' \\ & m = ' + latex(val2) + r' \end{aligned} \right.'

                da_dung = format_m_result(m1, m2)

                # Tạo các đáp án sai (nhiễu)
                s = [
                    format_m_result(-m1, m2),
                    format_m_result(m1, -m2),
                    format_m_result(m1 + 1, m2),
                    format_m_result(m2, m2 + Rational(1, 2)),
                    format_m_result(-m1, -m2)
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng với hệ tọa độ $Oxy$, cho hai điểm $A(%s;%s)$, $B(%s;%s)$ và đường thẳng $\\Delta: mx - y + %s = 0$. Tìm giá trị của tham số $m$ để $\\Delta$ cách đều hai điểm $A, B$.'
                                %(latex(xA), latex(yA), latex(xB), latex(yB), latex(c)))

                # Các đáp án
                da_d = '\\True $' + da_dung + '$'
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết, không bao giờ có mẫu số bằng 0
                loigiai = ('''Gọi $I$ là trung điểm đoạn $AB \\to \\begin{cases} I\\left( %s; %s \\right) \\\\ \\vec{AB} = (%s; %s) \\to \\vec{n}_{AB} = (%s; %s) \\end{cases}$. \\\\
            Khi đó: $\\Delta: mx - y + %s = 0$ (có $\\vec{n}_{\\Delta} = (m; -1)$) cách đều $A, B$ khi và chỉ khi: \\\\
            $\\left[ \\begin{matrix} I \\in \\Delta \\\\ \\Delta \\parallel AB \\end{matrix} \\right. \\Leftrightarrow \\left[ \\begin{matrix} m \\cdot \\left( %s \\right) - \\left( %s \\right) + %s = 0 \\\\ \\frac{m}{%s} = \\frac{-1}{%s} \\end{matrix} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & m = %s \\\\ & m = %s \\end{aligned} \\right.$.'''
                          %(latex(xI), latex(yI), latex(vecAB_x), latex(vecAB_y), latex(nx_AB), latex(ny_AB), 
                            latex(c), latex(xI), latex(yI), latex(c), latex(nx_AB), latex(ny_AB), latex(m1), latex(m2)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

