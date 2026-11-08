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


def bt_dang22_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên toạ độ ba đỉnh A, B, C không thẳng hàng
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(-3, 3)
    
        xb = random.randint(-4, 4)
        yb = random.randint(-4, 4)
        zb = random.randint(-4, 4)
    
        xc = random.randint(-4, 4)
        yc = random.randint(-4, 4)
        zc = random.randint(-4, 4)
    
        # Vectơ AB và AC
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        # Tích có hướng [AB, AC] để kiểm tra ba điểm không thẳng hàng
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        len_ac_sq = ac_x**2 + ac_y**2 + ac_z**2
        dot_ab_ac = ab_x * ac_x + ab_y * ac_y + ab_z * ac_z
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and len_ab_sq > 0
            and len_ac_sq > 0
            and dot_ab_ac != 0
        ):
            break
    
    # 1. Trọng tâm G của tam giác ABC
    xg_num = xa + xb + xc
    yg_num = ya + yb + yc
    zg_num = za + zb + zc
    
    str_xg = format_fraction_latex(xg_num, 3)
    str_yg = format_fraction_latex(yg_num, 3)
    str_zg = format_fraction_latex(zg_num, 3)
    
    str_xg_s = format_fraction_latex(xg_num + random.choice([-1, 1]), 3)
    
    # 2. ABCD là hình bình hành <=> vecto AB = vecto DC <=> D = C - AB = C + A - B
    xd = xc + xa - xb
    yd = yc + ya - yb
    zd = zc + za - zb
    
    # Toạ độ sai của D (nhầm sang hình bình hành ABDC: D = B + C - A)
    xd_s = xb + xc - xa
    yd_s = yb + yc - ya
    zd_s = zb + zc - za
    
    # 3. M thuộc đoạn AB sao cho MB = 2MA <=> vecto MB = -2 vecto MA <=> M = (2A + B)/3
    xm_num = 2 * xa + xb
    ym_num = 2 * ya + yb
    zm_num = 2 * za + zb
    
    str_xm = format_fraction_latex(xm_num, 3)
    str_ym = format_fraction_latex(ym_num, 3)
    str_zm = format_fraction_latex(zm_num, 3)
    
    str_xm_s = format_fraction_latex(xa + 2 * xb, 3)
    str_ym_s = format_fraction_latex(ya + 2 * yb, 3)
    str_zm_s = format_fraction_latex(za + 2 * zb, 3)
    
    # 4. cos góc BAC = (AB . AC) / (|AB| * |AC|)
    cos_sym = Rational(dot_ab_ac, 1) / (sp.sqrt(len_ab_sq) * sp.sqrt(len_ac_sq))
    str_cos_true = latex(cos_sym)
    str_cos_false = latex(-cos_sym)
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho tam giác $ABC$ có $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Toạ độ trọng tâm G của tam giác ABC
    nb_da_1_d = (
        "\\True Toạ độ trọng tâm $G$ của tam giác $ABC$ là $G\\left(%s;%s;%s\\right)$"
        % (str_xg, str_yg, str_zg)
    )
    nb_da_1_s = (
        "Toạ độ trọng tâm $G$ của tam giác $ABC$ là $G\\left(%s;%s;%s\\right)$"
        % (str_xg_s, str_yg, str_zg)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ trọng tâm $G$ của tam giác $ABC$ được tính theo công thức: \\\\ $\\begin{cases} x_G = \\frac{x_A + x_B + x_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ y_G = \\frac{y_A + y_B + y_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\end{cases}$ \\\\ Vậy tọa độ trọng tâm $G$ là $G\\left(%s;%s;%s\\right)$."""
        % (
            xa,
            xb,
            xc,
            str_xg,
            ya,
            yb,
            yc,
            str_yg,
            za,
            zb,
            zc,
            str_zg,
            str_xg,
            str_yg,
            str_zg,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Toạ độ điểm D sao cho ABCD là hình bình hành
    th_da_1_d = (
        "\\True Toạ độ điểm $D$ sao cho $ABCD$ là hình bình hành là $D(%s;%s;%s)$"
        % (xd, yd, zd)
    )
    th_da_1_s = (
        "Toạ độ điểm $D$ sao cho $ABCD$ là hình bình hành là $D(%s;%s;%s)$"
        % (xd_s, yd_s, zd_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Gọi tọa độ điểm $D$ là $D(x_D; y_D; z_D)$. \\\\ Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s;%s;%s)$. \\\\ $\\vec{DC} = (x_C - x_D; y_C - y_D; z_C - z_D) = (%s - x_D; %s - y_D; %s - z_D)$. \\\\ Tứ giác $ABCD$ là hình bình hành khi và chỉ khi: \\\\ $\\vec{AB} = \\vec{DC} \\Leftrightarrow \\begin{cases} %s - x_D = %s \\\\ %s - y_D = %s \\\\ %s - z_D = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_D = %s - (%s) = %s \\\\ y_D = %s - (%s) = %s \\\\ z_D = %s - (%s) = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $D$ là $D(%s;%s;%s)$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            xc,
            yc,
            zc,
            xc,
            ab_x,
            yc,
            ab_y,
            zc,
            ab_z,
            xc,
            ab_x,
            xd,
            yc,
            ab_y,
            yd,
            zc,
            ab_z,
            zd,
            xd,
            yd,
            zd,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Toạ độ điểm M thuộc đoạn AB sao cho MB = 2MA
    vd_da_1_d = (
        "\\True Toạ độ điểm $M$ thuộc đoạn $AB$ sao cho $MB = 2MA$ là $M\\left(%s;%s;%s\\right)$"
        % (str_xm, str_ym, str_zm)
    )
    vd_da_1_s = (
        "Toạ độ điểm $M$ thuộc đoạn $AB$ sao cho $MB = 2MA$ là $M\\left(%s;%s;%s\\right)$"
        % (str_xm_s, str_ym_s, str_zm_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì điểm $M$ thuộc đoạn thẳng $AB$ và $MB = 2MA$ nên điểm $M$ nằm giữa hai điểm $A$ và $B$. \\\\ Do đó hai vectơ $\\vec{MB}$ và $\\vec{MA}$ ngược hướng, suy ra $\\vec{MB} = -2\\vec{MA} \\Leftrightarrow \\vec{MB} + 2\\vec{MA} = \\vec{0}$. \\\\ Tọa độ điểm $M$ thỏa mãn: \\\\ $\\begin{cases} x_M = \\frac{2x_A + x_B}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\\\ y_M = \\frac{2y_A + y_B}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\\\ z_M = \\frac{2z_A + z_B}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $M$ là $M\\left(%s;%s;%s\\right)$."""
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
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: cos góc BAC
    vdc_da_1_d = "\\True $\\cos\\widehat{BAC} = %s$" % (str_cos_true)
    vdc_da_1_s = "$\\cos\\widehat{BAC} = %s$" % (str_cos_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s;%s;%s) \\Rightarrow AB = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s;%s;%s) \\Rightarrow AC = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Tích vô hướng của hai vectơ: \\\\ $\\vec{AB} \\cdot \\vec{AC} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Do đó côsin của góc $\\widehat{BAC}$ là: \\\\ $\\cos\\widehat{BAC} = \\frac{\\vec{AB} \\cdot \\vec{AC}}{|\\vec{AB}| \\cdot |\\vec{AC}|} = \\frac{%s}{\\sqrt{%s} \\cdot \\sqrt{%s}} = %s$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            ab_x,
            ab_y,
            ab_z,
            len_ab_sq,
            ac_x,
            ac_y,
            ac_z,
            ac_x,
            ac_y,
            ac_z,
            len_ac_sq,
            ab_x,
            ac_x,
            ab_y,
            ac_y,
            ab_z,
            ac_z,
            dot_ab_ac,
            dot_ab_ac,
            len_ab_sq,
            len_ac_sq,
            str_cos_true,
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
    