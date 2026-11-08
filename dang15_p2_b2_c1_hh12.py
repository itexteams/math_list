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


def bt_dang15_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hình thang cân ABCD với hai đáy AB, CD
    # Để D có toạ độ nguyên đẹp, ta chọn vector AB = k_base * u, DC song song AB
    while True:
        # Chọn vector u tối giản cho phương của đáy
        ux = random.choice([-2, 2])
        uy = random.choice([-1, 1])
        uz = random.choice([-2, 2])
    
        # Vector AB = 2 * u (đảm bảo độ dài đẹp)
        ab_x = 2 * ux
        ab_y = 2 * uy
        ab_z = 2 * uz
    
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(-3, 3)
    
        xb = xa + ab_x
        yb = ya + ab_y
        zb = za + ab_z
    
        # Để ABCD là hình thang cân đáy AB, CD thì AD = BC <=> AD^2 = BC^2
        # CD cùng phương với AB => DC = k * AB (với k != 1 để không là hình bình hành, k > 0)
        # Chọn k = 2 (CD = 2 * AB) để đáy lớn gấp đôi đáy nhỏ, toạ độ luôn nguyên
        # C = B + v sao cho v không cùng phương AB
        vx = random.choice([-3, -2, 2, 3])
        vy = random.choice([-2, -1, 1, 2])
        vz = random.choice([-3, -2, 2, 3])
    
        # Kiểm tra [AB, v] != 0
        cp1 = ab_y * vz - ab_z * vy
        cp2 = ab_z * vx - ab_x * vz
        cp3 = ab_x * vy - ab_y * vx
        if cp1 == 0 and cp2 == 0 and cp3 == 0:
            continue
    
        xc = xb + vx
        yc = yb + vy
        zc = zb + vz
    
    
        len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        dot_ab_bc = ab_x * vx + ab_y * vy + ab_z * vz
    
        # Ta cần k là số hữu tỉ dương và khác 1, đẹp nhất là k nguyên (ví dụ k = 2 hoặc 3)
        if (2 * dot_ab_bc) % len_ab_sq != 0:
            continue
    
        k_val = 1 + (2 * dot_ab_bc) // len_ab_sq
        if k_val <= 0 or k_val == 1:
            continue
    
        # Tọa độ điểm D
        xd = xc - k_val * ab_x
        yd = yc - k_val * ab_y
        zd = zc - k_val * ab_z
    
        # Cao độ trọng tâm G của tam giác ABC
        # zG = (za + zb + zc) / 3
        sum_z = za + zb + zc
    
        break
    
    # 1. Vectơ AB = (ab_x; ab_y; ab_z)
    # 2. Cao độ trọng tâm G của tam giác ABC
    z_g_val = Rational(sum_z, 3)
    bound_zg = math.floor(float(z_g_val))
    
    # 3. Mối liên hệ toạ độ đỉnh D(a; b; c) theo a:
    # Vì CD cùng phương AB nên:
    # (a - xc)/ab_x = (b - yc)/ab_y = (c - zc)/ab_z = -k
    # b theo a: b = yc + (ab_y / ab_x) * (a - xc)
    # c theo a: c = zc + (ab_z / ab_x) * (a - xc)
    slope_ba = Rational(ab_y, ab_x)
    slope_ca = Rational(ab_z, ab_x)
    
    const_b = yc - slope_ba * xc
    const_c = zc - slope_ca * xc
    
    str_b_expr = latex(slope_ba * symbols("a") + const_b)
    str_c_expr = latex(slope_ca * symbols("a") + const_c)
    
    # 4. Giá trị biểu thức T = a - 2b + c tại đỉnh D(xd; yd; zd)
    t_ans = xd - 2 * yd + zd
    t_ans_s = t_ans + random.choice([-3, -2, 2, 3])
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hình thang cân $ABCD$ có các đáy lần lượt là $AB, CD$. Biết $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$ và $D(a;b;c)$ với $a, b, c \\in \\mathbb{R}$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Vectơ AB
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (-ab_x, -ab_y, -ab_z)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xb, xa, yb, ya, zb, za, ab_x, ab_y, ab_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Trọng tâm G của tam giác ABC có cao độ lớn hơn bound_zg
    th_da_1_d = (
        "\\True Trọng tâm $G$ của tam giác $ABC$ có cao độ lớn hơn $%s$"
        % (bound_zg)
    )
    th_da_1_s = (
        "Trọng tâm $G$ của tam giác $ABC$ có cao độ lớn hơn $%s$" % (bound_zg + 2)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    str_zg_val = format_fraction_latex(sum_z, 3)
    
    loigiai_th_1 = (
        """Cao độ trọng tâm $G$ của tam giác $ABC$ là: \\\\ $z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\approx %s > %s$."""
        % (
            za,
            zb,
            zc,
            str_zg_val,
            str(round(float(z_g_val), 2)).replace(".", ","),
            bound_zg,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Biểu diễn tọa độ đỉnh D theo a
    vd_da_1_d = "\\True Tọa độ đỉnh $D\\left(a; %s; %s\\right)$" % (
        str_b_expr,
        str_c_expr,
    )
    vd_da_1_s = "\\True Tọa độ đỉnh $D\\left(a; %s; %s\\right)$" % (
        str_c_expr,
        str_b_expr,
    )
    vd_da_1_s = "Tọa độ đỉnh $D\\left(a; %s; %s\\right)$" % (
        latex(slope_ba * symbols("a") + const_b + 1),
        str_c_expr,
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì tứ giác $ABCD$ là hình thang có hai đáy $AB$ và $CD$ nên đường thẳng $CD$ song song với đường thẳng $AB$. \\\\ Do đó vectơ $\\vec{CD}$ cùng phương với vectơ $\\vec{AB} = (%s;%s;%s)$. \\\\ Ta có $\\vec{CD} = (a - (%s); b - (%s); c - (%s)) = (a - (%s); b - (%s); c - (%s))$. \\\\ Vì $\\vec{CD}$ cùng phương với $\\vec{AB}$ nên ta có tỉ lệ: \\\\ $\\frac{a - (%s)}{%s} = \\frac{b - (%s)}{%s} = \\frac{c - (%s)}{%s} \\Leftrightarrow \\begin{cases} b = %s \\\\ c = %s \\end{cases}$ \\\\ Vậy tọa độ đỉnh $D$ có dạng $D\\left(a; %s; %s\\right)$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            xc,
            yc,
            zc,
            xc,
            yc,
            zc,
            xc,
            ab_x,
            yc,
            ab_y,
            zc,
            ab_z,
            str_b_expr,
            str_c_expr,
            str_b_expr,
            str_c_expr,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Giá trị biểu thức T = a - 2b + c bằng t_ans
    vdc_da_1_d = "\\True Giá trị biểu thức $T = a - 2b + c$ bằng $%s$" % (t_ans)
    vdc_da_1_s = "Giá trị biểu thức $T = a - 2b + c$ bằng $%s$" % (t_ans_s)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    len_bc_sq = vx**2 + vy**2 + vz**2
    
    loigiai_vdc_1 = (
        """Hình thang $ABCD$ cân với hai đáy $AB, CD$ nên hai cạnh bên bằng nhau: $AD = BC \\Leftrightarrow AD^2 = BC^2$. \\\\ Ta có: \\\\ $BC^2 = (%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2 = %s$. \\\\ $AD^2 = (a - (%s))^2 + (b - (%s))^2 + (c - (%s))^2$. \\\\ Thay tọa độ $D\\left(a; %s; %s\\right)$ vào phương trình $AD^2 = BC^2$, giải phương trình bậc hai theo $a$, ta loại nghiệm ứng với hình bình hành ($a = %s$), thu được $a = %s$. \\\\ Khi đó ta tìm được $b = %s$ và $c = %s$, tức là $D(%s;%s;%s)$. \\\\ Suy ra giá trị của biểu thức $T = a - 2b + c = (%s) - 2 \\cdot (%s) + (%s) = %s$."""
        % (
            xc,
            xb,
            yc,
            yb,
            zc,
            zb,
            len_bc_sq,
            xa,
            ya,
            za,
            str_b_expr,
            str_c_expr,
            xc - ab_x,
            xd,
            yd,
            zd,
            xd,
            yd,
            zd,
            xd,
            yd,
            zd,
            t_ans,
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
    