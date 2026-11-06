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


def bt_dang31_p4_b2_c4_ds10(self):
            # --- BƯỚC 3: RANDOM BÀI TOÁN ---
            while True:
                xA = random.randint(1, 5)
                yA = random.randint(-10, 10)

                tu_sym = random.randint(-5, 5)
                mau_sym = random.choice([1, 2, 3, 4]) # Cho phép cả số nguyên
                x_sym = Rational(tu_sym, mau_sym)

                # Hệ phương trình:
                # 1) a*(xA**2) + b*xA + 2 = yA
                # 2) -b/(2a) = x_sym  => b = -2 * a * x_sym
                a_sym, b_sym = symbols('a b')
                eq1 = a_sym * (xA**2) + b_sym * xA + 2 - yA
                eq2 = b_sym + 2 * a_sym * x_sym

                # SỬA LỖI TẠI ĐÂY: Thêm dict=True và lấy phần tử [0]
                sol_list = solve((eq1, eq2), (a_sym, b_sym), dict=True)

                if sol_list:
                    sol = sol_list[0]
                    a_val = sol[a_sym]
                    b_val = sol[b_sym]
                    # Đảm bảo a khác 0 để là Parabol
                    if a_val != 0:
                        break

            # Tạo biểu thức Parabol chuẩn LaTeX (tự xử lý dấu +/-)
            x = symbols('x')
            f_x = a_val*x**2 + b_val*x + 2
            kq_chinh_xac = "y = " + latex(f_x)

            da_d = '\\True $%s$' % kq_chinh_xac

            # --- BƯỚC 4: ĐIỀU CHỈNH PHƯƠNG ÁN SAI ---
            s = []
            offsets = [Rational(1, 2), 1, Rational(-1, 2), -1, 2, -2, 3, -3]
            random.shuffle(offsets)

            for offset in offsets:
                a_f = a_val + offset
                b_f = b_val - offset
                if a_f == 0: continue

                f_sai = a_f*x**2 + b_f*x + 2
                sai_str = "y = " + latex(f_sai)

                if sai_str != kq_chinh_xac and ('$%s$' % sai_str) not in s:
                    s.append('$%s$' % sai_str)
                if len(s) >= 3:
                    break

            das1, das2, das3 = s[0], s[1], s[2]

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Xác định parabol $(P): y = ax^2 + bx + 2$ đi qua điểm $A(%s; %s)$ và có trục đối xứng $x = %s$.'''
                                 %(latex(xA), latex(yA), latex(x_sym)))

            # --- NỘI DUNG LỜI GIẢI ---
            vp1 = yA - 2
            # Rút gọn phương trình ax^2 + bx = vp1 thành (xA)a + b = vp1/xA
            rut_gon_a = xA
            rut_gon_vp = Rational(vp1, xA)
            b_theo_a = -2 * x_sym # b = (b_theo_a)*a

            loigiai = ('''Vì $(P)$ đi qua điểm $A(%s; %s)$ và có trục đối xứng $x = %s$ nên ta có hệ phương trình: \\\\
                             $\\begin{cases} a \\cdot (%s)^2 + b \\cdot (%s) + 2 = %s \\\\ -\\dfrac{b}{2a} = %s \\end{cases} 
                             \\Leftrightarrow \\begin{cases} %sa + %sb = %s \\\\ b = %sa \\end{cases}
                             \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$.\\\\
                             Vậy $(P): %s$.'''
                           %(latex(xA), latex(yA), latex(x_sym),
                             latex(xA), latex(xA), latex(yA),
                             latex(x_sym),
                             latex(xA**2), latex(xA), latex(vp1), latex(b_theo_a),
                             latex(a_val), latex(b_val),
                             kq_chinh_xac
                           ))

            # Xử lý danh sách đáp án
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')

            return content

