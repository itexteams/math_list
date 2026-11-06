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


def bt_dang71_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # Bước 1: Tạo giao điểm A(x0, y0) ngẫu nhiên là các số nguyên để bài toán đẹp
            x0 = random.randint(-3, 3)
            y0 = random.randint(-3, 3)

            # Bước 2: Tạo hai đường thẳng d1, d2 cắt nhau tại A
            # Đường thẳng d1: a1(x - x0) + b1(y - y0) = 0  => a1*x + b1*y + c1 = 0
            a1 = random.randint(-3, 3)
            if a1 == 0: a1 = 1
            b1 = random.randint(-3, 3)
            if b1 == 0: b1 = -2
            c1 = -(a1 * x0 + b1 * y0)

            # Đường thẳng d2: a2(x - x0) + b2(y - y0) = 0
            # Đảm bảo d2 không trùng hoặc song song với d1
            while True:
                a2 = random.randint(-3, 3)
                if a2 == 0: a2 = 2
                b2 = random.randint(-3, 3)
                if b2 == 0: b2 = 3
                if a1 * b2 != a2 * b1: # Kiểm tra định thức để chắc chắn cắt nhau
                    break
            c2 = -(a2 * x0 + b2 * y0)

            # Bước 3: Tạo đường thẳng Delta: Ax + By + C = 0
            A_coeff = random.randint(-4, 4)
            if A_coeff == 0: A_coeff = 3
            B_coeff = random.randint(-4, 4)
            if B_coeff == 0: B_coeff = 1
            C_coeff = random.randint(-5, 5)

            # Bước 4: Tính khoảng cách từ A(x0, y0) đến Delta
            tu_so = abs(A_coeff * x0 + B_coeff * y0 + C_coeff)
            mau_so_binh_phuong = A_coeff**2 + B_coeff**2
            khoang_cach = tu_so / sqrt(mau_so_binh_phuong)
            khoang_cach_rut_gon = simplify(khoang_cach)

            # Tạo các biểu thức đường thẳng để in
            line1_str = latex(a1*x + b1*y + c1).replace('**', '^') + " = 0"
            line2_str = latex(a2*x + b2*y + c2).replace('**', '^') + " = 0"
            delta_str = latex(A_coeff*x + B_coeff*y + C_coeff).replace('**', '^') + " = 0"

            # Bước 5: Tạo các phương án sai
            da_dung = "$%s$" % latex(khoang_cach_rut_gon)
            s = set()
            while len(s) < 3:
                # Tạo các giá trị sai bằng cách thay đổi tử số hoặc mẫu số
                sai_tu = random.randint(1, 10)
                sai_mau = random.choice([2, 5, 10, sqrt(2), sqrt(5), sqrt(10), sqrt(13), 2*sqrt(10)])
                temp_sai = simplify(sai_tu / sai_mau)
                da_sai = "$%s$" % latex(temp_sai)
                if da_sai != da_dung:
                    s.add(da_sai)

            list_sai = list(s)

            # Nội dung câu hỏi
            noidungcauhoi = ("Tính khoảng cách từ giao điểm của hai đường thẳng $%s$ và $%s$ đến đường thẳng $\\Delta: %s$." 
                             % (line1_str, line2_str, delta_str))

            # Các đáp án
            da_d = "\\True " + da_dung
            da_s1 = list_sai[0]
            da_s2 = list_sai[1]
            da_s3 = list_sai[2]

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = ("Tọa độ giao điểm $A$ của hai đường thẳng là nghiệm của hệ phương trình: \\\\"
                       "$\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases} \\rightarrow A(%s; %s)$. \\\\"
                       "Khoảng cách từ điểm $A$ đến đường thẳng $\\Delta$ được tính theo công thức: \\\\"
                       "$d(A; \\Delta) = \\frac{|%s \\cdot (%s) + %s \\cdot (%s) + (%s)|}{\\sqrt{%s^2 + %s^2}} = \\frac{%s}{\\sqrt{%s}} = %s$."
                       % (line1_str, line2_str, x0, y0, x0, y0, 
                          A_coeff, x0, B_coeff, y0, C_coeff, A_coeff, B_coeff, tu_so, mau_so_binh_phuong, latex(khoang_cach_rut_gon)))

            # Xuất câu trắc nghiệm (không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

