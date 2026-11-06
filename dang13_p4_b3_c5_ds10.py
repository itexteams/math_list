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


def bt_dang13_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến và logic ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các tham số ngẫu nhiên cho bài toán: (ax + 1/x^(1/m))^n
                # Để k là số nguyên, n*m phải chia hết cho (m+1). 
                # Cách đơn giản: n = j*(m+1)
                m = random.choice([2, 3, 4, 5]) # Chỉ số căn thức
                j = random.choice([2, 3, 4])     # Hệ số nhân để n vừa phải
                n = j * (m + 1)                 # Số mũ khai triển
                a = random.choice([1, 2, 3])     # Hệ số của x

                # Tính toán k: (n-k) - k/m = 0  => nm - mk - k = 0 => k = (nm)/(m+1)
                k_val = (n * m) // (m + 1)

                # Tính hệ số (Coefficient)
                he_so_to_hop = binomial(n, k_val)
                he_so_a = a**(n - k_val)
                ket_qua_so = he_so_to_hop * he_so_a

                # Các thông số phục vụ lời giải và hiển thị
                tu_so_mu = n * m
                mau_so_mu = m + 1 # Chính là hệ số của k trong tử số (nm - (m+1)k)

                # Đáp án đúng
                da_dung = ket_qua_so

                # Tạo các phương án nhiễu (đảm bảo không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Nhiễu bằng cách thay đổi k hoặc thay đổi hệ số a
                    sai = binomial(n, random.randint(1, n-1)) * (a**random.randint(1, 3))
                    if sai != da_dung:
                        s.add('$%s$' % latex(sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                da_d = ('\\True $%s$' % latex(da_dung))

                # Câu hỏi
                # Cấu trúc: (ax + 1/\sqrt[m]{x})^n
                bieu_thuc_gốc = '\\left( %sx + \\frac{1}{\\sqrt[%s]{x}} \\right)^{%s}' % (latex(a) if a > 1 else '', latex(m), latex(n))
                noidungcauhoi = ('''Tìm hệ số không chứa $x$ trong khai triển: $%s$ ($x > 0$).'''
                                 % (bieu_thuc_gốc))

                # Lời giải chi tiết
                # Số hạng tổng quát: C_n^k * (ax)^{n-k} * (x^{-1/m})^k
                loigiai = ('''Ta có: $%s = \\left( %sx + x^{-\\frac{1}{%s}} \\right)^{%s} = \\sum_{k=0}^{%s} C_{%s}^k \\left( %sx \\right)^{%s-k} \\left( x^{-\\frac{1}{%s}} \\right)^k = \\sum_{k=0}^{%s} C_{%s}^k \\cdot %s^{%s-k} \\cdot x^{\\frac{%s-%sk}{%s}}$. \\\\
                           Số hạng tổng quát trong khai triển là: $C_{%s}^k \\cdot %s^{%s-k} \\cdot x^{\\frac{%s-%sk}{%s}}$. \\\\
                           Hệ số của số hạng không chứa $x$ trong khai triển ứng với $k$ thỏa mãn: \\\\
                           $\\frac{%s-%sk}{%s} = 0 \\Leftrightarrow %s - %sk = 0 \\Leftrightarrow k = %s$. \\\\
                           Vậy hệ số không chứa $x$ trong khai triển là: $C_{%s}^{%s} \\cdot %s^{%s} = %s$.'''
                           % (bieu_thuc_gốc, latex(a) if a > 1 else '', latex(m), latex(n), 
                              latex(n), latex(n), latex(a) if a > 1 else '', latex(n), latex(m),
                              latex(n), latex(n), latex(a), latex(n), latex(tu_so_mu), latex(mau_so_mu), latex(m),
                              latex(n), latex(a), latex(n), latex(tu_so_mu), latex(mau_so_mu), latex(m),
                              latex(tu_so_mu), latex(mau_so_mu), latex(m), latex(tu_so_mu), latex(mau_so_mu), latex(k_val),
                              latex(n), latex(k_val), latex(a), latex(n - k_val), latex(ket_qua_so)
                              ))

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

