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


def bt_dang32_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu bốn điểm A, B, C, D không đồng phẳng
    while True:
        xa = random.randint(-2, 3)
        ya = random.randint(-1, 2)
        za = random.randint(0, 3)
    
        xb = random.randint(1, 4)
        yb = random.randint(-3, 0)
        zb = random.randint(0, 3)
    
        xc = random.randint(-3, 1)
        yc = random.randint(-2, 1)
        zc = random.randint(2, 5)
    
        xd = random.randint(0, 3)
        yd = random.randint(1, 4)
        zd = random.randint(0, 3)
    
        # AB, AC
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        ac_sq = ac_x**2 + ac_y**2 + ac_z**2
    
        # DC = C - D
        dc_x = xc - xd
        dc_y = yc - yd
        dc_z = zc - zd
        dc_sq = dc_x**2 + dc_y**2 + dc_z**2
    
        # DA = A - D
        da_x = xa - xd
        da_y = ya - yd
        da_z = za - zd
    
        # H là hình chiếu của A lên đường thẳng DC
        # H = D + t * DC với t = (DA . DC) / |DC|^2
        dot_da_dc = da_x * dc_x + da_y * dc_y + da_z * dc_z
    
        # E để ABCE là hình bình hành: vecto AE = vecto BC => E = A + C - B
        xe = xa + xc - xb
        ye = ya + yc - yb
        ze = za + zc - zb
    
        de_sq = (xe - xd) ** 2 + (ye - yd) ** 2 + (ze - zd) ** 2
    
        # Điểm I thỏa mãn IA + 2IB + 3IC = 0 <=> I = (A + 2B + 3C) / 6
        sum_xi = xa + 2 * xb + 3 * xc
        sum_yi = ya + 2 * yb + 3 * yc
        sum_zi = za + 2 * zb + 3 * zc
    
        # G thuộc (Oxy) để |GA + 2GB + 3GC| min <=> G là hình chiếu của I lên (Oxy)
        # G = (xI; yI; 0)
        xi_val = Rational(sum_xi, 6)
        yi_val = Rational(sum_yi, 6)
    
        # cos(AGB): GA = A - G, GB = B - G
        ga_x = xa - xi_val
        ga_y = ya - yi_val
        ga_z = Rational(za, 1)
    
        gb_x = xb - xi_val
        gb_y = yb - yi_val
        gb_z = Rational(zb, 1)
    
        dot_ga_gb = ga_x * gb_x + ga_y * gb_y + ga_z * gb_z
    
        if (
            dc_sq > 0
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xd, yd, zd) != (xc, yc, zc)
            and dot_ga_gb != 0
        ):
            break
    
    # 1. So sánh AB và AC[cite: 21]
    is_ab_eq_ac = ab_sq == ac_sq
    str_len_ab = latex(sp.sqrt(ab_sq))
    str_len_ac = latex(sp.sqrt(ac_sq))
    
    # 2. Độ dài đoạn DE[cite: 21]
    de_sym = sp.sqrt(de_sq)
    str_de_true = latex(de_sym)
    # Đáp án sai cho DE
    str_de_false = (
        str(int(math.sqrt(de_sq)) + 1)
        if de_sym.is_integer
        else latex(sp.sqrt(de_sq + 4))
    )
    
    # 3. Tung độ y_H của điểm H[cite: 21]
    # t = dot_da_dc / dc_sq => yH = yD + t * dc_y
    t_val = Rational(dot_da_dc, dc_sq)
    yh_val = yd + t_val * dc_y
    is_yh_lt_1 = yh_val < 1
    str_yh = format_fraction_latex(yh_val.p, yh_val.q)
    
    # 4. Góc AGB là góc tù / nhọn[cite: 21]
    # dot_ga_gb < 0 <=> góc tù; dot_ga_gb > 0 <=> góc nhọn
    is_agb_obtuse = dot_ga_gb < 0
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian $Oxyz$ cho các điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s), D(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xd, yd, zd)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: AB = AC[cite: 21]
    if is_ab_eq_ac:
        nb_da_1_d = "\\True $AB = AC$"
        nb_da_1_s = "$AB \\neq AC$"
    else:
        nb_da_1_d = "\\True $AB \\neq AC$"
        nb_da_1_s = "$AB = AC$"
    
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s) \\Rightarrow AB = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s) \\Rightarrow AC = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s$. \\\\ Vì $%s %s %s$ nên khẳng định $AB = AC$ là %s."""
        % (
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            ab_x,
            ab_y,
            ab_z,
            ab_x,
            ab_y,
            ab_z,
            str_len_ab,
            xc,
            xa,
            yc,
            ya,
            zc,
            za,
            ac_x,
            ac_y,
            ac_z,
            ac_x,
            ac_y,
            ac_z,
            str_len_ac,
            str_len_ab,
            "=" if is_ab_eq_ac else "\\neq",
            str_len_ac,
            "đúng" if is_ab_eq_ac else "sai",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Điểm E thỏa mãn tứ giác ABCE là hình bình hành thì DE = ...[cite: 21]
    th_da_1_d = (
        "\\True Điểm $E$ trong không gian thỏa mãn tứ giác $ABCE$ là hình bình hành thì $DE = %s$"
        % (str_de_true)
    )
    th_da_1_s = (
        "Điểm $E$ trong không gian thỏa mãn tứ giác $ABCE$ là hình bình hành thì $DE = %s$"
        % (str_de_false)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Tứ giác $ABCE$ là hình bình hành khi và chỉ khi: \\\\ $\\vec{AE} = \\vec{BC} \\Leftrightarrow \\begin{cases} x_E - x_A = x_C - x_B \\\\ y_E - y_A = y_C - y_B \\\\ z_E - z_A = z_C - z_B \\end{cases} \\Leftrightarrow \\begin{cases} x_E = x_A + x_C - x_B = %s + (%s) - (%s) = %s \\\\ y_E = y_A + y_C - y_B = %s + (%s) - (%s) = %s \\\\ z_E = z_A + z_C - z_B = %s + (%s) - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $E$ là $E(%s;%s;%s)$. \\\\ Khi đó độ dài đoạn thẳng $DE$ là: \\\\ $DE = \\sqrt{(x_E - x_D)^2 + (y_E - y_D)^2 + (z_E - z_D)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{%s} = %s$."""
        % (
            xa,
            xc,
            xb,
            xe,
            ya,
            yc,
            yb,
            ye,
            za,
            zc,
            zb,
            ze,
            xe,
            ye,
            ze,
            xe,
            xd,
            ye,
            yd,
            ze,
            zd,
            de_sq,
            str_de_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Biết H là hình chiếu vuông góc của A trên DC, khi đó y_H < 1[cite: 21]
    if is_yh_lt_1:
        vd_da_1_d = (
            "\\True Biết $H$ là hình chiếu vuông góc của $A$ trên đường thẳng $DC$. Khi đó $y_H < 1$"
        )
        vd_da_1_s = (
            "Biết $H$ là hình chiếu vuông góc của $A$ trên đường thẳng $DC$. Khi đó $y_H > 1$"
        )
    else:
        vd_da_1_d = (
            "\\True Biết $H$ là hình chiếu vuông góc của $A$ trên đường thẳng $DC$. Khi đó $y_H > 1$"
        )
        vd_da_1_s = (
            "Biết $H$ là hình chiếu vuông góc của $A$ trên đường thẳng $DC$. Khi đó $y_H < 1$"
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    str_t = format_fraction_latex(t_val.p, t_val.q)
    
    loigiai_vd_1 = (
        """Ta có $\\vec{DC} = (x_C - x_D; y_C - y_D; z_C - z_D) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Đường thẳng $DC$ đi qua điểm $D(%s;%s;%s)$ và có vectơ chỉ phương $\\vec{DC} = (%s;%s;%s)$. \\\\ Điểm $H \\in DC$ nên tọa độ của điểm $H$ có dạng: \\\\ $H(%s + %st; %s + %st; %s + %st)$. \\\\ Khi đó: $\\vec{AH} = (x_H - x_A; y_H - y_A; z_H - z_A) = (%s + %st; %s + %st; %s + %st)$. \\\\ Vì $H$ là hình chiếu vuông góc của $A$ lên đường thẳng $DC$ nên $AH \\perp DC$: \\\\ $\\vec{AH} \\cdot \\vec{DC} = 0 \\Leftrightarrow (%s) \\cdot (%s + %st) + (%s) \\cdot (%s + %st) + (%s) \\cdot (%s + %st) = 0$ \\\\ $\\Leftrightarrow %st + (%s) = 0 \\Leftrightarrow t = %s$. \\\\ Thay giá trị của $t$ vào, ta được tung độ của điểm $H$ là: \\\\ $y_H = %s + (%s) \\cdot \\left(%s\\right) = %s$. \\\\ Vì $%s %s 1$ nên mệnh đề là %s."""
        % (
            xc,
            xd,
            yc,
            yd,
            zc,
            zd,
            dc_x,
            dc_y,
            dc_z,
            xd,
            yd,
            zd,
            dc_x,
            dc_y,
            dc_z,
            xd,
            dc_x,
            yd,
            dc_y,
            zd,
            dc_z,
            xd - xa,
            dc_x,
            yd - ya,
            dc_y,
            zd - za,
            dc_z,
            dc_x,
            xd - xa,
            dc_x,
            dc_y,
            yd - ya,
            dc_y,
            dc_z,
            zd - za,
            dc_z,
            dc_sq,
            -dot_da_dc,
            str_t,
            yd,
            dc_y,
            str_t,
            str_yh,
            str_yh,
            "<" if is_yh_lt_1 else ">",
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: G di động trên (Oxy), biểu thức |GA + 2GB + 3GC| min thì góc AGB là góc tù/nhọn[cite: 21]
    if is_agb_obtuse:
        vdc_da_1_d = (
            "\\True Cho điểm $G$ di động trên mặt phẳng $(Oxy)$. Khi biểu thức $M = \\left|\\vec{GA} + 2\\vec{GB} + 3\\vec{GC}\\right|$ đạt giá trị nhỏ nhất thì $\\widehat{AGB}$ là góc tù"
        )
        vdc_da_1_s = (
            "Cho điểm $G$ di động trên mặt phẳng $(Oxy)$. Khi biểu thức $M = \\left|\\vec{GA} + 2\\vec{GB} + 3\\vec{GC}\\right|$ đạt giá trị nhỏ nhất thì $\\widehat{AGB}$ là góc nhọn"
        )
    else:
        vdc_da_1_d = (
            "\\True Cho điểm $G$ di động trên mặt phẳng $(Oxy)$. Khi biểu thức $M = \\left|\\vec{GA} + 2\\vec{GB} + 3\\vec{GC}\\right|$ đạt giá trị nhỏ nhất thì $\\widehat{AGB}$ là góc nhọn"
        )
        vdc_da_1_s = (
            "Cho điểm $G$ di động trên mặt phẳng $(Oxy)$. Khi biểu thức $M = \\left|\\vec{GA} + 2\\vec{GB} + 3\\vec{GC}\\right|$ đạt giá trị nhỏ nhất thì $\\widehat{AGB}$ là góc tù"
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_xi = format_fraction_latex(sum_xi, 6)
    str_yi = format_fraction_latex(sum_yi, 6)
    str_zi = format_fraction_latex(sum_zi, 6)
    str_dot_ga_gb = format_fraction_latex(dot_ga_gb.p, dot_ga_gb.q)
    
    loigiai_vdc_1 = (
        """Gọi điểm $I$ là điểm thỏa mãn đẳng thức vectơ: \\\\ $\\vec{IA} + 2\\vec{IB} + 3\\vec{IC} = \\vec{0} \\Leftrightarrow \\vec{OI} = \\frac{\\vec{OA} + 2\\vec{OB} + 3\\vec{OC}}{6}$. \\\\ Tọa độ điểm $I$ là: \\\\ $\\begin{cases} x_I = \\frac{x_A + 2x_B + 3x_C}{6} = \\frac{%s + 2 \\cdot (%s) + 3 \\cdot (%s)}{6} = %s \\\\ y_I = \\frac{y_A + 2y_B + 3y_C}{6} = \\frac{%s + 2 \\cdot (%s) + 3 \\cdot (%s)}{6} = %s \\\\ z_I = \\frac{z_A + 2z_B + 3z_C}{6} = \\frac{%s + 2 \\cdot (%s) + 3 \\cdot (%s)}{6} = %s \\end{cases} \\Rightarrow I\\left(%s;%s;%s\\right)$. \\\\ Khi đó ta có: \\\\ $\\vec{GA} + 2\\vec{GB} + 3\\vec{GC} = (\\vec{GI} + \\vec{IA}) + 2(\\vec{GI} + \\vec{IB}) + 3(\\vec{GI} + \\vec{IC}) = 6\\vec{GI} + (\\vec{IA} + 2\\vec{IB} + 3\\vec{IC}) = 6\\vec{GI}$. \\\\ Suy ra: $M = \\left|\\vec{GA} + 2\\vec{GB} + 3\\vec{GC}\\right| = 6 GI$. \\\\ Do điểm $G$ thuộc mặt phẳng $(Oxy)$ nên $GI$ đạt giá trị nhỏ nhất khi và chỉ khi $G$ là hình chiếu vuông góc của điểm $I$ lên mặt phẳng $(Oxy)$. \\\\ Khi đó tọa độ của điểm $G$ là $G\\left(%s;%s;0\\right)$. \\\\ Tọa độ các vectơ: \\\\ $\\vec{GA} = \\left(%s;%s;%s\\right)$, $\\vec{GB} = \\left(%s;%s;%s\\right)$. \\\\ Tích vô hướng: \\\\ $\\vec{GA} \\cdot \\vec{GB} = \\left(%s\\right) \\cdot \\left(%s\\right) + \\left(%s\\right) \\cdot \\left(%s\\right) + (%s) \\cdot (%s) = %s$. \\\\ Vì tích vô hướng $\\vec{GA} \\cdot \\vec{GB} %s 0$ nên $\\cos\\widehat{AGB} %s 0$, do đó $\\widehat{AGB}$ là góc %s."""
        % (
            xa,
            xb,
            xc,
            str_xi,
            ya,
            yb,
            yc,
            str_yi,
            za,
            zb,
            zc,
            str_zi,
            str_xi,
            str_yi,
            str_zi,
            str_xi,
            str_yi,
            format_fraction_latex(ga_x.p, ga_x.q),
            format_fraction_latex(ga_y.p, ga_y.q),
            za,
            format_fraction_latex(gb_x.p, gb_x.q),
            format_fraction_latex(gb_y.p, gb_y.q),
            zb,
            format_fraction_latex(ga_x.p, ga_x.q),
            format_fraction_latex(gb_x.p, gb_x.q),
            format_fraction_latex(ga_y.p, ga_y.q),
            format_fraction_latex(gb_y.p, gb_y.q),
            za,
            zb,
            str_dot_ga_gb,
            "<" if is_agb_obtuse else ">",
            "<" if is_agb_obtuse else ">",
            "tù" if is_agb_obtuse else "nhọn",
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
    