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


def bt_dang10_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # 1. Khởi tạo các giá trị ngẫu nhiên
            # Tọa độ điểm M(x_m, y_m)
            x_m = random.randint(-5, 5)
            y_m = random.randint(-5, 5)

            # Vectơ pháp tuyến n(a_n, b_n) cho câu a
            a_n = random.randint(1, 5) * random.choice([-1, 1])
            b_n = random.randint(1, 5) * random.choice([-1, 1])

            # Vectơ chỉ phương u(a_u, b_u) cho câu b (Dùng n của đề bài gốc làm chỉ phương)
            # Để đa dạng, ta lấy ngẫu nhiên một vectơ v(a_v, b_v)
            a_v = random.randint(1, 5) * random.choice([-1, 1])
            b_v = random.randint(1, 5) * random.choice([-1, 1])

            # Hệ số góc k cho câu c và d
            k_c = random.randint(-5, 5)
            k_d = random.randint(-5, 5)
            if k_d == k_c: k_d += 1

            # --- Tính toán phương trình đúng ---
            # a) Qua M, VTPT n: a_n(x - x_m) + b_n(y - y_m) = 0
            c_a = - (a_n * x_m + b_n * y_m)
            eq_a_true = f"{latex(a_n*x + b_n*y + c_a)} = 0"

            # b) Qua M, VTCP v: VTPT sẽ là (b_v, -a_v). PT: b_v(x - x_m) - a_v(y - y_m) = 0
            c_b = - (b_v * x_m - a_v * y_m)
            eq_b_true = f"{latex(b_v*x - a_v*y + c_b)} = 0"

            # c) Qua M, hệ số góc k_c: y - y_m = k_c(x - x_m) => k_c*x - y + (y_m - k_c*x_m) = 0
            c_c = y_m - k_c * x_m
            eq_c_true = f"{latex(k_c*x - y + c_c)} = 0"

            # d) Qua M, hệ số góc k_d: k_d*x - y + (y_m - k_d*x_m) = 0
            c_d = y_m - k_d * x_m
            eq_d_true = f"{latex(k_d*x - y + c_d)} = 0"

            # --- Nội dung câu hỏi ---
            noidungcauhoi = ('''Trong mặt phẳng $Oxy$, cho điểm $M(%s; %s)$ và hai vectơ $\\vec{n}=(%s; %s)$, $\\vec{v}=(%s; %s)$.''' 
                             %(latex(x_m), latex(y_m), latex(a_n), latex(b_n), latex(a_v), latex(b_v)))

            ########################################################################
            # Mệnh đề a: Qua M, VTPT n
            nb_da_1_d = '\\True Phương trình tổng quát của đường thẳng đi qua $M$ và nhận vectơ $\\vec{n}$ là vectơ pháp tuyến là $%s$' % eq_a_true
            nb_da_1_s = 'Phương trình tổng quát của đường thẳng đi qua $M$ và nhận vectơ $\\vec{n}$ là vectơ pháp tuyến là $%s$' % (f"{latex(a_n*x + b_n*y + c_a + random.randint(1,3))} = 0")
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Đường thẳng đi qua $M(%s; %s)$ và có vectơ pháp tuyến $\\vec{n}=(%s; %s)$ có phương trình là: \\\\
                            $%s(x - (%s)) + (%s)(y - %s) = 0 \\Leftrightarrow %s$.''' 
                            %(latex(x_m), latex(y_m), latex(a_n), latex(b_n), latex(a_n), latex(x_m), latex(b_n), latex(y_m), eq_a_true))

            ########################################################################
            # Mệnh đề b: Qua M, VTCP v
            th_da_1_d = '\\True Phương trình tổng quát của đường thẳng đi qua $M$ và nhận vectơ $\\vec{v}$ là vectơ chỉ phương là $%s$' % eq_b_true
            th_da_1_s = 'Phương trình tổng quát của đường thẳng đi qua $M$ và nhận vectơ $\\vec{v}$ là vectơ chỉ phương là $%s$' % (f"{latex(b_v*x + a_v*y + c_b)} = 0")
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Đường thẳng nhận $\\vec{v}=(%s; %s)$ làm vectơ chỉ phương nên có vectơ pháp tuyến là $\\vec{n'}=(%s; %s)$. \\\\
                            Phương trình tổng quát đi qua $M(%s; %s)$ là: \\\\
                            $%s(x - (%s)) + (%s)(y - %s) = 0 \\Leftrightarrow %s$.''' 
                            %(latex(a_v), latex(b_v), latex(b_v), latex(-a_v), latex(x_m), latex(y_m), latex(b_v), latex(x_m), latex(-a_v), latex(y_m), eq_b_true))

            ########################################################################
            # Mệnh đề c: Qua M, hệ số góc k_c
            vd_da_1_d = '\\True Phương trình đường thẳng đi qua $M$ có hệ số góc bằng $%s$ là $%s$' % (latex(k_c), eq_c_true)
            vd_da_1_s = 'Phương trình đường thẳng đi qua $M$ có hệ số góc bằng $%s$ là $%s$' % (latex(k_c), f"{latex(k_c*x + y + c_c)} = 0")
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Phương trình đường thẳng đi qua $M(x_0; y_0)$ có hệ số góc $k$ là: $y - y_0 = k(x - x_0)$. \\\\
                            Với $M(%s; %s)$ và $k = %s$, ta có: \\\\
                            $y - %s = %s(x - (%s)) \\Leftrightarrow %s$.''' 
                            %(latex(x_m), latex(y_m), latex(k_c), latex(y_m), latex(k_c), latex(x_m), eq_c_true))

            ########################################################################
            # Mệnh đề d: Qua M, hệ số góc k_d
            vdc_da_1_d = '\\True Phương trình đường thẳng đi qua $M$ có hệ số góc bằng $%s$ là $%s$' % (latex(k_d), eq_d_true)
            vdc_da_1_s = 'Phương trình đường thẳng đi qua $M$ có hệ số góc bằng $%s$ là $%s$' % (latex(k_d), f"{latex(x - k_d*y + c_d)} = 0")
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Tương tự, với $M(%s; %s)$ và $k = %s$, ta có: \\\\
                            $y - %s = %s(x - (%s)) \\Leftrightarrow %s$.''' 
                            %(latex(x_m), latex(y_m), latex(k_d), latex(y_m), latex(k_d), latex(x_m), eq_d_true))

            # Lặp để đảm bảo số câu đúng từ 1 đến 3
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+').replace('+ -', '-')
            return content   

