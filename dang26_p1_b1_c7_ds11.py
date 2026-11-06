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


def bt_dang26_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B1: Nghiên cứu đề bài và lời giải
            # Bài toán gốc: y = 1/(x-1) tại M(2,1). 
            # Tiếp tuyến: y = -1(x-2) + 1 = -x + 3. 
            # Giao Ox tại (3,0), Oy tại (0,3). Diện tích = 1/2 * 3 * 3 = 9/2.

            # B3: Suy nghĩ tìm cách random bài toán
            # Để số liệu đẹp (nguyên hoặc phân số đơn giản), ta chọn x0 và a sao cho (x0 - a) là số nhỏ.
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tham số k / (x - a)
                k = random.choice([-2, -1, 1, 2, 3])
                a = random.randint(-3, 3)

                # Chọn x0 sao cho x0 != a. Ưu tiên (x0-a) = 1, -1, 2 hoặc -2 để đạo hàm đẹp
                delta_x = random.choice([-2, -1, 1, 2])
                x0 = a + delta_x

                # Tính y0
                f = k / (x - a)
                y0 = f.subs(x, x0)

                # Đạo hàm và hệ số góc m
                f_prime = sp.diff(f, x)
                m = f_prime.subs(x, x0)

                # Phương trình tiếp tuyến: y = m(x - x0) + y0
                # Rút gọn về dạng y = mx + c
                c = simplify(y0 - m * x0)
                pttt_expr = simplify(m*x + c)

                # Giao điểm với Ox (y=0 -> x = -c/m)
                xa = simplify(-c / m)
                # Giao điểm với Oy (x=0 -> y = c)
                yb = c

                # Diện tích S = 1/2 * |xa| * |yb|
                S = simplify(Rational(1, 2) * abs(xa) * abs(yb))

                # Đáp án đúng
                da = '$%s$' % latex(S)

                # Tạo các đáp án nhiễu
                s = set()
                while len(s) < 3:
                    nhieu = random.choice([S + Rational(1, 2), S + 1, S * 2, S / 2, S + 2, S + Rational(3, 2)])
                    if nhieu != S and nhieu > 0:
                        s.add('$%s$' % latex(nhieu))

                list_nhieu = list(s)
                das1, das2, das3 = list_nhieu[0], list_nhieu[1], list_nhieu[2]

                # B2: Viết lại đề bài và lời giải theo mẫu code
                noidungcauhoi = (r'''Cho hàm số $y = \frac{%s}{x %s}$ có đồ thị $(C)$. Gọi $\Delta$ là tiếp tuyến của $(C)$ tại điểm $M(%s;%s)$. Diện tích tam giác được tạo bởi $\Delta$ và các trục bằng'''
                                 % (latex(k), latex(-a) if -a < 0 else '+ ' + latex(-a), latex(x0), latex(y0)))

                # Xử lý hiển thị dấu cho phương trình tiếp tuyến
                # Sử dụng sp.latex trực tiếp trên biểu thức để tự động xử lý +- và --
                pttt_str = latex(pttt_expr)

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                loigiai = (r'''Ta có $y' = %s$. \\
                           Tại điểm $x_0 = %s$, ta có $y_0 = %s$ và $y'(%s) = %s$. \\
                           Suy ra phương trình tiếp tuyến $\Delta$ là: $y = %s$. \\
                           Tiếp tuyến $\Delta$ cắt các trục $Ox, Oy$ lần lượt tại $A(%s;0), B(0;%s)$. \\
                           Do đó diện tích tam giác được tạo bởi $\Delta$ và các trục tọa độ bằng: \\
                           $S = \frac{1}{2} \cdot OA \cdot OB = \frac{1}{2} \cdot |%s| \cdot |%s| = %s$.'''
                           % (latex(f_prime), latex(x0), latex(y0), latex(x0), latex(m),
                              pttt_str, latex(xa), latex(yb), latex(xa), latex(yb), latex(S)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

