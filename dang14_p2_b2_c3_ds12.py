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


def bt_dang14_p2_b2_c3_ds12(self):
                # --- KHAI BÁO BIẾN NGẪU NHIÊN ---
                x = symbols('x')
                m = random.choice([2, 4, 6]) 
                n = random.randint(2, 5)
                f_expr = exp(x)
                g_expr = m * exp(x) - n

                # Nội dung câu hỏi
                noidungcauhoi = (r"""Cho hai hàm số $f(x)=e^x$ và $g(x)=%s$.""" % (latex(g_expr)))

                ########################################################################
                # Nhận biết ############################################################
                val_nb_true = m - n * ln(2)
                nb_da_1_d = r'\True Tích phân $\int_0^{\ln 2} g(x) \text{d}x = %s$' % (latex(val_nb_true))
                nb_da_1_s = r'Tích phân $\int_0^{\ln 2} g(x) \text{d}x = %s$' % (latex(m + n * ln(2)))
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                nb_da_1 = random.choice(list_nb_da_1)
                list_nb_1 = [nb_da_1]

                loigiai_nb_1 = (r'''Ta có $\int_0^{\ln 2} g(x) \text{d}x = \int_0^{\ln 2} (%s) \text{d}x = \left(%s e^x - %sx \right) \Big|_0^{\ln 2} = (%s \cdot 2 - %s \ln 2) - (%s \cdot 1 - 0) = %s$.''' 
                                % (latex(g_expr), m, n, m, n, m, latex(val_nb_true)))
                list_nb_2 = [loigiai_nb_1]

                # Xáo trộn Nhận biết
                combined_nb = list(zip(list_nb_1, list_nb_2))
                random.shuffle(combined_nb)
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ########################################################################
                # Thông hiểu ###########################################################
                p_limit = 2
                val_b_const = n * p_limit
                th_da_1_d = r'\True Hệ thức $%s \int_0^{%s} f(x) \text{d}x = %s + \int_0^{%s} g(x) \text{d}x$ là đúng' % (m, p_limit, val_b_const, p_limit)
                th_da_1_s = r'Hệ thức $\int_0^{%s} g(x) \text{d}x = %s \int_0^{%s} f(x) \text{d}x + %s$ là đúng' % (p_limit, m, p_limit, val_b_const)
                list_th_da_1 = [th_da_1_d, th_da_1_s]
                th_da_1 = random.choice(list_th_da_1)
                list_th_1 = [th_da_1]

                loigiai_th_1 = (r'''Ta có $g(x) = %s f(x) - %s$. Khi đó: $\int_0^{%s} g(x) \text{d}x = \int_0^{%s} [%s f(x) - %s] \text{d}x = %s \int_0^{%s} f(x) \text{d}x - %s \cdot %s$. Suy ra $%s \int_0^{%s} f(x) \text{d}x = %s + \int_0^{%s} g(x) \text{d}x$.''' 
                                % (m, n, p_limit, p_limit, m, n, m, p_limit, n, p_limit, m, p_limit, val_b_const, p_limit))
                list_th_2 = [loigiai_th_1]

                # Xáo trộn Thông hiểu
                combined_th = list(zip(list_th_1, list_th_2))
                random.shuffle(combined_th)
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ########################################################################
                # Vận dụng #############################################################
                limit_c1 = 2
                limit_c2 = 7
                val_c = n * (limit_c2 - limit_c1)
                vd_da_1_d = r'\True Tích phân $\int_{%s}^{%s} [%s f(x) - g(x)] \text{d}x = %s$' % (limit_c1, limit_c2, m, val_c)
                vd_da_1_s = r'Tích phân $\int_{%s}^{%s} [%s f(x) - g(x)] \text{d}x = %s$' % (limit_c1, limit_c2, m, val_c + 1)
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                vd_da_1 = random.choice(list_vd_da_1)
                list_vd_1 = [vd_da_1]

                loigiai_vd_1 = (r'''Xét hiệu $%s f(x) - g(x) = %s e^x - (%s e^x - %s) = %s$. Do đó $\int_{%s}^{%s} [%s f(x) - g(x)] \text{d}x = \int_{%s}^{%s} %s \text{d}x = %s x \Big|_{%s}^{%s} = %s$.''' 
                                % (m, m, m, n, n, limit_c1, limit_c2, m, limit_c1, limit_c2, n, n, limit_c1, limit_c2, val_c))
                list_vd_2 = [loigiai_vd_1]

                # Xáo trộn Vận dụng
                combined_vd = list(zip(list_vd_1, list_vd_2))
                random.shuffle(combined_vd)
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ########################################################################
                # Vận dụng cao #########################################################
                a_coeff = Rational(m, 2)
                b_coeff = -n
                c_coeff = n - Rational(m, 2)
                sum_abc = a_coeff + b_coeff + c_coeff 

                vdc_da_1_d = r'\True Nếu $\int_0^1 f(x) \cdot g(x) \text{d}x = a e^2 + b e + c$ ($a,b,c \in \mathbb{Q}$) thì $a+b+c = %s$' % (latex(sum_abc))
                vdc_da_1_s = r'Nếu $\int_0^1 f(x) \cdot g(x) \text{d}x = a e^2 + b e + c$ ($a,b,c \in \mathbb{Q}$) thì $a+b+c = %s$' % (latex(sum_abc + 1))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                vdc_da_1 = random.choice(list_vdc_da_1)
                list_vdc_1 = [vdc_da_1]

                loigiai_vdc_1 = (r'''Ta có $f(x) \cdot g(x) = e^x(%s e^x - %s) = %s e^{2x} - %s e^x$. Khi đó $\int_0^1 f(x) \cdot g(x) \text{d}x = \int_0^1 (%s e^{2x} - %s e^x) \text{d}x = \left( %s e^{2x} - %s e^x \right) \Big|_0^1 = (%s e^2 - %s e) - (%s - %s) = %s e^2 - %s e + %s$. Suy ra $a=%s, b=%s, c=%s \Rightarrow a+b+c = %s$.''' 
                                % (m, n, m, n, m, n, latex(a_coeff), n, latex(a_coeff), n, latex(a_coeff), n, latex(a_coeff), n, latex(c_coeff), latex(a_coeff), b_coeff, latex(c_coeff), latex(sum_abc)))
                list_vdc_2 = [loigiai_vdc_1]

                # Xáo trộn Vận dụng cao
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))
                random.shuffle(combined_vdc)
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

                # --- KIỂM TRA SỐ LƯỢNG ĐÁP ÁN ĐÚNG (1-3) ---
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    nb_sel = random.choice(list_nb_da_1)
                    th_sel = random.choice(list_th_da_1)
                    vd_sel = random.choice(list_vd_da_1)
                    vdc_sel = random.choice(list_vdc_da_1)
                    if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                        shuffled_answers_nb = [nb_sel]
                        shuffled_answers_th = [th_sel]
                        shuffled_answers_vd = [vd_sel]
                        shuffled_answers_vdc = [vdc_sel]
                        break

                # --- XUẤT NỘI DUNG ---
                content = ('\\begin{minipage}{\\textwidth} \n'
                        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                        '\\choiceTFn \n'
                        '{' + str(shuffled_answers_nb[0]) + '}\n'
                        '{' + str(shuffled_answers_th[0]) + '}\n'
                        '{' + str(shuffled_answers_vd[0]) + '}\n'
                        '{' + str(shuffled_answers_vdc[0]) + '}\n'
                        '\\loigiai{ \n'
                        '\\begin{enumEX}[a)]{1} \n'
                        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                        '\\end{enumEX}} \n'
                        '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')

                return content

