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


def bt_dang51_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Random hệ số a và b trong mẫu số (a - b*cos(x))
                a = random.choice([1, 2, 3, 4, 5])
                b = random.choice([2, 3, 4, 5, 6])
                if a == b: b += 1 # Tránh trường hợp mẫu số bằng 0 tại x=0

                # Hàm số y = u/v
                u = x
                v = a - b*cos(x)

                # Đạo hàm từng phần
                u_prime = 1
                v_prime = b*sin(x) # Đạo hàm của (a - b*cos(x)) là b*sin(x)

                # Kết quả đạo hàm: y' = (u'v - uv') / v^2
                tu_so_bieuthuc = v - u * v_prime
                mau_so_bieuthuc = v**2

                # Chuyển sang định dạng latex để hiển thị
                str_tu = latex(tu_so_bieuthuc)
                str_mau = latex(mau_so_bieuthuc)

                # Đáp án đúng
                da = f"$\\dfrac{{{str_tu}}}{{{str_mau}}}$"

                # Tạo các đáp án nhiễu (sai dấu hoặc sai công thức)
                s1 = f"$\\dfrac{{{latex(v + u * v_prime)}}}{{{str_mau}}}$" # Sai dấu giữa
                s2 = f"$\\dfrac{{{latex(v - v_prime)}}}{{{str_mau}}}$"     # Quên nhân x
                s3 = f"$\\dfrac{{{str_tu}}}{{{latex(v)}}}$"              # Quên bình phương mẫu

                # Trộn đáp án
                da_d = '\\True ' + da
                list_1 = [da_d, s1, s2, s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = f"Đạo hàm của hàm số $y = \\dfrac{{{latex(u)}}}{{{latex(v)}}}$ bằng "

                # Nội dung lời giải
                loigiai = (f"Áp dụng quy tắc đạo hàm hàm phân thức $\\left(\\dfrac{{u}}{{v}}\\right)' = \\dfrac{{u'v - uv'}}{{v^2}}$: \\\\\n"
                           f"Ta có: $u = {latex(u)} \\Rightarrow u' = {latex(u_prime)}$ \\\\\n"
                           f"$v = {latex(v)} \\Rightarrow v' = {latex(v_prime)}$ \\\\\n"
                           f"Vậy $y' = \\dfrac{{{latex(u_prime)}({latex(v)}) - {latex(u)}({latex(v_prime)})}}{{{latex(mau_so_bieuthuc)}}} = \\dfrac{{{str_tu}}}{{{str_mau}}}$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\cos{\\left(x \\right)}', '\\cos x').replace('\\sin{\\left(x \\right)}', '\\sin x')
            return content

