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


def bt_dang13_p4_b1_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số n dưới dấu căn (loại bỏ các số chính phương)
                perfect_squares = [4, 9, 16, 25, 36, 49, 64, 81]
                n = random.randint(2, 99)
                while n in perfect_squares:
                    n = random.randint(2, 99)

                # Tính căn bậc 2 của n
                val = math.sqrt(n)

                # Chuỗi giá trị đầy đủ để hiển thị trong lời giải (lấy khoảng 8 chữ số thập phân)
                val_full = str(val).replace('.', ',')[:10]
                str_val = f"{val:.10f}"
                phan_thap_phan = str_val.split('.')[1]

                # --- RANDOM YÊU CẦU LÀM TRÒN ---
                options_precision = [
                    (1, 'hàng phần mười', '0.1'),
                    (2, 'hàng phần trăm', '0.01'),
                    (3, 'hàng phần nghìn', '0.001')
                ]
                p, target_text, quantize_str = random.choice(options_precision)

                # Xác định các chữ số để viết lời giải
                chu_so_hang_lam_tron = phan_thap_phan[p-1]
                chu_so_ke_tiep = int(phan_thap_phan[p])

                # Kết quả đúng
                val_rounded = Decimal(float(val)).quantize(Decimal(quantize_str), rounding=ROUND_HALF_UP)
                kq = str(val_rounded).replace('.', ',')

                # --- TẠO CÁC PHƯƠNG ÁN NHIỄU ---
                options_set = set()

                # Nhiễu 1: Làm tròn sai hướng (Cộng thêm hoặc trừ đi 1 đơn vị ở hàng làm tròn cuối cùng)
                offset_val = Decimal(quantize_str)
                if chu_so_ke_tiep >= 5:
                    dist1 = str(val_rounded - offset_val).replace('.', ',')
                else:
                    dist1 = str(val_rounded + offset_val).replace('.', ',')
                options_set.add(dist1)

                # Nhiễu 2 & 3: Làm tròn sai bậc (thiếu hoặc thừa số thập phân)
                if p == 1:
                    dist2 = str(Decimal(float(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    dist3 = str(Decimal(float(val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                elif p == 2:
                    dist2 = str(Decimal(float(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    dist3 = str(Decimal(float(val)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).replace('.', ',')
                else: # p == 3
                    dist2 = str(Decimal(float(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    dist3 = str(Decimal(float(val)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)).replace('.', ',')

                options_set.add(dist2)
                options_set.add(dist3)

                # Phòng hờ trùng lặp đáp án, thêm nhiễu ngẫu nhiên
                offsets_pool = [2 * float(offset_val), -2 * float(offset_val), 3 * float(offset_val), -3 * float(offset_val)]
                while len(options_set) < 3:
                    random_offset = random.choice(offsets_pool)
                    dist_fallback = str(Decimal(float(val_rounded) + random_offset).quantize(Decimal(quantize_str))).replace('.', ',')
                    if dist_fallback != kq:
                        options_set.add(dist_fallback)

                options_list = list(options_set)[:3]

                # Câu hỏi
                noidungcauhoi = ('''Tìm giá trị gần đúng của $\\sqrt{%s}$ đến %s (dùng máy tính bỏ túi).''' % (n, target_text))

                # Các đáp án
                da_d = ('\\True $%s$' % (kq))
                da_s1 = ('$%s$' % (options_list[0]))
                da_s2 = ('$%s$' % (options_list[1])) 
                da_s3 = ('$%s$' % (options_list[2])) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Logic lời giải
                dau = "<" if chu_so_ke_tiep < 5 else "\\ge"
                loigiai=('''Ta có: $\\sqrt{%s} = %s\\dots$\\\\
                Cần lấy chính xác đến %s nên ta phải lấy $%s$ chữ số thập phân. Vì đứng sau số $%s$ ở %s là số $%s %s 5$ nên theo nguyên lý làm tròn ta được kết quả là $%s$.'''
                         % (n, val_full, target_text, p, chu_so_hang_lam_tron, target_text, chu_so_ke_tiep, dau, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

