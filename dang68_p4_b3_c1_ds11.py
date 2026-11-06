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


def bt_dang68_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các hệ số a, c, b và d/e cho hàm số y = tan(ax) + c*cot(bx + d\pi/e)
                a = random.choice([2, 3, 4])
                c = random.choice([2, 3, 4, 5])
                b = random.choice([2, 3, 4, 5])
                # Đưa tham số của bài gốc vào để có thể sinh ra bài toán mẫu
                b_c = random.choice([Rational(-1,3), Rational(1,3), Rational(-1,4), Rational(1,4), Rational(-1,6), Rational(1,6), Rational(1,2), Rational(-1,2)])

                # Biểu thức trong hàm cot
                expr_cot = b * x + b_c * pi

                # --- Xử lý điều kiện 1 (của tan): cos(ax) != 0 ---
                # ax != pi/2 + k*pi => x != pi/(2a) + k*pi/a
                ans1_val = Rational(1, 2*a)
                ans1_pi = latex(ans1_val * pi)

                # --- Xử lý điều kiện 2 (của cot): sin(bx + b_c*pi) != 0 ---
                # bx + b_c*pi != k*pi => bx != -b_c*pi + k*pi => x != (-b_c/b)*pi + k*pi/b
                ans2_val = -b_c / b
                ans2_pi = latex(ans2_val * pi)
                moved_val = latex(-b_c * pi) # Biểu thức pi khi chuyển vế

                # Đáp án đúng
                da_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + \\frac{k\\pi}{%s}; %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (ans1_pi, a, ans2_pi, b)

                # --- Các đáp án sai (Distractors) ---
                # Sai lầm 1: Chuyển vế sai dấu ở điều kiện cot
                ans2_err1_val = b_c / b
                ans2_err1_pi = latex(ans2_err1_val * pi)
                das1_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + \\frac{k\\pi}{%s}; %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (ans1_pi, a, ans2_err1_pi, b)

                # Sai lầm 2: Quên chia chu kỳ k*pi cho hệ số a và b
                das2_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + k\\pi; %s + k\\pi, k \\in \\mathbb{Z} \\right\\}' % (ans1_pi, ans2_pi)

                # Sai lầm 3: Nhớ nhầm điều kiện của tan và cot (cho sin(ax)!=0 và cos(bx+...)!=0)
                ans2_err3_val = (Rational(1,2) - b_c) / b
                ans2_err3_pi = latex(ans2_err3_val * pi)
                das3_str = 'D = \\mathbb{R} \\setminus \\left\\{ \\frac{k\\pi}{%s}; %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (a, ans2_err3_pi, b)

                # Câu hỏi
                noidungcauhoi = ('Tìm tập xác định của hàm số $y = \\tan %sx + %s \\cot\\left(%s\\right)$.' 
                                 % (a, c, latex(expr_cot)))

                # Các đáp án
                da_d = ('\\True $%s$' % (da_str))
                da_s1 = '$%s$' % (das1_str)
                da_s2 = '$%s$' % (das2_str)
                da_s3 = '$%s$' % (das3_str)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Hàm số xác định khi và chỉ khi: \\\\
                             $\\begin{cases} \\cos %sx \\neq 0 \\\\ \\sin\\left(%s\\right) \\neq 0 \\end{cases}$ \\\\
                             $\\Leftrightarrow \\begin{cases} %sx \\neq \\frac{\\pi}{2} + k\\pi \\\\ %s \\neq k\\pi \\end{cases}$ \\\\
                             $\\Leftrightarrow \\begin{cases} x \\neq %s + \\frac{k\\pi}{%s} \\\\ %sx \\neq %s + k\\pi \\end{cases}$ \\\\
                             $\\Leftrightarrow \\begin{cases} x \\neq %s + \\frac{k\\pi}{%s} \\\\ x \\neq %s + \\frac{k\\pi}{%s} \\end{cases}, k \\in \\mathbb{Z}$.\\\\
                             Vậy tập xác định của hàm số là $%s$.'''
                             % (a, latex(expr_cot),
                                a, latex(expr_cot),
                                ans1_pi, a, b, moved_val,
                                ans1_pi, a, ans2_pi, b,
                                da_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

