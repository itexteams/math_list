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


def bt_dang45_p1_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các giá trị ngẫu nhiên cho hàm số y = sqrt(m + k) / (ax^2 + bx + m)
                # Để đảm bảo lời giải đẹp, ta chọn b là số chẵn
                a = random.randint(1, 4)
                b_half = random.randint(-4, 4)
                if b_half == 0: b_half = 1
                b = 2 * b_half
                k = random.randint(1, 5)

                # Điều kiện 1: m + k >= 0 => m >= -k
                m_min_1 = -k

                # Điều kiện 2: ax^2 + bx + m # 0 với mọi x thuộc R
                # Vì a > 0, nên tam thức luôn dương khi Delta' < 0
                # Delta' = (b/2)^2 - a*m < 0  => m > (b/2)^2 / a
                tu_so_delta = b_half**2
                mau_so_delta = a
                val_delta = Rational(tu_so_delta, mau_so_delta)

                # Kết quả cuối cùng là m > max(m_min_1, val_delta)
                # Thông thường val_delta sẽ lớn hơn m_min_1 trong các bài toán này
                if val_delta > m_min_1:
                    kq_val = val_delta
                else:
                    kq_val = m_min_1

                # Đáp án đúng
                da_dung_str = 'm > %s' % (latex(kq_val))

                # Các phương án sai (ngẫu nhiên hóa dấu và giá trị)
                s = [
                    'm < %s' % (latex(kq_val)),
                    'm \\ge %s' % (latex(kq_val)),
                    'm > %s' % (latex(kq_val + 1)),
                    'm > %s' % (latex(kq_val - 1)),
                    'm > %s' % (latex(Rational(1, 2))),
                    'm > 1',
                ]

                # Lọc bỏ phương án sai nếu trùng với đáp án đúng
                s = [i for i in s if i != da_dung_str]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = (r'''Giá trị $m$ để hàm số $y = \frac{\sqrt{m + %s}}{%sx^2 %s x + m}$ xác định trên $\mathbb{R}$ là'''
                                 % (latex(k), latex(a) if a != 1 else "", (r'+ ' + str(b) if b > 0 else r'- ' + str(abs(b))))
                                 )

                # Các đáp án
                da_d = ('\\True $%s$' % da_dung_str)
                da_s1 = '$%s$' % das1
                da_s2 = '$%s$' % das2
                da_s3 = '$%s$' % das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (trình bày theo cách phân tích tam thức như ảnh mẫu)
                loigiai = (r'''Hàm số xác định khi $\begin{cases} m + %s \ge 0 \\ %sx^2 %s x + m \neq 0 \end{cases} \Leftrightarrow \begin{cases} m \ge %s \\ %s\left( x %s \right)^2 + m - %s \neq 0 \end{cases}$. \\
                             Để hàm số xác định với mọi $x \in \mathbb{R} \Leftrightarrow \begin{cases} m \ge %s \\ m - %s > 0 \end{cases}$ đúng với mọi $x \in \mathbb{R}$. \\
                             $\Leftrightarrow \begin{cases} m \ge %s \\ m > %s \end{cases} \Leftrightarrow m > %s$. \\
                             Vậy $m > %s$ thỏa mãn yêu cầu bài toán.'''
                           % (latex(k), latex(a), (r'+ ' + str(b) if b > 0 else r'- ' + str(abs(b))), 
                              latex(m_min_1), latex(a), 
                              latex(Rational(b, 2*a)), latex(val_delta),
                              latex(m_min_1), latex(val_delta),
                              latex(m_min_1), latex(val_delta), latex(kq_val),
                              latex(kq_val)
                             ))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

