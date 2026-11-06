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


def bt_dang19_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B1 & B3: Nghiên cứu đề bài và thiết lập tham số ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các hệ số a, b, c cho hàm y = ax^4 + bx^2 + c
                # Để giống bài mẫu, ta ưu tiên a=1, b=-4, c=5 hoặc các số nguyên nhỏ
                a = random.choice([1, -1, 2])
                b = random.choice([-4, -3, -2, 2, 3, 4])
                c = random.randint(1, 10)

                # Random hoành độ tiếp điểm x0
                x0 = random.choice([-2, -1, 1, 2])

                # Định nghĩa hàm số
                f = a*x**4 + b*x**2 + c

                # Đạo hàm và tính hệ số góc k = f'(x0)
                f_prime = diff(f, x)
                k = f_prime.subs(x, x0)

                # Tính tung độ tiếp điểm y0 = f(x0)
                y0 = f.subs(x, x0)

                # Phương trình tiếp tuyến có dạng: y = k(x - x0) + y0 => y = kx - k*x0 + y0
                hiso_tu_do = -k*x0 + y0

                # Tạo nội dung phương trình tiếp tuyến để so sánh (dạng y = kx + m)
                def format_line(k_val, m_val):
                    part1 = f"{k_val}x" if k_val != 0 else ""
                    if m_val > 0:
                        part2 = f"+{m_val}" if part1 != "" else f"{m_val}"
                    elif m_val < 0:
                        part2 = f"{m_val}"
                    else:
                        part2 = ""
                    return f"y={part1}{part2}".replace("+-", "-").replace("- -", "+")

                kq_chinh_xac = format_line(k, hiso_tu_do)

                # Tạo các đáp án nhiễu
                da_sai_1 = format_line(k, hiso_tu_do + random.choice([-4, 4]))
                da_sai_2 = format_line(-k, hiso_tu_do)
                da_sai_3 = format_line(k, hiso_tu_do + random.choice([-8, 8]))

                # Câu hỏi
                noidungcauhoi = (r'Phương trình tiếp tuyến của đồ thị hàm số $y = %s$ tại điểm có hoành độ $x = %s$ là' 
                                 % (latex(f), latex(x0)))

                # Các đáp án
                da_d = '\\True $' + kq_chinh_xac + '$'
                da_s1 = '$' + da_sai_1 + '$'
                da_s2 = '$' + da_sai_2 + '$'
                da_s3 = '$' + da_sai_3 + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Ta có $y' = %s$, $y'(%s) = %s$.\\'''
                           r'Điểm thuộc đồ thị đã cho có hoành độ $x = %s$ là: $M(%s;%s)$.\\'
                           r'Vậy phương trình tiếp tuyến của đồ thị hàm số tại $M(%s;%s)$ là:\\'
                           r'''$y = y'(%s)(x - (%s)) + %s \Leftrightarrow y = %s(x %s) + %s \Leftrightarrow %s$.'''
                           % (latex(f_prime), latex(x0), latex(k),
                              latex(x0), latex(x0), latex(y0),
                              latex(x0), latex(y0),
                              latex(x0), latex(x0), latex(y0), 
                              latex(k), '+' + str(-x0) if x0 < 0 else '-' + str(x0), latex(y0),
                              kq_chinh_xac))

                # Chỉnh sửa hiển thị dấu trong lời giải (x - -1 thành x + 1)
                loigiai = loigiai.replace("- -", "+").replace("+ -", "-")

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

