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


def bt_dang7_p4_b1_c1_ds12(self):
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Nhánh này hệ số đạo hàm dương k > 0 -> Đồng biến / Nghịch biến / Đồng biến
                x1 = randint(-5, 4)
                x2 = randint(-5, 5)
                k = randint(1, 3) # Hệ số đạo hàm (ví dụ: y' = k(x-x1)(x-x2))
                e = randint(-20, 20) # Hệ số tự do của y

                while x1 >= x2:
                    x1 = randint(-5, 4)
                    x2 = randint(-5, 5)

                coeff_3 = Rational(k, 3)
                coeff_2 = Rational(-k * (x1 + x2), 2)
                coeff_1 = k * x1 * x2

                # Vì k > 0 nên x1 là điểm cực đại, x2 là điểm cực tiểu
                y_cd = coeff_3 * (x1**3) + coeff_2 * (x1**2) + coeff_1 * x1 + e
                y_ct = coeff_3 * (x2**3) + coeff_2 * (x2**2) + coeff_1 * x2 + e

                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^3+%sx^2+%sx+%s$. Tìm khoảng đồng biến, nghịch biến và cực trị của hàm số.''' % (
                    latex(coeff_3), latex(coeff_2), latex(coeff_1), latex(e)
                )

                # Nội dung lời giải có bảng biến thiên kèm mũi tên và kết luận cực trị
                loigiai = ('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                           '''Ta có $y'=%sx^2+%sx+%s.\\\\ \n'''
                           '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'''
                           '''Bảng biến thiên\\\\ \n'''
                           '\\hspace*{3cm} \\begin{tikzpicture} \n'
                           '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                           '{$x$/1,$y\'$/1,$y$/2}  \n'
                           '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                           '\\tkzTabLine{,+,0,-,0,+,}  \n'
                           '\\tkzTabVar{-/ $-\\infty$, +/ $%s$, -/ $%s$, +/ $+\\infty$} \n'
                           '\\end{tikzpicture}  \\\\ \n'
                           '''Từ bảng biến thiên ta thấy\\\\ \n'''
                           '''\\hspace*{1cm}Hàm số nghịch biến trên khoảng $\\left(%s;%s\\right)$;\\\\ \n'''
                           '''\\hspace*{1cm}Hàm số đồng biến trên khoảng $\\left(-\\infty;%s\\right)$ và $\\left(%s;+\\infty\\right)$.\\\\ \n'''
                           '''\\hspace*{1cm}Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$;\\\\ \n'''
                           '''\\hspace*{1cm}Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{\\text{CT}}=%s$.'''
                           % (latex(k), latex(-k * (x1 + x2)), latex(k * x1 * x2), latex(x1), latex(x2),
                              latex(x1), latex(x2), latex(y_cd), latex(y_ct),
                              latex(x1), latex(x2), latex(x1), latex(x2),
                              latex(x1), latex(y_cd), latex(x2), latex(y_ct)))

            if dang == '2':
                # Nhánh này hệ số đạo hàm âm k < 0 -> Nghịch biến / Đồng biến / Nghịch biến
                x1 = randint(-5, 4)
                x2 = randint(-5, 5)
                k = randint(-3, -1) # Hệ số đạo hàm âm
                e = randint(-20, 20)

                while x1 >= x2:
                    x1 = randint(-5, 4)
                    x2 = randint(-5, 5)

                coeff_3 = Rational(k, 3)
                coeff_2 = Rational(-k * (x1 + x2), 2)
                coeff_1 = k * x1 * x2

                # Vì k < 0 nên x1 là điểm cực tiểu, x2 là điểm cực đại
                y_ct = coeff_3 * (x1**3) + coeff_2 * (x1**2) + coeff_1 * x1 + e
                y_cd = coeff_3 * (x2**3) + coeff_2 * (x2**2) + coeff_1 * x2 + e

                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^3+%sx^2+%sx+%s$. Tìm khoảng đồng biến, nghịch biến và cực trị của hàm số.''' % (
                    latex(coeff_3), latex(coeff_2), latex(coeff_1), latex(e)
                )

                # Nội dung lời giải
                loigiai = ('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                           '''Ta có $y'=%sx^2+%sx+%s.\\\\ \n'''
                           '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'''
                           '''Bảng biến thiên\\\\ \n'''
                           '\\hspace*{3cm} \\begin{tikzpicture} \n'
                           '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                           '{$x$/1,$y\'$/1,$y$/2}  \n'
                           '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                           '\\tkzTabLine{,-,0,+,0,-,}  \n'
                           '\\tkzTabVar{+/ $+\\infty$, -/ $%s$, +/ $%s$, -/ $-\\infty$} \n'
                           '\\end{tikzpicture}  \\\\ \n'
                           '''Từ bảng biến thiên ta thấy\\\\ \n'''
                           '''\\hspace*{1cm}Hàm số đồng biến trên khoảng $\\left(%s;%s\\right)$;\\\\ \n'''
                           '''\\hspace*{1cm}Hàm số nghịch biến trên khoảng $\\left(-\\infty;%s\\right)$ và $\\left(%s;+\\infty\\right)$.\\\\ \n'''
                           '''\\hspace*{1cm}Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$;\\\\ \n'''
                           '''\\hspace*{1cm}Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{\\text{CT}}=%s$.'''
                           % (latex(k), latex(-k * (x1 + x2)), latex(k * x1 * x2), latex(x1), latex(x2),
                              latex(x1), latex(x2), latex(y_ct), latex(y_cd),
                              latex(x1), latex(x2), latex(x1), latex(x2),
                              latex(x2), latex(y_cd), latex(x1), latex(y_ct)))

            # Xuất câu hỏi và thay thế các ký tự hiển thị toán học tối ưu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('+1x', '+x').replace('+0x^2', '').replace('+0x', '').replace('+0', '').replace('1x^3', 'x^3').replace('-1x^3', '-x^3')

            content = content.replace('-1x^2', '-x^2').replace('+1x^2', '+x^2').replace('--', '+')
            return content

