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


def bt_dang30_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai điểm A, B sao cho:
    # 1. OA vuông góc OB (tam giác OAB vuông tại O)
    # 2. OA = 3*k, OB = 4*k hoặc các bộ số Pythagore đẹp để cao độ tâm nội tiếp I bằng 0
    while True:
        # Chọn tỉ lệ cơ bản k_scale
        k_scale = random.choice([1, 2])
    
        # Chọn vectơ đơn vị hoặc trực giao cho OA và OB
        # Để z_I = (OB * zA + OA * zB) / (OA + OB + AB) = 0
        # Cần: OB * zA + OA * zB = 0 <=> zB / zA = - OB / OA
        # Ở bài gốc: OA = 3, OB = 4 => zB / zA = - 4/3.
        # Với zA = -2*k_scale => zB = 8/3 * k_scale
        l_oa = 3 * k_scale
        l_ob = 4 * k_scale
        l_ab = 5 * k_scale
    
        # Chọn A: xA^2 + yA^2 + zA^2 = (3*k_scale)^2 = 9*k_scale^2
        # Với k_scale = 1: 1^2 + 2^2 + (-2)^2 = 9
        s = k_scale
        xa = random.choice([-1, 1]) * s
        ya = random.choice([-2, 2]) * s
        za = -2 * s
    
        # OA . OB = 0 và |OB| = 4*s, zB = 8/3 * s
        # xA*xB + yA*yB + zA*zB = 0 <=> xa*xB + ya*yB = - za*zB = -(-2s)*(8s/3) = 16s^2/3
        # Chọn xB, yB dạng phân số có mẫu là 3: xB = X/3, yB = Y/3
        # X*xa + Y*ya = 16s^2, và X^2 + Y^2 + (8s)^2 = (12s)^2 = 144s^2 => X^2 + Y^2 = 80s^2
        # Thử nghiệm với xa = 1*s, ya = 2*s: X + 2Y = 16s, X^2 + Y^2 = 80s^2
        # X = 16s - 2Y => (16s - 2Y)^2 + Y^2 = 80s^2 => 5Y^2 - 64s Y + 176s^2 = 0
        # (5Y - 44s)(Y - 4s) = 0 => Y = 4s => X = 8s
        # Khi đó xB = 8s/3, yB = 4s/3, zB = 8s/3
        sign_x = 1 if xa > 0 else -1
        sign_y = 1 if ya > 0 else -1
    
        xb_num = 8 * s * sign_x
        yb_num = 4 * s * sign_y
        zb_num = 8 * s
    
        xb_val = Rational(xb_num, 3)
        yb_val = Rational(yb_num, 3)
        zb_val = Rational(zb_num, 3)
    
        # Kiểm tra lại OA . OB = 0
        dot_oa_ob = xa * xb_val + ya * yb_val + za * zb_val
        if dot_oa_ob == 0:
            break
    
    str_xb = format_fraction_latex(xb_num, 3)
    str_yb = format_fraction_latex(yb_num, 3)
    str_zb = format_fraction_latex(zb_num, 3)
    
    # 1. Mệnh đề a: OA vuông góc OB
    is_oa_perp_ob = True
    
    # 2. Mệnh đề b: Chân đường cao H(a; b; c) kẻ từ O xuống AB
    # Trong tam giác vuông OAB: AH = OA^2 / AB = (9 * s^2) / (5 * s) = 9/5 * s
    # Vectơ AH = (AH / AB) * vecto AB = (9/25) * vecto AB
    # H = A + 9/25 * (B - A)
    ab_vec_x = xb_val - xa
    ab_vec_y = yb_val - ya
    ab_vec_z = zb_val - za
    
    h_a = xa + Rational(9, 25) * ab_vec_x
    h_b = ya + Rational(9, 25) * ab_vec_y
    h_c = za + Rational(9, 25) * ab_vec_z
    
    val_expr_h = h_a + h_b - h_c
    str_val_h_true = format_fraction_latex(val_expr_h.p, val_expr_h.q)
    target_int_h = int(val_expr_h)  # Giá trị làm tròn hoặc số nguyên để tạo bẫy
    
    # 3. Mệnh đề c: N in (Oyz) cách đều O, A, B: N(0; y; z)
    # NO^2 = y^2 + z^2
    # NA^2 = xa^2 + (y - ya)^2 + (z - za)^2 = y^2 + z^2 - 2*ya*y - 2*za*z + (xa^2 + ya^2 + za^2)
    # NO = NA <=> 2*ya*y + 2*za*z = l_oa^2 = 9*s^2
    # NO = NB <=> 2*yb_val*y + 2*zb_val*z = l_ob^2 = 16*s^2
    eq1_y_coef = 2 * ya
    eq1_z_coef = 2 * za
    eq1_rhs = l_oa**2
    
    eq2_y_coef = 2 * yb_val
    eq2_z_coef = 2 * zb_val
    eq2_rhs = l_ob**2
    
    det_system = eq1_y_coef * eq2_z_coef - eq1_z_coef * eq2_y_coef
    det_y = eq1_rhs * eq2_z_coef - eq1_z_coef * eq2_rhs
    det_z = eq1_y_coef * eq2_rhs - eq1_rhs * eq2_y_coef
    
    yn_val = Rational(det_y, det_system)
    zn_val = Rational(det_z, det_system)
    
    str_yn = format_fraction_latex(yn_val.p, yn_val.q)
    is_yn_integer = yn_val.q == 1
    
    # 4. Mệnh đề d: Tâm đường tròn nội tiếp I của tam giác OAB:
    # I = (AB * O + OB * A + OA * B) / (OA + OB + AB)
    # z_I = (l_ob * za + l_oa * zb_val) / (l_oa + l_ob + l_ab)
    # Vì l_ob * za + l_oa * zb_val = (4s)*(-2s) + (3s)*(8s/3) = -8s^2 + 8s^2 = 0
    # nên z_I = 0 => I thuộc (Oxy) luôn Đúng!
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$ cho điểm $A(%s;%s;%s)$ và điểm $B\\left(%s;%s;%s\\right)$."""
        % (xa, ya, za, str_xb, str_yb, str_zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: OA vuông góc OB
    nb_da_1_d = "\\True $OA \\perp OB$"
    nb_da_1_s = "$OA$ không vuông góc với $OB$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ hai vectơ: \\\\ $\\vec{OA} = (%s;%s;%s)$, $\\vec{OB} = \\left(%s;%s;%s\\right)$. \\\\ Xét tích vô hướng của hai vectơ $\\vec{OA}$ và $\\vec{OB}$: \\\\ $\\vec{OA} \\cdot \\vec{OB} = (%s) \\cdot \\left(%s\\right) + (%s) \\cdot \\left(%s\\right) + (%s) \\cdot \\left(%s\\right) = 0$. \\\\ Vì $\\vec{OA} \\cdot \\vec{OB} = 0$ nên $OA \\perp OB$."""
        % (
            xa,
            ya,
            za,
            str_xb,
            str_yb,
            str_zb,
            xa,
            str_xb,
            ya,
            str_yb,
            za,
            str_zb,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Chân đường cao H(a; b; c) kẻ từ O xuống AB thì a + b - c = target_int_h
    th_da_1_d = (
        "\\True $H(a;b;c)$ là chân đường cao kẻ từ $O$ xuống $AB$ thì $a + b - c = %s$"
        % (str_val_h_true)
    )
    th_da_1_s = (
        "$H(a;b;c)$ là chân đường cao kẻ từ $O$ xuống $AB$ thì $a + b - c = %s$"
        % (target_int_h)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    str_ha = format_fraction_latex(h_a.p, h_a.q)
    str_hb = format_fraction_latex(h_b.p, h_b.q)
    str_hc = format_fraction_latex(h_c.p, h_c.q)
    
    loigiai_th_1 = (
        """Tam giác $OAB$ vuông tại $O$ có $OA = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s$, $OB = \\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2 + \\left(%s\\right)^2} = %s$. \\\\ Độ dài cạnh huyền: $AB = \\sqrt{OA^2 + OB^2} = \\sqrt{%s^2 + %s^2} = %s$. \\\\ Vì $H$ là hình chiếu của $O$ lên $AB$ nên trong tam giác vuông $OAB$ ta có: \\\\ $AH = \\frac{OA^2}{AB} = \\frac{%s^2}{%s} = %s$. \\\\ Suy ra $\\vec{AH} = \\frac{AH}{AB} \\vec{AB} = \\frac{9}{25} \\vec{AB}$. \\\\ Ta có $\\vec{AB} = \\left(%s;%s;%s\\right)$, do đó tọa độ của điểm $H(a;b;c)$ là: \\\\ $H = A + \\frac{9}{25} \\vec{AB} \\Rightarrow H\\left(%s;%s;%s\\right)$. \\\\ Khi đó: $a + b - c = %s + %s - \\left(%s\\right) = %s$. \\\\ Vì $%s \\neq %s$ nên khẳng định $a + b - c = %s$ là %s."""
        % (
            xa,
            ya,
            za,
            l_oa,
            str_xb,
            str_yb,
            str_zb,
            l_ob,
            l_oa,
            l_ob,
            l_ab,
            l_oa,
            l_ab,
            format_fraction_latex(9 * s, 5),
            format_fraction_latex(ab_vec_x.p, ab_vec_x.q),
            format_fraction_latex(ab_vec_y.p, ab_vec_y.q),
            format_fraction_latex(ab_vec_z.p, ab_vec_z.q),
            str_ha,
            str_hb,
            str_hc,
            str_ha,
            str_hb,
            str_hc,
            str_val_h_true,
            str_val_h_true,
            target_int_h,
            target_int_h,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: N in (Oyz) cách đều O, A, B có tung độ là số nguyên
    if is_yn_integer:
        vd_da_1_d = (
            "\\True $N \\in (Oyz)$ cách đều $3$ điểm $O, A, B$ có tung độ là số nguyên"
        )
        vd_da_1_s = (
            "$N \\in (Oyz)$ cách đều $3$ điểm $O, A, B$ có tung độ không phải là số nguyên"
        )
    else:
        vd_da_1_d = (
            "\\True $N \\in (Oyz)$ cách đều $3$ điểm $O, A, B$ có tung độ không phải là số nguyên"
        )
        vd_da_1_s = (
            "$N \\in (Oyz)$ cách đều $3$ điểm $O, A, B$ có tung độ là số nguyên"
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    str_zn = format_fraction_latex(zn_val.p, zn_val.q)
    
    loigiai_vd_1 = (
        """Vì điểm $N \\in (Oyz)$ nên tọa độ của điểm $N$ có dạng $N(0;y;z)$. \\\\ Điểm $N$ cách đều ba điểm $O, A, B$ khi và chỉ khi: \\\\ $\\begin{cases} NO^2 = NA^2 \\\\ NO^2 = NB^2 \\end{cases} \\Leftrightarrow \\begin{cases} y^2 + z^2 = (0 - (%s))^2 + (y - (%s))^2 + (z - (%s))^2 \\\\ y^2 + z^2 = \\left(0 - %s\\right)^2 + \\left(y - %s\\right)^2 + \\left(z - %s\\right)^2 \\end{cases}$ \\\\ $\\Leftrightarrow \\begin{cases} %sy + %sz = %s \\\\ %sy + %sz = %s \\end{cases} \\Leftrightarrow \\begin{cases} y = %s \\\\ z = %s \\end{cases} \\Rightarrow N\\left(0;%s;%s\\right)$. \\\\ Vì tung độ $y_N = %s$ %s số nguyên nên mệnh đề là %s."""
        % (
            xa,
            ya,
            za,
            str_xb,
            str_yb,
            str_zb,
            eq1_y_coef,
            eq1_z_coef,
            eq1_rhs,
            format_fraction_latex(eq2_y_coef.p, eq2_y_coef.q),
            format_fraction_latex(eq2_z_coef.p, eq2_z_coef.q),
            eq2_rhs,
            str_yn,
            str_zn,
            str_yn,
            str_zn,
            str_yn,
            "là" if is_yn_integer else "không phải là",
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tâm đường tròn nội tiếp I của tam giác OAB thì I in (Oxy)
    vdc_da_1_d = (
        "\\True Gọi $I$ là tâm đường tròn nội tiếp tam giác $OAB$ thì $I \\in (Oxy)$"
    )
    vdc_da_1_s = (
        "Gọi $I$ là tâm đường tròn nội tiếp tam giác $OAB$ thì $I \\notin (Oxy)$"
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Theo tính chất tâm đường tròn nội tiếp tam giác trong hình học giải tích, tọa độ tâm nội tiếp $I$ của tam giác $OAB$ thỏa mãn đẳng thức vectơ: \\\\ $AB \\cdot \\vec{IO} + OB \\cdot \\vec{IA} + OA \\cdot \\vec{IB} = \\vec{0}$ \\\\ $\\Rightarrow I = \\frac{AB \\cdot O + OB \\cdot A + OA \\cdot B}{OA + OB + AB} = \\frac{%s \\cdot A + %s \\cdot B}{%s + %s + %s} = \\frac{%s A + %s B}{%s}$. \\\\ Xét cao độ của điểm $I$: \\\\ $z_I = \\frac{%s \\cdot z_A + %s \\cdot z_B}{%s} = \\frac{%s \\cdot (%s) + %s \\cdot \\left(%s\\right)}{%s} = \\frac{%s + (%s)}{%s} = 0$. \\\\ Vì $z_I = 0$ nên điểm $I$ thuộc mặt phẳng tọa độ $(Oxy)$. \\\\ Do đó mệnh đề khẳng định $I \\in (Oxy)$ là đúng."""
        % (
            l_ob,
            l_oa,
            l_oa,
            l_ob,
            l_ab,
            l_ob,
            l_oa,
            l_oa + l_ob + l_ab,
            l_ob,
            l_oa,
            l_oa + l_ob + l_ab,
            l_ob,
            za,
            l_oa,
            str_zb,
            l_oa + l_ob + l_ab,
            l_ob * za,
            Rational(l_oa * zb_num, 3),
            l_oa + l_ob + l_ab,
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
    