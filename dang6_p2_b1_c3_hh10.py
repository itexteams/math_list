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


def bt_dang6_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            def simplify_line(a, b, c):
                """Rút gọn phương trình đường thẳng ax + by + c = 0 về dạng tối giản."""
                common = gcd(gcd(a, b), c)
                if a < 0 or (a == 0 and b < 0):
                    common = -common
                return a // common, b // common, c // common

            # B3: Suy nghĩ tìm cách random bài toán
            # Để bài toán đẹp, ta nên chọn tọa độ các đỉnh A, B, C là số nguyên.
            while True:
                x1, y1 = random.randint(-3, 3), random.randint(-3, 3) # Điểm A
                x2, y2 = random.randint(-3, 3), random.randint(-3, 3) # Điểm B
                x3, y3 = random.randint(-3, 3), random.randint(-3, 3) # Điểm C

                # Kiểm tra 3 điểm không thẳng hàng
                if (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1):
                    break

            # Tính toán các thông số bài toán
            # 1. Phương trình BC
            a_bc, b_bc, c_bc = simplify_line(y2 - y3, x3 - x2, x2*y3 - x3*y2)
            pt_bc = a_bc*x + b_bc*y + c_bc

            # 2. Phương trình đường cao kẻ từ B (vuông góc AC)
            # Véctơ AC = (x3-x1, y3-y1) là pháp vectơ của đường cao hb
            a_hb, b_hb, c_hb = simplify_line(x3 - x1, y3 - y1, -(x3 - x1)*x2 - (y3 - y1)*y2)
            pt_hb = a_hb*x + b_hb*y + c_hb

            # 3. Phương trình đường cao kẻ từ C (vuông góc AB)
            # Véctơ AB = (x2-x1, y2-y1) là pháp vectơ của đường cao hc
            a_hc, b_hc, c_hc = simplify_line(x2 - x1, y2 - y1, -(x2 - x1)*x3 - (y2 - y1)*y3)
            pt_hc = a_hc*x + b_hc*y + c_hc

            # 4. Trực tâm H (giao của hb và hc)
            sol_h = sp.solve([pt_hb, pt_hc], (x, y))
            hx, hy = sol_h[x], sol_h[y]

            # 5. Phương trình đường cao kẻ từ A (vuông góc BC)
            # Véctơ BC = (x3-x2, y3-y2) là pháp vectơ của đường cao ha
            a_ha, b_ha, c_ha = simplify_line(x3 - x2, y3 - y2, -(x3 - x2)*x1 - (y3 - y2)*y1)
            pt_ha = a_ha*x + b_ha*y + c_ha

            # 6. Trung điểm M của BC
            mx, my = Rational(x2 + x3, 2), Rational(y2 + y3, 2)

            # 7. Phương trình trung tuyến kẻ từ A (đi qua A và M)
            a_ma, b_ma, c_ma = simplify_line(y1 - my, mx - x1, x1*my - mx*y1)
            pt_ma = a_ma*x + b_ma*y + c_ma

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tam giác $ABC$ có phương trình của đường thẳng $BC$ là $%s=0$, phương trình các đường cao kẻ từ $B, C$ lần lượt là $%s=0$ và $%s=0$.''' 
                             %(latex(pt_bc), latex(pt_hb), latex(pt_hc)))

            ########################################################################
            # a) Nhận biết: Tọa độ điểm B
            da_a_d = '\\True Điểm $B$ có tọa độ là $(%s; %s)$' % (latex(x2), latex(y2))
            da_a_s = 'Điểm $B$ có tọa độ là $(%s; %s)$' % (latex(x2 + 1), latex(y2))
            list_a = [da_a_d, da_a_s]
            nb_da_1 = random.choice(list_a)

            loigiai_nb_1 = ('''Điểm $B$ là giao điểm của đường thẳng $BC$ và đường cao kẻ từ $B$. \\\\
            Tọa độ điểm $B$ là nghiệm của hệ phương trình: $\\begin{cases} %s=0 \\\\ %s=0 \\end{cases} \\Leftrightarrow \\begin{cases} x=%s \\\\ y=%s \\end{cases}$. \\\\
            Vậy $B(%s; %s)$.''' % (latex(pt_bc), latex(pt_hb), latex(x2), latex(y2), latex(x2), latex(y2)))

            ########################################################################
            # b) Thông hiểu: Tọa độ điểm C
            da_b_d = '\\True Điểm $C$ có tọa độ là $(%s; %s)$' % (latex(x3), latex(y3))
            da_b_s = 'Điểm $C$ có tọa độ là $(%s; %s)$' % (latex(y3), latex(x3))
            list_b = [da_b_d, da_b_s]
            th_da_1 = random.choice(list_b)

            loigiai_th_1 = ('''Điểm $C$ là giao điểm của đường thẳng $BC$ và đường cao kẻ từ $C$. \\\\
            Tọa độ điểm $C$ là nghiệm của hệ phương trình: $\\begin{cases} %s=0 \\\\ %s=0 \\end{cases} \\Leftrightarrow \\begin{cases} x=%s \\\\ y=%s \\end{cases}$. \\\\
            Vậy $C(%s; %s)$.''' % (latex(pt_bc), latex(pt_hc), latex(x3), latex(y3), latex(x3), latex(y3)))

            ########################################################################
            # c) Vận dụng: Phương trình đường cao kẻ từ A
            da_c_d = '\\True Phương trình đường cao kẻ từ $A$ là $%s=0$' % (latex(pt_ha))
            da_c_s = 'Phương trình đường cao kẻ từ $A$ là $%s=0$' % (latex(pt_ha + 2))
            list_c = [da_c_d, da_c_s]
            vd_da_1 = random.choice(list_c)

            loigiai_vd_1 = ('''Đường thẳng $AB$ đi qua $B(%s;%s)$ và vuông góc với đường cao kẻ từ $C$, nên có pháp vectơ $\\vec{n}_{AB}=(1; -1)$ (từ hệ số của $h_C$). \\\\
            Phương trình $AB$: $%s=0$. \\\\
            Đường thẳng $AC$ đi qua $C(%s;%s)$ và vuông góc với đường cao kẻ từ $B$. \\\\
            Phương trình $AC$: $%s=0$. \\\\
            Tọa độ điểm $A$ là giao của $AB$ và $AC$: $A(%s; %s)$. \\\\
            Đường cao kẻ từ $A$ đi qua $A$ và vuông góc với $BC$ ($%s=0$), nên có pháp vectơ là vectơ chỉ phương của $BC$. \\\\
            Vậy phương trình đường cao kẻ từ $A$ là $%s=0$.''' 
                            % (latex(x2), latex(y2), latex(simplify((x-x2)*(x2-x1) + (y-y2)*(y2-y1))), 
                               latex(x3), latex(y3), latex(simplify((x-x3)*(x3-x1) + (y-y3)*(y3-y1))),
                               latex(x1), latex(y1), latex(pt_bc), latex(pt_ha)))

            ########################################################################
            # d) Vận dụng cao: Phương trình đường trung tuyến kẻ từ A
            da_d_d = '\\True Phương trình đường trung tuyến kẻ từ $A$ là $%s=0$' % (latex(pt_ma))
            da_d_s = 'Phương trình đường trung tuyến kẻ từ $A$ là $%s=0$' % (latex(pt_ma - 5))
            list_d = [da_d_d, da_d_s]
            vdc_da_1 = random.choice(list_d)

            loigiai_vdc_1 = ('''Gọi $M$ là trung điểm của $BC$. Ta có $B(%s;%s)$ và $C(%s;%s)$. \\\\
            Tọa độ điểm $M$ là $M\\left( \\frac{%s+%s}{2}; \\frac{%s+%s}{2} \\right) = \\left( %s; %s \\right)$. \\\\
            Đường trung tuyến kẻ từ $A$ đi qua $A(%s;%s)$ và $M\\left( %s; %s \\right)$. \\\\
            Véctơ chỉ phương $\\vec{AM} = \\left( %s; %s \\right)$. \\\\
            Suy ra pháp vectơ $\\vec{n}_{AM} = (%s; %s)$. \\\\
            Vậy phương trình đường trung tuyến kẻ từ $A$ là $%s=0$.''' 
                             % (latex(x2), latex(y2), latex(x3), latex(y3), 
                                latex(x2), latex(x3), latex(y2), latex(y3), latex(mx), latex(my),
                                latex(x1), latex(y1), latex(mx), latex(my),
                                latex(mx-x1), latex(my-y1), latex(a_ma), latex(b_ma), latex(pt_ma)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                ans_a = random.choice(list_a)
                ans_b = random.choice(list_b)
                ans_c = random.choice(list_c)
                ans_d = random.choice(list_d)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content   

