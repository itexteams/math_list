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


def bt_dang43_p1_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Chọn n là bội của 3 để k = 2n/3 là số nguyên
                n_val = random.choice([12, 15, 18, 21])

                # Bước 2: Tính hằng số K trong phương trình A_n^2 - C_n^2 = K
                # Ta có A_n^2 - C_n^2 = n(n-1) - n(n-1)/2 = n(n-1)/2
                k_const = n_val * (n_val - 1) // 2
                delta = 1 + 8 * k_const
                n_neg = (1 - int(sqrt(delta))) // 2

                # Bước 3: Tìm số hạng không chứa x
                # Khai triển (x^2 - 1/x)^n có số hạng tổng quát: T_{k+1} = C_n^k * (x^2)^{n-k} * (-x^{-1})^k
                # T_{k+1} = C_n^k * (-1)^k * x^{2n - 2k - k} = C_n^k * (-1)^k * x^{2n - 3k}
                # Số hạng không chứa x <=> 2n - 3k = 0 <=> k = 2n/3
                k_val = (2 * n_val) // 3

                # Hệ số (vì k = 2n/3 với n chia hết cho 3 nên k luôn chẵn, (-1)^k = 1)
                # Tuy nhiên ta vẫn tính theo công thức tổng quát
                kq_val = binomial(n_val, k_val) * ((-1)**k_val)
                kq = str(kq_val).replace('.', ',')

                # Các đáp án trắc nghiệm
                da_d = ('\\True ' + '$%s$' % (kq))

                # Tạo các phương án sai
                s1 = '$%s$' % (str(-kq_val)).replace('.', ',')
                s2 = '$%s$' % (str(binomial(n_val, k_val - 1))).replace('.', ',')
                s3 = '$%s$' % (str(-binomial(n_val, k_val - 1))).replace('.', ',')

                # Đảm bảo không trùng lặp
                list_s = list(set([s1, s2, s3]))
                while len(list_s) < 3:
                    random_val = kq_val + randint(1, 100)
                    list_s.append('$%s$' % (str(random_val)).replace('.', ','))
                    list_s = list(set(list_s))

                da_s1 = list_s[0]
                da_s2 = list_s[1]
                da_s3 = list_s[2]

                # Câu hỏi
                noidungcauhoi = ('''Số hạng không chứa $x$ trong khai triển $\\left(x^2 - \\frac{1}{x}\\right)^{n}$ biết $A_{n}^2 - C_{n}^2 = %s$ là'''
                                 % (latex(k_const)))

                # Các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có: $A_{n}^2 - C_{n}^2 = %s \\Leftrightarrow \\frac{n!}{\\left(n-2\\right)!} - \\frac{n!}{2!\\left(n-2\\right)!} = %s$ \\\\
                             $\\Leftrightarrow n\\left(n-1\\right) - \\frac{n\\left(n-1\\right)}{2} = %s \\Leftrightarrow \\frac{1}{2}n\\left(n-1\\right) = %s$ \\\\
                             $\\Leftrightarrow n^2 - n - %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & n = %s \\\\ & n = %s \\text{ (loại)} \\end{aligned} \\right.$ \\\\
                             Suy ra số hạng tổng quát trong khai triển: $T_{k+1} = C_{%s}^k \\cdot \\left(x^2\\right)^{%s-k} \\cdot \\left(-\\frac{1}{x}\\right)^k = C_{%s}^k \\cdot \\left(-1\\right)^k \\cdot x^{%s-3k}$. \\\\
                             Tìm $%s - 3k = 0 \\Leftrightarrow k = %s$. \\\\
                             Vậy hệ số của số hạng không chứa $x$ trong khai triển là: $C_{%s}^{%s} \\cdot \\left(-1\\right)^{%s} = %s$.'''
                           % (latex(k_const), latex(k_const), latex(k_const), latex(k_const),
                              latex(2 * k_const), latex(n_val), latex(n_neg),
                              latex(n_val), latex(n_val), latex(n_val), latex(2 * n_val),
                              latex(2 * n_val), latex(k_val),
                              latex(n_val), latex(k_val), latex(k_val), kq
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

