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


def bt_dang16_p1_b2_c2_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số công nhân (tần số) cho từng nhóm
                f1 = random.randint(2, 8)
                f2 = random.randint(4, 12)
                f3 = random.randint(8, 20)
                f4 = random.randint(10, 25)
                f5 = random.randint(5, 15)

                n = f1 + f2 + f3 + f4 + f5

                # Giá trị đại diện (trung điểm) của các nhóm
                x1, x2, x3, x4, x5 = 15, 25, 35, 45, 55

                # Tính giá trị trung bình
                sum_x = f1 * x1 + f2 * x2 + f3 * x3 + f4 * x4 + f5 * x5
                mean = sum_x / n

                # Tính phương sai
                sum_x2 = f1 * (x1**2) + f2 * (x2**2) + f3 * (x3**2) + f4 * (x4**2) + f5 * (x5**2)
                variance = (sum_x2 / n) - (mean**2)

                # Tính độ lệch chuẩn
                std_dev = math.sqrt(variance)

                # Hàm format số liệu để hiển thị chuẩn Việt Nam (thay dấu chấm bằng phẩy)
                def fmt_val(val):
                    if isinstance(val, int) or val.is_integer():
                        return str(int(val))
                    # Giới hạn số thập phân để tránh chuỗi quá dài trong lời giải
                    v_str = f"{val:.4f}".rstrip('0').rstrip('.')
                    return v_str.replace('.', ',')

                mean_str = fmt_val(mean)
                var_str = fmt_val(variance)

                # Độ lệch chuẩn được làm tròn tới hàng phần chục theo yêu cầu đề bài
                std_dev_round = Decimal(str(std_dev)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                std_dev_str = str(std_dev_round).replace('.', ',')

                # Tạo các phương án nhiễu (sai số ngẫu nhiên, chưa căn hoặc lấy nhầm số trung bình)
                wrong_set = set()
                wrong_set.add(str(Decimal(str(variance)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')) # Quên căn (s^2)
                wrong_set.add(str(Decimal(str(mean)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','))     # Nhầm giá trị trung bình
                wrong_set.add(str(Decimal(str(std_dev + random.choice([0.5, 1.2, -0.6, -1.1]))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','))
                wrong_set.add(str(Decimal(str(std_dev + random.choice([0.4, 0.8, -0.4, -0.8]))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','))

                wrong_list = []
                for w in wrong_set:
                    if w != std_dev_str and len(wrong_list) < 3:
                        wrong_list.append(w)

                # Bổ sung thêm nếu list nhiễu chưa đủ 3
                while len(wrong_list) < 3:
                    w_fake = str(Decimal(str(std_dev + random.uniform(1.5, 3.0))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if w_fake != std_dev_str and w_fake not in wrong_list:
                        wrong_list.append(w_fake)

                random.shuffle(wrong_list)

                # Gán các đáp án
                da_d = ('\\True $%s$' % std_dev_str)
                da_s1 = ('$%s$' % wrong_list[0])
                da_s2 = ('$%s$' % wrong_list[1])
                da_s3 = ('$%s$' % wrong_list[2])

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Câu hỏi
                noidungcauhoi = ('''Một công ty thống kê lương của nhân viên theo tuần (đơn vị: USD) theo bảng sau:
            \\begin{center}
            \\begin{tabular}{|c|c|c|c|c|c|}
            \\hline
            Lương theo tuần (USD) & $[10;20)$ & $[20;30)$ & $[30;40)$ & $[40;50)$ & $[50;60]$ \\\\
            \\hline
            Số công nhân & %s & %s & %s & %s & %s \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Độ lệch chuẩn của mẫu số liệu này (làm tròn tới hàng phần chục) là''' 
                                 % (f1, f2, f3, f4, f5))

                # Lời giải chi tiết
                loigiai = ('''Ta có cỡ mẫu $n = %s$.\\\\
            Giá trị trung bình của mẫu số liệu: $\\overline{x} = \\frac{1}{%s}(%s \\cdot 15 + %s \\cdot 25 + %s \\cdot 35 + %s \\cdot 45 + %s \\cdot 55) = %s$.\\\\
            Phương sai của mẫu số liệu ghép nhóm:\\\\
            $s^2 = \\frac{1}{%s}(%s \\cdot 15^2 + %s \\cdot 25^2 + %s \\cdot 35^2 + %s \\cdot 45^2 + %s \\cdot 55^2) - %s^2 = %s$.\\\\
            Độ lệch chuẩn của mẫu số liệu ghép nhóm là: $s = \\sqrt{s^2} = \\sqrt{%s} \\approx %s$.'''
                           % (n, 
                              n, f1, f2, f3, f4, f5, mean_str, 
                              n, f1, f2, f3, f4, f5, mean_str, var_str, 
                              var_str, std_dev_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

