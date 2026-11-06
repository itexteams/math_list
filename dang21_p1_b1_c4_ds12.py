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


def bt_dang21_p1_b1_c4_ds12(self):
            # BƯỚC 1 & 3: Thiết lập biến ngẫu nhiên bằng Rational để tránh sai số
            while True:
                # Tạo các số nguyên trước rồi mới chia để có phân số chính xác
                pb_num = random.randint(2, 8)
                pb_val = Rational(pb_num, 10) # P(B) = 0.2 đến 0.8

                p_a_given_b_num = random.randint(1, 6)
                p_a_given_b_val = Rational(p_a_given_b_num, 10) # P(A|B)

                # P(A giao B) = P(B) * P(A|B)
                pa_giao_b = pb_val * p_a_given_b_val

                # P(A) phải lớn hơn P(A giao B) và <= 0.9
                # Chuyển pa_giao_b về số thực để lấy giới hạn dưới
                lower_limit = int(float(pa_giao_b) * 10) + 1
                if lower_limit <= 9:
                    pa_num = random.randint(lower_limit, 9)
                    pa_val = Rational(pa_num, 10)

                    # Tính kết quả P(B|A) = P(A giao B) / P(A)
                    kq_frac = pa_giao_b / pa_val

                    if kq_frac < 1:
                        break

            # Hàm phụ để hiển thị số thập phân kiểu VN (dùng dấu phẩy)
            def format_dec(val):
                return str(float(val)).replace('.', ',').rstrip('0').rstrip(',')

            # Đáp án đúng (Rút gọn tự động bởi sympy)
            da = '$%s$' % (latex(kq_frac))

            # BƯỚC 4: Tạo các phương án sai
            s = set()
            while len(s) < 3:
                tu = random.randint(1, 15)
                mau = random.randint(tu + 1, 30)
                gia_tri_sai = Rational(tu, mau)
                if gia_tri_sai != kq_frac:
                    s.add('$%s$' % (latex(gia_tri_sai)))

            list_sai = list(s)
            das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

            # BƯỚC 2: Viết nội dung câu hỏi
            noidungcauhoi = (r'''Cho hai biến cố $A, B$ sao cho $P(A) = %s; P(B) = %s; P(A|B) = %s$. Khi đó $P(B|A)$ bằng'''
                             % (format_dec(pa_val), format_dec(pb_val), format_dec(p_a_given_b_val)))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = (r'''Ta có công thức xác suất có điều kiện: $P(A \cap B) = P(B) \cdot P(A|B) = %s \cdot %s = %s$. \\
                         Khi đó, xác suất của biến cố $B$ với điều kiện biến cố $A$ đã xảy ra là: \\
                         $P(B|A) = \frac{P(A \cap B)}{P(A)} = \frac{P(B) \cdot P(A|B)}{P(A)} = \frac{%s \cdot %s}{%s} = %s$.'''
                       % (format_dec(pb_val), 
                          format_dec(p_a_given_b_val), 
                          format_dec(pa_giao_b),
                          format_dec(pb_val), 
                          format_dec(p_a_given_b_val), 
                          format_dec(pa_val), 
                          latex(kq_frac)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

