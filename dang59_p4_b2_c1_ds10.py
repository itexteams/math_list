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


def bt_dang59_p4_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các giá trị ngẫu nhiên để tạo bài toán hợp lý
                x_val = random.randint(4, 8)       # Số học sinh đăng ký cả 3 tổ hợp
                a = random.randint(2, 5)           # Số học sinh thuộc giao của A00 và B00 (sau khi trừ đi x)
                b = random.randint(2, 5)           # Số học sinh thuộc giao của A00 và A01 (sau khi trừ đi x)
                c = random.randint(2, 5)           # Số học sinh thuộc giao của B00 và A01 (sau khi trừ đi x)
                d = random.randint(8, 15)          # Số học sinh chỉ đăng ký A00
                e = random.randint(8, 15)          # Số học sinh chỉ đăng ký B00
                f = random.randint(8, 15)          # Số học sinh chỉ đăng ký A01

                # Tính toán các số liệu cho đề bài theo công thức bao hàm - loại trừ
                total = d + e + f + a + b + c + x_val
                nA = d + a + b + x_val
                nB = e + a + c + x_val
                nC = f + b + c + x_val

                nAB = a + x_val
                nAC = b + x_val
                nBC = c + x_val

                # Đáp án đúng
                kq = x_val
                da = '$%s$' % latex(kq)

                # Các đáp án trắc nghiệm sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    error_val = kq + random.choice([-3, -2, -1, 1, 2, 3])
                    if error_val > 0 and error_val != kq:
                        s.add('$%s$' % latex(error_val))

                s = list(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một lớp có $%s$ học sinh đăng ký xét tuyển Đại học theo các tổ hợp xét tuyển $A00$, $B00$ và $A01$; mỗi em đăng ký ít nhất một tổ hợp. Có $%s$ em đăng ký xét tuyển tổ hợp $A00$, $%s$ em đăng ký xét tuyển khối $B00$, $%s$ đăng ký xét tuyển tổ hợp $A01$. Có $%s$ em đăng ký đúng hai tổ hợp $A00$ và $B00$; Có $%s$ em đăng ký đúng hai khối $A00$ và $A01$; Có $%s$ em đăng ký đúng hai tổ hợp $B00$ và $A01$. Tìm số học sinh đăng ký cả ba tổ hợp $A00$, $B00$, $A01$.'''
                                 % (latex(total), latex(nA), latex(nB), latex(nC), latex(nAB), latex(nAC), latex(nBC)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $A$, $B$, $C$ lần lượt là tập hợp các học sinh đăng ký tổ hợp $A00$, $B00$ và $A01$.\\\\
                             Theo giả thiết bài toán, ta có các số liệu sau:\\\\
                             + Tổng số học sinh đăng ký xét tuyển là $n(A \\cup B \\cup C) = %s$.\\\\
                             + Số học sinh đăng ký tổ hợp $A00$ là $n(A) = %s$.\\\\
                             + Số học sinh đăng ký tổ hợp $B00$ là $n(B) = %s$.\\\\
                             + Số học sinh đăng ký tổ hợp $A01$ là $n(C) = %s$.\\\\
                             + Số học sinh đăng ký cả hai tổ hợp $A00$ và $B00$ là $n(A \\cap B) = %s$.\\\\
                             + Số học sinh đăng ký cả hai tổ hợp $A00$ và $A01$ là $n(A \\cap C) = %s$.\\\\
                             + Số học sinh đăng ký cả hai tổ hợp $B00$ và $A01$ là $n(B \\cap C) = %s$.\\\\
                             Sử dụng công thức bao hàm - loại trừ cho ba tập hợp:\\\\
                             $n(A \\cup B \\cup C) = n(A) + n(B) + n(C) - n(A \\cap B) - n(A \\cap C) - n(B \\cap C) + n(A \\cap B \\cap C)$.\\\\
                             Thay các giá trị đã biết vào công thức, ta được:\\\\
                             $%s = %s + %s + %s - (%s + %s + %s) + n(A \\cap B \\cap C)$\\\\
                             $%s = %s - %s + n(A \\cap B \\cap C)$\\\\
                             $%s = %s + n(A \\cap B \\cap C)$\\\\
                             Suy ra: $n(A \\cap B \\cap C) = %s - %s = %s$.\\\\
                             Vậy có $%s$ em đăng ký học cả ba tổ hợp $A00$, $B00$, $A01$.'''
                           % (latex(total), latex(nA), latex(nB), latex(nC), latex(nAB), latex(nAC), latex(nBC),
                              latex(total), latex(nA), latex(nB), latex(nC), latex(nAB), latex(nAC), latex(nBC),
                              latex(total), latex(nA + nB + nC), latex(nAB + nAC + nBC),
                              latex(total), latex(nA + nB + nC - (nAB + nAC + nBC)),
                              latex(total), latex(nA + nB + nC - (nAB + nAC + nBC)), latex(kq), latex(kq)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

