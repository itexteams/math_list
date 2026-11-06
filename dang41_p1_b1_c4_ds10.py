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


def bt_dang41_p1_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến m cho sympy
            m_sym = symbols('m')

            # Khai báo danh sách dạng (ở đây có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM ---
                # Hàm số: y = sqrt(a1*x + b1*m + c1) + (x - m)/(x + b2*m + c2)
                # Khoảng xác định yêu cầu: x thuộc (k; +inf). Ở đây lấy k = 0 như đề bài.
                k = 0

                # Random các hệ số sao cho bài toán có nghiệm đẹp và hợp lý
                # Điều kiện 1: a1*x >= -b1*m - c1  => x >= (-b1*m - c1)/a1
                # Để xác định trên (0, +inf) thì (-b1*m - c1)/a1 <= 0

                a1 = 2 # Giữ cố định cho giống mẫu hoặc random số nguyên dương
                b1 = randint(-5, -2) # b1 âm để khi chuyển vế m có dấu <=
                c1 = randint(2, 6)

                # Điều kiện 2: x != -b2*m - c2. Để x thuộc (0, +inf) thì -b2*m - c2 <= 0
                b2 = randint(1, 3) # b2 dương để m có dấu >=
                c2 = randint(-4, -1) # c2 âm

                # Tính toán các giá trị biên
                # Biên 1: (-b1*m - c1)/a1 <= 0  <=> -b1*m <= c1 <=> m <= c1/(-b1)
                bien_tren = Rational(c1, -b1)

                # Biên 2: -b2*m - c2 <= 0 <=> -b2*m <= c2 <=> m >= -c2/b2
                bien_duoi = Rational(-c2, b2)

                # Đảm bảo bien_duoi < bien_tren để có khoảng nghiệm
                if bien_duoi >= bien_tren:
                    # Swap hoặc điều chỉnh nhanh để có kết quả
                    bien_duoi, bien_tren = bien_tren, bien_duoi
                    if bien_duoi == bien_tren: bien_tren += 1

                # --- ĐÁP ÁN ĐÚNG ---
                kq_dung = r'%s \le m \le %s' % (latex(bien_duoi), latex(bien_tren))
                da = '$%s$' % kq_dung

                # --- BƯỚC 4: ĐIỀU CHỈNH CÁC PHƯƠNG ÁN SAI ---
                s = [
                    '$%s < m < %s$' % (latex(bien_duoi), latex(bien_tren)),
                    '$m \\le %s$' % (latex(bien_tren)),
                    '$m \\ge %s$' % (latex(bien_duoi)),
                    '$%s \\le m \\le %s$' % (latex(bien_duoi - 1), latex(bien_tren)),
                    '$%s \\le m \\le %s$' % (latex(bien_duoi), latex(bien_tren + 1)),
                    '$m \\in \\emptyset$'
                ]

                # Lấy ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- BƯỚC 2: VIẾT LẠI BÀI TOÁN THEO MẪU ---
                # Biểu thức hiển thị
                f_sqrt = latex(a1) + 'x' + ('' if b1 == 0 else ('+' if b1 > 0 else '') + latex(b1) + 'm') + ('+' if c1 > 0 else '') + latex(c1)
                f_mau = 'x' + ('' if b2 == 0 else ('+' if b2 > 0 else '') + latex(b2) + 'm') + ('+' if c2 > 0 else '') + latex(c2)

                noidungcauhoi = (r'Giá trị của $m$ để hàm số $y = \sqrt{%s} + \frac{x - m}{%s}$ xác định với mọi $x$ thuộc khoảng $(0; +\infty)$ là'
                                 % (f_sqrt, f_mau))

                # Nội dung lời giải
                # Giải chi tiết điều kiện
                # x >= ( -b1*m - c1 ) / a1
                ve_phai_1 = Rational(-b1, a1) # hệ số của m
                hang_so_1 = Rational(-c1, a1)

                # x != -b2*m - c2
                ve_phai_2 = -b2 # hệ số m
                hang_so_2 = -c2

                loigiai = (r'''Hàm số xác định khi $\begin{cases} %s \ge 0 \\ %s \neq 0 \end{cases} \Leftrightarrow \begin{cases} x \ge \frac{%s m %s}{%s} \\ x \neq %s m %s \end{cases}$. \\
                             Do đó để hàm số xác định với mọi $x$ thuộc khoảng $(0; +\infty)$, ta phải có \\
                             $\begin{cases} \frac{%s m %s}{%s} \le 0 \\ %s m %s \le 0 \end{cases} \Leftrightarrow \begin{cases} m \le %s \\ m \ge %s \end{cases} \Leftrightarrow %s \le m \le %s$. \\
                             Vậy $%s \le m \le %s$ thỏa mãn yêu cầu bài toán.'''
                           % (f_sqrt, f_mau, latex(-b1), latex(-c1), latex(a1), latex(-b2), latex(-c2),
                              latex(-b1), latex(-c1), latex(a1), latex(-b2), latex(-c2), 
                              latex(bien_tren), latex(bien_duoi), latex(bien_duoi), latex(bien_tren),
                              latex(bien_duoi), latex(bien_tren)
                             ))

                # Xuất câu trắc nghiệm
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

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

