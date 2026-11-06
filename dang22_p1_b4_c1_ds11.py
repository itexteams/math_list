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


def bt_dang22_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Giữ nguyên hệ số a=2, c=1. Random pha b và d.
                a = 2
                c = 1
                list_pha = [
                    (Rational(-1, 4), Rational(3, 4)),
                    (Rational(1, 4), Rational(-3, 4)),
                    (Rational(-1, 3), Rational(1, 3)),
                    (Rational(1, 6), Rational(5, 6)),
                    (Rational(1, 3), Rational(-1, 6))
                ]
                b, d = random.choice(list_pha)

                # Tính toán hệ số cho họ nghiệm 1: x = (d-b)pi + k2pi
                ho1_heso = d - b
                ho1_chuky = 2

                # Tính toán hệ số cho họ nghiệm 2: x = (1-d-b)pi/3 + k2pi/3
                ho2_heso = Rational(1 - d - b, 3)
                ho2_chuky = Rational(2, 3)

                nghiem_list = []

                # Lọc k cho cả 2 họ trong khoảng (0, 1) (tức là 0 < x < pi)
                # Duyệt k từ -5 đến 5 là đủ bao trùm cho khoảng (0; pi)
                for k in range(-5, 6):
                    # Kiểm tra họ 1
                    val1 = ho1_heso + k * ho1_chuky
                    if 0 < val1 < 1:
                        nghiem_list.append(val1)

                    # Kiểm tra họ 2
                    val2 = ho2_heso + k * ho2_chuky
                    if 0 < val2 < 1:
                        nghiem_list.append(val2)

                # Tính tổng nghiệm
                tong_nghiem = sum(nghiem_list)
                da = tong_nghiem
                da_latex = '$%s$' % latex(da * pi) if da != 0 else '$0$'

                # B4: Điều chỉnh phương án sai không trùng đáp án đúng
                sai_set = set()
                while len(sai_set) < 3:
                    # Tạo sai số ngẫu nhiên
                    sai_so = random.choice([Rational(1,4), Rational(-1,4), Rational(1,2), Rational(-1,2), Rational(1,6), Rational(-1,6), 1])
                    sai_val = da + sai_so
                    # Đảm bảo phương án sai luôn dương và khác đáp án đúng
                    if sai_val != da and sai_val > 0:
                        sai_set.add('$%s$' % latex(sai_val * pi))

                sai_list = list(sai_set)

                # B1 & B2: Khởi tạo chuỗi đề bài
                pt_trai = latex(a*x + b*pi)
                pt_phai = latex(c*x + d*pi)

                noidungcauhoi = (f"Cho phương trình $\\sin \\left( {pt_trai} \\right) = \\sin \\left( {pt_phai} \\right)$. "
                                 f"Tổng các nghiệm thuộc khoảng $(0;\\pi)$ của phương trình trên là")

                # Các đáp án
                da_d = ('\\True ' + da_latex)
                da_s1 = sai_list[0]
                da_s2 = sai_list[1]
                da_s3 = sai_list[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"Ta có: $\\sin \\left( {pt_trai} \\right) = \\sin \\left( {pt_phai} \\right) "
                           f"\\Leftrightarrow \\left[ \\begin{{aligned}} & {pt_trai} = {pt_phai} + k2\\pi \\\\ "
                           f"& {pt_trai} = \\pi - \\left( {pt_phai} \\right) + k2\\pi \\end{{aligned}} \\right.$\\\\\n"
                           f"$\\Leftrightarrow \\left[ \\begin{{aligned}} & x = {latex(ho1_heso*pi)} + k2\\pi \\\\ "
                           f"& x = {latex(ho2_heso*pi)} + k\\frac{{2\\pi}}{{3}} \\end{{aligned}} \\right. \\quad (k \\in \\mathbb{{Z}})$.\\\\\n"
                           f"+ Xét họ nghiệm thứ nhất, do $0 < x < \\pi$ nên không có giá trị $k \\in \\mathbb{{Z}}$ nào thỏa mãn (hoặc bạn có thể liệt kê nếu có).\\\\\n"
                           f"+ Xét họ nghiệm thứ hai, do $0 < x < \\pi$ ta tìm được các nghiệm hợp lệ.\\\\\n"
                           f"Tổng các nghiệm thu được là: {da_latex}.")

                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\choice \n'
                           '{' + str(list_1[1]) + '}\n'
                           '{' + str(list_1[2]) + '}\n'
                           '{' + str(list_1[3]) + '}\n'
                           '{' + str(list_1[0]) + '}\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n\\end{minipage}\n\n')
            return content

