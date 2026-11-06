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


def bt_dang36_p1_b3_c5_ds11(self):
            # Khai báo biến
            # --- BƯỚC 1 & 3: KHỞI TẠO VÀ RANDOM DỮ LIỆU ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # A: Giá niêm yết ban đầu (từ 500 triệu đến 1.5 tỷ, bước nhảy 10 triệu)
                A = random.randrange(500, 1501, 10) * 1000000 

                # r: Tỷ lệ giảm giá hàng năm (từ 1% đến 5%)
                r = random.randint(2, 5)

                # n: Số năm dự kiến và năm cần tính
                nam_bat_dau = 2025
                so_nam_du_kien = 10
                n = random.randint(3, 7) # Tính sau n năm (ví dụ từ 2023 đến 2027)
                nam_can_tinh = nam_bat_dau + n

                # --- BƯỚC 2: TÍNH TOÁN LỜI GIẢI ---
                # Công thức: An = A * (1 - r/100)^n
                gia_tri_chinh_xac = A * ((1 - r/100)**n)

                # Làm tròn đến hàng nghìn (chia 1000, làm tròn, rồi nhân lại 1000)
                kq_float = float(Decimal(gia_tri_chinh_xac / 1000).quantize(Decimal('1'), rounding=ROUND_HALF_UP)) * 1000

                # Định dạng hiển thị số tiền có dấu chấm phân cách hàng nghìn (kiểu VN: 750.000.000)
                def format_vn(ng):
                    return "{:,.0f}".format(ng).replace(',', '.')

                da_dung = format_vn(kq_float)

                # --- BƯỚC 4: TẠO CÁC PHƯƠNG ÁN SAI (KHÔNG TRÙNG ĐÁP ÁN ĐÚNG) ---
                s = set()
                while len(s) < 3:
                    # Tạo sai số bằng cách cộng/trừ các khoảng 500.000 hoặc 1.000.000
                    sai_so = random.choice([-2000000, -1000000, 1000000, 2000000, 5000000, -5000000])
                    phuong_an_sai = format_vn(kq_float + sai_so)
                    if phuong_an_sai != da_dung:
                        s.add(phuong_an_sai)

                list_sai = list(s)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Năm $%s$ một hãng xe niêm yết giá bán loại xe X là $%s$ đồng và dự định trong $%s$ năm tiếp theo, mỗi năm giảm $%s\\%%$ giá bán so với giá bán của năm liền trước. Theo dự định đó, năm $%s$ hãng xe ô tô niêm yết giá bán loại xe X là bao nhiêu (kết quả làm tròn đến hàng nghìn)?'''
                                 %(latex(nam_bat_dau), format_vn(A), latex(so_nam_du_kien), latex(r), latex(nam_can_tinh)))

                # Các đáp án
                da_d = '\\True $' + da_dung + '$ đồng'
                da_s1 = '$' + list_sai[0] + '$ đồng'
                da_s2 = '$' + list_sai[1] + '$ đồng'
                da_s3 = '$' + list_sai[2] + '$ đồng'

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Nội dung lời giải chi tiết
                loigiai = ('''Giá xe năm $%s$ là $A = %s$.\\\\
                             Giá xe sau $1$ năm (năm $%s$) là $A_1 = A - A \\cdot r = A(1-r)$.\\\\
                             Tương tự, giá xe sau $%s$ năm (năm $%s$) là:\\\\
                             $A_{%s} = A(1-r)^{%s} = %s \\cdot \\left(1 - \\frac{%s}{100}\\right)^{%s} \\approx %s$ đồng.'''
                           %(latex(nam_bat_dau), format_vn(A), 
                             latex(nam_bat_dau + 1), 
                             latex(n), latex(nam_can_tinh), 
                             latex(n), latex(n), format_vn(A), latex(r), latex(n), da_dung))

            # Xuất kết quả theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

