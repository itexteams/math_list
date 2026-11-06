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


def bt_dang23_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Để bài toán đẹp, ta chọn a âm để parabol y' có bề lõm hướng xuống -> có GTLN
                a = random.randint(-3, -1)
                b = random.randint(1, 5) * 3 # Chọn b chia hết cho 3 để đỉnh x_0 đẹp
                c = random.randint(1, 10)
                d = random.randint(-10, 10)

                f = a*x**3 + b*x**2 + c*x + d
                f_prime = diff(f, x)

                # Hệ số góc k = f'(x) = 3ax^2 + 2bx + c
                # Đạo hàm của k để tìm cực trị: k' = 6ax + 2b = 0 => x = -2b / 6a = -b / 3a
                x0 = Rational(- (2*b),(6*a))
                k_max = f_prime.subs(x, x0)

                # Chuyển đổi sang dạng số nguyên/phân số để hiển thị đẹp
                k_max_val = int(k_max) if k_max.is_integer else k_max

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % latex(k_max_val)

                s = []
                while len(s) < 3:
                    sai = k_max_val + random.choice([-3, -2, -1, 1, 2, 3, 5, 6])
                    if sai != k_max_val and sai not in s:
                        s.append(sai)

                das1 = '$%s$' % latex(s[0])
                das2 = '$%s$' % latex(s[1])
                das3 = '$%s$' % latex(s[2])

                # Câu hỏi
                noidungcauhoi = (r'Cho hàm số $y = %s$ có đồ thị $(C)$. Hệ số góc lớn nhất của tiếp tuyến với đồ thị $(C)$ là'
                                 % latex(f))

                # Các đáp án
                da_d = '\\True ' + str(da_dung)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết lại y hệt cấu trúc bài toán mẫu)
                # Xử lý hiển thị dấu cho đạo hàm
                f_prime_latex = latex(f_prime)

                loigiai = (r'Hàm số $y = %s$ có đồ thị $(C)$ có tập xác định $D = \mathbb{R}$.\\'
                           r'''Ta có hệ số góc của tiếp tuyến với đồ thị hàm số $(C)$ là $y' = %s$.\\'''
                           r'Vì đây là hàm số bậc hai có hệ số $a = %s < 0$ nên đạt giá trị lớn nhất tại đỉnh $x = \frac{-b}{2a} = %s$.\\'
                           r'''Vậy hệ số góc lớn nhất của tiếp tuyến với đồ thị hàm số là $y'\left(%s\right)=%s$.'''
                           % (latex(f), f_prime_latex, 3*a, latex(x0),latex(x0), latex(k_max_val)))

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

