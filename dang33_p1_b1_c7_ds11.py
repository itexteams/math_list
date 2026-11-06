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


def bt_dang33_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo danh sách dạng
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số: k là mẫu số, c là điểm xét đạo hàm
                # Trong ảnh: k = 3, c = 1
                k = random.choice([2, 3, 4, 5, 6])
                c = random.choice([1, 2, 3])

                # Tính toán đáp án đúng
                # Điều kiện liên tục: a*c + b = c^2/k
                # Điều kiện có đạo hàm: a = 2*c/k
                a_dung = Rational(2*c, k)
                b_dung = Rational(-c**2, k)

                # Định dạng hiển thị đáp án đúng
                da_dung_str = 'a = %s; b = %s' % (latex(a_dung), latex(b_dung))
                da_dung_str = da_dung_str.replace('.', ',')

                # Tạo các phương án sai
                s = []
                # Sai do tính toán nhầm dấu hoặc hệ số đạo hàm
                s1 = 'a = %s; b = %s' % (latex(a_dung), latex(-b_dung))
                s2 = 'a = %s; b = %s' % (latex(Rational(c, k)), latex(b_dung))
                s3 = 'a = 1; b = %s' % (latex(Rational(c**2, k) - 1))
                s4 = 'a = %s; b = %s' % (latex(a_dung), latex(b_dung + 1))

                list_sai = [s1, s2, s3, s4]
                random.shuffle(list_sai)

                das1 = list_sai[0].replace('.', ',')
                das2 = list_sai[1].replace('.', ',')
                das3 = list_sai[2].replace('.', ',')

                # Nội dung câu hỏi
                # f(x) = x^2/k khi x <= c; ax + b khi x > c
                noidungcauhoi = ('''Cho hàm số $f\\left(x\\right) = \\begin{cases} \\frac{x^2}{%s} & \\text{khi } x \\le %s \\\\ ax + b & \\text{khi } x > %s \\end{cases}$. Giá trị nào sau đây của $a, b$ thì hàm số có đạo hàm tại $x = %s$ là'''
                                 % (latex(k), latex(c), latex(c), latex(c)))

                # Các đáp án
                da_d = ('\\True $' + da_dung_str + '$')
                da_s1 = '$' + das1 + '$'
                da_s2 = '$' + das2 + '$'
                da_s3 = '$' + das3 + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo mẫu trong ảnh
                # Tính các giá trị trung gian cho lời giải
                f_c = Rational(c**2, k)

                loigiai = ('''Hàm số có đạo hàm tại $x = %s$ suy ra hàm số liên tục tại $x = %s$. Tức là \\\\
                             $\\lim_{x \\to %s^+} f\\left(x\\right) = \\lim_{x \\to %s^-} f\\left(x\\right) = f\\left(%s\\right) \\Leftrightarrow a \\cdot %s + b = \\frac{%s^2}{%s} \\Leftrightarrow %s a + b = %s$ (1). \\\\
                             Mà hàm số có đạo hàm tại $x = %s$ thì $\\lim_{x \\to %s^+} \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = \\lim_{x \\to %s^-} \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s}$. \\\\
                             Với $\\begin{cases} \\lim_{x \\to %s^+} \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = \\lim_{x \\to %s^+} \\frac{ax + b - \\left(a \\cdot %s + b\\right)}{x - %s} = \\lim_{x \\to %s^+} \\frac{a\\left(x - %s\\right)}{x - %s} = \\lim_{x \\to %s^+} a = a \\\\ \\lim_{x \\to %s^-} \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = \\lim_{x \\to %s^-} \\frac{\\frac{x^2}{%s} - \\frac{%s}{%s}}{x - %s} = \\lim_{x \\to %s^-} \\frac{\\left(x + %s\\right)\\left(x - %s\\right)}{%s\\left(x - %s\\right)} = \\lim_{x \\to %s^-} \\frac{x + %s}{%s} = %s \\end{cases}$. \\\\
                             Suy ra $a = %s$. Thay vào (1) được $b = %s$.'''
                             % (latex(c), latex(c), 
                                latex(c), latex(c), latex(c), latex(c), latex(c), latex(k), latex(c), latex(f_c),
                                latex(c), latex(c), latex(c), latex(c), latex(c), latex(c), latex(c),
                                latex(c), latex(c), latex(c), latex(c), latex(c), latex(c), latex(c), latex(c), latex(c), latex(c),
                                latex(c), latex(c), latex(c), latex(c), latex(k), latex(c**2), latex(k), latex(c), latex(c), latex(c), latex(c), latex(k), latex(c), latex(c), latex(c), latex(k), latex(a_dung),
                                latex(a_dung), latex(b_dung)))

                # Thay dấu chấm thành dấu phẩy cho số thập phân nếu có (trong trường hợp Rational ra số thập phân)
                loigiai = loigiai.replace('.', ',')

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
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

