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


def bt_dang17_p3_b2_c3_ds12(self):
            # Khai báo biến
            # --- BƯỚC 1 & 3: THIẾT LẬP VÀ RANDOM BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khai báo các hệ số sao cho kết quả đẹp (nguyên)
                # Hàm f(x) = a * x^(1/3). Tích phân từ 1 đến 8 của x^(1/3) là 45/4.
                # Chọn a là bội của 4 để kết quả là số nguyên.
                a = random.choice([4, 8, 12, 16, 20, 24])
                c1 = 1
                c2 = random.randint(2, 7)
                c3 = 8

                # Tính toán giá trị đúng bằng Sympy
                f = a * cbrt(x)
                val_integral = Integral(f, (x, c1, c3)).doit()
                kq_dung = int(val_integral)

                # Định dạng kết quả (thay dấu chấm bằng dấu phẩy nếu là số thập phân)
                kq = str(kq_dung).replace('.', ',')

                # --- BƯỚC 4: ĐIỀU CHỈNH PHƯƠNG ÁN SAI ---
                # Tạo các phương án sai không trùng với đáp án đúng
                s_list = []
                while len(s_list) < 3:
                    sai = kq_dung + random.choice([-10, -5, 5, 10, 15, -15, 20])
                    if sai != kq_dung and sai not in s_list:
                        s_list.append(sai)

                # Các đáp án trắc nghiệm theo mẫu
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = ['$%s$' % (latex(s_list[0])),
                     '$%s$' % (latex(s_list[1])),
                     '$%s$' % (latex(s_list[2]))]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- B2: VIẾT LẠI NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
                # Câu hỏi
                noidungcauhoi = (r'''Cho hàm số $f(x) = %s\sqrt[3]{x}$. Giá trị của biểu thức $I = \int_{%s}^{%s} f(x)\text{d}x - \int_{%s}^{%s} f(x)\text{d}x$ bằng'''
                                 % (latex(a), latex(c1), latex(c2), latex(c3), latex(c2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Ta có $I = \int_{%s}^{%s} f(x)\text{d}x + \int_{%s}^{%s} f(x)\text{d}x = \int_{%s}^{%s} f(x)\text{d}x$. \\
                             Mặt khác: $\int_{%s}^{%s} %s \sqrt[3]{x} \text{d}x = %s \cdot \frac{3}{4} x^{\frac{4}{3}} \bigg|_{%s}^{%s} = %s$.'''
                           % (latex(c1), latex(c2), latex(c2), latex(c3), latex(c1), latex(c3),
                              latex(c1), latex(c3), latex(a), latex(a), latex(c1), latex(c3), latex(kq_dung)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))

            # Xuất câu trắc nghiệm theo đúng định dạng mâu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

