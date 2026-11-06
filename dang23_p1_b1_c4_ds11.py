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


def bt_dang23_p1_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: SUY NGHĨ CÁCH RANDOM ---
                # Cấu trúc un = a / (n + b) và vn = c / (n + d)
                # Trong bài mẫu: a=1, b=1, c=3, d=3

                # Random tử số (a, c) và hằng số mẫu (b, d)
                a = randint(1, 5)      # Tử số của un (thường nhỏ)
                b = randint(1, 9)      # Số cộng thêm ở mẫu un
                c = randint(2, 9)      # Tử số của vn (để khác 1 cho bài toán hay hơn)
                while c == a:          # Tránh trường hợp a = c thì kết quả là 1
                    c = randint(2, 9)
                d = randint(1, 9)      # Số cộng thêm ở mẫu vn

                # Tính kết quả đúng (Limit = a/c)
                kq_val = Rational(a, c)
                kq = latex(kq_val)

                # --- TẠO CÁC ĐÁP ÁN TRẮC NGHIỆM ---
                # Đáp án đúng
                da_dung = '$%s$' % kq

                # Tạo đáp án nhiễu
                # Nhiễu 1: Nghịch đảo kết quả (c/a)
                s1_val = Rational(c, a)

                # Nhiễu 2: Chỉ lấy hệ số a hoặc c
                s2_val = a 

                # Nhiễu 3: Một phân số ngẫu nhiên khác hoặc phép tính sai
                s3_val = Rational(a + 1, c)

                # Danh sách nhiễu
                s = [
                    '$%s$' % latex(s1_val),
                    '$%s$' % latex(s2_val),
                    '$%s$' % latex(s3_val),
                    '$%s$' % latex(Rational(1, c)), # Trường hợp sai phổ biến quên a
                    '$0$',
                    '$+\\infty$'
                ]

                # Lọc trùng lặp giữa nhiễu và đáp án đúng
                s = [x for x in s if x != da_dung]

                # Chọn ngẫu nhiên 3 đáp án nhiễu
                random.shuffle(s)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # --- B2: VIẾT LẠI ĐỀ BÀI VÀ LỜI GIẢI ---

                # Xử lý hiển thị LaTeX cho đẹp (ẩn số 1 ở tử số nếu cần, nhưng bài mẫu viết số 1 nên ta giữ nguyên hoặc tùy chỉnh)
                # un = a / (n+b)
                un_str = "\\frac{%s}{n+%s}" % (a, b)
                # vn = c / (n+d)
                vn_str = "\\frac{%s}{n+%s}" % (c, d)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hai dãy số $(u_n)$ và $(v_n)$ có $u_n = %s ; v_n = %s$. Tính $\\lim_{n\\to+\\infty} \\frac{u_n}{v_n}$.'''
                                 % (un_str, vn_str))

                # Đưa các đáp án vào danh sách
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- XỬ LÝ LỜI GIẢI CHI TIẾT ---
                # Bước 1: Thay thế
                step1 = "\\lim_{n\\to+\\infty} \\frac{%s}{%s}" % (un_str, vn_str)

                # Bước 2: Nhân nghịch đảo: a(n+d) / c(n+b)
                # Xử lý hiển thị nếu a=1 hoặc c=1 thì không viết số 1 trước ngoặc
                tu_step2 = "n+%s" % d if a == 1 else "%s(n+%s)" % (a, d)
                mau_step2 = "n+%s" % b if c == 1 else "%s(n+%s)" % (c, b)
                step2 = "\\lim_{n\\to+\\infty} \\frac{%s}{%s}" % (tu_step2, mau_step2)

                # Bước 3: Chia cho n (Đặt nhân tử chung)
                # Tử: a(1 + d/n)
                phan_con_lai_tu = "1+\\frac{%s}{n}" % d
                tu_step3 = phan_con_lai_tu if a == 1 else "%s\\left(%s\\right)" % (a, phan_con_lai_tu)

                # Mẫu: c(1 + b/n)
                phan_con_lai_mau = "1+\\frac{%s}{n}" % b
                mau_step3 = phan_con_lai_mau if c == 1 else "%s\\left(%s\\right)" % (c, phan_con_lai_mau)

                step3 = "\\lim_{n\\to+\\infty} \\frac{%s}{%s}" % (tu_step3, mau_step3)

                # Nội dung lời giải
                loigiai = ('''Ta có $I = \\lim_{n\\to+\\infty} \\frac{u_n}{v_n} = %s = %s = %s = %s$.'''
                           % (step1, step2, step3, kq))

                # Xuất câu trắc nghiệm
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

