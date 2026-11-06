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


def bt_dang24_p4_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Danh sách dạng (ở đây có 1 dạng bài như hình)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các hệ số để phương trình có nghiệm đẹp hoặc thực tế
                # Phương trình có dạng: a*sqrt(b*x^2 + c*x + d) = sqrt(e*x^2 + f*x + g)

                # Để sát với đề mẫu: 4*sqrt(2x^2 - 3x + 1) = sqrt(9x^2 + 54x + 81)
                # Ta sẽ random các giá trị tương tự
                a_val = random.randint(3, 5) # Mẫu là 4
                b_val, c_val, d_val = 2, -3, 1 # Giữ nguyên cụm này để có điều kiện x >= 1 hoặc x <= 1/2

                # Tạo vế phải là một bình phương hoàn chỉnh (px + q)^2 để giống mẫu 9(x+3)^2
                p_val = random.randint(2, 4)
                q_val = random.randint(2, 9)

                e_val = p_val**2
                f_val = 2 * p_val * q_val
                g_val = q_val**2

                # Thiết lập các biểu thức sympy
                expr_left_inside = b_val*x**2 + c_val*x + d_val
                expr_right_inside = e_val*x**2 + f_val*x + g_val

                # Phương trình sau khi bình phương: a^2 * (b*x^2 + c*x + d) = e*x^2 + f*x + g
                coeff_A = a_val**2 * b_val - e_val
                coeff_B = a_val**2 * c_val - f_val
                coeff_C = a_val**2 * d_val - g_val

                eq_final = sp.Eq(coeff_A*x**2 + coeff_B*x + coeff_C, 0)
                all_roots = solve(eq_final, x)

                # Lọc nghiệm theo điều kiện b*x^2 + c*x + d >= 0
                valid_roots = []
                for r in all_roots:
                    if (b_val*r**2 + c_val*r + d_val) >= 0:
                        valid_roots.append(r)

                # Tính tổng các nghiệm
                tong_nghiem = sum(valid_roots)

                # Tạo các đáp án trắc nghiệm
                da_dung = '$%s$' % latex(tong_nghiem)

                # Tạo các đáp án nhiễu (tránh trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = tong_nghiem + random.choice([Rational(1, 2), 1, Rational(-2, 3), 2, Rational(5, 4)])
                    if sai != tong_nghiem:
                        s.add('$%s$' % latex(sai))

                list_sai = list(s)
                da_s1, da_s2, da_s3 = list_sai[0], list_sai[1], list_sai[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho phương trình $%s\\sqrt{%s} = \\sqrt{%s}$. Tính tổng các nghiệm của phương trình.'''
                                 % (latex(a_val), latex(expr_left_inside), latex(expr_right_inside)))

                # Đáp án đúng có tiền tố \True
                da_d = ('\\True ' + str(da_dung))

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                # Điều kiện: 2x^2 - 3x + 1 >= 0 <=> x >= 1 hoặc x <= 1/2
                loigiai = ('''$%s\\sqrt{%s} = \\sqrt{%s} \\Leftrightarrow \\begin{cases} %s \\ge 0 \\\\ %s(%s) = %s \\end{cases}$ \\\\
                           $\\Leftrightarrow \\begin{cases} \\left[ \\begin{aligned} & x \\ge 1 \\\\ & x \\le \\frac{1}{2} \\end{aligned} \\right. \\\\ %sx^2 %sx + %s = %sx^2 + %sx + %s \\end{cases}$ \\\\
                           $\\Leftrightarrow \\begin{cases} \\left[ \\begin{aligned} & x \\ge 1 \\\\ & x \\le \\frac{1}{2} \\end{aligned} \\right. \\\\ %sx^2 %sx %s = 0 \\end{cases} \\Leftrightarrow \\left[ \\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned} \\right. (\\text{thỏa mãn})$. \\\\
                           Tổng các nghiệm của phương trình là: $%s + \\left(%s\\right) = %s$.'''
                           % (latex(a_val), latex(expr_left_inside), latex(expr_right_inside), 
                              latex(expr_left_inside), latex(a_val**2), latex(expr_left_inside), latex(expr_right_inside),
                              latex(a_val**2 * b_val), latex(a_val**2 * c_val), latex(a_val**2 * d_val), 
                              latex(e_val), latex(f_val), latex(g_val),
                              latex(coeff_A), latex(coeff_B if coeff_B < 0 else "+"+str(coeff_B)), latex(coeff_C if coeff_C < 0 else "+"+str(coeff_C)),
                              latex(valid_roots[0]), latex(valid_roots[1]) if len(valid_roots) > 1 else "",
                              latex(valid_roots[0]), latex(valid_roots[1]) if len(valid_roots) > 1 else "0",
                              latex(tong_nghiem)
                             ))

            # Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

