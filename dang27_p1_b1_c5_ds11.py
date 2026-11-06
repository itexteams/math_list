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


def bt_dang27_p1_b1_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Random các giá trị
                # Chọn ngẫu nhiên tử số và mẫu số cho cơ số a
                list_primes = [2, 3, 5, 7]
                p = random.choice(list_primes)
                q = random.choice([x for x in list_primes if x != p])
                a = Rational(p, q) # Cơ số a = p/q

                # Random các chỉ số căn n, m, k
                n = random.randint(2, 4)
                m = random.randint(2, 4)
                k = random.randint(2, 4)

                # B1: Tính toán kết quả
                # Số mũ đúng: x = 1/n + 1/(n*m) + 1/(n*m*k)
                exp_final = Rational(1, n) + Rational(1, n*m) + Rational(1, n*m*k)

                # Đáp án đúng
                kq = 'P = \\left( %s \\right)^{%s}' % (latex(a), latex(exp_final))

                # Tạo các đáp án nhiễu (thay đổi số mũ)
                s = [
                    '$P = \\left( %s \\right)^{%s}$' % (latex(a), latex(exp_final + Rational(1, 2))),
                    '$P = \\left( %s \\right)^{%s}$' % (latex(a), latex(exp_final * 2)),
                    '$P = \\left( %s \\right)^{%s}$' % (latex(a), latex(Rational(1, n*m*k))),
                    '$P = \\left( %s \\right)^{%s}$' % (latex(a), latex(Rational(n+m+k, n*m*k))),
                    '$P = \\left( %s \\right)^{%s}$' % (latex(a), latex(exp_final - Rational(1, n*m*k))),
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (B2: Viết lại y hệt cấu trúc bài toán)
                # Định dạng hiển thị căn thức lồng nhau
                # \sqrt[n]{a \sqrt[m]{a \sqrt[k]{a}}}
                str_a = latex(a)
                cauhoi_math = '\\sqrt[%s]{%s \\sqrt[%s]{%s \\sqrt[%s]{%s}}}' % (n, str_a, m, str_a, k, str_a)
                # Xử lý trường hợp căn bậc 2 thì không ghi số 2
                cauhoi_math = cauhoi_math.replace('[2]', '') 

                noidungcauhoi = ('''Cho biểu thức $P = %s$. Mệnh đề nào trong các mệnh đề sau là đúng?'''
                                 % (cauhoi_math))

                # Các đáp án
                da_d = ('\\True $%s$' % (kq))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết chi tiết từng bước như ảnh mẫu)
                step1_exp = Rational(1, k) + 1
                step2_exp = Rational(step1_exp, m) + 1

                loigiai = ('''Ta có: \\\\
                             $P = \\sqrt[%s]{%s \\sqrt[%s]{%s \\cdot \\left( %s \\right)^{\\frac{1}{%s}}}} 
                             = \\sqrt[%s]{%s \\sqrt[%s]{\\left( %s \\right)^{%s}}} 
                             = \\sqrt[%s]{%s \\cdot \\left( %s \\right)^{\\frac{%s}{%s}}} 
                             = \\sqrt[%s]{\\left( %s \\right)^{%s}} 
                             = \\left( %s \\right)^{%s}$.'''
                           % (n, str_a, m, str_a, str_a, k,
                              n, str_a, m, str_a, latex(step1_exp),
                              n, str_a, str_a, latex(step1_exp), m,
                              n, str_a, latex(step2_exp),
                              str_a, latex(exp_final)
                             ))
                # Dọn dẹp các ký tự thừa nếu là căn bậc 2
                loigiai = loigiai.replace('[2]', '')

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

