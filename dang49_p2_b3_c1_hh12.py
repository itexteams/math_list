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


def bt_dang49_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu 4 điểm A, B, C, D sao cho tọa độ điểm I nguyên đẹp:
    # Điểm I thỏa mãn IA + IB + IC + 2ID = 0 <=> I = (A + B + C + 2D) / 5
    while True:
        xa = random.randint(-7, -4)
        ya = random.randint(2, 5)
        za = random.randint(-2, 2)
    
        xb = random.randint(0, 3)
        yb = random.randint(0, 3)
        zb = random.randint(1, 4)
    
        xc = random.randint(-4, -1)
        yc = random.randint(1, 4)
        zc = random.randint(2, 5)
    
        xd = random.randint(-3, 0)
        yd = random.randint(-3, 0)
        zd = random.randint(-1, 2)
    
        sum_x = xa + xb + xc + 2 * xd
        sum_y = ya + yb + yc + 2 * yd
        sum_z = za + zb + zc + 2 * zd
    
        # Kiểm tra chia hết cho 5 để I có tọa độ nguyên đẹp
        if sum_x % 5 == 0 and sum_y % 5 == 0 and sum_z % 5 == 0:
            # Khoảng cách AC, AD, AB
            ac_sq = (xc - xa) ** 2 + (yc - ya) ** 2 + (zc - za) ** 2
            ad_sq = (xd - xa) ** 2 + (yd - ya) ** 2 + (zd - za) ** 2
            ab_sq = (xb - xa) ** 2 + (yb - ya) ** 2 + (zb - za) ** 2
    
            len_ac = math.sqrt(ac_sq)
            len_ad = math.sqrt(ad_sq)
            len_ab = math.sqrt(ab_sq)
    
            sum_ac_ad = len_ac + len_ad
            two_ab = 2 * len_ab
    
            if (
                (xa, ya, za) != (xb, yb, zb)
                and (xa, ya, za) != (xc, yc, zc)
                and (xa, ya, za) != (xd, yd, zd)
                and abs(sum_ac_ad - two_ab) > 0.05
            ):
                break
    
    # 1. Điểm C cách mặt phẳng (Oyz) một khoảng bằng |xC|[cite: 24]
    dist_c_oyz = abs(xc)
    dist_c_oyz_s = dist_c_oyz + random.choice([-1, 1])
    
    # 2. So sánh AC + AD và 2AB[cite: 24]
    is_sum_lt_2ab = sum_ac_ad < two_ab
    
    # 3. Điểm I thỏa mãn IA + IB + IC + 2ID = 0 thì I có cao độ z_I = sum_z // 5[cite: 24]
    xi_val = sum_x // 5
    yi_val = sum_y // 5
    zi_val = sum_z // 5
    
    zi_val_s = zi_val + random.choice([-2, -1, 1, 2])
    
    # 4. Biểu thức P = MA^2 + MB^2 + MC^2 + 2MD^2 đạt GTNN:
    # Với I thỏa mãn IA + IB + IC + 2ID = 0, ta có:
    # P = (MI + IA)^2 + (MI + IB)^2 + (MI + IC)^2 + 2(MI + ID)^2
    #   = 5 MI^2 + 2 MI . (IA + IB + IC + 2ID) + IA^2 + IB^2 + IC^2 + 2ID^2
    #   = 5 MI^2 + const >= const
    # Dấu bằng xảy ra khi M trùng I => M(a; b; c) = (xi_val; yi_val; zi_val)[cite: 24]
    a_val = xi_val
    b_val = yi_val
    c_val = zi_val
    val_q = 100 * a_val + 10 * b_val + c_val
    
    bound_q = val_q + random.choice([5, 10, -5, -10])
    is_q_lt_bound = val_q < bound_q
    
    # Nội dung câu hỏi[cite: 24]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho $4$ điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s), D(%s;%s;%s)$, biết tọa độ điểm $M(a;b;c)$ để $P = MA^2 + MB^2 + MC^2 + 2MD^2$ đạt giá trị nhỏ nhất."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xd, yd, zd)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm C cách mặt phẳng (Oyz) một khoảng bằng dist_c_oyz[cite: 24]
    nb_da_1_d = (
        "\\True Điểm $C(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (xc, yc, zc, dist_c_oyz)
    )
    nb_da_1_s = (
        "Điểm $C(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (xc, yc, zc, dist_c_oyz_s)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng tọa độ $(Oyz)$ có phương trình là $x = 0$. \\\\ Khoảng cách từ điểm $C(%s;%s;%s)$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(C, (Oyz)) = |x_C| = |%s| = %s$."""
        % (
            xc,
            yc,
            zc,
            xc,
            dist_c_oyz,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: AC + AD < 2AB[cite: 24]
    if is_sum_lt_2ab:
        th_da_1_d = "\\True $AC + AD < 2AB$"
        th_da_1_s = "$AC + AD > 2AB$"
    else:
        th_da_1_d = "\\True $AC + AD > 2AB$"
        th_da_1_s = "$AC + AD < 2AB$"
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta tính độ dài các đoạn thẳng: \\\\ $AC = \\sqrt{(x_C - x_A)^2 + (y_C - y_A)^2 + (z_C - z_A)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{%s} \\approx %s$. \\\\ $AD = \\sqrt{(x_D - x_A)^2 + (y_D - y_A)^2 + (z_D - z_A)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{%s} \\approx %s$. \\\\ $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{%s} \\approx %s$. \\\\ Khi đó: \\\\ $AC + AD \\approx %s + %s = %s$. \\\\ $2AB \\approx 2 \\cdot %s = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            xc,
            xa,
            yc,
            ya,
            zc,
            za,
            ac_sq,
            str(round(len_ac, 2)).replace(".", ","),
            xd,
            xa,
            yd,
            ya,
            zd,
            za,
            ad_sq,
            str(round(len_ad, 2)).replace(".", ","),
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            ab_sq,
            str(round(len_ab, 2)).replace(".", ","),
            str(round(len_ac, 2)).replace(".", ","),
            str(round(len_ad, 2)).replace(".", ","),
            str(round(sum_ac_ad, 2)).replace(".", ","),
            str(round(len_ab, 2)).replace(".", ","),
            str(round(two_ab, 2)).replace(".", ","),
            str(round(sum_ac_ad, 2)).replace(".", ","),
            "<" if is_sum_lt_2ab else ">",
            str(round(two_ab, 2)).replace(".", ","),
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Gọi I là điểm thỏa mãn IA + IB + IC + 2ID = 0 thì I có cao độ bằng zi_val[cite: 24]
    vd_da_1_d = (
        "\\True Gọi $I$ là điểm thỏa mãn $\\vec{IA} + \\vec{IB} + \\vec{IC} + 2\\vec{ID} = \\vec{0}$ thì $I$ có cao độ bằng $%s$"
        % (zi_val)
    )
    vd_da_1_s = (
        "Gọi $I$ là điểm thỏa mãn $\\vec{IA} + \\vec{IB} + \\vec{IC} + 2\\vec{ID} = \\vec{0}$ thì $I$ có cao độ bằng $%s$"
        % (zi_val_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có hệ thức vectơ: \\\\ $\\vec{IA} + \\vec{IB} + \\vec{IC} + 2\\vec{ID} = \\vec{0} \\Leftrightarrow (\\vec{OA} - \\vec{OI}) + (\\vec{OB} - \\vec{OI}) + (\\vec{OC} - \\vec{OI}) + 2(\\vec{OD} - \\vec{OI}) = \\vec{0}$ \\\\ $\\Leftrightarrow 5\\vec{OI} = \\vec{OA} + \\vec{OB} + \\vec{OC} + 2\\vec{OD} \\Leftrightarrow \\vec{OI} = \\frac{\\vec{OA} + \\vec{OB} + \\vec{OC} + 2\\vec{OD}}{5}$. \\\\ Tọa độ của điểm $I$ thỏa mãn: \\\\ $\\begin{cases} x_I = \\frac{x_A + x_B + x_C + 2x_D}{5} = \\frac{%s + (%s) + (%s) + 2 \\cdot (%s)}{5} = %s \\\\ y_I = \\frac{y_A + y_B + y_C + 2y_D}{5} = \\frac{%s + (%s) + (%s) + 2 \\cdot (%s)}{5} = %s \\\\ z_I = \\frac{z_A + z_B + z_C + 2z_D}{5} = \\frac{%s + (%s) + (%s) + 2 \\cdot (%s)}{5} = %s \\end{cases} \\Rightarrow I(%s;%s;%s)$. \\\\ Do đó điểm $I$ có cao độ bằng $%s$."""
        % (
            xa,
            xb,
            xc,
            xd,
            xi_val,
            ya,
            yb,
            yc,
            yd,
            yi_val,
            za,
            zb,
            zc,
            zd,
            zi_val,
            xi_val,
            yi_val,
            zi_val,
            zi_val,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Giá trị Q = 100a + 10b + c là một số nhỏ hơn / lớn hơn bound_q[cite: 24]
    if is_q_lt_bound:
        vdc_da_1_d = (
            "\\True Giá trị $Q = 100a + 10b + c$ là một số nhỏ hơn $%s$" % (bound_q)
        )
        vdc_da_1_s = (
            "Giá trị $Q = 100a + 10b + c$ là một số lớn hơn $%s$" % (bound_q)
        )
    else:
        vdc_da_1_d = (
            "\\True Giá trị $Q = 100a + 10b + c$ là một số lớn hơn $%s$" % (bound_q)
        )
        vdc_da_1_s = (
            "Giá trị $Q = 100a + 10b + c$ là một số nhỏ hơn $%s$" % (bound_q)
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi $I(%s;%s;%s)$ là điểm thỏa mãn $\\vec{IA} + \\vec{IB} + \\vec{IC} + 2\\vec{ID} = \\vec{0}$. \\\\ Khi đó với mọi điểm $M$, ta có: \\\\ $P = MA^2 + MB^2 + MC^2 + 2MD^2$ \\\\ $= (\\vec{MI} + \\vec{IA})^2 + (\\vec{MI} + \\vec{IB})^2 + (\\vec{MI} + \\vec{IC})^2 + 2(\\vec{MI} + \\vec{ID})^2$ \\\\ $= 5MI^2 + 2\\vec{MI} \\cdot (\\vec{IA} + \\vec{IB} + \\vec{IC} + 2\\vec{ID}) + (IA^2 + IB^2 + IC^2 + 2ID^2)$ \\\\ $= 5MI^2 + IA^2 + IB^2 + IC^2 + 2ID^2$. \\\\ Vì các điểm $A, B, C, D, I$ cố định nên $IA^2 + IB^2 + IC^2 + 2ID^2$ không đổi. \\\\ Do đó biểu thức $P$ đạt giá trị nhỏ nhất khi và chỉ khi $5MI^2$ nhỏ nhất $\\Leftrightarrow MI = 0 \\Leftrightarrow M \\equiv I(%s;%s;%s)$. \\\\ Suy ra tọa độ điểm $M(a;b;c)$ là $a = %s, b = %s, c = %s$. \\\\ Khi đó giá trị của biểu thức $Q$ là: \\\\ $Q = 100a + 10b + c = 100 \\cdot (%s) + 10 \\cdot (%s) + (%s) = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            xi_val,
            yi_val,
            zi_val,
            xi_val,
            yi_val,
            zi_val,
            a_val,
            b_val,
            c_val,
            a_val,
            b_val,
            c_val,
            val_q,
            val_q,
            "<" if is_q_lt_bound else ">",
            bound_q,
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
    