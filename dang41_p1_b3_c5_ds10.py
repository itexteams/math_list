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


def bt_dang41_p1_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các giá trị ngẫu nhiên để bài toán luôn có nghiệm k nguyên
                # Khai triển (a*x^n + b/x^m)^p
                p = random.randint(5, 10) # Số mũ khai triển
                n = random.randint(2, 4)  # Số mũ của x ở số hạng đầu
                m = random.randint(1, 3)  # Số mũ của x ở mẫu số hạng sau

                # Chọn k_target trước để đảm bảo tìm được số hạng chứa x^T
                k_target = random.randint(0, p)

                # Hệ số a và b
                a = random.choice([2, 3, 4, 5])
                b = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])

                # Tính số mũ T của x cần tìm: T = n*(p-k) - m*k
                T = n * (p - k_target) - m * k_target

                # Tính hệ số đúng
                # He so = C(p, k) * a^(p-k) * b^k
                he_so_dung = binomial(p, k_target) * (a**(p - k_target)) * (b**k_target)

                # Tạo các phương án nhiễu
                # Nhiễu 1: Sai k (k_target + 1 hoặc -1)
                k_sai = k_target + 1 if k_target < p else k_target - 1
                he_so_sai1 = binomial(p, k_sai) * (a**(p - k_sai)) * (b**k_sai)

                # Nhiễu 2: Sai dấu (nếu hệ số đúng âm thì lấy dương và ngược lại)
                he_so_sai2 = -he_so_dung

                # Nhiễu 3: Tính nhầm lũy thừa của b (ví dụ b^(k+1))
                he_so_sai3 = binomial(p, k_target) * (a**(p - k_target)) * (abs(b)**k_target) if b < 0 else he_so_dung + random.randint(10, 100)

                if he_so_sai3 == he_so_dung:
                    he_so_sai3 = he_so_dung + 125

                # Định dạng hiển thị biểu thức trong đề bài
                dau_b = "+" if b > 0 else "-"
                tri_tuyet_b = abs(b)
                bieu_thuc = "\\left(%s x^{%s} %s \\frac{%s}{x^{%s}}\\right)^{%s}" % (latex(a), latex(n), dau_b, latex(tri_tuyet_b), latex(m), latex(p))

                # Các đáp án trắc nghiệm
                da = "$%s$" % (latex(he_so_dung))

                s = [
                    "$%s$" % (latex(he_so_sai1)),
                    "$%s$" % (latex(he_so_sai2)),
                    "$%s$" % (latex(he_so_sai3)),
                    "$%s$" % (latex(he_so_dung + random.randint(1, 10) * 10))
                ]

                # Loại bỏ các giá trị trùng với đáp án đúng trong danh sách sai
                s = [item for item in s if item != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ("Hệ số của số hạng chứa $x^{%s}$ trong khai triển của biểu thức $%s$ là"
                                 % (latex(T), bieu_thuc))

                # Các đáp án
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Xây dựng công thức tổng quát
                # Công thức: C_p^k * (ax^n)^{p-k} * (b/x^m)^k
                if b > 0:
                    tong_quat = "\\sum_{k=0}^{%s} C_{%s}^k \\cdot \\left(%s x^{%s}\\right)^{%s-k} \\cdot \\left(\\frac{%s}{x^{%s}}\\right)^k" % (latex(p), latex(p), latex(a), latex(n), latex(p), latex(b), latex(m))
                    rut_gon = "\\sum_{k=0}^{%s} C_{%s}^k \\cdot %s^{%s-k} \\cdot %s^k \\cdot x^{%s-%sk}" % (latex(p), latex(p), latex(a), latex(p), latex(b), latex(n*p), latex(n+m))
                else:
                    tong_quat = "\\sum_{k=0}^{%s} C_{%s}^k \\cdot \\left(%s x^{%s}\\right)^{%s-k} \\cdot \\left(-\\frac{%s}{x^{%s}}\\right)^k" % (latex(p), latex(p), latex(a), latex(n), latex(p), latex(tri_tuyet_b), latex(m))
                    rut_gon = "\\sum_{k=0}^{%s} (-1)^k \\cdot C_{%s}^k \\cdot %s^{%s-k} \\cdot %s^k \\cdot x^{%s-%sk}" % (latex(p), latex(p), latex(a), latex(p), latex(tri_tuyet_b), latex(n*p), latex(n+m))

                loigiai = ("Số hạng tổng quát trong khai triển là: \\\\"
                           " $T_{k+1} = C_{%s}^k \\cdot \\left(%s x^{%s}\\right)^{%s-k} \\cdot \\left(\\frac{%s}{x^{%s}}\\right)^k = C_{%s}^k \\cdot %s^{%s-k} \\cdot (%s)^k \\cdot x^{%s-%sk}$. \\\\"
                           " Số hạng chứa $x^{%s}$ ứng với: $%s - %sk = %s \\Leftrightarrow %sk = %s \\Leftrightarrow k = %s$. \\\\"
                           " Hệ số của số hạng chứa $x^{%s}$ là $C_{%s}^{%s} \\cdot %s^{%s} \\cdot (%s)^{%s} = %s$."
                           % (latex(p), latex(a), latex(n), latex(p), latex(b), latex(m), 
                              latex(p), latex(a), latex(p), latex(b), latex(n*p), latex(n+m),
                              latex(T), latex(n*p), latex(n+m), latex(T), latex(n+m), latex(n*p - T), latex(k_target),
                              latex(T), latex(p), latex(k_target), latex(a), latex(p - k_target), latex(b), latex(k_target), latex(he_so_dung)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

