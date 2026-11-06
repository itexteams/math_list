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


def bt_dang31_p1_b1_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Hàm kiểm tra số chính phương để tránh sqrt(4), sqrt(9)...
                def is_perfect_square(n):
                    return math.isqrt(n)**2 == n

                # Tạo cơ số ngẫu nhiên dạng sqrt(k) - p hoặc p - sqrt(k) hoặc sqrt(k) + p
                valid_base = False
                while not valid_base:
                    k = random.randint(2, 15) # Số dưới dấu căn
                    if is_perfect_square(k): continue

                    p = random.randint(1, 3) # Số nguyên đi kèm
                    hinh_thuc = random.choice(['sqrt-p', 'p-sqrt', 'sqrt+p'])

                    if hinh_thuc == 'sqrt-p':
                        coso_sympy = sqrt(k) - p
                    elif hinh_thuc == 'p-sqrt':
                        coso_sympy = p - sqrt(k)
                    else:
                        coso_sympy = sqrt(k) + p

                    # Tính giá trị xấp xỉ để phân loại
                    val_a = float(coso_sympy.evalf())

                    # Điều kiện: cơ số phải dương và không bằng 1
                    if val_a > 0 and abs(val_a - 1) > 0.01:
                        valid_base = True
                        a_tex = latex(coso_sympy)

                        # Phân loại để viết lời giải y hệt ảnh
                        if 0 < val_a < 1:
                            is_small_base = True
                            dk_tex = r"0 < %s < 1" % a_tex
                        else:
                            is_small_base = False
                            dk_tex = r"%s > 1" % a_tex

                # Chọn ngẫu nhiên dấu bất đẳng thức đề bài: '<' hoặc '>'
                ds_dau = ['<', '>']
                dau_de = random.choice(ds_dau)

                # Logic so sánh mũ (đúng theo tính chất lũy thừa)
                if is_small_base:
                    # Nếu 0 < a < 1: Đổi chiều bất đẳng thức
                    kq_m_n = 'm > n' if dau_de == '<' else 'm < n'
                else:
                    # Nếu a > 1: Giữ nguyên chiều
                    kq_m_n = 'm < n' if dau_de == '<' else 'm > n'

                # Đáp án đúng
                da_dung = '$%s$' % kq_m_n

                # Tạo danh sách các phương án nhiễu
                s_options = ['$m < n$', '$m > n$', '$m = n$', '$m \\le n$', '$m \\ge n$']
                if da_dung in s_options:
                    s_options.remove(da_dung)

                random.shuffle(s_options)
                das1, das2, das3 = s_options[:3]

                # Nội dung câu hỏi
                noidungcauhoi = (r'Cho $\left(%s\right)^m %s \left(%s\right)^n$. Khi đó'
                                 % (a_tex, dau_de, a_tex))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Lời giải y hệt mẫu ảnh bạn cung cấp
                loigiai = (r'Do $%s$ nên $\left(%s\right)^m %s \left(%s\right)^n \Leftrightarrow %s$.'
                           % (dk_tex, a_tex, dau_de, a_tex, kq_m_n))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

