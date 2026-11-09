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


def bt_dang35_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu cho ba điểm A, B, C không thẳng hàng
    while True:
        xa = random.randint(-4, 4)
        ya = random.randint(-4, 4)
        za = random.randint(-4, 4)
    
        xb = random.randint(-4, 4)
        yb = random.randint(-4, 4)
        zb = random.randint(-4, 4)
    
        xc = random.randint(-4, 4)
        yc = random.randint(-4, 4)
        zc = random.randint(-4, 4)
    
        # Đảm bảo yB != yC để tìm được duy nhất điểm M trên Oy[cite: 21]
        if yb == yc:
            continue
    
        # Vectơ AB, AC
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        # Kiểm tra ba điểm A, B, C không thẳng hàng
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        # Kiểm tra hệ phương trình tìm N(x; y; 0) trên (Oxy) có nghiệm duy nhất[cite: 21]:
        # 2(xA - xB)x + 2(yA - yB)y = const1
        # 2(xB - xC)x + 2(yB - yC)y = const2
        det_n = 4 * ((xa - xb) * (yb - yc) - (ya - yb) * (xb - xc))
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and det_n != 0
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
        ):
            break
    
    # 1. Trung điểm của đoạn thẳng AB[cite: 21]
    xm_ab_num = xa + xb
    ym_ab_num = ya + yb
    zm_ab_num = za + zb
    
    str_xm_ab = format_fraction_latex(xm_ab_num, 2)
    str_ym_ab = format_fraction_latex(ym_ab_num, 2)
    str_zm_ab = format_fraction_latex(zm_ab_num, 2)
    
    str_zm_ab_s = format_fraction_latex(zm_ab_num + random.choice([-2, -1, 1, 2]), 2)
    
    # 2. Vectơ AB = (ab_x; ab_y; ab_z)[cite: 21]
    # Vectơ sai thường gặp (đổi dấu hoặc nhầm thành A - B)
    ab_x_s = -ab_x
    ab_y_s = ab_y
    ab_z_s = -ab_z
    
    # 3. Điểm M thuộc trục Oy cách đều B và C: M(0; y; 0)[cite: 21]
    # MB^2 = MC^2 <=> xb^2 + (y - yb)^2 + zb^2 = xc^2 + (y - yc)^2 + zc^2
    # <=> -2*yb*y + (xb^2 + yb^2 + zb^2) = -2*yc*y + (xc^2 + yc^2 + zc^2)
    # <=> 2*(yc - yb)*y = (xc^2 + yc^2 + zc^2) - (xb^2 + yb^2 + zb^2)
    diff_bc_sq = (xc**2 + yc**2 + zc**2) - (xb**2 + yb**2 + zb**2)
    ym_val = Rational(diff_bc_sq, 2 * (yc - yb))
    
    str_ym = format_fraction_latex(ym_val.p, ym_val.q)
    str_ym_s = format_fraction_latex(ym_val.p + random.choice([-2, -1, 1, 2]), ym_val.q)
    
    # 4. Điểm N thuộc mặt phẳng (Oxy) cách đều ba điểm A, B, C: N(xn; yn; 0)[cite: 21]
    # NA^2 = NB^2 <=> 2(xA - xB)x + 2(yA - yB)y = (xB^2 + yB^2 + zB^2) - (xA^2 + yA^2 + zA^2)
    # NB^2 = NC^2 <=> 2(xB - xC)x + 2(yB - yC)y = (xC^2 + yC^2 + zC^2) - (xB^2 + yB^2 + zB^2)
    eq1_c = (xb**2 + yb**2 + zb**2) - (xa**2 + ya**2 + za**2)
    eq2_c = (xc**2 + yc**2 + zc**2) - (xb**2 + yb**2 + zb**2)
    
    a11 = 2 * (xa - xb)
    a12 = 2 * (ya - yb)
    a21 = 2 * (xb - xc)
    a22 = 2 * (yb - yc)
    
    det_main = a11 * a22 - a12 * a21
    det_xn = (-eq1_c) * a22 - a12 * (-eq2_c)
    det_yn = a11 * (-eq2_c) - (-eq1_c) * a21
    
    xn_val = Rational(det_xn, det_main)
    yn_val = Rational(det_yn, det_main)
    
    str_xn = format_fraction_latex(xn_val.p, xn_val.q)
    str_yn = format_fraction_latex(yn_val.p, yn_val.q)
    
    # Tọa độ N sai (nhầm mẫu số giống câu hỏi gốc)[cite: 21]
    str_yn_s = (
        format_fraction_latex(yn_val.p, 2)
        if yn_val.q != 2
        else format_fraction_latex(yn_val.p + 1, 2)
    )
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Cho ba điểm $A(%s;%s;%s); B(%s;%s;%s)$ và $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ trung điểm của AB[cite: 21]
    nb_da_1_d = "\\True Tọa độ trung điểm của $AB$ là $M\\left(%s;%s;%s\\right)$" % (
        str_xm_ab,
        str_ym_ab,
        str_zm_ab,
    )
    nb_da_1_s = "Tọa độ trung điểm của $AB$ là $M\\left(%s;%s;%s\\right)$" % (
        str_xm_ab,
        str_ym_ab,
        str_zm_ab_s,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Gọi $M$ là trung điểm của đoạn thẳng $AB$. Khi đó tọa độ điểm $M$ thỏa mãn: \\\\ $\\begin{cases} x_M = \\frac{x_A + x_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ y_M = \\frac{y_A + y_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ z_M = \\frac{z_A + z_B}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases}$ \\\\ Vậy tọa độ trung điểm của đoạn thẳng $AB$ là $M\\left(%s;%s;%s\\right)$."""
        % (
            xa,
            xb,
            str_xm_ab,
            ya,
            yb,
            str_ym_ab,
            za,
            zb,
            str_zm_ab,
            str_xm_ab,
            str_ym_ab,
            str_zm_ab,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Tọa độ vectơ AB[cite: 21]
    nb_da_2_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    nb_da_2_s = "$\\vec{AB} = (%s;%s;%s)$" % (ab_x_s, ab_y_s, ab_z_s)
    list_th_da_1 = [nb_da_2_d, nb_da_2_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tọa độ của vectơ $\\vec{AB}$ là: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xb, xa, yb, ya, zb, za, ab_x, ab_y, ab_z)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Điểm M thuộc trục Oy cách đều hai điểm B, C[cite: 21]
    vd_da_1_d = (
        "\\True Điểm $M$ thuộc trục $Oy$ cách đều hai điểm $B, C$ có tọa độ là $M\\left(0;%s;0\\right)$"
        % (str_ym)
    )
    vd_da_1_s = (
        "Điểm $M$ thuộc trục $Oy$ cách đều hai điểm $B, C$ có tọa độ là $M\\left(0;%s;0\\right)$"
        % (str_ym_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    b_sq_sum = xb**2 + yb**2 + zb**2
    c_sq_sum = xc**2 + yc**2 + zc**2
    
    loigiai_vd_1 = (
        """Vì điểm $M$ thuộc trục $Oy$ nên tọa độ của điểm $M$ có dạng $M(0;y;0)$. \\\\ Ta có: \\\\ $MB^2 = (0 - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2 = y^2 - 2 \\cdot (%s)y + %s$. \\\\ $MC^2 = (0 - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2 = y^2 - 2 \\cdot (%s)y + %s$. \\\\ Điểm $M$ cách đều hai điểm $B$ và $C$ khi và chỉ khi: \\\\ $MB^2 = MC^2 \\Leftrightarrow -2 \\cdot (%s)y + %s = -2 \\cdot (%s)y + %s \\Leftrightarrow %sy = %s \\Leftrightarrow y = %s$. \\\\ Vậy tọa độ điểm $M$ là $M\\left(0;%s;0\\right)$."""
        % (
            xb,
            yb,
            zb,
            yb,
            b_sq_sum,
            xc,
            yc,
            zc,
            yc,
            c_sq_sum,
            yb,
            b_sq_sum,
            yc,
            c_sq_sum,
            2 * (yc - yb),
            diff_bc_sq,
            str_ym,
            str_ym,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm N thuộc mặt phẳng (Oxy) cách đều ba điểm A, B, C[cite: 21]
    vdc_da_1_d = (
        "\\True Điểm $N$ thuộc mặt phẳng $(Oxy)$ cách đều ba điểm $A, B, C$ có tọa độ $N\\left(%s;%s;0\\right)$"
        % (str_xn, str_yn)
    )
    vdc_da_1_s = (
        "Điểm $N$ thuộc mặt phẳng $(Oxy)$ cách đều ba điểm $A, B, C$ có tọa độ $N\\left(%s;%s;0\\right)$"
        % (str_xn, str_yn_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì điểm $N$ thuộc mặt phẳng tọa độ $(Oxy)$ nên tọa độ của điểm $N$ có dạng $N(x;y;0)$. \\\\ Điểm $N$ cách đều ba điểm $A, B, C$ khi và chỉ khi: \\\\ $\\begin{cases} NA^2 = NB^2 \\\\ NB^2 = NC^2 \\end{cases} \\Leftrightarrow \\begin{cases} (x - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2 = (x - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2 \\\\ (x - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2 = (x - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2 \\end{cases}$ \\\\ Thu gọn ta được hệ phương trình bậc nhất hai ẩn $x, y$: \\\\ $\\begin{cases} %sx + %sy = %s \\\\ %sx + %sy = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $N$ là $N\\left(%s;%s;0\\right)$."""
        % (
            xa,
            ya,
            za,
            xb,
            yb,
            zb,
            xb,
            yb,
            zb,
            xc,
            yc,
            zc,
            a11,
            a12,
            -eq1_c,
            a21,
            a22,
            -eq2_c,
            str_xn,
            str_yn,
            str_xn,
            str_yn,
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
    