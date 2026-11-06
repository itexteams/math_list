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


def bt_dang17_p3_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random giá trị góc beta và giá trị lượng giác vế phải (đảm bảo ra góc đẹp)
                # Bộ dữ liệu: (chuỗi góc vế phải gốc, giá trị độ tương ứng phi, góc beta của đề bài)
                list_data = [
                    ('\\frac{\\sqrt{3}}{2}', 60, 40),
                    ('\\frac{1}{2}', 30, 20),
                    ('\\frac{\\sqrt{2}}{2}', 45, 30),
                    ('-\\frac{1}{2}', -30, 10),
                    ('-\\frac{\\sqrt{3}}{2}', -60, 20)
                ]

                val_str, phi, beta = random.choice(list_data)

                # Biến đổi: sin(2x - beta) = sin(phi)
                # Họ 1: 2x - beta = phi + k360 <=> 2x = phi + beta + k360 <=> x = (phi + beta)/2 + k180
                # Họ 2: 2x - beta = 180 - phi + k360 <=> 2x = 180 - phi + beta + k360 <=> x = (180 - phi + beta)/2 + k180

                phi1 = phi + beta
                phi2 = 180 - phi + beta

                x1_base = Rational(phi1, 2)
                x2_base = Rational(phi2, 2)

                # Chặn nghiệm trên đoạn [-180; 180] cho họ 1
                k1_min_frac = Rational(-180 - x1_base, 180)
                k1_max_frac = Rational(180 - x1_base, 180)

                list_k1 = []
                for k in range(-5, 6):
                    if k1_min_frac <= k <= k1_max_frac:
                        list_k1.append(k)

                # Chặn nghiệm trên đoạn [-180; 180] cho họ 2
                k2_min_frac = Rational(-180 - x2_base, 180)
                k2_max_frac = Rational(180 - x2_base, 180)

                list_k2 = []
                for k in range(-5, 6):
                    if k2_min_frac <= k <= k2_max_frac:
                        list_k2.append(k)

                # Tổng số nghiệm phân biệt
                total_solutions = len(list_k1) + len(list_k2)
                kq = str(total_solutions)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai không trùng đáp án đúng
                s = []
                for val_s in [2, 4, 6, 7, 3, 5]:
                    if str(val_s) != kq:
                        s.append('$%s$' % val_s)

                s = list(set(s))
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Số nghiệm của phương trình $\\sin \\left( 2x-%s^\\circ \\right)=%s$ với $-180^\\circ \\le x \\le 180^\\circ$ là bao nhiêu?'''
                                 %(latex(beta), val_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuỗi hệ ngoặc vuông liệt kê nghiệm cho họ 1
                str_he_k1 = '\\left[ \\begin{aligned} '
                for k in sorted(list_k1):
                    x_val = x1_base + k*180
                    str_he_k1 += '& k = %s \\Rightarrow x = %s^\\circ \\\\ ' % (latex(k), latex(x_val))
                str_he_k1 += '\\end{aligned} \\right.'

                # Chuỗi hệ ngoặc vuông liệt kê nghiệm cho họ 2
                str_he_k2 = '\\left[ \\begin{aligned} '
                for k in sorted(list_k2):
                    x_val = x2_base + k*180
                    str_he_k2 += '& k = %s \\Rightarrow x = %s^\\circ \\\\ ' % (latex(k), latex(x_val))
                str_he_k2 += '\\end{aligned} \\right.'

                # Lời giải chi tiết bám sát từng bước như ảnh gốc
                loigiai = ('''Ta có: \\\\
                           $\\sin \\left( 2x-%s^\\circ \\right)=%s \\Leftrightarrow \\sin \\left( 2x-%s^\\circ \\right)=\\sin %s^\\circ$ \\\\
                           $\\Leftrightarrow \\left[ \\begin{aligned} & 2x-%s^\\circ=%s^\\circ+k360^\\circ \\\\ & 2x-%s^\\circ=180^\\circ-%s^\\circ+k360^\\circ \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & 2x=%s^\\circ+k360^\\circ \\\\ & 2x=%s^\\circ+k360^\\circ \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & x=%s^\\circ+k180^\\circ \\\\ & x=%s^\\circ+k180^\\circ \\end{aligned} \\right.$ \\\\
                           - Xét nghiệm $x=%s^\\circ+k180^\\circ$. \\\\
                           Ta có: $-180^\\circ \\le x \\le 180^\\circ \\Leftrightarrow -180^\\circ \\le %s^\\circ+k180^\\circ \\le 180^\\circ \\Leftrightarrow %s \\le k \\le %s$. \\\\
                           Vì $k \\in \\mathbb{Z}$ nên $%s$. \\\\
                           - Xét nghiệm $x=%s^\\circ+k180^\\circ$. \\\\
                           Ta có: $-180^\\circ \\le x \\le 180^\\circ \\Leftrightarrow -180^\\circ \\le %s^\\circ+k180^\\circ \\le 180^\\circ \\Leftrightarrow %s \\le k \\le %s$. \\\\
                           Vì $k \\in \\mathbb{Z}$ nên $%s$. \\\\
                           Vậy có tất cả $%s$ nghiệm thỏa mãn bài toán.'''
                           %(latex(beta), val_str, latex(beta), latex(phi),
                              latex(beta), latex(phi), latex(beta), latex(phi), latex(phi1), latex(phi2), latex(x1_base), latex(x2_base),
                              latex(x1_base), latex(x1_base), latex(k1_min_frac), latex(k1_max_frac), str_he_k1,
                              latex(x2_base), latex(x2_base), latex(k2_min_frac), latex(k2_max_frac), str_he_k2,
                              latex(total_solutions)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(total_solutions))                                                                                                                                                                                                                                                                                                                                                 
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

