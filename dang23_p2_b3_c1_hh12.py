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


def bt_dang23_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai điểm A, B sao cho O, A, B không thẳng hàng và tọa độ trung điểm I nguyên chẵn/lẻ rõ ràng
    while True:
        xa = random.randint(-4, 4)
        ya = random.choice([-4, -2, 2, 4])
        za = random.choice([-4, -2, 2, 4])
    
        xb = random.randint(-4, 4)
        yb = 0  # Chọn yB = 0 như bài gốc
        zb = random.choice([-4, -2, 2, 4])
    
        # Đảm bảo tổng tung độ chia hết cho 2 để trung điểm có tung độ nguyên
        if (ya + yb) % 2 != 0:
            continue
    
        # Đảm bảo tổng hoành độ chia hết cho 2 để M(a;b;c) có a, b, c nguyên đẹp
        if (xa + xb) % 2 != 0:
            continue
    
        # Tích có hướng [OA, OB] để tính diện tích tam giác OAB
        cp_x = ya * zb - za * yb
        cp_y = za * xb - xa * zb
        cp_z = xa * yb - ya * xb
    
        cp_sq = cp_x**2 + cp_y**2 + cp_z**2
    
        # AB^2
        ab_sq = (xb - xa) ** 2 + (yb - ya) ** 2 + (zb - za) ** 2
    
        if (
            cp_sq > 0
            and ab_sq > 0
            and (xa, ya, za) != (0, 0, 0)
            and (xb, yb, zb) != (0, 0, 0)
        ):
            break
    
    # 1. Tính độ dài đoạn thẳng AB = sqrt(ab_sq)
    # Chọn một giá trị so sánh dạng căn thức sqrt(comp_sq)
    comp_sq = ab_sq - random.choice([4, 6, 8])
    if comp_sq <= 0:
        comp_sq = ab_sq + 4
    
    str_comp_val = latex(sp.sqrt(comp_sq))
    is_ab_gt = ab_sq > comp_sq
    
    # 2. Trung điểm I của đoạn thẳng AB có tung độ y_I = (ya + yb) / 2
    yi_val = (ya + yb) // 2
    yi_val_s = yi_val + random.choice([-2, -1, 1, 2])
    
    # 3. Diện tích tam giác OAB: S_OAB = 1/2 * sqrt(cp_sq)
    s_oab_sym = Rational(1, 2) * sp.sqrt(cp_sq)
    # Chọn một mốc so sánh diện tích s_comp_sym
    comp_s_sq = cp_sq - random.choice([8, 12, 16])
    if comp_s_sq <= 0:
        comp_s_sq = cp_sq + 12
    
    s_comp_sym = Rational(1, 2) * sp.sqrt(comp_s_sq)
    str_s_comp = latex(s_comp_sym)
    is_s_oab_gt = cp_sq > comp_s_sq
    
    # 4. Tìm điểm M(a;b;c) thuộc (Oxy) để P = |MA + MB| đạt giá trị nhỏ nhất:
    # Gọi I là trung điểm của AB: I((xa+xb)/2; (ya+yb)/2; (za+zb)/2)
    # Ta có vecto MA + vecto MB = 2 * vecto MI => P = 2*MI
    # P nhỏ nhất khi MI nhỏ nhất <=> M là hình chiếu vuông góc của I lên (Oxy)
    # Do đó: a = x_I = (xa + xb)/2, b = y_I = (ya + yb)/2, c = 0
    a_m = (xa + xb) // 2
    b_m = (ya + yb) // 2
    c_m = 0
    sum_abc = a_m + b_m + c_m
    is_sum_odd = sum_abc % 2 != 0
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho điểm $A(%s;%s;%s)$ và $B(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: AB > comp_val
    if is_ab_gt:
        nb_da_1_d = "\\True $AB > %s$" % (str_comp_val)
        nb_da_1_s = "$AB < %s$" % (str_comp_val)
    else:
        nb_da_1_d = "\\True $AB < %s$" % (str_comp_val)
        nb_da_1_s = "$AB > %s$" % (str_comp_val)
    
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có độ dài đoạn thẳng $AB$ là: \\\\ $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{%s} = %s$. \\\\ Vì $%s %s %s$ nên $\\sqrt{%s} %s \\sqrt{%s} = %s$, suy ra mệnh đề là %s."""
        % (
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            ab_sq,
            latex(sp.sqrt(ab_sq)),
            ab_sq,
            ">" if is_ab_gt else "<",
            comp_sq,
            ab_sq,
            ">" if is_ab_gt else "<",
            comp_sq,
            str_comp_val,
            "đúng" if "\\True" in nb_da_1 else "sai",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Trung điểm đoạn thẳng AB có tung độ bằng yi_val
    th_da_1_d = "\\True Trung điểm đoạn thẳng $AB$ có tung độ bằng $%s$" % (yi_val)
    th_da_1_s = "Trung điểm đoạn thẳng $AB$ có tung độ bằng $%s$" % (yi_val_s)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Gọi $I$ là trung điểm của đoạn thẳng $AB$. Khi đó tung độ của điểm $I$ là: \\\\ $y_I = \\frac{y_A + y_B}{2} = \\frac{%s + (%s)}{2} = %s$. \\\\ Vậy trung điểm đoạn thẳng $AB$ có tung độ bằng $%s$."""
        % (ya, yb, yi_val, yi_val)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Diện tích tam giác S_OAB > str_s_comp
    if is_s_oab_gt:
        vd_da_1_d = "\\True $S_{OAB} > %s$" % (str_s_comp)
        vd_da_1_s = "$S_{OAB} < %s$" % (str_s_comp)
    else:
        vd_da_1_d = "\\True $S_{OAB} < %s$" % (str_s_comp)
        vd_da_1_s = "$S_{OAB} > %s$" % (str_s_comp)
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có $\\vec{OA} = (%s;%s;%s)$ và $\\vec{OB} = (%s;%s;%s)$. \\\\ Tích có hướng của hai vectơ: \\\\ $[\\vec{OA}, \\vec{OB}] = \\left( \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix} \\right) = (%s;%s;%s)$. \\\\ Diện tích tam giác $OAB$ là: \\\\ $S_{OAB} = \\frac{1}{2} \\left|[\\vec{OA}, \\vec{OB}]\\right| = \\frac{1}{2} \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\frac{\\sqrt{%s}}{2} = %s$. \\\\ So sánh với $%s = \\frac{\\sqrt{%s}}{2}$, vì $%s %s %s$ nên mệnh đề là %s."""
        % (
            xa,
            ya,
            za,
            xb,
            yb,
            zb,
            ya,
            za,
            yb,
            zb,
            za,
            xa,
            zb,
            xb,
            xa,
            ya,
            xb,
            yb,
            cp_x,
            cp_y,
            cp_z,
            cp_x,
            cp_y,
            cp_z,
            cp_sq,
            latex(s_oab_sym),
            str_s_comp,
            comp_s_sq,
            cp_sq,
            ">" if is_s_oab_gt else "<",
            comp_s_sq,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tồn tại điểm M(a;b;c) trên (Oxy) để P = |MA + MB| min thì a + b + c là một số tự nhiên lẻ
    if is_sum_odd:
        vdc_da_1_d = (
            "\\True Tồn tại điểm $M(a;b;c)$ trên mặt phẳng $(Oxy)$ thỏa mãn $P = \\left|\\vec{MA} + \\vec{MB}\\right|$ đạt giá trị nhỏ nhất thì $a + b + c$ có giá trị là một số tự nhiên lẻ"
        )
        vdc_da_1_s = (
            "Tồn tại điểm $M(a;b;c)$ trên mặt phẳng $(Oxy)$ thỏa mãn $P = \\left|\\vec{MA} + \\vec{MB}\\right|$ đạt giá trị nhỏ nhất thì $a + b + c$ có giá trị là một số tự nhiên chẵn"
        )
    else:
        vdc_da_1_d = (
            "\\True Tồn tại điểm $M(a;b;c)$ trên mặt phẳng $(Oxy)$ thỏa mãn $P = \\left|\\vec{MA} + \\vec{MB}\\right|$ đạt giá trị nhỏ nhất thì $a + b + c$ có giá trị là một số tự nhiên chẵn"
        )
        vdc_da_1_s = (
            "Tồn tại điểm $M(a;b;c)$ trên mặt phẳng $(Oxy)$ thỏa mãn $P = \\left|\\vec{MA} + \\vec{MB}\\right|$ đạt giá trị nhỏ nhất thì $a + b + c$ có giá trị là một số tự nhiên lẻ"
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    zi_val = (za + zb) // 2
    
    loigiai_vdc_1 = (
        """Gọi $I$ là trung điểm của đoạn thẳng $AB$, ta có: \\\\ $I\\left(\\frac{x_A + x_B}{2}; \\frac{y_A + y_B}{2}; \\frac{z_A + z_B}{2}\\right) \\Rightarrow I(%s;%s;%s)$. \\\\ Ta có $\\vec{MA} + \\vec{MB} = 2\\vec{MI}$, suy ra: \\\\ $P = \\left|\\vec{MA} + \\vec{MB}\\right| = \\left|2\\vec{MI}\\right| = 2 MI$. \\\\ Biểu thức $P$ đạt giá trị nhỏ nhất khi và chỉ khi đoạn thẳng $MI$ ngắn nhất, tức là $M$ là hình chiếu vuông góc của điểm $I$ lên mặt phẳng $(Oxy)$. \\\\ Do đó tọa độ của điểm $M$ là $M(%s;%s;0) \\Rightarrow a = %s, b = %s, c = 0$. \\\\ Khi đó: $a + b + c = %s + (%s) + 0 = %s$. \\\\ Vì $%s$ là một số %s nên mệnh đề là %s."""
        % (
            a_m,
            b_m,
            zi_val,
            a_m,
            b_m,
            a_m,
            b_m,
            a_m,
            b_m,
            sum_abc,
            sum_abc,
            "lẻ" if is_sum_odd else "chẵn",
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
    