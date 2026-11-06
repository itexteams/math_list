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


def bt_dang31_p3_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Chọn ngẫu nhiên bộ 3 số chia hết phổ biến
                bo_so = [(3, 4, 5), (2, 3, 5), (3, 5, 7), (2, 5, 7), (2, 3, 7), (4, 5, 7)]
                a, b, c = random.choice(bo_so)

                # Chọn ngẫu nhiên số chữ số (3 hoặc 4 chữ số)
                n_digits = random.choice([3, 4])

                lower_limit = 10**(n_digits - 1)
                upper_limit = 10**n_digits - 1
                total_numbers = upper_limit - lower_limit + 1

                # Hàm tính bội chung nhỏ nhất
                def lcm(x, y):
                    return (x * y) // math.gcd(x, y)

                lcm_ab = lcm(a, b)
                lcm_bc = lcm(b, c)
                lcm_ca = lcm(c, a)
                lcm_abc = lcm(lcm_ab, c)

                # Hàm tìm số đầu, số cuối và số lượng số chia hết cho k
                def get_info(k):
                    min_k = ((lower_limit + k - 1) // k) * k
                    max_k = (upper_limit // k) * k
                    n_k = (max_k - min_k) // k + 1
                    return min_k, max_k, n_k

                min_a, max_a, nA = get_info(a)
                min_b, max_b, nB = get_info(b)
                min_c, max_c, nC = get_info(c)

                min_ab, max_ab, nAB = get_info(lcm_ab)
                min_bc, max_bc, nBC = get_info(lcm_bc)
                min_ca, max_ca, nCA = get_info(lcm_ca)

                min_abc, max_abc, nABC = get_info(lcm_abc)

                # Kết quả đúng theo nguyên lý bao hàm - loại trừ
                ans_val = nA + nB + nC - (nAB + nBC + nCA) + nABC

                # Tạo các phương án sai
                s = set()
                s.add(nA + nB + nC)
                s.add(nA + nB + nC - (nAB + nBC + nCA))
                s.add(nA + nB + nC - nAB - nBC - nCA)
                while len(s) < 6:
                    dev = random.choice([-300, -200, -100, 100, 200, 300, 50, -50])
                    dummy = ans_val + dev
                    if dummy > 0 and dummy != ans_val and dummy < total_numbers:
                        s.add(dummy)

                s_list = [f'${x}$' for x in s if x != ans_val]
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                da = f'${ans_val}$'

                # Câu hỏi
                noidungcauhoi = ('''Số các số tự nhiên có $%s$ chữ số và chia hết cho ít nhất một trong ba số $%s$; $%s$; $%s$ bằng bao nhiêu?'''
                                 %(latex(n_digits), latex(a), latex(b), latex(c)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Các số tự nhiên có $%s$ chữ số là các số từ $%s$ đến $%s$. Có tất cả $%s$ số.\\\\
            Số các số có $%s$ chữ số chia hết cho $%s$ là: $(%s - %s) : %s + 1 = %s$ số.\\\\
            Số các số có $%s$ chữ số chia hết cho $%s$ là: $(%s - %s) : %s + 1 = %s$ số.\\\\
            Số các số có $%s$ chữ số chia hết cho $%s$ là: $(%s - %s) : %s + 1 = %s$ số.\\\\
            Số các số có $%s$ chữ số chia hết cho cả $%s$ và $%s$ (chia hết cho \\text{BCNN}$(%s, %s) = %s$) là: $(%s - %s) : %s + 1 = %s$ số.\\\\
            Số các số có $%s$ chữ số chia hết cho cả $%s$ và $%s$ (chia hết cho \\text{BCNN}$(%s, %s) = %s$) là: $(%s - %s) : %s + 1 = %s$ số.\\\\
            Số các số có $%s$ chữ số chia hết cho cả $%s$ và $%s$ (chia hết cho \\text{BCNN}$(%s, %s) = %s$) là: $(%s - %s) : %s + 1 = %s$ số.\\\\
            Số các số có $%s$ chữ số chia hết cho cả ba số $%s, %s, %s$ (chia hết cho \\text{BCNN}$(%s, %s, %s) = %s$) là: $(%s - %s) : %s + 1 = %s$ số.\\\\
            Theo nguyên lý bao hàm - loại trừ, số các số tự nhiên có $%s$ chữ số chia hết cho ít nhất một trong ba số $%s; %s; %s$ là:\\\\
            $|A \\cup B \\cup C| = |A| + |B| + |C| - (|A \\cap B| + |B \\cap C| + |C \\cap A|) + |A \\cap B \\cap C|$\\\\
            $= %s + %s + %s - (%s + %s + %s) + %s = %s$ số.'''
                           %(latex(n_digits), latex(lower_limit), latex(upper_limit), latex(total_numbers),
                             latex(n_digits), latex(a), latex(max_a), latex(min_a), latex(a), latex(nA),
                             latex(n_digits), latex(b), latex(max_b), latex(min_b), latex(b), latex(nB),
                             latex(n_digits), latex(c), latex(max_c), latex(min_c), latex(c), latex(nC),
                             latex(n_digits), latex(a), latex(b), latex(a), latex(b), latex(lcm_ab), latex(max_ab), latex(min_ab), latex(lcm_ab), latex(nAB),
                             latex(n_digits), latex(b), latex(c), latex(b), latex(c), latex(lcm_bc), latex(max_bc), latex(min_bc), latex(lcm_bc), latex(nBC),
                             latex(n_digits), latex(c), latex(a), latex(c), latex(a), latex(lcm_ca), latex(max_ca), latex(min_ca), latex(lcm_ca), latex(nCA),
                             latex(n_digits), latex(a), latex(b), latex(c), latex(a), latex(b), latex(c), latex(lcm_abc), latex(max_abc), latex(min_abc), latex(lcm_abc), latex(nABC),
                             latex(n_digits), latex(a), latex(b), latex(c),
                             latex(nA), latex(nB), latex(nC), latex(nAB), latex(nBC), latex(nCA), latex(nABC), latex(ans_val)
                             ))
                dapan='\\shortans[0]{$%s$}\n'%(latex(ans_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 
