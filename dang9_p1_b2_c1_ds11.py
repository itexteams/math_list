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


def bt_dang9_p1_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập random bài toán
                # Chọn ngẫu nhiên loại hàm: 'cos' hoặc 'sin'
                loai_ham = random.choice(['cos', 'sin'])
                # Chọn ngẫu nhiên dấu trong ngoặc: '+' hoặc '-'
                dau_ngoac = random.choice(['+', '-'])
                # Chọn ngẫu nhiên góc lượng giác đặc biệt
                mau_so = random.choice([3, 4, 6])
                goc_val = Rational(1, mau_so) # hệ số của pi

                # Tính toán các giá trị lượng giác bằng SymPy
                val_cos = cos(goc_val * pi)
                val_sin = sin(goc_val * pi)

                # Định dạng hiển thị chuỗi LaTeX cho các hệ số lượng giác đặc biệt
                str_cos = latex(val_cos).replace('.', ',')
                str_sin = latex(val_sin).replace('.', ',')

                # Chuỗi vế trái
                str_vt = '%s\\left(\\alpha %s \\frac{\\pi}{%s}\\right)' % (loai_ham, dau_ngoac, latex(mau_so))

                # Xác định vế phải chính xác theo công thức cộng lượng giác
                if loai_ham == 'cos':
                    if dau_ngoac == '+':
                        # cos(a + b) = cos(a)cos(b) - sin(a)sin(b)
                        str_vd_dung = '%s\\cos\\alpha - %s\\sin\\alpha' % (str_cos, str_sin)
                        giai_thich_buoc = '\\cos\\alpha \\cdot \\cos\\frac{\\pi}{%s} - \\sin\\alpha \\cdot \\sin\\frac{\\pi}{%s}' % (latex(mau_so), latex(mau_so))
                        # Bộ nhiễu cho hàm cos(+)
                        nhiieu_list = [
                            '\\cos\\alpha + %s' % str_cos,
                            '%s\\sin\\alpha - %s\\cos\\alpha' % (str_cos, str_sin),
                            '%s\\sin\\alpha - %s\\cos\\alpha' % (str_sin, str_cos),
                            '%s\\cos\\alpha + %s\\sin\\alpha' % (str_cos, str_sin)
                        ]
                    else:
                        # cos(a - b) = cos(a)cos(b) + sin(a)sin(b)
                        str_vd_dung = '%s\\cos\\alpha + %s\\sin\\alpha' % (str_cos, str_sin)
                        giai_thich_buoc = '\\cos\\alpha \\cdot \\cos\\frac{\\pi}{%s} + \\sin\\alpha \\cdot \\sin\\frac{\\pi}{%s}' % (latex(mau_so), latex(mau_so))
                        nhiieu_list = [
                            '\\cos\\alpha - %s' % str_cos,
                            '%s\\cos\\alpha - %s\\sin\\alpha' % (str_cos, str_sin),
                            '%s\\sin\\alpha + %s\\cos\\alpha' % (str_cos, str_sin),
                            '%s\\sin\\alpha - %s\\cos\\alpha' % (str_sin, str_cos)
                        ]
                else: # loai_ham == 'sin'
                    if dau_ngoac == '+':
                        # sin(a + b) = sin(a)cos(b) + cos(a)sin(b)
                        str_vd_dung = '%s\\sin\\alpha + %s\\cos\\alpha' % (str_cos, str_sin)
                        giai_thich_buoc = '\\sin\\alpha \\cdot \\cos\\frac{\\pi}{%s} + \\cos\\alpha \\cdot \\sin\\frac{\\pi}{%s}' % (latex(mau_so), latex(mau_so))
                        nhiieu_list = [
                            '\\sin\\alpha + %s' % str_sin,
                            '%s\\sin\\alpha - %s\\cos\\alpha' % (str_cos, str_sin),
                            '%s\\cos\\alpha - %s\\sin\\alpha' % (str_cos, str_sin),
                            '%s\\cos\\alpha + %s\\sin\\alpha' % (str_sin, str_cos)
                        ]
                    else:
                        # sin(a - b) = sin(a)cos(b) - cos(a)sin(b)
                        str_vd_dung = '%s\\sin\\alpha - %s\\cos\\alpha' % (str_cos, str_sin)
                        giai_thich_buoc = '\\sin\\alpha \\cdot \\cos\\frac{\\pi}{%s} - \\cos\\alpha \\cdot \\sin\\frac{\\pi}{%s}' % (latex(mau_so), latex(mau_so))
                        nhiieu_list = [
                            '\\sin\\alpha - %s' % str_sin,
                            '%s\\sin\\alpha + %s\\cos\\alpha' % (str_cos, str_sin),
                            '%s\\cos\\alpha - %s\\sin\\alpha' % (str_sin, str_cos),
                            '%s\\cos\\alpha + %s\\sin\\alpha' % (str_cos, str_sin)
                        ]

                # Đáp án đúng
                da = '$%s = %s$' % (str_vt, str_vd_dung)
                da_chon = da

                # B4: Điều chỉnh các phương án sai không được trùng với đáp án đúng
                s_set = set()
                for bieu_thuc_sai in nhiieu_list:
                    p_an_sai = '$%s = %s$' % (str_vt, bieu_thuc_sai)
                    if p_an_sai != da:
                        s_set.add(p_an_sai)

                list_sai = list(s_set)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Đẳng thức nào sau đây là đúng?''')

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Ta có: $%s = %s = %s$.'''
                           % (str_vt, giai_thich_buoc, str_vd_dung))

            # Xuất câu trắc nghiệm định dạng minipage TeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

