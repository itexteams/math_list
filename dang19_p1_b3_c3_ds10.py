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


def bt_dang19_p1_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            # Hàm hỗ trợ đổi dấu . thành , trong số thập phân
            def format_num(num):
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            if dang=='1':
                # B3: Random bối cảnh
                city = random.choice(["Hà Nội", "Đà Nẵng", "TP. Hồ Chí Minh", "Vinh", "Huế", "Nha Trang"])
                month = random.choice(["sáu", "bảy", "tám", "chín"])

                # Random 7 nhiệt độ liên tiếp
                n = 7
                data = [random.randint(30, 39) for _ in range(n)]

                data_str = "; ".join(map(str, data))
                data_sum_str = " + ".join(map(str, data))

                # B2: Tính toán các thông số
                mean_val = sum(data) / n
                mean_round = round(mean_val, 2)

                var_val = sum((val - mean_val)**2 for val in data) / n
                var_round = round(var_val, 2)

                std_val = math.sqrt(var_val)
                std_round = round(std_val, 2)

                # Xử lý trường hợp std_round tình cờ là số nguyên (rất hiếm nhưng cần đề phòng)
                if std_round == int(std_round):
                    std_round += 0.01

                # Tạo đáp án đúng: khoảng (k; k+1)
                k = math.floor(std_round)
                da_d_str = f"({k}; {k+1})"

                # Tạo đáp án nhiễu
                # Nhiễu 1: Khoảng trên
                da_s1_str = f"({k+1}; {k+2})"

                # Nhiễu 2: Khoảng chứa phương sai (bẫy quên căn bậc 2)
                k_var = math.floor(var_round)
                if k_var == k: # Đảm bảo không bị trùng đáp án đúng
                    k_var = k + 2
                da_s2_str = f"({k_var}; {k_var+1})"

                # Nhiễu 3: Khoảng có chứa phân số giả lập
                da_s3_str = f"\\left[{k+2}; \\frac{{{2*(k+2) + 1}}}{{2}}\\right]"

                # Định dạng lại các số thập phân ra chuỗi
                mean_str = format_num(mean_round)
                var_str = format_num(var_round)
                std_str = format_num(std_round)

                # Thiết lập đáp án
                du = ['$%s$' % da_d_str]
                da = random.choice(du)

                s = [
                    '$%s$' % da_s1_str,
                    '$%s$' % da_s2_str,
                    '$%s$' % da_s3_str
                ]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Nhiệt độ cao nhất của %s trong 7 ngày liên tiếp trong tháng %s được ghi lại là:\\\\
            $%s$ (Độ C).\\\\
            Độ lệch chuẩn của mẫu số liệu thuộc khoảng nào dưới đây?''' 
                                 % (city, month, data_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Số trung bình cộng của mẫu số liệu là:
            $\\bar{x} = \\frac{%s}{7} \\approx %s$\\\\
            Phương sai của mẫu số liệu là: $s^2 = \\frac{\\sum_{i=1}^7(x_i - \\bar{x})^2}{7} \\approx %s$\\\\
            Độ lệch chuẩn cần tính là: $s \\approx \\sqrt{%s} \\approx %s$.\\\\
            Ta thấy $%s \\in %s$.'''
                           % (data_sum_str, mean_str, var_str, var_str, std_str, std_str, da_d_str))

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

