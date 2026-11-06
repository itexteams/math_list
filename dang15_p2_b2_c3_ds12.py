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


def bt_dang15_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số k để bài toán phong phú (mặc định trong ảnh k=1)
            k = random.randint(1, 5) 
            if k == 1:
                f_str = "x \\sin x"
            else:
                f_str = f"{k}x \\sin x"

            f = k * x * sin(x)
            f_prime = diff(f, x)

            # Nội dung câu hỏi
            noidungcauhoi = f"Cho hàm số $f(x) = {f_str}$ có đạo hàm là $f'(x)$."

            ########################################################################
            # Nhận biết: Tính tích phân 2f'(x) từ 0 đến pi/2
            ########################################################################
            val_a_dung = k * pi
            val_a_sai = k * pi / 2

            da_a_d = f"\\True $\\int_{{0}}^{{\\frac{{\\pi}}{{2}}}} 2f'(x) \\text{{d}}x = {latex(val_a_dung)}$"
            da_a_s = f"$\\int_{{0}}^{{\\frac{{\\pi}}{{2}}}} 2f'(x) \\text{{d}}x = {latex(val_a_sai)}$"
            list_nb = [da_a_d, da_a_s]
            nb_da = random.choice(list_nb)

            loigiai_nb = (f"Ta có $\\int_{{0}}^{{\\frac{{\\pi}}{{2}}}} 2f'(x) \\text{{d}}x = 2f(x) \\big|_0^{{\\frac{{\\pi}}{{2}}}} = 2 \\left[ f\\left(\\frac{{\\pi}}{{2}}\\right) - f(0) \\right] = "
                          f"2 \\left( {k} \\cdot \\frac{{\\pi}}{{2}} \\sin \\frac{{\\pi}}{{2}} - 0 \\right) = {latex(val_a_dung)}$.")

            ########################################################################
            # Thông hiểu: Tích phân [f'(x) - k.sin(x)]
            ########################################################################
            # Nguyên hàm của f'(x) - k.sin(x) là f(x) + k.cos(x)
            val_b_dung = k * (pi/2 - 1)
            val_b_sai = k * (pi/2 + 1)

            da_b_d = f"\\True $\\int_{{0}}^{{\\frac{{\\pi}}{{2}}}} [f'(x) - {k if k>1 else ''} \\sin x] \\text{{d}}x = {latex(val_b_dung)}$"
            da_b_s = f"$\\int_{{0}}^{{\\frac{{\\pi}}{{2}}}} [f'(x) - {k if k>1 else ''} \\sin x] \\text{{d}}x = {latex(val_b_sai)}$"
            list_th = [da_b_d, da_b_s]
            th_da = random.choice(list_th)

            loigiai_th = (f"Ta có $\\int_{{0}}^{{\\frac{{\\pi}}{{2}}}} [f'(x) - {k if k>1 else ''} \\sin x] \\text{{d}}x = "
                          f"\\int_{{0}}^{{\\frac{{\\pi}}{{2}}}} f'(x) \\text{{d}}x + \\int_{{0}}^{{\\frac{{\\pi}}{{2}}}} (-{k if k>1 else ''} \\sin x) \\text{{d}}x = "
                          f"{f_str} \\big|_0^{{\\frac{{\\pi}}{{2}}}} + {k if k>1 else ''} \\cos x \\big|_0^{{\\frac{{\\pi}}{{2}}}} = "
                          f"{latex(k * pi/2)} - {k} = {latex(val_b_dung)}$.")

            ########################################################################
            # Vận dụng: Tích phân f(x)/sin(x) từ pi/3 đến pi/2
            ########################################################################
            # Tích phân k.x từ pi/3 đến pi/2 = k/2 * (pi^2/4 - pi^2/9) = k/2 * 5pi^2/36 = 5k.pi^2/72
            val_c_tu = 5 * k
            val_c_dung = f"\\frac{{{val_c_tu}\\pi^2}}{{72}}"
            val_c_sai = f"\\frac{{{val_c_tu}\\pi^2}}{{36}}"

            da_c_d = f"\\True $\\int_{{\\frac{{\\pi}}{{3}}}}^{{\\frac{{\\pi}}{{2}}}} \\frac{{f(x)}}{{\\sin x}} \\text{{d}}x = {val_c_dung}$"
            da_c_s = f"$\\int_{{\\frac{{\\pi}}{{3}}}}^{{\\frac{{\\pi}}{{2}}}} \\frac{{f(x)}}{{\\sin x}} \\text{{d}}x = {val_c_sai}$"
            list_vd = [da_c_d, da_c_s]
            vd_da = random.choice(list_vd)

            loigiai_vd = (f"Ta có $\\int_{{\\frac{{\\pi}}{{3}}}}^{{\\frac{{\\pi}}{{2}}}} \\frac{{f(x)}}{{\\sin x}} \\text{{d}}x = "
                          f"\\int_{{\\frac{{\\pi}}{{3}}}}^{{\\frac{{\\pi}}{{2}}}} {k if k>1 else ''}x \\text{{d}}x = "
                          f"\\frac{{{k if k>1 else ''}x^2}}{{2}} \\bigg|_{{\\frac{{\\pi}}{{3}}}}^{{\\frac{{\\pi}}{{2}}}} = "
                          f"\\frac{{{k if k>1 else ''}}}{{2}} \\left( \\frac{{\\pi^2}}{{4}} - \\frac{{\\pi^2}}{{9}} \\right) = {val_c_dung}$.")

            ########################################################################
            # Vận dụng cao: Tích phân (k^2.x^2)/[f(x)]^2 từ pi/4 đến pi/2
            ########################################################################
            # f(x)^2 = k^2.x^2.sin^2(x) => k^2.x^2/f(x)^2 = 1/sin^2(x)
            # Tích phân 1/sin^2(x) từ pi/4 đến pi/2 là [-cot(x)] từ pi/4 đến pi/2 = 0 - (-1) = 1
            val_d_dung = 1
            val_d_sai = 0

            da_d_d = f"\\True $\\int_{{\\frac{{\\pi}}{{4}}}}^{{\\frac{{\\pi}}{{2}}}} \\frac{{{'' if k==1 else k**2}x^2}}{{[f(x)]^2}} \\text{{d}}x = {val_d_dung}$"
            da_d_s = f"$\\int_{{\\frac{{\\pi}}{{4}}}}^{{\\frac{{\\pi}}{{2}}}} \\frac{{{'' if k==1 else k**2}x^2}}{{[f(x)]^2}} \\text{{d}}x = {val_d_sai}$"
            list_vdc = [da_d_d, da_d_s]
            vdc_da = random.choice(list_vdc)

            loigiai_vdc = (f"Ta có $\\int_{{\\frac{{\\pi}}{{4}}}}^{{\\frac{{\\pi}}{{2}}}} \\frac{{{'' if k==1 else k**2}x^2}}{{[f(x)]^2}} \\text{{d}}x = "
                           f"\\int_{{\\frac{{\\pi}}{{4}}}}^{{\\frac{{\\pi}}{{2}}}} \\frac{{1}}{{\\sin^2 x}} \\text{{d}}x = "
                           f"-\\cot x \\big|_{{\\frac{{\\pi}}{{4}}}}^{{\\frac{{\\pi}}{{2}}}} = 1$.")

            # Xử lý trộn và đếm đáp án đúng
            def count_true(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb)
                d2 = random.choice(list_th)
                d3 = random.choice(list_vd)
                d4 = random.choice(list_vdc)
                if 1 <= count_true([d1, d2, d3, d4]) <= 3:
                    break

            # Xuất nội dung
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + d1 + '}\n'
                '{' + d2 + '}\n'
                '{' + d3 + '}\n'
                '{' + d4 + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb + '\n'
                '\\item ' + loigiai_th + '\n'
                '\\item ' + loigiai_vd + '\n'
                '\\item ' + loigiai_vdc + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

