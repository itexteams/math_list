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


def bt_dang11_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Danh sách dạng (ở đây có 1 dạng bài tìm nguyên hàm f(x))
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                c = random.choice([-3, -2, -1, 2, 3])
                coeff_integral_e = random.randint(1, 5) * random.choice([-1, 1])
                b = coeff_integral_e * c # Đảm bảo b/c là số nguyên
                a = 2 * random.randint(1, 4)

                # Giá trị f(x0) = y0
                x0 = 0
                y0 = random.randint(-5, 5)

                # Biểu thức f'(x)
                f_prime = a*x + b*exp(c*x)

                # B2: Tính toán lời giải
                # Nguyên hàm F(x) = (a/2)x^2 + (b/c)e^(cx) + C
                F_indefinite = integrate(f_prime, x)
                # Tính hằng số C: F_indefinite.subs(x, 0) + C = y0
                C_val = y0 - F_indefinite.subs(x, x0)

                # Hàm số f(x) cuối cùng
                f_x = F_indefinite + C_val

                # Đáp án đúng
                kq_dung = '$f(x) = %s$' % latex(f_x)

                # B4: Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Sai hằng số C
                    C_sai = C_val + random.choice([-2, -1, 1, 2, 3])
                    # Hoặc sai dấu trong biểu thức
                    f_sai = F_indefinite + C_sai
                    f_sai_str = '$f(x) = %s$' % latex(f_sai)
                    if f_sai_str != kq_dung:
                        s.add(f_sai_str)

                list_sai = list(s)

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Tìm hàm số $f(x)$ biết rằng $f'(x) = %s$ và $f(%s) = %s$.'''
                                 % (latex(f_prime), latex(x0), latex(y0)))

                # Các đáp án
                da_d = '\\True ' + kq_dung
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('Ta có $f(x) = \\int f\'(x)\\text{d}x = \\int (%s) dx = %s + C$. \\\\'
                           'Theo giả thiết $f(%s) = %s$, suy ra: \\\\'
                           '$%s + C = %s \\Rightarrow C = %s$. \\\\'
                           'Vậy $f(x) = %s$.'
                           % (latex(f_prime), latex(F_indefinite), 
                              latex(x0), latex(y0),
                              latex(F_indefinite.subs(x, x0)), latex(y0), latex(C_val),
                              latex(f_x)))

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

