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


def bt_dang74_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bài toán mẫu: y = (2sinx - 1) / (sqrt(3)sin2x - cos2x)
                # Tổng quát: mẫu số dạng A*sin(ax) - B*cos(ax) != 0
                # Ta random a, và random cặp (A, B) = (sqrt(3), 1) hoặc (1, sqrt(3)) hoặc (1, 1)

                a = random.choice([2, 3, 4])

                # Random cặp hệ số (A, B) và góc phụ alpha tương ứng
                # sqrt(3)sin(ax) - cos(ax) = 2(sqrt(3)/2 sin(ax) - 1/2 cos(ax)) = 2(sin(ax)cos(pi/6) - cos(ax)sin(pi/6)) = 2sin(ax - pi/6)
                # sqrt(3)sin(ax) + cos(ax) = 2(sqrt(3)/2 sin(ax) + 1/2 cos(ax)) = 2(sin(ax)cos(pi/6) + cos(ax)sin(pi/6)) = 2sin(ax + pi/6)
                # sin(ax) - sqrt(3)cos(ax) = 2(1/2 sin(ax) - sqrt(3)/2 cos(ax)) = 2(sin(ax)cos(pi/3) - cos(ax)sin(pi/3)) = 2sin(ax - pi/3)
                # sin(ax) + sqrt(3)cos(ax) = 2(1/2 sin(ax) + sqrt(3)/2 cos(ax)) = 2(sin(ax)cos(pi/3) + cos(ax)sin(pi/3)) = 2sin(ax + pi/3)

                cases = [
                    ('\\sqrt{3}', '-', '1', '\\frac{\\sqrt{3}}{2}', '\\frac{1}{2}', '\\frac{\\pi}{6}'),
                    ('\\sqrt{3}', '+', '1', '\\frac{\\sqrt{3}}{2}', '\\frac{1}{2}', '-\\frac{\\pi}{6}'),
                    ('1', '-', '\\sqrt{3}', '\\frac{1}{2}', '\\frac{\\sqrt{3}}{2}', '\\frac{\\pi}{3}'),
                    ('1', '+', '\\sqrt{3}', '\\frac{1}{2}', '\\frac{\\sqrt{3}}{2}', '-\\frac{\\pi}{3}')
                ]

                # Chọn ngẫu nhiên trường hợp, đảm bảo có trường hợp của bài mẫu (index 0)
                A_str, sign, B_str, cos_alpha, sin_alpha, alpha = random.choice(cases)

                # Xử lý chuỗi hiển thị mẫu số
                if A_str == '1':
                    term1 = '\\sin %sx' % a
                else:
                    term1 = '%s\\sin %sx' % (A_str, a)

                if B_str == '1':
                    term2 = '\\cos %sx' % a
                else:
                    term2 = '%s\\cos %sx' % (B_str, a)

                mau_so_str = '%s %s %s' % (term1, sign, term2)

                # Hàm số
                noidungcauhoi = ('Tìm tập xác định của hàm số $y = \\frac{2\\sin x - 1}{%s}$.' % mau_so_str)

                # Đáp án
                # sin(ax - alpha_val) != 0 <=> ax - alpha_val != k*pi <=> x != alpha_val/a + k*pi/a

                # Xử lý chuỗi kết quả alpha/a
                if alpha == '\\frac{\\pi}{6}':
                    ans_pi = '\\frac{\\pi}{%s}' % (6*a)
                    moved_alpha = '\\frac{\\pi}{6}'
                elif alpha == '-\\frac{\\pi}{6}':
                    ans_pi = '-\\frac{\\pi}{%s}' % (6*a)
                    moved_alpha = '-\\frac{\\pi}{6}'
                elif alpha == '\\frac{\\pi}{3}':
                    ans_pi = '\\frac{\\pi}{%s}' % (3*a)
                    moved_alpha = '\\frac{\\pi}{3}'
                elif alpha == '-\\frac{\\pi}{3}':
                    ans_pi = '-\\frac{\\pi}{%s}' % (3*a)
                    moved_alpha = '-\\frac{\\pi}{3}'

                da_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (ans_pi, a)

                # Distractors
                # Sai lầm 1: Quên chia chu kỳ cho a
                das1_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + k\\pi, k \\in \\mathbb{Z} \\right\\}' % (ans_pi)

                # Sai lầm 2: Nhầm dấu của alpha
                if '-' in ans_pi:
                    ans_err_pi = ans_pi.replace('-', '')
                else:
                    ans_err_pi = '-' + ans_pi
                das2_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (ans_err_pi, a)

                # Sai lầm 3: Sai chu kỳ thành k2pi/a
                das3_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + \\frac{k2\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (ans_pi, a)

                # Đóng gói các đáp án
                da_d = ('\\True $%s$' % (da_str))
                da_s1 = ('$%s$' % (das1_str))
                da_s2 = ('$%s$' % (das2_str))
                da_s3 = ('$%s$' % (das3_str))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Xử lý dấu trong biểu thức khai triển
                if sign == '-':
                    khaitrien_sign = '-'
                    goc_sign = '-'
                else:
                    khaitrien_sign = '+'
                    goc_sign = '+'

                alpha_pos = alpha.replace('-', '')

                loigiai = ('''Hàm số xác định khi và chỉ khi mẫu số khác $0$: \\\\
                             $%s \\neq 0$ \\\\
                             Chia cả hai vế cho $2$, ta có: \\\\
                             $\\Leftrightarrow %s \\sin %sx %s %s \\cos %sx \\neq 0$ \\\\
                             $\\Leftrightarrow \\sin %sx \\cos \\left( %s \\right) %s \\cos %sx \\sin \\left( %s \\right) \\neq 0$ \\\\
                             Áp dụng công thức $\\sin(a %s b) = \\sin a \\cos b %s \\cos a \\sin b$, ta được: \\\\
                             $\\Leftrightarrow \\sin\\left(%sx %s %s\\right) \\neq 0$ \\\\
                             $\\Leftrightarrow %sx %s %s \\neq k\\pi$ \\\\
                             $\\Leftrightarrow %sx \\neq %s + k\\pi$ \\\\
                             $\\Leftrightarrow x \\neq %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z}$.\\\\
                             Vậy tập xác định của hàm số là $%s$.'''
                             % (mau_so_str,
                                cos_alpha, a, sign, sin_alpha, a,
                                a, alpha_pos, sign, a, alpha_pos,
                                goc_sign, khaitrien_sign,
                                a, goc_sign, alpha_pos,
                                a, goc_sign, alpha_pos,
                                a, moved_alpha,
                                ans_pi, a,
                                da_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

