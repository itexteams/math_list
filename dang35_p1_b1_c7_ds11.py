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


def bt_dang35_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến x0
            x0 = symbols('x0')

            # Khai báo danh sách dạng (ở đây chỉ có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Tìm cách random bài toán
                # Để đảm bảo có 2 tiếp tuyến và nghiệm x0 đẹp (nguyên), ta chọn 2 nghiệm x01, x02 trước
                # Chọn x01, x02 sao cho tổng của chúng là số chẵn để điểm A có hoành độ nguyên
                while True:
                    x01 = randint(-5, 5)
                    x02 = randint(-5, 5)
                    if x01 != x02 and (x01 + x02) % 2 == 0:
                        break

                a = 1 # Giữ hệ số a=1 giống trong ảnh cho đơn giản
                b = randint(-6, 6)
                c = randint(-6, 6)

                # Tính hoành độ điểm A: x_A = (x01 + x02) / 2
                xa = (x01 + x02) // 2

                # Hàm số f(x) = ax^2 + bx + c
                f = a*x**2 + b*x + c
                f_prime = diff(f, x)

                # Tính tung độ yA dựa trên điều kiện tiếp tuyến đi qua A
                # yA = f'(x01)*(xa - x01) + f(x01)
                ya = (2*a*x01 + b)*(xa - x01) + a*x01**2 + b*x01 + c

                # Thành phần cho lời giải
                f_latex = latex(f)
                f_prime_latex = latex(f_prime)

                # Biểu thức f(x0) và f'(x0)
                f_x0 = a*x0**2 + b*x0 + c
                f_prime_x0 = 2*a*x0 + b

                # Phương trình tiếp tuyến tại M(x0, y0)
                # y = f'(x0)(x - x0) + f(x0)
                pttt_ve_phai = (f_prime_x0)*(x - x0) + f_x0

                # Khi đi qua A(xa, ya)
                # ya = (2*a*x0 + b)*(xa - x0) + a*x0**2 + b*x0 + c
                # Khai triển vế trái để viết loigiai chi tiết
                # (2ax0 + b)(xa - x0) = 2ax_a.x0 - 2ax0^2 + b.xa - b.x0
                term1 = 2*a*xa  # hệ số của x0 trong (f'x0)(xa-x0)
                term2 = -2*a    # hệ số của x0^2
                term3 = b*xa    # hằng số
                term4 = -b      # hệ số của x0

                # Phương trình bậc 2 theo x0: -ax0^2 + (2axa)x0 + (bxa + c - ya) = 0
                coeff_x0_2 = -a
                coeff_x0 = 2*a*xa
                const_term = b*xa + c - ya

                # Giải x0
                roots = sorted([x01, x02])

                # Tính các thông số cho từng tiếp tuyến để đưa vào lời giải
                res_list = []
                for r in roots:
                    y0_val = a*r**2 + b*r + c
                    k_val = 2*a*r + b
                    # pt: y = k(x - r) + y0_val => y = kx - k*r + y0_val
                    b_line = -k_val*r + y0_val
                    line_eq = "y = " + latex(k_val*x + b_line)
                    res_list.append({'x0': r, 'y0': y0_val, 'k': k_val, 'line': line_eq})

                # Câu hỏi
                noidungcauhoi = ('''Số tiếp tuyến của đồ thị hàm số $y = %s$ qua điểm $A\\left(%s;%s\\right)$ là'''
                                 %(f_latex, latex(xa), latex(ya)))

                # Đáp án đúng
                kq = 2
                da_d = ('\\True ' + str(kq))

                # Bước 4: Điều chỉnh các phương án sai
                s = [0, 1, 3]
                random.shuffle(s)
                da_s1 = str(s[0])
                da_s2 = str(s[1])
                da_s3 = str(s[2])

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B1, B2)
                loigiai = ('''Gọi $M\\left(x_0;y_0\\right)$ là tiếp điểm. \\\\
                             $y' = %s$. \\\\
                             Suy ra phương trình tiếp tuyến cần tìm là $y = \\left(%s\\right)\\left(x - x_0\\right) + %s$. \\\\
                             Vì tiếp tuyến này qua $A\\left(%s;%s\\right)$ nên $\\left(%s\\right)\\left(%s - x_0\\right) + %s = %s$ \\\\
                             $\\Leftrightarrow %sx_0 %sx_0^2 %s %sx_0 + %s x_0^2 %s x_0 + %s = %s$ \\\\
                             $\\Leftrightarrow %sx_0^2 + %sx_0 + %s = 0 \\Leftrightarrow \\left[\\begin{aligned} & x_0 = %s \\\\ & x_0 = %s \\end{aligned}\\right.$. \\\\
                             Với $x_0 = %s \\Rightarrow \\left\\{\\begin{aligned} & y_0 = %s \\\\ & y'\\left(x_0\\right) = %s \\end{aligned}\\right.$ thì phương trình tiếp tuyến là $%s$. \\\\
                             Với $x_0 = %s \\Rightarrow \\left\\{\\begin{aligned} & y_0 = %s \\\\ & y'\\left(x_0\\right) = %s \\end{aligned}\\right.$ thì phương trình tiếp tuyến là $%s$.'''
                           %(f_prime_latex, 
                             latex(f_prime_x0), latex(f_x0),
                             latex(xa), latex(ya),
                             latex(f_prime_x0), latex(xa), latex(f_x0), latex(ya),
                             latex(term1) if term1 != 0 else "", 
                             latex(term2), 
                             "+" + latex(term3) if term3 >= 0 else latex(term3),
                             "+" + latex(term4) if term4 >= 0 else latex(term4),
                             "+" + latex(a) if a != 1 else "",
                             "+" + latex(b) if b >= 0 else latex(b),
                             "+" + latex(c) if c >= 0 else latex(c),
                             latex(ya),
                             latex(coeff_x0_2), latex(coeff_x0), latex(const_term),
                             latex(roots[0]), latex(roots[1]),
                             latex(res_list[0]['x0']), latex(res_list[0]['y0']), latex(res_list[0]['k']), res_list[0]['line'],
                             latex(res_list[1]['x0']), latex(res_list[1]['y0']), latex(res_list[1]['k']), res_list[1]['line']
                            ))

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

