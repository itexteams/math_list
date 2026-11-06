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


def bt_dang49_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # f(x) = (ax + b) / sqrt(|x - c| - 1)
                # g(x) = (dx - sqrt(m - kx)) / (|x| + h)

                c = randint(2, 6) # Tham số dịch chuyển trong trị tuyệt đối
                k = randint(2, 4) # Hệ số của x trong căn thức m - kx
                a = randint(1, 5) # Hệ số x tử số f(x)
                b = randint(-5, 5) # Hệ số tự do tử số f(x)
                d = randint(1, 5) # Hệ số x tử số g(x)
                h = randint(1, 10) # Hệ số tự do mẫu số g(x)

                # Tính toán tập xác định D1: |x - c| > 1
                # <=> x - c > 1 hoặc x - c < -1
                # <=> x > c + 1 hoặc x < c - 1
                x_left = c - 1
                x_right = c + 1

                # Tính toán tập xác định D2: m - kx >= 0 <=> x <= m/k
                # D2 = (-inf; m/k]

                # Để D2 subset D1, vì D2 kéo dài tới -inf nên m/k phải nằm trong khoảng (-inf; x_left)
                # Tức là m/k < x_left => m < k * x_left
                threshold = k * x_left

                # Đáp án đúng
                kq = 'm < %s' % (latex(threshold))

                # --- B4: Điều chỉnh các phương án sai ---
                # Tạo danh sách các phương án nhiễu không trùng với đáp án đúng
                du = ['\\True $%s$' % (kq)]

                s = [
                    '$m \\le %s$' % (latex(threshold)),
                    '$m < %s$' % (latex(threshold + k)),
                    '$m > %s$' % (latex(threshold)),
                    '$m < %s$' % (latex(x_left)),
                    '$m \\ge %s$' % (latex(threshold)),
                    '$m < %s$' % (latex(k * x_right))
                ]

                # Lấy ngẫu nhiên 3 đáp án sai
                random.shuffle(s)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Câu hỏi
                noidungcauhoi = (r'''Cho hàm số $f(x) = \frac{%sx %s}{\sqrt{|x - %s| - 1}}$ có tập xác định là $D_1$ và hàm số $g(x) = \frac{%sx - \sqrt{m - %sx}}{|x| + %s}$ có tập xác định là $D_2$. Tìm điều kiện của tham số $m$ để $D_2 \subset D_1$.'''
                                 % (latex(a), (f'+ {b}' if b >= 0 else f'- {abs(b)}'), latex(c), latex(d), latex(k), latex(h)))

                # Nội dung lời giải (Viết y hệt logic trong ảnh)
                loigiai = (r'''Xét $f(x) = \frac{%sx %s}{\sqrt{|x - %s| - 1}}$ \\
                           ĐKXĐ: $|x - %s| - 1 > 0 \Leftrightarrow |x - %s| > 1 \Leftrightarrow \left[\begin{aligned} &x - %s > 1 \\ &x - %s < -1 \end{aligned}\right. \Leftrightarrow \left[\begin{aligned} &x > %s \\ &x < %s \end{aligned}\right.$ \\
                           $\Rightarrow D_1 = (-\infty; %s) \cup (%s; +\infty)$. \\
                           Xét $g(x) = \frac{%sx - \sqrt{m - %sx}}{|x| + %s}$ \\
                           Ta thấy $|x| + %s > 0$ với mọi $x \in \mathbb{R}$. \\
                           ĐKXĐ: $m - %sx \geq 0 \Leftrightarrow x \leq \frac{m}{%s} \Rightarrow D_2 = \left(-\infty; \frac{m}{%s}\right]$. \\
                           Để $D_2 \subset D_1$ thì $\frac{m}{%s} < %s \Leftrightarrow m < %s$. \\
                           Vậy với $m < %s$ thì $D_2 \subset D_1$.'''
                           % (latex(a), (f'+ {b}' if b >= 0 else f'- {abs(b)}'), latex(c), 
                              latex(c), latex(c), latex(c), latex(c), latex(x_right), latex(x_left),
                              latex(x_left), latex(x_right),
                              latex(d), latex(k), latex(h), latex(h),
                              latex(k), latex(k), latex(k),
                              latex(k), latex(x_left), latex(threshold), latex(threshold)))

                # Trộn đáp án
                list_1 = [du[0], da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

