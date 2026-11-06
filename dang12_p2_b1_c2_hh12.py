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


def bt_dang12_p2_b1_c2_hh12(self):
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

    # Random tham số bài toán
    while True:
        # Mặt phẳng (Q): A_Q*x + B_Q*y + C_Q*z + D_Q = 0
        A_Q = randint(-12, -6)
        B_Q = randint(20, 50)
        C_Q = randint(-10, -5)

        # Sinh điểm K(xK; yK; zK)
        xK = randint(1, 6)
        yK = randint(1, 4)
        zK = randint(1, 6)
        # Đặt D_Q sao cho điểm K thuộc (Q)
        D_Q = -(A_Q * xK + B_Q * yK + C_Q * zK)

        # Hai điểm H và C
        xH, yH, zH = randint(3, 7), randint(1, 4), randint(3, 6)
        # Để đơn giản như bài toán mẫu, cho cùng tung độ yC = yH hoặc khác một chút
        dx = randint(-5, -2)
        dy = 0
        dz = randint(-9, -5)
        xC, yC, zC = xH + dx, yH + dy, zH + dz

        # Vectơ HC = (dx, dy, dz)
        # Tích có hướng: n_P = [HC, n_Q]
        nP_x = dy * C_Q - dz * B_Q
        nP_y = dz * A_Q - dx * C_Q
        nP_z = dx * B_Q - dy * A_Q

        if nP_x == 0 and nP_y == 0 and nP_z == 0:
            continue

        # Tính hệ số tự do D_planeP = -(nP_x * xH + nP_y * yH + nP_z * zH)
        D_planeP = -(nP_x * xH + nP_y * yH + nP_z * zH)

        if D_planeP == 0:
            continue

        a_val = nP_x
        b_val = nP_y
        c_val = nP_z
        sum_abc = a_val + b_val + c_val
        break

    # Mặt phẳng (P_songsong) ở ý c: lấy bội số k = 2
    k_mult = 2
    A_P_c = k_mult * A_Q
    B_P_c = k_mult * B_Q
    C_P_c = k_mult * C_Q
    D_P_c = -1 if D_Q != -1 else -2  # Đảm bảo D_P_c != k_mult * D_Q

    str_plane_Q = format_plane(A_Q, B_Q, C_Q, D_Q)
    str_plane_P_c = format_plane(A_P_c, B_P_c, C_P_c, D_P_c)

    # Nội dung câu hỏi[cite: 4]
    noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(Q)$ có phương trình $%s$.''' % str_plane_Q)

    ################################################################################
    # Nhận biết: Ý a - Vectơ pháp tuyến của (Q)[cite: 4]
    vec_n_opp = (-A_Q, -B_Q, -C_Q)

    nb_da_1_d = '$\\vec{n} = (%s; %s; %s)$ không phải là một vectơ pháp tuyến của $(Q)$' % (vec_n_opp[0], vec_n_opp[1], vec_n_opp[2])
    nb_da_1_s = '\\True $\\vec{n} = (%s; %s; %s)$ là một vectơ pháp tuyến của $(Q)$' % (vec_n_opp[0], vec_n_opp[1], vec_n_opp[2])
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Mặt phẳng $(Q)$ có một vectơ pháp tuyến là $\\vec{n}_Q = (%s; %s; %s)$.\\\\
    Ta có $\\vec{n} = (%s; %s; %s) = -1 \\cdot (%s; %s; %s) = -\\vec{n}_Q$.\\\\
    Do đó $\\vec{n}$ cũng là một vectơ pháp tuyến của $(Q)$.'''
                    % (A_Q, B_Q, C_Q,
                       vec_n_opp[0], vec_n_opp[1], vec_n_opp[2],
                       A_Q, B_Q, C_Q))
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ################################################################################
    # Thông hiểu: Ý b - Điểm K thuộc mặt phẳng (Q)[cite: 4]
    th_da_1_d = '\\True Điểm $K(%s;%s;%s)$ thuộc mặt phẳng $(Q)$' % (xK, yK, zK)
    th_da_1_s = 'Điểm $K(%s;%s;%s)$ không thuộc mặt phẳng $(Q)$' % (xK, yK, zK)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Thay toạ độ điểm $K(%s;%s;%s)$ vào phương trình mặt phẳng $(Q)$, ta được:\\\\
    $(%s) \\cdot %s + (%s) \\cdot %s + (%s) \\cdot %s %s = %s + %s + %s %s = 0$.\\\\
    Vậy điểm $K(%s;%s;%s)$ thuộc mặt phẳng $(Q)$.'''
                    % (xK, yK, zK,
                       A_Q, xK, B_Q, yK, C_Q, zK,
                       ('+ ' + str(D_Q)) if D_Q > 0 else ('- ' + str(abs(D_Q))),
                       A_Q * xK, B_Q * yK, C_Q * zK,
                       ('+ ' + str(D_Q)) if D_Q > 0 else ('- ' + str(abs(D_Q))),
                       xK, yK, zK))
    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ################################################################################
    # Vận dụng: Ý c - Vị trí tương đối của hai mặt phẳng (Q) và (P)[cite: 4]
    vd_da_1_d = 'Mặt phẳng $(Q)$ và mặt phẳng $(P): %s$ cắt nhau' % str_plane_P_c
    vd_da_1_s = '\\True Mặt phẳng $(Q)$ và mặt phẳng $(P): %s$ song song với nhau' % str_plane_P_c
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Mặt phẳng $(Q)$ có vectơ pháp tuyến $\\vec{n}_Q = (%s; %s; %s)$.\\\\
    Mặt phẳng $(P)$ có vectơ pháp tuyến $\\vec{n}_P = (%s; %s; %s)$.\\\\
    Xét tỉ lệ giữa các hệ số:\\\\
    $\\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s} = %s \\neq \\frac{%s}{%s}$.\\\\
    Do đó mặt phẳng $(Q)$ song song với mặt phẳng $(P)$ (kí hiệu $(Q) // (P)$).'''
                    % (A_Q, B_Q, C_Q,
                       A_P_c, B_P_c, C_P_c,
                       A_P_c, A_Q, B_P_c, B_Q, C_P_c, C_Q,
                       k_mult,
                       D_P_c, D_Q))
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ################################################################################
    # Vận dụng cao: Ý d - Mặt phẳng qua H, C và vuông góc với (Q)[cite: 4]
    sign_d = '+ %s' % D_planeP if D_planeP > 0 else '- %s' % abs(D_planeP)

    vdc_da_1_d = ('\\True Mặt phẳng $(P)$ đi qua hai điểm $H(%s;%s;%s), C(%s;%s;%s)$ và vuông góc với $(Q)$ có phương trình dạng $ax+by+cz %s = 0$. Khi đó $a+b+c = %s$' 
                  % (xH, yH, zH, xC, yC, zC, sign_d, sum_abc))
    vdc_da_1_s = ('Mặt phẳng $(P)$ đi qua hai điểm $H(%s;%s;%s), C(%s;%s;%s)$ và vuông góc với $(Q)$ có phương trình dạng $ax+by+cz %s = 0$. Khi đó $a+b+c = %s$' 
                  % (xH, yH, zH, xC, yC, zC, sign_d, sum_abc + randint(5, 15)))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Ta có $\\vec{HC} = (%s - %s; %s - %s; %s - %s) = (%s; %s; %s)$.\\\\
    Mặt phẳng $(Q)$ có vectơ pháp tuyến $\\vec{n}_Q = (%s; %s; %s)$.\\\\
    Vì mặt phẳng $(P)$ đi qua hai điểm $H, C$ và vuông góc với $(Q)$ nên nhận vectơ pháp tuyến là:\\\\
    $\\vec{n}_P = [\\vec{HC}, \\vec{n}_Q] = (%s \\cdot (%s) - (%s) \\cdot %s; (%s) \\cdot (%s) - (%s) \\cdot (%s); (%s) \\cdot %s - (%s) \\cdot (%s)) = (%s; %s; %s)$.\\\\
    Phương trình mặt phẳng $(P)$ đi qua điểm $H(%s;%s;%s)$ là:\\\\
    $%s(x - %s) + %s(y - %s) + (%s)(z - %s) = 0 \\Leftrightarrow %s x + %s y + %s z %s = 0$.\\\\
    Đồng nhất với dạng $ax + by + cz %s = 0$, ta được:\\\\
    $a = %s, b = %s, c = %s$.\\\\
    Khi đó $a + b + c = %s + %s + (%s) = %s$.'''
                     % (xC, xH, yC, yH, zC, zH, dx, dy, dz,
                        A_Q, B_Q, C_Q,
                        dy, C_Q, dz, B_Q, dz, A_Q, dx, C_Q, dx, B_Q, dy, A_Q,
                        nP_x, nP_y, nP_z,
                        xH, yH, zH,
                        nP_x, xH, nP_y, yH, nP_z, zH,
                        a_val, b_val, c_val, sign_d,
                        sign_d,
                        a_val, b_val, c_val,
                        a_val, b_val, c_val, sum_abc))
    list_vdc_2 = [loigiai_vdc_1]

    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Kiểm soát số lượng khẳng định đúng từ 1 đến 3
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

    # Xuất câu hỏi theo mẫu \choiceTFn
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

