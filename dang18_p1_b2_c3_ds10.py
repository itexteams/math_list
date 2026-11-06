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


def bt_dang18_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng phần tử từ 8 đến 20
                n_items = random.randint(8, 20)

                # Random các chỉ số IQ từ 60 đến 120
                data = [random.randint(60, 120) for _ in range(n_items)]

                # Cố ý tạo giá trị lặp lại để tạo mốt (giống số 74 trong đề gốc)
                dup_val = random.choice(data)
                data[1] = dup_val
                if n_items > 10:
                    data[n_items - 2] = dup_val

                # Trộn ngẫu nhiên dãy số liệu ban đầu
                random.shuffle(data)

                # Xử lý chuỗi hiển thị đề bài (ngắt dòng mỗi 10 phần tử)
                data_str_parts = []
                for i in range(0, n_items, 10):
                    data_str_parts.append(" \\quad ".join(map(str, data[i:i+10])))
                data_str = " \\\\[5pt]\n".join(data_str_parts)

                # Sắp xếp số liệu để tìm trung vị
                sorted_data = sorted(data)
                sorted_str_parts = []
                for i in range(0, n_items, 10):
                    sorted_str_parts.append(" \\quad ".join(map(str, sorted_data[i:i+10])))
                sorted_str = " \\\\[5pt]\n".join(sorted_str_parts)

                # Phân loại logic tìm trung vị (chẵn / lẻ)
                mid_idx = n_items // 2
                s_vals = set() # Chứa các đáp án nhiễu

                if n_items % 2 != 0:
                    # Trường hợp N Lẻ: lấy phần tử ở chính giữa
                    med = sorted_data[mid_idx]
                    kq = str(med)
                    loigiai_med = f"Dãy trên có ${n_items}$ giá trị nên ta lấy giá trị ở giữa là ${kq}$."

                    # Bẫy học sinh lấy nhầm giá trị bên cạnh
                    s_vals.add(sorted_data[mid_idx - 1])
                    s_vals.add(sorted_data[mid_idx + 1])
                else:
                    # Trường hợp N Chẵn: lấy trung bình cộng 2 phần tử ở giữa
                    v1 = sorted_data[mid_idx - 1]
                    v2 = sorted_data[mid_idx]
                    med = (v1 + v2) / 2

                    # Định dạng kết quả (bỏ .0 nếu là số nguyên)
                    if float(med).is_integer():
                        kq = str(int(med))
                    else:
                        kq = str(round(med, 1)).replace('.', ',')

                    loigiai_med = f"Dãy trên có ${n_items}$ giá trị (là số chẵn) nên ta lấy trung bình cộng $2$ giá trị ở giữa là $\\frac{{{v1} + {v2}}}{{2}} = {kq}$."

                    # Bẫy học sinh chỉ lấy 1 trong 2 giá trị ở giữa
                    s_vals.add(v1)
                    s_vals.add(v2)

                da = f'${kq}$'

                # Tạo thêm các đáp án nhiễu dùng chung
                s_vals.add(sorted_data[-1]) # Bẫy: lấy giá trị lớn nhất (giống 90 trong đề gốc)
                s_vals.add(sorted_data[0]) # Bẫy: lấy giá trị nhỏ nhất
                s_vals.add(dup_val) # Bẫy: nhầm sang mốt (mode)

                # Loại bỏ đáp án đúng khỏi tập nhiễu (nếu có)
                s_vals = {v for v in s_vals if v != med and int(v) != med}

                # Bổ sung nhiễu ngẫu nhiên xung quanh nếu chưa đủ 3
                while len(s_vals) < 3:
                    cand = med + random.choice([-2, 2, -3, 3, -4, 4])
                    if cand != med and cand not in s_vals:
                        s_vals.add(cand)

                # Lấy đúng 3 đáp án nhiễu và định dạng
                s_vals_list = list(s_vals)[:3]
                s = []
                for v in s_vals_list:
                    if float(v).is_integer():
                        s.append(f'${int(v)}$')
                    else:
                        s.append(f'${str(round(v, 1)).replace(".", ",")}$')

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = f'''Chỉ số IQ của một nhóm học sinh: 
            \\begin{{center}}
            {data_str}
            \\end{{center}}
            Số trung vị của mẫu số liệu là'''

                # Gán đáp án vào danh sách
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = f'''Sắp xếp mẫu số liệu theo thứ tự không giảm là: 
            \\begin{{center}}
            {sorted_str}
            \\end{{center}}
            {loigiai_med}'''

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

