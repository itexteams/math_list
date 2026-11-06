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


def bt_dang22_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số và tọa độ điểm cực trị
                # Hàm số: y = c*x^3 + d*x^2 + a*x + b

                while True:
                    c = randint(1, 3)
                    d = randint(-3, 3)
                    xA = randint(-2, 3)
                    yA = randint(-5, 5)
                    if c != 0 and d != 0 and xA != 0:
                        break

                # Giải hệ phương trình tìm a, b
                # y' = 3cx^2 + 2dx + a
                # Điểm cực trị A(xA, yA) => y'(xA) = 0 và y(xA) = yA

                a, b = symbols('a b')
                eq1 = Eq(3*c*xA**2 + 2*d*xA + a, 0)
                eq2 = Eq(c*xA**3 + d*xA**2 + a*xA + b, yA)

                sol = solve((eq1, eq2), (a, b))
                a_val = sol[a]
                b_val = sol[b]

                # Biểu thức tính: k*a + m*b
                k=random.choice([2,3,4,5,6,7,8,9])   
                m=random.choice([2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]) 
                kq = k*a_val + m*b_val

                # Hàm số ban đầu
                if c == 1:
                    str_c = "x^3"
                elif c == -1:
                    str_c = "-x^3"
                else:
                    str_c = f"{c}x^3"

                if d == 1:
                    str_d = "+ x^2"
                elif d == -1:
                    str_d = "- x^2"
                elif d > 0:
                    str_d = f"+ {d}x^2"
                else:
                    str_d = f"- {abs(d)}x^2"

                ham_so = f"y = {str_c} {str_d} + ax + b"

                # Tính các giá trị cho biểu thức tính toán
                y_phay_xA = 3*c*xA**2 + 2*d*xA
                y_xA_part = c*xA**3 + d*xA**2

                # Các đáp án trắc nghiệm
                da = '$%s$' % (latex(kq))

                # Tạo các phương án sai
                s_set = []
                for i in range(-5, 6):
                    if i != 0:
                        wrong_val = kq + i
                        if wrong_val not in s_set:
                            s_set.append(wrong_val)

                random.shuffle(s_set)
                s = s_set[:3]

                das1 = '$%s$' % (latex(s[0]))
                das2 = '$%s$' % (latex(s[1]))
                das3 = '$%s$' % (latex(s[2]))

                # Biểu thức yêu cầu tính
                if m == 1:
                    bieu_thuc = f"{k}a + b"
                elif m == -1:
                    bieu_thuc = f"{k}a - b"
                elif m > 0:
                    bieu_thuc = f"{k}a + {m}b"
                else:
                    bieu_thuc = f"{k}a - {abs(m)}b"

                # Câu hỏi
                noidungcauhoi = ('''Biết đồ thị hàm số $%s$ có điểm cực trị là $A(%s; %s)$. Khi đó giá trị của $%s$ bằng bao nhiêu?'''
                                 % (ham_so, latex(xA), latex(yA), bieu_thuc))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $y' = %s + %s + a$. \\\\
                             Đồ thị hàm số có điểm cực trị là $A(%s; %s)$ nên ta có hệ phương trình: \\\\
                             $\\begin{cases} y'(%s) = 0 \\\\ y(%s) = %s \\end{cases} \\Leftrightarrow \\begin{cases} %s + a = 0 \\\\ %s + %s \\cdot a + b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$. \\\\
                             Khi đó, giá trị của $%s$ là: $%s \\cdot (%s) + %s \\cdot (%s) = %s$.'''
                           % (latex(3*c*x**2), latex(2*d*x),
                              latex(xA), latex(yA),
                              latex(xA), latex(xA), latex(yA),
                              latex(y_phay_xA), latex(y_xA_part), latex(xA), latex(yA),
                              latex(a_val), latex(b_val),
                              bieu_thuc, k, latex(a_val), m, latex(b_val), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content  

