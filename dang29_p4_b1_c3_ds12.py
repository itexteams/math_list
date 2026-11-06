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


def bt_dang29_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')


            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hằng số a trong (x + a)
                # Trong đề gốc, a = 1 để có (x+2) và (x+1)
                a = random.randint(1, 4)
                a_plus_1 = a + 1

                x_target = random.randint(1, 4)


                f0_den = 2 * a
                f0_val = Rational(1, f0_den)

                # Tính toán đáp án đúng: f(x) = e^x / (2 * (x + a))
                ans_num = exp(x_target)
                ans_den = 2 * (x_target + a)

                # Đáp án đúng dưới dạng LaTeX
                da_dung = r'$\frac{e^{%s}}{%s}$' % (x_target if x_target != 1 else "", ans_den)
                if x_target == 1:
                     da_dung = r'$\frac{e}{%s}$' % (ans_den)

                # --- B4: Điều chỉnh các phương án sai ---
                s = [
                    r'$\frac{e^{%s}}{%s}$' % (x_target, ans_den + 2),
                    r'$\frac{e^{%s}}{%s}$' % (x_target, ans_den - 1 if ans_den > 1 else ans_den + 3),
                    r'$\frac{e^{%s}}{%s}$' % (x_target + 1, ans_den),
                    r'$\frac{e^{%s}}{%s}$' % (x_target, a * x_target),
                    r'$\frac{e^{%s}}{%s}$' % (x_target, 2 * x_target)
                ]

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # --- B2: Viết lại nội dung đề bài ---
                noidungcauhoi = (
                    '''Cho hàm số $f(x)$ có đạo hàm trên $\\mathbb{R}$ thỏa mãn '''
                    '''$(x + %s)f(x) + (x + %s)f\'(x) = e^x$ và $f(0) = \\frac{1}{%s}$. '''
                    '''Tính $f(%s)$.'''
                    % (latex(a_plus_1), latex(a), latex(f0_den), latex(x_target))
                )

                # Nội dung lời giải chi tiết
                loigiai = (
                    '''Ta có: \\\\ '''
                    '''$(x + %s)f(x) + (x + %s)f\'(x) = e^x \\Leftrightarrow (x + %s)f(x) + f(x) + (x + %s)f\'(x) = e^x$ \\\\ '''
                    '''$\\Leftrightarrow [(x + %s)f(x)] + [(x + %s)f(x)]\' = e^x$ \\\\ '''
                    '''$\\Leftrightarrow e^x[(x + %s)f(x)] + e^x[(x + %s)f(x)]\' = e^{2x}$ \\\\ '''
                    '''$\\Leftrightarrow [e^x(x + %s)f(x)]\' = e^{2x} \\Rightarrow e^x(x + %s)f(x) = \\int e^{2x}dx = \\frac{1}{2}e^{2x} + C$. \\\\ '''
                    '''Mà $f(0) = \\frac{1}{%s} \\Rightarrow e^0(0 + %s)\\cdot\\frac{1}{%s} = \\frac{1}{2}e^0 + C \\Rightarrow C = 0$. \\\\ '''
                    '''Vậy $f(x) = \\frac{e^{2x}}{2e^x(x + %s)} = \\frac{e^x}{2(x + %s)}$. \\\\ '''
                    '''Khi đó $f(%s) =$ %s.'''
                    % (a_plus_1, a, a, a, 
                       a, a, a, a, a, a, 
                       f0_den, a, f0_den, a, a, 
                       x_target, da_dung)
                )

                # Đưa vào danh sách đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

