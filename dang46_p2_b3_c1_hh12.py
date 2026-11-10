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


def bt_dang46_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C không thẳng hàng
    while True:
        xa = random.randint(1, 4)
        ya = random.randint(1, 4)
        za = random.randint(2, 5)
    
        xb = random.randint(-1, 2)
        yb = random.randint(0, 3)
        zb = random.randint(0, 3)
    
        # Chọn BC có tỉ lệ đẹp
        bc_x = random.choice([2, 3, -2, -3])
        bc_y = random.choice([-3, -2, 2, 3])
        bc_z = random.choice([2, 3, -2, -3])
    
        xc = xb + bc_x
        yc = yb + bc_y
        zc = zb + bc_z
    
        # Vectơ AB, AC
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        # Tích có hướng [AB, AC] để tính diện tích
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        cp_sq = cp_x**2 + cp_y**2 + cp_z**2
        len_bc_sq = bc_x**2 + bc_y**2 + bc_z**2
    
        # Chân đường cao H kẻ từ A xuống BC:
        # H = B + t * BC với t = (BA . BC) / |BC|^2 = - (AB . BC) / |BC|^2
        dot_ba_bc = (-ab_x) * bc_x + (-ab_y) * bc_y + (-ab_z) * bc_z
        t_val = Rational(dot_ba_bc, len_bc_sq)
    
        h_a = xb + t_val * bc_x
        h_b = yb + t_val * bc_y
        h_c = zb + t_val * bc_z
    
        # Biểu thức S = a + 2b - 5c
        s_expr_val = h_a + 2 * h_b - 5 * h_c
    
        if (
            cp_sq > 0
            and len_bc_sq > 0
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and s_expr_val.q == 1
        ):
            break
    
    # 1. Vectơ BC = (bc_x; bc_y; bc_z)[cite: 21]
    bc_x_s = bc_x
    bc_y_s = -bc_y if bc_y != 0 else 1
    bc_z_s = bc_z
    
    # 2. Trọng tâm G của tam giác ABC có tung độ y_G[cite: 21]
    yg_num = ya + yb + yc
    yg_val = Rational(yg_num, 3)
    bound_yg = 2
    is_yg_gt_2 = yg_val > bound_yg
    str_yg = format_fraction_latex(yg_num, 3)
    
    # 3. Diện tích tam giác PQR tạo bởi 3 trung điểm: S_PQR = 1/4 * S_ABC = 1/8 * sqrt(cp_sq)[cite: 21]
    # So sánh S_PQR với \sqrt{2}[cite: 21]
    s_pqr_sq = Rational(cp_sq, 64)
    s_pqr_val = math.sqrt(float(s_pqr_sq))
    bound_s = math.sqrt(2)
    is_s_gt_sqrt2 = s_pqr_val > bound_s
    
    # 4. Giá trị biểu thức S = a + 2b - 5c[cite: 21]
    val_s_int = int(s_expr_val.p)
    val_s_int_s = val_s_int + random.choice([-3, -2, 2, 3])
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho tam giác $ABC$ có tọa độ các đỉnh $A(%s;%s;%s), B(%s;%s;%s)$ và $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ BC[cite: 21]
    nb_da_1_d = "\\True $\\vec{BC} = (%s;%s;%s)$" % (bc_x, bc_y, bc_z)
    nb_da_1_s = "$\\vec{BC} = (%s;%s;%s)$" % (bc_x_s, bc_y_s, bc_z_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ của vectơ $\\vec{BC}$ là: \\\\ $\\vec{BC} = (x_C - x_B; y_C - y_B; z_C - z_B) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xc, xb, yc, yb, zc, zb, bc_x, bc_y, bc_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Trọng tâm G của tam giác có tung độ lớn hơn 2[cite: 21]
    if is_yg_gt_2:
        th_da_1_d = "\\True Trọng tâm $G$ của tam giác có tung độ lớn hơn $2$"
        th_da_1_s = "Trọng tâm $G$ của tam giác có tung độ nhỏ hơn $2$"
    else:
        th_da_1_d = "\\True Trọng tâm $G$ của tam giác có tung độ nhỏ hơn $2$"
        th_da_1_s = "Trọng tâm $G$ của tam giác có tung độ lớn hơn $2$"
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Tung độ trọng tâm $G$ của tam giác $ABC$ là: \\\\ $y_G = \\frac{y_A + y_B + y_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\approx %s$. \\\\ Vì $%s %s 2$ nên khẳng định là %s."""
        % (
            ya,
            yb,
            yc,
            str_yg,
            str(round(float(yg_val), 2)).replace(".", ","),
            str(round(float(yg_val), 2)).replace(".", ","),
            ">" if is_yg_gt_2 else "<",
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: P, Q, R lần lượt là trung điểm ba cạnh của tam giác thì S_PQR > \sqrt{2}[cite: 21]
    if is_s_gt_sqrt2:
        vd_da_1_d = (
            "\\True $P, Q, R$ lần lượt là trung điểm ba cạnh của tam giác thì $S_{PQR} > \\sqrt{2}$"
        )
        vd_da_1_s = (
            "$P, Q, R$ lần lượt là trung điểm ba cạnh của tam giác thì $S_{PQR} < \\sqrt{2}$"
        )
    else:
        vd_da_1_d = (
            "\\True $P, Q, R$ lần lượt là trung điểm ba cạnh của tam giác thì $S_{PQR} < \\sqrt{2}$"
        )
        vd_da_1_s = (
            "$P, Q, R$ lần lượt là trung điểm ba cạnh của tam giác thì $S_{PQR} > \\sqrt{2}$"
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s;%s;%s)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s;%s;%s)$. \\\\ Tích có hướng của hai vectơ $\\vec{AB}$ và $\\vec{AC}$ là: \\\\ $[\\vec{AB}, \\vec{AC}] = \\left( \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix} \\right) = (%s;%s;%s)$. \\\\ Diện tích tam giác $ABC$ là: \\\\ $S_{ABC} = \\frac{1}{2} \\left|[\\vec{AB}, \\vec{AC}]\\right| = \\frac{1}{2} \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\frac{\\sqrt{%s}}{2}$. \\\\ Vì $P, Q, R$ lần lượt là trung điểm của ba cạnh $AB, BC, CA$ nên tam giác $PQR$ đồng dạng với tam giác $ABC$ theo tỉ số $k = \\frac{1}{2}$. \\\\ Do đó tỉ số diện tích là: \\\\ $S_{PQR} = \\frac{1}{4} S_{ABC} = \\frac{\\sqrt{%s}}{8} \\approx %s$. \\\\ So sánh với $\\sqrt{2} \\approx 1,41$, ta thấy $%s %s \\sqrt{2}$ nên khẳng định là %s."""
        % (
            ab_x,
            ab_y,
            ab_z,
            ac_x,
            ac_y,
            ac_z,
            ab_y,
            ab_z,
            ac_y,
            ac_z,
            ab_z,
            ab_x,
            ac_z,
            ac_x,
            ab_x,
            ab_y,
            ac_x,
            ac_y,
            cp_x,
            cp_y,
            cp_z,
            cp_x,
            cp_y,
            cp_z,
            cp_sq,
            cp_sq,
            str(round(s_pqr_val, 2)).replace(".", ","),
            str(round(s_pqr_val, 2)).replace(".", ","),
            ">" if is_s_gt_sqrt2 else "<",
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm H(a;b;c) là chân đường cao đỉnh A. Giá trị S = a + 2b - 5c[cite: 21]
    vdc_da_1_d = (
        "\\True Điểm $H(a;b;c)$ là chân đường cao đỉnh $A$. Khi đó giá trị biểu thức $S = a + 2b - 5c$ bằng $%s$"
        % (val_s_int)
    )
    vdc_da_1_s = (
        "Điểm $H(a;b;c)$ là chân đường cao đỉnh $A$. Khi đó giá trị biểu thức $S = a + 2b - 5c$ bằng $%s$"
        % (val_s_int_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_ha = format_fraction_latex(h_a.p, h_a.q)
    str_hb = format_fraction_latex(h_b.p, h_b.q)
    str_hc = format_fraction_latex(h_c.p, h_c.q)
    str_t = format_fraction_latex(t_val.p, t_val.q)
    
    loigiai_vdc_1 = (
        """Đường thẳng $BC$ đi qua điểm $B(%s;%s;%s)$ và nhận vectơ $\\vec{BC} = (%s;%s;%s)$ làm vectơ chỉ phương. \\\\ Vì điểm $H$ thuộc đường thẳng $BC$ nên tọa độ điểm $H$ có dạng: \\\\ $H(%s + %st; %s + %st; %s + %st)$. \\\\ Khi đó vectơ $\\vec{AH}$ có tọa độ là: \\\\ $\\vec{AH} = (x_H - x_A; y_H - y_A; z_H - z_A) = (%s + %st; %s + %st; %s + %st)$. \\\\ Vì $H$ là chân đường cao kẻ từ đỉnh $A$ của tam giác $ABC$ nên $AH \\perp BC \\Leftrightarrow \\vec{AH} \\cdot \\vec{BC} = 0$: \\\\ $(%s)(%s + %st) + (%s)(%s + %st) + (%s)(%s + %st) = 0$ \\\\ $\\Leftrightarrow %st + (%s) = 0 \\Leftrightarrow t = %s$. \\\\ Thay giá trị $t = %s$ vào, ta được tọa độ của điểm $H(a;b;c)$ là: \\\\ $\\begin{cases} a = %s + (%s) \\cdot \\left(%s\\right) = %s \\\\ b = %s + (%s) \\cdot \\left(%s\\right) = %s \\\\ c = %s + (%s) \\cdot \\left(%s\\right) = %s \\end{cases} \\Rightarrow H\\left(%s;%s;%s\\right)$. \\\\ Khi đó giá trị của biểu thức $S = a + 2b - 5c$ là: \\\\ $S = %s + 2 \\cdot \\left(%s\\right) - 5 \\cdot \\left(%s\\right) = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            xb,
            yb,
            zb,
            bc_x,
            bc_y,
            bc_z,
            xb,
            bc_x,
            yb,
            bc_y,
            zb,
            bc_z,
            xb - xa,
            bc_x,
            yb - ya,
            bc_y,
            zb - za,
            bc_z,
            bc_x,
            xb - xa,
            bc_x,
            bc_y,
            yb - ya,
            bc_y,
            bc_z,
            zb - za,
            bc_z,
            len_bc_sq,
            -dot_ba_bc,
            str_t,
            str_t,
            xb,
            bc_x,
            str_t,
            str_ha,
            yb,
            bc_y,
            str_t,
            str_hb,
            zb,
            bc_z,
            str_t,
            str_hc,
            str_ha,
            str_hb,
            str_hc,
            str_ha,
            str_hb,
            str_hc,
            val_s_int,
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
    