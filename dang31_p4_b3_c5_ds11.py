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


def bt_dang31_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến loại bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # r: lãi suất (%) từ 5% đến 9%
                r_val = random.randint(5, 9)
                # n: số năm gửi từ 2 đến 5 năm
                n_val = random.randint(2, 5)
                # price: giá trị chiếc xe (triệu đồng) từ 30 đến 100
                price_val = random.randint(30, 100)

                # --- Tính toán ---
                r_decimal = r_val / 100
                # Tính số tiền x cần thiết: x * ((1 + r)^n - 1) = price
                # => x = price / ((1 + r)^n - 1)
                mau_so = (1 + r_decimal)**n_val - 1
                x_raw = price_val / mau_so

                # Vì x là số tự nhiên tối thiểu để ĐỦ mua xe, ta lấy trần (ceil) của x_raw
                x_ans = math.ceil(x_raw)

                # --- B4: Điều chỉnh các phương án sai ---
                # Tạo danh sách các số nguyên xung quanh x_ans
                s_options = []
                offsets = [-10, -5, -2, -1, 1, 2, 5, 10, 15]
                for offset in offsets:
                    wrong_val = x_ans + offset
                    if wrong_val > 0 and wrong_val != x_ans:
                        s_options.append(f'${wrong_val}$')

                random.shuffle(s_options)
                das1 = s_options[0]
                das2 = s_options[1]
                das3 = s_options[2]

                # Đáp án đúng
                da = f'${x_ans}$'

                # --- B2: Viết lại bài toán theo mẫu code ---
                # Câu hỏi
                noidungcauhoi = ('''Ông An dự định gửi vào ngân hàng một số tiền với lãi suất không đổi là $%s\\%%$ một năm. Biết rằng cứ sau mỗi năm số tiền lãi sẽ được nhập vào vốn ban đầu để tính lãi cho năm kế tiếp. Tính số tiền tối thiểu $x$ (triệu đồng, $x \\in \\mathbb{N}$) ông An gửi vào ngân hàng để sau $%s$ năm số tiền lãi đủ mua một chiếc xe gắn máy giá trị $%s$ triệu đồng.'''
                                 % (latex(r_val), latex(n_val), latex(price_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách và trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Áp dụng công thức $P = P_0(1+r)^n$. \\\\
                             Số tiền ông An có được sau $%s$ năm là: $P = x(1 + %s)^{%s}$. \\\\
                             Tiền lãi ông An có được sau $%s$ năm là: $P - x = x(1 + %s)^{%s} - x = x\\left((1 + %s)^{%s} - 1\\right)$. \\\\
                             Số tiền lãi trên ít nhất là $%s$ triệu đồng nên: \\\\
                             $x\\left((1 + %s)^{%s} - 1\\right) \\ge %s \\Leftrightarrow x \\ge \\frac{%s}{(1 + %s)^{%s} - 1} \\approx %s$. \\\\
                             Vì $x \\in \\mathbb{N}$ nên số tiền tối thiểu là $x = %s$ triệu đồng.'''
                           % (latex(n_val), latex(r_decimal), latex(n_val),
                              latex(n_val), latex(r_decimal), latex(n_val), latex(r_decimal), latex(n_val),
                              latex(price_val),
                              latex(r_decimal), latex(n_val), latex(price_val), latex(price_val), latex(r_decimal), latex(n_val), 
                              latex(round(x_raw, 2)), latex(x_ans)))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

