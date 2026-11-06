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


def bt_dang14_p1_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            # Hàm hỗ trợ định dạng số: nếu là số nguyên thì bỏ phần thập phân, đổi dấu '.' thành ','
            def format_num(num):
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            if dang=='1':
                # Random 16 giá trị cho mẫu số liệu
                data = [random.randint(5, 20) for _ in range(16)]
                random.shuffle(data) # Xáo trộn để tạo đề

                # Sắp xếp để tính toán
                sorted_data = sorted(data)

                # Chuỗi hiển thị đề bài và lời giải
                data_str = "    ".join(map(str, data))
                sorted_data_str = "    ".join(map(str, sorted_data))

                # Tính toán các đại lượng
                min_val = sorted_data[0]
                max_val = sorted_data[-1]
                R = max_val - min_val

                # n = 16 => Q1 lấy trung bình vị trí 3 và 4 (index 3, 4); Q2 lấy 7, 8; Q3 lấy 11, 12
                q2_val = (sorted_data[7] + sorted_data[8]) / 2
                q1_val = (sorted_data[3] + sorted_data[4]) / 2
                q3_val = (sorted_data[11] + sorted_data[12]) / 2

                delta_q = q3_val - q1_val

                # Chuẩn hóa định dạng chuỗi kết quả
                R_str = format_num(R)
                q1_str = format_num(q1_val)
                q2_str = format_num(q2_val)
                q3_str = format_num(q3_val)
                dq_str = format_num(delta_q)

                # Các đáp án trắc nghiệm
                du = ['$R = %s$ và $\\Delta_Q = %s$' % (R_str, dq_str)]
                da = random.choice(du)

                # Sinh các đáp án nhiễu
                s = [
                    '$R = %s$ và $\\Delta_Q = %s$' % (format_num(R + random.choice([1, 2])), dq_str),
                    '$R = %s$ và $\\Delta_Q = %s$' % (R_str, format_num(delta_q + random.choice([0.5, 1, -0.5]))),
                    '$R = %s$ và $\\Delta_Q = %s$' % (format_num(R - random.choice([1, 2])), dq_str),
                    '$R = %s$ và $\\Delta_Q = %s$' % (format_num(R + random.choice([2, 3])), format_num(delta_q + random.choice([0.5, -0.5]))),
                    '$R = %s$ và $\\Delta_Q = %s$' % (R_str, format_num(delta_q + 1.5))
                ]

                # Lọc bỏ các đáp án trùng với đáp án đúng để tránh lỗi
                s = list(set(s) - set(du))
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Mẫu số liệu sau đây cho biết số bài hát ở mỗi album trong bộ sưu tập của Bình:
            \\begin{center}
            %s
            \\end{center}
            Khoảng biến thiên và khoảng tứ phân vị của mẫu số liệu lần lượt là''' 
                                 % (data_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Sắp xếp mẫu số liệu theo thứ tự không giảm:
            \\begin{center}
            %s
            \\end{center}
            Khoảng biến thiên: $R = %s - %s = %s$.\\\\
            Mẫu số liệu có 16 giá trị nên ta có $Q_2 = \\frac{%s + %s}{2} = %s$; $Q_1 = \\frac{%s + %s}{2} = %s$ và $Q_3 = \\frac{%s + %s}{2} = %s$.\\\\
            Vậy khoảng tứ phân vị là $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$.'''
                           % (sorted_data_str, 
                              max_val, min_val, R_str,
                              sorted_data[7], sorted_data[8], q2_str,
                              sorted_data[3], sorted_data[4], q1_str,
                              sorted_data[11], sorted_data[12], q3_str,
                              q3_str, q1_str, dq_str))

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

