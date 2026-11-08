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


def bt_dang16_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu tam giác ABC sao cho BC = 2*AB
    while True:
        xb = random.randint(-3, 3)
        yb = random.randint(-3, 3)
        zb = random.randint(-3, 3)
    
        # Vector BA có 3 thành phần độ lớn khác nhau đôi một
        mags = random.sample([1, 2, 3, 4], 3)
        signs_ba = [random.choice([-1, 1]) for _ in range(3)]
        ba_x = mags[0] * signs_ba[0]
        ba_y = mags[1] * signs_ba[1]
        ba_z = mags[2] * signs_ba[2]
    
        # Đỉnh A
        xa = xb + ba_x
        ya = yb + ba_y
        za = zb + ba_z
    
        # Vector BC có độ lớn gấp đôi BA: hoán vị các thành phần độ lớn nhân 2
        perm_mags = [mags[1], mags[2], mags[0]]
        signs_bc = [random.choice([-1, 1]) for _ in range(3)]
        bc_x = 2 * perm_mags[0] * signs_bc[0]
        bc_y = 2 * perm_mags[1] * signs_bc[1]
        bc_z = 2 * perm_mags[2] * signs_bc[2]
    
        # Đỉnh C sao cho xC != 0 (để khoảng cách đến Oyz khác 0)
        xc = xb + bc_x
        yc = yb + bc_y
        zc = zb + bc_z
    
        if xc == 0:
            continue
    
        # Kiểm tra BA và BC không cùng phương
        cp_x = ba_y * bc_z - ba_z * bc_y
        cp_y = ba_z * bc_x - ba_x * bc_z
        cp_z = ba_x * bc_y - ba_y * bc_x
    
        if cp_x != 0 or cp_y != 0 or cp_z != 0:
            break
    
    # 1. Độ dài đoạn AB = sqrt(ba_x^2 + ba_y^2 + ba_z^2)
    len_ab_sq = ba_x**2 + ba_y**2 + ba_z**2
    len_bc_sq = bc_x**2 + bc_y**2 + bc_z**2
    
    # Chuỗi căn thức AB
    str_ab = "\\sqrt{%s}" % len_ab_sq
    str_ab_s = "\\sqrt{%s}" % (len_ab_sq + random.choice([2, 4, -2]))
    
    # 2. Khoảng cách từ C(xc; yc; zc) đến mặt phẳng (Oyz): d(C, (Oyz)) = |xc|
    dist_c_oyz = abs(xc)
    dist_c_oyz_s = abs(xc) + random.choice([1, 2])
    
    # 3. Chân đường phân giác trong D của góc B:
    # BA / BC = 1/2 => DA / DC = 1/2 => vecto(DA) = -1/2 * vecto(DC)
    # => 2 * vecto(DA) + vecto(DC) = 0 => D = (2A + C) / 3
    da_num = 2 * xa + xc
    db_num = 2 * ya + yc
    dc_num = 2 * za + zc
    
    a_val = Rational(da_num, 3)
    b_val = Rational(db_num, 3)
    c_val = Rational(dc_num, 3)
    
    str_a = format_fraction_latex(da_num, 3)
    str_b = format_fraction_latex(db_num, 3)
    str_c = format_fraction_latex(dc_num, 3)
    
    # 4. Giá trị biểu thức P = a + b + 2c
    val_p = a_val + b_val + 2 * c_val
    is_p_int = val_p.q == 1
    val_p_int = val_p.p if is_p_int else 0
    p_is_prime_gt_7 = is_p_int and isprime(val_p_int) and val_p_int > 7
    
    if is_p_int:
        str_val_p = str(val_p_int)
    else:
        str_val_p = format_fraction_latex(val_p.p, val_p.q)
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho tam giác $ABC$ có $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$. Gọi $D(a;b;c)$ là chân đường phân giác trong góc $B$ của tam giác $ABC$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: AB = sqrt(len_ab_sq)
    nb_da_1_d = "\\True $AB = %s$" % (str_ab)
    nb_da_1_s = "$AB = %s$" % (str_ab_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có $\\vec{BA} = (x_A - x_B; y_A - y_B; z_A - z_B) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Độ dài đoạn thẳng $AB$ là: \\\\ $AB = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s$."""
        % (
            xa,
            xb,
            ya,
            yb,
            za,
            zb,
            ba_x,
            ba_y,
            ba_z,
            ba_x,
            ba_y,
            ba_z,
            str_ab,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Điểm C cách mặt phẳng (Oyz) một khoảng bằng |xc|
    th_da_1_d = (
        "\\True Điểm $C(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (xc, yc, zc, dist_c_oyz)
    )
    th_da_1_s = (
        "Điểm $C(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (xc, yc, zc, dist_c_oyz_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Mặt phẳng $(Oyz)$ có phương trình là $x = 0$. \\\\ Khoảng cách từ điểm $C(%s;%s;%s)$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(C, (Oyz)) = |x_C| = |%s| = %s$."""
        % (xc, yc, zc, xc, dist_c_oyz)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: vecto(DA) = -1/2 * vecto(DC) (*)
    vd_da_1_d = "\\True $\\vec{DA} = -\\frac{1}{2}\\vec{DC}$ (*)"
    vd_da_1_s = "$\\vec{DA} = \\frac{1}{2}\\vec{DC}$ (*)"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có $AB = \\sqrt{%s}$ và $\\vec{BC} = (%s;%s;%s) \\Rightarrow BC = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = 2\\sqrt{%s}$. \\\\ Do $D$ là chân đường phân giác trong góc $B$ của tam giác $ABC$ nên theo tính chất đường phân giác trong, ta có: \\\\ $\\frac{DA}{DC} = \\frac{BA}{BC} = \\frac{\\sqrt{%s}}{2\\sqrt{%s}} = \\frac{1}{2}$. \\\\ Vì $D$ nằm giữa hai điểm $A$ và $C$ nên hai vectơ $\\vec{DA}$ và $\\vec{DC}$ ngược hướng. \\\\ Do đó ta có hệ thức vectơ: $\\vec{DA} = -\\frac{1}{2}\\vec{DC}$ (*)."""
        % (
            len_ab_sq,
            bc_x,
            bc_y,
            bc_z,
            bc_x,
            bc_y,
            bc_z,
            len_bc_sq,
            len_ab_sq,
            len_ab_sq,
            len_ab_sq,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Giá trị của a + b + 2c là một số nguyên tố lớn hơn 7
    if p_is_prime_gt_7:
        vdc_da_1_d = "\\True Giá trị của $a + b + 2c$ là một số nguyên tố lớn hơn $7$"
        vdc_da_1_s = (
            "Giá trị của $a + b + 2c$ là một số hợp số chia hết cho $2$"
        )
    else:
        vdc_da_1_d = (
            "\\True Giá trị của $a + b + 2c$ không phải là số nguyên tố lớn hơn $7$"
        )
        vdc_da_1_s = "Giá trị của $a + b + 2c$ là một số nguyên tố lớn hơn $7$"
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Từ đẳng thức $\\vec{DA} = -\\frac{1}{2}\\vec{DC} \\Leftrightarrow 2\\vec{DA} + \\vec{DC} = \\vec{0}$, tọa độ điểm $D(a;b;c)$ thỏa mãn: \\\\ $\\begin{cases} a = \\frac{2x_A + x_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\\\ b = \\frac{2y_A + y_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\\\ c = \\frac{2z_A + z_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $D$ là $D\\left(%s; %s; %s\\right)$. \\\\ Khi đó giá trị của biểu thức $a + b + 2c$ là: \\\\ $a + b + 2c = %s + %s + 2 \\cdot (%s) = %s$."""
        % (
            xa,
            xc,
            str_a,
            ya,
            yc,
            str_b,
            za,
            zc,
            str_c,
            str_a,
            str_b,
            str_c,
            str_a,
            str_b,
            str_c,
            str_val_p,
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
    