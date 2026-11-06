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


def bt_dang50_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các thông số ngẫu nhiên cho bài toán
                # P(x) = x*(1 + a1*x)^n1 + x^2*(1 + a2*x)^n2
                # Tìm hệ số của x^p
                p = 5 

                n1 = randint(5, 8)
                n2 = randint(10, 15)

                a1 = choice([-3, -2, 2, 3])
                a2 = choice([-3, -2, 2, 3])

                # Tính toán k và m
                # Số hạng 1: x * C(n1, k) * (a1*x)^k = a1^k * C(n1, k) * x^(k+1) -> k + 1 = p
                k = p - 1
                # Số hạng 2: x^2 * C(n2, m) * (a2*x)^m = a2^m * C(n2, m) * x^(m+2) -> m + 2 = p
                m = p - 2

                # Tính hệ số tương ứng
                h1 = (a1**k) * math.comb(n1, k)
                h2 = (a2**m) * math.comb(n2, m)
                kq_val = h1 + h2

                # Định dạng hiển thị dấu cho hệ số a1, a2 trong đề bài
                str_a1 = str(a1) if a1 < 0 else "+" + str(a1)
                str_a2 = str(a2) if a2 < 0 else "+" + str(a2)

                # Các đáp án trắc nghiệm
                da = "$%s$" % (kq_val)

                # Tạo các phương án nhiễu
                s = set()
                while len(s) < 3:
                    sai = kq_val + randint(-100, 100) * 10
                    if sai != kq_val:
                        s.add("$%s$" % (sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Tìm hệ số của $x^{%s}$ trong khai triển $P\\left(x\\right) = x\\left(1 %sx\\right)^{%s} + x^2\\left(1 %sx\\right)^{%s}$.'''
                                 % (latex(p), latex(str_a1), latex(n1), latex(str_a2), latex(n2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Khai triển $P\\left(x\\right)$ có số hạng tổng quát $x C_{%s}^{k} \\left(%sx\\right)^{k} + x^2 C_{%s}^{m} \\left(%sx\\right)^{m} = \\left(%s\\right)^{k} C_{%s}^{k} x^{k+1} + \\left(%s\\right)^{m} C_{%s}^{m} x^{m+2}$\\\\
                             $\\left(k \\in \\mathbb{N}, k \\le %s, m \\in \\mathbb{N}, m \\le %s\\right)$\\\\
                             Hệ số của $x^{%s}$ ứng với $k, m$ thỏa hệ $\\begin{cases} k+1 = %s \\\\ m+2 = %s \\end{cases} \\Leftrightarrow \\begin{cases} k = %s \\\\ m = %s \\end{cases}$.\\\\
                             Vậy hệ số cần tìm là $\\left(%s\\right)^{%s} C_{%s}^{%s} + \\left(%s\\right)^{%s} C_{%s}^{%s} = %s$.'''
                           % (latex(n1), latex(a1), latex(n2), latex(a2), latex(a1), latex(n1), latex(a2), latex(n2),
                              latex(n1), latex(n2), latex(p), latex(p), latex(p), latex(k), latex(m),
                              latex(a1), latex(k), latex(n1), latex(k), latex(a2), latex(m), latex(n2), latex(m), latex(kq_val)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

