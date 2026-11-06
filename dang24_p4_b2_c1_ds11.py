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


def bt_dang24_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập tham số random bài toán
                # Biểu thức tổng quát: cos(goc - x) + cos(goc + x) - cos(x)
                # Trong đề bài gốc, goc = 120 độ -> cos(120) = -1/2, sin(120) = sqrt(3)/2
                # Ta có thể random góc đặc biệt này từ các giá trị: 60, 120, 150
                goc = random.choice([60, 120, 150])

                # Tính toán các giá trị lượng giác bằng SymPy
                val_cos = cos(goc * pi / 180)
                val_sin = sin(goc * pi / 180)

                # Định dạng hiển thị phân số sang tiếng Việt (thay thế dấu chấm bằng dấu phẩy)
                def format_fraction_vn(val):
                    str_val = latex(val)
                    return str_val.replace('.', ',')

                str_cos = format_fraction_vn(val_cos)
                str_sin = format_fraction_vn(val_sin)

                # Kết quả biến đổi rút gọn chính xác:
                # cos(goc - x) + cos(goc + x) - cos(x) = 2*cos(goc)*cos(x) - cos(x) = (2*cos(goc) - 1)*cos(x)
                he_so_kq = 2 * val_cos - 1

                if he_so_kq == 0:
                    da_dung_str = '0'
                elif he_so_kq == 1:
                    da_dung_str = '\\cos x'
                elif he_so_kq == -1:
                    da_dung_str = '-\\cos x'
                else:
                    da_dung_str = '%s\\cos x' % latex(he_so_kq)

                da = '$%s$' % da_dung_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Điều chỉnh các phương án sai (nhiễu) không trùng đáp án đúng
                s_set = set()
                nhiieu_list = [
                    '0',
                    '\\cos x',
                    '-\\cos x',
                    '-2\\cos x',
                    '\\sin x - \\cos x',
                    '2\\sin x',
                    '\\sin x + \\cos x'
                ]

                for item in nhiieu_list:
                    p_an = '$%s$' % item
                    if p_an != da:
                        s_set.add(p_an)

                list_sai = list(s_set)
                random.shuffle(list_sai)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Rút gọn biểu thức $\\cos (%s^\\circ - x) + \\cos (%s^\\circ + x) - \\cos x$.'''
                                 % (latex(goc), latex(goc)))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý dấu cho lời giải chi tiết
                # cos(goc - x) = cos(goc)cos(x) + sin(goc)sin(x)
                # cos(goc + x) = cos(goc)cos(x) - sin(goc)sin(x)
                sign_sin1 = '+' if val_sin >= 0 else '-'
                sign_cos2 = '+' if val_cos >= 0 else '-'
                sign_sin2 = '-' if val_sin >= 0 else '+'

                str_val_cos_abs = latex(abs(val_cos)).replace('.', ',')
                str_val_sin_abs = latex(abs(val_sin)).replace('.', ',')

                part1 = '%s\\frac{%s}{%s}\\cos x %s \\frac{\\sqrt{%s}}{%s}\\sin x' % (
                    '-' if val_cos < 0 else '', str_val_cos_abs if '/' not in str_cos else latex(abs(val_cos).p), latex(abs(val_cos).q) if '/' in str_cos else '1',
                    sign_sin1, latex(abs(val_sin)**2 if '/' not in str_sin else abs(val_sin).p**2), latex(abs(val_sin).q) if '/' in str_sin else '1'
                )
                # Rút gọn chuỗi hiển thị thủ công để khớp cấu trúc mẫu toán học đẹp mắt
                if goc == 120:
                    buoc_khai_trien_str = '-\\frac{1}{2}\\cos x + \\frac{\\sqrt{3}}{2}\\sin x - \\frac{1}{2}\\cos x - \\frac{\\sqrt{3}}{2}\\sin x - \\frac{1}{2}\\cos x' # Biểu thức mẫu phụ
                    buoc_khai_trien_str = '-\\frac{1}{2}\\cos x + \\frac{\\sqrt{3}}{2}\\sin x - \\frac{1}{2}\\cos x - \\frac{\\sqrt{3}}{2}\\sin x - \\cos x'
                elif goc == 60:
                    buoc_khai_trien_str = '\\frac{1}{2}\\cos x + \\frac{\\sqrt{3}}{2}\\sin x + \\frac{1}{2}\\cos x - \\frac{\\sqrt{3}}{2}\\sin x - \\cos x'
                else: # 150
                    buoc_khai_trien_str = '-\\frac{\\sqrt{3}}{2}\\cos x + \\frac{1}{2}\\sin x - \\frac{\\sqrt{3}}{2}\\cos x - \\frac{1}{2}\\sin x - \\cos x'

                # Lời giải chi tiết
                loigiai = ('''$\\cos (%s^\\circ - x) + \\cos (%s^\\circ + x) - \\cos x = %s = %s$.'''
                           % (latex(goc), latex(goc), buoc_khai_trien_str, da_dung_str))

            # Xuất câu trắc nghiệm định dạng minipage TeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

