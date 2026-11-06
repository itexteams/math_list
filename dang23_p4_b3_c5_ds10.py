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


def bt_dang23_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            x, y = symbols('x y')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn ngẫu nhiên số mũ n trong khoảng từ 4 đến 5
                n = random.randint(4, 5)

                bieu_thuc = (x - y)**n
                kq_dung = expand(bieu_thuc)

                def format_latex(expr):
                    s = latex(expr)
                    s = s.replace('(', '\\left(').replace(')', '\\right)')
                    return s

                da = '$%s$' % (format_latex(kq_dung))

                # Tạo các phương án nhiễu
                s1 = '$%s$' % (format_latex(expand((x + y)**n)))

                terms = sp.Add.make_args(kq_dung)
                last_term = terms[-1]
                kq_sai2 = kq_dung - 2 * last_term
                s2 = '$%s$' % (format_latex(kq_sai2))

                terms_list = list(terms)
                kq_sai3 = 0
                for term in terms_list:
                    if term == terms_list[0]:
                        kq_sai3 += term
                    else:
                        kq_sai3 -= abs(term)
                s3 = '$%s$' % (format_latex(kq_sai3))

                noidungcauhoi = ('Khai triển nhị thức $\\left( x-y \\right)^{%s}$.'
                                 % (n))

                da_d = ('\\True ' + str(da))
                da_s1 = str(s1)
                da_s2 = str(s2)
                da_s3 = str(s3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                buoc_khai_trien = ''
                for k in range(n + 1):
                    # Sử dụng hàm binomial đã import
                    coeff = binomial(n, k) 
                    sign = '+' if k % 2 == 0 else '-'
                    if k == 0:
                        term_str = 'x^{%s}' % (n)
                    elif k == n:
                        term_str = ' %s y^{%s}' % (sign, n)
                    else:
                        term_str = ' %s %s x^{%s} y^{%s}' % (sign, coeff if coeff != 1 else '', n - k, k)
                    buoc_khai_trien += term_str

                loigiai = ('Áp dụng công thức nhị thức Newton: \\\\ '
                           '$\\left( a+b \\right)^{n} = \\sum_{k=0}^{n} C_{n}^{k} a^{n-k} b^{k}$. \\\\ '
                           'Với $a=x, b=-y$ và $n=%s$, ta có: \\\\ '
                           '$\\left( x-y \\right)^{%s} = C_{%s}^{0} x^{%s} + C_{%s}^{1} x^{%s} \\left( -y \\right)^{1} + \\dots + C_{%s}^{%s} \\left( -y \\right)^{%s}$. \\\\ '
                           'Kết quả khai triển là: \\\\ '
                           '$%s$.'
                           % (n, n, n, n, n, n-1, n, n, n, format_latex(kq_dung)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

