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


def bt_dang36_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo ngẫu nhiên giá trị a (đáp án đúng) dưới dạng phân số hoặc số nguyên để bài toán đa dạng
                # Chọn tử số là số lẻ và mẫu số là 2 để có kết quả dạng như bài gốc (ví dụ: 1/2, 3/2, 5/2,...)
                tu = random.choice([1, 3, 5, -1, -3, -5])
                mau = 2
                a_val = Rational(tu, mau)


                # Ta chọn ngẫu nhiên c để tạo bài toán tổng quát, c phải là số nguyên dương
                c_val = randint(1, 5)
                # Từ f'(1^+) = f'(1^-) => 2*a*1 = c => 2a = c => a = c/2
                a_val = Rational(c_val, 2)

                # Chọn b ngẫu nhiên (trong bài mẫu b = 1)
                b_val = randint(1, 4)

                # Từ điều kiện liên tục: a*(1)^2 + b = c*(1) + d => a + b = c + d => d = a + b - c
                d_val = a_val + b_val - c_val

                # Đáp án đúng
                da = '$%s$' % (latex(a_val)).replace('.', ',')

                # Tạo các phương án sai (nhiễu) không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai_val = a_val + random.choice([1, 2, -1, -2, Rational(1, 2), Rational(-1, 2), 0])
                    if sai_val != a_val:
                        s.add('$%s$' % (latex(sai_val)).replace('.', ','))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Biểu diễn các phân số gọn gàng trong đề bài
                b_latex = latex(b_val)
                d_latex = latex(d_val)
                c_latex = '' if c_val == 1 else latex(c_val) # nếu c=1 thì chỉ hiện x thay vì 1x

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = f(x) = \\begin{cases} ax^2 + %s & \\text{khi } x > 1 \\\\ %sx + %s & \\text{khi } x \\le 1 \\end{cases}$. Nếu $f(x)$ có đạo hàm tại $x = 1$ thì $a$ bằng'''
                                 % (b_latex, c_latex, d_latex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Biến phục vụ lời giải
                hai_a = latex(2*a_val)
                hai_a_x = '2ax'
                c_str = latex(c_val)

                # Nội dung lời giải chi tiết theo các bước
                loigiai = ('''Ta có: $y\' = f\'(x) = \\begin{cases} %s & \\text{khi } x > 1 \\\\ %s & \\text{khi } x \\le 1 \\end{cases}$.\\\\
                             Để hàm số có đạo hàm tại $x = 1$ thì đạo hàm bên trái bằng đạo hàm bên phải:\\\\
                             $2a \\cdot 1 = %s \\Leftrightarrow 2a = %s \\Leftrightarrow a = %s$.'''
                           % (hai_a_x, c_str, c_str, c_str, latex(a_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

