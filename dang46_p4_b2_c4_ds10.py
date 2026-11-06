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


def bt_dang46_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các giá trị để bài toán đẹp
                # Hàm số y = 4x^2 - 4mx + m^2 - 2m
                # Đỉnh x_I = m/2
                # Đoạn xét [a, b] = [-2, 0]
                a_val, b_val = -2, 0
                target_min = random.randint(1, 5) # Giá trị nhỏ nhất đề bài yêu cầu (ví dụ: 3)

                # Tạo nội dung câu hỏi
                noidungcauhoi = (r'''Cho hàm số $y = f(x) = 4x^2 - 4mx + m^2 - 2m$. Tìm giá trị của tham số $m$ sao cho hàm số đạt giá trị nhỏ nhất trên đoạn $[%s;%s]$ bằng $%s$.'''
                                 %(latex(a_val), latex(b_val), latex(target_min)))

                # --- GIẢI CHI TIẾT ĐỂ LẤY ĐÁP ÁN ĐÚNG ---
                m = symbols('m')
                f_x = 4*x**2 - 4*m*x + m**2 - 2*m
                x_I = m/2

                da_dung_list = []

                # Trường hợp 1: m/2 < -2 <=> m < -4
                # f(x) đồng biến trên [-2, 0] => min = f(-2)
                f_neg2 = 4*(-2)**2 - 4*m*(-2) + m**2 - 2*m # m^2 + 6m + 16
                sol1 = solve(f_neg2 - target_min, m)
                for s in sol1:
                    if s.is_real and s < -4:
                        da_dung_list.append(s)

                # Trường hợp 2: -2 <= m/2 <= 0 <=> -4 <= m <= 0
                # min = f(m/2) = -2m
                f_vertex = -2*m
                sol2 = solve(f_vertex - target_min, m)
                for s in sol2:
                    if s.is_real and -4 <= s <= 0:
                        da_dung_list.append(s)

                # Trường hợp 3: m/2 > 0 <=> m > 0
                # f(x) nghịch biến trên [-2, 0] => min = f(0)
                f_0 = m**2 - 2*m
                sol3 = solve(f_0 - target_min, m)
                for s in sol3:
                    if s.is_real and s > 0:
                        da_dung_list.append(s)

                # Định dạng đáp án đúng
                if not da_dung_list:
                    # Nếu vô tình rơi vào bộ số không có nghiệm (hiếm), fix cứng để code không lỗi
                    da_dung_str = r'm \in \emptyset'
                else:
                    # Chuyển các giá trị sang latex, sắp xếp và đưa vào tập hợp
                    da_dung_list = sorted(list(set(da_dung_list)))
                    items = [latex(v) for v in da_dung_list]
                    da_dung_str = r'm \in \left\{ ' + "; ".join(items) + r' \right\}'

                # --- TẠO PHƯƠNG ÁN SAI (B4: Không trùng đáp án đúng) ---
                s = [
                    r'$m \in \left\{ -1; 3 \right\}$',
                    r'$m \in \left\{ -\frac{3}{2}; 1 \right\}$',
                    r'$m \in \left\{ \frac{3}{2}; 3 \right\}$',
                    r'$m \in \left\{ -2; 4 \right\}$',
                    r'$m \in \left\{ -\frac{1}{2} \right\}$'
                ]
                # Lọc bỏ nếu lỡ trùng
                s = [item for item in s if item != f'${da_dung_str}$']
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung lời giải chi tiết (B2: Viết y hệt mẫu ảnh)
                loigiai = (r'''Ta có $a = 4 > 0$ nên đồ thị hàm số là một parabol có bề lõm hướng lên và có hoành độ đỉnh $x_I = \frac{m}{2}$. \\
            - Nếu $\frac{m}{2} < %s \Leftrightarrow m < %s$ thì $x_I < %s < %s$. Suy ra $f(x)$ đồng biến trên đoạn $[%s;%s]$. \\
            Do đó $\min_{[%s;%s]} f(x) = f(%s) = m^2 + 6m + 16$. \\
            Theo yêu cầu bài toán: $m^2 + 6m + 16 = %s$ (vô nghiệm). \\
            - Nếu $%s \le \frac{m}{2} \le %s \Leftrightarrow %s \le m \le %s$ thì $x_I \in [%s;%s]$. Suy ra $f(x)$ đạt giá trị nhỏ nhất tại $x_I = \frac{m}{2}$. \\
            Do đó $\min_{[%s;%s]} f(x) = f\left(\frac{m}{2}\right) = -2m$. \\
            Theo yêu cầu bài toán $-2m = %s \Leftrightarrow m = %s$ (thỏa mãn $%s \le m \le %s$). \\
            - Nếu $\frac{m}{2} > %s \Leftrightarrow m > %s$ thì $x_I > %s > %s$. Suy ra $f(x)$ nghịch biến trên đoạn $[%s;%s]$. \\
            Do đó $\min_{[%s;%s]} f(x) = f(%s) = m^2 - 2m$. \\
            Theo yêu cầu bài toán: $m^2 - 2m = %s \Leftrightarrow \left[\begin{aligned} & m = -1 \\ & m = 3 \end{aligned}\right. \Leftrightarrow m = 3$ (Vì $m > 0$). \\
            Từ các trường hợp trên, ta được $%s$.''' 
                %(latex(a_val), latex(2*a_val), latex(a_val), latex(b_val), latex(a_val), latex(b_val), 
                  latex(a_val), latex(b_val), latex(a_val), latex(target_min),
                  latex(a_val), latex(b_val), latex(2*a_val), latex(2*b_val), latex(a_val), latex(b_val),
                  latex(a_val), latex(b_val), latex(target_min), latex(Rational(-target_min, 2)), latex(2*a_val), latex(2*b_val),
                  latex(b_val), latex(2*b_val), latex(b_val), latex(a_val), latex(a_val), latex(b_val),
                  latex(a_val), latex(b_val), latex(b_val), latex(target_min), da_dung_str))

                # Đóng gói đáp án
                da_d = r'\True $' + da_dung_str + r'$'
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

