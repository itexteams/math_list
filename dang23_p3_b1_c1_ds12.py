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


def bt_dang23_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                while True:
                    # Cấu trúc hàm số y = c1*x^3 + c2*x^2 + c4
                    c1 = random.choice([-1, 1])
                    c2 = random.choice([-3, 3])
                    c4 = randint(-5, 5)

                    # Hệ số của biểu thức m*a^2 + n*b
                    m = random.choice([1, 2, 3])
                    n = random.choice([-2, -1, 1, 2])

                    # Tìm nghiệm đạo hàm
                    x2 = int(-2*c2 / (3*c1))
                    val0 = c4
                    val2 = c1*(x2**3) + c2*(x2**2) + c4

                    # Đạo hàm bậc 2 tại x = 0 là 2*c2
                    y_dp_0 = 2*c2
                    if y_dp_0 < 0: # x=0 là điểm cực đại
                        a = val0
                        b = val2
                        x_cd = 0
                        x_ct = x2
                    else: # x=0 là điểm cực tiểu
                        a = val2
                        b = val0
                        x_cd = x2
                        x_ct = 0

                    kq = m*(a**2) + n*b

                    if kq != 0:
                        break

                # Xây dựng chuỗi hàm số y
                y_str = ""
                if c1 == 1: y_str += "x^3"
                else: y_str += "-x^3"
                if c2 > 0: y_str += " + %sx^2" % (c2)
                else: y_str += " - %sx^2" % (-c2)
                if c4 > 0: y_str += " + %s" % (c4)
                elif c4 < 0: y_str += " - %s" % (-c4)

                # Xây dựng chuỗi đạo hàm y'
                y_prime_str = ""
                if c1 == 1: y_prime_str += "3x^2"
                else: y_prime_str += "-3x^2"
                if c2 > 0: y_prime_str += " + %sx" % (2*c2)
                else: y_prime_str += " - %sx" % (-2*c2)

                # Xây dựng chuỗi biểu thức tính toán
                if m == 1:
                    str_m = "a^2"
                else:
                    str_m = "%sa^2" % (m)

                if n == 1:
                    str_n = "+ b"
                elif n == -1:
                    str_n = "- b"
                elif n > 0:
                    str_n = "+ %sb" % (n)
                else:
                    str_n = "- %sb" % (-n)

                expr_str = "%s %s" % (str_m, str_n)

                # Chuỗi cho biểu thức thay số
                if m == 1:
                    sub_m = "(%s)^2" % (a)
                else:
                    sub_m = "%s \\cdot (%s)^2" % (m, a)

                if n == 1:
                    sub_n = "+ (%s)" % (b)
                elif n == -1:
                    sub_n = "- (%s)" % (b)
                elif n > 0:
                    sub_n = "+ %s \\cdot (%s)" % (n, b)
                else:
                    sub_n = "- %s \\cdot (%s)" % (-n, b)

                calc_str = "%s %s" % (sub_m, sub_n)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = du[0]

                s_set = []
                while len(s_set) < 3:
                    fake_ans = kq + random.choice([-8, -6, -4, -2, -1, 1, 2, 4, 6, 8])
                    if fake_ans != kq and fake_ans not in s_set:
                        s_set.append(fake_ans)

                das1 = '$%s$' % (s_set[0])
                das2 = '$%s$' % (s_set[1])
                das3 = '$%s$' % (s_set[2])

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = %s$. Gọi $a, b$ lần lượt là giá trị cực đại và giá trị cực tiểu của hàm số đó. Giá trị của $%s$ bằng bao nhiêu?''' % (y_str, expr_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $y' = %s$. \\\\
                             $y' = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned} \\right.$. \\\\
                             Suy ra hàm số đạt cực đại tại $x = %s$, giá trị cực đại $a = y(%s) = %s$; hàm số đạt cực tiểu tại $x = %s$, giá trị cực tiểu $b = y(%s) = %s$. \\\\
                             Khi đó, $%s = %s = %s$.'''
                           % (y_prime_str, y_prime_str, min(0, x2), max(0, x2), x_cd, x_cd, a, x_ct, x_ct, b, expr_str, calc_str, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content  

