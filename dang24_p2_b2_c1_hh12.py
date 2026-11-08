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


def bt_dang24_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hình hộp ABCD.A'B'C'D'
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(1, 4)
        za = random.randint(-3, 3)
    
        xb = random.randint(1, 4)
        yb = random.randint(-3, 1)
        zb = random.randint(-3, 3)
    
        # Điểm C sao cho zC khác 0 để khoảng cách đến (Oxy) dương
        xc = random.randint(-4, 0)
        yc = random.randint(1, 4)
        zc = random.choice([-8, -7, -6, -5, 5, 6, 7, 8])
    
        # Kiểm tra đáy ABCD không suy biến (ba điểm A, B, C không thẳng hàng)
        ab_x, ab_y, ab_z = xb - xa, yb - ya, zb - za
        ac_x, ac_y, ac_z = xc - xa, yc - ya, zc - za
    
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # Vì ABCD là hình bình hành nên:
    # vecto AB = vecto DC <=> D = C - AB = C + A - B
    xd = xc + xa - xb
    yd = yc + ya - yb
    zd = zc + za - zb
    
    # Vectơ cạnh bên v = DD' = BB' = AA' = CC'
    vx = random.randint(5, 10)
    vy = random.randint(-3, 3)
    vz = random.randint(10, 18)
    
    # Điểm D' = D + v
    xd_p = xd + vx
    yd_p = yd + vy
    zd_p = zd + vz
    
    # 1. Khoảng cách từ điểm C đến mặt phẳng (Oxy): d(C, (Oxy)) = |zc|[cite: 20]
    dist_c_oxy = abs(zc)
    dist_c_oxy_s = dist_c_oxy + random.choice([1, 2])
    
    # 2. Giao điểm của hai đường chéo AC, BD là tâm I của hình bình hành ABCD[cite: 20]:
    # I là trung điểm AC: yI = (yA + yC) / 2
    yi_num = ya + yc
    str_yi = format_fraction_latex(yi_num, 2)
    # Tạo giá trị tung độ sai
    str_yi_s = format_fraction_latex(yi_num + random.choice([-2, 2]), 2)
    
    # 3. Tọa độ của vectơ DD' = D' - D = (vx; vy; vz)[cite: 20]
    dd_p_x = xd_p - xd
    dd_p_y = yd_p - yd
    dd_p_z = zd_p - zd
    
    dd_p_x_s = dd_p_x + random.choice([-1, 1])
    dd_p_y_s = dd_p_y
    dd_p_z_s = dd_p_z
    
    # 4. Điểm B' = B + DD' = (xb + vx; yb + vy; zb + vz)[cite: 20]
    # Cao độ của B' là z_b_p = zb + vz[cite: 20]
    zb_p = zb + vz
    bound_zb_p = zb_p + 2  # Mốc so sánh[cite: 20]
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$ cho hình hộp $ABCD.A'B'C'D'$. Biết $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$ và $D'(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xd_p, yd_p, zd_p)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm C cách mặt phẳng (Oxy) một khoảng bằng dist_c_oxy[cite: 20]
    nb_da_1_d = (
        "\\True Điểm $C(%s;%s;%s)$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$"
        % (xc, yc, zc, dist_c_oxy)
    )
    nb_da_1_s = (
        "Điểm $C(%s;%s;%s)$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$"
        % (xc, yc, zc, dist_c_oxy_s)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng $(Oxy)$ có phương trình là $z = 0$. \\\\ Khoảng cách từ điểm $C(%s;%s;%s)$ đến mặt phẳng $(Oxy)$ là: \\\\ $d(C, (Oxy)) = |z_C| = |%s| = %s$."""
        % (xc, yc, zc, zc, dist_c_oxy)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Giao điểm của hai đường chéo AC, BD có tung độ bằng str_yi[cite: 20]
    th_da_1_d = (
        "\\True Giao điểm của hai đường chéo $AC, BD$ có tung độ bằng $%s$"
        % (str_yi)
    )
    th_da_1_s = (
        "Giao điểm của hai đường chéo $AC, BD$ có tung độ bằng $%s$" % (str_yi_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $ABCD$ là hình bình hành nên giao điểm của hai đường chéo $AC, BD$ chính là trung điểm của đoạn thẳng $AC$. \\\\ Tung độ của trung điểm đoạn thẳng $AC$ là: \\\\ $y = \\frac{y_A + y_C}{2} = \\frac{%s + (%s)}{2} = %s$."""
        % (ya, yc, str_yi)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Vectơ DD'[cite: 20]
    vd_da_1_d = "\\True $\\vec{DD'} = (%s;%s;%s)$" % (dd_p_x, dd_p_y, dd_p_z)
    vd_da_1_s = "$\\vec{DD'} = (%s;%s;%s)$" % (dd_p_x_s, dd_p_y_s, dd_p_z_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì tứ giác $ABCD$ là hình bình hành nên ta có: \\\\ $\\vec{AB} = \\vec{DC} \\Leftrightarrow \\begin{cases} x_B - x_A = x_C - x_D \\\\ y_B - y_A = y_C - y_D \\\\ z_B - z_A = z_C - z_D \\end{cases} \\Leftrightarrow \\begin{cases} x_D = x_C + x_A - x_B = %s + (%s) - (%s) = %s \\\\ y_D = y_C + y_A - y_B = %s + (%s) - (%s) = %s \\\\ z_D = z_C + z_A - z_B = %s + (%s) - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $D$ là $D(%s;%s;%s)$. \\\\ Khi đó tọa độ của vectơ $\\vec{DD'}$ là: \\\\ $\\vec{DD'} = (x_{D'} - x_D; y_{D'} - y_D; z_{D'} - z_D) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (
            xc,
            xa,
            xb,
            xd,
            yc,
            ya,
            yb,
            yd,
            zc,
            za,
            zb,
            zd,
            xd,
            yd,
            zd,
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
    # Mệnh đề d: Điểm B' có cao độ lớn hơn bound_zb_p[cite: 20]
    # zb_p < bound_zb_p nên phát biểu 'lớn hơn bound_zb_p' là SAI[cite: 20]
    vdc_da_1_d = (
        "\\True Điểm $B'$ có cao độ bằng $%s$, là một số nhỏ hơn $%s$"
        % (zb_p, bound_zb_p)
    )
    vdc_da_1_s = "Điểm $B'$ có cao độ lớn hơn $%s$" % (bound_zb_p)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì $ABCD.A'B'C'D'$ là hình hộp nên các cạnh bên đôi một song song và bằng nhau, suy ra $\\vec{BB'} = \\vec{DD'} = (%s;%s;%s)$. \\\\ Gọi tọa độ điểm $B'$ là $B'(x_{B'}; y_{B'}; z_{B'})$, ta có: \\\\ $\\begin{cases} x_{B'} = x_B + %s = %s + (%s) = %s \\\\ y_{B'} = y_B + %s = %s + (%s) = %s \\\\ z_{B'} = z_B + %s = %s + (%s) = %s \\end{cases} \\Rightarrow B'(%s;%s;%s)$. \\\\ Cao độ của điểm $B'$ là $z_{B'} = %s < %s$, do đó mệnh đề khẳng định cao độ lớn hơn $%s$ là sai."""
        % (
            dd_p_x,
            dd_p_y,
            dd_p_z,
            dd_p_x,
            xb,
            dd_p_x,
            xb + dd_p_x,
            dd_p_y,
            yb,
            dd_p_y,
            yb + dd_p_y,
            dd_p_z,
            zb,
            dd_p_z,
            zb_p,
            xb + dd_p_x,
            yb + dd_p_y,
            zb_p,
            zb_p,
            bound_zb_p,
            bound_zb_p,
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
    