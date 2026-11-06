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


def bt_dang8_p3_b3_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- Randomization of the problem parameters ---
                # Direction vectơ components a = (a1, a2, a3)
                # Exclude 0 to ensure the vectơ is well-defined and not parallel/perpendicular to the plane in a trivial way
                a1 = random.choice([-3, -2, -1, 1, 2, 3])
                a2 = random.choice([-3, -2, -1, 1, 2, 3])
                a3 = random.choice([-3, -2, -1, 1, 2, 3])

                # Point on the line (x0, y0, z0)
                x0 = random.randint(-5, 5)
                y0 = random.randint(-5, 5)
                z0 = random.randint(-5, 5)

                # Plane: y=0, Normal vectơ b = (0, 1, 0).

                # --- Calculation of the result ---
                # N = |a|^2 = a1^2 + a2^2 + a3^2
                N = a1**2 + a2**2 + a3**2

                # A = a1^2 + a3^2 (This is N - a2^2, the numerator for cos^2(phi))
                A = a1**2 + a3**2

                # cos(phi) = sqrt(A/N) = sqrt(A*N) / N
                # The form is sqrt(a)/b
                a_val = A * N
                b_val = N

                # T = a - 3b + 2026
                kq = a_val - 3*b_val + 2026

                # The true value for the question is kq.

                # --- Multiple Choice Answers ---
                # The correct answer in LaTeX format
                da = '$%s$'%(latex(kq))

                # Incorrect answers
                s = [latex(kq + random.randint(1, 3)),
                     latex(kq + random.randint(4, 6)),
                     latex(kq - random.randint(1, 3)),
                     latex(kq - random.randint(4, 6)),
                     latex(kq + random.randint(7, 9)),
                     latex(kq - random.randint(7, 9)),
                    ]

                # Convert incorrect answers to LaTeX format
                s_latex = ['$%s$'%(val) for val in s]

                # Select three distinct incorrect answers
                das1 = random.choice(s_latex)
                s_latex.remove(das1)
                das2 = random.choice(s_latex)
                s_latex.remove(das2)
                das3 = random.choice(s_latex)

                # --- Question Content ---
                # Line equation: x = x0 + a1*t, y = y0 + a2*t, z = z0 + a3*t

                def format_t_coeff(coeff):
                    if coeff == 1:
                        return 't'
                    elif coeff == -1:
                        return '-t'
                    else:
                        return latex(coeff) + 't'

                def format_line_part(p0, coeff):
                    part = ''
                    if p0 != 0:
                        part += latex(p0)
                        if coeff > 0:
                            part += '+'

                    if coeff != 0:
                        if p0 == 0 and coeff < 0:
                            part += '-'

                        if abs(coeff) == 1:
                            part += 't'
                        else:
                            part += latex(abs(coeff)) + 't'

                    if part.startswith('+'): part = part[1:]
                    if part.startswith('-'): # Handle negative p0 case
                        if p0 != 0: part = latex(p0) + '+' + format_t_coeff(coeff)
                        if p0 == 0: part = format_t_coeff(coeff)

                    # Simplified formatting for display
                    if p0 != 0:
                        term_t = format_t_coeff(coeff)
                        if coeff > 0:
                            return latex(p0) + '+' + term_t
                        else:
                            return latex(p0) + term_t
                    else:
                        return format_t_coeff(coeff)

                # Simple formatting:
                def format_line_simple(p0, coeff):
                    p0_str = latex(p0)

                    if coeff == 1:
                        t_str = 't'
                    elif coeff == -1:
                        t_str = '-t'
                    else:
                        t_str = latex(coeff) + 't'

                    if p0 == 0:
                        return t_str
                    elif coeff > 0:
                        return p0_str + '+' + t_str
                    else:
                        return p0_str + t_str.replace('+-', '-')

                line_x = format_line_simple(x0, a1)
                line_y = format_line_simple(y0, a2)
                line_z = format_line_simple(z0, a3)

                noidungcauhoi = ('''Trên một sân khấu đã thiết lập sẵn một hệ tọa độ $Oxyz$. \\\\
            Biết cosin góc giữa tia sáng có phương trình $d: \\begin{cases} x = %s \\\\ y = %s \\\\ z = %s \\end{cases}$ và mặt sân khấu có \\\\
            phương trình $y = 0$ bằng $\\frac{\\sqrt{a}}{b}, (a,b \\in \\mathbb{Z})$. Giá trị $T = a - 3b + 2026$ bằng bao nhiêu?'''
                                 %(line_x, line_y, line_z))

                # --- Answers List ---
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # --- Solution Content ---
                loigiai=('''Đường thẳng $d$ có vectơ chỉ phương là $\\vec{a} = (%s; %s; %s)$. \\\\
            Mặt phẳng $(P):y=0$ có vectơ pháp tuyến là $\\vec{b} = (0; 1; 0)$. \\\\
            Ta có \\\\
            $\\sin(d, (P)) = \\frac{|\\vec{a} \\cdot \\vec{b}|}{|\\vec{a}| \\cdot |\\vec{b}|} = \\frac{|%s \\cdot 0 + %s \\cdot 1 + %s \\cdot 0|}{\\sqrt{%s^2 + %s^2 + %s^2} \\cdot \\sqrt{0^2+1^2+0^2}} = \\frac{|%s|}{\\sqrt{%s}} = \\frac{%s}{\\sqrt{%s}}$. \\\\
            $\\cos^2(d, (P)) = 1 - \\sin^2(d, (P)) = 1 - \\left( \\frac{%s}{\\sqrt{%s}} \\right)^2 = 1 - \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\
            $\\cos(d, (P)) = \\sqrt{\\frac{%s}{%s}} = \\frac{\\sqrt{%s}}{\\sqrt{%s}} = \\frac{\\sqrt{%s \\cdot %s}}{%s} = \\frac{\\sqrt{%s}}{%s}$. \\\\
            Từ đó ta có $a=%s, b=%s$. \\\\
            Giá trị $T = a - 3b + 2026 = %s - 3 \\cdot (%s) + 2026 = %s$.'''
                         %(latex(a1), latex(a2), latex(a3),
                           # Dòng 126 (10 %s)
                           latex(a1), latex(a2), latex(a3), latex(a1), latex(a2), latex(a3),
                           latex(a2), latex(N), latex(abs(a2)), latex(N),
                           # Dòng 127 (6 %s)
                           latex(abs(a2)), latex(N), latex(a2**2), latex(N), latex(A), latex(N),
                           # Dòng 128 (9 %s)
                           latex(A), latex(N), latex(A), latex(N), latex(A), latex(N), latex(N), latex(a_val), latex(b_val),
                           # Dòng 129 (2 %s)
                           latex(a_val), latex(b_val),
                           # Dòng 130 (3 %s)
                           latex(a_val), latex(b_val), latex(kq)
                           ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content   

