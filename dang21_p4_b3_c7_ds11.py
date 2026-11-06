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


def bt_dang21_p4_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Random các hệ số A, B, a và hằng số b
                A_val = random.choice([i for i in range(-10, 11) if i != 0])
                B_val = random.choice([i for i in range(-10, 11) if i != 0])
                a_val = random.choice([i for i in range(2, 6)]) # a thường dương để biểu thức đẹp
                b_val = random.randint(1, 9)

                t = symbols('t')
                # Biểu thức gốc: y = A*sin(at+b) + B*cos(at+b)
                expr_inside = a_val * t + b_val
                y = A_val * sin(expr_inside) + B_val * cos(expr_inside)

                # Tính đạo hàm cấp 1 và cấp 2
                y_prime = sp.diff(y, t)
                y_double_prime = sp.diff(y_prime, t)

                # Chuẩn bị hiển thị Latex
                A_lat = latex(A_val)
                B_lat = latex(B_val)
                a_lat = latex(a_val)
                b_lat = latex(b_val)
                a_sq_lat = latex(a_val**2)

                # Hàm xử lý dấu để tránh dạng + - hoặc - -
                def format_expr(val, func_str, is_first=False):
                    lat = latex(val * eval(f"sp.{func_str}(a_val*t + b_val)"))
                    if is_first:
                        return lat
                    return (" + " + lat) if val > 0 else lat

                # Bước 2: Viết lại bài toán theo mẫu code
                noidungcauhoi = (r'''Cho hàm số $y = %s$. Chứng minh rằng $y'' + %s y = 0$.''' 
                                % (latex(y), a_sq_lat))

                # Các đáp án trắc nghiệm (Ở đây là bài tập chứng minh nên ta giả định các phương án nhiễu)
                da_d = r'\True Đẳng thức đúng'
                da_s1 = r'Đẳng thức sai'
                da_s2 = r'$y'' - %s y = 0$' % a_sq_lat
                da_s3 = r'$y'' + %s y = %s$' % (a_lat, A_lat)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (r'''Tập xác định: $D = \mathbb{R}$. \\
                           Ta có: \\
                           $y' = (%s)' = %s$. \\
                           $y'' = (%s)' = %s$. \\
                           Đặt $-%s$ làm nhân tử chung: \\
                           $y'' = -%s \left( %s \right) = -%s y$. \\
                           Do đó: $y'' + %s y = 0$.''' 
                           % (latex(y), latex(y_prime), 
                              latex(y_prime), latex(y_double_prime),
                              a_sq_lat, a_sq_lat, latex(y), a_sq_lat, a_sq_lat))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

