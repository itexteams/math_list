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


def bt_dang42_p1_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến danh sách dạng bài
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # P: Số tiền ban đầu (triệu đồng)
                P_val = random.randint(50, 200) 
                # r: Lãi suất hàng tháng (%)
                r_val = random.choice([0.5, 0.6, 0.7, 0.8, 0.9])
                r = r_val / 100
                # a: Số tiền gửi thêm mỗi tháng từ tháng thứ 2 (triệu đồng)
                a_val = random.randint(1, 10)
                # n_year: Số năm gửi
                n_year = random.randint(2, 4)
                n = n_year * 12 # Tổng số tháng

                # --- Tính toán theo công thức trong hình ---
                # T1: Tiền từ 100 triệu ban đầu sau n tháng
                # T1 = P * (1 + r)^n
                T1_val = P_val * (1 + r)**n * 10**6

                # T2: Tiền từ các khoản gửi thêm 2 triệu mỗi tháng (từ tháng 2 đến tháng n => n-1 tháng)
                # Công thức: T2 = a/r * [(1+r)^(n-1) - 1] * (1+r)
                T2_val = (a_val * 10**6 / r) * ((1 + r)**(n - 1) - 1) * (1 + r)

                # Tổng tiền T = T1 + T2
                T_total = T1_val + T2_val

                # Làm tròn đến hàng nghìn
                kq_final = int(Decimal(T_total).quantize(Decimal('1000'), rounding=ROUND_HALF_UP))

                # Định dạng hiển thị số tiền (ví dụ: 171.761.000)
                def format_money(n):
                    return "{:,}".format(n).replace(",", ".")

                kq_str = format_money(kq_final)

                # --- B4: Điều chỉnh các phương án sai ---
                du = [f"{kq_str}"]
                da = random.choice(du)

                # Tạo các đáp án nhiễu (sai lệch vài triệu)
                s = [
                    format_money(kq_final + 1000000),
                    format_money(kq_final - 1000000),
                    format_money(kq_final + 500000),
                    format_money(kq_final - 500000),
                    format_money(kq_final + 2000000),
                    format_money(kq_final - 2000000),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (f"Ông Nam gửi {P_val} triệu đồng vào một ngân hàng với lãi suất {r_val}\\%/tháng. "
                                 f"Biết rằng nếu không rút tiền ra khỏi ngân hàng thì cứ sau mỗi tháng số tiền lãi sẽ được nhập vào gốc để tính lãi cho tháng tiếp theo "
                                 f"và từ tháng thứ hai trở đi, mỗi tháng ông gửi thêm vào tài khoản với số tiền {a_val} triệu đồng. "
                                 f"Hỏi sau đúng {n_year} năm số tiền ông nhận được cả gốc lẫn lãi là bao nhiêu? "
                                 f"Biết rằng trong suốt thời gian gửi lãi suất không thay đổi và ông không rút tiền ra (kết quả được làm tròn đến hàng nghìn).")

                # Các đáp án
                da_d = '\\True ' + f"${da}$"
                da_s1 = f"${das1}$"
                da_s2 = f"${das2}$"
                da_s3 = f"${das3}$"

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải (B2: Viết lại y hệt mẫu) ---
                loigiai = (f"Với {P_val} triệu ban đầu số tiền cả lãi và gốc thu được sau {n_year} năm ({n} tháng) là:\\\\"
                           f"$T_1 = {P_val} \\cdot (1 + {r_val}\\%)^{{{n}}} \\cdot 10^6 \\approx {format_money(int(T1_val))}$\\\\"
                           f"Mỗi tháng tiếp theo gửi {a_val} triệu (từ tháng thứ 2) thì tổng số tiền cả lãi và gốc của các khoản này là:\\\\"
                           f"$T_2 = \\frac{{{a_val}}}{{{r}}} \\cdot \\left[ (1 + {r})^{{{n-1}}} - 1 \\right] \\cdot (1 + {r}) \\cdot 10^6 \\approx {format_money(int(T2_val))}$\\\\"
                           f"Vậy tổng số tiền là $T = T_1 + T_2 \\approx {kq_str}$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

