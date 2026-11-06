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


def bt_dang24_p1_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Các hàm xử lý chuỗi thông minh để triệt tiêu lỗi +- và -- cũng như hệ số 1
        def fmt_inner(b):
            if b == 1: return "+\\vec{j}"
            elif b == -1: return "-\\vec{j}"
            elif b > 0: return f"+{b}\\vec{{j}}"
            else: return f"{b}\\vec{{j}}"

        def fmt_outer(val, var):
            if val == 1: return f"+\\vec{{{var}}}"
            elif val == -1: return f"-\\vec{{{var}}}"
            elif val > 0: return f"+{val}\\vec{{{var}}}"
            else: return f"{val}\\vec{{{var}}}"

        def fmt_term_first(val, var):
            if val == 1: return f"\\vec{{{var}}}"
            elif val == -1: return f"-\\vec{{{var}}}"
            else: return f"{val}\\vec{{{var}}}"

        # Random các hệ số a, b, c, d khác 0
        # Cố định a không bằng 1 hoặc -1 để giữ nguyên cấu trúc ngoặc như đề gốc
        a = random.choice([2, 3, 4, 5, -2, -3, -4, -5])
        b = random.choice([i for i in range(-5, 6) if i != 0])
        c = random.choice([i for i in range(-5, 6) if i != 0])
        d = random.choice([i for i in range(-5, 6) if i != 0])

        # Tọa độ vector AO
        x_AO = a
        y_AO = a * b + d
        z_AO = c

        # Tọa độ điểm A (trái dấu với AO)
        x_A, y_A, z_A = -x_AO, -y_AO, -z_AO

        # Chuỗi biểu thức đề bài và biểu thức đã rút gọn
        bieu_thuc_de = f"{a}(\\vec{{i}}{fmt_inner(b)}){fmt_outer(c, 'k')}{fmt_outer(d, 'j')}"
        bieu_thuc_rut_gon = f"{fmt_term_first(x_AO, 'i')}{fmt_outer(y_AO, 'j')}{fmt_outer(z_AO, 'k')}"

        # Xây dựng đáp án đúng
        da_dung_tuple = (x_A, y_A, z_A)

        # Xây dựng các đáp án nhiễu theo bẫy logic
        distractors = [
            (x_AO, y_AO, -z_AO),  # Quên đổi dấu vector OA
            (x_AO, d, z_AO),      # Quên nhân phân phối a vào b
            (x_AO, z_AO, d),      # Nhầm lẫn thứ tự tọa độ j, k
            (x_AO, y_AO, z_AO),   # Nhầm hoàn toàn A thành AO
            (-x_AO, -y_AO, z_AO)  # Đổi dấu nhầm/sót
        ]

        # Lọc các đáp án nhiễu để đảm bảo không trùng với đáp án đúng và không trùng nhau
        valid_dist = []
        for dt in distractors:
            if dt != da_dung_tuple and dt not in valid_dist:
                valid_dist.append(dt)

        # Bổ sung ngẫu nhiên nếu bị thiếu (phòng hờ)
        while len(valid_dist) < 3:
            new_d = (randint(-10, 10), randint(-10, 10), randint(-10, 10))
            if new_d != da_dung_tuple and new_d not in valid_dist:
                valid_dist.append(new_d)

        da_dung_str = f"({x_A}; {y_A}; {z_A})"
        da_sai1_str = f"({valid_dist[0][0]}; {valid_dist[0][1]}; {valid_dist[0][2]})"
        da_sai2_str = f"({valid_dist[1][0]}; {valid_dist[1][1]}; {valid_dist[1][2]})"
        da_sai3_str = f"({valid_dist[2][0]}; {valid_dist[2][1]}; {valid_dist[2][2]})"

        # Các đáp án trắc nghiệm
        du = ['$%s$' % (da_dung_str)]
        da = random.choice(du)

        s = [
             '$%s$' % (da_sai1_str),
             '$%s$' % (da_sai2_str),
             '$%s$' % (da_sai3_str)
            ]

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Câu hỏi
        noidungcauhoi = ('Trong không gian $Oxyz$, cho vectơ $\\overrightarrow{AO} = %s$. Tọa độ của điểm $A$ là' % (bieu_thuc_de))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Ta có: $\\overrightarrow{AO} = %s = %s \\Leftrightarrow A(%s; %s; %s)$.''' % (bieu_thuc_de, bieu_thuc_rut_gon, x_A, y_A, z_A))


    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\n\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

