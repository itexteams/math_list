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


def bt_dang25_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')


            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo số tử số ngẫu nhiên (giống số 2026 trong đề)
                n_tu = randint(2020, 2030)

                # Chọn hệ số cho x^2 (thường là 1 để giống đề bài)
                a_coeff = 1

                # Chọn giá trị x bị loại (nghiệm x0)
                x0 = randint(-10, 10)
                if x0 == 0: x0 = 3 # Tránh số 0 quá đơn giản hoặc giữ nguyên số 3 như đề

                # Chọn các hệ số b, d sao cho b != d
                b = randint(-5, 5)
                d = randint(-5, 5)
                while b == d:
                    d = randint(-5, 5)

                # Chọn hệ số tự do c
                c = randint(-10, 10)

                # Tính e để (b-d)*x0 + c = e => e = b*x0 - d*x0 + c
                e = (b - d) * x0 + c

                # Biểu thức trong căn bậc 3
                f1 = a_coeff*x**2 + b*x + c
                f2 = a_coeff*x**2 + d*x + e

                # Đáp án đúng
                kq = x0
                da_dung = r'$D = \mathbb{R} \setminus \{%s\}$' % (latex(kq))

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = x0 + randint(-5, 5)
                    if sai != x0:
                        s.add(r'$D = \mathbb{R} \setminus \{%s\}$' % (latex(sai)))

                list_sai = list(s)
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                # Nội dung câu hỏi
                noidungcauhoi = (r'Tìm tập xác định của hàm số $y = \frac{%s}{\sqrt[3]{%s} - \sqrt[3]{%s}}$.'
                                 % (latex(n_tu), latex(f1), latex(f2)))

                # Nội dung lời giải
                # Giải: f1 = f2 <=> (b-d)x = e-c
                loigiai = (r'''Hàm số xác định khi $\sqrt[3]{%s} - \sqrt[3]{%s} \neq 0$ \\
                             $\Leftrightarrow \sqrt[3]{%s} \neq \sqrt[3]{%s}$ \\
                             $\Leftrightarrow %s \neq %s$ \\
                             $\Leftrightarrow %s \neq %s \Leftrightarrow x \neq %s$. \\
                             Vậy tập xác định của hàm số là $%s$.'''
                           % (latex(f1), latex(f2), 
                              latex(f1), latex(f2),
                              latex(f1), latex(f2),
                              latex((b-d)*x), latex(e-c), latex(kq),
                              da_dung))

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_all = [('\\True ' + da_dung), da_s1, da_s2, da_s3]
                random.shuffle(list_all)

                # Xuất nội dung theo định dạng mẫu
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

