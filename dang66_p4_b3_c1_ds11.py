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


def bt_dang66_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các hệ số a và b/c cho hàm số y = (1 + sin x) / cos(ax + b\pi/c)
                a = random.choice([2, 3, 4])
                # Đưa tham số của bài gốc (-1/3) vào tập random để có thể sinh ra chính xác bài toán mẫu
                b_c = random.choice([Rational(-1,3), Rational(1,3), Rational(-1,4), Rational(1,4), Rational(-1,6), Rational(1,6), Rational(2,3), Rational(-2,3)])

                # Biểu thức trong hàm cos (ở mẫu số)
                expr_den = a * x + b_c * pi

                # Tử số (cố định hàm 1 + sin x hoặc có thể thay đổi tương tự)
                tu_so = '1 + \\sin x'

                # Tính toán đáp án đúng
                # Điều kiện: cos(ax + b_c * pi) != 0
                # => ax + b_c * pi != pi/2 + k*pi
                # => ax != (1/2 - b_c)*pi + k*pi
                v1 = Rational(1, 2) - b_c
                v1_pi = v1 * pi

                # => x != (1/2 - b_c)/a * pi + k*pi/a
                ans_val = v1 / a
                ans_pi = ans_val * pi

                da_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (latex(ans_pi), a)

                # Các đáp án sai (Distractors)
                # Sai lầm 1: Quên chia chu kỳ k*pi cho a
                das1_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + k\\pi, k \\in \\mathbb{Z} \\right\\}' % (latex(ans_pi))

                # Sai lầm 2: Chuyển vế sai dấu (ví dụ - chuyển qua vẫn giữ nguyên hoặc + chuyển thành +)
                v2 = Rational(1, 2) + b_c
                ans2_val = v2 / a
                ans2_pi = ans2_val * pi
                das2_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (latex(ans2_pi), a)

                # Sai lầm 3: Nhầm sang điều kiện của sin (khác 0 => khác k*pi)
                v3 = -b_c
                ans3_val = v3 / a
                ans3_pi = ans3_val * pi
                das3_str = 'D = \\mathbb{R} \\setminus \\left\\{ %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (latex(ans3_pi), a)

                # Đưa phương án nhiễu vào danh sách
                s = [das1_str, das2_str, das3_str]
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Tìm tập xác định của hàm số $y = \\frac{%s}{\\cos\\left(%s\\right)}$.' 
                                 % (tu_so, latex(expr_den)))

                # Các đáp án
                da_d = ('\\True $%s$' % (da_str))
                da_s1 = '$%s$' % (das1)
                da_s2 = '$%s$' % (das2)
                da_s3 = '$%s$' % (das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Hàm số xác định khi và chỉ khi $\\cos\\left(%s\\right) \\neq 0$ \\\\
                             $\\Leftrightarrow %s \\neq \\frac{\\pi}{2} + k\\pi$ \\\\
                             $\\Leftrightarrow %sx \\neq %s + k\\pi$ \\\\
                             $\\Leftrightarrow x \\neq %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z}$.\\\\
                             Vậy tập xác định của hàm số là $D = \\mathbb{R} \\setminus \\left\\{ %s + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}$.'''
                             % (latex(expr_den), latex(expr_den), a, latex(v1_pi), latex(ans_pi), a, latex(ans_pi), a))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

