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


def bt_dang28_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # --- BƯỚC 3: THIẾT LẬP CÁC THAM SỐ RANDOM ---
            k = random.choice([2, 3, 5]) # Cơ số của hàm mũ
            n_year = random.randint(2024, 2026) # Năm trong tổng T
            c_val = 0 # Để giống mẫu C=0, F(0) = 1/ln(k)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho $F(x)$ là nguyên hàm của hàm số $f(x) = %s^x$, thỏa mãn $F(0) = \frac{1}{\ln %s}$.''' 
                             % (k, k))

            ########################################################################
            # Nhận biết (Câu a) ############################################
            nb_da_1_d = r'\True $F(x) = \int f(x) \text{d}x = \frac{%s^x}{\ln %s} + C$' % (k, k)
            nb_da_1_s = r'$F(x) = \int f(x) \text{d}x = %s^x \cdot \ln %s + C$' % (k, k)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''$F(x) = \int f(x) \text{d}x = \int %s^x \text{d}x = \frac{%s^x}{\ln %s} + C$.''' 
                            % (k, k, k))

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            th_da_1_d = r'\True Hàm số $F(x)$ cần tìm là $F(x) = \frac{%s^x}{\ln %s}$' % (k, k)
            th_da_1_s = r'Hàm số $F(x)$ cần tìm là $F(x) = \frac{%s^x}{\ln %s} + 1$' % (k, k)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Ta có: $F(0) = \frac{%s^0}{\ln %s} + C = \frac{1}{\ln %s} + C$ mà $F(0) = \frac{1}{\ln %s} \Rightarrow C = 0 \Rightarrow F(x) = \frac{%s^x}{\ln %s}$.''' 
                            % (k, k, k, k, k, k))

            ########################################################################
            # Vận dụng (Câu c) ############################################
            # Tính toán giá trị đúng cho T: T = (1/ln k) * (k^(n+1)-1)/(k-1)
            t_tu = k**(n_year + 1) - 1
            t_mau = (k - 1)
            vd_da_1_d = r'\True Giá trị của tổng $T = F(0) + F(1) + \dots + F(%s)$ là $T = \frac{%s^{%s} - 1}{%s \ln %s}$' % (n_year, k, n_year + 1, t_mau, k)
            vd_da_1_s = r'Giá trị của tổng $T = F(0) + F(1) + \dots + F(%s)$ là $T = \frac{%s^{%s} - 1}{\ln %s}$' % (n_year, k, n_year, k)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''$T = F(0) + F(1) + \dots + F(%s) = \frac{1}{\ln %s}(1 + %s + %s^2 + \dots + %s^{%s}) = \frac{1}{\ln %s} \cdot \frac{%s^{%s} - 1}{%s - 1} = \frac{%s^{%s} - 1}{%s \ln %s}$.''' 
                            % (n_year, k, k, k, k, n_year, k, k, n_year + 1, k, k, n_year + 1, t_mau, k))

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            # Tính thể tích V = pi * tích phân [0, 1] của (k^x / ln k)^2 dx
            # V = (pi/ln^2 k) * [ k^(2x) / (2 ln k) ] cận 0-1 = pi(k^2 - 1) / (2 ln^3 k)
            v_tu = (k**2 - 1)
            vdc_da_1_d = r'\True Thể tích khối tròn xoay tạo thành khi quay $(H)$ quanh trục $Ox$ là $V = \frac{%s \pi}{2 \ln^3 %s}$' % (v_tu, k)
            vdc_da_1_s = r'Thể tích khối tròn xoay tạo thành khi quay $(H)$ quanh trục $Ox$ là $V = \frac{%s \pi}{\ln^3 %s}$' % (v_tu, k)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Ta có thể tích của khối tròn xoay tạo thành khi quay $(H)$ quanh trục $Ox$ bằng: \\ 
            $V = \pi \int_0^1 \left( \frac{%s^x}{\ln %s} \right)^2 \text{d}x = \pi \int_0^1 \frac{%s^{2x}}{\ln^2 %s} \text{d}x = \pi \cdot \left( \frac{%s^{2x}}{2 \ln^3 %s} \right) \bigg|_0^1 = \frac{%s \pi}{2 \ln^3 %s}$.''' 
                             % (k, k, k, k, k, k, v_tu, k))

            # --- BƯỚC 4: XỬ LÝ LỰA CHỌN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                da_nb = random.choice(list_nb_da_1)
                da_th = random.choice(list_th_da_1)
                da_vd = random.choice(list_vd_da_1)
                da_vdc = random.choice(list_vdc_da_1)

                answers = [da_nb, da_th, da_vd, da_vdc]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung theo mẫu LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(da_nb) + '}\n'
                '{' + str(da_th) + '}\n'
                '{' + str(da_vd) + '}\n'
                '{' + str(da_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

