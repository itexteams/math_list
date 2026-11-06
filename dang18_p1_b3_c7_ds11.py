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


def bt_dang18_p1_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B2 & B3: Thiết lập random
            lisdang = ['cos', 'sin']
            dang = random.choice(lisdang)

            # Random hệ số a và b
            a = random.choice([i for i in range(-5, 6) if i != 0])
            b = random.randint(-10, 10)

            # Xử lý hiển thị biểu thức ax + b
            if b > 0:
                bieu_thuc_trong = f"{a}x + {b}" if a != 1 else f"x + {b}"
            elif b < 0:
                bieu_thuc_trong = f"{a}x - {abs(b)}" if a != 1 else f"x - {abs(b)}"
            else:
                bieu_thuc_trong = f"{a}x" if a != 1 else "x"
            bieu_thuc_trong = bieu_thuc_trong.replace("-1x", "-x").replace(" 1x", " x")

            # Thiết lập hàm số
            if dang == 'cos':
                y = cos(a*x + b)
                ten_ham = "\\cos"
            else:
                y = sin(a*x + b)
                ten_ham = "\\sin"

            # Tính toán đạo hàm
            y_prime = y.diff(x)
            y_second_prime = y_prime.diff(x)

            # Đáp án đúng
            da_dung = f"${latex(y_second_prime)}$"

            # --- PHẦN SỬA LỖI: TẠO ĐÁP ÁN NHIỄU AN TOÀN ---
            s_set = set()
            # Thêm các dạng nhiễu cơ bản
            s_set.add(f"${latex(-y_second_prime)}$")
            s_set.add(f"${latex(y_prime)}$")
            s_set.add(f"${latex(-y_prime)}$")
            s_set.add(f"${latex(y)}$")
            s_set.add(f"${latex(a**2 * y)}$")

            # Loại bỏ đáp án đúng nếu nó lọt vào danh sách nhiễu
            if da_dung in s_set:
                s_set.remove(da_dung)

            # Nếu vẫn chưa đủ 3 đáp án nhiễu, thêm các giá trị random khác để không bao giờ bị lỗi index
            counter = 1
            while len(s_set) < 3:
                s_set.add(f"${latex((a+counter)*y)}$")
                counter += 1

            # Chuyển thành list và xáo trộn
            s_list = list(s_set)
            random.shuffle(s_list)

            das1 = s_list[0]
            das2 = s_list[1]
            das3 = s_list[2]
            # ----------------------------------------------

            # Câu hỏi
            noidungcauhoi = f"Đạo hàm cấp $2$ của hàm số $y = {ten_ham}({bieu_thuc_trong})$ là"

            # Các đáp án trắc nghiệm
            da_d = '\\True ' + da_dung
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Trộn thứ tự đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = (f"Tập xác định: $\\mathscr{{D}} = \\mathbb{{R}}$.\\\\ \n"
                       f"Đạo hàm cấp 1: $y' = ({ten_ham}({bieu_thuc_trong}))' = {latex(y_prime)}$.\\\\ \n"
                       f"Đạo hàm cấp 2: $y'' = ({latex(y_prime)})' = {latex(y_second_prime)}$.")

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

