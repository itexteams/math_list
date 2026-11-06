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


def bt_dang55_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B1 & B3: Nghiên cứu đề bài và thiết lập random
            # Bài toán gốc: y = cos(3x).sin(2x) tại x = pi/3
            # Random hệ số a, b trong cos(ax) và sin(bx)
            a_val = random.randint(2, 5)
            b_val = random.randint(2, 5)
            # Random giá trị x0 có dạng pi/k
            k_val = random.choice([2, 3, 4, 6])
            x0 = pi / k_val

            # Hàm số
            y = cos(a_val * x) * sin(b_val * x)

            # Tính đạo hàm tổng quát
            y_prime = diff(y, x)

            # Tính giá trị đạo hàm tại x0
            # Để hiển thị đẹp, ta tính các thành phần đạo hàm riêng biệt
            # (cos(ax))' = -a*sin(ax)
            # (sin(bx))' = b*cos(bx)
            y_prime_value = y_prime.subs(x, x0)

            # B2: Viết lại bài toán theo mẫu code Python
            noidungcauhoi = (r'''Cho hàm số $y = \cos %sx \cdot \sin %sx$. Tính đạo hàm $y'\left( \frac{\pi}{%s} \right)$.''' 
                             % (latex(a_val), latex(b_val), latex(k_val)))

            # Đáp án đúng
            da_dung = latex(y_prime_value)
            if da_dung == '0': da_dung = '0' # Xử lý số 0

            # Tạo các đáp án nhiễu (random sai lệch)
            list_sai = [
                latex(y_prime_value + 1),
                latex(y_prime_value - 1),
                latex(-y_prime_value),
                latex(y_prime_value * 2),
                latex(Rational(1, 2)),
                latex(-Rational(1, 2))
            ]
            # Loại bỏ đáp án đúng nếu lỡ trùng trong list sai
            if da_dung in list_sai: list_sai.remove(da_dung)
            random.shuffle(list_sai)

            da_s1 = list_sai[0]
            da_s2 = list_sai[1]
            da_s3 = list_sai[2]

            # Trộn đáp án
            da_d = r'\True $' + da_dung + '$'
            list_1 = [da_d, '$' + da_s1 + '$', '$' + da_s2 + '$', '$' + da_s3 + '$']
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = (r'''Ta có $y' = (\cos %sx)' \cdot \sin %sx + \cos %sx \cdot (\sin %sx)' = -%s \sin %sx \cdot \sin %sx + %s \cos %sx \cdot \cos %sx$. \\
                         Do đó $y'\left( \frac{\pi}{%s} \right) = -%s \sin \left( \frac{%s\pi}{%s} \right) \cdot \sin \left( \frac{%s\pi}{%s} \right) + %s \cos \left( \frac{%s\pi}{%s} \right) \cdot \cos \left( \frac{%s\pi}{%s} \right) = %s$.'''
                         % (latex(a_val), latex(b_val), latex(a_val), latex(b_val), 
                            latex(a_val), latex(a_val), latex(b_val), latex(b_val), latex(a_val), latex(b_val),
                            latex(k_val), latex(a_val), latex(a_val), latex(k_val), latex(b_val), latex(k_val),
                            latex(b_val), latex(a_val), latex(k_val), latex(b_val), latex(k_val),
                            latex(y_prime_value)
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

