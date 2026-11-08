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


def bt_dang23_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên tọa độ các điểm A, B, D'
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(1, 5)
    
        xb = random.randint(-3, 3)
        yb = random.randint(1, 4)
        zb = random.randint(1, 5)
    
        xd_p = random.randint(-3, 3)
        yd_p = random.choice([-4, -3, -2, 2, 3, 4])
        zd_p = random.randint(1, 5)
    
        # C' = B + D' - A trong hình hộp ABCD.A'B'C'D'
        xc_p = xb + xd_p - xa
        yc_p = yb + yd_p - ya
        zc_p = zb + zd_p - za
    
        # G là trọng tâm tam giác ABC': G = (A + B + C')/3 = (2B + D')/3
        xg_num = 2 * xb + xd_p
        yg_num = 2 * yb + yd_p
        zg_num = 2 * zb + zd_p
    
        # Vector AG = G - A = (2B + D' - 3A) / 3
        u_x = xg_num - 3 * xa
        u_y = yg_num - 3 * ya
        u_z = zg_num - 3 * za
    
        # Giá trị T = -u_x * a - u_y * b - u_z * c = - (u_x * xG + u_y * yG + u_z * zG)
        # u . (D - G) = 0 <=> u . D = u . G
        # Biểu thức T_val = - (u_x * xg_num + u_y * yg_num + u_z * zg_num) / 3
        val_num = -(u_x * xg_num + u_y * yg_num + u_z * zg_num)
        if val_num % 3 == 0 and u_x != 0 and u_y != 0 and u_z != 0:
            t_val = val_num // 3
            break
    
    # 1. Khoảng cách từ D'(xd_p; yd_p; zd_p) đến mặt phẳng (Oxz): d(D', (Oxz)) = |yd_p|[cite: 19]
    dist_dp_oxz = abs(yd_p)
    dist_dp_oxz_s = dist_dp_oxz + random.choice([1, 2])
    
    # 2. Cao độ của C'[cite: 19]
    zc_p_true = zc_p
    zc_p_false = zc_p + random.choice([-2, -1, 1, 2])
    
    # 3. Tọa độ vectơ AG[cite: 19]
    str_ag_x = format_fraction_latex(u_x, 3)
    str_ag_y = format_fraction_latex(u_y, 3)
    str_ag_z = format_fraction_latex(u_z, 3)
    
    str_ag_x_s = format_fraction_latex(u_x + random.choice([-2, 2]), 3)
    
    # 4. Tam giác AGD vuông tại G <=> AG . GD = 0[cite: 19]
    # Hệ số của a, b, c trong biểu thức: c_a = -u_x, c_b = -u_y, c_c = -u_z
    c_a = -u_x
    c_b = -u_y
    c_c = -u_z
    
    # Xây dựng chuỗi biểu thức T = c_a*a + c_b*b + c_c*c
    terms = []
    if c_a == 1:
        terms.append("a")
    elif c_a == -1:
        terms.append("-a")
    else:
        terms.append("%sa" % c_a)
    
    if c_b == 1:
        terms.append("+ b")
    elif c_b == -1:
        terms.append("- b")
    elif c_b > 0:
        terms.append("+ %sb" % c_b)
    else:
        terms.append("- %sb" % (-c_b))
    
    if c_c == 1:
        terms.append("+ c")
    elif c_c == -1:
        terms.append("- c")
    elif c_c > 0:
        terms.append("+ %sc" % c_c)
    else:
        terms.append("- %sc" % (-c_c))
    
    expr_str = " ".join(terms)
    
    # Chọn mốc so sánh
    bound_comp = t_val + 2
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho hình hộp $ABCD.A'B'C'D'$ biết $A(%s;%s;%s); B(%s;%s;%s); D'(%s;%s;%s); D(a;b;c)$. Gọi $G$ là trọng tâm tam giác $ABC'$, biết rằng tam giác $AGD$ là tam giác vuông tại $G$."""
        % (xa, ya, za, xb, yb, zb, xd_p, yd_p, zd_p)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm D' cách mặt phẳng (Oxz) một khoảng bằng dist_dp_oxz[cite: 19]
    nb_da_1_d = (
        "\\True Điểm $D'(%s;%s;%s)$ cách mặt phẳng $(Oxz)$ một khoảng bằng $%s$"
        % (xd_p, yd_p, zd_p, dist_dp_oxz)
    )
    nb_da_1_s = (
        "Điểm $D'(%s;%s;%s)$ cách mặt phẳng $(Oxz)$ một khoảng bằng $%s$"
        % (xd_p, yd_p, zd_p, dist_dp_oxz_s)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng $(Oxz)$ có phương trình là $y = 0$. \\\\ Khoảng cách từ điểm $D'(%s;%s;%s)$ đến mặt phẳng $(Oxz)$ là: \\\\ $d(D', (Oxz)) = |y_{D'}| = |%s| = %s$."""
        % (xd_p, yd_p, zd_p, yd_p, dist_dp_oxz)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Điểm C' có cao độ bằng zc_p[cite: 19]
    th_da_1_d = "\\True Điểm $C'$ có cao độ bằng $%s$" % (zc_p_true)
    th_da_1_s = "Điểm $C'$ có cao độ bằng $%s$" % (zc_p_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Theo quy tắc hình hộp ta có: \\\\ $\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AB} + \\vec{AD} + \\vec{DD'}$. \\\\ Mặt khác $\\vec{AD} + \\vec{DD'} = \\vec{AD'}$, do đó: \\\\ $\\vec{AC'} = \\vec{AB} + \\vec{AD'} \\Leftrightarrow C' - A = (B - A) + (D' - A) \\Leftrightarrow C' = B + D' - A$. \\\\ Suy ra tọa độ điểm $C'$ là: \\\\ $\\begin{cases} x_{C'} = x_B + x_{D'} - x_A = %s + (%s) - (%s) = %s \\\\ y_{C'} = y_B + y_{D'} - y_A = %s + (%s) - (%s) = %s \\\\ z_{C'} = z_B + z_{D'} - z_A = %s + (%s) - (%s) = %s \\end{cases} \\Rightarrow C'(%s;%s;%s)$. \\\\ Vậy điểm $C'$ có cao độ bằng $%s$."""
        % (
            xb,
            xd_p,
            xa,
            xc_p,
            yb,
            yd_p,
            ya,
            yc_p,
            zb,
            zd_p,
            za,
            zc_p,
            xc_p,
            yc_p,
            zc_p,
            zc_p_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Vectơ AG[cite: 19]
    vd_da_1_d = "\\True $\\vec{AG} = \\left(%s;%s;%s\\right)$" % (
        str_ag_x,
        str_ag_y,
        str_ag_z,
    )
    vd_da_1_s = "$\\vec{AG} = \\left(%s;%s;%s\\right)$" % (
        str_ag_x_s,
        str_ag_y,
        str_ag_z,
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    str_xg = format_fraction_latex(xg_num, 3)
    str_yg = format_fraction_latex(yg_num, 3)
    str_zg = format_fraction_latex(zg_num, 3)
    
    loigiai_vd_1 = (
        """Vì $G$ là trọng tâm tam giác $ABC'$ nên tọa độ điểm $G$ là: \\\\ $\\begin{cases} x_G = \\frac{x_A + x_B + x_{C'}}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ y_G = \\frac{y_A + y_B + y_{C'}}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ z_G = \\frac{z_A + z_B + z_{C'}}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\end{cases} \\Rightarrow G\\left(%s;%s;%s\\right)$. \\\\ Khi đó tọa độ vectơ $\\vec{AG}$ là: \\\\ $\\vec{AG} = (x_G - x_A; y_G - y_A; z_G - z_A) = \\left(%s - (%s); %s - (%s); %s - (%s)\\right) = \\left(%s;%s;%s\\right)$."""
        % (
            xa,
            xb,
            xc_p,
            str_xg,
            ya,
            yb,
            yc_p,
            str_yg,
            za,
            zb,
            zc_p,
            str_zg,
            str_xg,
            str_yg,
            str_zg,
            str_xg,
            xa,
            str_yg,
            ya,
            str_zg,
            za,
            str_ag_x,
            str_ag_y,
            str_ag_z,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Giá trị của biểu thức expr_str là một số lớn hơn bound_comp[cite: 19]
    # Vì t_val < bound_comp = t_val + 2 nên mệnh đề khẳng định "lớn hơn bound_comp" là SAI[cite: 19]
    vdc_da_1_d = (
        "\\True Giá trị của biểu thức $%s$ bằng $%s$, là một số nhỏ hơn $%s$"
        % (expr_str, t_val, bound_comp)
    )
    vdc_da_1_s = "Giá trị của biểu thức $%s$ là một số lớn hơn $%s$" % (
        expr_str,
        bound_comp,
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có $\\vec{AG} = \\frac{1}{3}(%s; %s; %s)$ và tọa độ điểm $D(a;b;c)$. \\\\ Vectơ $\\vec{GD} = (a - x_G; b - y_G; c - z_G) = \\left(a - %s; b - %s; c - %s\\right)$. \\\\ Tam giác $AGD$ vuông tại $G$ khi và chỉ khi: \\\\ $\\vec{AG} \\cdot \\vec{GD} = 0 \\Leftrightarrow (%s)\\left(a - %s\\right) + (%s)\\left(b - %s\\right) + (%s)\\left(c - %s\\right) = 0$ \\\\ $\\Leftrightarrow %s a + %s b + %s c - \\left[(%s) \\cdot %s + (%s) \\cdot %s + (%s) \\cdot %s\\right] = 0$ \\\\ $\\Leftrightarrow %s = %s$. \\\\ Vì $%s < %s$ nên giá trị của biểu thức không lớn hơn $%s$."""
        % (
            u_x,
            u_y,
            u_z,
            str_xg,
            str_yg,
            str_zg,
            u_x,
            str_xg,
            u_y,
            str_yg,
            u_z,
            str_zg,
            u_x,
            u_y,
            u_z,
            u_x,
            str_xg,
            u_y,
            str_yg,
            u_z,
            str_zg,
            expr_str,
            t_val,
            t_val,
            bound_comp,
            bound_comp,
        )
    )
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    
    def count_true_answers(answers):
        return sum("\\True" in ans for ans in answers)
    
    
    # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
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
    content = (
        "\\begin{minipage}{\\textwidth} \n"
        "\\begin{ex}\n"
        + str(noidungcauhoi)
        + "\n"
        "\\choiceTFn \n"
        "{" + str(shuffled_answers_nb[0]) + "}\n"
        "{" + str(shuffled_answers_th[0]) + "}\n"
        "{" + str(shuffled_answers_vd[0]) + "}\n"
        "{" + str(shuffled_answers_vdc[0]) + "}\n"
        "\\loigiai{ \n"
        "\\begin{enumEX}[a)]{1} \n"
        "\\item " + str(shuffled_solutions_nb[0]) + "\n"
        "\\item " + str(shuffled_solutions_th[0]) + "\n"
        "\\item " + str(shuffled_solutions_vd[0]) + "\n"
        "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
        "\\end{enumEX}} \n"
        "\\end{ex}\n \\end{minipage}\n\n")
    return content
    