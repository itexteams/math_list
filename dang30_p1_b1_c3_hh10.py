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


def bt_dang30_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến và loại bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn ngẫu nhiên tọa độ cho vectơ chỉ phương u = (a; b)
                a = randint(1, 9) * random.choice([-1, 1])
                b = randint(1, 9) * random.choice([-1, 1])

                # Đảm bảo a và b không làm cho các phương án nhiễu bị trùng lặp dễ dàng
                if abs(a) == abs(b):
                    b = b + 1 if b > 0 else b - 1

                # Đáp án đúng: n_delta = u_d = (a; b)
                kq_dung = (a, b)
                da_str = '(%s;%s)' % (latex(a), latex(b))

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                # Các phương án nhiễu phổ biến:
                # 1. Vectơ pháp tuyến của d (vuông góc với u): (-b; a)
                # 2. Vectơ đối của vectơ pháp tuyến d: (b; -a)
                # 3. Vectơ đối của u: (-a; -b)

                s = [
                    '(%s;%s)' % (latex(-b), latex(a)),
                    '(%s;%s)' % (latex(b), latex(-a)),
                    '(%s;%s)' % (latex(-a), latex(-b)),
                    '(%s;%s)' % (latex(a), latex(-b)),
                    '(%s;%s)' % (latex(-a), latex(b))
                ]

                # Loại bỏ giá trị trùng với đáp án đúng nếu có
                s = [item for item in s if item != da_str]
                # Lấy ngẫu nhiên 3 đáp án sai duy nhất
                wrong_options = random.sample(list(set(s)), 3)

                das1 = wrong_options[0]
                das2 = wrong_options[1]
                das3 = wrong_options[2]

                # B2: Viết lại bài toán theo mẫu
                # Câu hỏi
                noidungcauhoi = ('''Đường thẳng $d$ có một vectơ chỉ phương là $\\vec{u} = (%s;%s)$. Đường thẳng $\\Delta$ vuông góc với $d$ có một vectơ pháp tuyến là'''
                                 % (latex(a), latex(b)))

                # Các đáp án
                da_d = ('\\True $\\vec{n} = ' + da_str + '$')
                da_s1 = ('$\\vec{n} = ' + str(das1) + '$')
                da_s2 = ('$\\vec{n} = ' + str(das2) + '$')
                da_s3 = ('$\\vec{n} = ' + str(das3) + '$')

                # Trộn các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo ảnh
                loigiai = ('''Ta có đường thẳng $d$ có vectơ chỉ phương là $\\vec{u}_d = (%s;%s)$.\\\\
                             Vì đường thẳng $\\Delta$ vuông góc với đường thẳng $d$ nên vectơ pháp tuyến của đường thẳng $\\Delta$ chính là vectơ chỉ phương của đường thẳng $d$.\\\\
                             Do đó, $\\vec{n}_{\\Delta} = \\vec{u}_d = (%s;%s)$.'''
                           % (latex(a), latex(b), latex(a), latex(b)))

            # Xuất câu trắc nghiệm theo đúng cấu trúc content yêu cầu
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

