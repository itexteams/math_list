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


def bt_dang19_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1 & 3: Nghiên cứu đề bài và Random các số
                # Chọn a, b ngẫu nhiên để tạo nhị thức (ax + b)^5
                a = randint(2, 4)
                b = randint(2, 5)
                n = 5

                # Tính toán các hệ số cụ thể để lập phương án và lời giải
                def nCr(n, r):
                    return math.comb(n, r)

                # Biểu thức đúng
                expr = (a*x + b)**n
                poly_correct = expand(expr)
                da = latex(poly_correct)

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                # Sai kiểu A: Hệ số của x^n bằng 1
                poly_sai_A = expand((1*x + b)**n) + (a**n - 1)*x**n # Giữ các hạng tử sau nhưng đổi hạng tử đầu? 
                # Cách đơn giản hơn: lấy poly_correct nhưng thay hệ số đầu thành 1
                terms = [poly_correct.coeff(x, i) * x**i for i in range(n + 1)]
                terms[-1] = 1 * x**n
                da_s1 = latex(sum(terms))

                # Sai kiểu B: Sai một hệ số ở giữa (ví dụ hệ số x^4)
                terms_B = [poly_correct.coeff(x, i) * x**i for i in range(n + 1)]
                terms_B[-2] = (poly_correct.coeff(x, n-1) // 2) * x**(n-1)
                da_s2 = latex(sum(terms_B))

                # Sai kiểu C: Đổi dấu xen kẽ (khai triển của (ax - b)^5)
                expr_sai_C = (a*x - b)**n
                da_s3 = latex(expand(expr_sai_C))

                # Câu hỏi
                noidungcauhoi = ('''Khai triển nhị thức $\\left(%sx+%s\\right)^%s$.'''
                                 %(latex(a), latex(b), latex(n)))

                # Các đáp án
                da_d = ('\\True ' + '$' + str(da) + '$')
                da_s1_str = '$' + str(da_s1) + '$'
                da_s2_str = '$' + str(da_s2) + '$'
                da_s3_str = '$' + str(da_s3) + '$'

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1_str, da_s2_str, da_s3_str]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Bản sao y hệt logic hình ảnh)
                # Tính từng hạng tử cho lời giải
                c0 = nCr(5, 0) * (a**5)
                c1 = nCr(5, 1) * (a**4) * b
                c2 = nCr(5, 2) * (a**3) * (b**2)
                c3 = nCr(5, 3) * (a**2) * (b**3)
                c4 = nCr(5, 4) * (a**1) * (b**4)
                c5 = nCr(5, 5) * (b**5)

                loigiai = ('''$\\left(%sx+%s\\right)^5 = C_5^0 \\left(%sx\\right)^5 + C_5^1 \\left(%sx\\right)^4 \\cdot %s + C_5^2 \\left(%sx\\right)^3 \\cdot %s^2 + C_5^3 \\left(%sx\\right)^2 \\cdot %s^3 + C_5^4 \\left(%sx\\right)^1 \\cdot %s^4 + C_5^5 \\cdot %s^5$\\\\
                           $= %sx^5 + %sx^4 + %sx^3 + %sx^2 + %sx + %s$.'''
                           %(latex(a), latex(b), latex(a), latex(a), latex(b), 
                             latex(a), latex(b), latex(a), latex(b), latex(a), 
                             latex(b), latex(b),
                             latex(c0), latex(c1), latex(c2), latex(c3), latex(c4), latex(c5)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

