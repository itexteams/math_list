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


def bt_dang46_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- BƯỚC RANDOM THÔNG SỐ ---
            # C: Giá mua vào, P0: Giá bán cũ, Q0: Số xe bán cũ, k: Hệ số tăng khi giảm giá
            C = random.randint(8, 15)
            margin = random.randint(2, 5)
            P0 = C + margin
            Q0 = random.choice([40, 50, 60, 80, 100])
            k = random.choice([10, 15, 20, 25, 30])

            # --- TÍNH TOÁN CÁC BIỂU THỨC ---
            # 1. Số xe bán được: Q = Q0 + k * (P0 - x) = (Q0 + k*P0) - k*x
            Q_expr = (Q0 + k*P0) - k*x
            coeff_Q_const = Q0 + k*P0
            coeff_Q_x = k

            # 2. Lợi nhuận: f(x) = (x - C) * Q_expr
            f_expr = sp.expand((x - C) * Q_expr)
            # Lấy các hệ số của f(x) = ax^2 + bx + c
            a_f = sp.Poly(f_expr, x).coeffs()[0]
            b_f = sp.Poly(f_expr, x).coeffs()[1]
            c_f = sp.Poly(f_expr, x).coeffs()[2]

            # 3. Tìm giá trị lớn nhất
            x_max = Rational(-b_f, 2*a_f)
            f_max = f_expr.subs(x, x_max)

            # Hàm chuyển đổi dấu chấm thành dấu phẩy cho số thập phân
            def fmt(val):
                s = str(val)
                if '/' in s: # Nếu là phân số sympy
                    s = str(float(val))
                return s.replace('.', ',')

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Một công ty chuyên kinh doanh xe máy điện các loại. Hiện nay công ty đang kinh doanh loại xe máy điện A với chi phí mua vào là $%s$ triệu, bán ra là $%s$ triệu. Với giá bán này thì số xe máy điện loại A bán được trong một tháng là $%s$ chiếc. Nhằm đẩy mạnh hơn nữa doanh số tiêu thụ loại xe này trong một tháng, công ty dự định giảm giá bán và ước tính rằng nếu giảm $1$ triệu đồng mỗi xe thì số lượng xe bán ra trong một tháng sẽ tăng $%s$ chiếc. Gọi giá bán mới của chiếc xe máy điện A là $x$ ($%s \\le x \\le %s$). ''' 
                             % (fmt(C), fmt(P0), fmt(Q0), fmt(k), fmt(C), fmt(P0)))

            # --- CÁC ĐÁP ÁN VÀ LỜI GIẢI ---

            # a) Số xe máy điện
            da_a_d = '\\True Số xe máy điện A mà công ty bán được trong một tháng là $%s - %s x$' % (fmt(coeff_Q_const), fmt(coeff_Q_x))
            da_a_s = 'Số xe máy điện A mà công ty bán được trong một tháng là $%s - %s x$' % (fmt(coeff_Q_const - 5), fmt(coeff_Q_x - 5))
            list_a = [da_a_d, da_a_s]
            choice_a = random.choice(list_a)
            sol_a = ('''Nếu giảm $1$ triệu đồng thì số xe tăng $%s$, nên nếu giảm $(%s - x)$ triệu đồng thì số xe tăng thêm là $%s(%s - x)$. \\\\ Số xe bán được trong một tháng là: $Q(x) = %s + %s(%s - x) = %s - %s x$.''' 
                     % (fmt(k), fmt(P0), fmt(k), fmt(P0), fmt(Q0), fmt(k), fmt(P0), fmt(coeff_Q_const), fmt(coeff_Q_x)))

            # b) Hàm lợi nhuận
            da_b_d = '\\True Lợi nhuận thu được trong một tháng của công ty là $f(x) = %s x^2 + %s x %s$' % (fmt(a_f), fmt(b_f), fmt(c_f) if c_f < 0 else '+ ' + fmt(c_f))
            da_b_s = 'Lợi nhuận thu được trong một tháng của công ty là $f(x) = %s x^2 + %s x %s$' % (fmt(a_f), fmt(b_f - 25), fmt(c_f + 100))
            list_b = [da_b_d, da_b_s]
            choice_b = random.choice(list_b)
            sol_b = ('''Lợi nhuận = (Giá bán - Giá mua) $\\times$ Số lượng. \\\\ $f(x) = (x - %s)(%s - %s x) = %s x^2 + %s x %s$.''' 
                     % (fmt(C), fmt(coeff_Q_const), fmt(coeff_Q_x), fmt(a_f), fmt(b_f), fmt(c_f) if c_f < 0 else '+ ' + fmt(c_f)))

            # c) So sánh lợi nhuận max (Phủ định)
            target_c = float(f_max) - 6.25
            da_c_d = '\\True Lợi nhuận thu được lớn nhất của công ty trong một tháng có thể đạt trên $%s$ triệu đồng' % (fmt(target_c))
            da_c_s = 'Lợi nhuận thu được lớn nhất của công ty trong một tháng không thể đạt $%s$ triệu đồng' % (fmt(target_c))
            list_c = [da_c_d, da_c_s]
            choice_c = random.choice(list_c)
            sol_c = ('''Xét hàm lợi nhuận $f(x) = %s x^2 + %s x %s$ trên đoạn $[%s; %s]$. \\\\ Ta tìm được giá trị lớn nhất của hàm số tại $x = %s$.''' 
                     % (fmt(a_f), fmt(b_f), fmt(c_f) if c_f < 0 else '+ ' + fmt(c_f), fmt(C), fmt(P0), fmt(x_max)))

            # d) Giá trị lợi nhuận max
            da_d_d = '\\True Lợi nhuận thu được lớn nhất của công ty trong một tháng là $%s$ triệu đồng' % (fmt(f_max))
            da_d_s = 'Lợi nhuận thu được lớn nhất của công ty trong một tháng là $%s$ triệu đồng' % (fmt(float(f_max) - 10))
            list_d = [da_d_d, da_d_s]
            choice_d = random.choice(list_d)
            sol_d = ('''Tọa độ đỉnh của parabol là $x = \\frac{-b}{2a} = \\frac{-%s}{2 \\cdot (%s)} = %s$. \\\\ Vì $x = %s \\in [%s; %s]$ nên giá trị lớn nhất của lợi nhuận là $f(%s) = %s$ triệu đồng.''' 
                     % (fmt(b_f), fmt(a_f), fmt(x_max), fmt(x_max), fmt(C), fmt(P0), fmt(x_max), fmt(f_max)))

            # --- KIỂM TRA SỐ CÂU ĐÚNG (1-3) ---
            while True:
                ans_a = random.choice(list_a)
                ans_b = random.choice(list_b)
                ans_c = random.choice(list_c)
                ans_d = random.choice(list_d)

                true_count = sum('\\True' in ans for ans in [ans_a, ans_b, ans_c, ans_d])
                if 1 <= true_count <= 3:
                    break

            # --- XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sol_a) + '\n'
                '\\item ' + str(sol_b) + '\n'
                '\\item ' + str(sol_c) + '\n'
                '\\item ' + str(sol_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

