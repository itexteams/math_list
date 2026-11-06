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


def bt_dang48_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random giá trị tan x nguyên dương từ 1 đến 3 để tạo ra nhiều câu hỏi khác nhau
                # Bài mẫu tương ứng với k = 2
                k = random.choice([1, 2, 3])

                # Tính toán giá trị trung gian
                tan_sq = k**2
                mẫu_cos_sq = 1 + tan_sq

                # Chuỗi hiển thị Latex cho các giá trị căn số trong lời giải
                str_cos_abs = '\\frac{1}{\\sqrt{%s}}' % (str(mẫu_cos_sq))
                str_cos_neg = '-\\frac{1}{\\sqrt{%s}}' % (str(mẫu_cos_sq))
                str_sin_neg = '-\\frac{%s}{\\sqrt{%s}}' % (str(k), str(mẫu_cos_sq))

                # Đáp án đúng cho biểu thức sin(x + pi/3) = sin(x)*cos(pi/3) + cos(x)*sin(pi/3)
                # = (str_sin_neg) * (1/2) + (str_cos_neg) * (sqrt(3)/2) = - (k + sqrt(3)) / (2*sqrt(mẫu_cos_sq))
                if k == 1:
                    da = '$-\\frac{1 + \\sqrt{3}}{2\\sqrt{2}}$'
                    s_raw = [
                        '$\\frac{1 - \\sqrt{3}}{2\\sqrt{2}}$',
                        '$\\frac{1 + \\sqrt{3}}{2\\sqrt{2}}$',
                        '$\\frac{-1 + \\sqrt{3}}{2\\sqrt{2}}$',
                        '$\\frac{1 + 2\\sqrt{3}}{2\\sqrt{2}}$',
                        '$-\\frac{1 + 2\\sqrt{3}}{2\\sqrt{2}}$'
                    ]
                else:
                    da = '$-\\frac{%s + \\sqrt{3}}{2\\sqrt{%s}}$' % (str(k), str(mẫu_cos_sq))
                    s_raw = [
                        '$\\frac{%s - \\sqrt{3}}{2\\sqrt{%s}}$' % (str(k), str(mẫu_cos_sq)),
                        '$\\frac{%s + \\sqrt{3}}{2\\sqrt{%s}}$' % (str(k), str(mẫu_cos_sq)),
                        '$\\frac{-%s + \\sqrt{3}}{2\\sqrt{%s}}$' % (str(k), str(mẫu_cos_sq)),
                        '$\\frac{1 + %s\\sqrt{3}}{2\\sqrt{%s}}$' % (str(k), str(mẫu_cos_sq)),
                        '$-\\frac{1 + %s\\sqrt{3}}{2\\sqrt{%s}}$' % (str(k), str(mẫu_cos_sq))
                    ]

                # Bước 4: Điều chỉnh phương án sai loại bỏ phần tử trùng đáp án đúng
                s = [item for item in s_raw if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Bước 2: Viết lại đề bài theo định dạng cấu trúc mẫu %s
                noidungcauhoi = ('''Cho $\\tan x = %s \\left(\\pi < x < \\frac{3\\pi}{2}\\right)$. Tính giá trị của $\\sin \\left(x + \\frac{\\pi}{3}\\right)$.'''
                                 % (str(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuỗi hiển thị bước kết luận cuối cùng cho loigiai
                if k == 1:
                    chuoi_kq_cuoi = '-\\frac{1 + \\sqrt{3}}{2\\sqrt{2}}'
                else:
                    chuoi_kq_cuoi = '-\\frac{%s + \\sqrt{3}}{2\\sqrt{%s}}' % (str(k), str(mẫu_cos_sq))

                # Bước 2: Viết nội dung lời giải đầy đủ, chi tiết, trình bày rõ từng bước theo sát nội dung gốc
                loigiai = ('''$\\pi < x < \\frac{3\\pi}{2}$ suy ra $\\sin x < 0, \\cos x < 0$. \\\\
            Ta có: $1 + \\tan^2 x = \\frac{1}{\\cos^2 x} \\Leftrightarrow \\cos^2 x = \\frac{1}{1 + \\tan^2 x} \\Leftrightarrow \\cos^2 x = \\frac{1}{%s} \\Leftrightarrow \\cos x = \\pm %s$ \\\\
            Do $\\cos x < 0$ nên nhận $\\cos x = %s$. \\\\
            $\\tan x = \\frac{\\sin x}{\\cos x} \\Rightarrow \\sin x = \\tan x \\cdot \\cos x = %s$. \\\\
            $\\sin \\left(x + \\frac{\\pi}{3}\\right) = \\sin x \\cdot \\cos \\frac{\\pi}{3} + \\cos x \\cdot \\sin \\frac{\\pi}{3} = \\left(%s\\right) \\cdot \\frac{1}{2} + \\left(%s\\right) \\cdot \\frac{\\sqrt{3}}{2} = %s$.'''
                           % (str(mẫu_cos_sq), str_cos_abs, str_cos_neg, str_sin_neg, str_sin_neg, str_cos_neg, chuoi_kq_cuoi))

            # Xuất câu trắc nghiệm hoàn chỉnh
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

