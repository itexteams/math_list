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


def bt_dang67_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn hệ số a ngẫu nhiên để bài toán đa dạng: y = (a*x*sin(x) + a*cos(x)) / tan(x)
                # Trong đề bài gốc, a = 1.
                a = random.randint(1, 5)

                # Biểu thức tử số và mẫu số
                tu_so = a*x*sin(x) + a*cos(x)
                mau_so = tan(x)

                # Hàm số ban đầu
                y = tu_so / mau_so

                # Rút gọn hàm số y để tính đạo hàm dễ hơn: y = (a*x*sin(x) + a*cos(x)) * (cos(x)/sin(x))
                # y = a*x*cos(x) + a*cos^2(x)/sin(x)
                y_rut_gon = a*x*cos(x) + a*(cos(x)**2 / sin(x))

                # Tính đạo hàm y'
                y_prime = diff(y_rut_gon, x)

                # Vế trái (VT): y' + y*tan(x)
                vt_expr = y_prime + y * tan(x)
                vt_simplified = simplify(vt_expr)

                # Vế phải (VP): Biểu thức mục tiêu theo đề bài (đã nhân thêm hệ số a)
                # Đề bài gốc: -cos^3(x) / sin^2(x). Với hệ số a: -a*cos^3(x) / sin^2(x)
                vp_latex = r"-\frac{%s \cos^3 x}{\sin^2 x}" % (latex(a) if a != 1 else "")

                # Các đáp án nhiễu cho câu hỏi trắc nghiệm (Thay đổi vế phải)
                da_dung = "$y' + y \\cdot \\tan x = %s$" % vp_latex

                s = [
                    "$y' + y \\cdot \\tan x = \\frac{%s \\cos^3 x}{\\sin^2 x}$" % (latex(a) if a != 1 else ""),
                    "$y' + y \\cdot \\tan x = -%s \\cos x$" % (latex(a) if a != 1 else ""),
                    "$y' + y \\cdot \\tan x = %s \\sin^2 x$" % (latex(a) if a != 1 else ""),
                    "$y' + y \\cdot \\tan x = -\\frac{%s \\sin^3 x}{\\cos^2 x}$" % (latex(a) if a != 1 else ""),
                ]

                das1 = random.choice(s); s.remove(das1)
                das2 = random.choice(s); s.remove(das2)
                das3 = random.choice(s)

                # B2: Viết lại nội dung câu hỏi
                noidungcauhoi = (r"Cho hàm số $y = \frac{%s x \sin x + %s \cos x}{\tan x}$. Chứng minh đẳng thức $y' + y \cdot \tan x = %s$. " 
                                 % (latex(a) if a != 1 else "", latex(a) if a != 1 else "",vp_latex))

                # Đáp án
                da_d = '\\True ' + da_dung
                da_s1 = das1
                da_s2 = das2
                da_s3 = das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (r'''Ta tiến hành rút gọn trước khi tính đạo hàm: \\
                           $y = \frac{%s x \sin x + %s \cos x}{\tan x} = \frac{(%s x \sin x + %s \cos x) \cdot \cos x}{\sin x} = %s x \cos x + \frac{%s \cos^2 x}{\sin x}$. \\
                           $\Rightarrow y' = %s(\cos x - x \sin x) - \frac{%s \cos x}{\sin^2 x} - %s \cos x = -%s x \sin x - \frac{%s \cos x}{\sin^2 x}$. \\
                           $\Rightarrow VT = -%s x \sin x - \frac{%s \cos x}{\sin^2 x} + (%s x \sin x + %s \cos x) = \frac{-%s \cos x(1 - \sin^2 x)}{\sin^2 x} = %s$.''' 
                           % (latex(a) if a != 1 else "", latex(a) if a != 1 else "", 
                              latex(a) if a != 1 else "", latex(a) if a != 1 else "",
                              latex(a) if a != 1 else "", latex(a) if a != 1 else "",
                              latex(a) if a != 1 else "", latex(a) if a != 1 else "",
                              latex(a) if a != 1 else "", latex(a) if a != 1 else "",
                              latex(a) if a != 1 else "", latex(a) if a != 1 else "",
                              latex(a) if a != 1 else "", latex(a) if a != 1 else "",
                              latex(a) if a != 1 else "", latex(a) if a != 1 else "",
                              vp_latex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

