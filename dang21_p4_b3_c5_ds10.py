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


def bt_dang21_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn ngẫu nhiên số mũ n từ 4 đến 6 để đảm bảo độ phức tạp vừa phải
                n = randint(4, 6)

                # Hàm hỗ trợ định dạng LaTeX theo yêu cầu
                def format_latex(expr_obj):
                    res = latex(expr_obj)
                    res = res.replace('(', '\\left(').replace(')', '\\right)')
                    return res

                # 1. Tính toán đáp án đúng
                x_sym = symbols('x')
                bieu_thuc = (x_sym - 1/x_sym)**n
                # Khai triển và sắp xếp theo số mũ giảm dần
                khai_trien = expand(bieu_thuc)
                da_dung_str = format_latex(khai_trien)

                # 2. Tạo các phương án sai (B4: Điều chỉnh phương án sai)
                # Phương án sai 1: Thay tất cả dấu trừ thành dấu cộng
                da_sai_1 = format_latex(expand((x_sym + 1/x_sym)**n))

                # Phương án sai 2: Giữ nguyên hệ số nhưng sai dấu ở một vài vị trí hoặc nhân hệ số đầu với n
                khai_trien_sai_2 = n * x_sym**n + expand(bieu_thuc - x_sym**n)
                da_sai_2 = format_latex(khai_trien_sai_2)

                # Phương án sai 3: Đảo ngược dấu của toàn bộ khai triển
                da_sai_3 = format_latex(expand(-(x_sym - 1/x_sym)**n))

                # Câu hỏi
                noidungcauhoi = ('''Khai triển nhị thức $\\left(x - \\frac{1}{x}\\right)^{%s}$.'''
                                 %(latex(n)))

                # Các đáp án
                da_d = ('\\True $%s$' % (da_dung_str))
                da_s1 = '$%s$' % (da_sai_1)
                da_s2 = '$%s$' % (da_sai_2)
                da_s3 = '$%s$' % (da_sai_3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B2: Viết lại y hệt bài toán)
                buoc_khai_trien = []
                for k in range(n + 1):
                    ckn = binomial(n, k)
                    # Tạo chuỗi cho từng hạng tử: C_n^k * x^(n-k) * (-1/x)^k
                    term = 'C_{%s}^{%s} \\cdot x^{%s} \\cdot \\left(\\frac{-1}{x}\\right)^{%s}' % (latex(n), latex(k), latex(n-k), latex(k))
                    buoc_khai_trien.append(term)

                chuoi_buoc_giai = ' + '.join(buoc_khai_trien)

                loigiai = ('''Áp dụng công thức khai triển nhị thức Newton, ta có:\\\\
                             $\\left(x - \\frac{1}{x}\\right)^{%s} = %s$\\\\
                             $= %s$.'''
                           %(latex(n), chuoi_buoc_giai, da_dung_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

