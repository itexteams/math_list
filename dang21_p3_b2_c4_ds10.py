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


def bt_dang21_p3_b2_c4_ds10(self):
            # Khai báo biến
            # --- Khai báo biến ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Tạo các hệ số ngẫu nhiên cho Parabol (P): y = x^2 + ax + b
                # Ở đây chọn a = 1, b = -2 như đề gốc để đảm bảo tính ổn định, hoặc random nhỏ
                a_p = 1
                b_p = -2

                # 2. Tạo hệ số cho đường thẳng d: y = -(m + k)x + m + h
                # Trong đề gốc: k = 1, h = 2
                k = randint(1, 3)
                h = randint(2, 5)

                # Để đơn giản và giống đề gốc (Delta luôn dương), ta chọn m < - (h+2)
                limit_upper = -(h + 2)

                # 4. Thiết lập khoảng của m: [L; R)
                # Đề gốc: [-10; -4), với limit_upper = -4
                L = randint(-15, -10)
                R = limit_upper

                # 5. Tính số giá trị nguyên m
                # m thuộc [L; R) => m nhận các giá trị L, L+1, ..., R-1
                so_gia_tri = max(0, R - L)

                # Đáp án đúng
                kq = so_gia_tri

                # Các đáp án trắc nghiệm
                du = ['$%s$' % kq]
                da = du[0]

                # Tạo danh sách đáp án nhiễu
                s_raw = [kq + 1, kq + 2, kq + 3, kq - 1, kq - 2, kq - 3]
                s_raw = [x for x in s_raw if x >= 0] # Không lấy số âm nếu không cần thiết
                s_raw = list(set(s_raw)) # Loại bỏ trùng
                if kq in s_raw: s_raw.remove(kq)

                random.shuffle(s_raw)
                das1 = '$%s$' % s_raw[0]
                das2 = '$%s$' % s_raw[1]
                das3 = '$%s$' % s_raw[2]

                # --- Câu hỏi ---
                noidungcauhoi = ('''Hỏi có bao nhiêu giá trị $m$ nguyên trong nửa khoảng $[%s;%s)$ để đường thẳng $d: y = -(m+%s)x + m + %s$ cắt parabol $(P): y = x^2 + x - 2$ tại hai điểm phân biệt nằm về cùng một phía đối với trục tung?'''
                                 % (latex(L), latex(R), latex(k), latex(h)))

                # --- Các đáp án ---
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải ---
                # Delta = m^2 + m(2k+6) + (k+1)^2 + 4h + 8. 
                # Với các số nguyên nhỏ, biểu thức này thường dương với m < R.
                delta_expr = f"m^2 + {2*k+6}m + {(k+1)**2 + 4*h + 8}"

                loigiai = ('''Phương trình hoành độ giao điểm của $d$ và $(P)$:
                             $$x^2 + x - 2 = -(m + %s)x + m + %s \\Leftrightarrow x^2 + (m + %s)x - m - %s = 0 \\quad (*).$$
                             $d$ cắt $(P)$ tại hai điểm phân biệt nằm về cùng một phía đối với trục tung khi và chỉ khi $(*)$ có hai nghiệm phân biệt cùng dấu:
                             $$\\begin{cases} \\Delta > 0 \\\\ P > 0 \\end{cases} \\Leftrightarrow \\begin{cases} %s > 0 \\\\ -m - %s > 0 \\end{cases} \\Leftrightarrow m < %s.$$
                             Kết hợp điều kiện $m \\in [%s;%s)$, ta có $m \\in [%s;%s)$.
                             Vậy có $%s$ giá trị $m$ nguyên thỏa mãn bài toán.'''
                           % (latex(k), latex(h), latex(k+1), latex(h+2), 
                              delta_expr, latex(h+2), latex(limit_upper),
                              latex(L), latex(R), latex(L), latex(R), latex(kq)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content



