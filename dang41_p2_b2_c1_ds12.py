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


def bt_dang41_p2_b2_c1_ds12(self):
    # Khai báo biến
    x = symbols('x')

    # Random các tham số
    a = randint(1, 2)
    b = randint(2, 5)
    c = 3 * (a**2)
    d = randint(1, 4)

    fx = x**3 - 3 * (a**2) * x + b
    gx = c * x + d

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hàm số $y = f(x) = %s$ và $y = g(x) = %s$.'''
                     % (latex(fx), latex(gx)))

    ######################################################################## Nhận biết ############################################
    x3 = -2
    x4 = 1
    val_min_g_true = gx.subs(x, x3)
    val_min_g_false = gx.subs(x, x4) if gx.subs(x, x4) != val_min_g_true else val_min_g_true + 2

    # Các đáp án
    nb_da_1_d = '\\True Giá trị nhỏ nhất của hàm số $g(x)$ trên đoạn $[%s; %s]$ là $%s$' % (x3, x4, latex(val_min_g_true))
    nb_da_1_s = 'Giá trị nhỏ nhất của hàm số $g(x)$ trên đoạn $[%s; %s]$ là $%s$' % (x3, x4, latex(val_min_g_false))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có $g'(x) = %s > 0, \\forall x \\in \\mathbb{R}$, nên hàm số $g(x)$ đồng biến trên đoạn $[%s; %s]$.\\\\
    Suy ra giá trị nhỏ nhất của hàm số $g(x)$ trên đoạn $[%s; %s]$ là $\\min_{[%s; %s]} g(x) = g(%s) = %s$.'''
                    % (latex(c), x3, x4, x3, x4, x3, x4, x3, latex(val_min_g_true)))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ######################################################################## Thông hiểu ############################################
    f_prime = diff(fx, x)
    x5 = 0
    x6 = 2
    val_max_fprime_true = f_prime.subs(x, x6)
    val_max_fprime_false = f_prime.subs(x, x5) if f_prime.subs(x, x5) != val_max_fprime_true else val_max_fprime_true - 2

    # Các đáp án
    th_da_1_d = '\\True Giá trị lớn nhất của hàm số $f\'(x)$ trên đoạn $[%s; %s]$ là $%s$' % (x5, x6, latex(val_max_fprime_true))
    th_da_1_s = 'Giá trị lớn nhất của hàm số $f\'(x)$ trên đoạn $[%s; %s]$ là $%s$' % (x5, x6, latex(val_max_fprime_false))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Ta có $f'(x) = %s$.\\\\
    Đạo hàm của $f'(x)$ là $(f'(x))' = 6x \\ge 0, \\forall x \\in [%s; %s]$, nên hàm số $f'(x)$ đồng biến trên đoạn $[%s; %s]$.\\\\
    Suy ra giá trị lớn nhất của $f'(x)$ trên đoạn [%s; %s] là $\\max_{[%s; %s]} f'(x) = f'(%s) = %s$.'''
                    % (latex(f_prime), x5, x6, x5, x6, x5, x6, x5, x6, x6, latex(val_max_fprime_true)))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################
    k = a
    hx = sp.expand(fx + gx)
    h_prime = diff(hx, x)

    # Các đáp án
    vd_da_1_d = '\\True Hàm số $y = f(x) + g(x)$ đạt giá trị lớn nhất và giá trị nhỏ nhất trên đoạn $[%s; %s]$ lần lượt tại $x_1 = %s; x_2 = %s$' % (latex(-k), latex(k), latex(k), latex(-k))
    vd_da_1_s = 'Hàm số $y = f(x) + g(x)$ đạt giá trị lớn nhất và giá trị nhỏ nhất trên đoạn $[%s; %s]$ lần lượt tại $x_1 = %s; x_2 = %s$' % (latex(-k), latex(k), latex(-k), latex(k))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Xét $h(x) = f(x) + g(x) = %s$.\\\\
    Ta có $h'(x) = %s \\ge 0, \\forall x \\in \\mathbb{R}$, nên hàm số $h(x)$ đồng biến trên đoạn $[%s; %s]$.\\\\
    Do đó hàm số $h(x)$ đạt giá trị lớn nhất tại $x_1 = %s$ và đạt giá trị nhỏ nhất tại $x_2 = %s$.'''
                    % (latex(hx), latex(h_prime), latex(-k), latex(k), latex(k), latex(-k)))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################
    k0 = a
    m0 = randint(1, 2)
    u0 = m0 + k0
    K_val = fx.subs(x, u0)

    # Các đáp án
    vdc_da_1_d = '\\True Với $m$ là tham số dương. Để $\\min_{[m+%s; m+%s]} f(x) = %s$ thì $m = %s$' % (k0, k0 + 1, latex(K_val), m0)
    vdc_da_1_s = 'Với $m$ là tham số dương. Để $\\min_{[m+%s; m+%s]} f(x) = %s$ thì $m = %s$' % (k0, k0 + 1, latex(K_val), m0 + 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Vì $m > 0$ nên với mọi $x \\in [m+%s; m+%s]$, ta có $x \\ge m+%s > %s$.\\\\
    Ta có $f'(x) = %s > 0, \\forall x \\in [m+%s; m+%s]$.\\\\
    Do đó hàm số $f(x)$ đồng biến trên đoạn $[m+%s; m+%s]$.\\\\
    Suy ra $\\min_{[m+%s; m+%s]} f(x) = f(m+%s) = (m+%s)^3 - %s(m+%s) + %s$.\\\\
    Để $\\min_{[m+%s; m+%s]} f(x) = %s \\Leftrightarrow (m+%s)^3 - %s(m+%s) + %s = %s \\Leftrightarrow m = %s$ (do $m > 0$).'''
                     % (k0, k0 + 1, k0, a, latex(f_prime), k0, k0 + 1, k0, k0 + 1, k0, k0 + 1, k0, k0, latex(3 * (a**2)), k0, latex(b), k0, k0 + 1, latex(K_val), k0, latex(3 * (a**2)), k0, latex(b), latex(K_val), m0))

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' +
    str(noidungcauhoi) + 
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
        '\\end{ex}\n \\end{minipage}\n\n')
    return content

