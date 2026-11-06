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


def bt_dang11_p2_b1_c2_hh12(self):
    # Hàm định dạng phương trình mặt phẳng Ax + By + Cz + D = 0
    def format_plane(A_coef, B_coef, C_coef, D_coef):
        terms = []
        if A_coef != 0:
            if A_coef == 1:
                terms.append("x")
            elif A_coef == -1:
                terms.append("-x")
            else:
                terms.append("%sx" % A_coef)

        if B_coef != 0:
            if len(terms) == 0:
                if B_coef == 1:
                    terms.append("y")
                elif B_coef == -1:
                    terms.append("-y")
                else:
                    terms.append("%sy" % B_coef)
            else:
                if B_coef == 1:
                    terms.append("+ y")
                elif B_coef == -1:
                    terms.append("- y")
                elif B_coef > 0:
                    terms.append("+ %sy" % B_coef)
                else:
                    terms.append("- %sy" % abs(B_coef))

        if C_coef != 0:
            if len(terms) == 0:
                if C_coef == 1:
                    terms.append("z")
                elif C_coef == -1:
                    terms.append("-z")
                else:
                    terms.append("%sz" % C_coef)
            else:
                if C_coef == 1:
                    terms.append("+ z")
                elif C_coef == -1:
                    terms.append("- z")
                elif C_coef > 0:
                    terms.append("+ %sz" % C_coef)
                else:
                    terms.append("- %sz" % abs(C_coef))

        if D_coef != 0:
            if D_coef > 0:
                terms.append("+ %s" % D_coef)
            else:
                terms.append("- %s" % abs(D_coef))

        return " ".join(terms) + " = 0"

    # Random hệ số của bài toán
    while True:
        # Mặt phẳng (P): A_P*x + B_P*y + C_P*z + D_P = 0
        # Để mệnh đề d) có dạng ax + by - 2z + d = 0, C_P != 0
        A_P = randint(1, 3)
        B_P = randint(1, 4)
        C_P = randint(1, 3)
        D_P = randint(-6, -1)

        # Điểm M(xM; yM; zM)
        xM = randint(-2, 3)
        yM = randint(-3, 2)
        zM = randint(-3, 2)

        # Điểm A(xA; yA; zA) không thuộc (P) để mp(Q) song song với (P)
        xA = randint(1, 3)
        yA = randint(1, 4)
        zA = randint(-3, -1)
        if A_P * xA + B_P * yA + C_P * zA + D_P == 0:
            continue

        # Mặt phẳng (Q) đi qua A và song song với (P): A_P*x + B_P*y + C_P*z + D_Q = 0
        D_Q = -(A_P * xA + B_P * yA + C_P * zA)
        if D_Q == D_P:
            continue


        if 2 % B_P != 0:
            continue
        k_scale = -2 // B_P
        a_val = 0
        b_val = (-C_P) * k_scale
        c_val = -2
        d_val = 0
        T_val = a_val - 3 * b_val + d_val
        break

    str_plane_P = format_plane(A_P, B_P, C_P, D_P)
    str_plane_Q = format_plane(A_P, B_P, C_P, D_Q)
    str_plane_Q_wrong = format_plane(A_P, B_P, C_P, D_Q + 3)

    # Giá trị thế điểm M vào phương trình (P)
    val_M_sub = A_P * xM + B_P * yM + C_P * zM + D_P

    # Nội dung câu hỏi
    noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(P)$ có phương trình $%s$.''' % str_plane_P)

    ################################################################################
    # Nhận biết: Ý a - Vectơ pháp tuyến của (P)
    nb_da_1_d = '\\True Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\\vec{n} = (%s;%s;%s)$' % (A_P, B_P, C_P)
    nb_da_1_s = 'Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\\vec{n} = (%s;%s;%s)$' % (A_P, B_P + 1, C_P)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Từ phương trình tổng quát của mặt phẳng $(P): %s$, ta có một vectơ pháp tuyến của $(P)$ là $\\vec{n} = (%s;%s;%s)$.'''
                    % (str_plane_P, A_P, B_P, C_P))
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ################################################################################
    # Thông hiểu: Ý b - Điểm M thuộc mặt phẳng (P)
    if val_M_sub == 0:
        th_da_1_d = '\\True Điểm $M(%s;%s;%s)$ thuộc mặt phẳng $(P)$' % (xM, yM, zM)
        th_da_1_s = 'Điểm $M(%s;%s;%s)$ không thuộc mặt phẳng $(P)$' % (xM, yM, zM)
        str_thuoc = '\\text{thuộc}'
        str_symbol = '\\in'
        str_dau = '='
    else:
        th_da_1_d = 'Điểm $M(%s;%s;%s)$ thuộc mặt phẳng $(P)$' % (xM, yM, zM)
        th_da_1_s = '\\True Điểm $M(%s;%s;%s)$ không thuộc mặt phẳng $(P)$' % (xM, yM, zM)
        str_thuoc = '\\text{không thuộc}'
        str_symbol = '\\notin'
        str_dau = '\\neq'

    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Thay toạ độ điểm $M(%s;%s;%s)$ vào phương trình mặt phẳng $(P)$ ta được:\\\\
    $%s \\cdot (%s) + %s \\cdot (%s) + %s \\cdot (%s) %s = %s %s 0$.\\\\
    Do đó điểm $M %s (P)$.'''
                    % (xM, yM, zM,
                       A_P, xM, B_P, yM, C_P, zM,
                       ('+ ' + str(D_P)) if D_P > 0 else ('- ' + str(abs(D_P))),
                       val_M_sub, str_dau, str_symbol))
    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ################################################################################
    # Vận dụng: Ý c - Mặt phẳng (Q) qua A song song với (P)
    vd_da_1_d = '\\True Phương trình mặt phẳng $(Q)$ đi qua $A(%s;%s;%s)$ và song song với mặt phẳng $(P)$ là\\\\$%s$' % (xA, yA, zA, str_plane_Q)
    vd_da_1_s = 'Phương trình mặt phẳng $(Q)$ đi qua $A(%s;%s;%s)$ và song song với mặt phẳng $(P)$ là\\\\$%s$' % (xA, yA, zA, str_plane_Q_wrong)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Mặt phẳng $(Q)$ song song với $(P)$ nên nhận vectơ pháp tuyến của $(P)$ là $\\vec{n} = (%s;%s;%s)$ làm một vectơ pháp tuyến.\\\\
    Phương trình mặt phẳng $(Q)$ đi qua điểm $A(%s;%s;%s)$ là:\\\\
    $%s(x - %s) + %s(y - %s) + %s(z - (%s)) = 0 \\Leftrightarrow %s$.'''
                    % (A_P, B_P, C_P,
                       xA, yA, zA,
                       A_P, xA, B_P, yA, C_P, zA,
                       str_plane_Q))
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ################################################################################
    # Vận dụng cao: Ý d - Mặt phẳng (alpha) chứa trục Ox và vuông góc với (P)
    vdc_da_1_d = '\\True Mặt phẳng $(\\alpha)$ chứa trục $Ox$ và vuông góc với mặt phẳng $(P)$ có phương trình tổng quát dạng $ax+by-2z+d=0$, khi đó $T = a - 3b + d = %s$' % T_val
    vdc_da_1_s = 'Mặt phẳng $(\\alpha)$ chứa trục $Ox$ và vuông góc với mặt phẳng $(P)$ có phương trình tổng quát dạng $ax+by-2z+d=0$, khi đó $T = a - 3b + d = %s$' % (T_val + 5)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Trục $Ox$ đi qua gốc toạ độ $O(0;0;0)$ và có vectơ chỉ phương $\\vec{i} = (1;0;0)$.\\\\
    Mặt phẳng $(P)$ có vectơ pháp tuyến $\\vec{n}_P = (%s;%s;%s)$.\\\\
    Vì mặt phẳng $(\\alpha)$ chứa trục $Ox$ và vuông góc với $(P)$ nên một vectơ pháp tuyến của $(\\alpha)$ là:\\\\
    $\\vec{n}_\\alpha = [\\vec{i}, \\vec{n}_P] = (0 \\cdot %s - 0 \\cdot %s; 0 \\cdot %s - 1 \\cdot %s; 1 \\cdot %s - 0 \\cdot %s) = (0; -%s; %s)$.\\\\
    Mặt phẳng $(\\alpha)$ đi qua $O(0;0;0)$ nên có phương trình: $0(x - 0) - %s(y - 0) + %s(z - 0) = 0 \\Leftrightarrow -%sy + %sz = 0$.\\\\
    Để đưa về dạng $ax + by - 2z + d = 0$, ta nhân hai vế của phương trình với $%s$, ta được:\\\\
    $%sy - 2z = 0 \\Leftrightarrow 0x + %sy - 2z + 0 = 0$.\\\\
    Suy ra $a = 0, b = %s, d = 0$.\\\\
    Khi đó $T = a - 3b + d = 0 - 3 \\cdot (%s) + 0 = %s$.'''
                     % (A_P, B_P, C_P,
                        C_P, B_P, A_P, C_P, B_P, A_P, C_P, B_P,
                        C_P, B_P, C_P, B_P,
                        k_scale,
                        b_val, b_val,
                        b_val,
                        b_val, T_val))
    list_vdc_2 = [loigiai_vdc_1]

    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Kiểm soát số lượng câu đúng từ 1 đến 3
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

    # Xuất câu hỏi dạng Đúng/Sai (choiceTFn)
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n'
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

