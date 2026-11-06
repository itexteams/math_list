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


def bt_dang18_p4_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 3: RANDOM BÀI TOÁN ---
                # Random hệ số k cho mẫu số (ví dụ: 1n^2, 2n^2, 3n^2...)
                # Nếu k=1 thì quay về đúng bài toán gốc trong ảnh
                k = randint(1, 6) 

                # Biến n dùng cho biểu thức symbolic (nếu cần tính toán tự động bằng sympy)
                n = symbols('n')

                # Xây dựng chuỗi hiển thị cho mẫu số
                if k == 1:
                    mau_so_str = "n^2"
                    mau_so_giai = "2n^2" # Khi thay tổng n(n+1)/2 thì mẫu thành 2*1*n^2
                    he_so_cuoi = "2"
                else:
                    mau_so_str = f"{k}n^2"
                    mau_so_giai = f"{2*k}n^2" # Khi thay tổng n(n+1)/2 thì mẫu thành 2*k*n^2
                    he_so_cuoi = f"{2*k}"

                # Tính kết quả chính xác
                # Lim = 1/(2k)
                kq_fraction = Rational(1, 2 * k)
                kq = latex(kq_fraction)
                h1=1/(2*k)
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq1=str(kqz).replace('.', ',')

                # --- TẠO CÁC ĐÁP ÁN TRẮC NGHIỆM ---
                # Đáp án đúng
                du = ['$%s$' % kq]
                da = random.choice(du)

                # Tạo đáp án nhiễu (Distractors)
                # Nhiễu 1: 1/k (quên chia 2)
                s1 = latex(Rational(1, k))
                # Nhiễu 2: 1/(2k+2) (lệch mẫu)
                s2 = latex(Rational(1, 2*k + 2))
                # Nhiễu 3: 0 hoặc 1 hoặc 1/(k+1) tùy chọn
                s3 = "0" if k > 1 else latex(Rational(1, 3)) # Tránh trùng nếu k=1

                s = [
                    '$%s$' % s1,
                    '$%s$' % s2,
                    '$%s$' % s3,
                    '$1$',
                    '$+\\infty$'
                ]

                # Chọn 3 đáp án sai ngẫu nhiên từ danh sách s
                list_sai = random.sample(s, 3)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # --- NỘI DUNG CÂU HỎI (B2) ---
                noidungcauhoi = ('''Tính $\\lim_{n \\to +\\infty} \\left( \\frac{1}{%s} + \\frac{2}{%s} + \\frac{3}{%s} + ... + \\frac{n}{%s} \\right)$.''' % (mau_so_str, mau_so_str, mau_so_str, mau_so_str))

                # Các đáp án để hiển thị
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- NỘI DUNG LỜI GIẢI (B2) ---
                # Tái hiện lại từng bước giải như trong ảnh
                loigiai = ('''$\\lim_{n \\to +\\infty} \\left( \\frac{1}{%s} + \\frac{2}{%s} + \\frac{3}{%s} + ... + \\frac{n}{%s} \\right)$ \\\\
                $= \\lim_{n \\to +\\infty} \\left( \\frac{1+2+3+...+n}{%s} \\right)$ \\\\
                $= \\lim_{n \\to +\\infty} \\left( \\frac{n(n+1)}{%s} \\right)$ \\\\
                $= \\lim_{n \\to +\\infty} \\left( \\frac{1}{%s} + \\frac{1}{%sn} \\right) = %s$.'''
                % (
                    mau_so_str, mau_so_str, mau_so_str, mau_so_str, # Dòng 1
                    mau_so_str, # Dòng 2
                    mau_so_giai, # Dòng 3 (đã nhân 2 vào mẫu)
                    he_so_cuoi, he_so_cuoi, kq # Dòng 4: tách 1/2k + 1/2kn
                ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

