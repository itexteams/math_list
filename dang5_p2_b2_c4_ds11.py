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


def bt_dang5_p2_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 1: NGẪU NHIÊN HÓA CÁC HỆ SỐ (Đảm bảo số đẹp như hình)
            a_val = random.randint(2, 9)        # Ví dụ: 2
            b_val = random.randint(-10, -2)     # Ví dụ: -6
            c_val = random.randint(1, 10)       # Ví dụ: 5
            d_val = random.randint(-9, -1)      # Ví dụ: -3 (để x-3)

            # Các biểu thức toán học
            f_num = sqrt(a_val**2 * x**2 + b_val * x + c_val)
            f_den = x + d_val  # x - 3
            g_x_expr = (a_val * x) / (x + d_val)

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $f(x)=\frac{%s}{%s}$ và $g(x)=\frac{%s}{%s}$.''' % (
                latex(f_num), latex(f_den), latex(a_val*x), latex(f_den)
            )

            ########################################################################
            # Nhận biết: Giới hạn của g(x) tại +vô cực
            ########################################################################
            nb_da_1_d = r'\True $\lim_{x \to +\infty} g(x) = %s$' % (latex(a_val))
            nb_da_1_s = r'$\lim_{x \to +\infty} g(x) = 0$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Lời giải a
            loigiai_nb_1 = r'''$\lim_{x \to +\infty} g(x) = \lim_{x \to +\infty} \frac{%sx}{x %s} = \lim_{x \to +\infty} \frac{%s}{1 %s} = %s$.''' % (
                latex(a_val), latex(d_val), latex(a_val), latex(d_val/x), latex(a_val)
            )

            ########################################################################
            # Thông hiểu: Giới hạn của f(x) tại +vô cực
            ########################################################################
            th_da_1_d = r'\True $\lim_{x \to +\infty} f(x) = %s$' % (latex(a_val))
            th_da_1_s = r'$\lim_{x \to +\infty} f(x) = -\infty$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Lời giải b
            loigiai_th_1 = r'''$\lim_{x \to +\infty} f(x) = \lim_{x \to +\infty} \frac{x\sqrt{%s %s + %s}}{x(1 %s)} = %s$.''' % (
                latex(a_val**2), latex(b_val/x), latex(c_val/x**2), latex(d_val/x), latex(a_val)
            )

            ########################################################################
            # Vận dụng: Giới hạn của f(x) tại -vô cực
            ########################################################################
            vd_da_1_d = r'\True $\lim_{x \to -\infty} f(x) = %s$' % (latex(-a_val))
            vd_da_1_s = r'$\lim_{x \to -\infty} f(x) = %s$' % (latex(a_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Lời giải c
            loigiai_vd_1 = r'''$\lim_{x \to -\infty} f(x) = \lim_{x \to -\infty} \frac{-x\sqrt{%s %s + %s}}{x(1 %s)} = -%s$.''' % (
                latex(a_val**2), latex(b_val/x), latex(c_val/x**2), latex(d_val/x), latex(a_val)
            )

            ########################################################################
            # Vận dụng cao: Giới hạn [f(x)-g(x)](x-d)
            ########################################################################
            # Kết quả là b / (2*a)
            ketqua_d = Rational(b_val, 2 * a_val)
            vdc_da_1_d = r'\True $\lim_{x \to +\infty} [f(x)-g(x)](x %s) = %s$' % (latex(d_val), latex(ketqua_d))
            vdc_da_1_s = r'$\lim_{x \to +\infty} [f(x)-g(x)](x %s) = %s$' % (latex(d_val), latex(b_val))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Lời giải d
            loigiai_vdc_1 = r'''$\lim_{x \to +\infty} [f(x)-g(x)](x %s) = \lim_{x \to +\infty} (\sqrt{%sx^2 %sx + %s} - %sx) \\= \lim_{x \to +\infty} \frac{%sx + %s}{\sqrt{%sx^2 %sx + %s} + %sx} = \frac{%s}{%s} = %s$.''' % (
                latex(d_val), a_val**2, ("+" if b_val > 0 else "") + str(b_val), c_val, a_val,
                b_val, c_val, a_val**2, ("+" if b_val > 0 else "") + str(b_val), c_val, a_val,
                b_val, 2*a_val, latex(ketqua_d)
            )

            # Hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum(1 for ans in answers if r'\True' in ans)

            # Vòng lặp xáo trộn theo mẫu
            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Xuất nội dung
            content = (r'\begin{minipage}{\textwidth}' + '\n'
                r'\begin{ex}' + '\n' +
                str(noidungcauhoi) + '\n'
                r'\choiceTFn' + '\n'
                '{' + ans_nb + '}\n'
                '{' + ans_th + '}\n'
                '{' + ans_vd + '}\n'
                '{' + ans_vdc + '}\n'
                r'\loigiai{' + '\n'
                r'\begin{enumEX}[a)]{1}' + '\n'
                r'\item ' + loigiai_nb_1 + '\n'
                r'\item ' + loigiai_th_1 + '\n'
                r'\item ' + loigiai_vd_1 + '\n'
                r'\item ' + loigiai_vdc_1 + '\n'
                r'\end{enumEX}}' + '\n'
                r'\end{ex}' + '\n' + r'\end{minipage}' + '\n\n')
            return content

