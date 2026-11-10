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


def bt_dang75_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C không thẳng hàng[cite: 24]
    # Đảm bảo:
    # 1. Điểm A có zA != 0 để khoảng cách d(A, (Oxy)) = |zA| > 0[cite: 24]
    # 2. Trọng tâm G: zG = (zA + zB + zC)/3 có thể nguyên hoặc không nguyên[cite: 24]
    # 3. Biểu thức T = 3*MA^2 + 2*MB^2 - MC^2 đạt giá trị nhỏ nhất khi M trùng I thỏa mãn 3*IA + 2*IB - IC = 0[cite: 24]
    #    => 4*OI = 3*OA + 2*OB - OC => I = (3*A + 2*B - C) / 4[cite: 24]
    while True:
        xa = random.randint(-2, 2)
        ya = random.randint(-2, 2)
        za = random.choice([-2, -1, 1, 2])
    
        xb = random.randint(-2, 2)
        yb = random.randint(-2, 2)
        zb = random.randint(-2, 2)
    
        xc = random.randint(-2, 2)
        yc = random.randint(-2, 2)
        zc = random.randint(-2, 2)
    
        # AB và AC[cite: 24]
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        # Tích có hướng để kiểm tra A, B, C không thẳng hàng[cite: 24]
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        if (cp_x != 0 or cp_y != 0 or cp_z != 0) and (xa, ya, za) != (xb, yb, zb):
            # Tích vô hướng AB . AC[cite: 24]
            dot_ab_ac = ab_x * ac_x + ab_y * ac_y + ab_z * ac_z
    
            # Trọng tâm G[cite: 24]
            sum_z_g = za + zb + zc
            is_zg_integer = (sum_z_g % 3 == 0)
    
            # Tọa độ điểm M = (3*A + 2*B - C) / 4[cite: 24]
            xm_num = 3 * xa + 2 * xb - xc
            ym_num = 3 * ya + 2 * yb - yc
            zm_num = 3 * za + 2 * zb - zc
    
            dist_a_oxy = abs(za)
            break
    
    # 1. Khẳng định a: Điểm A cách mặt phẳng (Oxy) một khoảng bằng dist_a_oxy[cite: 24]
    dist_a_oxy_false = dist_a_oxy + random.choice([-1, 1])
    if dist_a_oxy_false <= 0:
        dist_a_oxy_false = dist_a_oxy + 2
    
    # 2. Khẳng định b: Trọng tâm tam giác ABC có cao độ là số nguyên[cite: 24]
    # is_zg_integer đã xác định
    
    # 3. Khẳng định c: AB . AC = dot_ab_ac[cite: 24]
    dot_ab_ac_true = dot_ab_ac
    dot_ab_ac_false = dot_ab_ac + random.choice([-2, -1, 1, 2])
    
    # 4. Khẳng định d: Tọa độ điểm M[cite: 24]
    str_xm_true = format_fraction_latex(xm_num, 4)
    str_ym_true = format_fraction_latex(ym_num, 4)
    str_zm_true = format_fraction_latex(zm_num, 4)
    str_pt_m_true = "M\\left(%s;%s;%s\\right)" % (str_xm_true, str_ym_true, str_zm_true)
    
    # Đổi dấu một tọa độ để tạo phương án sai như mẫu[cite: 24]
    str_ym_false = format_fraction_latex(-ym_num if ym_num != 0 else 2, 4)
    str_zm_false = format_fraction_latex(-zm_num if zm_num != 0 else -4, 4)
    str_pt_m_false = "M\\left(%s;%s;%s\\right)" % (str_xm_true, str_ym_false, str_zm_false)
    if str_pt_m_false == str_pt_m_true:
        str_pt_m_false = "M\\left(-\\frac{3}{4};-\\frac{1}{2};1\\right)"[cite: 24]
    
    # Nội dung câu hỏi[cite: 24]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$. Điểm $M$ thỏa mãn điều kiện $3MA^2 + 2MB^2 - MC^2$ đạt giá trị nhỏ nhất."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Điểm A cách mặt phẳng (Oxy) một khoảng bằng dist_a_oxy[cite: 24]
    nb_da_1_d = (
        "\\True Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$"
        % (xa, ya, za, dist_a_oxy)
    )
    nb_da_1_s = (
        "Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$"
        % (xa, ya, za, dist_a_oxy_false)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng tọa độ $(Oxy)$ có phương trình là $z = 0$. \\\\ Khoảng cách từ điểm $A(%s;%s;%s)$ đến mặt phẳng $(Oxy)$ là: \\\\ $d(A, (Oxy)) = |z_A| = |%s| = %s$. \\\\ Do đó khẳng định là %s."""
        % (
            xa,
            ya,
            za,
            za,
            dist_a_oxy,
            "đúng" if "\\True" in nb_da_1 else "sai",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Trọng tâm tam giác ABC có cao độ là số nguyên[cite: 24]
    if is_zg_integer:
        th_da_1_d = "\\True Trọng tâm tam giác $ABC$ có cao độ là số nguyên"
        th_da_1_s = "Trọng tâm tam giác $ABC$ có cao độ không phải là số nguyên"
    else:
        th_da_1_d = "\\True Trọng tâm tam giác $ABC$ có cao độ không phải là số nguyên"
        th_da_1_s = "Trọng tâm tam giác $ABC$ có cao độ là số nguyên"
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    str_zg_val = format_fraction_latex(sum_z_g, 3)
    
    loigiai_th_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$. Cao độ của điểm $G$ là: \\\\ $z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s$. \\\\ Vì $%s$ %s số nguyên nên khẳng định là %s."""
        % (
            za,
            zb,
            zc,
            str_zg_val,
            str_zg_val,
            "là" if is_zg_integer else "không phải là",
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: AB . AC = dot_ab_ac[cite: 24]
    vd_da_1_d = "\\True $\\vec{AB} \\cdot \\vec{AC} = %s$" % (dot_ab_ac_true)
    vd_da_1_s = "$\\vec{AB} \\cdot \\vec{AC} = %s$" % (dot_ab_ac_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Tích vô hướng của hai vectơ $\\vec{AB}$ và $\\vec{AC}$ là: \\\\ $\\vec{AB} \\cdot \\vec{AC} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Do đó khẳng định là %s."""
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
            ab_x,
            ac_x,
            ab_y,
            ac_y,
            ab_z,
            ac_z,
            dot_ab_ac_true,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tọa độ điểm M[cite: 24]
    vdc_da_1_d = "\\True Tọa độ điểm $M$ là $%s$" % (str_pt_m_true)
    vdc_da_1_s = "Tọa độ điểm $M$ là $%s$" % (str_pt_m_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi điểm $I$ thỏa mãn hệ thức vectơ: \\\\ $3\\vec{IA} + 2\\vec{IB} - \\vec{IC} = \\vec{0} \\Leftrightarrow 3(\\vec{OA} - \\vec{OI}) + 2(\\vec{OB} - \\vec{OI}) - (\\vec{OC} - \\vec{OI}) = \\vec{0}$ \\\\ $\\Leftrightarrow 4\\vec{OI} = 3\\vec{OA} + 2\\vec{OB} - \\vec{OC} \\Leftrightarrow \\vec{OI} = \\frac{3\\vec{OA} + 2\\vec{OB} - \\vec{OC}}{4}$. \\\\ Tọa độ của điểm $I$ là: \\\\ $\\begin{cases} x_I = \\frac{3x_A + 2x_B - x_C}{4} = \\frac{3 \\cdot (%s) + 2 \\cdot (%s) - (%s)}{4} = %s \\\\ y_I = \\frac{3y_A + 2y_B - y_C}{4} = \\frac{3 \\cdot (%s) + 2 \\cdot (%s) - (%s)}{4} = %s \\\\ z_I = \\frac{3z_A + 2z_B - z_C}{4} = \\frac{3 \\cdot (%s) + 2 \\cdot (%s) - (%s)}{4} = %s \\end{cases} \\Rightarrow I\\left(%s;%s;%s\\right)$. \\\\ Khi đó với điểm $M$ bất kì, ta có: \\\\ $3MA^2 + 2MB^2 - MC^2 = 3(\\vec{MI} + \\vec{IA})^2 + 2(\\vec{MI} + \\vec{IB})^2 - (\\vec{MI} + \\vec{IC})^2$ \\\\ $= (3 + 2 - 1)MI^2 + 2\\vec{MI}(3\\vec{IA} + 2\\vec{IB} - \\vec{IC}) + (3IA^2 + 2IB^2 - IC^2)$ \\\\ $= 4MI^2 + (3IA^2 + 2IB^2 - IC^2)$. \\\\ Do $A, B, C$ và $I$ cố định nên $3IA^2 + 2IB^2 - IC^2$ không đổi, vì vậy biểu thức đạt giá trị nhỏ nhất khi và chỉ khi: \\\\ $MI^2 = 0 \\Leftrightarrow M \\equiv I \\Rightarrow %s$. \\\\ Do đó khẳng định là %s."""
        % (
            xa,
            xb,
            xc,
            str_xm_true,
            ya,
            yb,
            yc,
            str_ym_true,
            za,
            zb,
            zc,
            str_zm_true,
            str_xm_true,
            str_ym_true,
            str_zm_true,
            str_pt_m_true,
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
    