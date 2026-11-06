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


def bt_dang35_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Ta sẽ chọn x0 là một phân số dạng 1/n với n nguyên dương từ 2 đến 10
            # Hoặc x0 là một số nguyên dương từ 2 đến 10 để đa dạng đề bài.
            n = random.randint(2, 10)
            loai_de = random.choice(['phan_so', 'so_nguyen'])

            if loai_de == 'phan_so':
                x0 = Rational(1, n)
            else:
                x0 = n

            # --- B1 & B2: Nghiên cứu đề bài và viết lại theo mẫu ---
            f = ln(x)
            f_prime = diff(f, x) # Đạo hàm là 1/x
            f_prime_value = f_prime.subs(x, x0)

            # Đáp án đúng
            da = '$%s$' % latex(f_prime_value)

            # Tạo các đáp án nhiễu (s)
            # Nhiễu 1: Thay vì 1/x thì lấy chính giá trị x0
            # Nhiễu 2: Đạo hàm nhầm thành 1/(x*ln(10)) hoặc giá trị âm
            # Nhiễu 3: Bình phương kết quả hoặc nghịch đảo ngược lại
            s = [
                '$%s$' % latex(x0),
                '$%s$' % latex(-f_prime_value),
                '$%s$' % latex(f_prime_value**2),
                '$%s$' % latex(1/f_prime_value if f_prime_value != 1 else 2),
                '$0$',
                '$1$'
            ]

            # Loại bỏ giá trị trùng với đáp án đúng nếu có
            s = [i for i in s if i != da]
            random.shuffle(s)

            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Nội dung câu hỏi
            noidungcauhoi = (r'Tính đạo hàm của hàm số $y = \ln x$ tại điểm $x = %s$.' 
                             % latex(x0))

            # Các đáp án trắc nghiệm
            da_d = r'\True ' + str(da)
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = (r'''Ta có: $y' = (\ln x)' = \frac{1}{x}$. \\ '''
                       r'''Từ đó $y'\left( %s \right) = \frac{1}{%s} = %s$.'''
                       % (latex(x0), latex(x0), latex(f_prime_value)))

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

