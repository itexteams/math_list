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


def bt_dang40_p1_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến và thiết lập ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn ngẫu nhiên cơ số b (b > 1)
                b_val = random.choice([2, 3, 4, 5, 6, 10])
                b = sp.Integer(b_val)

                # Tính toán kết quả chính xác
                # Nguyên hàm của (b^x - b^-x) là (b^x + b^-x) / ln(b)
                # I = 2 * [ (b^1 + b^-1)/ln(b) - (b^0 + b^-0)/ln(b) ]
                # I = 2 * (b + 1/b - 2) / ln(b) = [2 * (b-1)^2] / (b * ln(b))

                tuso = 2 * (b - 1)**2
                mauso = b

                # Rút gọn phân số tuso/mauso
                phan_so = Rational(tuso, mauso)
                ts = phan_so.p
                ms = phan_so.q

                # Đáp án đúng: \frac{ts}{ms \ln b}
                if ms == 1:
                    da_dung = r'$\frac{%s}{\ln %s}$' % (latex(ts), latex(b))
                else:
                    da_dung = r'$\frac{%s}{%s \ln %s}$' % (latex(ts), latex(ms), latex(b))

                # Bước 4: Điều chỉnh các phương án sai
                s = [
                    r'$\frac{%s}{\ln %s}$' % (latex(ts + 1), latex(b)),
                    r'$\frac{%s}{%s}$' % (latex(ts), latex(ms * b)),
                    r'$%s \ln %s$' % (latex(phan_so), latex(b)),
                    r'$\frac{%s}{%s \ln %s}$' % (latex(ts), latex(ms + 1), latex(b)),
                    r'$\frac{1}{\ln %s}$' % (latex(b)),
                    r'$\frac{%s}{%s \ln %s}$' % (latex(ts * 2), latex(ms), latex(b))
                ]

                # Lọc bỏ đáp án trùng với đáp án đúng (nếu có)
                s = [item for item in s if item != da_dung]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (r'Tích phân $I = \int_{-1}^{1} |%s^x - %s^{-x}| \text{d}x$ bằng'
                                 % (latex(b), latex(b)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2 - Viết lại y hệt cấu trúc lời giải hình ảnh)
                loigiai = (r'''Xét $I = \int_{-1}^{1} |%s^x - %s^{-x}| \text{d}x$, ta có $%s^x - %s^{-x} = 0 \Rightarrow x = 0$. \\
                             $\Rightarrow I = \int_{-1}^{0} |%s^x - %s^{-x}| \text{d}x + \int_{0}^{1} |%s^x - %s^{-x}| \text{d}x$ \\
                             $= \left| \int_{-1}^{0} (%s^x - %s^{-x}) \text{d}x \right| + \left| \int_{0}^{1} (%s^x - %s^{-x}) \text{d}x \right|$ \\
                             $= \left| \left( \frac{%s^x + %s^{-x}}{\ln %s} \right) \bigg|_{-1}^{0} \right| + \left| \left( \frac{%s^x + %s^{-x}}{\ln %s} \right) \bigg|_{0}^{1} \right|$ \\
                             $= \left| \frac{2}{\ln %s} - \frac{%s + \frac{1}{%s}}{\ln %s} \right| + \left| \frac{%s + \frac{1}{%s}}{\ln %s} - \frac{2}{\ln %s} \right|$ \\
                             $= %s$.'''
                           % (latex(b), latex(b), latex(b), latex(b),
                              latex(b), latex(b), latex(b), latex(b),
                              latex(b), latex(b), latex(b), latex(b),
                              latex(b), latex(b), latex(b),
                              latex(b), latex(b), latex(b),
                              latex(b), latex(b), latex(b), latex(b),
                              latex(b), latex(b), latex(b), latex(b),
                              da_dung.replace('$', '')))

            # Xuất câu trắc nghiệm
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

