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


def bt_dang21_p2_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Tư duy random
            # Ta chọn mẫu số n trong biểu thức (sin(x/n) + cos(x/n))^2
            # Trong ảnh n = 2. Ta có thể random n trong tập {2, 4, 6, 8}
            n_val = random.choice([2, 4, 6, 8])
            # Biểu thức trong ngoặc
            expr_inside = sin(x/n_val) + cos(x/n_val)
            # Hàm số f(x) ban đầu
            f_x_raw = (expr_inside)**2
            # Hàm số sau khi rút gọn: f(x) = 1 + sin(2x/n)
            k = Rational(2, n_val)
            f_x_simplified = 1 + sin(k*x)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x) = \left( \sin \frac{x}{%s} + \cos \frac{x}{%s} \right)^2$.''' 
                             % (n_val, n_val))

            ########################################################################
            # Nhận biết: Rút gọn hàm số
            ########################################################################
            nb_da_1_d = r'\True $f(x) = 1 + \sin %s$' % (latex(k*x))
            nb_da_1_s = r'$f(x) = 1 + \cos %s$' % (latex(k*x))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Ta có: $f(x) = \left( \sin \frac{x}{%s} + \cos \frac{x}{%s} \right)^2 = \sin^2 \frac{x}{%s} + \cos^2 \frac{x}{%s} + 2\sin \frac{x}{%s} \cos \frac{x}{%s} = 1 + \sin %s$.'''
                            % (n_val, n_val, n_val, n_val, n_val, n_val, latex(k*x)))

            ########################################################################
            # Thông hiểu: Tính liên tục
            ########################################################################
            th_da_1_d = r'\True Hàm số $f(x)$ liên tục trên $\mathbb{R}$'
            th_da_1_s = r'Hàm số $f(x)$ không liên tục trên $\mathbb{R}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r'''Nhận thấy hàm số $f(x)$ xác định và liên tục trên $\mathbb{R}$.'''

            ########################################################################
            # Vận dụng: Công thức nguyên hàm
            ########################################################################
            vd_da_1_d = r'\True $\int f(x)\text{\text{d}x} = \int \text{d}x + \int \sin %s \text{d}x$' % (latex(k*x))
            vd_da_1_s = r'$\int f(x)\text{d}x = \int \text{d}x - \int \sin %s \text{d}x$' % (latex(k*x))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'''Áp dụng tính chất nguyên hàm của một tổng: \\
                $\int f(x)\text{d}x = \int \left(1 + \sin %s \right) \text{d}x = \int \text{d}x + \int \sin %s \text{d}x$.''' % (latex(k*x), latex(k*x))

            ########################################################################
            # Vận dụng cao: Kết quả nguyên hàm
            ########################################################################
            # Nguyên hàm đúng: x - (1/k)*cos(kx) + C
            nguyen_ham = integrate(f_x_simplified, x)
            vdc_da_1_d = r'\True $\int f(x)\text{d}x = %s + C$' % (latex(nguyen_ham))
            vdc_da_1_s = r'$\int f(x)\text{d}x = x + %s \cos %s + C$' % (latex(1/k), latex(k*x)) # Sai dấu
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r'''Ta có $\int f(x)\text{d}x = x - \frac{1}{%s} \cos %s + C = %s + C$.''' % (latex(k), latex(k*x), latex(nguyen_ham))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chọn đáp án ngẫu nhiên đảm bảo có 1-3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Xuất nội dung theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

