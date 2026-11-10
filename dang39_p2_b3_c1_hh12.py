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


def bt_dang39_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai điểm A, B sao cho OA = OB (tam giác OAB cân tại O)
    while True:
        xa = random.randint(1, 4)
        ya = random.randint(2, 5)
        za = random.randint(3, 6)
    
        oa_sq = xa**2 + ya**2 + za**2
    
        # Chọn hoán vị hoặc đổi dấu để tạo điểm B thỏa mãn OB^2 = OA^2 nhưng B khác A
        coords = [xa, ya, za]
        random.shuffle(coords)
        signs = [random.choice([-1, 1]), random.choice([-1, 1]), random.choice([-1, 1])]
    
        xb = coords[0] * signs[0]
        yb = coords[1] * signs[1]
        zb = coords[2] * signs[2]
    
        ob_sq = xb**2 + yb**2 + zb**2
    
        # Đảm bảo A, B, O không thẳng hàng và A khác B
        ab_vec = (xb - xa, yb - ya, zb - za)
        ab_sq = ab_vec[0] ** 2 + ab_vec[1] ** 2 + ab_vec[2] ** 2
    
        # Tích có hướng [OA, OB] khác 0
        cp_x = ya * zb - za * yb
        cp_y = za * xb - xa * zb
        cp_z = xa * yb - ya * xb
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and oa_sq == ob_sq
        ):
            break
    
    # 1. Vectơ OA = (xa; ya; za)
    oa_x_s = xa + random.choice([-1, 1])
    oa_y_s = ya
    oa_z_s = za
    
    # 2. Khẳng định về điểm M trên đoạn thẳng AB thỏa mãn MA = 2MB:
    # Vì M thuộc đoạn thẳng AB nên chỉ có DUY NHẤT 1 điểm M thỏa mãn
    
    # 3. Tam giác OAB cân tại O (luôn đúng do OA = OB và O, A, B không thẳng hàng)
    
    # 4. Tìm M(x; y; 0) thuộc mặt phẳng (Oxy) với x - y = c_line sao cho MA^2 + MB^2 đạt GTNN
    # Gọi I là trung điểm của AB:
    xi_num = xa + xb
    yi_num = ya + yb
    zi_num = za + zb
    
    xi = Rational(xi_num, 2)
    yi = Rational(yi_num, 2)
    zi = Rational(zi_num, 2)
    
    # MA^2 + MB^2 = 2*MI^2 + AB^2 / 2
    # MA^2 + MB^2 nhỏ nhất <=> MI nhỏ nhất
    # Điểm M(x; y; 0) nằm trên đường thẳng d trong (Oxy): x - y = c_line <=> y = x - c_line
    # Ta chọn c_line nguyên đẹp (ví dụ -1, 0, 1)
    c_line = random.choice([-2, -1, 0, 1, 2])
    
    # Khoảng cách từ M(x; x - c_line; 0) đến I(xi; yi; zi):
    # MI^2 = (x - xi)^2 + (x - c_line - yi)^2 + zi^2
    # f(x) = 2x^2 - 2(xi + yi + c_line)x + xi^2 + (yi + c_line)^2 + zi^2
    # f'(x) = 4x - 2(xi + yi + c_line) = 0 <=> x_min = (xi + yi + c_line) / 2
    xm_opt = Rational(xi + yi + c_line, 2)
    ym_opt = xm_opt - c_line
    
    val_sum_sq = xm_opt**2 + ym_opt**2
    val_sum_sq_float = float(val_sum_sq)
    
    # Chọn mốc so sánh k_bound
    bound_sq = math.ceil(val_sum_sq_float) + random.choice([1, 2])
    is_sum_lt = val_sum_sq < bound_sq
    
    str_val_sum_sq = format_fraction_latex(val_sum_sq.p, val_sum_sq.q)
    str_xm_opt = format_fraction_latex(xm_opt.p, xm_opt.q)
    str_ym_opt = format_fraction_latex(ym_opt.p, ym_opt.q)
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$ cho các điểm $A(%s;%s;%s), B(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Vectơ OA
    nb_da_1_d = "\\True $\\vec{OA} = (%s;%s;%s)$" % (xa, ya, za)
    nb_da_1_s = "$\\vec{OA} = (%s;%s;%s)$" % (oa_x_s, oa_y_s, oa_z_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ của vectơ $\\vec{OA}$ chính là tọa độ của điểm $A$, do đó: \\\\ $\\vec{OA} = (x_A - 0; y_A - 0; z_A - 0) = (%s;%s;%s)$."""
        % (xa, ya, za)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Tồn tại điểm M thuộc đoạn thẳng AB thỏa mãn MA = 2MB
    th_da_1_d = (
        "\\True Tồn tại duy nhất một điểm $M$ thuộc đoạn thẳng $AB$ thỏa mãn $MA = 2MB$"
    )
    th_da_1_s = (
        "Tồn tại hai điểm $M$ thuộc đoạn thẳng $AB$ thỏa mãn $MA = 2MB$"
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì điểm $M$ thuộc đoạn thẳng $AB$ nên điểm $M$ nằm giữa hai điểm $A$ và $B$. \\\\ Khi đó hai vectơ $\\vec{MA}$ và $\\vec{MB}$ ngược hướng. \\\\ Do đó hệ thức $MA = 2MB$ tương đương với: \\\\ $\\vec{MA} = -2\\vec{MB} \\Leftrightarrow \\vec{OA} - \\vec{OM} = -2(\\vec{OB} - \\vec{OM}) \\Leftrightarrow 3\\vec{OM} = \\vec{OA} + 2\\vec{OB} \\Leftrightarrow \\vec{OM} = \\frac{\\vec{OA} + 2\\vec{OB}}{3}$. \\\\ Hệ thức này xác định duy nhất một điểm $M$ thuộc đoạn thẳng $AB$. \\\\ Khẳng định tồn tại hai điểm $M$ thuộc đoạn thẳng $AB$ là sai (chỉ có hai điểm nếu xét trên đường thẳng $AB$)."""
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Tam giác OAB cân tại O
    vd_da_1_d = "\\True Tam giác $OAB$ cân tại $O$"
    vd_da_1_s = "Tam giác $OAB$ là tam giác đều"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có độ dài các đoạn thẳng: \\\\ $OA = \\sqrt{x_A^2 + y_A^2 + z_A^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $OB = \\sqrt{x_B^2 + y_B^2 + z_B^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{%s}$. \\\\ Vì $OA = OB = \\sqrt{%s} \\neq AB$ và ba điểm $O, A, B$ không thẳng hàng nên tam giác $OAB$ là tam giác cân tại $O$."""
        % (
            xa,
            ya,
            za,
            oa_sq,
            xb,
            yb,
            zb,
            ob_sq,
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            ab_sq,
            oa_sq,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tồn tại M(x; y; 0) với x - y = c_line sao cho MA^2 + MB^2 min thì x^2 + y^2 < bound_sq
    str_sign_c = "- %s" % (abs(c_line)) if c_line < 0 else "+ %s" % (c_line) if c_line > 0 else ""
    str_line_eq = "x - y = %s" % (c_line)
    
    if is_sum_lt:
        vdc_da_1_d = (
            "\\True Tồn tại điểm $M(x;y;0)$ với $%s$ sao cho $MA^2 + MB^2$ đạt giá trị nhỏ nhất thì $x^2 + y^2 < %s$"
            % (str_line_eq, bound_sq)
        )
        vdc_da_1_s = (
            "Tồn tại điểm $M(x;y;0)$ với $%s$ sao cho $MA^2 + MB^2$ đạt giá trị nhỏ nhất thì $x^2 + y^2 > %s$"
            % (str_line_eq, bound_sq)
        )
    else:
        vdc_da_1_d = (
            "\\True Tồn tại điểm $M(x;y;0)$ với $%s$ sao cho $MA^2 + MB^2$ đạt giá trị nhỏ nhất thì $x^2 + y^2 > %s$"
            % (str_line_eq, bound_sq)
        )
        vdc_da_1_s = (
            "Tồn tại điểm $M(x;y;0)$ với $%s$ sao cho $MA^2 + MB^2$ đạt giá trị nhỏ nhất thì $x^2 + y^2 < %s$"
            % (str_line_eq, bound_sq)
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_xi = format_fraction_latex(xi_num, 2)
    str_yi = format_fraction_latex(yi_num, 2)
    str_zi = format_fraction_latex(zi_num, 2)
    
    loigiai_vdc_1 = (
        """Gọi $I$ là trung điểm của đoạn thẳng $AB$. Khi đó: \\\\ $\\begin{cases} x_I = \\frac{x_A + x_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ y_I = \\frac{y_A + y_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ z_I = \\frac{z_A + z_B}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases} \\Rightarrow I\\left(%s;%s;%s\\right)$. \\\\ Ta có hệ thức: \\\\ $MA^2 + MB^2 = (\\vec{MI} + \\vec{IA})^2 + (\\vec{MI} + \\vec{IB})^2 = 2MI^2 + 2\\vec{MI} \\cdot (\\vec{IA} + \\vec{IB}) + IA^2 + IB^2 = 2MI^2 + \\frac{AB^2}{2}$. \\\\ Do đó $MA^2 + MB^2$ đạt giá trị nhỏ nhất khi và chỉ khi $MI$ ngắn nhất, tức là $M$ là hình chiếu vuông góc của điểm $I$ lên đường thẳng $d: \\begin{cases} x - y = %s \\\\ z = 0 \\end{cases}$. \\\\ Điểm $M(x;y;0) \\in d \\Rightarrow y = x - (%s)$. \\\\ Ta có: \\\\ $MI^2 = (x - x_I)^2 + (y - y_I)^2 + z_I^2 = \\left(x - %s\\right)^2 + \\left(x - (%s) - %s\\right)^2 + \\left(%s\\right)^2$ \\\\ $= 2x^2 - 2\\left(%s + %s + (%s)\\right)x + C$. \\\\ Biểu thức bậc hai theo $x$ đạt giá trị nhỏ nhất tại hoành độ: \\\\ $x = \\frac{%s + %s + (%s)}{2} = %s \\Rightarrow y = %s - (%s) = %s$. \\\\ Suy ra tọa độ điểm $M$ là $M\\left(%s;%s;0\\right)$. \\\\ Khi đó: $x^2 + y^2 = \\left(%s\\right)^2 + \\left(%s\\right)^2 = %s \\approx %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            xa,
            xb,
            str_xi,
            ya,
            yb,
            str_yi,
            za,
            zb,
            str_zi,
            str_xi,
            str_yi,
            str_zi,
            c_line,
            c_line,
            str_xi,
            c_line,
            str_yi,
            str_zi,
            str_xi,
            str_yi,
            c_line,
            str_xi,
            str_yi,
            c_line,
            str_xm_opt,
            str_xm_opt,
            c_line,
            str_ym_opt,
            str_xm_opt,
            str_ym_opt,
            str_xm_opt,
            str_ym_opt,
            str_val_sum_sq,
            str(round(val_sum_sq_float, 2)).replace(".", ","),
            str(round(val_sum_sq_float, 2)).replace(".", ","),
            "<" if is_sum_lt else ">",
            bound_sq,
            "đúng" if "\\True" in vdc_da_1 else "sai",
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
        "\\end{ex}\n \\end{minipage}\n\n" )
    return content
    