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


def bt_dang15_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y, t = symbols('x y t')

            # --- BƯỚC 1: KHỞI TẠO DỮ LIỆU NGẪU NHIÊN ---
            # Đường thẳng Delta: x = x0 + u1*t, y = y0 + u2*t
            u1 = random.choice([-3, -2, -1, 1, 2, 3])
            u2 = random.choice([-3, -2, -1, 1, 2, 3])
            x0 = random.randint(-5, 5)
            y0 = random.randint(-5, 5)

            # Điểm A(xA, yA)
            xA = random.randint(-5, 5)
            yA = random.randint(-5, 5)

            # Chuyển Delta sang dạng tổng quát: u2(x - x0) - u1(y - y0) = 0 <=> Ax + By + C = 0
            A_dt = u2
            B_dt = -u1
            C_dt = -u2*x0 + u1*y0

            # Hàm hỗ trợ viết phương trình đẹp (xử lý dấu + -)
            def format_eq(A, B, C):
                def term(coeff, var):
                    if coeff == 0: return ""
                    if coeff == 1: return " + " + var
                    if coeff == -1: return " - " + var
                    return (" + " if coeff > 0 else " - ") + str(abs(coeff)) + var

                eq = term(A, "x") + term(B, "y")
                if C != 0:
                    eq += (" + " if C > 0 else " - ") + str(abs(C))
                eq += " = 0"
                # Xóa dấu "+" ở đầu nếu có
                if eq.startswith(" + "): eq = eq[3:]
                return eq

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $\\left( Oxy \\right)$, cho đường thẳng $\\Delta : \\begin{cases} x = %s %s %s t \\\\ y = %s %s %s t \\end{cases} \\left( t \\in \\mathbb{R} \\right)$ và điểm $A\\left( %s; %s \\right)$.''' 
                             % (latex(x0), '+' if u1 > 0 else '-', latex(abs(u1)), 
                                latex(y0), '+' if u2 > 0 else '-', latex(abs(u2)), 
                                latex(xA), latex(yA)))

            ########################################################################
            # a) Nhận biết: Đường thẳng vuông góc
            # d1 vuông góc Delta => n_d1 cùng phương u_Delta = (u1, u2)
            d1_A, d1_B = u1, u2
            d1_C = random.randint(-10, 10)
            eq_d1 = format_eq(d1_A, d1_B, d1_C)

            nb_da_1_d = '\\True Đường thẳng $d_1 : %s$ vuông góc với đường thẳng $\\Delta$' % eq_d1
            nb_da_1_s = 'Đường thẳng $d_1 : %s$ song song với đường thẳng $\\Delta$' % eq_d1

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Đường thẳng $\\Delta$ có vectơ chỉ phương $\\vec{u}_{\\Delta} = \\left( %s; %s \\right)$. \\\\
                            Đường thẳng $d_1$ có vectơ pháp tuyến $\\vec{n}_{d_1} = \\left( %s; %s \\right)$. \\\\
                            Ta thấy $\\vec{n}_{d_1} = \\vec{u}_{\\Delta}$ nên $d_1 \\perp \\Delta$.''' 
                            % (latex(u1), latex(u2), latex(d1_A), latex(d1_B)))

            ########################################################################
            # b) Thông hiểu: Khoảng cách
            dist_num = abs(A_dt * xA + B_dt * yA + C_dt)
            dist_den_sq = A_dt**2 + B_dt**2
            dist_val = Rational(dist_num, 1) / sqrt(dist_den_sq)

            th_da_1_d = '\\True $d\\left( A, \\Delta \\right) = %s$' % latex(dist_val)
            th_da_1_s = '$d\\left( A, \\Delta \\right) = %s$' % latex(dist_val * 2)

            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Phương trình tổng quát của $\\Delta$ là: $%s\\left( x - %s \\right) %s %s\\left( y - %s \\right) = 0 \\Leftrightarrow %s$. \\\\
                            Khoảng cách từ điểm $A$ đến đường thẳng $\\Delta$ là: \\\\
                            $d\\left( A, \\Delta \\right) = \\frac{\\left| %s \\cdot \\left( %s \\right) %s %s \\cdot \\left( %s \\right) %s %s \\right|}{\\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2}} = %s$.''' 
                            % (latex(A_dt), latex(x0), '+' if -u1 > 0 else '', latex(-u1), latex(y0), format_eq(A_dt, B_dt, C_dt),
                               latex(A_dt), latex(xA), '+' if B_dt > 0 else '', latex(B_dt), latex(yA), '+' if C_dt > 0 else '', latex(C_dt),
                               latex(A_dt), latex(B_dt), latex(dist_val)))

            ########################################################################
            # c) Vận dụng: Đường thẳng song song qua A
            # d2: A_dt(x - xA) + B_dt(y - yA) = 0
            d2_C = -A_dt * xA - B_dt * yA
            eq_d2 = format_eq(A_dt, B_dt, d2_C)

            vd_da_1_d = '\\True Đường thẳng $d_2 : %s$ đi qua điểm $A$ và song song với đường thẳng $\\Delta$' % eq_d2
            vd_da_1_s = 'Đường thẳng $d_2 : %s$ đi qua điểm $A$ và vuông góc với đường thẳng $\\Delta$' % eq_d2

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Đường thẳng $d_2$ song song với $\\Delta$ nên có vectơ pháp tuyến $\\vec{n}_{d_2} = \\vec{n}_{\\Delta} = \\left( %s; %s \\right)$. \\\\
                            Vì $d_2$ đi qua $A\\left( %s; %s \\right)$ nên có phương trình: \\\\
                            $%s\\left( x - %s \\right) %s %s\\left( y - %s \\right) = 0 \\Leftrightarrow %s$.''' 
                            % (latex(A_dt), latex(B_dt), latex(xA), latex(yA),
                               latex(A_dt), latex(xA), '+' if B_dt > 0 else '', latex(B_dt), latex(yA), eq_d2))

            ########################################################################
            # d) Vận dụng cao: Góc 45 độ và hệ số góc
            # k_delta = u2/u1. Tan(45) = |(k-k_d)/(1+k*k_d)| = 1
            k_delta = Rational(u2, u1)
            # k1 = (1+k_d)/(1-k_d), k2 = (k_d-1)/(1+k_d)
            k_cands = []
            if k_delta != 1: k_cands.append((1 + k_delta) / (1 - k_delta))
            if k_delta != -1: k_cands.append((k_delta - 1) / (1 + k_delta))

            # Lấy k dương
            k_pos = [k for k in k_cands if k > 0]
            k_val = k_pos[0] if k_pos else Rational(1, 1)

            # Phương trình d3: y - yA = k_val(x - xA) <=> k_val*x - y + (yA - k_val*xA) = 0
            # Lấy một điểm B thuộc d3: xB = xA + 1, yB = yA + k_val
            xB = xA + 1
            yB = yA + k_val

            vdc_da_1_d = '\\True Gọi $d_3$ là đường thẳng có hệ số góc dương, đi qua $A$ và tạo với $\\Delta$ góc $45^\\circ$. Khi đó, điểm $B\\left( %s; %s \\right)$ thuộc $d_3$' % (latex(xB), latex(yB))
            vdc_da_1_s = 'Gọi $d_3$ là đường thẳng có hệ số góc dương, đi qua $A$ và tạo với $\\Delta$ góc $45^\\circ$. Khi đó, điểm $B\\left( %s; %s \\right)$ thuộc $d_3$' % (latex(xA+10), latex(yA+10))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Đường thẳng $\\Delta$ có hệ số góc $k_{\\Delta} = %s$. Gọi $k$ là hệ số góc của $d_3$ ($k > 0$). \\\\
                            Ta có $\\tan 45^\\circ = \\left| \\frac{k - k_{\\Delta}}{1 + k \\cdot k_{\\Delta}} \\right| \\Leftrightarrow \\left| \\frac{k - \\left( %s \\right)}{1 + k \\cdot \\left( %s \\right)} \\right| = 1$. \\\\
                            Giải phương trình trên với điều kiện $k > 0$ ta được $k = %s$. \\\\
                            Phương trình đường thẳng $d_3$ là: $y - %s = %s\\left( x - %s \\right) \\Leftrightarrow %s$. \\\\
                            Thử tọa độ điểm $B\\left( %s; %s \\right)$ vào phương trình $d_3$ thấy thỏa mãn.''' 
                            % (latex(k_delta), latex(k_delta), latex(k_delta), latex(k_val), 
                               latex(yA), latex(k_val), latex(xA), format_eq(k_val, -1, yA - k_val*xA), latex(xB), latex(yB)))

            # --- BƯỚC 2: XÁO TRỘN VÀ KIỂM TRA SỐ CÂU ĐÚNG ---
            while True:
                da_a = random.choice(list_nb_da_1)
                da_b = random.choice(list_th_da_1)
                da_c = random.choice(list_vd_da_1)
                da_d = random.choice(list_vdc_da_1)

                true_count = sum('\\True' in ans for ans in [da_a, da_b, da_c, da_d])
                if 1 <= true_count <= 3:
                    break

            # --- BƯỚC 3: XUẤT NỘI DUNG THEO MẪU ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(da_a) + '}\n'
                '{' + str(da_b) + '}\n'
                '{' + str(da_c) + '}\n'
                '{' + str(da_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -','+')
            return content   

