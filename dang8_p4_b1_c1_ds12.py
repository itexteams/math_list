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


def bt_dang8_p4_b1_c1_ds12(self):
            # Khai báo các dạng toán trùng phương bậc 4
            lisdang = ['1', '2', '3', '4']
            dang = random.choice(lisdang)

            # Khai báo nghiệm nguyên dương và hệ số tỉ lệ chung
            x0 = randint(1, 3)     # Điểm cực trị nguyên dương, nghiệm sẽ là -x0, 0, x0
            k = randint(1, 2)      # Hệ số để điều chỉnh độ lớn phương trình đạo hàm
            e = randint(-15, 15)   # Hệ số tự do của hàm số y

            if dang == '4':
                # Đạo hàm có 3 nghiệm phân biệt, hệ số a_goc > 0: y' = 4kx^3 - 4k(x0^2)x
                # Dáng điệu BBT: Xuống / Lên / Xuống / Lên
                coeff_4 = Rational(k, 1)
                coeff_2 = -2 * k * (x0**2)

                y_0 = e
                y_cc = coeff_4 * (x0**4) + coeff_2 * (x0**2) + e # Giá trị tại x = -x0 và x = x0 là bằng nhau

                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Tìm khoảng đồng biến, nghịch biến và cực trị của hàm số.''' % (
                    latex(coeff_4), latex(coeff_2), latex(e)
                )

                loigiai = ('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\'
                           '''Ta có $y'=%sx^3+%sx$.\\\\'''
                           '''\\hspace*{1.1cm} $y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s}$. \\\\'''
                           '''Bảng biến thiên\\\\'''
                           '\\hspace*{2cm} \\begin{tikzpicture} \n'
                           '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                           '{$x$/1,$y\'$/1,$y$/2}  \n'
                           '{$-\\infty$,$%s$,0,$%s$,$+\\infty$}  \n'
                           '\\tkzTabLine{,-,0,+,0,-,0,+,}  \n'
                           '\\tkzTabVar{+/ $+\\infty$, -/ $%s$, +/ $%s$, -/ $%s$, +/ $+\\infty$} \n'
                           '\\end{tikzpicture}  \\\\'
                           '''Từ bảng biến thiên ta thấy\\\\'''
                           '''\\hspace*{1cm}Hàm số nghịch biến trên khoảng $\\left(-\\infty;%s\\right)$ và $\\left(0;%s\\right)$;\\\\'''
                           '''\\hspace*{1cm}Hàm số đồng biến trên khoảng $\\left(%s;0\\right)$ và $\\left(%s;+\\infty\\right)$.\\\\'''
                           '''\\hspace*{1cm}Hàm số đạt cực đại tại điểm $x=0$, giá trị cực đại là $y_{\\text{CĐ}}=%s$;\\\\'''
                           '''\\hspace*{1cm}Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$, giá trị cực tiểu là $y_{\\text{CT}}=%s$.'''
                           % (latex(4*k), latex(-4*k*(x0**2)), latex(-x0), latex(x0),
                              latex(-x0), latex(x0), latex(y_cc), latex(y_0), latex(y_cc),
                              latex(-x0), latex(x0), latex(-x0), latex(x0),
                              latex(y_0), latex(-x0), latex(x0), latex(y_cc)))

            elif dang == '3':
                # Đạo hàm có 3 nghiệm phân biệt, hệ số a_goc < 0: y' = -4kx^3 + 4k(x0^2)x
                # Dáng điệu BBT: Lên / Xuống / Lên / Xuống
                coeff_4 = Rational(-k, 1)
                coeff_2 = 2 * k * (x0**2)

                y_0 = e
                y_cc = coeff_4 * (x0**4) + coeff_2 * (x0**2) + e

                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Tìm khoảng đồng biến, nghịch biến và cực trị của hàm số.''' % (
                    latex(coeff_4), latex(coeff_2), latex(e)
                )

                loigiai = ('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\'
                           '''Ta có $y'=%sx^3+%sx$.\\\\'''
                           '''\\hspace*{1.1cm} $y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s}$. \\\\'''
                           '''Bảng biến thiên\\\\ '''
                           '\\hspace*{2cm} \\begin{tikzpicture} \n'
                           '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                           '{$x$/1,$y\'$/1,$y$/2}  \n'
                           '{$-\\infty$,$%s$,0,$%s$,$+\\infty$}  \n'
                           '\\tkzTabLine{,+,0,-,0,+,0,-,}  \n'
                           '\\tkzTabVar{-/ $-\\infty$, +/ $%s$, -/ $%s$, +/ $%s$, -/ $-\\infty$} \n'
                           '\\end{tikzpicture}  \\\\ \n'
                           '''Từ bảng biến thiên ta thấy\\\\ '''
                           '''\\hspace*{1cm}Hàm số đồng biến trên khoảng $\\left(-\\infty;%s\\right)$ và $\\left(0;%s\\right)$;\\\\ '''
                           '''\\hspace*{1cm}Hàm số nghịch biến trên khoảng $\\left(%s;0\\right)$ và $\\left(%s;+\\infty\\right)$.\\\\'''
                           '''\\hspace*{1cm}Hàm số đạt cực tiểu tại điểm $x=0$, giá trị cực tiểu là $y_{\\text{CT}}=%s$;\\\\ \n'''
                           '''\\hspace*{1cm}Hàm số đạt cực đại tại các điểm $x=%s$ và $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$.'''
                           % (latex(-4*k), latex(4*k*(x0**2)), latex(-x0), latex(x0),
                              latex(-x0), latex(x0), latex(y_cc), latex(y_0), latex(y_cc),
                              latex(-x0), latex(x0), latex(-x0), latex(x0),
                              latex(y_0), latex(-x0), latex(x0), latex(y_cc)))

            elif dang == '2':
                # Đạo hàm chỉ có 1 nghiệm duy nhất x = 0, hệ số a_goc > 0. Thí dụ: y' = 4kx^3 + 4k(x0^2)x
                # Dáng điệu BBT: Đi xuống rồi đi lên
                coeff_4 = Rational(k, 1)
                coeff_2 = 2 * k * (x0**2)
                y_0 = e

                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Tìm khoảng đồng biến, nghịch biến và cực trị của hàm số.''' % (
                    latex(coeff_4), latex(coeff_2), latex(e)
                )

                loigiai = ('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\'
                           '''Ta có $y'=%sx^3+%sx$.\\\\'''
                           '''\\hspace*{1.1cm} $y'=0 \\Leftrightarrow x=0$.\\\\'''
                           '''Bảng biến thiên\\\\'''
                           '\\hspace*{2cm} \\begin{tikzpicture} \n'
                           '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                           '{$x$/1,$y\'$/1,$y$/2}  \n'
                           '{$-\\infty$,0,$+\\infty$}  \n'
                           '\\tkzTabLine{,-,0,+,}  \n'
                           '\\tkzTabVar{+/ $+\\infty$, -/ $%s$, +/ $+\\infty$} \n'
                           '\\end{tikzpicture}  \\\\ \n'
                           '''Từ bảng biến thiên ta thấy\\\\'''
                           '''\\hspace*{1cm}Hàm số nghịch biến trên khoảng $\\left(-\\infty;0\\right)$;\\\\'''
                           '''\\hspace*{1cm}Hàm số đồng biến trên khoảng $\\left(0;+\\infty\\right)$.\\\\'''
                           '''\\hspace*{1cm}Hàm số không có điểm cực đại;\\\\'''
                           '''\\hspace*{1cm}Hàm số đạt cực tiểu tại điểm $x=0$, giá trị cực tiểu là $y_{\\text{CT}}=%s$.'''
                           % (latex(4*k), latex(4*k*(x0**2)), latex(y_0), latex(y_0)))

            elif dang == '1':
                # Đạo hàm chỉ có 1 nghiệm duy nhất x = 0, hệ số a_goc < 0. Thí dụ: y' = -4kx^3 - 4k(x0^2)x
                # Dáng điệu BBT: Đi lên rồi đi xuống
                coeff_4 = Rational(-k, 1)
                coeff_2 = -2 * k * (x0**2)
                y_0 = e

                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Tìm khoảng đồng biến, nghịch biến và cực trị của hàm số.''' % (
                    latex(coeff_4), latex(coeff_2), latex(e)
                )

                loigiai = ('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\'
                           '''Ta có $y'=%sx^3+%sx$.\\\\'''
                           '''\\hspace*{1.1cm} $y'=0 \\Leftrightarrow x=0$.\\\\'''
                           '''Bảng biến thiên\\\\'''
                           '\\hspace*{2cm} \\begin{tikzpicture} \n'
                           '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                           '{$x$/1,$y\'$/1,$y$/2}  \n'
                           '{$-\\infty$,0,$+\\infty$}  \n'
                           '\\tkzTabLine{,+,0,-,}  \n'
                           '\\tkzTabVar{-/ $-\\infty$, +/ $%s$, -/ $-\\infty$} \n'
                           '\\end{tikzpicture}  \\\\ \n'
                           '''Từ bảng biến thiên ta thấy\\\\'''
                           '''\\hspace*{1cm}Hàm số đồng biến trên khoảng $\\left(-\\infty;0\\right)$;\\\\ '''
                           '''\\hspace*{1cm}Hàm số nghịch biến trên khoảng $\\left(0;+\\infty\\right)$.\\\\ '''
                           '''\\hspace*{1cm}Hàm số đạt cực đại tại điểm $x=0$, giá trị cực đại là $y_{\\text{CĐ}}=%s$;\\\\ '''
                           '''\\hspace*{1cm}Hàm số không có điểm cực tiểu.'''
                           % (latex(-4*k), latex(-4*k*(x0**2)), latex(y_0), latex(y_0)))

            # Xuất và xử lý làm sạch văn bản chuỗi LaTeX giống dạng 7
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('+1x', '+x').replace('+0x^2', '').replace('+0x', '').replace('+0', '').replace('1x^4', 'x^4').replace('-1x^4', '-x^4')

            content = content.replace('-1x^3', '-x^3').replace('+1x^3', '+x^3').replace('-1x^2', '-x^2').replace('+1x^2', '+x^2').replace('--', '+')
            return content

