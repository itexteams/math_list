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


def bt_dang17_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Hàm số có dạng y = (ax + b) / (cx + d)
            # Để có giao điểm với trục hoành đẹp, ta chọn x0 là số nguyên
            # Để đạo hàm không quá phức tạp, chọn các hệ số nhỏ

            while True:
                a = random.randint(1, 5)
                x0 = random.randint(-5, 5)
                # y(x0) = 0 => a*x0 + b = 0 => b = -a*x0
                b = -a * x0

                c = random.randint(1, 3)
                d = random.randint(-10, 10)

                # Điều kiện: x0 không là nghiệm mẫu và ad - bc != 0 (hàm không suy biến)
                if (c * x0 + d != 0) and (a * d - b * c != 0):
                    break

            # Thiết lập hàm số
            tu = a * x + b
            mau = c * x + d
            f = tu / mau

            # B1 & B2: Nghiên cứu đề bài và viết lại theo mẫu code
            # Tính đạo hàm
            f_prime = sp.diff(f, x)
            y_prime_x0 = f_prime.subs(x, x0)

            # Phương trình tiếp tuyến: y = f'(x0)(x - x0) + f(x0)
            # Vì x0 là giao điểm trục hoành nên f(x0) = 0
            # y = k*x - k*x0
            k = y_prime_x0
            constant_term = -k * x0

            # Tạo các đáp án nhiễu
            # Đáp án đúng
            da_dung = f'y = {latex(sp.expand(k * (x - x0)))}'

            # Danh sách các đáp án sai (nhiễu)
            s = [
                f'y = {latex(sp.expand(Rational(1, 2) * k * (x - x0)))}',
                f'y = {latex(sp.expand(-k * (x - x0)))}',
                f'y = {latex(sp.expand(k * x))}',
                f'y = {latex(sp.expand(2 * k * (x - x0)))}',
                f'y = {latex(sp.expand(k * (x + x0)))}'
            ]

            du = [f'${da_dung}$']
            da = random.choice(du)

            # Lấy ngẫu nhiên 3 đáp án sai
            random.shuffle(s)
            das1 = f'${s[0]}$'
            das2 = f'${s[1]}$'
            das3 = f'${s[2]}$'

            # Nội dung câu hỏi
            noidungcauhoi = (r'Lập phương trình tiếp tuyến của đồ thị $(H): y = \frac{%s}{%s}$ tại giao điểm của $(H)$ và trục hoành.'
                             % (latex(tu), latex(mau)))

            # Các đáp án trắc nghiệm
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            # Xử lý hiển thị dấu + - tự động thông qua latex của sympy
            loigiai = (r'''Giao điểm của $(H)$ và trục hoành là điểm $M(%s; 0)$. \\
                        Ta có $y' = \frac{%s}{(%s)^2}$ nên $y'(%s) = %s$. \\
                        Phương trình tiếp tuyến với $(H)$ tại điểm $M$ là: 
                        $y = y'(%s)(x - %s) + 0 \Leftrightarrow %s$.'''
                       % (latex(x0), latex(a * d - b * c), latex(mau), latex(x0), latex(k),
                          latex(x0), latex(x0), da_dung))

            # Chỉnh sửa hiển thị +- thành -
            noidungcauhoi = noidungcauhoi.replace('+ -', '- ').replace('- -', '+ ')
            loigiai = loigiai.replace('+ -', '- ').replace('- -', '+ ')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

