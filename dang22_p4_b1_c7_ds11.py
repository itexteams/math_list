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


def bt_dang22_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B1 & B3: Thiết lập các giá trị ngẫu nhiên để bài toán luôn mới
            # Hàm số bậc 3 dạng: y = (a/3)x^3 + bx^2 + cx + d
            # Trong ảnh gốc: a=1, b=3, c=0, d=-2, k=-9

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo các hệ số sao cho đạo hàm ra nghiệm đẹp
                # y' = ax^2 + 2bx + c. Để nghiệm x0 đẹp, ta chọn x0 trước rồi suy ra k.
                a = 1
                b = random.randint(1, 5) # Trong ảnh là 3
                c = 0
                d = random.randint(-5, 5) # Trong ảnh là -2
                while d==0:
                    d = random.randint(-5, 5) # Trong ảnh là -2

                # Chọn một tọa độ tiếp điểm x0 nguyên để k đẹp
                x0_val = random.randint(-5, 2) # Trong ảnh là -3

                # Hàm số f(x)
                f = Rational(a, 3)*x**3 + b*x**2 + c*x + d
                f_prime = sp.diff(f, x)

                # Tính hệ số góc k tại x0_val
                k_val = f_prime.subs(x, x0_val)

                # Giải phương trình f'(x) = k để tìm x0 (có thể có 2 nghiệm, ta lấy x0_val làm chuẩn)
                # f' = ax^2 + 2bx + c = k_val <=> ax^2 + 2bx + (c - k_val) = 0

                y0_val = f.subs(x, x0_val)

                # Biểu diễn phương trình tiếp tuyến: y = k(x - x0) + y0
                # Dạng hiển thị: y - y0 = k(x - x0)

                # Xử lý hiển thị dấu cho y - y0 và x - x0
                y_part = f"y - {latex(y0_val)}" if y0_val >= 0 else f"y + {latex(abs(y0_val))}"
                x_part = f"x - {latex(x0_val)}" if x0_val >= 0 else f"x + {latex(abs(x0_val))}"

                # Đáp án đúng (Dạng C trong ảnh: y - y0 = k(x - x0))
                da_dung = f"${y_part} = {latex(k_val)}({x_part})$"

                # Tạo các đáp án nhiễu
                s = [
                    f"${y_part} = {latex(-k_val)}({x_part})$",
                    f"${y_part.replace('-', '+') if '-' in y_part else y_part.replace('+', '-')} = {latex(k_val)}({x_part})$",
                    f"${y_part} = {latex(k_val)}({x_part.replace('-', '+') if '-' in x_part else x_part.replace('+', '-')})$",
                    f"$y = {latex(k_val)}x + {latex(random.randint(-20, 20))}$"
                ]

                random.shuffle(s)
                da_s1, da_s2, da_s3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (f"Cho hàm số $y = {latex(f)}$ có đồ thị là $(C)$. "
                                 f"Lập phương trình tiếp tuyến với đồ thị $(C)$ biết tiếp tuyến có hệ số góc $k = {latex(k_val)}$.")

                # Nội dung lời giải
                # Xử lý chuỗi đạo hàm để thay thế ++ thành + hoặc +- thành -
                f_prime_str = latex(f_prime).replace('+-', '-').replace('--', '+')

                loigiai = (f"Ta có $y' = {f_prime_str}$. \\\\\n"
                           f"Gọi $x_0$ là hoành độ tiếp điểm, ta có: $y'(x_0) = {latex(k_val)} \\Leftrightarrow {latex(f_prime).replace('x', 'x_0')} = {latex(k_val)}$ \\\\\n"
                           f"$\\Leftrightarrow {latex(sp.simplify(f_prime - k_val)).replace('x', 'x_0')} = 0 \\Leftrightarrow x_0 = {latex(x0_val)}$. \\\\\n"
                           f"Với $x_0 = {latex(x0_val)} \\Rightarrow y_0 = {latex(y0_val)}$. \\\\\n"
                           f"Vậy phương trình tiếp tuyến là: $y = y'(x_0)(x - x_0) + y_0 \\Leftrightarrow$ {da_dung}.")

                # Đưa các đáp án vào danh sách
                da_d = '\\True ' + da_dung
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # B2: Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '- ').replace('- -', '+ ').replace('- +', '- ').replace('+ +', '+ ')
            return content

