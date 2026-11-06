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


def bt_dang6_p2_b1_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ đổi dấu chấm thành dấu phẩy cho số thập phân
            def format_decimal(val):
                return str(float(val)).replace('.', ',')

            # Khai báo các giá trị ngẫu nhiên
            # p1: P(A), p2: P(B), p12: P(A \cap B)
            p1 = Rational(random.choice([2, 4, 5, 6]), 10)
            p2 = Rational(random.choice([5, 6, 7]), 10)

            # Điều kiện tồn tại: p12 <= min(p1, p2) và p12 >= p1 + p2 - 1
            min_p12 = max(0, p1 + p2 - 1)
            max_p12 = min(p1, p2)
            # Lấy p12 sao cho thường là không độc lập
            p12 = Rational(random.randint(int(min_p12*10) + 1, int(max_p12*10) - 1), 10)

            # Các giá trị tính toán dưới dạng Rational
            p_not_A = 1 - p1
            p_not_B = 1 - p2
            p_exactly_1 = p1 + p2 - 2*p12
            p_B_given_A = p12 / p1
            p_B_given_not_A = (p2 - p12) / p_not_A

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một công ty đấu thầu 2 dự án. Khả năng thắng thầu của dự án 1 là $%s$ và khả năng thắng thầu của dự án 2 là $%s$. Khả năng thắng thầu cả 2 dự án là $%s$.
            Gọi $A$ là biến cố: "Thắng thầu dự án 1"
            Gọi $B$ là biến cố: "Thắng thầu dự án 2".
            Khi đó:''' % (format_decimal(p1), format_decimal(p2), format_decimal(p12)))

            ########################################################################
            # Nhận biết (Câu a)
            ########################################################################
            is_independent = (p12 == p1 * p2)
            if is_independent:
                nb_da_1_d = '\\True $A$ và $B$ là hai biến cố độc lập'
                nb_da_1_s = '$A$ và $B$ là hai biến cố không độc lập'
            else:
                nb_da_1_d = '\\True $A$ và $B$ là hai biến cố không độc lập'
                nb_da_1_s = '$A$ và $B$ là hai biến cố độc lập'

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Theo đề, ta có: $P(A)=%s \\Rightarrow P(\\overline{A})=%s$ \\\\
            $P(B)=%s \\Rightarrow P(\\overline{B})=%s$ \\\\
            $P(A \\cap B)=%s$ \\\\
            Nhận thấy $P(A \\cap B) %s P(A) \\cdot P(B)$ (vì $%s %s %s$) \\\\
            Do đó $A$ và $B$ là hai biến cố %s độc lập.''' 
                            % (format_decimal(p1), format_decimal(p_not_A), 
                               format_decimal(p2), format_decimal(p_not_B), 
                               format_decimal(p12), 
                               '=' if is_independent else '\\neq',
                               format_decimal(p12), '=' if is_independent else '\\neq', format_decimal(p1*p2),
                               '' if is_independent else 'không'))

            ########################################################################
            # Thông hiểu (Câu b)
            ########################################################################
            th_val_d = format_decimal(p_exactly_1)
            th_val_s = format_decimal(p1 + p2 - p12) # Xác suất thắng ít nhất 1 dự án (sai so với đề)
            th_da_1_d = '\\True Xác suất để công ty thắng thầu đúng 1 dự án bằng $%s$' % th_val_d
            th_da_1_s = 'Xác suất để công ty thắng thầu đúng 1 dự án bằng $%s$' % th_val_s

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Gọi $C$ là biến cố "thắng thầu đúng 1 dự án". \\\\
            $P(C) = P(A \\cap \\overline{B}) + P(\\overline{A} \\cap B) = P(A) - P(A \\cap B) + P(B) - P(A \\cap B)$ \\\\
            $= %s + %s - 2 \\cdot %s = %s$.''' 
                            % (format_decimal(p1), format_decimal(p2), format_decimal(p12), format_decimal(p_exactly_1)))

            ########################################################################
            # Vận dụng (Câu c)
            ########################################################################
            vd_val_d = latex(p_B_given_A)
            vd_val_s = format_decimal(p12)
            vd_da_1_d = '\\True Xác suất để công ty thắng thầu dự án 2 biết công ty thắng thầu dự án 1 là $%s$' % vd_val_d
            vd_da_1_s = 'Xác suất để công ty thắng thầu dự án 2 biết công ty thắng thầu dự án 1 là $%s$' % vd_val_s

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Gọi $D$ là biến cố "thắng dự án 2 biết thắng dự án 1". \\\\
            $P(D) = P(B|A) = \\frac{P(B \\cap A)}{P(A)} = \\frac{%s}{%s} = %s$.'''
                            % (format_decimal(p12), format_decimal(p1), latex(p_B_given_A)))

            ########################################################################
            # Vận dụng cao (Câu d)
            ########################################################################
            vdc_val_d = latex(p_B_given_not_A)
            vdc_val_s = format_decimal(p2)
            vdc_da_1_d = '\\True Xác suất để công ty thắng thầu dự án 2 biết công ty không thắng thầu dự án 1 là $%s$' % vdc_val_d
            vdc_da_1_s = 'Xác suất để công ty thắng thầu dự án 2 biết công ty không thắng thầu dự án 1 là $%s$' % vdc_val_s

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Gọi $E$ là biến cố "thắng dự án 2 biết không thắng dự án 1". \\\\
            $P(E) = P(B|\\overline{A}) = \\frac{P(B \\cap \\overline{A})}{P(\\overline{A})} = \\frac{P(B) - P(A \\cap B)}{P(\\overline{A})} = \\frac{%s - %s}{%s} = %s$.'''
                             % (format_decimal(p2), format_decimal(p12), format_decimal(p_not_A), latex(p_B_given_not_A)))

            # Logic chọn đáp án đúng/sai (1-3 câu đúng)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    break

            # Gán danh sách đáp án và lời giải (giữ nguyên thứ tự a, b, c, d)
            shuffled_answers = [d1, d2, d3, d4]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

