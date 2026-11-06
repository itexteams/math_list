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


def bt_dang34_p4_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x = symbols('x')
                # --- BƯỚC RANDOM BÀI TOÁN ---
                # Tìm một phương trình bậc 3 có 3 nghiệm phân biệt và tìm 4 điểm đổi dấu
                found = False
                while not found:
                    # Tạo phương trình ax^3 + bx + c
                    a = random.randint(1, 2)
                    # Chọn 3 nghiệm nguyên tạm thời để đảm bảo đồ thị cắt trục hoành 3 lần
                    roots = sorted(random.sample(range(-4, 5), 3))
                    # Khai triển (x-r1)(x-r2)(x-r3) và thêm hằng số tự do c để số không quá "đẹp"
                    expr_temp = a * (x - roots[0]) * (x - roots[1]) * (x - roots[2])
                    f_expr = expand(expr_temp) + random.randint(-2, 2)

                    # Quét các điểm nguyên từ -8 đến 8 để tìm các khoảng đổi dấu
                    pts = []
                    vals = []
                    for i in range(-8, 9):
                        v = int(f_expr.subs(x, i))
                        if v != 0:
                            if not pts or (v * vals[-1] < 0):
                                pts.append(i)
                                vals.append(v)
                        if len(pts) == 4:
                            found = True
                            break

                # Gán các giá trị tìm được vào biến để đưa vào lời giải
                v1, v2, v3, v4 = pts
                f1, f2, f3, f4 = vals

                # Hàm định dạng hiển thị giá trị số kèm dấu so sánh với 0
                def fmt(val):
                    return f"{val} > 0" if val > 0 else f"{val} < 0"

                # --- ĐÁP ÁN ---
                # Kết quả đúng
                da = "Phương trình có đúng 3 nghiệm trên $\\mathbb{R}$"

                # Các đáp án trắc nghiệm sai
                s = [
                    "Phương trình vô nghiệm",
                    "Phương trình có đúng 1 nghiệm thực",
                    "Phương trình có đúng 2 nghiệm thực",
                    "Phương trình có vô số nghiệm"
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (r'''Cho phương trình $%s = 0$ (1). Tìm số nghiệm của phương trình.'''
                                 %(latex(f_expr)))

                # --- CÁC ĐÁP ÁN ---
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- NỘI DUNG LỜI GIẢI (Y hệt mẫu hình ảnh) ---
                loigiai = (r'''Hàm số $f(x) = %s$ liên tục trên $\mathbb{R}$. \\
                             Do $f(%s) = %s, f(%s) = %s, f(%s) = %s, f(%s) = %s$ nên phương trình có ít nhất 3 nghiệm trên $(%s;%s), (%s;%s), (%s;%s)$. \\
                             Mà phương trình bậc ba có tối đa 3 nghiệm nên phương trình có đúng 3 nghiệm trên $\mathbb{R}$.'''
                           %(latex(f_expr), 
                             v1, f1, v2, fmt(f2), v3, fmt(f3), v4, fmt(f4),
                             v1, v2, v2, v3, v3, v4))

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

