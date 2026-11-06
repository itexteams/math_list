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


def bt_dang55_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random bài toán
                # Để đảm bảo bài toán có nghiệm đẹp, ta chọn hoành độ đỉnh x_v là số nguyên
                # Vì M(0, c) và N(x_n, c) có cùng tung độ, đỉnh sẽ nằm ở trung điểm: x_v = x_n / 2
                # Ta chọn x_v nguyên dương, suy ra x_n = 2 * x_v
                xv = randint(1, 4)
                xn = 2 * xv

                # Tung độ c của M và N (c > 0 để parabol hướng lên hoặc c < 0)
                c_val = randint(1, 5) * random.choice([-1, 1])

                # Từ giả thiết đỉnh nằm trên trục hoành (y_v = 0) và đi qua M(0, c_val)
                # Ta có hệ: y = a(x - xv)^2. Tại x=0, y=c_val => a*xv^2 = c_val => a = c_val / xv^2
                a_val = Rational(c_val, xv**2)
                b_val = -2 * a_val * xv

                # Tính toán các giá trị để trình bày lời giải
                delta = b_val**2 - 4*a_val*c_val # Delta luôn bằng 0 do đỉnh thuộc Ox

                # Đáp án đúng
                kq_str = "y = "
                if a_val == 1: kq_str += "x^2"
                elif a_val == -1: kq_str += "-x^2"
                else: kq_str += latex(a_val) + "x^2"

                if b_val > 0: kq_str += " + " + (latex(b_val) if b_val != 1 else "") + "x"
                elif b_val < 0: kq_str += " - " + (latex(abs(b_val)) if b_val != -1 else "") + "x"

                if c_val > 0: kq_str += " + " + str(c_val)
                elif c_val < 0: kq_str += " - " + str(abs(c_val))

                da = "$%s$" % kq_str

                # Bước 4: Tạo phương án sai (không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    a_sai = a_val + randint(1, 2) * random.choice([-1, 1])
                    if a_sai == 0: a_sai = 5 # Tránh a=0 không là parabol
                    b_sai = b_val + randint(1, 2)
                    c_sai = c_val
                    f_sai = latex(a_sai) + "x^2 " + ("+" if b_sai > 0 else "") + latex(b_sai) + "x + " + latex(c_sai)
                    f_sai_str = "$y = %s$" % f_sai.replace("+ -", "- ")
                    if f_sai_str != da and f_sai_str not in s:
                        s.append(f_sai_str)

                das1, das2, das3 = s

                # Câu hỏi
                noidungcauhoi = (r'''Xác định parabol $y = ax^2 + bx + c$, biết rằng parabol đó có đỉnh nằm trên trục hoành và đi qua hai điểm $M(0;%s), N(%s;%s)$?'''
                                 %(latex(c_val), latex(xn), latex(c_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo hình ảnh
                loigiai=(r'''Vì $(P)$ có đỉnh nằm trên trục hoành nên $-\frac{\Delta}{4a} = 0 \Leftrightarrow \Delta = 0 \Leftrightarrow b^2 - 4ac = 0 \quad (1)$.\\
            Hơn nữa $(P)$ đi qua hai điểm $M(0;%s), N(%s;%s)$ nên ta có $\begin{cases} c = %s \\ %sa + %sb + c = %s \end{cases} \quad (2)$.\\
            Từ $(1)$ và $(2)$ ta có hệ:
            $\begin{cases} b^2 - 4a(%s) = 0 \\ c = %s \\ %sa + %sb = 0 \end{cases} \Leftrightarrow \begin{cases} c = %s \\ b = %sa \\ %s a^2 - %sa = 0 \end{cases} \Leftrightarrow \begin{cases} a = %s \\ b = %s \\ c = %s \end{cases}$ (vì $a \neq 0$).\\
            Vậy $(P): %s$.'''
                         %(latex(c_val), latex(xn), latex(c_val), 
                           latex(c_val), latex(xn**2), latex(xn), latex(c_val),
                           latex(c_val), latex(c_val), latex(xn**2), latex(xn),
                           latex(c_val), latex(Rational(-xn**2, xn)), latex((-Rational(-xn**2, xn))**2), latex(4*c_val),
                           latex(a_val), latex(b_val), latex(c_val),
                           kq_str))

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

