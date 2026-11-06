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


def bt_dang67_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến ký hiệu cho Sympy
            x_sym = symbols('x')

            # B1: Nghiên cứu đề bài và lời giải (Đã thực hiện)
            # B2 & B3: Viết code và thiết lập logic Random

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random thông số bài toán
                # Giá nhập (C)
                gia_nhap = randint(30, 80) 

                # Để x = (A + gia_nhap)/2 là số nguyên, (A + gia_nhap) phải chẵn
                # Chọn hệ số A trong biểu thức (A - x) sao cho A > gia_nhap
                buoc_nhay = randint(20, 50) * 2
                he_so_a = gia_nhap + buoc_nhay

                # Tính toán đáp án đúng
                # Hàm lợi nhuận y = (he_so_a - x) * (x - gia_nhap)
                # y = -x^2 + (he_so_a + gia_nhap)x - (he_so_a * gia_nhap)
                tong = he_so_a + gia_nhap
                tich = he_so_a * gia_nhap
                gia_ban_toi_uu = tong // 2
                lai_nhieu_nhat = (he_so_a - gia_ban_toi_uu) * (gia_ban_toi_uu - gia_nhap)

                # Đáp án đúng
                da_dung_val = gia_ban_toi_uu
                da = '$%s$ USD' % latex(da_dung_val)

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s_vals = set()
                while len(s_vals) < 3:
                    sai = gia_ban_toi_uu + random.choice([-20, -15, -10, -5, 5, 10, 15, 20])
                    if sai != gia_ban_toi_uu and sai > gia_nhap:
                        s_vals.add(sai)

                list_s_vals = list(s_vals)
                das1 = '$%s$ USD' % latex(list_s_vals[0])
                das2 = '$%s$ USD' % latex(list_s_vals[1])
                das3 = '$%s$ USD' % latex(list_s_vals[2])

                # Nội dung câu hỏi
                noidungcauhoi = ('''Một cửa hàng buôn giày nhập một đôi với giá là $%s$ USD. Cửa hàng ước tính rằng nếu đôi giày được bán với giá $x$ USD thì mỗi tháng khách hàng sẽ mua $(%s - x)$ đôi. Cửa hàng bán một đôi giày giá bao nhiêu thì thu được nhiều lãi nhất.'''
                                 % (latex(gia_nhap), latex(he_so_a)))

                # Nội dung lời giải (Viết y hệt mẫu trong ảnh)
                loigiai = ('''Gọi $y$ (USD) là số tiền lãi của cửa hàng bán giày. \\\\
                            Ta có $y = (%s - x)(x - %s) = -x^2 + %sx - %s = -(x - %s)^2 + %s \\le %s$. \\\\
                            Dấu "$=$" xảy ra $\\Leftrightarrow x = %s$. \\\\
                            Vậy cửa hàng lãi nhiều nhất khi bán đôi giày với giá $%s$ USD.'''
                           % (latex(he_so_a), latex(gia_nhap), latex(tong), latex(tich), 
                              latex(gia_ban_toi_uu), latex(lai_nhieu_nhat), latex(lai_nhieu_nhat),
                              latex(gia_ban_toi_uu), latex(gia_ban_toi_uu)))

                # Sắp xếp các phương án
                da_d = ('\\True ' + str(da))
                list_options = [da_d, das1, das2, das3]
                random.shuffle(list_options)

            # Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

