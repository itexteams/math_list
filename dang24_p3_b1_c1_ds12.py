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


def bt_dang24_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số của hàm số bậc 4 trùng phương: y = ax^4 + bx^2 + c
                a = random.choice([1, 2, 3, 4, -1, -2, -3, -4])

                # Để hàm số có 3 điểm cực trị thì a và b trái dấu
                if a > 0:
                    b = -randint(1, 10)
                else:
                    b = randint(1, 10)

                c = randint(-10, 10)

                # Hàm số ban đầu
                y_str = ""
                if a == 1: y_str += "x^4"
                elif a == -1: y_str += "-x^4"
                else: y_str += f"{a}x^4"

                if b > 0: y_str += f" + {b}x^2"
                elif b < 0: y_str += f" - {abs(b)}x^2"

                if c > 0: y_str += f" + {c}"
                elif c < 0: y_str += f" - {abs(c)}"

                # Đạo hàm y' = 4ax^3 + 2bx
                y_prime_str = ""
                if 4*a == 1: y_prime_str += "x^3"
                elif 4*a == -1: y_prime_str += "-x^3"
                else: y_prime_str += f"{4*a}x^3"

                if 2*b > 0: y_prime_str += f" + {2*b}x"
                elif 2*b < 0: y_prime_str += f" - {abs(2*b)}x"

                # Nghiệm của đạo hàm
                # 4ax^3 + 2bx = 0 <=> x(4ax^2 + 2b) = 0
                # Nghiệm: x1 = 0, x2, x3 = +- sqrt(-b/2a)

                # Do hàm bậc 4 trùng phương có 3 cực trị, một trong các cực trị luôn bằng 0.
                # Vậy tích x1*x2*x3 luôn bằng 0.
                kq = 0

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = du[0]

                # Tạo các phương án sai
                s_set = []
                fake_options = [abs(b), abs(c), abs(a), -b, -c, 1, -1, 3, 5]
                for opt in fake_options:
                    if opt != kq and opt not in s_set:
                        s_set.append(opt)

                random.shuffle(s_set)
                s = s_set[:3]

                das1 = '$%s$' % (s[0])
                das2 = '$%s$' % (s[1])
                das3 = '$%s$' % (s[2])

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = %s$ đạt cực trị tại $x_1, x_2, x_3$. Khi đó, giá trị của tích $x_1x_2x_3$ bằng bao nhiêu?''' % (y_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # x(4ax^2 + 2b) = 0
                term1 = f"{4*a}x^2"
                if 2*b > 0:
                    term1 += f" + {2*b}"
                else:
                    term1 += f" - {abs(2*b)}"

                frac_val = Rational(-b, 2*a)
                frac_str = latex(frac_val)

                loigiai = ('''Ta có $y' = %s$. \\\\
                             $y' = 0 \\Leftrightarrow x \\cdot (%s) = 0 \\Leftrightarrow \\left[ \\begin{aligned} & x = 0 \\\\ & x^2 = %s \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & x_1 = 0 \\\\ & x_2 = \\sqrt{%s} \\\\ & x_3 = -\\sqrt{%s} \\end{aligned} \\right.$. \\\\
                             Khi đó, giá trị của tích $x_1x_2x_3 = 0 \\cdot \\sqrt{%s} \\cdot \\left(-\\sqrt{%s}\\right) = 0$.'''
                           % (y_prime_str, term1, frac_str, frac_str, frac_str, frac_str, frac_str))
                dapan='\\shortans[0]{$%s$}\n'%(latex(0))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content  

