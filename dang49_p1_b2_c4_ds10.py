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


def bt_dang49_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: KHỞI TẠO CÁC GIÁ TRỊ NGẪU NHIÊN ---
                # Parabol y = ax^2 + bx + c
                a = random.choice([1, 2, 3, -1, -2, -3])

                # Giả sử hoành độ đỉnh x_d là một số nguyên từ -5 đến 5 (khác 0)
                x_d = random.choice([i for i in range(-5, 6) if i != 0])

                # Tính b dựa trên công thức x_d = -b/(2a) => b = -2 * a * x_d
                b = -2 * a * x_d

                # Chọn một điểm N(x_n, y_n) mà Parabol đi qua
                # Để tránh trùng với đỉnh, ta chọn x_n khác x_d
                x_n = random.choice([i for i in range(-4, 5) if i != x_d])
                # Tính y_n để có điểm N cố định: y_n = a*x_n^2 + b*x_n + c_thuc
                # Nhưng đề bài cho N trước, nên ta random c_thuc trước để tính y_n
                c_thuc = random.randint(-15, 15)
                y_n = a * (x_n**2) + b * x_n + c_thuc

                # Đáp án đúng là phương trình Parabol
                # Định dạng chuỗi hiển thị: ax^2 + bx + c
                def format_poly(a, b, c):
                    res = f"{a}x^2" if a != 1 else "x^2"
                    if a == -1: res = "-x^2"

                    if b > 0: res += f" + {b}x"
                    elif b < 0: res += f" - {abs(b)}x"

                    if c > 0: res += f" + {c}"
                    elif c < 0: res += f" - {abs(c)}"
                    return res

                kq_str = f"y = {format_poly(a, b, c_thuc)}"

                # --- BƯỚC 2: TẠO CÁC PHƯƠNG ÁN SAI (KHÔNG TRÙNG ĐÁP ÁN ĐÚNG) ---
                du = [f"${kq_str}$"]
                da = du[0]

                s = set()
                while len(s) < 3:
                    # Tạo sai số bằng cách thay đổi hệ số c hoặc b
                    b_sai = b + random.choice([-2, 2, 4])
                    c_sai = c_thuc + random.choice([-5, -2, 2, 5, 10])
                    sai_str = f"$y = {format_poly(a, b_sai, c_sai)}$"
                    if sai_str != da:
                        s.add(sai_str)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # --- BƯỚC 3: NỘI DUNG CÂU HỎI ---
                noidungcauhoi = ('''Xác định parabol $y = %sx^2 + bx + c$, biết rằng parabol đó có hoành độ đỉnh $%s$ và đi qua điểm $N(%s;%s)$ ?'''
                                 %(latex(a), latex(x_d), latex(x_n), latex(y_n)))

                # --- BƯỚC 4: NỘI DUNG LỜI GIẢI (Bám sát mẫu ảnh) ---
                # Tính toán các bước trung gian cho lời giải
                # Bước b: -b/2a = x_d => b = -2*a*x_d
                # Bước c: a*x_n^2 + b*x_n + c = y_n => c = y_n - a*x_n^2 - b*x_n
                term_ax2 = a * (x_n**2)
                term_bx = b * x_n

                loigiai = ('''Vì $(P)$ có hoành độ đỉnh $%s$ nên $-\\frac{b}{2a} = %s \\Leftrightarrow b = -2 \\cdot %s \\cdot (%s) \\Leftrightarrow b = %s$. \\\\
                             Hơn nữa $(P)$ đi qua điểm $N(%s;%s)$ nên $%s + (%s) + c = %s \\Leftrightarrow %s + c = %s \\Leftrightarrow c = %s$. \\\\
                             Vậy $(P): %s$.'''
                           %(latex(x_d), latex(x_d), latex(a), latex(x_d), latex(b),
                             latex(x_n), latex(y_n), 
                             latex(term_ax2), latex(term_bx), latex(y_n),
                             latex(term_ax2 + term_bx), latex(y_n), latex(c_thuc),
                             kq_str))

                # --- BƯỚC 5: XUẤT KẾT QUẢ ---
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

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

