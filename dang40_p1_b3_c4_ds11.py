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


def bt_dang40_p1_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # --- BƯỚC 1: RANDOM BÀI TOÁN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo các hệ số sao cho f(0)>0, f(1)<0, f(2)>0
                # f(0) = d. Cho d dương.
                d = randint(1, 3)
                # Cho a dương để khi x tiến tới vô cùng f(x) dương
                a = randint(1, 3)
                # c ngẫu nhiên nhỏ
                c = randint(-2, 2)

                # Điều kiện f(1) = a + b + c + d < 0 => b < -(a + c + d)
                b = -(a + abs(c) + d + randint(2, 5))

                # Định nghĩa hàm số
                f_expr = a*x**4 + b*x**2 + c*x + d

                # Tính giá trị tại các điểm
                f0 = f_expr.subs(x, 0)
                f1 = f_expr.subs(x, 1)
                f2 = f_expr.subs(x, 2)

                # Đảm bảo điều kiện bài toán (nếu f2 chưa dương thì tăng a)
                while f2 <= 0:
                    a += 1
                    f_expr = a*x**4 + b*x**2 + c*x + d
                    f2 = f_expr.subs(x, 2)

                # --- BƯỚC 2: CÁC ĐÁP ÁN TRẮC NGHIỆM ---
                # Đáp án đúng
                da_dung = "Phương trình có ít nhất hai nghiệm trên khoảng $(0; 2)$"

                # Các đáp án nhiễu
                s = [
                    "Phương trình vô nghiệm trên khoảng $(0; 2)$ ",
                    "Phương trình có đúng một nghiệm trên khoảng $(0; 2)$ ",
                    "Phương trình có ít nhất ba nghiệm trên khoảng $(0; 2)$ ",
                    "Phương trình chỉ có nghiệm dương lớn hơn $2$",
                    "Hàm số không cắt trục hoành trên khoảng $(0; 2)$ "
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- BƯỚC 3: NỘI DUNG CÂU HỎI ---
                # Chuyển biểu thức sang latex
                f_latex = latex(f_expr).replace('**', '^')

                noidungcauhoi = (r"Cho phương trình $%s = 0$. Chọn khẳng định \textbf{đúng} trong các khẳng định sau:" % f_latex)

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- BƯỚC 4: NỘI DUNG LỜI GIẢI ---
                loigiai = (r"""Xét hàm số $f(x) = %s$. Hàm số liên tục trên $\mathbb{R}$. \\
                            Ta có: $\begin{cases} f(0) = %s \\ f(1) = %s \\ f(2) = %s \end{cases}$. \\
                            Vì $f(0) \cdot f(1) = %s \cdot (%s) < 0$ nên phương trình có ít nhất một nghiệm thuộc $(0; 1)$. \\
                            Vì $f(1) \cdot f(2) = (%s) \cdot %s < 0$ nên phương trình có ít nhất một nghiệm thuộc $(1; 2)$. \\
                            Vậy phương trình có ít nhất hai nghiệm trên khoảng $(0; 2)$.""" 
                           % (f_latex, latex(f0), latex(f1), latex(f2), 
                              latex(f0), latex(f1), latex(f1), latex(f2)))

            # --- BƯỚC 5: XUẤT NỘI DUNG ---
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

