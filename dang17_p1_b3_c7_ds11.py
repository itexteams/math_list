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


def bt_dang17_p1_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Bước 1: Random các thông số bài toán
            # Random hệ số a trong khoảng từ -10 đến 10 (khác 0)
            a = random.choice([i for i in range(-10, 11) if i != 0])

            # Random hàm số (0 là cos, 1 là sin)
            loai_ham = random.randint(0, 1)

            if loai_ham == 0:
                f = a * cos(x)
                ten_ham = f"{a if a != 1 else ''}\\cos x".replace('1\\cos', '\\cos').replace('-1\\cos', '-\\cos')
            else:
                f = a * sin(x)
                ten_ham = f"{a if a != 1 else ''}\\sin x".replace('1\\sin', '\\sin').replace('-1\\sin', '-\\sin')

            # Điểm tính đạo hàm (trong hình là pi/2, ta có thể fix hoặc random)
            # Ở đây mình chọn các điểm đẹp: pi, pi/2, pi/3, pi/4, pi/6
            list_x0 = [pi, pi/2, pi/3, pi/4, pi/6]
            x0 = random.choice(list_x0)

            # Bước 2: Tính toán đạo hàm và kết quả
            f_prime = diff(f, x)
            f_double_prime = diff(f_prime, x)
            kq_value = f_double_prime.subs(x, x0)

            # Định dạng hiển thị dấu cho đúng quy tắc toán học
            def format_expr(expr):
                s = latex(expr)
                return s.replace('+-', '-').replace('--', '+')

            # Bước 3: Tạo các phương án nhiễu
            da_dung = '$y\'\'\\left(%s\\right) = %s$' % (latex(x0), latex(kq_value))

            # Tạo danh sách đáp án sai (tránh trùng với đáp án đúng)
            s = set()
            while len(s) < 3:
                nhieu = random.choice([-3, -2, -1, 0, 1, 2, 3, 5])
                # Đảm bảo nhiễu là một biểu thức latex
                val_nhieu = '$y\'\'\\left(%s\\right) = %s$' % (latex(x0), latex(nhieu))
                if val_nhieu != da_dung:
                    s.add(val_nhieu)

            list_nhieu = list(s)

            # Nội dung câu hỏi
            noidungcauhoi = (r'Đạo hàm cấp hai của hàm số $y = %s$ tại điểm $x_0 = %s$ là' 
                             % (ten_ham, latex(x0)))

            # Nội dung lời giải
            loigiai = (r'''Ta có $y = %s \Rightarrow y' = %s \Rightarrow y'' = %s$.\\''' 
                       r'''Vậy $y''\left(%s\right) = %s$.''' 
                       % (ten_ham, format_expr(f_prime), format_expr(f_double_prime), 
                          latex(x0), latex(kq_value)))

            # Các đáp án trắc nghiệm
            da_d = '\\True ' + da_dung
            da_s1 = list_nhieu[0]
            da_s2 = list_nhieu[1]
            da_s3 = list_nhieu[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
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

