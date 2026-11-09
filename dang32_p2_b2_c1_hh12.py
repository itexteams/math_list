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


def bt_dang32_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hình hộp ABCD.A'B'C'D'
    # I là tâm của ABCD (trung điểm AC và BD), I' là tâm của A'B'C'D'
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(1, 4)
        za = random.randint(-3, 3)
    
        xb = random.randint(1, 4)
        yb = random.randint(-3, 1)
        zb = random.randint(-3, 3)
    
        # Tâm I có dạng số bán nguyên (mẫu số bằng 2) như đề gốc I(1/2; 4; -7/2)
        # 2*xI = xA + xC = xB + xD => chọn xD, yD, zD nguyên sao cho xB + xD lẻ
        xd = random.randint(-4, 0)
        yd = random.randint(5, 9)
        zd = random.randint(-8, -4)
    
        # Đảm bảo hoành độ của 2*I là số lẻ để xI là phân số /2
        if (xb + xd) % 2 == 0:
            xd += 1
    
        # Đảm bảo cao độ của 2*I là số lẻ để zI là phân số /2
        if (zb + zd) % 2 == 0:
            zd += 1
    
        # Điểm C thỏa mãn I là trung điểm AC, BD => C = B + D - A
        xc = xb + xd - xa
        yc = yb + yd - ya
        zc = zb + zd - za
    
        # Vectơ cạnh bên v = DD' = II'
        vx = random.randint(6, 11)
        vy = random.randint(-2, 2)
        vz = random.randint(12, 18)
    
        # Đỉnh D' = D + v
        xd_p = xd + vx
        yd_p = yd + vy
        zd_p = zd + vz
    
        # Kiểm tra đáy ABCD không suy biến
        ab_x, ab_y, ab_z = xb - xa, yb - ya, zb - za
        ad_x, ad_y, ad_z = xd - xa, yd - ya, zd - za
    
        cp_x = ab_y * ad_z - ab_z * ad_y
        cp_y = ab_z * ad_x - ab_x * ad_z
        cp_z = ab_x * ad_y - ab_y * ad_x
    
        if cp_x != 0 or cp_y != 0 or cp_z != 0:
            break
    
    # Tọa độ tâm I = (B + D) / 2
    xi_num = xb + xd
    yi_num = yb + yd
    zi_num = zb + zd
    
    str_xi = format_fraction_latex(xi_num, 2)
    str_yi = format_fraction_latex(yi_num, 2)
    str_zi = format_fraction_latex(zi_num, 2)
    
    # 1. Khoảng cách từ I đến mặt phẳng (Oyz): d(I, (Oyz)) = |xI| = |xi_num| / 2
    dist_i_oyz_val = Rational(abs(xi_num), 2)
    str_dist_i_oyz = format_fraction_latex(abs(xi_num), 2)
    # Tạo giá trị khoảng cách sai (như số nguyên 1 ở đề gốc)
    dist_i_oyz_s = 1 if dist_i_oyz_val != 1 else 2
    
    # 2. Điểm D có tung độ bằng yD
    yd_true = yd
    yd_false = yd + random.choice([-2, 2])
    
    # 3. Vectơ DD' = D' - D = (vx; vy; vz)
    dd_p_x = xd_p - xd
    dd_p_y = yd_p - yd
    dd_p_z = zd_p - zd
    
    dd_p_z_s = dd_p_z + random.choice([-3, -2, 2, 3])
    
    # 4. Tâm I'(x; y; z) của hình bình hành A'B'C'D':
    # Ta có vecto II' = vecto DD' => I' = I + DD'
    # x = xI + vx, y = yI + vy, z = zI + vz
    xi_prime = Rational(xi_num, 2) + vx
    yi_prime = Rational(yi_num, 2) + vy
    zi_prime = Rational(zi_num, 2) + vz
    
    str_x_ip = format_fraction_latex(xi_prime.p, xi_prime.q)
    str_y_ip = format_fraction_latex(yi_prime.p, yi_prime.q)
    str_z_ip = format_fraction_latex(zi_prime.p, zi_prime.q)
    
    # Giá trị biểu thức T = x . y . z
    t_val = xi_prime * yi_prime * zi_prime
    str_t_val = format_fraction_latex(t_val.p, t_val.q)
    str_t_val_s = format_fraction_latex(t_val.p + random.choice([20, 40, -40]), t_val.q)
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$ cho hình hộp $ABCD.A'B'C'D'$. Biết tọa độ các đỉnh là $A(%s;%s;%s)$, $B(%s;%s;%s)$, $D'(%s;%s;%s)$, \\\\ Điểm $I\\left(%s;%s;%s\\right)$ và $I'(x;y;z)$ lần lượt là tâm hình bình hành $ABCD$ và $A'B'C'D'$."""
        % (
            xa,
            ya,
            za,
            xb,
            yb,
            zb,
            xd_p,
            yd_p,
            zd_p,
            str_xi,
            str_yi,
            str_zi,
        )
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Khoảng cách từ I đến mặt phẳng (Oyz)
    nb_da_1_d = (
        "\\True $I\\left(%s;%s;%s\\right)$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (str_xi, str_yi, str_zi, str_dist_i_oyz)
    )
    nb_da_1_s = (
        "$I\\left(%s;%s;%s\\right)$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (str_xi, str_yi, str_zi, dist_i_oyz_s)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng $(Oyz)$ có phương trình là $x = 0$. \\\\ Khoảng cách từ điểm $I\\left(%s;%s;%s\\right)$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(I, (Oyz)) = |x_I| = \\left|%s\\right| = %s$."""
        % (str_xi, str_yi, str_zi, str_xi, str_dist_i_oyz)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Điểm D có tung độ bằng yD
    th_da_1_d = "\\True Điểm $D$ có tung độ bằng $%s$" % (yd_true)
    th_da_1_s = "Điểm $D$ có tung độ bằng $%s$" % (yd_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $I$ là tâm của hình bình hành $ABCD$ nên $I$ là trung điểm của đoạn thẳng $BD$. \\\\ Do đó ta có: \\\\ $\\begin{cases} x_I = \\frac{x_B + x_D}{2} \\\\ y_I = \\frac{y_B + y_D}{2} \\\\ z_I = \\frac{z_B + z_D}{2} \\end{cases} \\Rightarrow \\begin{cases} x_D = 2x_I - x_B = 2 \\cdot \\left(%s\\right) - (%s) = %s \\\\ y_D = 2y_I - y_B = 2 \\cdot (%s) - (%s) = %s \\\\ z_D = 2z_I - z_B = 2 \\cdot \\left(%s\\right) - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $D$ là $D(%s;%s;%s)$. Vậy điểm $D$ có tung độ bằng $%s$."""
        % (
            str_xi,
            xb,
            xd,
            str_yi,
            yb,
            yd,
            str_zi,
            zb,
            zd,
            xd,
            yd,
            zd,
            yd_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Vectơ DD' = (dd_p_x; dd_p_y; dd_p_z)
    vd_da_1_d = "\\True $\\vec{DD'} = (%s;%s;%s)$" % (dd_p_x, dd_p_y, dd_p_z)
    vd_da_1_s = "$\\vec{DD'} = (%s;%s;%s)$" % (dd_p_x, dd_p_y, dd_p_z_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Với $D(%s;%s;%s)$ và $D'(%s;%s;%s)$, tọa độ của vectơ $\\vec{DD'}$ là: \\\\ $\\vec{DD'} = (x_{D'} - x_D; y_{D'} - y_D; z_{D'} - z_D) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (
            xd,
            yd,
            zd,
            xd_p,
            yd_p,
            zd_p,
            xd_p,
            xd,
            yd_p,
            yd,
            zd_p,
            zd,
            dd_p_x,
            dd_p_y,
            dd_p_z,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Giá trị biểu thức T = x.y.z
    vdc_da_1_d = "\\True Giá trị biểu thức $T = x \\cdot y \\cdot z$ bằng $%s$" % (str_t_val)
    vdc_da_1_s = "Giá trị biểu thức $T = x \\cdot y \\cdot z$ bằng $%s$" % (str_t_val_s)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì $I$ và $I'$ lần lượt là tâm của hai hình bình hành đáy $ABCD$ và $A'B'C'D'$ nên đoạn thẳng $II'$ song song và bằng các cạnh bên của hình hộp. \\\\ Do đó ta có $\\vec{II'} = \\vec{DD'} = (%s;%s;%s)$. \\\\ Gọi tọa độ điểm $I'(x;y;z)$, ta có: \\\\ $\\begin{cases} x - x_I = %s \\\\ y - y_I = %s \\\\ z - z_I = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = x_I + %s = %s + %s = %s \\\\ y = y_I + %s = %s + %s = %s \\\\ z = z_I + %s = %s + %s = %s \\end{cases} \\Rightarrow I'\\left(%s;%s;%s\\right)$. \\\\ Khi đó giá trị của biểu thức $T = x \\cdot y \\cdot z$ là: \\\\ $T = \\left(%s\\right) \\cdot \\left(%s\\right) \\cdot \\left(%s\\right) = %s$."""
        % (
            dd_p_x,
            dd_p_y,
            dd_p_z,
            dd_p_x,
            dd_p_y,
            dd_p_z,
            dd_p_x,
            str_xi,
            dd_p_x,
            str_x_ip,
            dd_p_y,
            str_yi,
            dd_p_y,
            str_y_ip,
            dd_p_z,
            str_zi,
            dd_p_z,
            str_z_ip,
            str_x_ip,
            str_y_ip,
            str_z_ip,
            str_x_ip,
            str_y_ip,
            str_z_ip,
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
        "\\end{ex}\n \\end{minipage}\n\n" )
    return content
    