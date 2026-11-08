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


def bt_dang9_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên tọa độ ba điểm A, B, C không thẳng hàng
    while True:
        xa, ya, za = (
            random.randint(-4, 4),
            random.randint(-4, 4),
            random.randint(-4, 4),
        )
        xb, yb, zb = (
            random.randint(-4, 4),
            random.randint(-4, 4),
            random.randint(-4, 4),
        )
        xc, yc, zc = (
            random.randint(-4, 4),
            random.randint(-4, 4),
            random.randint(-4, 4),
        )
    
        # Tọa độ các vectơ AB, AC
        u1, u2, u3 = xb - xa, yb - ya, zb - za
        v1, v2, v3 = xc - xa, yc - ya, zc - za
    
        # Tích có hướng [AB, AC] để kiểm tra ba điểm không thẳng hàng
        cp_x = u2 * v3 - u3 * v2
        cp_y = u3 * v1 - u1 * v3
        cp_z = u1 * v2 - u2 * v1
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # 1. Trung điểm M của đoạn thẳng AB: M = (A + B) / 2
    str_xm = format_fraction_latex(xa + xb, 2)
    str_ym = format_fraction_latex(ya + yb, 2)
    str_zm = format_fraction_latex(za + zb, 2)
    
    # Tọa độ sai của M (nhầm sang A - B hoặc hoán vị)
    str_xm_s = format_fraction_latex(xa - xb, 2)
    str_ym_s = format_fraction_latex(ya - yb, 2)
    str_zm_s = format_fraction_latex(za - zb, 2)
    
    # 2. C là trung điểm của BE => E = 2C - B
    xe = 2 * xc - xb
    ye = 2 * yc - yb
    ze = 2 * zc - zb
    
    # Tọa độ sai của E (nhầm sang E = 2B - C hoặc sai dấu)
    xe_s = 2 * xb - xc
    ye_s = 2 * yb - yc
    ze_s = 2 * zb - zc
    
    # 3. N là trung điểm của đoạn thẳng BC => N = (B + C) / 2
    # Độ dài đường trung tuyến AN:
    # AN^2 = (xN - xA)^2 + (yN - yA)^2 + (zN - zA)^2 = ((xB + xC - 2xA)/2)^2 + ...
    num_x_an = xb + xc - 2 * xa
    num_y_an = yb + yc - 2 * ya
    num_z_an = zb + zc - 2 * za
    val_inside_sqrt = num_x_an**2 + num_y_an**2 + num_z_an**2
    
    str_an = "\\frac{\\sqrt{%s}}{2}" % val_inside_sqrt
    str_an_s = "\\frac{\\sqrt{%s}}{2}" % (val_inside_sqrt + random.choice([3, 5, 7]))
    
    # 4. Tâm I(m; n; p) của hình bình hành ABCD là trung điểm của đường chéo AC:
    # I = (A + C) / 2
    # m^2 + n^2 + p^2 = ((xA + xC)/2)^2 + ((yA + yC)/2)^2 + ((zA + zC)/2)^2
    num_i_sq = (xa + xc) ** 2 + (ya + yc) ** 2 + (za + zc) ** 2
    str_t_val = format_fraction_latex(num_i_sq, 4)
    str_t_val_s = format_fraction_latex(num_i_sq + random.choice([2, 4, 6]), 4)
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho tam giác $ABC$ biết $A(%s;%s;%s)$, $B(%s;%s;%s)$ và $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Phát biểu a: Tọa độ trung điểm M của đoạn AB
    nb_da_1_d = "\\True Tọa độ trung điểm $M$ của đoạn $AB$ là $M(%s;%s;%s)$" % (
        str_xm,
        str_ym,
        str_zm,
    )
    nb_da_1_s = "Tọa độ trung điểm $M$ của đoạn $AB$ là $M(%s;%s;%s)$" % (
        str_xm_s,
        str_ym_s,
        str_zm_s,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ trung điểm $M$ của đoạn thẳng $AB$ là: \\\\ $\\begin{cases} x_M = \\frac{x_A + x_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ y_M = \\frac{y_A + y_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ z_M = \\frac{z_A + z_B}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases} \\Rightarrow M(%s;%s;%s)$."""
        % (
            xa,
            xb,
            str_xm,
            ya,
            yb,
            str_ym,
            za,
            zb,
            str_zm,
            str_xm,
            str_ym,
            str_zm,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Phát biểu b: Gọi C là trung điểm của đoạn BE. Tọa độ điểm E
    th_da_1_d = (
        "\\True Gọi $C$ là trung điểm của đoạn $BE$. Toạ độ của điểm $E$ là $E(%s;%s;%s)$"
        % (xe, ye, ze)
    )
    th_da_1_s = (
        "Gọi $C$ là trung điểm của đoạn $BE$. Toạ độ của điểm $E$ là $E(%s;%s;%s)$"
        % (xe_s, ye_s, ze_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $C$ là trung điểm của đoạn thẳng $BE$ nên ta có: \\\\ $\\begin{cases} x_C = \\frac{x_B + x_E}{2} \\\\ y_C = \\frac{y_B + y_E}{2} \\\\ z_C = \\frac{z_B + z_E}{2} \\end{cases} \\Leftrightarrow \\begin{cases} x_E = 2x_C - x_B = 2 \\cdot (%s) - (%s) = %s \\\\ y_E = 2y_C - y_B = 2 \\cdot (%s) - (%s) = %s \\\\ z_E = 2z_C - z_B = 2 \\cdot (%s) - (%s) = %s \\end{cases}$ \\\\ Vậy $E(%s;%s;%s)$."""
        % (xc, xb, xe, yc, yb, ye, zc, zb, ze, xe, ye, ze)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Phát biểu c: Độ dài đường trung tuyến AN
    str_xn = format_fraction_latex(xb + xc, 2)
    str_yn = format_fraction_latex(yb + yc, 2)
    str_zn = format_fraction_latex(zb + zc, 2)
    
    vd_da_1_d = (
        "\\True Gọi $N$ là trung điểm của đoạn thẳng $BC$. Độ dài đường trung tuyến $AN = %s$"
        % (str_an)
    )
    vd_da_1_s = (
        "Gọi $N$ là trung điểm của đoạn thẳng $BC$. Độ dài đường trung tuyến $AN = %s$"
        % (str_an_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Tọa độ trung điểm $N$ của đoạn thẳng $BC$ là: \\\\ $x_N = \\frac{x_B + x_C}{2} = \\frac{%s + (%s)}{2} = %s$. \\\\ $y_N = \\frac{y_B + y_C}{2} = \\frac{%s + (%s)}{2} = %s$. \\\\ $z_N = \\frac{z_B + z_C}{2} = \\frac{%s + (%s)}{2} = %s$. \\\\ $\\Rightarrow N\\left(%s;%s;%s\\right)$. \\\\ Độ dài đoạn thẳng $AN$ là: \\\\ $AN = \\sqrt{(x_N - x_A)^2 + (y_N - y_A)^2 + (z_N - z_A)^2} \\\\= \\sqrt{\\left(%s - (%s)\\right)^2 + \\left(%s - (%s)\\right)^2 + \\left(%s - (%s)\\right)^2} \\\\= %s$."""
        % (
            xb,
            xc,
            str_xn,
            yb,
            yc,
            str_yn,
            zb,
            zc,
            str_zn,
            str_xn,
            str_yn,
            str_zn,
            str_xn,
            xa,
            str_yn,
            ya,
            str_zn,
            za,
            str_an,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Phát biểu d: Gọi I(m; n; p) là tâm của hình bình hành ABCD. Giá trị của biểu thức m^2 + n^2 + p^2 = ...
    vdc_da_1_d = (
        "\\True Gọi $I(m;n;p)$ là tâm của hình bình hành $ABCD$. Giá trị của biểu thức $m^2 + n^2 + p^2 = %s$"
        % (str_t_val)
    )
    vdc_da_1_s = (
        "Gọi $I(m;n;p)$ là tâm của hình bình hành $ABCD$. Giá trị của biểu thức $m^2 + n^2 + p^2 = %s$"
        % (str_t_val_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_m = format_fraction_latex(xa + xc, 2)
    str_n = format_fraction_latex(ya + yc, 2)
    str_p = format_fraction_latex(za + zc, 2)
    
    loigiai_vdc_1 = (
        """Vì $ABCD$ là hình bình hành nên tâm $I$ của hình bình hành chính là trung điểm của đường chéo $AC$. \\\\ Do đó tọa độ điểm $I(m;n;p)$ là: \\\\ $\\begin{cases} m = \\frac{x_A + x_C}{2} = \\frac{%s + (%s)}{2} = %s \\\\ n = \\frac{y_A + y_C}{2} = \\frac{%s + (%s)}{2} = %s \\\\ p = \\frac{z_A + z_C}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases}$ \\\\ Suy ra giá trị của biểu thức là: \\\\ $m^2 + n^2 + p^2 = \\left(%s\\right)^2 + \\left(%s\\right)^2 + \\left(%s\\right)^2 = %s$."""
        % (
            xa,
            xc,
            str_m,
            ya,
            yc,
            str_n,
            za,
            zc,
            str_p,
            str_m,
            str_n,
            str_p,
            str_t_val,
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
    