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


def bt_dang69_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # --- PHẦN KHỞI TẠO BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1 & 3: Thiết lập các giá trị ngẫu nhiên và tính toán logic
                # d1: mx + ny + p = 0  => n1 = (m, n)
                # d2: x = x0 + at; y = y0 - (a+k)t => u2 = (a, -(a+k)) => n2 = (a+k, a)
                # Điều kiện vuông góc: n1.n2 = 0 <=> m(a+k) + n*a = 0 <=> a(m+n) = -mk

                while True:
                    m = randint(1, 6)
                    n = randint(-6, -1)
                    k = randint(1, 5)
                    p = randint(-10, 10)
                    x0 = randint(-5, 5)
                    y0 = randint(-5, 5)

                    # Đảm bảo m+n != 0 và kết quả a là số nguyên để bài toán "đẹp"
                    if (m + n) != 0 and (m * k) % (m + n) == 0:
                        a_val = - (m * k) // (m + n)
                        break

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                kq = a_val
                s = set()
                while len(s) < 3:
                    sai = random.choice([kq + 1, kq - 1, -kq, kq + 2, kq - 2, 0, 1])
                    if sai != kq:
                        s.add(sai)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                # Định dạng dấu cho p trong phương trình d1
                p_str = ('+ ' + str(p)) if p >= 0 else str(p)

                noidungcauhoi = ('''Với giá trị nào của $a$ thì hai đường thẳng $d_1: %sx %s y %s = 0$ và $d_2: \\begin{cases} x = %s + at \\\\ y = %s - (a + %s)t \\end{cases}$ vuông góc với nhau?'''
                                 % (latex(m), latex(n), p_str, latex(x0), latex(y0), latex(k)))

                # Các đáp án
                da_d = ('\\True $a = %s$' % (latex(kq)))
                da_s1 = ('$a = %s$' % (latex(das1)))
                da_s2 = ('$a = %s$' % (latex(das2)))
                da_s3 = ('$a = %s$' % (latex(das3)))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Đường thẳng $d_1$ có vectơ pháp tuyến $\\vec{n}_1 = (%s; %s)$.\\\\
                             Đường thẳng $d_2$ có vectơ chỉ phương $\\vec{u}_2 = (a; -(a + %s))$, suy ra $d_2$ có vectơ pháp tuyến $\\vec{n}_2 = (a + %s; a)$.\\\\
                             Để $d_1 \\perp d_2$ thì $\\vec{n}_1 \\cdot \\vec{n}_2 = 0$\\\\
                             $\\Leftrightarrow %s(a + %s) + (%s)a = 0$\\\\
                             $\\Leftrightarrow %sa + %s %s a = 0$\\\\
                             $\\Leftrightarrow %sa = %s \\Leftrightarrow a = %s$.'''
                           % (latex(m), latex(n), latex(k), latex(k), 
                              latex(m), latex(k), latex(n), 
                              latex(m), latex(m*k), (('+ ' + str(n)) if n >= 0 else str(n)),
                              latex(m+n), latex(-m*k), latex(kq)))

            # --- XUẤT CÂU TRẮC NGHIỆM ---
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

