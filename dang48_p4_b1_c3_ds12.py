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


def bt_dang48_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x = symbols('x')

                # Random hệ số của mẫu số Dx + E
                D_val = 1
                E_val = random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])

                # Random hệ số của tử số Ax^2 + Bx + C
                A_val = random.choice([2, 3, 4, 6, 8, -2, -4])
                B_val = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
                C_val = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

                den_expr = D_val * x + E_val
                num_expr = A_val * x**2 + B_val * x + C_val

                # Thực hiện phép chia đa thức tử số cho mẫu số
                q_expr, r_val = div(num_expr, den_expr, domain='QQ')

                # Đảm bảo phần dư r_val != 0
                while r_val == 0:
                    C_val += 1
                    num_expr = A_val * x**2 + B_val * x + C_val
                    q_expr, r_val = div(num_expr, den_expr, domain='QQ')

                y_expr = num_expr / den_expr
                y_tex = "\\frac{%s}{%s}" % (latex(num_expr), latex(den_expr))

                # Tách phân thức
                split_expr = q_expr + r_val / den_expr
                split_tex = latex(split_expr)

                # Tích phân thương và phần dư
                int_q = integrate(q_expr, x)
                int_r = Rational(r_val, D_val) * log(Abs(den_expr))
                F_correct_expr = int_q + int_r
                F_correct_tex = latex(F_correct_expr)

                # CÁC PHƯƠNG ÁN NHIỄU (SAI)
                # Sai 1: Quên chia cho D_val ở phần log (quên hệ số 1/a)
                int_r_w1 = r_val * log(Abs(den_expr))
                F_w1_expr = int_q + int_r_w1
                F_w1_tex = latex(F_w1_expr) + " + C"

                # Sai 2: Đổi dấu phần log
                F_w2_expr = int_q - int_r
                F_w2_tex = latex(F_w2_expr) + " + C"

                # Sai 3: Nhầm sang đạo hàm
                F_w3_expr = diff(y_expr, x)
                F_w3_tex = latex(F_w3_expr) + " + C"

                # Sai 4: Quên + C
                F_w4_tex = latex(F_correct_expr)

                # Đáp án đúng
                du = ['$%s + C$' % (F_correct_tex)]
                da = random.choice(du)

                # Danh sách phương án sai
                s_candidates = [
                    '$%s$' % (F_w1_tex),
                    '$%s$' % (F_w2_tex),
                    '$%s$' % (F_w3_tex),
                    '$%s$' % (F_w4_tex)
                ]

                # Lọc bỏ phương án trùng với đáp án đúng
                s = [ans for ans in s_candidates if ans != da and ans != '$%s + C$' % (F_correct_tex)]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Tìm nguyên hàm của hàm số $y = %s$.' % (y_tex))

                # Đánh dấu đáp án đúng / sai
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Ta có $y = %s = %s$. \\\\ '
                           'Họ tất cả các nguyên hàm của hàm số đã cho là: \\\\ '
                           '$\\int %s \\mathrm{d}x = \\int \\left( %s \\right) \\mathrm{d}x = %s + C$.' 
                           % (y_tex, split_tex, y_tex, split_tex, F_correct_tex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n').replace('\\log', '\\ln')
            return content 

