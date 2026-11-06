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


def bt_dang14_p2_b1_c3_hh10(self):
            # Khai báo biến
            # --- BƯỚC 1: RANDOM TỌA ĐỘ VÀ KIỂM TRA KHÔNG THẲNG HÀNG ---
            while True:
                x1, y1 = random.randint(-5, 5), random.randint(-5, 5) # Điểm A
                x2, y2 = random.randint(-5, 5), random.randint(-5, 5) # Điểm B
                x3, y3 = random.randint(-5, 5), random.randint(-5, 5) # Điểm C

                # Kiểm tra tính thẳng hàng bằng định thức: (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
                if (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) != 0:
                    break

            # --- BƯỚC 2: TÍNH TOÁN CÁC THÔNG SỐ CỦA BÀI TOÁN ---
            # Vectơ BC = (u_bc_x; u_bc_y)
            u_bc_x = x3 - x2
            u_bc_y = y3 - y2

            # Vectơ AB = (u_ab_x; u_ab_y)
            u_ab_x = x2 - x1
            u_ab_y = y2 - y1

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng $Oxy$, cho ba điểm $A(%s; %s)$, $B(%s; %s)$ và $C(%s; %s)$.''' 
                             %(latex(x1), latex(y1), latex(x2), latex(y2), latex(x3), latex(y3)))

            ########################################################################
            # a) Phương trình đường thẳng qua A và vuông góc với BC
            # PTTQ: (x3-x2)(x - x1) + (y3-y2)(y - y1) = 0
            # <=> u_bc_x*x + u_bc_y*y - (u_bc_x*x1 + u_bc_y*y1) = 0
            const_a = u_bc_x * x1 + u_bc_y * y1
            pt_a_dung = '%sx + %sy %s = 0' % (latex(u_bc_x), latex(u_bc_y), latex(-const_a) if -const_a < 0 else '+ ' + latex(-const_a))

            a_da_d = '\\True Phương trình tổng quát của đường thẳng qua $A$ và vuông góc với $BC$ là $%s$' % pt_a_dung
            a_da_s = 'Phương trình tổng quát của đường thẳng qua $A$ và vuông góc với $BC$ là $%sx + %sy + %s = 0$' % (latex(u_bc_y), latex(u_bc_x), latex(random.randint(1, 10)))
            list_a = [a_da_d, a_da_s]

            loigiai_a = ('''Ta có $\\vec{BC} = (%s; %s)$. Đường thẳng qua $A$ và vuông góc với $BC$ nhận $\\vec{BC}$ làm vectơ pháp tuyến. \\\\
                         Phương trình là: $%s(x - %s) + %s(y - %s) = 0 \\Leftrightarrow %s$.''' 
                         %(latex(u_bc_x), latex(u_bc_y), latex(u_bc_x), latex(x1), latex(u_bc_y), latex(y1), pt_a_dung))

            ########################################################################
            # b) Phương trình tham số của đường thẳng AB
            # AB qua A(x1, y1), vtcp (u_ab_x, u_ab_y)
            b_da_d = '\\True Phương trình tham số của đường thẳng $AB$ là $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$' % (latex(x1), latex(u_ab_x), latex(y1), latex(u_ab_y))
            b_da_s = 'Phương trình tham số của đường thẳng $AB$ là $\\begin{cases} x = %s - %st \\\\ y = %s + %st \\end{cases}$' % (latex(x1), latex(u_ab_x), latex(y1), latex(u_ab_x))
            list_b = [b_da_d, b_da_s]

            loigiai_b = ('''Đường thẳng $AB$ đi qua $A(%s; %s)$ và có vectơ chỉ phương $\\vec{AB} = (%s; %s)$. \\\\
                         Phương trình tham số là $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$.''' 
                         %(latex(x1), latex(y1), latex(u_ab_x), latex(u_ab_y), latex(x1), latex(u_ab_x), latex(y1), latex(u_ab_y)))

            ########################################################################
            # c) Vectơ pháp tuyến của BC có độ dài L và tung độ âm
            # Vtcp BC = (a, b) -> Vptn n = (-b, a) hoặc (b, -a)
            # Ở đây ta giữ nguyên độ dài đề bài cho là 2*sqrt(5) để khớp mẫu
            L = 2*sqrt(5)
            # n_chuan = (-u_bc_y, u_bc_x). Độ dài d = sqrt(u_bc_x^2 + u_bc_y^2)
            # n_can_tim = (L/d) * n_chuan. Nếu tung độ vẫn dương thì đổi dấu cả vector.
            d_val = sqrt(u_bc_x**2 + u_bc_y**2)
            nx = simplify(-u_bc_y * L / d_val)
            ny = simplify(u_bc_x * L / d_val)
            if ny > 0:
                nx, ny = -nx, -ny

            c_da_d = '\\True Vectơ pháp tuyến có tung độ âm và có độ dài $2\\sqrt{5}$ của đường thẳng $BC$ là $\\left(%s; %s \\right)$' % (latex(nx), latex(ny))
            c_da_s = 'Vectơ pháp tuyến có tung độ âm và có độ dài $2\\sqrt{5}$ của đường thẳng $BC$ là $\\left(%s; %s\\right)$' % (latex(ny), latex(nx))
            list_c = [c_da_d, c_da_s]

            loigiai_c = ('''Vectơ chỉ phương của $BC$ là $\\vec{u} = (%s; %s)$. \\\\
                         Vectơ pháp tuyến có dạng $\\vec{n} = (k%s; -k%s)$. \\\\
                         Độ dài $|\\vec{n}| = |k|\\sqrt{%s^2 + %s^2} = |k|\\sqrt{%s}$. \\\\
                         Để $|\\vec{n}| = 2\\sqrt{5} = \\sqrt{20}$, ta có $|k| = \\sqrt{\\frac{20}{%s}}$. \\\\
                         Kết hợp điều kiện tung độ âm, ta tìm được $\\vec{n} = \\left(%s; %s\\right)$.''' 
                         %(latex(u_bc_x), latex(u_bc_y), latex(-u_bc_y), latex(-u_bc_x), latex(-u_bc_y), latex(u_bc_x), 
                           latex(u_bc_x**2 + u_bc_y**2), latex(u_bc_x**2 + u_bc_y**2), latex(nx), latex(ny)))

            ########################################################################
            # d) Phương trình tham số của đường trung bình ứng với cạnh BC
            mx, my = Rational(x1+x2, 2), Rational(y1+y2, 2)
            # Vtcp đường trung bình cùng phương BC, chọn luôn u_bc
            d_da_d = '\\True Phương trình tham số đường trung bình ứng với cạnh $BC$ là $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$' % (latex(mx), latex(u_bc_x), latex(my), latex(u_bc_y))
            d_da_s = 'Phương trình tham số đường trung bình ứng với cạnh $BC$ là $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$' % (latex(x1), latex(u_bc_x), latex(y1), latex(u_bc_y))
            list_d = [d_da_d, d_da_s]

            loigiai_d = ('''Đường trung bình ứng với cạnh $BC$ đi qua trung điểm $M$ của $AB$. \\\\
                         Tọa độ $M\\left(\\frac{%s+%s}{2}; \\frac{%s+%s}{2}\\right) = \\left(%s; %s\\right)$. \\\\
                         Vectơ chỉ phương của đường trung bình song song với $BC$ nên chọn $\\vec{u} = \\vec{BC} = (%s; %s)$. \\\\
                         Vậy PTTS là: $\\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$.''' 
                         %(latex(x1), latex(x2), latex(y1), latex(y2), latex(mx), latex(my), latex(u_bc_x), latex(u_bc_y), latex(mx), latex(u_bc_x), latex(my), latex(u_bc_y)))

            # --- BƯỚC 3: XỬ LÝ ĐÁP ÁN VÀ XUẤT NỘI DUNG ---
            def count_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                sel_a = random.choice(list_a)
                sel_b = random.choice(list_b)
                sel_c = random.choice(list_c)
                sel_d = random.choice(list_d)
                if 1 <= count_true([sel_a, sel_b, sel_c, sel_d]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(sel_a) + '}\n'
                '{' + str(sel_b) + '}\n'
                '{' + str(sel_c) + '}\n'
                '{' + str(sel_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('+ 0t', '').replace('- -', '+')
            return content   

