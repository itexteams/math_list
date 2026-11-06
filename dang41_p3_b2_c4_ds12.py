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


def bt_dang41_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo danh sách các dạng (ở đây chỉ có 1 dạng theo ảnh)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: NGẪU NHIÊN HÓA CÁC THÔNG SỐ ---
                # k: tỉ số trẻ em nam gấp k lần trẻ em nữ (ví dụ: 1.2, 1.5, 2.0)
                list_k = [1.2, 1.5, 2.0, 2.5]
                k = random.choice(list_k)

                # p1: tỉ lệ trẻ nam bị hen phế quản (ví dụ 8% -> 0.08)
                p1_val = random.choice([0.06, 0.07, 0.08, 0.09, 0.1])
                # p2: tỉ lệ trẻ nữ bị hen phế quản (ví dụ 5% -> 0.05)
                p2_val = random.choice([0.03, 0.04, 0.05, 0.06])

                # --- BƯỚC 2: TÍNH TOÁN XÁC SUẤT ---
                # P(T) = k/(k+1), P(not T) = 1/(k+1)
                pt_tu = int(k * 10)
                pt_mau = int((k + 1) * 10)
                PT = Rational(pt_tu, pt_mau) # Xác suất chọn được trẻ nam
                PnotT = 1 - PT               # Xác suất chọn được trẻ nữ

                # Bayes: P(T|H) = [P(H|T)*P(T)] / [P(H|T)*P(T) + P(H|not T)*P(not T)]
                tu_so = p1_val * PT
                mau_so = (p1_val * PT) + (p2_val * PnotT)
                kq_chinh_xac = tu_so / mau_so

                # Làm tròn đến hàng phần mười
                kq_decimal = Decimal(float(kq_chinh_xac)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # --- BƯỚC 3: TẠO CÁC PHƯƠNG ÁN SAI ---
                # Đảm bảo các đáp án không trùng nhau và nằm trong khoảng (0, 1)
                s_vals = []
                while len(s_vals) < 3:
                    sai = float(kq_decimal) + random.choice([-0.3, -0.2, -0.1, 0.1, 0.2, 0.3])
                    sai = round(sai, 1)
                    # Kiểm tra điều kiện: không trùng đáp án đúng, không trùng list cũ, nằm trong (0, 1)
                    if sai != float(kq_decimal) and sai not in s_vals and 0 < sai < 1:
                        s_vals.append(sai)

                da_d = '\\True $' + kq_str + '$'
                da_s1 = '$' + str(s_vals[0]).replace('.', ',') + '$'
                da_s2 = '$' + str(s_vals[1]).replace('.', ',') + '$'
                da_s3 = '$' + str(s_vals[2]).replace('.', ',') + '$'

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # --- BƯỚC 4: NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
                # Chuyển p1, p2 sang dạng % để in ra đề bài
                p1_percent = int(p1_val * 100)
                p2_percent = int(p2_val * 100)
                k_in = str(k).replace('.', ',')

                noidungcauhoi = ('''Thực hiện khảo sát tại một địa phương mà số trẻ em nam gấp %s lần số trẻ em nữ, có %s\\%% số trẻ em nam bị hen phế quản, %s\\%% số trẻ em nữ bị hen phế quản. Chọn ngẫu nhiên một trẻ em. Giả sử trẻ em được chọn bị hen phế quản. Xác suất chọn được trẻ em nam là bao nhiêu? (làm tròn kết quả đến hàng phần mười).'''
                                 % (k_in, p1_percent, p2_percent))

                loigiai = ('''Gọi $T$: "trẻ em được chọn là nam" và $H$: "trẻ em được chọn bị hen phế quản".\\\\
            Theo đề bài ta có $P(T) = %s$; $P(\\overline{T}) = %s$; $P(H|T) = %s$; $P(H|\\overline{T}) = %s$.\\\\
            Theo công thức Bayes, ta có:
            $$P(T|H) = \\frac{P(H|T) \\cdot P(T)}{P(H|T) \\cdot P(T) + P(H|\\overline{T}) \\cdot P(\\overline{T})} = \\frac{%s \\cdot %s}{%s \\cdot %s + %s \\cdot %s} \\approx %s.$$'''
                           % (latex(PT), latex(PnotT), str(p1_val).replace('.', ','), str(p2_val).replace('.', ','),
                              str(p1_val).replace('.', ','), latex(PT),
                              str(p1_val).replace('.', ','), latex(PT),
                              str(p2_val).replace('.', ','), latex(PnotT),
                              kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

            # --- BƯỚC 5: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

