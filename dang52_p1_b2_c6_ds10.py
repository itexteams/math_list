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


def bt_dang52_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Thay vì cơ số 3, ta có thể chọn ngẫu nhiên cơ số b trong khoảng [2, 5]
                b = random.choice([2, 3, 4, 5])

                # Số các số tự nhiên có 4 chữ số luôn là 9000 (từ 1000 đến 9999)
                tong_so = 9000

                # Tìm các giá trị N sao cho A = b^N nằm trong khoảng [1000, 9999]
                # 1000 <= b^N <= 9999  =>  log_b(1000) <= N <= log_b(9999)
                n_min = math.ceil(math.log(1000, b))
                n_max = math.floor(math.log(9999, b))

                # Danh sách các số nguyên N thỏa mãn
                list_N = list(range(n_min, n_max + 1))
                so_truong_hop = len(list_N)

                # Tính xác suất P = so_truong_hop / 9000
                tu = so_truong_hop
                mau = tong_so

                # Rút gọn phân số cho đáp án đúng
                phan_so_kq = Rational(tu, mau)
                da_dung = '$' + latex(phan_so_kq) + '$'

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s = []
                while len(s) < 3:
                    # Tạo mẫu số ngẫu nhiên quanh mẫu số đúng để làm nhiễu
                    mau_sai = random.choice([2500, 3000, 4500, 5000, 1500, 2250, 4000])
                    tu_sai = 1
                    ps_sai = Rational(tu_sai, mau_sai)
                    da_sai = '$' + latex(ps_sai) + '$'
                    if da_sai != da_dung and da_sai not in s:
                        s.append(da_sai)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Chọn ngẫu nhiên một số tự nhiên $A$ có $4$ chữ số. Gọi $N$ là số thỏa mãn $%s^N = A$. Xác suất để $N$ là một số tự nhiên bằng'''
                                 % (latex(b)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Viết lại lời giải chi tiết giống nội dung trong ảnh
                # Tạo chuỗi liệt kê các giá trị N: "7, 8" hoặc "5, 6"
                chuoi_n = ", ".join(map(str, list_N))

                loigiai = ('''Gọi số $A = \\overline{abcd}$, khi đó số $A$ có $9 \\cdot 10 \\cdot 10 \\cdot 10 = 9000$ cách chọn. \\\\
                             Xét phương trình $%s^N = A$, để $N$ là số tự nhiên thì $A = %s^n$ với $n$ là số tự nhiên. \\\\
                             Do $A$ là số tự nhiên có $4$ chữ số nên $1000 \\le %s^n \\le 9999$. \\\\
                             Ta có các trường hợp $n = %s$ (có %s trường hợp). \\\\
                             Xác suất để $N$ là số tự nhiên là $P = \\frac{%s}{9000} = %s$.'''
                           % (latex(b), latex(b), latex(b), chuoi_n, so_truong_hop, so_truong_hop, latex(phan_so_kq)))

            # Xuất câu trắc nghiệm theo mẫu content
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

