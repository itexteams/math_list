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


def bt_dang13_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân kiểu Việt Nam (dùng dấu phẩy)
            def format_vn(value):
                return str(value).replace('.', ',')

            # --- Bước 1: Random các giá trị cho bài toán ---
            xA0 = random.randint(1, 5)
            yA0 = random.randint(-5, -1)
            vAx = random.choice([-40, -35, -30, -25])
            vAy = random.choice([20, 25, 30, 35])

            xB0 = random.randint(2, 6)
            yB0 = random.randint(1, 5)
            vBx = random.choice([-35, -30, -25, -20])
            vBy = random.choice([-45, -40, -35, -30])

            # --- Bước 2: Tính toán các thông số lý thuyết sử dụng Sympy ---
            t = symbols('t', real=True, nonnegative=True)

            # 1. Cosin góc giữa hai đường đi
            uA = (vAx, vAy)
            uB = (vBx, vBy)
            dot_product = abs(uA[0]*uB[0] + uA[1]*uB[1])
            normA = sqrt(uA[0]**2 + uA[1]**2)
            normB = sqrt(uB[0]**2 + uB[1]**2)
            cos_alpha = dot_product / (normA * normB)
            cos_val_latex = latex(simplify(cos_alpha))

            # 2. Khoảng cách giữa hai tàu d(t)
            dx = (xA0 + vAx*t) - (xB0 + vBx*t)
            dy = (yA0 + vAy*t) - (yB0 + vBy*t)
            d_sq = dx**2 + dy**2
            d_sq_expanded = simplify(d_sq)

            # Tìm thời điểm t để d(t) đạt GTNN
            f_prime = diff(d_sq, t)
            t_min_val = solve(f_prime, t)[0]
            t_min_latex = latex(t_min_val)

            # Khoảng cách nhỏ nhất
            d_min_val = sqrt(d_sq.subs(t, t_min_val))
            d_min_float = round(float(d_min_val), 2)

            # 3. Tàu A đứng yên, tàu B chạy. Khoảng cách từ A(xA0, yA0) đến đường thẳng quỹ đạo B
            # VTCP của B là (vBx, vBy) => VTPT là (vBy, -vBx)
            A_line, B_line, C_line = vBy, -vBx, -(vBy*xB0 - vBx*yB0)
            dist_A_to_B = abs(A_line*xA0 + B_line*yA0 + C_line) / sqrt(A_line**2 + B_line**2)
            dist_fixed_float = round(float(dist_A_to_B), 2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có hai con tàu $A$ và $B$ cùng xuất phát từ hai bến, chuyển động đều theo đường thẳng ngoài biển. Trên màn hình ra đa của trạm điều khiển (được coi như mặt phẳng tọa độ $Oxy$ với đơn vị trên các trục tính theo ki-lô-mét), sau khi xuất phát $t$ (giờ) ($t \\ge 0$), vị trí của tàu $A$ có tọa độ được xác định bởi công thức $\\left\\{ \\begin{array}{l} x = %s %s t \\\\ y = %s + %s t \\end{array} \\right.$, vị trí của tàu $B$ có tọa độ là $N\\left( %s %s t; %s %s t \\right)$.'''
                             %(xA0, vAx, yA0, vAy, xB0, vBx, yB0, vBy))

            ########################################################################
            # Nhận biết - Ý a
            nb_da_1_d = '\\True Cosin góc giữa hai đường đi của hai tàu $A$ và $B$ bằng $%s$' % cos_val_latex
            nb_da_1_s = 'Cosin góc giữa hai đường đi của hai tàu $A$ và $B$ bằng $\\frac{1}{5\\sqrt{79}}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Đường thẳng quỹ đạo tàu $A$ có vectơ chỉ phương $\\vec{u}_A = \\left( %s; %s \\right)$. \\\\ Đường thẳng quỹ đạo tàu $B$ có vectơ chỉ phương $\\vec{u}_B = \\left( %s; %s \\right)$. \\\\ Gọi $\\alpha$ là góc giữa hai đường đi, ta có: \\\\ $\\cos \\alpha = \\frac{|\\vec{u}_A \\cdot \\vec{u}_B|}{|\\vec{u}_A| \\cdot |\\vec{u}_B|} = \\frac{|(%s)(%s) + (%s)(%s)|}{\\sqrt{(%s)^2+(%s)^2} \\cdot \\sqrt{(%s)^2+(%s)^2}} = %s$.''' 
                            %(vAx, vAy, vBx, vBy, vAx, vBx, vAy, vBy, vAx, vAy, vBx, vBy, cos_val_latex))

            ########################################################################
            # Thông hiểu - Ý b
            th_da_1_d = '\\True Sau $%s$ giờ kể từ thời điểm xuất phát thì hai tàu gần nhau nhất' % t_min_latex
            th_da_1_s = 'Sau $\\frac{9}{85}$ giờ kể từ thời điểm xuất phát thì hai tàu gần nhau nhất'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Tại thời điểm $t$, khoảng cách giữa hai tàu là \\\\ $d(t) = \\sqrt{[(%s %s t) - (%s %s t)]^2 + [(%s + %s t) - (%s %s t)]^2}$. \\\\ Ta có $d^2(t) = %s$. \\\\ Đây là một tam thức bậc hai của $t$, đạt giá trị nhỏ nhất khi $t = %s$ (giờ).''' 
                            %(xA0, vAx, xB0, vBx, yA0, vAy, yB0, vBy, latex(d_sq_expanded), t_min_latex))

            ########################################################################
            # Vận dụng - Ý c
            vd_da_1_d = '\\True Tại thời điểm gần nhau nhất, hai tàu cách nhau khoảng $%s$ km' % format_vn(d_min_float)
            vd_da_1_s = 'Tại thời điểm gần nhau nhất, hai tàu cách nhau khoảng 1,63 km'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Với $t = %s$, thay vào biểu thức $d(t)$ ta có: \\\\ $d = \\sqrt{%s} \\approx %s$ (km). \\\\ Vậy tại thời điểm gần nhau nhất, hai tàu cách nhau khoảng $%s$ km.''' 
                            %(t_min_latex, latex(simplify(d_sq.subs(t, t_min_val))), format_vn(d_min_float), format_vn(d_min_float)))

            ########################################################################
            # Vận dụng cao - Ý d
            vdc_da_1_d = '\\True Nếu tàu $A$ đứng yên ở vị trí ban đầu, tàu $B$ chạy thì khoảng cách ngắn nhất giữa hai tàu bằng $%s$ km' % format_vn(dist_fixed_float)
            vdc_da_1_s = 'Nếu tàu $A$ đứng yên ở vị trí ban đầu, tàu $B$ chạy thì khoảng cách ngắn nhất giữa hai tàu bằng 3,4 km'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Vị trí ban đầu của tàu $A$ là $M\\left( %s; %s \\right)$. \\\\ Đường thẳng $\\Delta$ biểu diễn quỹ đạo tàu $B$ đi qua $N\\left( %s; %s \\right)$ và có vectơ pháp tuyến $\\vec{n} = \\left( %s; %s \\right)$. \\\\ Phương trình đường thẳng $\\Delta$: $%s(x - %s) + (%s)(y - %s) = 0 \\Leftrightarrow %sx + %sy + %s = 0$. \\\\ Khoảng cách ngắn nhất chính là khoảng cách từ $M$ đến $\\Delta$: \\\\ $d(M, \\Delta) = \\frac{|%s(%s) + %s(%s) + %s|}{\\sqrt{(%s)^2 + (%s)^2}} = %s$ (km).''' 
                             %(xA0, yA0, xB0, yB0, vBy, -vBx, vBy, xB0, -vBx, yB0, A_line, B_line, C_line, A_line, xA0, B_line, yA0, C_line, A_line, B_line, format_vn(dist_fixed_float)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Xuất nội dung theo đúng cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ 
                str(noidungcauhoi)+ 
                ' \n \\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                ' \\loigiai{ \n'
                ' \\begin{enumEX}[a)]{1} \n'
                ' \\item '+str(loigiai_nb_1)+'\n'
                ' \\item '+str(loigiai_th_1)+'\n'
                ' \\item '+str(loigiai_vd_1)+'\n'
                ' \\item '+str(loigiai_vdc_1)+'\n'
                ' \\end{enumEX}} \n'
                ' \\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content   

