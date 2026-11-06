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


def bt_dang9_p2_b1_c3_ds12(self):
            # Khai báo biến ngẫu nhiên
            a = randint(2, 10)
            b = randint(2, 20)
            n = randint(3, 10)

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $f(x)=\dfrac{%sx^{%s}+%s}{x}$ với $x \neq 0$.''' % (latex(a), latex(n), latex(b))

            ######################################################################## 
            # Nhận biết: Biến đổi hàm số
            ########################################################################
            nb_da_1_d = r'\True $f(x)=%sx^{%s}+\dfrac{%s}{x}$' % (latex(a), latex(n-1), latex(b))
            nb_da_1_s = r'$f(x)=%sx^{%s}+%s$' % (latex(a), latex(n-1), latex(b))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = r'Ta có $f(x) = \dfrac{%sx^{%s}}{x} + \dfrac{%s}{x} = %sx^{%s} + \dfrac{%s}{x}$.' % (latex(a), latex(n), latex(b), latex(a), latex(n-1), latex(b))

            ######################################################################## 
            # Thông hiểu: Tách nguyên hàm
            ########################################################################
            th_da_1_d = r'\True $\displaystyle\int f(x) \text{d}x=%s\displaystyle\int x^{%s} \text{d}x+%s\displaystyle\int \dfrac{1}{x} \text{d}x$' % (latex(a), latex(n-1), latex(b))
            th_da_1_s = r'$\displaystyle\int f(x) \text{d}x=%s\displaystyle\int x^{%s} \text{d}x+%s\displaystyle\int \dfrac{1}{x} \text{d}x$' % (latex(a), latex(n), latex(b))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = r'Sử dụng tính chất nguyên hàm: $\displaystyle\int f(x) \text{d}x = \displaystyle\int \left(%sx^{%s} + \dfrac{%s}{x}\right) \text{d}x = %s\displaystyle\int x^{%s} \text{d}x + %s\displaystyle\int \dfrac{1}{x} \text{d}x$.' % (latex(a), latex(n-1), latex(b), latex(a), latex(n-1), latex(b))

            ######################################################################## 
            # Vận dụng: Tính nguyên hàm
            ########################################################################
            # Tính a/n bằng nsimplify để rút gọn phân số
            he_so_nguyen_ham = nsimplify(Rational(a, n))
            vd_da_1_d = r'\True $\displaystyle\int f(x) \text{d}x=%sx^{%s}+%s\ln |x|+C$' % (latex(he_so_nguyen_ham), latex(n), latex(b))
            vd_da_1_s = r'$\displaystyle\int f(x) \text{d}x=%sx^{%s}+%s\ln |x|+C$' % (latex(a), latex(n), latex(b))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = r'Ta có $\displaystyle\int f(x) \text{d}x = %s \cdot \dfrac{x^{%s}}{%s} + %s\ln |x| + C = %sx^{%s} + %s\ln |x| + C$.' % (latex(a), latex(n), latex(n), latex(b), latex(he_so_nguyen_ham), latex(n), latex(b))

            ######################################################################## 
            # Vận dụng cao: Đạo hàm (Sửa lỗi dấu ở đây)
            ########################################################################
            # Đạo hàm của ax^{n-1} + b/x là a(n-1)x^{n-2} - b/x^2
            vdc_da_1_d = r'''\True $f'(x)=%sx^{%s}-\dfrac{%s}{x^2}$''' % (latex(a*(n-1)), latex(n-2), latex(b))
            vdc_da_1_s = r'''$f'(x)=%sx^{%s}+\dfrac{%s}{x^2}$''' % (latex(a*(n-1)), latex(n-2), latex(b))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = 'Ta có $f\'(x) = \\left(%sx^{%s} + %sx^{-1}\\right)\' = %s(%s)x^{%s} - %sx^{-2} = %sx^{%s} - \\dfrac{%s}{x^2}$.' % (latex(a), latex(n-1), latex(b), latex(a), latex(n-1), latex(n-2), latex(b), latex(a*(n-1)), latex(n-2), latex(b))

            # Thuật toán xáo trộn câu hỏi và đảm bảo số lượng câu đúng (từ 1 đến 3 câu \True)
            answers_raw = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            solutions_raw = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Đóng gói và xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +  
                '\n\\choiceTFn \n'
                '{' + str(answers_raw[0]) + '}\n'
                '{' + str(answers_raw[1]) + '}\n'
                '{' + str(answers_raw[2]) + '}\n'
                '{' + str(answers_raw[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(solutions_raw[0]) + '\n'
                '\\item ' + str(solutions_raw[1]) + '\n'
                '\\item ' + str(solutions_raw[2]) + '\n'
                '\\item ' + str(solutions_raw[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('--','+').replace('-1x','-x').replace('+1x','+x').replace('x^{1}','x').replace('$1x','$x').replace(' 1x',' x')
            return content


