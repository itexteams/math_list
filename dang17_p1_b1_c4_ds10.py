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


def bt_dang17_p1_b1_c4_ds10(self):
            #Khai báo biến
            # --- PHẦN KHỞI TẠO BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                x, m = symbols('x m')

                # B3: Suy nghĩ tìm cách random bài toán
                # Thiết lập thông số để bài toán có nghiệm đẹp m > m2
                while True:
                    a = randint(1, 5)
                    b = randint(-5, -1) # b âm để -bm/a cùng dấu với m
                    c = randint(-5, -1) # c âm để x <= ...
                    d = randint(1, 5)
                    e = randint(-10, 10)
                    k = randint(-5, 2)
                    l = k + randint(2, 5) # Đảm bảo đoạn [k, l] có độ dài ít nhất 2

                    # Tính các biên của m:
                    # 1. l <= (dm+e)/-c  => m >= (-cl - e)/d  (m0)
                    # 2. -bm/a < k       => m < ak/-b         (m1)
                    # 3. -bm/a > l       => m > al/-b         (m2)
                    m0 = Rational(-c * l - e, d)
                    m1 = Rational(a * k, -b)
                    m2 = Rational(a * l, -b)

                    # Điều kiện để bài toán có kết quả gọn: m > m2
                    if m2 >= m0 and m1 < m0:
                        break

                fx = a * x + b * m
                gx = c * x + d * m + e
                tx_val = randint(1, 5)
                tx_const = randint(-5, 5)
                tx = tx_val * x + tx_const
                dau = random.choice(['+', '-'])

                # Biểu thức x theo m để trình bày lời giải
                expr_x1 = simplify(-b * m / a)
                expr_x2 = simplify((d * m + e) / -c)

                # --- B2: VIẾT LẠI CÂU HỎI ---
                noidungcauhoi = (r'Xác định tham số $m$ để hàm số $y = \dfrac{%s}{%s} %s \sqrt{%s}$ '
                                 r'có tập xác định chứa đoạn $[%s; %s]$?' 
                                 % (latex(tx), latex(fx), dau, latex(gx), latex(k), latex(l)))

                # --- B4: ĐIỀU CHỈNH PHƯƠNG ÁN ---
                # Đáp án đúng
                da_dung = r'$m > %s$' % latex(m2)

                # Các đáp án nhiễu (Đảm bảo không trùng với đáp án đúng)
                s_list = [
                    r'$m \ge %s$' % latex(m0),
                    r'$m < %s$' % latex(m1),
                    r'$m > %s$' % latex(m1),
                    r'$m \le %s$' % latex(m2),
                    r'$m > %s$' % latex(m2 + 1)
                ]

                # Lọc bỏ các phương án nếu lỡ trùng với da_dung
                s_filtered = [ans for ans in s_list if ans != da_dung]
                wrong_answers = random.sample(s_filtered, 3)

                # Đưa các đáp án vào danh sách và xáo trộn
                da_d = '\\True ' + da_dung
                list_1 = [da_d, wrong_answers[0], wrong_answers[1], wrong_answers[2]]
                random.shuffle(list_1)

                # --- NỘI DUNG LỜI GIẢI ---
                loigiai = (r'Hàm số xác định khi và chỉ khi: '
                           r'$\begin{cases} %s \ne 0 \\ %s \ge 0 \end{cases} \Leftrightarrow \begin{cases} x \ne %s \\ x \le %s \end{cases}$.\\'
                           r'Để tập xác định chứa đoạn $[%s; %s]$ thì:\\'
                           r'$\begin{cases} %s \ge %s \\ \left[ \begin{aligned} & %s < %s \\ & %s > %s \end{aligned} \right. \end{cases} '
                           r'\Leftrightarrow \begin{cases} m \ge %s \\ \left[ \begin{aligned} & m < %s \\ & m > %s \end{aligned} \right. \end{cases} '
                           r'\Leftrightarrow m > %s$.'
                           % (latex(fx), latex(gx), latex(expr_x1), latex(expr_x2),
                              latex(k), latex(l),
                              latex(expr_x2), latex(l), latex(expr_x1), latex(k), latex(expr_x1), latex(l),
                              latex(m0), latex(m1), latex(m2), latex(m2)))

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

