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


def bt_dang69_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C sao cho BA và BC có độ dài đẹp để tỉ lệ phân giác hữu tỉ đẹp
    # Cụ thể: BC = 2*BA (như đề gốc: BA = sqrt(L), BC = 2*sqrt(L))[cite: 22]
    # Khi đó DA / DC = BA / BC = 1/2 <=> \vec{DC} = -2\vec{DA} <=> D = (2A + C) / 3[cite: 22]
    while True:
        xa = random.randint(1, 3)
        ya = random.randint(1, 4)
        za = random.randint(-2, 1)
    
        xb = random.randint(1, 4)
        yb = random.randint(-3, 0)
        zb = random.randint(2, 5)
    
        ba_x = xa - xb
        ba_y = ya - yb
        ba_z = za - zb
        ba_sq = ba_x**2 + ba_y**2 + ba_z**2
    
        # Tìm vectơ BC có độ dài BC^2 = 4 * ba_sq sao cho A, B, C không thẳng hàng[cite: 22]
        # Ta có thể tìm một hoán vị và đổi dấu các thành phần của 2*BA[cite: 22]
        components = [2 * ba_x, 2 * ba_y, 2 * ba_z]
        random.shuffle(components)
        s_signs = [random.choice([-1, 1]), random.choice([-1, 1]), random.choice([-1, 1])]
        bc_x = components[0] * s_signs[0]
        bc_y = components[1] * s_signs[1]
        bc_z = components[2] * s_signs[2]
    
        # Kiểm tra không cùng phương với BA[cite: 22]
        cp_x = ba_y * bc_z - ba_z * bc_y
        cp_y = ba_z * bc_x - ba_x * bc_z
        cp_z = ba_x * bc_y - ba_y * bc_x
    
        if cp_x != 0 or cp_y != 0 or cp_z != 0:
            xc = xb + bc_x
            yc = yb + bc_y
            zc = zb + bc_z
    
            # Kiểm tra tọa độ D = (2A + C)/3[cite: 22]
            xd_num = 2 * xa + xc
            yd_num = 2 * ya + yc
            zd_num = 2 * za + zc
    
            # Trọng tâm G = (A + B + C)/3[cite: 22]
            xg_num = xa + xb + xc
            yg_num = ya + yb + yc
            zg_num = za + zb + zc
    
            # Trung điểm M của BC: M = (B + C)/2[cite: 22]
            # AM^2 = (xM - xA)^2 + (yM - yA)^2 + (zM - zA)^2[cite: 22]
            # 4*AM^2 = (xB + xC - 2xA)^2 + (yB + yC - 2yA)^2 + (zB + zC - 2zA)^2[cite: 22]
            am_sq_4 = (
                (xb + xc - 2 * xa) ** 2
                + (yb + yc - 2 * ya) ** 2
                + (zb + zc - 2 * za) ** 2
            )
            if am_sq_4 % 4 == 0:
                am_sq = am_sq_4 // 4
                break
    
    # 1. Khẳng định a: AB + 2*AC[cite: 22]
    ab_x = xb - xa
    ab_y = yb - ya
    ab_z = zb - za
    
    ac_x = xc - xa
    ac_y = yc - ya
    ac_z = zc - za
    
    vec_sum_x = ab_x + 2 * ac_x
    vec_sum_y = ab_y + 2 * ac_y
    vec_sum_z = ab_z + 2 * ac_z
    
    vec_sum_x_false = vec_sum_x + random.choice([-2, 2])
    vec_sum_y_false = vec_sum_y
    vec_sum_z_false = vec_sum_z
    
    # 2. Khẳng định b: Trọng tâm G của tam giác ABC[cite: 22]
    str_xg = format_fraction_latex(xg_num, 3)
    str_yg = format_fraction_latex(yg_num, 3)
    str_zg = format_fraction_latex(zg_num, 3)
    
    str_xg_false = format_fraction_latex(xg_num + random.choice([-1, 1]), 3)
    
    # 3. Khẳng định c: AM = sqrt(am_sq)[cite: 22]
    str_am_true = latex(sp.sqrt(am_sq))
    str_am_false = latex(sp.sqrt(am_sq + random.choice([-3, -2, 2, 3])))
    if str_am_false == str_am_true:
        str_am_false = "\\sqrt{31}"[cite: 22]
    
    # 4. Khẳng định d: Chân đường phân giác trong góc B là D(xd; yd; zd)[cite: 22]
    str_xd = format_fraction_latex(xd_num, 3)
    str_yd = format_fraction_latex(yd_num, 3)
    str_zd = format_fraction_latex(zd_num, 3)
    
    str_xd_false = format_fraction_latex(xd_num + random.choice([-1, 1]), 3)
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho tam giác $ABC$ có $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$. Gọi $D$ là chân đường phân giác trong góc $B$ của tam giác $ABC$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: AB + 2*AC[cite: 22]
    nb_da_1_d = "\\True $\\vec{AB} + 2\\vec{AC} = (%s;%s;%s)$" % (
        vec_sum_x,
        vec_sum_y,
        vec_sum_z,
    )
    nb_da_1_s = "$\\vec{AB} + 2\\vec{AC} = (%s;%s;%s)$" % (
        vec_sum_x_false,
        vec_sum_y_false,
        vec_sum_z_false,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Suy ra: \\\\ $2\\vec{AC} = 2(%s;%s;%s) = (%s;%s;%s)$. \\\\ Khi đó: \\\\ $\\vec{AB} + 2\\vec{AC} = (%s + (%s); %s + (%s); %s + (%s)) = (%s;%s;%s)$."""
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
            2 * ac_x,
            2 * ac_y,
            2 * ac_z,
            ab_x,
            2 * ac_x,
            ab_y,
            2 * ac_y,
            ab_z,
            2 * ac_z,
            vec_sum_x,
            vec_sum_y,
            vec_sum_z,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Trọng tâm G của tam giác ABC[cite: 22]
    th_da_1_d = (
        "\\True Gọi $G$ là trọng tâm tam giác $ABC$, ta có $G\\left(%s;%s;%s\\right)$"
        % (str_xg, str_yg, str_zg)
    )
    th_da_1_s = (
        "Gọi $G$ là trọng tâm tam giác $ABC$, ta có $G\\left(%s;%s;%s\\right)$"
        % (str_xg_false, str_yg, str_zg)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Tọa độ trọng tâm $G$ của tam giác $ABC$ được tính theo công thức: \\\\ $\\begin{cases} x_G = \\frac{x_A + x_B + x_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ y_G = \\frac{y_A + y_B + y_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\end{cases} \\Rightarrow G\\left(%s;%s;%s\\right)$. \\\\ Do đó mệnh đề là %s."""
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
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Gọi M là trung điểm BC, ta có AM = ...[cite: 22]
    vd_da_1_d = "\\True Gọi $M$ là trung điểm $BC$, ta có $AM = %s$" % (str_am_true)
    vd_da_1_s = "Gọi $M$ là trung điểm $BC$, ta có $AM = %s$" % (str_am_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    str_xm = format_fraction_latex(xb + xc, 2)
    str_ym = format_fraction_latex(yb + yc, 2)
    str_zm = format_fraction_latex(zb + zc, 2)
    
    loigiai_vd_1 = (
        """Tọa độ trung điểm $M$ của đoạn thẳng $BC$ là: \\\\ $\\begin{cases} x_M = \\frac{x_B + x_C}{2} = \\frac{%s + (%s)}{2} = %s \\\\ y_M = \\frac{y_B + y_C}{2} = \\frac{%s + (%s)}{2} = %s \\\\ z_M = \\frac{z_B + z_C}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases} \\Rightarrow M\\left(%s;%s;%s\\right)$. \\\\ Khi đó độ dài đoạn thẳng $AM$ là: \\\\ $AM = \\sqrt{(x_M - x_A)^2 + (y_M - y_A)^2 + (z_M - z_A)^2} = \\sqrt{%s} = %s$. \\\\ Do đó khẳng định là %s."""
        % (
            xb,
            xc,
            str_xm,
            yb,
            yc,
            str_ym,
            zb,
            zc,
            str_zm,
            str_xm,
            str_ym,
            str_zm,
            am_sq,
            str_am_true,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Chân đường phân giác trong góc B là D(xd; yd; zd)[cite: 22]
    vdc_da_1_d = "\\True $D\\left(%s;%s;%s\\right)$" % (str_xd, str_yd, str_zd)
    vdc_da_1_s = "\\True $D\\left(%s;%s;%s\\right)$" % (
        str_xd_false,
        str_yd,
        str_zd,
    )
    # Đổi đáp án sai không chứa \True
    vdc_da_1_s = "$D\\left(%s;%s;%s\\right)$" % (str_xd_false, str_yd, str_zd)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Độ dài các đoạn thẳng $BA$ và $BC$ là: \\\\ $BA = \\sqrt{(x_A - x_B)^2 + (y_A - y_B)^2 + (z_A - z_B)^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $BC = \\sqrt{(x_C - x_B)^2 + (y_C - y_B)^2 + (z_C - z_B)^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = 2\\sqrt{%s}$. \\\\ Theo tính chất đường phân giác trong góc $B$ của tam giác $ABC$, ta có: \\\\ $\\frac{DA}{DC} = \\frac{BA}{BC} = \\frac{\\sqrt{%s}}{2\\sqrt{%s}} = \\frac{1}{2} \\Leftrightarrow DC = 2DA$. \\\\ Vì $D$ nằm trên đoạn thẳng $AC$ nên hai vectơ $\\vec{DC}$ và $\\vec{DA}$ ngược hướng, suy ra: \\\\ $\\vec{DC} = -2\\vec{DA} \\Leftrightarrow \\vec{OC} - \\vec{OD} = -2(\\vec{OA} - \\vec{OD}) \\Leftrightarrow 3\\vec{OD} = 2\\vec{OA} + \\vec{OC} \\Leftrightarrow \\vec{OD} = \\frac{2\\vec{OA} + \\vec{OC}}{3}$. \\\\ Do đó tọa độ điểm $D$ là: \\\\ $\\begin{cases} x_D = \\frac{2x_A + x_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\\\ y_D = \\frac{2y_A + y_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\\\ z_D = \\frac{2z_A + z_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\end{cases} \\Rightarrow D\\left(%s;%s;%s\\right)$. \\\\ Do đó mệnh đề là %s."""
        % (
            ba_x,
            ba_y,
            ba_z,
            ba_sq,
            bc_x,
            bc_y,
            bc_z,
            4 * ba_sq,
            ba_sq,
            ba_sq,
            ba_sq,
            xa,
            xc,
            str_xd,
            ya,
            yc,
            str_yd,
            za,
            zc,
            str_zd,
            str_xd,
            str_yd,
            str_zd,
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
    