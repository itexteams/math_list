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


def bt_dang45_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    while True:
        xa = random.randint(1, 3)
        ya = random.randint(2, 4)
        za = 0
    
        xd = xa
        yd = ya + random.choice([1, 2, -1, -2])
        zd = 0
    
        xc = random.randint(-2, 0)
        yc = random.randint(1, 3)
        zc = 0
    
        # B nằm ngoài mặt phẳng (Oxy) để tạo hình học không gian
        xb = random.randint(0, 3)
        yb = random.randint(1, 3)
        zb = random.choice([2, 3, 4])
    
        # AC = (xc - xa; yc - ya; 0)
        ac_x = xc - xa
        ac_y = yc - ya
    
        # CD = (xd - xc; yd - yc; 0)
        cd_x = xd - xc
        cd_y = yd - yc
        cd_z = 0
    
        # AB = (xb - xa; yb - ya; zb - za)
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        # Tính trực tâm H(x0; y0; z0) của tam giác ACD:
        # Do tam giác ACD nằm trong (Oxy) nên z0 = 0
        # AD song song với Oy (do xd = xa) nên đường cao từ C vuông góc AD có phương trình: y = yc => y0 = yc
        # Đường cao kẻ từ D vuông góc với AC có VTPT là AC(ac_x; ac_y):
        # ac_x * (x - xd) + ac_y * (y - yd) = 0
        # Thay y = yc vào: ac_x * (x0 - xd) + ac_y * (yc - yd) = 0
        # x0 = xd - ac_y * (yc - yd) / ac_x
        if ac_x != 0:
            x0_val = Rational(xd, 1) - Rational(ac_y * (yc - yd), ac_x)
            y0_val = Rational(yc, 1)
            z0_val = 0
    
            # Biểu thức T = k_mul * x0 - y0 + 2026 * z0 với k_mul = ac_x
            # ac_x * x0 = ac_x * xd - ac_y * (yc - yd) => ac_x * x0 - y0 là số nguyên!
            k_mul = abs(ac_x)
            val_expr_d = k_mul * x0_val - y0_val
            if val_expr_d.q == 1 and val_expr_d.p > 0:
                val_target_d = int(val_expr_d.p)
                break
    
    # 1. Trọng tâm G của tam giác ABC
    xg_num = xa + xb + xc
    yg_num = ya + yb + yc
    zg_num = za + zb + zc
    
    str_xg_true = format_fraction_latex(xg_num, 3)
    str_yg_true = format_fraction_latex(yg_num, 3)
    str_zg_true = format_fraction_latex(zg_num, 3)
    
    str_xg_false = format_fraction_latex(xg_num + random.choice([-1, 1]), 3)
    
    # 2. Góc giữa 2 vectơ AB và CD
    dot_ab_cd = ab_x * cd_x + ab_y * cd_y + ab_z * cd_z
    len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
    len_cd_sq = cd_x**2 + cd_y**2 + cd_z**2
    
    cos_val = dot_ab_cd / (math.sqrt(len_ab_sq) * math.sqrt(len_cd_sq))
    # Giới hạn miền giá trị cos_val
    cos_val = max(-1.0, min(1.0, cos_val))
    angle_rad = math.acos(cos_val)
    angle_deg = math.degrees(angle_rad)
    
    # Làm tròn góc đến độ nguyên bằng ROUND_HALF_UP
    angle_rounded = int(
        Decimal(str(angle_deg)).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    )
    angle_false = (
        angle_rounded + random.choice([-3, -2, 2, 3])
        if angle_rounded + 2 <= 180
        else angle_rounded - 3
    )
    
    # 3. Điểm E thỏa mãn 2*EA + 4*EB - 3*EC = 0 <=> 3*OE = 2*OA + 4*OB - 3*OC
    xe_num = 2 * xa + 4 * xb - 3 * xc
    ye_num = 2 * ya + 4 * yb - 3 * yc
    ze_num = 2 * za + 4 * zb - 3 * zc
    
    str_xe_true = format_fraction_latex(xe_num, 3)
    str_ye_true = format_fraction_latex(ye_num, 3)
    str_ze_true = format_fraction_latex(ze_num, 3)
    
    # Điểm E sai (ví dụ đổi dấu cao độ hoặc lệch tọa độ)
    str_ze_false = format_fraction_latex(-ze_num, 3)
    
    # 4. Trực tâm H của tam giác ACD: k_mul * x0 - y0 + 2026 * z0 = val_target_d
    val_target_d_false = val_target_d + random.choice([-2, -1, 1, 2])
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho bốn điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$ và $D(%s;%s;%s)$. Xét tính đúng sai của các mệnh đề sau:"""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xd, yd, zd)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Trọng tâm của tam giác ABC
    nb_da_1_d = (
        "\\True Trọng tâm của tam giác $ABC$ là điểm $G\\left(%s;%s;%s\\right)$"
        % (str_xg_true, str_yg_true, str_zg_true)
    )
    nb_da_1_s = (
        "Trọng tâm của tam giác $ABC$ là điểm $G\\left(%s;%s;%s\\right)$"
        % (str_xg_false, str_yg_true, str_zg_true)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ trọng tâm $G$ của tam giác $ABC$ được tính theo công thức: \\\\ $\\begin{cases} x_G = \\frac{x_A + x_B + x_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ y_G = \\frac{y_A + y_B + y_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\end{cases} \\Rightarrow G\\left(%s;%s;%s\\right)$."""
        % (
            xa,
            xb,
            xc,
            str_xg_true,
            ya,
            yb,
            yc,
            str_yg_true,
            za,
            zb,
            zc,
            str_zg_true,
            str_xg_true,
            str_yg_true,
            str_zg_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Góc giữa 2 vectơ AB và CD
    th_da_1_d = (
        "\\True Góc giữa hai vectơ $\\vec{AB}$ và $\\vec{CD}$ xấp xỉ bằng $%s^\\circ$"
        % (angle_rounded)
    )
    th_da_1_s = (
        "Góc giữa hai vectơ $\\vec{AB}$ và $\\vec{CD}$ xấp xỉ bằng $%s^\\circ$"
        % (angle_false)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s) \\Rightarrow |\\vec{AB}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $\\vec{CD} = (x_D - x_C; y_D - y_C; z_D - z_C) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s) \\Rightarrow |\\vec{CD}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Tích vô hướng của hai vectơ $\\vec{AB}$ và $\\vec{CD}$ là: \\\\ $\\vec{AB} \\cdot \\vec{CD} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Khi đó: \\\\ $\\cos(\\vec{AB}, \\vec{CD}) = \\frac{\\vec{AB} \\cdot \\vec{CD}}{|\\vec{AB}| \\cdot |\\vec{CD}|} = \\frac{%s}{\\sqrt{%s} \\cdot \\sqrt{%s}} \\approx %s$. \\\\ Suy ra $(\\vec{AB}, \\vec{CD}) \\approx %s^\\circ$."""
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
            len_ab_sq,
            xd,
            xc,
            yd,
            yc,
            zd,
            zc,
            cd_x,
            cd_y,
            cd_z,
            cd_x,
            cd_y,
            cd_z,
            len_cd_sq,
            ab_x,
            cd_x,
            ab_y,
            cd_y,
            ab_z,
            cd_z,
            dot_ab_cd,
            dot_ab_cd,
            len_ab_sq,
            len_cd_sq,
            str(round(cos_val, 4)).replace(".", ","),
            angle_rounded,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Điểm E thỏa mãn 2*EA + 4*EB - 3*EC = 0
    vd_da_1_d = (
        "\\True Điểm $E$ thỏa mãn $2\\vec{EA} + 4\\vec{EB} - 3\\vec{EC} = \\vec{0}$ thì $E\\left(%s;%s;%s\\right)$"
        % (str_xe_true, str_ye_true, str_ze_true)
    )
    vd_da_1_s = (
        "Điểm $E$ thỏa mãn $2\\vec{EA} + 4\\vec{EB} - 3\\vec{EC} = \\vec{0}$ thì $E\\left(%s;%s;%s\\right)$"
        % (str_xe_true, str_ye_true, str_ze_false)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có hệ thức vectơ: \\\\ $2\\vec{EA} + 4\\vec{EB} - 3\\vec{EC} = \\vec{0} \\Leftrightarrow 2(\\vec{OA} - \\vec{OE}) + 4(\\vec{OB} - \\vec{OE}) - 3(\\vec{OC} - \\vec{OE}) = \\vec{0}$ \\\\ $\\Leftrightarrow 3\\vec{OE} = 2\\vec{OA} + 4\\vec{OB} - 3\\vec{OC} \\Leftrightarrow \\vec{OE} = \\frac{2\\vec{OA} + 4\\vec{OB} - 3\\vec{OC}}{3}$. \\\\ Tọa độ điểm $E$ thỏa mãn: \\\\ $\\begin{cases} x_E = \\frac{2x_A + 4x_B - 3x_C}{3} = \\frac{2 \\cdot (%s) + 4 \\cdot (%s) - 3 \\cdot (%s)}{3} = %s \\\\ y_E = \\frac{2y_A + 4y_B - 3y_C}{3} = \\frac{2 \\cdot (%s) + 4 \\cdot (%s) - 3 \\cdot (%s)}{3} = %s \\\\ z_E = \\frac{2z_A + 4z_B - 3z_C}{3} = \\frac{2 \\cdot (%s) + 4 \\cdot (%s) - 3 \\cdot (%s)}{3} = %s \\end{cases} \\Rightarrow E\\left(%s;%s;%s\\right)$."""
        % (
            xa,
            xb,
            xc,
            str_xe_true,
            ya,
            yb,
            yc,
            str_ye_true,
            za,
            zb,
            zc,
            str_ze_true,
            str_xe_true,
            str_ye_true,
            str_ze_true,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Trực tâm H(x0; y0; z0) của tam giác ACD thì k_mul*x0 - y0 + 2026*z0 = val_target_d
    vdc_da_1_d = (
        "\\True Gọi $H(x_0;y_0;z_0)$ là trực tâm của tam giác $ACD$ thì $%sx_0 - y_0 + 2026z_0 = %s$"
        % (k_mul, val_target_d)
    )
    vdc_da_1_s = (
        "Gọi $H(x_0;y_0;z_0)$ là trực tâm của tam giác $ACD$ thì $%sx_0 - y_0 + 2026z_0 = %s$"
        % (k_mul, val_target_d_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_x0 = format_fraction_latex(x0_val.p, x0_val.q)
    str_y0 = format_fraction_latex(y0_val.p, y0_val.q)
    
    loigiai_vdc_1 = (
        """Nhận xét: Ba điểm $A(%s;%s;0), C(%s;%s;0), D(%s;%s;0)$ đều có cao độ bằng $0$ nên tam giác $ACD$ nằm hoàn toàn trong mặt phẳng tọa độ $(Oxy)$. \\\\ Do đó trực tâm $H(x_0;y_0;z_0)$ của tam giác $ACD$ cũng thuộc mặt phẳng $(Oxy)$, suy ra $z_0 = 0$. \\\\ Ta có: \\\\ $\\vec{AD} = (x_D - x_A; y_D - y_A; 0) = (0; %s; 0) \\Rightarrow AD // Oy$. \\\\ Vì $H$ là trực tâm tam giác $ACD$ nên đường cao $CH \\perp AD$. \\\\ Do $AD // Oy$ nên đường cao $CH$ song song hoặc trùng với trục $Ox$, phương trình là $y = y_C = %s$, suy ra $y_0 = %s$. \\\\ Mặt khác, đường cao kẻ từ đỉnh $D$ vuông góc với cạnh $AC$, tức là $DH \\perp AC \\Leftrightarrow \\vec{DH} \\cdot \\vec{AC} = 0$. \\\\ Ta có $\\vec{AC} = (%s; %s; 0)$ và $\\vec{DH} = (x_0 - %s; y_0 - (%s); 0) = (x_0 - %s; %s - (%s); 0) = (x_0 - %s; %s; 0)$. \\\\ Khi đó: \\\\ $\\vec{DH} \\cdot \\vec{AC} = 0 \\Leftrightarrow (%s)(x_0 - %s) + (%s)(%s) = 0$ \\\\ $\\Leftrightarrow %s x_0 + (%s) = 0 \\Leftrightarrow x_0 = %s$. \\\\ Vậy trực tâm $H$ có tọa độ $H\\left(%s;%s;0\\right)$. \\\\ Khi đó giá trị của biểu thức là: \\\\ $%sx_0 - y_0 + 2026z_0 = %s \\cdot \\left(%s\\right) - (%s) + 2026 \\cdot 0 = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            xa,
            ya,
            xc,
            yc,
            xd,
            yd,
            yd - ya,
            yc,
            str_y0,
            ac_x,
            ac_y,
            xd,
            yd,
            xd,
            str_y0,
            yd,
            xd,
            yc - yd,
            ac_x,
            xd,
            ac_y,
            yc - yd,
            ac_x,
            -ac_x * xd + ac_y * (yc - yd),
            str_x0,
            str_x0,
            str_y0,
            k_mul,
            k_mul,
            str_x0,
            str_y0,
            val_target_d,
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
    