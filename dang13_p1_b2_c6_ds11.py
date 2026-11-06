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


def bt_dang13_p1_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random bài toán
                # n_total: Tổng số học sinh (từ 35 đến 50)
                # n_math: Nam giỏi Toán
                # n_lit: Nữ giỏi Văn
                n_total = randint(35, 50)
                n_math = randint(10, 18)
                n_lit = randint(5, 9)

                # Tính toán xác suất đúng
                tu_so = n_math + n_lit
                kq_frac = Rational(tu_so, n_total)

                # Đáp án đúng
                da = '$%s$' % (latex(kq_frac))

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s_list = []
                # Sai lầm 1: Lấy hiệu thay vì cộng
                s_list.append(Rational(abs(n_math - n_lit), n_total))
                # Sai lầm 2: Chỉ lấy nam giỏi Toán
                s_list.append(Rational(n_math, n_total))
                # Sai lầm 3: Chỉ lấy nữ giỏi Văn
                s_list.append(Rational(n_lit, n_total))
                # Sai lầm 4: Lấy phần bù
                s_list.append(Rational(n_total - tu_so, n_total))
                # Sai lầm 5: Một phân số ngẫu nhiên khác
                s_list.append(Rational(randint(2, 12), n_total))

                # Lọc bỏ các giá trị trùng với đáp án đúng và trùng nhau
                s_filtered = []
                for item in s_list:
                    val = '$%s$' % (latex(item))
                    if val != da and val not in s_filtered:
                        s_filtered.append(val)

                # Lấy 3 đáp án sai từ danh sách đã lọc
                random.shuffle(s_filtered)
                das1 = s_filtered[0]
                das2 = s_filtered[1]
                das3 = s_filtered[2]

                # Câu hỏi
                noidungcauhoi = ('''Một lớp học $%s$ học sinh gồm có $%s$ học sinh nam giỏi Toán và $%s$ học sinh nữ giỏi Văn. Chọn ngẫu nhiên một học sinh. Xác suất để chọn được một nam sinh giỏi Toán hoặc một nữ sinh giỏi Văn là'''
                                 % (latex(n_total), latex(n_math), latex(n_lit)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết lại chi tiết giống ảnh, không viết tắt)
                # n(A) và n(B) là số kết quả thuận lợi
                p_a = Rational(n_math, n_total)
                p_b = Rational(n_lit, n_total)

                loigiai = ('''Gọi $A$ là biến cố: "chọn một nam sinh giỏi Toán"; $B$ là biến cố: "chọn một nữ sinh giỏi Văn". \\\\
            Khi đó $A \\cup B$ là biến cố: "chọn được một nam sinh giỏi Toán hoặc một nữ sinh giỏi Văn". \\\\
            Ta thấy $A$ và $B$ là $2$ biến cố xung khắc. \\\\
            Số phần tử của không gian mẫu: $n\\left(\\Omega\\right) = %s$. \\\\
            Số kết quả thuận lợi của biến cố $A, B$ lần lượt là: $n\\left(A\\right) = %s, n\\left(B\\right) = %s$. \\\\
            Suy ra: $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = %s$ và $P\\left(B\\right) = \\frac{n\\left(B\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = %s$. \\\\
            Vậy xác suất cần tính là: $P\\left(A \\cup B\\right) = P\\left(A\\right) + P\\left(B\\right) = \\frac{%s}{%s} + \\frac{%s}{%s} = %s$.'''
                           % (latex(n_total), latex(n_math), latex(n_lit),
                              latex(n_math), latex(n_total), latex(p_a),
                              latex(n_lit), latex(n_total), latex(p_b),
                              latex(n_math), latex(n_total), latex(n_lit), latex(n_total), latex(kq_frac)))

            # Xuất câu trắc nghiệm (B2: Đúng cấu trúc mẫu, không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

