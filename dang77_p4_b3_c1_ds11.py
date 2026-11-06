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


def bt_dang77_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số a, b cho mẫu số: sin(ax) - sin(bx)
                # Chọn a, b sao cho (a+b)/2 và (a-b)/2 là số nguyên
                a_b_pairs = [(5, 3), (7, 3), (5, 1), (7, 1), (9, 3)]
                a, b = random.choice(a_b_pairs)

                # Tính các hệ số sau khi biến đổi: m = (a+b)/2, n = (a-b)/2
                m = (a + b) // 2
                n = (a - b) // 2

                # Xử lý chuỗi hệ số
                m_str = 'x' if m == 1 else '%sx' % m
                n_str = 'x' if n == 1 else '%sx' % n

                # Hàm định dạng nghiệm
                def fmt_ans_cos(c):
                    if c == 1: return '\\frac{\\pi}{2} + k\\pi'
                    return '\\frac{\\pi}{%s} + \\frac{k\\pi}{%s}' % (2*c, c)

                def fmt_ans_sin(c):
                    if c == 1: return 'k\\pi'
                    return '\\frac{k\\pi}{%s}' % c

                ans1 = fmt_ans_cos(m)
                ans2 = fmt_ans_sin(n)
                da_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s; %s, k \\in \\mathbb{Z} \\right\\}' % (ans1, ans2)

                # --- Các đáp án sai (Distractors) ---
                das1_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s; %s, k \\in \\mathbb{Z} \\right\\}' % (fmt_ans_sin(m), fmt_ans_cos(n))
                das2_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s, k \\in \\mathbb{Z} \\right\\}' % (ans1)
                das3_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s, k \\in \\mathbb{Z} \\right\\}' % (ans2)

                # Đóng gói các đáp án
                da_d = ('\\True $%s$' % da_str)
                da_s1 = ('$%s$' % das1_str)
                da_s2 = ('$%s$' % das2_str)
                da_s3 = ('$%s$' % das3_str)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Câu hỏi
                noidungcauhoi = ('Tìm tập xác định của hàm số $y = \\frac{2\\sin x - 1}{\\sin %sx - \\sin %sx}$.' % (a, b))

                # Nội dung lời giải
                loigiai = ('''Hàm số xác định khi và chỉ khi mẫu số khác $0$: \\\\
                             $\\sin %sx - \\sin %sx \\neq 0$ \\\\
                             Áp dụng công thức $\\sin \\alpha - \\sin \\beta = 2\\cos\\frac{\\alpha + \\beta}{2}\\sin\\frac{\\alpha - \\beta}{2}$, ta có: \\\\
                             $\\Leftrightarrow 2\\cos %s \\sin %s \\neq 0$ \\\\
                             $\\Leftrightarrow \\begin{cases} \\cos %s \\neq 0 \\\\ \\sin %s \\neq 0 \\end{cases}$ \\\\
                             $\\Leftrightarrow \\begin{cases} %s \\neq \\frac{\\pi}{2} + k\\pi \\\\ %s \\neq k\\pi \\end{cases}$ \\\\
                             $\\Leftrightarrow \\begin{cases} x \\neq %s \\\\ x \\neq %s \\end{cases}, k \\in \\mathbb{Z}$.\\\\
                             Vậy tập xác định của hàm số là $%s$.'''
                             % (a, b,
                                m_str, n_str,
                                m_str, n_str,
                                m_str, n_str,
                                ans1, ans2,
                                da_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

