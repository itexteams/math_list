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


def bt_dang15_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Khởi tạo các giá trị ngẫu nhiên cho bài toán f(x) = m - n*ln(x + k)
            # Theo ảnh: m=90, n=18, k=2
            k_val = random.randint(1, 3)
            n_val = random.choice([12, 18, 24])
            m_val = random.choice([80, 90, 100])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=%s-%s \\ln(x+%s)$.''' 
                             % (latex(m_val), latex(n_val), latex(k_val)))

            ########################################################################
            # a) Nhận biết: Tập xác định
            ########################################################################
            nb_da_1_d = '\\True Tập xác định của hàm số đã cho là $\\mathscr{D}=\\left( -%s;+\\infty \\right)$' % (latex(k_val))
            nb_da_1_s = 'Tập xác định của hàm số đã cho là $\\mathscr{D}=\\left( %s;+\\infty \\right)$' % (latex(k_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Hàm số xác định khi $x+%s > 0 \\Leftrightarrow x > -%s$. \\\\ Vậy tập xác định của hàm số là $\\mathscr{D}=\\left( -%s;+\\infty \\right)$.''' 
                            % (latex(k_val), latex(k_val), latex(k_val)))

            ########################################################################
            # b) Thông hiểu: Tính đơn điệu
            ########################################################################
            th_da_1_d = '\\True Hàm số đã cho nghịch biến trên khoảng $\\left( -%s;+\\infty \\right)$' % (latex(k_val))
            th_da_1_s = 'Hàm số đã cho đồng biến trên khoảng $\\left( -%s;+\\infty \\right)$' % (latex(k_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Ta có $f\'(x)= -\\frac{%s}{x+%s}$. \\\\ Với mọi $x \\in \\left( -%s;+\\infty \\right)$ thì $x+%s > 0$ nên $f\'(x) < 0$. \\\\ Suy ra hàm số nghịch biến trên khoảng $\\left( -%s;+\\infty \\right)$.''' 
                            % (latex(n_val), latex(k_val), latex(k_val), latex(k_val), latex(k_val)))

            ########################################################################
            # c) Vận dụng: Giải bất phương trình f(x) >= C
            ########################################################################
            # Chọn C sao cho (m-C)/n là số thực để tính số nghiệm nguyên
            C_val = m_val - random.choice([24, 36, 48]) 
            ratio_val = Rational(m_val - C_val, n_val)
            # Số nghiệm nguyên trên (-k; e^(ratio)-k] là floor(e^ratio)
            num_sol = math.floor(math.exp(float(ratio_val)))

            vd_da_1_d = '\\True Bất phương trình $f(x) \\ge %s$ có đúng %s nghiệm nguyên' % (latex(C_val), latex(num_sol))
            vd_da_1_s = 'Bất phương trình $f(x) \\ge %s$ có đúng %s nghiệm nguyên' % (latex(C_val), latex(num_sol - 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Lời giải chi tiết với đúng 16 tham số %s để tránh lỗi TypeError
            loigiai_vd_1 = ('''Ta có $f(x) \\ge %s \\Leftrightarrow %s - %s \\ln(x+%s) \\ge %s \\Leftrightarrow \\ln(x+%s) \\le %s \\\\ \\Leftrightarrow x+%s \\le e^{%s} \\Leftrightarrow x \\le e^{%s} - %s$. \\\\ Kết hợp điều kiện $x > -%s$, ta có $x \\in \\left( -%s; e^{%s} - %s \\right]$. \\\\ Vì $e^{%s} \\approx %s$ nên số nghiệm nguyên là %s.''' 
                            % (
                                latex(C_val), latex(m_val), latex(n_val), latex(k_val), latex(C_val), 
                                latex(k_val), latex(ratio_val), latex(k_val), latex(ratio_val), 
                                latex(ratio_val), latex(k_val), latex(k_val), latex(k_val), 
                                latex(ratio_val), latex(k_val), latex(ratio_val), 
                                str(round(math.exp(float(ratio_val)), 2)).replace('.', ','), latex(num_sol)
                            ))

            ########################################################################
            # d) Vận dụng cao: GTNN của g(x) = f(x) + 3x trên [1, 5]
            ########################################################################
            p_val = 3
            x_start, x_end = 1, 5
            x0_val = n_val / p_val - k_val # Nghiệm của g'(x) = 0

            def calc_g(val_x):
                return m_val - n_val * math.log(val_x + k_val) + p_val * val_x

            # Tìm Min trong các giá trị biên và điểm cực trị
            points = {x_start: calc_g(x_start), x_end: calc_g(x_end)}
            if x_start < x0_val < x_end:
                points[x0_val] = calc_g(x0_val)

            min_x_point = min(points, key=points.get)
            min_val_latex = '%s - %s \\ln %s' % (latex(int(m_val + p_val * min_x_point)), latex(n_val), latex(int(min_x_point + k_val)))

            vdc_da_1_d = '\\True Giá trị nhỏ nhất của hàm số $g(x) = f(x) + %sx$ trên đoạn $[%s; %s]$ bằng $%s$' % (latex(p_val), latex(x_start), latex(x_end), min_val_latex)
            vdc_da_1_s = 'Giá trị nhỏ nhất của hàm số $g(x) = f(x) + %sx$ trên đoạn $[%s; %s]$ bằng $%s$' % (latex(p_val), latex(x_start), latex(x_end), latex(m_val))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Xét $g(x) = f(x) + %sx = %s - %s \\ln(x+%s) + %sx$ trên $[%s; %s]$. \\\\ Ta có $g\'(x) = -\\frac{%s}{x+%s} + %s = \\frac{%sx + %s - %s}{x+%s}$. \\\\ $g\'(x) = 0 \\Leftrightarrow x = %s$. \\\\ So sánh giá trị tại các điểm $x \\in \\{%s; %s; %s\\}$, ta được giá trị nhỏ nhất là $%s$.''' 
                             % (latex(p_val), latex(m_val), latex(n_val), latex(k_val), latex(p_val), latex(x_start), latex(x_end),
                                latex(n_val), latex(k_val), latex(p_val), latex(p_val), latex(p_val*k_val), latex(n_val), latex(k_val),
                                latex(int(x0_val)), latex(x_start), latex(x_end), latex(int(x0_val)), min_val_latex))

            ########################################################################
            # Trộn đáp án và Xuất kết quả
            ########################################################################
            def check_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                da_a = random.choice(list_nb_da_1)
                da_b = random.choice(list_th_da_1)
                da_c = random.choice(list_vd_da_1)
                da_d = random.choice(list_vdc_da_1)
                if 1 <= check_true([da_a, da_b, da_c, da_d]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(da_a) + '}\n'
                '{' + str(da_b) + '}\n'
                '{' + str(da_c) + '}\n'
                '{' + str(da_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

