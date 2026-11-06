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


def bt_dang51_p4_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                tong_he_so = random.choice([8, 10, 12, 14])

                if tong_he_so == 8:
                    a, b, c, d = 1, 7, 3, 5
                elif tong_he_so == 10:
                    a, b, c, d = 1, 9, 3, 7
                elif tong_he_so == 12:
                    a, b, c, d = 1, 11, 3, 9
                else:
                    a, b, c, d = 1, 13, 3, 11

                # Tính toán các hệ số góc sau khi dùng công thức biến đổi tích thành tổng
                # Vế trái: -1/2 * [cos((a+b)x) - cos((b-a)x)] = 1/2 * [cos(|a-b|x) - cos((a+b)x)]
                hieu1 = abs(a - b)
                tong1 = a + b

                # Vế phải: 1/2 * [cos(|c-d|x) - cos((c+d)x)]
                hieu2 = abs(c - d)
                tong2 = c + d

                # Do tong1 == tong2 nên phương trình trở thành cos(hieu1 * x) = cos(hieu2 * x)
                # Giải phương trình cos(hieu1 * x) = cos(hieu2 * x)
                # TH1: hieu1 * x = hieu2 * x + k2pi => (hieu1 - hieu2) * x = k2pi => x = k2pi / (hieu1 - hieu2)
                # TH2: hieu1 * x = -hieu2 * x + k2pi => (hieu1 + hieu2) * x = k2pi => x = k2pi / (hieu1 + hieu2)

                mau1 = hieu1 - hieu2
                mau2 = hieu1 + hieu2

                # Rút gọn phân số cho k2pi / mau1 và k2pi / mau2
                # Với bài toán gốc: hieu1=6, hieu2=2 => mau1=4, mau2=8 
                # => x = k2pi/4 = kpi/2 và x = k2pi/8 = kpi/4. Kết hợp nghiệm thu được x = kpi/4

                g1 = Rational(2, mau1) # Hệ số của k*pi ở TH1
                g2 = Rational(2, mau2) # Hệ số của k*pi ở TH2

                # Tìm nghiệm tổng quát (kết hợp nghiệm)
                # Đối với các bộ số được chọn, nghiệm g2 luôn là ước hoặc tập con bao hàm cả g1, do đó nghiệm cuối cùng là kpi / (mau2/2)
                mau_kq = int(mau2 / 2)

                kq_str = "x = \\frac{k\\pi}{%s}, k \\in \\mathbb{Z}" % mau_kq
                if mau_kq == 1:
                    kq_str = "x = k\\pi, k \\in \\mathbb{Z}"

                # Các đáp án trắc nghiệm (không dấu chấm ở cuối)
                du = ['$%s$' % kq_str]
                da = random.choice(du)

                # Tạo danh sách các phương án sai ngẫu nhiên không trùng với đáp án đúng
                s = [
                    '$x = k\\pi, k \\in \\mathbb{Z}$',
                    '$x = \\frac{k\\pi}{6}, k \\in \\mathbb{Z}$',
                    '$x = \\frac{k\\pi}{4}, k \\in \\mathbb{Z}$',
                    '$x = \\frac{k\\pi}{2}, k \\in \\mathbb{Z}$',
                    '$x = \\frac{k\\pi}{3}, k \\in \\mathbb{Z}$'
                ]

                # Loại bỏ đáp án đúng khỏi danh sách đáp án nhiễu nếu nó trùng
                s_filtered = [item for item in s if item != ('$%s$' % kq_str)]

                das1 = random.choice(s_filtered)
                s_filtered.remove(das1)
                das2 = random.choice(s_filtered)
                s_filtered.remove(das2)
                das3 = random.choice(s_filtered)

                # Câu hỏi sử dụng định dạng %s
                noidungcauhoi = ('''Giải phương trình $\\sin %sx \\sin %sx = \\sin %sx \\sin %sx$.'''
                                 % (latex(a) if a != 1 else "", latex(b), latex(c), latex(d)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuỗi hiển thị phân số trong lời giải
                frac1 = "\\frac{k\\pi}{%s}" % int(mau1/2) if int(mau1/2) != 1 else "k\\pi"
                frac2 = "\\frac{k\\pi}{%s}" % int(mau2/2) if int(mau2/2) != 1 else "k\\pi"

                # Nội dung lời giải sử dụng định dạng %s đầy đủ chi tiết từng bước
                loigiai = ('''Ta có: $\\sin %sx \\sin %sx = \\sin %sx \\sin %sx \\Leftrightarrow \\cos %sx - \\cos %sx = \\cos %sx - \\cos %sx$ \\\\
            $\\Leftrightarrow \\cos %sx = \\cos %sx \\Leftrightarrow \\begin{bmatrix} %sx = %sx + k2\\pi \\\\ %sx = -%sx + k2\\pi \\end{bmatrix} \\Leftrightarrow \\begin{bmatrix} x = %s \\\\ x = %s \\end{bmatrix} \\Leftrightarrow x = \\frac{k\\pi}{%s}, k \\in \\mathbb{Z}$.'''
                           % (latex(a) if a != 1 else "", latex(b), latex(c), latex(d), latex(hieu1), latex(tong1), latex(hieu2), latex(tong2),
                              latex(hieu1), latex(hieu2), latex(hieu1), latex(hieu2), latex(hieu1), latex(hieu2), frac1, frac2, latex(mau_kq)))

            # Xuất câu trắc nghiệm đúng định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

