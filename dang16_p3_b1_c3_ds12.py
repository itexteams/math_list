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


def bt_dang16_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # f(x) = a^x + b*x^(n-1)
                # F(x) = a^x/ln(a) + k*x^n + C
                a = random.randint(2, 5)        # Cơ số của hàm mũ
                n = random.randint(2, 4)        # Số mũ của x trong F(x)
                k = random.randint(1, 5)        # Hệ số của x^n trong F(x)
                b = n * k                       # Hệ số của x^(n-1) trong f(x) để chia hết

                x0 = 1 
                x1 = 2

                # Giả sử F(1) = a/ln(a) để C = -k (giống mẫu trong ảnh)
                # F(1) = a/ln(a) + k*(1)^n + C = a/ln(a) => C = -k
                C = -k

                # Tính F(x1) = F(2)
                # F(2) = a^2/ln(a) + k*(2^n) + C
                val_F2 = (a**2)/math.log(a) + k*(x1**n) + C

                # Làm tròn đến hàng phần mười (0.1)
                kq_decimal = Decimal(str(val_F2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % kq_str

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai_val = float(kq_decimal) + random.choice([-2.5, -1.2, 1.5, 2.3, 3.4, -3.1, 4.2])
                    sai_str = str(Decimal(str(sai_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if sai_str != kq_str:
                        s.add('$%s$' % sai_str)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi (B2: Viết lại y hệt bài toán theo mẫu)
                # f(x) = a^x + b*x^(n-1)
                f_x_latex = f"{a}^x + {b}x^{{{n-1}}}" if n-1 > 1 else f"{a}^x + {b}x"
                F_1_latex = f"\\frac{{{a}}}{{\\ln {a}}}"

                noidungcauhoi = ('''Biết hàm số $F(x)$ là một nguyên hàm của hàm số $f(x) = %s$ và $F(1) = %s$. Giá trị của $F(2)$ (làm tròn đến hàng phần mười) bằng?'''
                                 % (f_x_latex, F_1_latex))

                # Nội dung lời giải
                loigiai = ('''Ta có $\\int f(x) \\text{d} x = \\int (%s) \\text{d} x = \\frac{%s^x}{\\ln %s} + %sx^{%s} + C$. \\\\
                             Suy ra $F(x) = \\frac{%s^x}{\\ln %s} + %sx^{%s} + C$. \\\\
                             Theo giả thiết: $F(1) = \\frac{%s}{\\ln %s} + %s \\cdot 1^{%s} + C = \\frac{%s}{\\ln %s} \\Rightarrow C = %s$. \\\\
                             Do đó $F(2) = \\frac{%s^2}{\\ln %s} + %s \\cdot 2^{%s} + (%s) \\approx %s$.'''
                           % (f_x_latex, a, a, k, n,
                              a, a, k, n,
                              a, a, k, n, a, a, C,
                              a, a, k, n, C, kq_str))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                da_d = '\\True ' + str(da)
                list_ans = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

