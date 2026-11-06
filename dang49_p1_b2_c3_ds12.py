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


def bt_dang49_p1_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            t = symbols('t')

            # Danh sách dạng (ở đây chỉ có 1 dạng theo yêu cầu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # v0: vận tốc ban đầu (m/s)
                v0 = random.randint(10, 20)
                # Hệ số của gia tốc a(t) = k1*t^2 + k2*t
                k1 = random.randint(1, 3)
                k2 = random.choice([2, 4, 6, 8])
                # T: Khoảng thời gian (giây)
                T_val = random.randint(3, 5)

                # Biểu thức gia tốc
                a_t = k1*t**2 + k2*t

                # Tìm vận tốc v(t) = nguyên hàm a(t) + C. Với v(0) = v0 => C = v0
                v_t = integrate(a_t, t) + v0

                # Quãng đường S = tích phân v(t) từ 0 đến T
                S_val = integrate(v_t, (t, 0, T_val))

                # Chuyển kết quả sang số thập phân và định dạng dấu phẩy theo mẫu
                # Nếu kết quả là phân số, tính toán để lấy độ chính xác 2 chữ số
                kq_float = float(S_val)
                kq_str = str(Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # --- B4: Điều chỉnh các phương án sai không trùng đáp án đúng ---
                da_dung = f"${kq_str}$"

                # Tạo các phương án nhiễu (cộng/trừ ngẫu nhiên)
                s = []
                while len(s) < 3:
                    sai_so = random.choice([5, 10, 15, 2.5, 7.25, -5, -10, -2.5])
                    nhieu_val = kq_float + sai_so
                    if nhieu_val > 0:
                        nhieu_str = str(Decimal(str(nhieu_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                        nhieu_latex = f"${nhieu_str}$"
                        if nhieu_latex != da_dung and nhieu_latex not in s:
                            s.append(nhieu_latex)

                # --- B2: Viết lại bài toán theo mẫu ---
                noidungcauhoi = (r'''Một chất điểm đang chuyển động với vận tốc $v_0 = %s$ m/s thì tăng tốc với gia tốc $a(t) = %s$ (m/s$^2$). Quãng đường (đơn vị: m) chất điểm đó đi được trong khoảng thời gian $%s$ giây kể từ lúc bắt đầu tăng vận tốc là'''
                                 %(latex(v0), latex(a_t), latex(T_val)))

                # Các đáp án
                da_d = ('\\True ' + da_dung)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Tìm v(t) và hằng số C
                v_nguyen_ham = integrate(a_t, t)
                loigiai = (r'''Ta có $a(t) = %s \Rightarrow v(t) = \int a(t) \text{d} t = %s + C$. \\
                             Mà $v(0) = %s \Rightarrow C = %s$. \\
                             Do đó $v(t) = %s$. \\
                             Vậy quãng đường đi được là $S = \int_{0}^{%s} \left( %s \right) \text{d}t = $%s m.'''
                           %(latex(a_t), latex(v_nguyen_ham), latex(v0), latex(v0), latex(v_t),
                             latex(T_val), latex(v_t), da_dung))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

