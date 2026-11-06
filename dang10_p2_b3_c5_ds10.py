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


def bt_dang10_p2_b3_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến và hằng số ngẫu nhiên
            x = symbols('x')
            n = 5  # Số mũ cố định theo đề hoặc có thể dùng random.randint(4, 6)
            m = random.choice([2, 3, 4]) # Mẫu số của hệ số x
            k_val = Rational(-1, m) # Hệ số của x là -1/m

            # Biểu thức khai triển: (1 - 1/m * x)^n
            expr = (1 + k_val * x)**n
            poly = expand(expr)

            # Lấy danh sách các hệ số a_0, a_1, ..., a_n
            coeffs = []
            for i in range(n + 1):
                coeffs.append(poly.coeff(x, i))

            # --- Bắt đầu nội dung câu hỏi ---
            noidungcauhoi = ('''Cho $\\left( 1 - \\frac{1}{%s} x \\right)^{%s} = a_{0} + a_{1}x + a_{2}x^{2} + a_{3}x^{3} + a_{4}x^{4} + a_{5}x^{5}$.''' 
                             %(latex(m), latex(n)))

            ########################################################################
            # Nhận biết: Kiểm tra hệ số a_3
            ########################################################################
            a3_val = coeffs[3]
            a3_wrong = Rational(n, m) # Một giá trị sai thường gặp

            nb_da_1_d = '\\True $a_{3} = %s$' %(latex(a3_val))
            nb_da_1_s = '$a_{3} = %s$' %(latex(a3_wrong))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Số hạng tổng quát trong khai triển là $T_{k+1} = C_{%s}^{k} \\cdot \\left( -\\frac{1}{%s} x \\right)^{k} = C_{%s}^{k} \\cdot \\left( -\\frac{1}{%s} \\right)^{k} \\cdot x^{k}$.\\\\
            Hệ số $a_{3}$ ứng với $k=3$, ta có $a_{3} = C_{%s}^{3} \\cdot \\left( -\\frac{1}{%s} \\right)^{3} = %s$.'''
                            %(latex(n), latex(m), latex(n), latex(m), latex(n), latex(m), latex(a3_val)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Kiểm tra hệ số a_5
            ########################################################################
            a5_val = coeffs[5]
            a5_wrong = -Rational(1, m**(n-1))

            th_da_1_d = '\\True $a_{5} = %s$' %(latex(a5_val))
            th_da_1_s = '$a_{5} = %s$' %(latex(a5_wrong))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Hệ số $a_{5}$ ứng với $k=5$, ta có $a_{5} = C_{%s}^{5} \\cdot \\left( -\\frac{1}{%s} \\right)^{5} = 1 \\cdot \\left( -\\frac{1}{%s} \\right) = %s$.'''
                            %(latex(n), latex(m), latex(m**n), latex(a5_val)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Hệ số lớn nhất
            ########################################################################
            max_coeff = max(coeffs)
            max_val_str = str(max_coeff).replace('.', ',') # Định dạng dấu phẩy cho số thập phân

            vd_da_1_d = '\\True Hệ số lớn nhất trong tất cả hệ số là $%s$' %(latex(max_coeff))
            vd_da_1_s = 'Hệ số lớn nhất trong tất cả hệ số là $%s$' %(latex(coeffs[1] if coeffs[1] > 0 else coeffs[0]))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Giải thích tìm max
            loigiai_vd_1 = ('''Tính các hệ số: $a_{0}=%s$; $a_{1}=%s$; $a_{2}=%s$; $a_{3}=%s$; $a_{4}=%s$; $a_{5}=%s$.\\\\
            So sánh các giá trị trên, ta thấy hệ số lớn nhất là $%s$.'''
                            %(latex(coeffs[0]), latex(coeffs[1]), latex(coeffs[2]), latex(coeffs[3]), latex(coeffs[4]), latex(coeffs[5]), latex(max_coeff)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Tổng các hệ số
            ########################################################################
            sum_coeffs = expr.subs(x, 1)

            vdc_da_1_d = '\\True Tổng $a_{0} + a_{1} + a_{2} + a_{3} + a_{4} + a_{5} = %s$' %(latex(sum_coeffs))
            vdc_da_1_s = 'Tổng $a_{0} + a_{1} + a_{2} + a_{3} + a_{4} + a_{5} = %s$' %(latex(sum_coeffs * 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Tổng các hệ số của đa thức $P(x)$ chính là giá trị của đa thức tại $x=1$.\\\\
            Thay $x=1$ vào biểu thức $\\left( 1 - \\frac{1}{%s} x \\right)^{%s}$, ta được:\\\\
            $S = \\left( 1 - \\frac{1}{%s} \\cdot 1 \\right)^{%s} = \\left( \\frac{%s}{%s} \\right)^{%s} = %s$.'''
                             %(latex(m), latex(n), latex(m), latex(n), latex(m-1), latex(m), latex(n), latex(sum_coeffs)))

            list_vdc_2 = [loigiai_vdc_1]
            list_vdc_1 = [vdc_da_1]

            # --- Phần logic trộn và xuất nội dung ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    shuffled_answers = current_answers
                    # Lấy lời giải tương ứng
                    shuffled_solutions = [
                        loigiai_nb_1 if ans_nb in list_nb_da_1 else "",
                        loigiai_th_1 if ans_th in list_th_da_1 else "",
                        loigiai_vd_1 if ans_vd in list_vd_da_1 else "",
                        loigiai_vdc_1 if ans_vdc in list_vdc_da_1 else ""
                    ]
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(ans_nb)+'}\n'
                '{'+str(ans_th)+'}\n'
                '{'+str(ans_vd)+'}\n'
                '{'+str(ans_vdc)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

