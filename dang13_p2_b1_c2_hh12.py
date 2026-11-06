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


def bt_dang13_p2_b1_c2_hh12(self):
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
            if len(terms) == 0:
                terms.append("%s" % D_coef)
            else:
                if D_coef > 0:
                    terms.append("+ %s" % D_coef)
                else:
                    terms.append("- %s" % abs(D_coef))
        elif len(terms) == 0:
            terms.append("0")

        return " ".join(terms) + " = 0"

    # Random hệ số bài toán
    while True:
        # A(a_val; 0; 0), B(0; b_val; 0), C(0; 0; c_val) với a_val, b_val, c_val > 0
        # Trong bài mẫu: a_val = 2, b_val = 2, c_val = 3
        a_val = randint(2, 4)
        b_val = randint(2, 4)
        c_val = randint(2, 5)

        # Phương trình đoạn chắn: x/a + y/b + z/c = 1
        # BCNN của a_val, b_val, c_val
        lcm_ab = (a_val * b_val) // math.gcd(a_val, b_val)
        lcm_abc = (lcm_ab * c_val) // math.gcd(lcm_ab, c_val)

        # Vectơ pháp tuyến mặt phẳng (ABC): n_ABC = (A1, B1, C1)
        A1 = lcm_abc // a_val
        B1 = lcm_abc // b_val
        C1 = lcm_abc // c_val
        gcd_n = math.gcd(math.gcd(A1, B1), C1)
        A1 //= gcd_n
        B1 //= gcd_n
        C1 //= gcd_n

        # Ý b: Mặt phẳng (P) đi qua C(0; 0; c_val) và vuông góc với đường thẳng AB
        # AB = (-a_val, b_val, 0), chọn VTPT n = (k1, k2, 0)
        gcd_ab = math.gcd(a_val, b_val)
        n_b_x = -a_val // gcd_ab
        n_b_y = b_val // gcd_ab
        n_b_z = 0
        # Chuẩn hoá dấu để hệ số đầu tiên dương: ví dụ nếu n_b_x < 0 thì đổi dấu thành (a/gcd, -b/gcd, 0)
        if n_b_x < 0:
            n_b_x, n_b_y = -n_b_x, -n_b_y
        # mp qua C(0; 0; c_val): n_b_x*(x - 0) + n_b_y*(y - 0) + 0*(z - c_val) = 0
        D_b = 0
        str_plane_b_d = format_plane(n_b_x, n_b_y, n_b_z, D_b)
        str_plane_b_s = format_plane(n_b_x, n_b_y, n_b_z, D_b + 2)

        # Ý c: Mặt phẳng (beta) chứa AB và vuông góc với (ABC)
        # AB = (-a_val, b_val, 0), n_ABC = (A1, B1, C1)
        # n_beta = [AB, n_ABC] = (b_val*C1, a_val*C1, -a_val*B1 - b_val*A1)
        n_c_x = b_val * C1
        n_c_y = a_val * C1
        n_c_z = -a_val * B1 - b_val * A1
        gcd_beta = math.gcd(math.gcd(abs(n_c_x), abs(n_c_y)), abs(n_c_z))
        n_c_x //= gcd_beta
        n_c_y //= gcd_beta
        n_c_z //= gcd_beta
        if n_c_x < 0:
            n_c_x, n_c_y, n_c_z = -n_c_x, -n_c_y, -n_c_z
        # Đi qua A(a_val; 0; 0): n_c_x*(x - a_val) + n_c_y*y + n_c_z*z = 0
        D_c = -n_c_x * a_val
        str_plane_c_d = format_plane(n_c_x, n_c_y, n_c_z, D_c)
        # Tạo phương án sai như trong mẫu: đổi dấu hệ số D hoặc hệ số z
        str_plane_c_s = format_plane(n_c_x, n_c_y, n_c_z, -D_c if D_c != 0 else 2)

        # Ý d: M(a; b; c) thuộc (Oyz) => a = 0
        # |MA + MB + MC| = 3*|MG| nhỏ nhất <=> M là hình chiếu của trọng tâm G lên (Oyz)
        # G = ((a_val)/3; (b_val)/3; (c_val)/3)
        # => M(0; b_val/3; c_val/3) => a = 0, b = b_val/3, c = c_val/3
        # Khi đó 3(a + b) + c = 3*(0 + b_val/3) + c_val/3 = b_val + c_val/3 (nếu c_val chia hết cho 3 thì nguyên)
        # Để có biểu thức 3(a + b) + c là số nguyên đẹp:
        # 3*(a + b) + 3*c? Đề gốc: 3(a + b) + c = b_val + c_val/3 hoặc 3(a + b) + 3c.
        # Trong đề gốc: A(2;0;0), B(0;2;0), C(0;0;3) => G(2/3; 2/3; 1)
        # M thuộc (Oyz) => a = 0, b = 2/3, c = 1 => 3(a + b) + c = 3*(2/3) + 1 = 3.
        # Nhưng đề ghi = 5 là một mệnh đề sai!
        # Giá trị đúng của biểu thức K = 3*(0 + Rational(b_val, 3)) + Rational(c_val, 3) = b_val + Rational(c_val, 3)
        # Để K là số hữu tỉ hoặc số nguyên, nếu c_val chia hết cho 3 thì K là số nguyên
        if c_val % 3 != 0:
            continue
        K_val = b_val + c_val // 3
        break

    # Nội dung câu hỏi[cite: 5]
    noidungcauhoi = ('''Trong không gian $(Oxyz)$ cho $A(%s;0;0), B(0;%s;0), C(0;0;%s)$.''' % (a_val, b_val, c_val))

    ################################################################################
    # Ý a: Một vectơ pháp tuyến của (ABC)[cite: 5]
    nb_da_1_d = '\\True Một vectơ pháp tuyến của mặt phẳng $(ABC)$ là $\\vec{n} = (%s;%s;%s)$' % (A1, B1, C1)
    nb_da_1_s = 'Một vectơ pháp tuyến của mặt phẳng $(ABC)$ là $\\vec{n} = (%s;%s;%s)$' % (A1 + 1, B1, C1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Phương trình theo đoạn chắn của mặt phẳng $(ABC)$ là:\\\\
    $\\frac{x}{%s} + \\frac{y}{%s} + \\frac{z}{%s} = 1 \\Leftrightarrow %s x + %s y + %s z - %s = 0$.\\\\
    Do đó một vectơ pháp tuyến của mặt phẳng $(ABC)$ là $\\vec{n} = (%s; %s; %s)$.'''
                    % (a_val, b_val, c_val,
                       A1, B1, C1, lcm_abc // gcd_n,
                       A1, B1, C1))
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ################################################################################
    # Ý b: Mặt phẳng đi qua C và vuông góc với đường thẳng AB[cite: 5]
    vd_da_1_d = '\\True Mặt phẳng đi qua $C$ và vuông góc với đường thẳng $AB$ có phương trình là $%s$' % str_plane_b_d
    vd_da_1_s = 'Mặt phẳng đi qua $C$ và vuông góc với đường thẳng $AB$ có phương trình là $%s$' % str_plane_b_s
    list_th_da_1 = [vd_da_1_d, vd_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Ta có $\\vec{AB} = (%s; %s; 0)$, cùng phương với vectơ $\\vec{n} = (%s; %s; 0)$.\\\\
    Mặt phẳng đi qua $C(0; 0; %s)$ và vuông góc với đường thẳng $AB$ nhận $\\vec{n} = (%s; %s; 0)$ làm một vectơ pháp tuyến, có phương trình là:\\\\
    $%s(x - 0) + (%s)(y - 0) + 0(z - %s) = 0 \\Leftrightarrow %s$.'''
                    % (-a_val, b_val,
                       n_b_x, n_b_y,
                       c_val,
                       n_b_x, n_b_y,
                       n_b_x, n_b_y, c_val,
                       str_plane_b_d))
    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ################################################################################
    # Ý c: Mặt phẳng chứa đường thẳng AB và vuông góc với mp(ABC)[cite: 5]
    th_da_1_d = '\\True Mặt phẳng chứa đường thẳng $AB$ và vuông góc với mặt phẳng $(ABC)$ có phương trình là\\\\$%s$' % str_plane_c_d
    th_da_1_s = 'Mặt phẳng chứa đường thẳng $AB$ và vuông góc với mặt phẳng $(ABC)$ có phương trình là\\\\$%s$' % str_plane_c_s
    list_vd_da_1 = [th_da_1_d, th_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Mặt phẳng $(ABC)$ có vectơ pháp tuyến $\\vec{n}_{ABC} = (%s; %s; %s)$.\\\\
    Đường thẳng $AB$ có vectơ chỉ phương $\\vec{AB} = (%s; %s; 0)$.\\\\
    Mặt phẳng cần tìm chứa $AB$ và vuông góc với $(ABC)$ nên nhận một vectơ pháp tuyến là:\\\\
    $\\vec{n} = [\\vec{AB}, \\vec{n}_{ABC}] = (%s \\cdot %s - 0 \\cdot %s; 0 \\cdot %s - (%s) \\cdot %s; (%s) \\cdot %s - %s \\cdot %s) = (%s; %s; %s)$, cùng phương với $(%s; %s; %s)$.\\\\
    Mặt phẳng đi qua $A(%s; 0; 0)$ có phương trình là:\\\\
    $%s(x - %s) + %s(y - 0) + (%s)(z - 0) = 0 \\Leftrightarrow %s$.'''
                    % (A1, B1, C1,
                       -a_val, b_val,
                       b_val, C1, B1, A1, -a_val, C1, -a_val, B1, b_val, A1,
                       b_val * C1, a_val * C1, -a_val * B1 - b_val * A1,
                       n_c_x, n_c_y, n_c_z,
                       a_val,
                       n_c_x, a_val, n_c_y, n_c_z,
                       str_plane_c_d))
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ################################################################################
    # Ý d: Điểm M thuộc (Oyz) sao cho |MA + MB + MC| nhỏ nhất[cite: 5]
    b_M_num = b_val
    c_M = c_val // 3
    vdc_da_1_d = 'Gọi $M(a;b;c) \\in (Oyz)$ sao cho $|\\vec{MA} + \\vec{MB} + \\vec{MC}|$ nhỏ nhất. Khi đó $3(a+b)+c = %s$' % (K_val + 2)
    vdc_da_1_s = '\\True Gọi $M(a;b;c) \\in (Oyz)$ sao cho $|\\vec{MA} + \\vec{MB} + \\vec{MC}|$ nhỏ nhất. Khi đó $3(a+b)+c = %s$' % K_val
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Gọi $G$ là trọng tâm tam giác $ABC$, toạ độ điểm $G$ là:\\\\
    $G\\left(\\frac{%s + 0 + 0}{3}; \\frac{0 + %s + 0}{3}; \\frac{0 + 0 + %s}{3}\\right) \\Rightarrow G\\left(\\frac{%s}{3}; \\frac{%s}{3}; %s\\right)$.\\\\
    Ta có: $|\\vec{MA} + \\vec{MB} + \\vec{MC}| = |3\\vec{MG}| = 3MG$.\\\\
    Do đó $|\\vec{MA} + \\vec{MB} + \\vec{MC}|$ nhỏ nhất khi và chỉ khi $MG$ nhỏ nhất $\\Leftrightarrow M$ là hình chiếu vuông góc của $G$ lên mặt phẳng $(Oyz)$.\\\\
    Suy ra $M\\left(0; \\frac{%s}{3}; %s\\right)$, do đó $a = 0, b = \\frac{%s}{3}, c = %s$.\\\\
    Khi đó $3(a + b) + c = 3\\left(0 + \\frac{%s}{3}\\right) + %s = %s + %s = %s$.'''
                     % (a_val, b_val, c_val,
                        a_val, b_val, c_M,
                        b_val, c_M,
                        b_val, c_M,
                        b_val, c_M,
                        b_val, c_M, K_val))
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

    # Xuất câu hỏi trắc nghiệm Đúng/Sai
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

