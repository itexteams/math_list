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


def bt_dang10_p2_b3_c3_ds12(self):
                # Khai báo biến
                x = symbols('x')

                # Tạo tham số ngẫu nhiên
                n_val = random.randint(1, 3)
                k = 6 * n_val
                m = random.randint(3, 7)
                c_val = random.randint(1, 3) # Đường thẳng y = c
                a_lim = 1
                b_lim = 4

                f = k*sqrt(x) - m
                f_minus_c = f - c_val

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Cho hình phẳng $(H)$ giới hạn bởi đồ thị hàm số $y = f(x) = %s$, đường thẳng $y = %s$ và hai đường thẳng $x = %s, x = %s$.''' 
                                 % (latex(f), latex(c_val), latex(a_lim), latex(b_lim)))

                ########################################################################
                # a) Nhận biết: Nguyên hàm của f(x)
                ########################################################################
                nh_f = integrate(f, x)
                nb_da_1_d = r'''\True $\int f(x) \text{d}x = %s + C$''' % (latex(nh_f))
                nb_da_1_s = r'''$\int f(x) \text{d}x = %s + C$''' % (latex(k*x - m)) # Sai công thức nguyên hàm

                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                # Biến này sẽ được gán lại trong vòng lặp validation bên dưới
                loigiai_nb_1 = r'''Ta có $\int f(x) \text{d}x = \int (%s) \text{d}x = %s + C$.''' % (latex(f), latex(nh_f))

                ########################################################################
                # b) Thông hiểu: Nguyên hàm của [f(x) - c]
                ########################################################################
                nh_g = integrate(f_minus_c, x)
                th_da_1_d = r'''\True $\int [f(x) - %s] \text{d}x = %s + C$''' % (c_val, latex(nh_g))
                th_da_1_s = r'''$\int [f(x) - %s] \text{d}x = %s + C$''' % (c_val, latex(nh_f)) # Sai vì quên trừ c

                list_th_da_1 = [th_da_1_d, th_da_1_s]
                loigiai_th_1 = r'''Ta có $\int [f(x) - %s] \text{d}x = \int (%s) \text{d}x = %s + C$.''' % (c_val, latex(f_minus_c), latex(nh_g))

                ########################################################################
                # c) Vận dụng: Tích phân xác định
                ########################################################################
                val_b = nh_g.subs(x, b_lim)
                val_a = nh_g.subs(x, a_lim)
                tp_val = val_b - val_a

                vd_da_1_d = r'''\True $\int_{%s}^{%s} [f(x) - %s] \text{d}x = %s$''' % (a_lim, b_lim, c_val, tp_val)
                vd_da_1_s = r'''$\int_{%s}^{%s} [f(x) - %s] \text{d}x = %s$''' % (a_lim, b_lim, c_val, tp_val + random.randint(1, 5))

                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                loigiai_vd_1 = (r'''$\int_{%s}^{%s} [f(x) - %s] \text{d}x = (%s) \Big|_{%s}^{%s} = %s$.''' 
                                % (a_lim, b_lim, c_val, latex(nh_g), a_lim, b_lim, tp_val))

                ########################################################################
                # d) Vận dụng cao: Diện tích hình phẳng
                ########################################################################
                s_val = abs(tp_val)
                vdc_da_1_d = r'''\True Diện tích hình phẳng $(H)$ bằng %s''' % (s_val)
                vdc_da_1_s = r'''Diện tích hình phẳng $(H)$ bằng %s''' % (s_val + 2)

                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                loigiai_vdc_1 = (r'''Diện tích $S = \int_{%s}^{%s} |f(x) - %s| \text{d}x = |%s| = %s$.''' 
                                 % (a_lim, b_lim, c_val, tp_val, s_val))

                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                # Vòng lặp đảm bảo số lượng đáp án đúng từ 1 đến 3
                while True:
                    ans_a = random.choice(list_nb_da_1)
                    ans_b = random.choice(list_th_da_1)
                    ans_c = random.choice(list_vd_da_1)
                    ans_d = random.choice(list_vdc_da_1)

                    if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                        break

                # Xuất nội dung theo template giống dang9
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + 
                    '\n\\choiceTFn \n'
                    '{' + str(ans_a) + '}\n'
                    '{' + str(ans_b) + '}\n'
                    '{' + str(ans_c) + '}\n'
                    '{' + str(ans_d) + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + str(loigiai_nb_1) + '\n'
                    '\\item ' + str(loigiai_th_1) + '\n'
                    '\\item ' + str(loigiai_vd_1) + '\n'
                    '\\item ' + str(loigiai_vdc_1) + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n\\end{minipage}\n\n')

                return content

