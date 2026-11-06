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


def bt_dang8_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            def get_line_eq(p1, p2):
                """Lập phương trình đường thẳng qua 2 điểm."""
                if p1 == p2: return None
                return sp.Line(p1, p2).equation(x, y)

            def get_perp_line(point, line_eq):
                """Lập phương trình đường thẳng qua 1 điểm và vuông góc với đường thẳng cho trước."""
                coeffs = line_eq.as_coefficients_dict()
                a, b = coeffs[x], coeffs[y]
                # Đường thẳng vuông góc có dạng bx - ay + k = 0
                k = -(b * point[0] - a * point[1])
                return b * x - a * y + k

            def format_eq(eq):
                """Đưa phương trình về dạng chuẩn Ax + By + C = 0 với A > 0 và tối giản."""
                eq = simplify(eq)
                coeffs = eq.as_coefficients_dict()
                a = coeffs.get(x, 0)
                b = coeffs.get(y, 0)
                c = coeffs.get(1, 0)

                # Tìm ước chung lớn nhất để tối giản
                common = sp.gcd_list([a, b, c])
                a, b, c = a/common, b/common, c/common

                # Đảm bảo hệ số đầu tiên dương
                if a < 0 or (a == 0 and b < 0):
                    a, b, c = -a, -b, -c
                return a * x + b * y + c

            # --- BƯỚC 1: SINH DỮ LIỆU NGẪU NHIÊN ---
            # Để đảm bảo tọa độ đẹp, ta chọn 3 điểm A, B, C trước
            while True:
                xA, yA = random.randint(-4, 4), random.randint(-4, 4)
                xB, yB = random.randint(-4, 4), random.randint(-4, 4)
                xC, yC = random.randint(-4, 4), random.randint(-4, 4)

                A, B, C_pt = (xA, yA), (xB, yB), (xC, yC)

                # Kiểm tra không thẳng hàng
                if (yB - yA) * (xC - xB) != (yC - yB) * (xB - xA):
                    break

            # Các đường thẳng chính xác
            eq_BC = format_eq(get_line_eq(B, C_pt))
            eq_AB = format_eq(get_line_eq(A, B))
            eq_AC = format_eq(get_line_eq(A, C_pt))

            # Các đường cao
            hB_dung = format_eq(get_perp_line(B, eq_AC))
            hC_dung = format_eq(get_perp_line(C_pt, eq_AB))
            hA_dung = format_eq(get_perp_line(A, eq_BC))

            # Đường trung tuyến kẻ từ A
            mid_BC = (Rational(xB + xC, 2), Rational(yB + yC, 2))
            mA_dung = format_eq(get_line_eq(A, mid_BC))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tam giác $ABC$ có phương trình của đường thẳng $BC$ là $%s=0$, phương trình các đường cao kẻ từ $B, C$ lần lượt là $%s=0$ và $%s=0$.''' 
                             % (latex(eq_BC), latex(hB_dung), latex(hC_dung)))

            ########################################################################
            # (a) Nhận biết: Tọa độ điểm B
            da_a_d = '\\True Điểm $B$ có tọa độ là $\\left( %s; %s \\right)$' % (latex(xB), latex(yB))
            da_a_s = 'Điểm $B$ có tọa độ là $\\left( %s; %s \\right)$' % (latex(xB + 1), latex(yB))
            list_a = [da_a_d, da_a_s]
            nb_da = random.choice(list_a)
            sol_a = ('''Điểm $B$ là giao điểm của đường thẳng $BC$ và đường cao kẻ từ $B$. \\\\
                     Giải hệ phương trình: $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Rightarrow B(%s; %s)$.''' 
                     % (latex(eq_BC), latex(hB_dung), latex(xB), latex(yB)))

            ########################################################################
            # (b) Thông hiểu: Tọa độ điểm C
            da_b_d = '\\True Điểm $C$ có tọa độ là $\\left( %s; %s \\right)$' % (latex(xC), latex(yC))
            da_b_s = 'Điểm $C$ có tọa độ là $\\left( %s; %s \\right)$' % (latex(xC), latex(yC - 1))
            list_b = [da_b_d, da_b_s]
            th_da = random.choice(list_b)
            sol_b = ('''Điểm $C$ là giao điểm của đường thẳng $BC$ và đường cao kẻ từ $C$. \\\\
                     Giải hệ phương trình: $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Rightarrow C(%s; %s)$.''' 
                     % (latex(eq_BC), latex(hC_dung), latex(xC), latex(yC)))

            ########################################################################
            # (c) Vận dụng: Phương trình đường cao kẻ từ A
            hA_sai = hA_dung + random.randint(1, 5)
            da_c_d = '\\True Phương trình đường cao kẻ từ $A$ là $%s=0$' % (latex(hA_dung))
            da_c_s = 'Phương trình đường cao kẻ từ $A$ là $%s=0$' % (latex(hA_sai))
            list_c = [da_c_d, da_c_s]
            vd_da = random.choice(list_c)
            sol_c = ('''Đường thẳng $AB$ đi qua $B(%s; %s)$ và vuông góc với đường cao kẻ từ $C$ ($%s=0$) nên có phương trình: $%s=0$. \\\\
                     Đường thẳng $AC$ đi qua $C(%s; %s)$ và vuông góc với đường cao kẻ từ $B$ ($%s=0$) nên có phương trình: $%s=0$. \\\\
                     Tọa độ điểm $A$ là nghiệm của hệ: $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Rightarrow A(%s; %s)$. \\\\
                     Đường cao kẻ từ $A$ vuông góc với $BC$ ($%s=0$) và đi qua $A$ nên có phương trình: $%s=0$.''' 
                     % (latex(xB), latex(yB), latex(hC_dung), latex(eq_AB),
                        latex(xC), latex(yC), latex(hB_dung), latex(eq_AC),
                        latex(eq_AB), latex(eq_AC), latex(xA), latex(yA),
                        latex(eq_BC), latex(hA_dung)))

            ########################################################################
            # (d) Vận dụng cao: Phương trình đường trung tuyến kẻ từ A
            mA_sai = mA_dung + random.randint(1, 5)
            da_d_d = '\\True Phương trình đường trung tuyến kẻ từ $A$ là $%s=0$' % (latex(mA_dung))
            da_d_s = 'Phương trình đường trung tuyến kẻ từ $A$ là $%s=0$' % (latex(mA_sai))
            list_d = [da_d_d, da_d_s]
            vdc_da = random.choice(list_d)
            sol_d = ('''Gọi $M$ là trung điểm của $BC$. Tọa độ $M$ là $M\\left( \\frac{%s+%s}{2}; \\frac{%s+%s}{2} \\right) = \\left( %s; %s \\right)$. \\\\
                     Đường trung tuyến kẻ từ $A$ đi qua $A(%s; %s)$ và $M\\left( %s; %s \\right)$ nên có phương trình: $%s=0$.''' 
                     % (latex(xB), latex(xC), latex(yB), latex(yC), latex(mid_BC[0]), latex(mid_BC[1]),
                        latex(xA), latex(yA), latex(mid_BC[0]), latex(mid_BC[1]), latex(mA_dung)))

            # Kiểm tra số lượng đáp án đúng (từ 1 đến 3)
            def count_true(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb = random.choice(list_a)
                th = random.choice(list_b)
                vd = random.choice(list_c)
                vdc = random.choice(list_d)
                if 1 <= count_true([nb, th, vd, vdc]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb) + '}\n'
                '{' + str(th) + '}\n'
                '{' + str(vd) + '}\n'
                '{' + str(vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sol_a) + '\n'
                '\\item ' + str(sol_b) + '\n'
                '\\item ' + str(sol_c) + '\n'
                '\\item ' + str(sol_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

