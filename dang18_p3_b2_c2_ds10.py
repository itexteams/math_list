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


def bt_dang18_p3_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- NGÂN HÀNG MIỀN NGHIỆM ---
                # Thêm nhiều hệ bất phương trình khác nhau vào đây.
                # Cấu trúc: 'he_bpt' (LaTeX của hệ), 'dinh' (Danh sách các đỉnh), 'ten_hinh' (Tên gọi)
                danh_sach_mien_nghiem = [
                    {
                        # Mẫu gốc của bạn
                        'he_bpt': '\\begin{cases} x+y \\ge 5 \\\\ x-2y \\le 2 \\\\ y \\le 3 \\end{cases}',
                        'dinh': [('A', 4, 1), ('B', 8, 3), ('C', 2, 3)],
                        'ten_hinh': 'tam giác $ABC$'
                    },
                    {
                        # Kịch bản 2: Tam giác có đỉnh gốc tọa độ
                        'he_bpt': '\\begin{cases} y \\ge 0 \\\\ x + y \\le 4 \\\\ x - y \\ge 0 \\end{cases}',
                        'dinh': [('O', 0, 0), ('A', 4, 0), ('B', 2, 2)],
                        'ten_hinh': 'tam giác $OAB$'
                    },
                    {
                        # Kịch bản 3: Tứ giác
                        'he_bpt': '\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le 5 \\\\ x \\le 3 \\end{cases}',
                        'dinh': [('O', 0, 0), ('A', 3, 0), ('B', 3, 2), ('C', 0, 5)],
                        'ten_hinh': 'tứ giác $OABC$'
                    },
                    {
                        # Kịch bản 4: Tam giác khác
                        'he_bpt': '\\begin{cases} y \\ge -1 \\\\ 2x + y \\le 5 \\\\ 2x - y \\ge -1 \\end{cases}',
                        'dinh': [('M', -1, -1), ('N', 3, -1), ('P', 1, 3)],
                        'ten_hinh': 'tam giác $MNP$'
                    }
                ]

                # Random chọn 1 miền nghiệm
                mien_nghiem = random.choice(danh_sach_mien_nghiem)

                # Randomize các hệ số a, b của bất phương trình ax + by + m >= 0 và khoảng [-k; k]
                a = random.randint(1, 4)
                b = random.randint(-5, -2) # Luôn âm
                k = random.randint(15, 30)

                # Xử lý hiển thị dấu cộng/trừ để không bị lỗi + - hay - -
                if b < 0:
                    ineq_str = f"{a}x - {-b}y + m \\ge 0"
                    m_ineq_str = f"m \\ge -{a}x + {-b}y"
                    F_str = f"-{a}x + {-b}y"
                else:
                    ineq_str = f"{a}x + {b}y + m \\ge 0"
                    m_ineq_str = f"m \\ge -{a}x - {b}y"
                    F_str = f"-{a}x - {b}y"

                # Xử lý nội dung tọa độ các đỉnh để đưa vào lời giải
                chuoi_toa_do_dinh = ", ".join([f"${ten}({x_v}; {y_v})$" for ten, x_v, y_v in mien_nghiem['dinh']])

                # Tính giá trị biểu thức F tại các đỉnh của miền nghiệm và tìm Max
                max_F = -float('inf')
                x_max, y_max = 0, 0

                for ten, x_v, y_v in mien_nghiem['dinh']:
                    F_val = -a*x_v - b*y_v
                    if F_val > max_F:
                        max_F = F_val
                        x_max = x_v
                        y_max = y_v

                # Tính toán số giá trị nguyên của m thỏa mãn
                kq = k - max_F + 1

                # Các đáp án trắc nghiệm
                du = [f'${kq}$']
                da = random.choice(du)

                # Tạo đáp án nhiễu
                s = [f'${kq + 1}$',
                     f'${kq + 2}$',
                     f'${kq + 3}$',
                     f'${kq - 1}$',
                     f'${kq - 2}$',
                     f'${kq - 3}$']

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = (f'''Cho hệ bất phương trình: ${mien_nghiem['he_bpt']}$ (I). Có bao nhiêu giá trị nguyên của tham số $m$ trong $[{-k}; {k}]$ để bất phương trình ${ineq_str}$ nghiệm đúng với mọi cặp số $(x;y)$ thoả mãn hệ bất phương trình (I)?''')

                # Gán đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải động theo số lượng đỉnh
                loigiai = (f'''Miền nghiệm của hệ bất phương trình (I) là miền {mien_nghiem['ten_hinh']} với {chuoi_toa_do_dinh}. \\\\
            Ta có: ${ineq_str} \\Leftrightarrow {m_ineq_str}$. \\\\
            Đặt $F = {F_str}$. \\\\
            Tính giá trị của $F = {F_str}$ tại các cặp số $(x;y)$ là toạ độ của các đỉnh {mien_nghiem['ten_hinh']} rồi so sánh các giá trị đó, ta được $F$ đạt giá trị lớn nhất bằng ${max_F}$ tại $x = {x_max}, y = {y_max}$. \\\\
            Để bất phương trình ${ineq_str}$ nghiệm đúng với mọi $x,y$ thoả mãn hệ bất phương trình đã cho thì $m \\ge \\max F$ trên miền nghiệm của hệ bất phương trình đó hay $m \\ge {max_F}$. \\\\
            Vậy trong đoạn $[{-k}; {k}]$ thì $m \\in \\{{{max_F}; {max_F+1}; \\dots; {k}\\}}$ có ${kq}$ giá trị nguyên.''')
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

