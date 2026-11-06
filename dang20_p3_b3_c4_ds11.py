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


def bt_dang20_p3_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, a = symbols('x a')

            # Khai báo biến dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Thiết lập Logic Random bài toán ---
                # 1. Chọn x0 ngẫu nhiên (thường là 1, 2, 3)
                x0 = random.randint(1, 3)

                # 2. Tạo mẫu số dạng sqrt(x + c) - d sao cho tại x0 mẫu bằng 0
                d = random.randint(2, 4)
                c = d**2 - x0
                mau_so = sqrt(x + c) - d

                # 3. Tạo tử số dạng (x - x0)(ax + k) để luôn triệt tiêu tại x0
                k_val = random.randint(1, 5)
                tu_so_expand = expand((x - x0) * (a * x + k_val))

                # 4. Tạo f(x0) = a^2 + m*a + n
                m_val = random.choice([-4, -2, 0, 2, 4])
                n_val = random.randint(5, 15)
                f_x0_expr = a**2 + m_val*a + n_val

                # --- Tính toán giới hạn và giải tìm a ---
                # Giới hạn sau khi khử dạng vô định: Lim = (a*x0 + k) * 2d
                f_limit_val = (a * x0 + k_val) * (2 * d)

                # Giải phương trình: f_limit_val = f_x0_expr
                pt = Equality(f_limit_val, f_x0_expr)
                cac_nghiem = solve(pt, a)

                # Lọc nghiệm thực
                cac_nghiem_thuc = [sol for sol in cac_nghiem if sol.is_real]
                so_luong_a = len(cac_nghiem_thuc)

                # --- B2: Thiết lập đáp án trắc nghiệm ---
                da = str(so_luong_a)

                # Tạo danh sách các phương án nhiễu (loại trừ đáp án đúng)
                s = ["0", "1", "2", "3", "4"]
                if da in s:
                    s.remove(da)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (r'''Cho hàm số $f(x) = \begin{cases} \dfrac{%s}{%s} & \text{khi } x \neq %s \\ %s & \text{khi } x = %s \end{cases}$. Số giá trị thực của $a$ để hàm số liên tục tại $x = %s$ bằng bao nhiêu?''' 
                                 % (latex(tu_so_expand), latex(mau_so), latex(x0), latex(f_x0_expr), latex(x0), latex(x0)))

                # --- Các đáp án ---
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn ngẫu nhiên thứ tự đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải ---
                pt_rut_gon = simplify(f_x0_expr - f_limit_val)

                # Trình bày hệ thức nghiệm
                if so_luong_a > 0:
                    chuoi_nghiem = r'$\Leftrightarrow \left[\begin{aligned}' + "".join([rf" a &= {latex(sol)} \\" for sol in cac_nghiem_thuc]) + r'\end{aligned}\right.$'
                else:
                    chuoi_nghiem = "Phương trình vô nghiệm."

                loigiai = (r'''Tập xác định: $D = [%s; +\infty)$. \\
                             Ta có: $f(%s) = %s$. \\
                             $\lim_{x \to %s} f(x) = \lim_{x \to %s} \dfrac{%s}{%s}$ \\
                             $= \lim_{x \to %s} \dfrac{(x-%s)(ax+%s)(\sqrt{x+%s}+%s)}{(\sqrt{x+%s}-%s)(\sqrt{x+%s}+%s)}$ \\
                             $= \lim_{x \to %s} \dfrac{(x-%s)(ax+%s)(\sqrt{x+%s}+%s)}{x-%s}$ \\
                             $= \lim_{x \to %s} (ax+%s)(\sqrt{x+%s}+%s) = %s$. \\
                             Hàm số liên tục tại $x = %s$ khi $\lim_{x \to %s} f(x) = f(%s)$ \\
                             $\Leftrightarrow %s = %s \Leftrightarrow %s = 0$ \\
                             %s \\
                             Vậy có $%s$ giá trị thực của $a$ thỏa mãn.''' 
                           % (latex(-c), latex(x0), latex(f_x0_expr), 
                              latex(x0), latex(x0), latex(tu_so_expand), latex(mau_so),
                              latex(x0), latex(x0), latex(k_val), latex(c), latex(d), latex(c), latex(d), latex(c), latex(d),
                              latex(x0), latex(x0), latex(k_val), latex(c), latex(d), latex(x0),
                              latex(x0), latex(k_val), latex(c), latex(d), latex(f_limit_val),
                              latex(x0), latex(x0), latex(x0),
                              latex(f_limit_val), latex(f_x0_expr), latex(pt_rut_gon),
                              chuoi_nghiem, latex(so_luong_a)))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(so_luong_a))
            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

