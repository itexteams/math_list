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


def bt_dang36_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các thông số của bài toán
                # n là số mũ (từ 3 đến 6)
                n = random.randint(3, 6)
                # dx là số hạng bé Delta x (0.01, 0.02, 0.001, ...)
                list_dx = [0.01, 0.02, 0.03, 0.001, 0.002]
                dx = random.choice(list_dx)

                # Tính toán các giá trị
                x_val = 1
                tong_val = x_val + dx

                # Số hạng 1: C(n,0) * x^n = 1
                t1 = 1
                # Số hạng 2: C(n,1) * x^(n-1) * dx = n * dx
                t2 = n * dx

                # Kết quả gần đúng (2 số hạng đầu)
                kq_gan_dung = t1 + t2

                # Tạo các phương án nhiễu dựa trên việc lấy thêm số hạng (giống mẫu trong ảnh)
                # Phương án đúng (A trong ảnh): 2 số hạng đầu
                da_dung_val = kq_gan_dung

                # Các số hạng tiếp theo để tạo phương án sai (3 số hạng, 4 số hạng, hoặc giá trị chính xác)
                t3 = binomial(n, 2) * (dx**2)
                t4 = binomial(n, 3) * (dx**3)
                t_chinh_xac = (1 + dx)**n

                # Định dạng hiển thị số thập phân dùng dấu phẩy
                def format_vn(val):
                    s = "{:g}".format(float(val))
                    return s.replace('.', ',')

                # Các phương án trắc nghiệm
                da_d = '$%s$' % (format_vn(da_dung_val))

                # Tạo danh sách các phương án sai (B, C, D trong ảnh thường là lấy thêm các bậc cao hơn)
                s1 = '$%s$' % (format_vn(t1 + t2 + t3))
                s2 = '$%s$' % (format_vn(t1 + t2 + t3 + t4))
                s3 = '$%s$' % (format_vn(t_chinh_xac))

                # Đảm bảo không trùng lặp nếu n nhỏ hoặc dx nhỏ làm các giá trị bằng nhau
                s = list(set([s1, s2, s3]))
                while len(s) < 3:
                    nhieu = da_dung_val + random.choice([0.1, 0.05, -0.01])
                    s.append('$%s$' % (format_vn(nhieu)))

                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Dùng hai số hạng đầu tiên trong khai triển $\\left(x + \\Delta x\\right)^{%s}$ để tính gần đúng số $\\left(%s\\right)^{%s}$.'''
                                 % (latex(n), format_vn(tong_val), latex(n)))

                # Các đáp án
                da_true = ('\\True ' + str(da_d))
                list_1 = [da_true, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Chuyển đổi dx sang định dạng phẩy để in lời giải
                dx_str = format_vn(dx)
                kq_str = format_vn(da_dung_val)

                loigiai = ('''Ta có $\\left(%s\\right)^{%s} = \\left(1 + %s\\right)^{%s}$.\\\\
                             Khai triển nhị thức Newton: $\\left(1 + %s\\right)^{%s} = C_{%s}^0 + C_{%s}^1 \\cdot %s + C_{%s}^2 \\cdot %s^2 + \\dots + C_{%s}^{%s} \\cdot %s^{%s}$.\\\\
                             Dùng hai số hạng đầu tiên để tính gần đúng, ta được:\\\\
                             $\\left(%s\\right)^{%s} \\approx C_{%s}^0 + C_{%s}^1 \\cdot %s = 1 + %s \\cdot %s = %s$.'''
                           % (format_vn(tong_val), latex(n), dx_str, latex(n),
                              dx_str, latex(n), latex(n), latex(n), dx_str, latex(n), dx_str, latex(n), latex(n), dx_str, latex(n),
                              format_vn(tong_val), latex(n), latex(n), latex(n), dx_str, latex(n), dx_str, kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

