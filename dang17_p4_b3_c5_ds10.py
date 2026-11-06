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


def bt_dang17_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Tìm cách random bài toán
                # Chọn n để phương trình có nghiệm nguyên dương đẹp
                # Phương trình: n(n-1)(n-2) + c*n(n-1) = K <=> n(n-1)(n-2+c) = K
                n_val = randint(4, 6) # n nguyên dương, n >= 3
                c_val = randint(1, 3) # Hệ số của A_n^2
                K_val = n_val * (n_val - 1) * (n_val - 2 + c_val)

                # Biến số trong khai triển (1 + bx)^n
                b_val = random.choice([-4, -3, -2, 2, 3, 4])
                k_pow = 3 # Tìm hệ số của x^3

                # Tính toán đáp án đúng
                # Hệ số của x^k trong (1 + bx)^n là C_n^k * b^k
                kq_val = sp.binomial(n_val, k_pow) * (b_val**k_pow)
                da = str(kq_val)

                # Bước 4: Điều chỉnh phương án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    # Tạo các phương án sai dựa trên việc tính sai tổ hợp hoặc lũy thừa
                    sai = random.choice([
                        sp.binomial(n_val, k_pow) * (b_val**(k_pow-1)),
                        sp.binomial(n_val, k_pow-1) * (b_val**k_pow),
                        -kq_val,
                        kq_val + randint(1, 20),
                        kq_val - randint(1, 20),
                        b_val**n_val
                    ])
                    if str(sai) != da:
                        s.add('$%s$' % latex(sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                # Cấu trúc: A_n^3 + c*A_n^2 = K. Hệ số của x^3 trong (1 + bx)^n
                noidungcauhoi = ('''Gọi $n$ là số nguyên dương thỏa mãn $A_n^3 + %s A_n^2 = %s$. Tìm hệ số của $x^3$ trong khai triển nhị thức Niu-tơn của $\\left( 1 %s x \\right)^n$.'''
                                 % (latex(c_val) if c_val != 1 else '', 
                                    latex(K_val), 
                                    ('+' + str(b_val)) if b_val > 0 else str(b_val)
                                   ))

                # Các đáp án
                da_d = ('\\True $%s$' % latex(kq_val))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết lại y hệt logic lời giải mẫu)
                # n(n-1)(n-2) + c*n(n-1) = K <=> n(n-1)(n-2+c) = K
                pt_bien_doi = n_val * (n_val - 1) * (n_val - 2 + c_val)

                loigiai = ('''Điều kiện: $n \\ge 3; n \\in \\mathbb{N}$.\\\\
                             $A_n^3 + %s A_n^2 = %s \\Leftrightarrow \\frac{n!}{\\left( n-3 \\right)!} + %s \\cdot \\frac{n!}{\\left( n-2 \\right)!} = %s$\\\\
                             $\\Leftrightarrow n(n-1)(n-2) + %s \\cdot n(n-1) = %s$\\\\
                             $\\Leftrightarrow n(n-1)\\left( n - 2 + %s \\right) = %s$\\\\
                             $\\Leftrightarrow n^2(n-1) = %s$ (nếu $%s=2$) hoặc giải phương trình ta được $n = %s$ (thỏa mãn).\\\\
                             Ta có khai triển: $\\left( 1 %s x \\right)^{%s} = \\sum_{k=0}^{%s} C_{%s}^k \\left( %s x \\right)^k = \\sum_{k=0}^{%s} C_{%s}^k \\left( %s \\right)^k x^k$.\\\\
                             Hệ số của $x^3$ trong khai triển trên ứng với $k = 3$.\\\\
                             Vậy hệ số của $x^3$ trong khai triển $\\left( 1 %s x \\right)^{%s}$ là $C_{%s}^3 \\cdot \\left( %s \\right)^3 = %s$.'''
                           % (latex(c_val) if c_val != 1 else '', latex(K_val), 
                              latex(c_val) if c_val != 1 else '', latex(K_val),
                              latex(c_val) if c_val != 1 else '', latex(K_val),
                              latex(c_val), latex(K_val),
                              latex(n_val**2 * (n_val-1)), latex(c_val), latex(n_val),
                              ('+' + str(b_val)) if b_val > 0 else str(b_val), latex(n_val),
                              latex(n_val), latex(n_val), latex(b_val),
                              latex(n_val), latex(n_val), latex(b_val),
                              ('+' + str(b_val)) if b_val > 0 else str(b_val), latex(n_val),
                              latex(n_val), latex(b_val), latex(kq_val)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

