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


def bt_dang14_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo danh sách dạng bài
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Tạo các hệ số ngẫu nhiên cho hàm y = (ax + b)^2 - 2k|ax + b| + c
                # Giống ảnh: a=2, b=-1, hệ số t = 4 (tức k=2), c=3
                a = random.randint(2, 4)
                b = random.randint(-5, 5)
                if b == 0: b = 1

                k = random.randint(2, 5) 
                he_so_t = 2 * k # Đây là số 4 trong ảnh mẫu
                c = random.randint(1, 10)

                # Chuỗi hiển thị biểu thức trong trị tuyệt đối
                # Xử lý dấu của b để hiển thị đẹp: 2x - 1 hoặc 2x + 1
                dau_b = "+" if b > 0 else "-"
                bieu_thuc_t = f"{a}x {dau_b} {abs(b)}"

                # 2. Tính toán kết quả
                # Đặt t = |ax + b|, t >= 0. Hàm trở thành f(t) = t^2 - 2kt + c
                # Đỉnh t_I = k. Giá trị nhỏ nhất là f(k) = k^2 - 2k^2 + c = c - k^2
                t_I = k
                min_val = c - k**2

                # Tìm x: |ax + b| = k
                x1 = Rational(k - b, a)
                x2 = Rational(-k - b, a)

                # 3. Tạo đáp án
                kq = min_val
                da_d = f"\\True ${latex(kq)}$"

                # Tạo 3 đáp án sai không trùng nhau và không trùng đáp án đúng
                s_options = set()
                while len(s_options) < 3:
                    sai = kq + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    if sai != kq:
                        s_options.add(f"${latex(sai)}$")

                list_sai = list(s_options)

                # 4. Nội dung câu hỏi
                noidungcauhoi = (f"Tìm giá trị nhỏ nhất của hàm số $y = ({bieu_thuc_t})^2 - {he_so_t}|{bieu_thuc_t}| + {c}$.")

                # 5. Nội dung lời giải (Bám sát 100% cấu trúc ảnh mẫu)
                loigiai = (f'''Đặt $t = |{bieu_thuc_t}| \\geq 0$ thì $y = t^2 - {he_so_t}t + {c}, t \\geq 0$. \\\\
            Hàm số $y = t^2 - {he_so_t}t + {c}$ có $a = 1 > 0$ nên bề lõm hướng lên. \\\\
            Hoành độ đỉnh $t_I = -\\frac{{b}}{{2a}} = {t_I} \\in [0; +\\infty)$. \\\\
            Do đó $\\min y = \\min f(t) = f({t_I}) = {min_val}$ đạt được khi $|{bieu_thuc_t}| = {t_I} \\Leftrightarrow x = {latex(x1)}$ hoặc $x = {latex(x2)}$.''')

                # 6. Đưa các đáp án vào danh sách và trộn
                list_1 = [da_d, list_sai[0], list_sai[1], list_sai[2]]
                random.shuffle(list_1)

            # 7. Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

