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


def bt_dang60_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu các vectơ OA, OB, AC, BD[cite: 24]
    while True:
        xa = random.randint(1, 4)
        ya = random.randint(-4, -1)
        za = random.randint(4, 8)
    
        xb = random.randint(3, 7)
        yb = random.randint(4, 7)
        zb = random.randint(1, 4)
    
        # Vectơ AC = (ac_x; ac_y; ac_z)[cite: 24]
        ac_x = random.randint(-6, -2)
        ac_y = random.randint(5, 8)
        ac_z = random.randint(8, 12)
    
        # Vectơ BD = (bd_x; bd_y; bd_z)[cite: 24]
        bd_x = random.randint(-12, -7)
        bd_y = random.choice([0, 1, -1])
        bd_z = random.randint(5, 9)
    
        # Tọa độ điểm C: C = A + AC[cite: 24]
        xc = xa + ac_x
        yc = ya + ac_y
        zc = za + ac_z
    
        # Tọa độ điểm D: D = B + BD[cite: 24]
        xd = xb + bd_x
        yd = yb + bd_y
        zd = zb + bd_z
    
        # Khoảng cách AB[cite: 24]
        ab_vec_x = xb - xa
        ab_vec_y = yb - ya
        ab_vec_z = zb - za
        ab_sq = ab_vec_x**2 + ab_vec_y**2 + ab_vec_z**2
    
        # Độ dài OC và OD[cite: 24]
        oc_sq = xc**2 + yc**2 + zc**2
        od_sq = xd**2 + yd**2 + zd**2
    
        len_oc = math.sqrt(oc_sq)
        len_od = math.sqrt(od_sq)
        two_od = 2 * len_od
    
        # Đảm bảo yc != ac_y để khẳng định c có tính phân loại (tránh nhầm tung độ điểm C với tung độ vectơ AC)[cite: 24]
        if (
            (xa, ya, za) != (xb, yb, zb)
            and yc != ac_y
            and abs(len_oc - two_od) > 0.2
        ):
            break
    
    # 1. Khẳng định a: Điểm A cách mặt phẳng (Oyz) một khoảng bằng |xa|[cite: 24]
    dist_a_oyz = abs(xa)
    dist_a_oyz_s = dist_a_oyz + random.choice([-1, 1])
    if dist_a_oyz_s <= 0:
        dist_a_oyz_s = dist_a_oyz + 2
    
    # 2. Khẳng định b: AB = sqrt(ab_sq)[cite: 24]
    str_ab_true = latex(sp.sqrt(ab_sq))
    str_ab_false = latex(sp.sqrt(ab_sq + random.choice([-4, -2, 2, 4])))
    if str_ab_false == str_ab_true:
        str_ab_false = "4\\sqrt{6}"[cite: 24]
    
    # 3. Khẳng định c: Điểm C có tung độ bằng yc[cite: 24]
    # Tạo phương án sai là tung độ của vectơ AC (ac_y)[cite: 24]
    yc_true = yc
    yc_false = ac_y
    
    # 4. Khẳng định d: OC < 2OD[cite: 24]
    is_oc_lt_2od = len_oc < two_od
    
    # Nội dung câu hỏi[cite: 24]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho các vectơ $\\vec{OA} = (%s;%s;%s); \\vec{OB} = (%s;%s;%s); \\vec{AC} = (%s;%s;%s); \\vec{BD} = (%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, ac_x, ac_y, ac_z, bd_x, bd_y, bd_z)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm A cách mặt phẳng (Oyz) một khoảng bằng dist_a_oyz[cite: 24]
    nb_da_1_d = "\\True Điểm $A$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$" % (
        dist_a_oyz
    )
    nb_da_1_s = "Điểm $A$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$" % (
        dist_a_oyz_s
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Từ $\\vec{OA} = (%s;%s;%s)$ suy ra tọa độ của điểm $A$ là $A(%s;%s;%s)$. \\\\ Mặt phẳng tọa độ $(Oyz)$ có phương trình là $x = 0$. \\\\ Khoảng cách từ điểm $A$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(A, (Oyz)) = |x_A| = |%s| = %s$."""
        % (
            xa,
            ya,
            za,
            xa,
            ya,
            za,
            xa,
            dist_a_oyz,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Độ dài đoạn thẳng AB[cite: 24]
    th_da_1_d = "\\True $AB = %s$" % (str_ab_true)
    th_da_1_s = "$AB = %s$" % (str_ab_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tọa độ vectơ $\\vec{AB}$ là: \\\\ $\\vec{AB} = \\vec{OB} - \\vec{OA} = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Khi đó độ dài đoạn thẳng $AB$ là: \\\\ $AB = |\\vec{AB}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
        % (
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            ab_vec_x,
            ab_vec_y,
            ab_vec_z,
            ab_vec_x,
            ab_vec_y,
            ab_vec_z,
            ab_sq,
            str_ab_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Điểm C có tung độ bằng yc[cite: 24]
    vd_da_1_d = "\\True Điểm $C$ có tung độ bằng $%s$" % (yc_true)
    vd_da_1_s = "Điểm $C$ có tung độ bằng $%s$" % (yc_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có hệ thức: $\\vec{OC} = \\vec{OA} + \\vec{AC}$. \\\\ Suy ra tọa độ của điểm $C$ là: \\\\ $\\begin{cases} x_C = x_A + x_{\\vec{AC}} = %s + (%s) = %s \\\\ y_C = y_A + y_{\\vec{AC}} = %s + (%s) = %s \\\\ z_C = z_A + z_{\\vec{AC}} = %s + (%s) = %s \\end{cases} \\Rightarrow C(%s;%s;%s)$. \\\\ Do đó điểm $C$ có tung độ bằng $y_C = %s$."""
        % (
            xa,
            ac_x,
            xc,
            ya,
            ac_y,
            yc,
            za,
            ac_z,
            zc,
            xc,
            yc,
            zc,
            yc,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: OC < 2OD[cite: 24]
    if is_oc_lt_2od:
        vdc_da_1_d = "\\True $OC < 2OD$"
        vdc_da_1_s = "$OC > 2OD$"
    else:
        vdc_da_1_d = "\\True $OC > 2OD$"
        vdc_da_1_s = "$OC < 2OD$"
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Từ $\\vec{OD} = \\vec{OB} + \\vec{BD}$, ta xác định tọa độ điểm $D$: \\\\ $\\begin{cases} x_D = x_B + x_{\\vec{BD}} = %s + (%s) = %s \\\\ y_D = y_B + y_{\\vec{BD}} = %s + (%s) = %s \\\\ z_D = z_B + z_{\\vec{BD}} = %s + (%s) = %s \\end{cases} \\Rightarrow D(%s;%s;%s)$. \\\\ Khoảng cách từ gốc tọa độ $O$ đến các điểm $C(%s;%s;%s)$ và $D(%s;%s;%s)$ là: \\\\ $OC = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} \\approx %s$. \\\\ $OD = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} \\approx %s \\Rightarrow 2OD \\approx 2 \\cdot %s = %s$. \\\\ Vì $%s %s %s$ nên khẳng định $OC %s 2OD$ là %s."""
        % (
            xb,
            bd_x,
            xd,
            yb,
            bd_y,
            yd,
            zb,
            bd_z,
            zd,
            xd,
            yd,
            zd,
            xc,
            yc,
            zc,
            xd,
            yd,
            zd,
            xc,
            yc,
            zc,
            oc_sq,
            str(round(len_oc, 2)).replace(".", ","),
            xd,
            yd,
            zd,
            od_sq,
            str(round(len_od, 2)).replace(".", ","),
            str(round(len_od, 2)).replace(".", ","),
            str(round(two_od, 2)).replace(".", ","),
            str(round(len_oc, 2)).replace(".", ","),
            "<" if is_oc_lt_2od else ">",
            str(round(two_od, 2)).replace(".", ","),
            "<" if is_oc_lt_2od else ">",
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
    