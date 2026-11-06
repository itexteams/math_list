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


def bt_dang5_p2_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Hàm phụ để định dạng số thập phân (nếu có) sang dấu phẩy
            def fmt(val):
                s = latex(val)
                return s.replace('.', ',')

            # 1. Random hệ số và nội dung câu hỏi
            # f(x) = ax^2 + bx + c
            # Trong ảnh gốc c = 2. Để random, ta chọn c là số nguyên.
            a_val = randint(1, 3) * random.choice([-1, 1])
            b_val = randint(-5, 5)
            c_val = 2 # Giữ hằng số như đề bài hoặc có thể dùng randint(1, 5)
            f_x = a_val*x**2 + b_val*x + c_val

            noidungcauhoi = ('''Cho hàm số $f\\left( x \\right) = a x^2 + b x + %s, a \\neq 0$ có đồ thị là một Parabol $\\left( P \\right)$.''' 
                             % (latex(c_val)))

            ########################################################################
            # Nhận biết - Câu (a): f'(-1) và f''(1) -> a+b
            ########################################################################
            x1, x2 = -1, 1
            f_prime = diff(f_x, x)
            f_double_prime = diff(f_x, x, 2)
            v1 = f_prime.subs(x, x1)
            v2 = f_double_prime.subs(x, x2)
            sum_ab = a_val + b_val

            nb_da_1_d = '\\True Biết $f\'\\left( %s \\right) = %s$ và $f\'\'\\left( %s \\right) = %s$. Khi đó $a + b = %s$' % (latex(x1), latex(v1), latex(x2), latex(v2), latex(sum_ab))
            nb_da_1_s = 'Biết $f\'\\left( %s \\right) = %s$ và $f\'\'\\left( %s \\right) = %s$. Khi đó $a + b = %s$' % (latex(x1), latex(v1), latex(x2), latex(v2), latex(sum_ab + randint(1, 3)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Ta có $f\'\\left( x \\right) = 2ax + b$ và $f\'\'\\left( x \\right) = 2a$. \\\\
            Từ giả thiết: $\\begin{cases} f\'\'\\left( %s \\right) = 2a = %s \\\\ f\'\\left( %s \\right) = 2a\\left( %s \\right) + b = %s \\end{cases} 
            \\Rightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$. \\\\
            Vậy $a + b = %s + %s = %s$.''' 
                            % (latex(x2), latex(v2), latex(x1), latex(x1), latex(v1), latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(sum_ab)))

            ########################################################################
            # Thông hiểu - Câu (b): Trục đối xứng và f''(x) -> b
            ########################################################################
            x3 = randint(1, 5) * random.choice([-1, 1])
            v3 = f_double_prime.subs(x, x3)
            # Để trục đối xứng là x = x_sym, ta cần -b/2a = x_sym -> b = -2a * x_sym
            x_sym = Rational(-b_val, 2*a_val)

            th_da_1_d = '\\True $\\left( P \\right)$ có trục đối xứng là đường thẳng $x = %s, f\'\'\\left( %s \\right) = %s$. Khi đó $b = %s$' % (fmt(x_sym), latex(x3), latex(v3), latex(b_val))
            th_da_1_s = '$\\left( P \\right)$ có trục đối xứng là đường thẳng $x = %s, f\'\'\\left( %s \\right) = %s$. Khi đó $b = %s$' % (fmt(x_sym), latex(x3), latex(v3), latex(b_val + 1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $f\'\'\\left( x \\right) = 2a = %s \\Rightarrow a = %s$. \\\\
            Trục đối xứng $x = -\\frac{b}{2a} = %s \\Rightarrow b = -2a \\cdot \\left( %s \\right) = %s$.''' 
                            % (latex(v3), latex(a_val), fmt(x_sym), fmt(x_sym), latex(b_val)))

            ########################################################################
            # Vận dụng - Câu (c): Đi qua điểm A và f''(2024) -> b
            ########################################################################
            x4 = 1
            y4 = f_x.subs(x, x4)
            x5 = 2024
            v5 = f_double_prime.subs(x, x5)

            vd_da_1_d = '\\True $\\left( P \\right)$ đi qua điểm $A\\left( %s; %s \\right), f\'\'\\left( %s \\right) = %s$. Khi đó $b = %s$' % (latex(x4), latex(y4), latex(x5), latex(v5), latex(b_val))
            vd_da_1_s = '$\\left( P \\right)$ đi qua điểm $A\\left( %s; %s \\right), f\'\'\\left( %s \\right) = %s$. Khi đó $b = %s$' % (latex(x4), latex(y4), latex(x5), latex(v5), latex(b_val - 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có $f\'\'\\left( %s \\right) = 2a = %s \\Rightarrow a = %s$. \\\\
            $\\left( P \\right)$ đi qua $A\\left( %s; %s \\right) \\Rightarrow a\\left( %s \\right)^2 + b\\left( %s \\right) + %s = %s$. \\\\
            Thay $a = %s$ vào ta được: $%s + b + %s = %s \\Rightarrow b = %s$.''' 
                            % (latex(x5), latex(v5), latex(a_val), latex(x4), latex(y4), latex(x4), latex(x4), latex(c_val), latex(y4), latex(a_val), latex(a_val), latex(c_val), latex(y4), latex(b_val)))

            ########################################################################
            # Vận dụng cao - Câu (d): Cắt trục hoành và f''(-1) -> b
            ########################################################################
            # Để đảm bảo cắt trục hoành tại x_root nguyên, ta tính ngược
            x_root = -1
            # Ta cần f(x_root) = 0 -> a(x_root)^2 + b(x_root) + c = 0
            # Với x_root = -1, c = 2 -> a - b + 2 = 0 -> b = a + 2
            # Điều chỉnh b_val và a_val ở bước này để câu (d) logic
            a_vdc = a_val
            b_vdc = a_vdc + 2
            v7 = 2 * a_vdc

            vdc_da_1_d = '\\True $\\left( P \\right)$ cắt trục hoành tại điểm có hoành độ bằng $%s, f\'\'\\left( %s \\right) = %s$. Khi đó $b = %s$' % (latex(x_root), latex(x_root), latex(v7), latex(b_vdc))
            vdc_da_1_s = '$\\left( P \\right)$ cắt trục hoành tại điểm có hoành độ bằng $%s, f\'\'\\left( %s \\right) = %s$. Khi đó $b = %s$' % (latex(x_root), latex(x_root), latex(v7), latex(b_vdc + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có $f\'\'\\left( %s \\right) = 2a = %s \\Rightarrow a = %s$. \\\\
            $\\left( P \\right)$ cắt trục hoành tại điểm có hoành độ $x = %s \\Rightarrow f\\left( %s \\right) = 0$. \\\\
            Ta có $a\\left( %s \\right)^2 + b\\left( %s \\right) + %s = 0 \\Leftrightarrow %s - b + %s = 0 \\Rightarrow b = %s$.''' 
                             % (latex(x_root), latex(v7), latex(a_vdc), latex(x_root), latex(x_root), latex(x_root), latex(x_root), latex(c_val), latex(a_vdc), latex(c_val), latex(b_vdc)))

            # --- Logic xáo trộn và kiểm tra số câu đúng (giữ nguyên khung của bạn) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lại vào list để zip với lời giải tương ứng
            # Lưu ý: lời giải phải đi kèm với đáp án đã chọn
            idx_nb = list_nb_da_1.index(ans_nb)
            idx_th = list_th_da_1.index(ans_th)
            idx_vd = list_vd_da_1.index(ans_vd)
            idx_vdc = list_vdc_da_1.index(ans_vdc)

            final_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
            final_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(final_answers[0]) + '}\n'
                '{' + str(final_answers[1]) + '}\n'
                '{' + str(final_answers[2]) + '}\n'
                '{' + str(final_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(final_solutions[0]) + '\n'
                '\\item ' + str(final_solutions[1]) + '\n'
                '\\item ' + str(final_solutions[2]) + '\n'
                '\\item ' + str(final_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-').replace('+ -','-')
            return content

