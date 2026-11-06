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


def bt_dang45_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Hàm số có dạng y = sqrt( (mx + n)/(x - p) - k )
                # Biến đổi thành: sqrt( ((m-k)x + (n + kp)) / (x - p) )
                # Để tập xác định là (a, b], ta cần hệ số của x ở tử số âm: m - k < 0 => k > m

                p = random.randint(1, 5)        # Giá trị a = p
                b = p + random.randint(3, 10)   # Giá trị b (b > a)
                k = random.randint(3, 6)        # Số thực k bị trừ
                m = random.randint(1, k - 1)    # Hệ số m (m < k)

                # Tính n sao cho nghiệm của tử số là b: (m-k)b + n + kp = 0
                # => n = (k-m)b - kp
                n = (k - m) * b - k * p

                # Các giá trị tính toán cho lời giải
                a = p
                tong_ab = a + b

                # Tử số sau khi quy đồng: Ax + B
                A = m - k
                B = n + k * p

                # Bước 4: Điều chỉnh các phương án sai
                kq = tong_ab
                s = set()
                while len(s) < 3:
                    sai = kq + random.choice([-3, -2, -1, 1, 2, 3, 5, -5])
                    if sai != kq and sai > 0:
                        s.add(f'${sai}$')

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                # Biểu thức tử số của hàm số ban đầu: mx + n
                tu_so_bandau = f"{m}x + {n}" if n > 0 else f"{m}x - {abs(n)}"
                if m == 1: tu_so_bandau = tu_so_bandau.replace("1x", "x")

                noidungcauhoi = (r"Tập xác định của hàm số $y = \sqrt{\frac{%s}{x - %s} - %s}$ là $(a;b]$ với $a, b$ là các số thực. Tính tổng $a + b$."
                                 % (tu_so_bandau, p, k))

                # Đáp án
                da_d = r'\True $%s$' % kq
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Bước 2: Viết lại y hệt lời giải theo mẫu
                # Biểu thức tử số sau quy đồng
                tu_so_quydong = f"{A}x + {B}"
                if A == -1: tu_so_quydong = tu_so_quydong.replace("-1x", "-x")

                loigiai = (r'''Ta có $y = \sqrt{\frac{%s}{x - %s} - %s} = \sqrt{\frac{%s - %s(x - %s)}{x - %s}} = \sqrt{\frac{%s}{x - %s}}$. \\
                             Điều kiện xác định của hàm số: \\
                             $\begin{cases} x - %s \neq 0 \\ \frac{%s}{x - %s} \ge 0 \end{cases} \Leftrightarrow \frac{%s}{x - %s} \ge 0 \Leftrightarrow \left[\begin{array}{l} \begin{cases} %s \ge 0 \\ x - %s > 0 \end{cases} \\ \begin{cases} %s \le 0 \\ x - %s < 0 \end{cases} \end{array}\right. \Leftrightarrow \left[\begin{array}{l} \begin{cases} x \le %s \\ x > %s \end{cases} (TM) \\ \begin{cases} x \ge %s \\ x < %s \end{cases} (L) \end{array}\right.\\ \Leftrightarrow %s < x \le %s$. \\
                             TXĐ: $D = (%s; %s]$. \\
                             Vậy $a = %s, b = %s \Rightarrow a + b = %s$.'''
                           % (tu_so_bandau, p, k, tu_so_bandau, k, p, p, tu_so_quydong, p, 
                              p, tu_so_quydong, p, tu_so_quydong, p,
                              tu_so_quydong, p, tu_so_quydong, p,
                              b, a, b, a, a, b, a, b, a, b, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

