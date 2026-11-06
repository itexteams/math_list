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


def bt_dang35_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết lập bộ tham số random để tạo ra các câu hỏi tương tự hình mẫu bài toán gốc
                # Bộ dữ liệu gồm: (chuỗi latex vế trái phương trình, giá trị cos(2x), phân số alpha_v (không chứa pi) để tính toán hữu tỷ)
                list_data = [
                    ('2\\cos 2x - 1 = 0', '\\frac{1}{2}', Rational(1, 3)),          # alpha = pi/3
                    ('2\\cos 2x - \\sqrt{2} = 0', '\\frac{\\sqrt{2}}{2}', Rational(1, 4)),  # alpha = pi/4
                    ('2\\cos 2x - \\sqrt{3} = 0', '\\frac{\\sqrt{3}}{2}', Rational(1, 6))   # alpha = pi/6
                ]

                pt_goc, val_cos, alpha_v = random.choice(list_data)

                alpha = alpha_v * pi
                x_basic = alpha / 2
                x_basic_v = alpha_v / 2  # Phần số hữu tỷ đứng trước pi của nghiệm cơ bản (x = alpha/2)

                # Tìm tất cả nghiệm trong đoạn [0, \pi] để xác định nghiệm lớn nhất
                nghiem_trong_doan = []

                # Họ 1: x = alpha/2 + k*pi
                for k in [-1, 0, 1, 2]:
                    val = x_basic + k*pi
                    if 0 <= val <= pi:
                        nghiem_trong_doan.append(val)

                # Họ 2: x = -alpha/2 + k*pi
                for k in [-1, 0, 1, 2]:
                    val = -x_basic + k*pi
                    if 0 <= val <= pi:
                        nghiem_trong_doan.append(val)

                # Lấy nghiệm lớn nhất
                max_nghiem = max(nghiem_trong_doan)

                # Đáp án đúng dạng chuỗi
                da = '$x = %s$' % (latex(max_nghiem))

                # Tạo các phương án nhiễu (sai) không trùng đáp án đúng
                list_s = [pi, 5*pi/6, 2*pi/3, 11*pi/12, 3*pi/4, pi/2, pi/3, pi/4, pi/6]
                s = []
                for ng in list_s:
                    if ng != max_nghiem:
                        s.append('$x = %s$' % (latex(ng)))

                # Trích xuất 3 đáp án sai ngẫu nhiên
                s = list(set(s))
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Nghiệm lớn nhất của phương trình $%s$ trong đoạn $\\left[ 0;\\pi  \\right]$ là'''
                                 % (pt_goc))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Biên soạn chuỗi latex cho x_basic
                x_basic_str = latex(x_basic)

                # SỬA LỖI TẠI ĐÂY: Sử dụng alpha_v (phần số hữu tỷ đã cô lập pi) để tính toán với Rational vô tư
                # 0 <= alpha/2 + k*pi <= pi  <=>  -alpha_v/2 <= k <= 1 - alpha_v/2
                k1_min_val = -x_basic_v
                k1_max_val = Rational(1, 1) - x_basic_v
                k1_min = latex(k1_min_val)
                k1_max = latex(k1_max_val)

                # 0 <= -alpha/2 + k*pi <= pi  <=>  alpha_v/2 <= k <= 1 + alpha_v/2
                k2_min_val = x_basic_v
                k2_max_val = Rational(1, 1) + x_basic_v
                k2_min = latex(k2_min_val)
                k2_max = latex(k2_max_val)

                # Liệt kê tập nghiệm tìm được sau khi chặn k
                str_nghiem_tim_duoc = ''
                for ng in sorted(list(set(nghiem_trong_doan))):
                    str_nghiem_tim_duoc += '& x = %s \\\\ ' % (latex(ng))

                # Nội dung lời giải chi tiết y hệt từng bước trong ảnh mẫu
                loigiai = ('''Phương trình $%s \\Leftrightarrow \\cos 2x = %s \\Leftrightarrow \\left[ \\begin{aligned} & 2x = \\frac{\\pi}{%s} + k2\\pi  \\\\ & 2x = -\\frac{\\pi}{%s} + k2\\pi  \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & x = %s + k\\pi  \\\\ & x = -%s + k\\pi  \\end{aligned} \\right.$ \\\\
                           Xét $x \\in \\left[ 0;\\pi  \\right] \\Leftrightarrow \\left[ \\begin{aligned} & 0 \\le %s + k\\pi  \\le \\pi  \\\\ & 0 \\le -%s + k\\pi  \\le \\pi  \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & %s \\le k \\le %s \\\\ & %s \\le k \\le %s \\end{aligned} \\right.$ mà $k \\in \\mathbb{Z}$ suy ra $\\left[ \\begin{aligned} & k=0 \\\\ & k=1 \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} %s \\end{aligned} \\right.$ \\\\
                           Vậy nghiệm lớn nhất của phương trình $%s$ trong đoạn $\\left[ 0;\\pi  \\right]$ là $x = %s$.'''
                           % (pt_goc, val_cos, latex(Rational(1, alpha_v)), latex(Rational(1, alpha_v)), x_basic_str, x_basic_str,
                              x_basic_str, x_basic_str, k1_min, k1_max, k2_min, k2_max,
                              str_nghiem_tim_duoc, pt_goc, latex(max_nghiem)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

