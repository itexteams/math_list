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


def bt_dang10_p2_b1_c2_hh12(self):
    # Khai báo biến và tạo bài toán ngẫu nhiên
    while True:
        # Random tọa độ điểm A
        xA, yA, zA = randint(-3, 3), randint(-3, 3), randint(-3, 3)

        # Random tọa độ vectơ AB và AC sao cho không cùng phương
        u1, u2, u3 = randint(1, 4), randint(2, 6), randint(2, 6)
        v1, v2, v3 = randint(-3, 1), randint(4, 8), randint(5, 9)

        # Kiểm tra không cùng phương: tích có hướng khác (0, 0, 0)
        # n_ABC = AB x AC
        nx = u2 * v3 - u3 * v2
        ny = u3 * v1 - u1 * v3
        nz = u1 * v2 - u2 * v1
        if nx == 0 and ny == 0 and nz == 0:
            continue

        xB, yB, zB = xA + u1, yA + u2, zA + u3
        xC, yC, zC = xA + v1, yA + v2, zA + v3

        # Random vectơ CD sao cho CD không cùng phương với AB
        # n_p = AB x CD
        w1, w2, w3 = randint(0, 3), randint(-2, 2), randint(-4, 1)
        if w1 == 0 and w2 == 0 and w3 == 0:
            continue

        xD, yD, zD = xC + w1, yC + w2, zC + w3

        # Tích có hướng của AB và CD: n_p = AB x CD
        n_p_x = u2 * w3 - u3 * w2
        n_p_y = u3 * w1 - u1 * w3
        n_p_z = u1 * w2 - u2 * w1
        if n_p_x == 0 and n_p_y == 0 and n_p_z == 0:
            continue

        # Rút gọn vectơ pháp tuyến của mp chứa AB và // CD
        gcd_np = math.gcd(math.gcd(abs(n_p_x), abs(n_p_y)), abs(n_p_z))
        if gcd_np != 0:
            n_p_x //= gcd_np
            n_p_y //= gcd_np
            n_p_z //= gcd_np
        if n_p_x < 0 or (n_p_x == 0 and n_p_y < 0) or (n_p_x == 0 and n_p_y == 0 and n_p_z < 0):
            n_p_x, n_p_y, n_p_z = -n_p_x, -n_p_y, -n_p_z

        # mp(P) đi qua A: n_p_x*(x - xA) + n_p_y*(y - yA) + n_p_z*(z - zA) = 0
        # => n_p_x*x + n_p_y*y + n_p_z*z + D_p = 0
        D_p = -(n_p_x * xA + n_p_y * yA + n_p_z * zA)

        # Kiểm tra D không thuộc mặt phẳng (P) để AB // CD và mp chứa AB song song với CD thật sự
        if n_p_x * xD + n_p_y * yD + n_p_z * zD + D_p == 0:
            continue

        # Tích vô hướng AB . AC
        dot_AB_AC = u1 * v1 + u2 * v2 + u3 * v3

        # Mặt phẳng đi qua B vuông góc với AC nhận AC = (v1, v2, v3) làm VTPT
        # v1*(x - xB) + v2*(y - yB) + v3*(z - zB) = 0
        gcd_ac = math.gcd(math.gcd(abs(v1), abs(v2)), abs(v3))
        n_q_x, n_q_y, n_q_z = v1 // gcd_ac, v2 // gcd_ac, v3 // gcd_ac
        if n_q_x < 0 or (n_q_x == 0 and n_q_y < 0) or (n_q_x == 0 and n_q_y == 0 and n_q_z < 0):
            n_q_x, n_q_y, n_q_z = -n_q_x, -n_q_y, -n_q_z
        D_q = -(n_q_x * xB + n_q_y * yB + n_q_z * zB)

        break

    # Hàm phụ trợ biểu diễn phương trình mặt phẳng
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

    # Biểu diễn vectơ dạng i, j, k
    def format_vec_ijk(c1, c2, c3):
        res = []
        # c1 * i
        if c1 == 1:
            res.append("\\vec{i}")
        elif c1 == -1:
            res.append("-\\vec{i}")
        elif c1 != 0:
            res.append("%s\\vec{i}" % c1)

        # c2 * j
        if c2 != 0:
            if len(res) == 0:
                if c2 == 1:
                    res.append("\\vec{j}")
                elif c2 == -1:
                    res.append("-\\vec{j}")
                else:
                    res.append("%s\\vec{j}" % c2)
            else:
                if c2 == 1:
                    res.append("+ \\vec{j}")
                elif c2 == -1:
                    res.append("- \\vec{j}")
                elif c2 > 0:
                    res.append("+ %s\\vec{j}" % c2)
                else:
                    res.append("- %s\\vec{j}" % abs(c2))

        # c3 * k
        if c3 != 0:
            if len(res) == 0:
                if c3 == 1:
                    res.append("\\vec{k}")
                elif c3 == -1:
                    res.append("-\\vec{k}")
                else:
                    res.append("%s\\vec{k}" % c3)
            else:
                if c3 == 1:
                    res.append("+ \\vec{k}")
                elif c3 == -1:
                    res.append("- \\vec{k}")
                elif c3 > 0:
                    res.append("+ %s\\vec{k}" % c3)
                else:
                    res.append("- %s\\vec{k}" % abs(c3))
        return " ".join(res)

    str_vec_AB_ijk = format_vec_ijk(u1, u2, u3)
    str_vec_AB_ijk_wrong = format_vec_ijk(u1, u2 + 1, u3)

    str_plane_Q = format_plane(n_q_x, n_q_y, n_q_z, D_q)
    str_plane_Q_wrong = format_plane(n_q_x, n_q_y, n_q_z, D_q + 2)

    str_plane_P = format_plane(n_p_x, n_p_y, n_p_z, D_p)
    str_plane_P_wrong = format_plane(n_p_x, n_p_y, n_p_z, D_p + 3)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Trong không gian $Oxyz$, cho bốn điểm $A(%s;%s;%s); B(%s;%s;%s); C(%s;%s;%s); D(%s;%s;%s)$.''' 
                     % (xA, yA, zA, xB, yB, zB, xC, yC, zC, xD, yD, zD))

    ################################################################################
    # Ý a: Tọa độ vectơ AB
    nb_da_1_d = '\\True $\\vec{AB} = %s$' % str_vec_AB_ijk
    nb_da_1_s = '$\\vec{AB} = %s$' % str_vec_AB_ijk_wrong
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Ta có $\\vec{AB} = (%s - %s; %s - %s; %s - %s) = (%s; %s; %s) = %s$.'''
                    % (xB, xA, yB, yA, zB, zA, u1, u2, u3, str_vec_AB_ijk))
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ################################################################################
    # Ý b: Vuông góc giữa AB và AC
    if dot_AB_AC == 0:
        th_da_1_d = '\\True $\\vec{AB} \\perp \\vec{AC}$'
        th_da_1_s = '$\\vec{AB} // \\vec{AC}$'
    else:
        th_da_1_d = '$\\vec{AB} \\perp \\vec{AC}$'
        th_da_1_s = '\\True $\\vec{AB}$ không vuông góc với $\\vec{AC}$'

    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Ta có $\\vec{AB} = (%s; %s; %s)$ và $\\vec{AC} = (%s; %s; %s)$.\\\\
    Xét tích vô hướng: $\\vec{AB} \\cdot \\vec{AC} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s %s 0$.\\\\
    Do đó %s.'''
                    % (u1, u2, u3, v1, v2, v3,
                       u1, v1, u2, v2, u3, v3,
                       dot_AB_AC,
                       '=' if dot_AB_AC == 0 else '\\neq',
                       '$\\vec{AB} \\perp \\vec{AC}$' if dot_AB_AC == 0 else '$\\vec{AB}$ không vuông góc với $\\vec{AC}$'))
    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ################################################################################
    # Ý c: Mặt phẳng qua B và vuông góc với AC
    vd_da_1_d = '\\True Phương trình mặt phẳng đi qua điểm $B$ và vuông góc với $AC$ là $%s$' % str_plane_Q
    vd_da_1_s = 'Phương trình mặt phẳng đi qua điểm $B$ và vuông góc với $AC$ là $%s$' % str_plane_Q_wrong
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Mặt phẳng vuông góc với $AC$ nên nhận $\\vec{n} = (%s; %s; %s)$ làm một vectơ pháp tuyến.\\\\
    Mặt phẳng đi qua $B(%s; %s; %s)$ có phương trình:\\\\
    $%s(x - %s) + (%s)(y - %s) + (%s)(z - %s) = 0 \\Leftrightarrow %s$.'''
                    % (n_q_x, n_q_y, n_q_z,
                       xB, yB, zB,
                       n_q_x, xB, n_q_y, yB, n_q_z, zB,
                       str_plane_Q))
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ################################################################################
    # Ý d: Mặt phẳng chứa AB song song với CD
    vdc_da_1_d = '\\True Phương trình mặt phẳng chứa $AB$ song song với $CD$ là $%s$' % str_plane_P
    vdc_da_1_s = 'Phương trình mặt phẳng chứa $AB$ song song với $CD$ là $%s$' % str_plane_P_wrong
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Ta có $\\vec{AB} = (%s; %s; %s)$ và $\\vec{CD} = (%s; %s; %s)$.\\\\
    Vectơ pháp tuyến của mặt phẳng là $\\vec{n} = [\\vec{AB}, \\vec{CD}] = (%s; %s; %s)$, cùng phương với $(%s; %s; %s)$.\\\\
    Mặt phẳng đi qua $A(%s; %s; %s)$ có phương trình:\\\\
    $%s(x - %s) + (%s)(y - %s) + (%s)(z - %s) = 0 \\Leftrightarrow %s$.\\\\
    Thay toạ độ điểm $D(%s; %s; %s)$ vào phương trình mặt phẳng ta thấy không thoả mãn, do đó mặt phẳng song song với $CD$.'''
                     % (u1, u2, u3, w1, w2, w3,
                        u2 * w3 - u3 * w2, u3 * w1 - u1 * w3, u1 * w2 - u2 * w1,
                        n_p_x, n_p_y, n_p_z,
                        xA, yA, zA,
                        n_p_x, xA, n_p_y, yA, n_p_z, zA,
                        str_plane_P,
                        xD, yD, zD))
    list_vdc_2 = [loigiai_vdc_1]

    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Kiểm soát số lượng câu đúng
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
               '\\end{ex}\n \\end{minipage}\n\n').replace('--', '+').replace('- -', '+')
    return content

