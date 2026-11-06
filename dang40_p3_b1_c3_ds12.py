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


def bt_dang40_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Danh sách dạng (ở đây chỉ có 1 dạng theo yêu cầu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Tạo các hệ số ngẫu nhiên
                # f'(x) = (a*x + b)f(x). Chọn a_half = a/2
                a_half = random.randint(1, 3) 
                a = 2 * a_half
                b = random.randint(-5, 5)

                # f(x0) = e^(y0)
                x0 = random.randint(-2, 2)
                y0 = random.randint(1, 6)

                # Tính C: y0 = a_half * x0^2 + b * x0 + C
                C_val = y0 - (a_half * (x0**2) + b * x0)

                # Phương trình f(x) = e^(p*x^4 + q*x + r)
                # Để giống mẫu (triệt tiêu x), chọn q = b
                q = b
                p = random.randint(1, 3)
                r = random.randint(-5, 5)

                # 2. Giải phương trình tìm số nghiệm: p*x^4 - a_half*x^2 + (r - C) = 0
                # Đặt T = x^2 (T >= 0). Phương trình: p*T^2 - a_half*T + (r - C_val) = 0
                A = p
                B = -a_half
                K = r - C_val

                delta = B**2 - 4*A*K
                so_nghiem = 0

                if delta < 0:
                    so_nghiem = 0
                elif delta == 0:
                    t = -B / (2*A)
                    if t > 0: so_nghiem = 2
                    elif t == 0: so_nghiem = 1
                    else: so_nghiem = 0
                else:
                    t1 = (-B + sp.sqrt(delta)) / (2*A)
                    t2 = (-B - sp.sqrt(delta)) / (2*A)
                    # Kiểm tra nghiệm t1
                    if t1 > 0: so_nghiem += 2
                    elif t1 == 0: so_nghiem += 1
                    # Kiểm tra nghiệm t2
                    if t2 > 0: so_nghiem += 2
                    elif t2 == 0: so_nghiem += 1

                # 3. Chuẩn bị nội dung hiển thị
                kq = so_nghiem

                # Các đáp án trắc nghiệm (số nghiệm thường từ 0 đến 4)
                options = [0, 1, 2, 3, 4]
                if kq in options: options.remove(kq)
                random.shuffle(options)

                da_d = '\\True $%s$' % kq
                da_s1 = '$%s$' % options[0]
                da_s2 = '$%s$' % options[1]
                da_s3 = '$%s$' % options[2]

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # 4. Nội dung câu hỏi
                f_prime_expr = latex((a*x + b))
                target_exp = latex(p*x**4 + q*x + r)

                noidungcauhoi = (r'''Cho hàm số $y = f(x) > 0$ liên tục trên $\mathbb{R}$ và $f(%s) = e^{%s}$. Biết $f'(x) = (%s)f(x), \forall x \in \mathbb{R}$. Hỏi phương trình $f(x) = e^{%s}$ có bao nhiêu nghiệm?'''
                                 % (latex(x0), latex(y0), f_prime_expr, target_exp))

                # 5. Nội dung lời giải
                ln_f_expr = latex(a_half*x**2 + b*x)
                eq_final = latex(p*x**4 - a_half*x**2 + (r - C_val))

                loigiai = (r'''Ta có: $f'(x) = (%s)f(x) \Rightarrow \frac{f'(x)}{f(x)} = %s$ \\
                           $\Rightarrow \int \frac{f'(x)}{f(x)} dx = \int (%s) dx \Rightarrow \ln f(x) = %s + C$. \\
                           Theo giả thiết $f(%s) = e^{%s} \Rightarrow \ln f(%s) = %s$. \\
                           Thay $x = %s$ vào biểu thức $\ln f(x)$, ta được: \\
                           $%s = %s \cdot (%s)^2 + %s \cdot (%s) + C \Rightarrow C = %s$. \\
                           Vậy $\ln f(x) = %s + %s$. \\
                           Phương trình $f(x) = e^{%s} \Leftrightarrow \ln f(x) = %s$ \\
                           $\Leftrightarrow %s + %s = %s \Leftrightarrow %s = 0$. \\
                           Số nghiệm của phương trình là $%s$.'''
                           % (f_prime_expr, f_prime_expr, f_prime_expr, ln_f_expr,
                              latex(x0), latex(y0), latex(x0), latex(y0),
                              latex(x0), latex(y0), latex(a_half), latex(x0), latex(b), latex(x0), latex(C_val),
                              ln_f_expr, latex(C_val), target_exp, target_exp,
                              ln_f_expr, latex(C_val), target_exp, eq_final,
                              latex(kq)))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))  

            # Xuất câu trắc nghiệm ra định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

