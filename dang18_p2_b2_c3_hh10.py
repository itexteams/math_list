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


def bt_dang18_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo các biến ký hiệu
            x, y = symbols('x y')

            def solve_geometry():
                while True:
                    # 1. Sinh ngẫu nhiên tọa độ điểm A và B (đảm bảo A khác B)
                    xA, yA = random.randint(-5, 5), random.randint(-5, 5)
                    xB, yB = xA + random.choice([-4, -3, -2, 2, 3, 4]), yA + random.choice([-4, -3, -2, 2, 3, 4])
                    A = (xA, yA)
                    B = (xB, yB)

                    # 2. Phương trình đường thẳng d đi qua A và B
                    # Vectơ AB = (xB-xA, yB-yA) -> Vectơ pháp tuyến n_d = (-(yB-yA), xB-xA)
                    a_d_raw = -(yB - yA)
                    b_d_raw = xB - xA
                    c_d_raw = -(a_d_raw * xA + b_d_raw * yA)

                    # Rút gọn hệ số cho đường thẳng d
                    common_d = gcd(gcd(a_d_raw, b_d_raw), c_d_raw)
                    a_d, b_d, c_d = a_d_raw // common_d, b_d_raw // common_d, c_d_raw // common_d
                    if a_d < 0 or (a_d == 0 and b_d < 0):
                        a_d, b_d, c_d = -a_d, -b_d, -c_d

                    # 3. Tạo đường thẳng Delta: a_delta*x + b_delta*y + c_delta = 0
                    # Chọn Delta sao cho A không thuộc Delta
                    a_delta = random.randint(-3, 3)
                    if a_delta == 0: a_delta = 1
                    b_delta = random.randint(-3, 3)
                    if b_delta == 0: b_delta = -2

                    # Tính c_delta sao cho A không thuộc Delta
                    c_delta = -(a_delta * xA + b_delta * yA) + random.choice([-3, -2, 2, 3])

                    # Kiểm tra cosin có "đẹp" không (tùy chọn, ở đây tính chính xác bằng sympy)
                    tu_cos = Abs(a_d * a_delta + b_d * b_delta)
                    mau_cos = sqrt(a_d**2 + b_d**2) * sqrt(a_delta**2 + b_delta**2)
                    cos_phi = tu_cos / mau_cos

                    # 4. Tìm điểm M nguyên trên Delta và tính khoảng cách đến d
                    # Tham số hóa Delta: tìm 1 điểm nguyên M0(x0, y0) thuộc Delta
                    M_found = None
                    for tx in range(-20, 20):
                        # Từ a_delta*x + b_delta*y + c_delta = 0 => y = (-c_delta - a_delta*x)/b_delta
                        if (-c_delta - a_delta * tx) % b_delta == 0:
                            ty = (-c_delta - a_delta * tx) // b_delta
                            M_found = (tx, ty)
                            break

                    if M_found:
                        dist_h = Abs(a_d * M_found[0] + b_d * M_found[1] + c_d) / sqrt(a_d**2 + b_d**2)
                        if dist_h > 0:
                            return A, B, (a_d, b_d, c_d), (a_delta, b_delta, c_delta), cos_phi, dist_h, M_found

            # Khởi tạo dữ liệu bài toán
            A, B, line_d, line_delta, cos_val, dist_h, M_target = solve_geometry()

            # --- NỘI DUNG CÂU HỎI ---
            pt_delta = line_delta[0]*x + line_delta[1]*y + line_delta[2]
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $\\left( Oxy \\right)$, cho hai điểm $A\\left( %s;%s \\right)$, $B\\left( %s;%s \\right)$ và đường thẳng $\\Delta : %s = 0$.''' 
                            % (A[0], A[1], B[0], B[1], latex(pt_delta)))

            ########################################################################
            # a) Nhận biết: Kiểm tra A thuộc Delta
            val_A_delta = line_delta[0]*A[0] + line_delta[1]*A[1] + line_delta[2]
            nb_da_1_d = '\\True Điểm $A$ không thuộc đường thẳng $\\Delta$'
            nb_da_1_s = 'Điểm $A$ thuộc đường thẳng $\\Delta$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Thay tọa độ điểm $A\\left( %s;%s \\right)$ vào phương trình đường thẳng $\\Delta$, ta có: \\\\
                            $%s \\cdot \\left( %s \\right) + \\left( %s \\right) \\cdot \\left( %s \\right) + \\left( %s \\right) = %s \\neq 0$. \\\\
                            Vậy điểm $A$ không thuộc đường thẳng $\\Delta$.''' 
                            %(A[0], A[1], line_delta[0], A[0], line_delta[1], A[1], line_delta[2], val_A_delta))

            ########################################################################
            # b) Thông hiểu: Phương trình đường thẳng d đi qua A, B
            pt_d = line_d[0]*x + line_d[1]*y + line_d[2]
            th_da_1_d = '\\True Phương trình đường thẳng $d$ đi qua 2 điểm $A, B$ là $%s = 0$' % latex(pt_d)
            th_da_1_s = 'Phương trình đường thẳng $d$ đi qua 2 điểm $A, B$ là $%s = 0$' % latex(pt_d + random.randint(1, 5))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $\\overrightarrow{AB} = \\left( %s; %s \\right)$. \\\\
                            Đường thẳng $d$ đi qua $A\\left( %s;%s \\right)$ và có vectơ pháp tuyến $\\vec{n}_d = \\left( %s; %s \\right)$ nên có phương trình là: \\\\
                            $%s\\left( x - %s \\right) + %s\\left( y - %s \\right) = 0 \\Leftrightarrow %s = 0$.''' 
                            % (B[0]-A[0], B[1]-A[1], A[0], A[1], line_d[0], line_d[1], line_d[0], A[0], line_d[1], A[1], latex(pt_d)))

            ########################################################################
            # c) Vận dụng: Tính cosin góc giữa d và Delta
            def format_latex_float(val):
                return latex(val).replace('.', ',')

            cos_tex = format_latex_float(cos_val)
            vd_da_1_d = '\\True $\\cos\\left( d, \\Delta \\right) = %s$' % cos_tex
            vd_da_1_s = '$\\cos\\left( d, \\Delta \\right) = %s$' % format_latex_float(cos_val * Rational(1, 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Đường thẳng $d$ có vectơ pháp tuyến $\\vec{n}_d = \\left( %s; %s \\right)$. \\\\
                            Đường thẳng $\\Delta$ có vectơ pháp tuyến $\\vec{n}_{\\Delta} = \\left( %s; %s \\right)$. \\\\
                            Ta có $\\cos\\left( d, \\Delta \\right) = \\frac{\\left| \\vec{n}_d \\cdot \\vec{n}_{\\Delta} \\right|}{\\left| \\vec{n}_d \\right| \\cdot \\left| \\vec{n}_{\\Delta} \\right|} = \\frac{\\left| %s \\cdot (%s) + %s \\cdot (%s) \\right|}{\\sqrt{(%s)^2 + (%s)^2} \\cdot \\sqrt{(%s)^2 + (%s)^2}} = %s$.''' 
                            % (line_d[0], line_d[1], line_delta[0], line_delta[1], line_d[0], line_delta[0], line_d[1], line_delta[1], line_d[0], line_d[1], line_delta[0], line_delta[1], cos_tex))

            ########################################################################
            # d) Vận dụng cao: Điểm trên Delta cách d một khoảng h
            h_tex = format_latex_float(dist_h)
            sum_M = M_target[0] + M_target[1]
            vdc_da_1_d = '\\True Tổng hoành độ và tung độ của điểm có tọa độ nguyên thuộc đường thẳng $\\Delta$ có khoảng cách đến đường thẳng $d$ bằng $%s$ là $%s$' % (h_tex, sum_M)
            vdc_da_1_s = 'Tổng hoành độ và tung độ của điểm có tọa độ nguyên thuộc đường thẳng $\\Delta$ có khoảng cách đến đường thẳng $d$ bằng $%s$ là $%s$' % (h_tex, sum_M + 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Gọi $M\\left( x_M; y_M \\right) \\in \\Delta \\Rightarrow %s x_M + %s y_M + %s = 0$. \\\\
                            Khoảng cách từ $M$ đến đường thẳng $d$ là $d\\left( M, d \\right) = \\frac{\\left| %s x_M + %s y_M + %s \\right|}{\\sqrt{%s^2 + %s^2}} = %s$. \\\\
                            Vì $M$ có tọa độ nguyên và $M \\in \\Delta$, giải hệ điều kiện trên ta tìm được điểm $M\\left( %s; %s \\right)$. \\\\
                            Vậy tổng hoành độ và tung độ của điểm $M$ là $%s + %s = %s$.''' 
                            % (line_delta[0], line_delta[1], line_delta[2], line_d[0], line_d[1], line_d[2], line_d[0], line_d[1], h_tex, M_target[0], M_target[1], M_target[0], M_target[1], sum_M))

            ########################################################################
            # XỬ LÝ ĐÁP ÁN ĐÚNG/SAI VÀ XUẤT NỘI DUNG
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content   

