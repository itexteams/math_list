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


def bt_dang23_p1_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            # Hàm hỗ trợ định dạng số
            def format_num(num):
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            if dang=='1':
                n = 12

                while True:
                    # B3: Thuật toán tạo số liệu luôn có đúng 2 giá trị bất thường ở phía trên
                    # 10 giá trị cân nặng bình thường (kg)
                    core_data = [random.randint(40, 55) for _ in range(10)]

                    # Thêm 2 giá trị cực lớn (outlier)
                    outlier_1 = random.randint(70, 85)
                    outlier_2 = random.randint(outlier_1 + 1, 95)

                    data = core_data + [outlier_1, outlier_2]
                    data.sort()

                    # B2: Tính toán Q1, Q2, Q3 theo quy tắc n=12
                    q2_val = (data[5] + data[6]) / 2
                    q1_val = (data[2] + data[3]) / 2
                    q3_val = (data[8] + data[9]) / 2

                    iqr_val = q3_val - q1_val
                    if iqr_val == 0:
                        continue

                    lower_limit = q1_val - 1.5 * iqr_val
                    upper_limit = q3_val + 1.5 * iqr_val

                    # Kiểm tra xem có đúng 2 giá trị bất thường ở phía trên và 0 ở phía dưới không
                    outliers = [val for val in data if val < lower_limit or val > upper_limit]
                    if len(outliers) == 2 and outliers[0] == outlier_1 and outliers[1] == outlier_2:
                        break

                # Xáo trộn số liệu để xuất đề bài
                data_raw = data.copy()
                random.shuffle(data_raw)
                data_str_de = " \\quad ".join(map(str, data_raw))
                sorted_data_str = " \\quad ".join(map(str, data))

                # Định dạng các text phép tính phân số nếu cần
                q1_str = f"{format_num(q1_val)}" if data[2] == data[3] else f"\\frac{{{data[2]} + {data[3]}}}{{2}} = {format_num(q1_val)}"
                q2_str = f"{format_num(q2_val)}" if data[5] == data[6] else f"\\frac{{{data[5]} + {data[6]}}}{{2}} = {format_num(q2_val)}"
                q3_str = f"{format_num(q3_val)}" if data[8] == data[9] else f"\\frac{{{data[8]} + {data[9]}}}{{2}} = {format_num(q3_val)}"

                # Chuẩn bị đáp án đúng
                ans_correct_str = f"{outlier_1} và {outlier_2}"
                du = [ans_correct_str]
                da = random.choice(du)

                # Sinh đáp án nhiễu
                min_val = str(data[0])

                s_pool = [
                    str(outlier_1),
                    str(outlier_2),
                    f"{min_val} và {outlier_2}",
                    f"{min_val} và {outlier_1}",
                    str(data[-3]) # Lấy giá trị lớn thứ 3 (không phải outlier)
                ]

                s = []
                for opt in s_pool:
                    if opt not in du and opt not in s:
                        s.append(opt)

                random.shuffle(s)
                das1 = str(s[0])
                das2 = str(s[1])
                das3 = str(s[2])

                # Random thông tin lớp học
                to_num = random.randint(1, 4)
                lop_name = random.choice(["10A", "10B", "10C", "10D"])

                # Câu hỏi
                noidungcauhoi = ('''Cân nặng (đơn vị kg) của 12 em học sinh Tổ %s lớp %s được cho bởi mẫu liệu sau:
            \\begin{center}
            %s
            \\end{center}
            Các giá trị bất thường của mẫu số liệu trên bằng cách sử dụng biểu đồ hộp là''' 
                                 % (to_num, lop_name, data_str_de))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Sắp xếp mẫu số liệu trên theo thứ tự không giảm ta được
            \\begin{center}
            %s
            \\end{center}
            Từ mẫu số liệu ta tính được $Q_2 = %s$, $Q_1 = %s$ và $Q_3 = %s$.\\\\
            Do đó khoảng tứ phân vị là: $\\Delta_Q = %s - %s = %s$.\\\\
            Ta có $Q_1 - 1,5.\\Delta_Q = %s - 1,5.%s = %s$ và $Q_3 + 1,5.\\Delta_Q = %s + 1,5.%s = %s$ 
            nên mẫu số liệu có hai giá trị được xem là bất thường là $%s$ và $%s$ kg (đều lớn hơn $%s$ kg).'''
                           % (sorted_data_str, 
                              q2_str, q1_str, q3_str,
                              format_num(q3_val), format_num(q1_val), format_num(iqr_val),
                              format_num(q1_val), format_num(iqr_val), format_num(lower_limit), 
                              format_num(q3_val), format_num(iqr_val), format_num(upper_limit), 
                              outlier_1, outlier_2, format_num(upper_limit)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

