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


def bt_dang25_p1_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn cận a từ 1 đến 3, cận b lớn hơn a từ 1 đến 5 đơn vị
                a = randint(1, 3)
                b = a + randint(1, 5)
                # Chọn hằng số c từ 1 đến 5
                c = randint(1, 5)

                x = symbols('x')
                f = (x - c)/x

                # Tính toán giá trị đúng để tạo chuỗi LaTeX
                # I = (b - a) - c*(ln(b) - ln(a)) = (b-a) - c*ln(b/a)
                hieu_can = b - a

                # Tạo chuỗi LaTeX cho đáp án đúng
                def format_ans(h, coeff, can_a, can_b):
                    # Phần số nguyên
                    s_h = f"{h}"
                    # Phần logarit
                    if can_a == 1:
                        log_part = f"\\ln {can_b}"
                    else:
                        log_part = f"\\ln \\frac{{{can_b}}}{{{can_a}}}"

                    if coeff == 1:
                        return f"{s_h} - {log_part}"
                    else:
                        return f"{s_h} - {coeff}{log_part}"

                da_chuan = format_ans(hieu_can, c, a, b)

                # B4: Điều chỉnh các phương án sai không được trùng đáp án đúng
                du = [f'${da_chuan}$']
                da = du[0]

                # Tạo danh sách các phương án nhiễu
                s = set()
                while len(s) < 3:
                    # Các biến thể: đổi dấu, đổi hằng số, đổi hiệu cận
                    sai1 = format_ans(hieu_can, c, a, b).replace('-', '+')
                    sai2 = format_ans(hieu_can + randint(1,2), c, a, b)
                    sai3 = format_ans(hieu_can, c + randint(1,2), a, b)
                    sai4 = f"{hieu_can} - \\ln {b+a}"

                    for item in [sai1, sai2, sai3, sai4]:
                        item_str = f'${item}$'
                        if item_str != da:
                            s.add(item_str)

                s_list = list(s)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = (r'Tính tích phân $I = \int_{%s}^{%s} \frac{x-%s}{x} \, \text{d} x$.' 
                                 % (latex(a), latex(b), latex(c)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết lại y hệt logic hình ảnh)
                # Biểu thức logarit trong lời giải
                if a == 1:
                    log_step = f"({b} - {c}\\ln {b}) - ({a} - {c}\\ln 1)"
                else:
                    log_step = f"({b} - {c}\\ln {b}) - ({a} - {c}\\ln {a})"

                loigiai = (r'''Ta có $I = \int_{%s}^{%s} \frac{x-%s}{x} \, \text{d} x = \int_{%s}^{%s} \left( 1 - \frac{%s}{x} \right) \, \text{d} x$ \\
                              $= \left( x - %s\ln|x| \right) \Big|_{%s}^{%s} = %s$ \\
                              $= %s$.'''
                           % (latex(a), latex(b), latex(c), latex(a), latex(b), latex(c),
                              latex(c) if c != 1 else "", latex(a), latex(b), 
                              log_step, da_chuan))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

