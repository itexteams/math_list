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


def bt_dang34_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C sao cho tam giác ABC không suy biến
    # và các phép tính tọa độ M, N, D ra kết quả đẹp
    while True:
        xa = random.randint(-4, 4)
        ya = random.randint(-4, 4)
        za = random.randint(-3, 3)
    
        xb = random.randint(-4, 4)
        yb = random.randint(-4, 4)
        zb = random.randint(-3, 3)
    
        xc = random.randint(-4, 4)
        yc = random.randint(-4, 4)
        zc = random.randint(-3, 3)
    
        # Đảm bảo zC != zB để tìm được duy nhất điểm M trên Oz
        if zc == zb:
            continue
    
        # Kiểm tra ba điểm A, B, C không thẳng hàng
        ab_x, ab_y, ab_z = xb - xa, yb - ya, zb - za
        ac_x, ac_y, ac_z = xc - xa, yc - ya, zc - za
    
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        # Kiểm tra hệ phương trình tìm N(x; y; 0) trên (Oxy) có nghiệm duy nhất:
        # 2(xA - xB)x + 2(yA - yB)y = const1
        # 2(xB - xC)x + 2(yB - yC)y = const2
        det_n = 4 * ((xa - xb) * (yb - yc) - (ya - yb) * (xb - xc))
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and det_n != 0
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
        ):
            break
    
    # 1. Trọng tâm G của tam giác ABC[cite: 20]
    sum_xg = xa + xb + xc
    sum_yg = ya + yb + yc
    sum_zg = za + zb + zc
    
    str_xg = format_fraction_latex(sum_xg, 3)
    str_yg = format_fraction_latex(sum_yg, 3)
    str_zg = format_fraction_latex(sum_zg, 3)
    
    str_zg_s = format_fraction_latex(sum_zg + random.choice([-2, -1, 1, 2]), 3)
    
    # 2. Điểm M trên trục Oz cách đều B và C: M(0; 0; zm)[cite: 20]
    # MB^2 = MC^2 <=> xb^2 + yb^2 + (zm - zb)^2 = xc^2 + yc^2 + (zm - zc)^2
    # <=> 2(zc - zb)zm = (xc^2 + yc^2 + zc^2) - (xb^2 + yb^2 + zb^2)
    diff_sq = (xc**2 + yc**2 + zc**2) - (xb**2 + yb**2 + zb**2)
    zm_val = Rational(diff_sq, 2 * (zc - zb))
    
    str_zm = format_fraction_latex(zm_val.p, zm_val.q)
    str_zm_s = format_fraction_latex(zm_val.p + random.choice([-1, 1]), zm_val.q)
    
    # 3. Điểm N thuộc mặt phẳng (Oxy) cách đều ba điểm A, B, C: N(xn; yn; 0)[cite: 20]
    # NA^2 = NB^2 <=> 2(xa - xb)xn + 2(ya - yb)yn = (xb^2 + yb^2 + zb^2) - (xa^2 + ya^2 + za^2)
    # NB^2 = NC^2 <=> 2(xb - xc)xn + 2(yb - yc)yn = (xc^2 + yc^2 + zc^2) - (xb^2 + yb^2 + zb^2)
    eq1_c = (xb**2 + yb**2 + zb**2) - (xa**2 + ya**2 + za**2)
    eq2_c = (xc**2 + yc**2 + zc**2) - (xb**2 + yb**2 + zb**2)
    
    a11 = 2 * (xa - xb)
    a12 = 2 * (ya - yb)
    a21 = 2 * (xb - xc)
    a22 = 2 * (yb - yc)
    
    det_main = a11 * a22 - a12 * a21
    det_xn = (-eq1_c) * a22 - a12 * (-eq2_c)
    det_yn = a11 * (-eq2_c) - (-eq1_c) * a21
    
    xn_val = Rational(det_xn, det_main)
    yn_val = Rational(det_yn, det_main)
    
    str_xn = format_fraction_latex(xn_val.p, xn_val.q)
    str_yn = format_fraction_latex(yn_val.p, yn_val.q)
    
    # Tọa độ N sai (ví dụ làm tròn số nguyên hoặc đổi giá trị)[cite: 20]
    str_xn_s = "0"
    str_yn_s = "3"
    
    # 4. ABCD là hình thang có đáy AD và S_ABCD = 3 * S_ABC[cite: 20]
    # Do AD // BC nên khoảng cách từ A đến BC bằng khoảng cách từ D đến BC (cùng bằng h).
    # S_ABCD = S_ABC + S_ACD = 1/2 * (BC + AD) * h = 3 * S_ABC = 3 * (1/2 * BC * h)
    # <=> AD = 2 * BC
    # Để ABCD là hình thang thì hai đáy AD và BC cùng hướng: vecto AD = 2 * vecto BC
    # => D = A + 2 * vecto BC
    bc_x = xc - xb
    bc_y = yc - yb
    bc_z = zc - zb
    
    xd = xa + 2 * bc_x
    yd = ya + 2 * bc_y
    zd = za + 2 * bc_z
    
    sum_mnp = xd + yd + zd
    sum_mnp_s = sum_mnp + random.choice([-4, -2, 2, 4])
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho ba điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ trọng tâm của tam giác ABC[cite: 20]
    nb_da_1_d = (
        "\\True Tọa độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$"
        % (str_xg, str_yg, str_zg)
    )
    nb_da_1_s = (
        "Tọa độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$"
        % (str_xg, str_yg, str_zg_s)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$. Khi đó ta có: \\\\ $\\begin{cases} x_G = \\frac{x_A + x_B + x_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ y_G = \\frac{y_A + y_B + y_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\end{cases}$ \\\\ Vậy tọa độ trọng tâm của tam giác $ABC$ là $\\left(%s;%s;%s\\right)$."""
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
    # Mệnh đề b: Tọa độ điểm M trên trục Oz cách đều hai điểm B, C[cite: 20]
    th_da_1_d = (
        "\\True Tọa độ điểm $M$ trên trục $Oz$ cách đều hai điểm $B, C$ là $\\left(0;0;%s\\right)$"
        % (str_zm)
    )
    th_da_1_s = (
        "Tọa độ điểm $M$ trên trục $Oz$ cách đều hai điểm $B, C$ là $\\left(0;0;%s\\right)$"
        % (str_zm_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì điểm $M$ thuộc trục $Oz$ nên tọa độ của điểm $M$ có dạng $M(0;0;z)$. \\\\ Ta có: \\\\ $MB^2 = (0 - (%s))^2 + (0 - (%s))^2 + (z - (%s))^2 = z^2 - 2 \\cdot (%s)z + %s$. \\\\ $MC^2 = (0 - (%s))^2 + (0 - (%s))^2 + (z - (%s))^2 = z^2 - 2 \\cdot (%s)z + %s$. \\\\ Điểm $M$ cách đều hai điểm $B, C \\Leftrightarrow MB^2 = MC^2$ \\\\ $\\Leftrightarrow -2 \\cdot (%s)z + %s = -2 \\cdot (%s)z + %s \\Leftrightarrow z = %s$. \\\\ Vậy tọa độ điểm $M$ là $\\left(0;0;%s\\right)$."""
        % (
            xb,
            yb,
            zb,
            zb,
            xb**2 + yb**2 + zb**2,
            xc,
            yc,
            zc,
            zc,
            xc**2 + yc**2 + zc**2,
            zb,
            xb**2 + yb**2 + zb**2,
            zc,
            xc**2 + yc**2 + zc**2,
            str_zm,
            str_zm,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Tọa độ điểm N thuộc mặt phẳng (Oxy) cách đều ba điểm A, B, C[cite: 20]
    vd_da_1_d = (
        "\\True Tọa độ điểm $N$ thuộc mặt phẳng $(Oxy)$ cách đều ba điểm $A, B, C$ là $\\left(%s;%s;0\\right)$"
        % (str_xn, str_yn)
    )
    vd_da_1_s = (
        "Tọa độ điểm $N$ thuộc mặt phẳng $(Oxy)$ cách đều ba điểm $A, B, C$ là $(%s;%s;0)$"
        % (str_xn_s, str_yn_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì điểm $N$ thuộc mặt phẳng $(Oxy)$ nên tọa độ của điểm $N$ có dạng $N(x;y;0)$. \\\\ Điểm $N$ cách đều ba điểm $A, B, C$ khi và chỉ khi: \\\\ $\\begin{cases} NA^2 = NB^2 \\\\ NB^2 = NC^2 \\end{cases} \\Leftrightarrow \\begin{cases} (x - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2 = (x - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2 \\\\ (x - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2 = (x - (%s))^2 + (y - (%s))^2 + (0 - (%s))^2 \\end{cases}$ \\\\ Giải hệ hai phương trình bậc nhất hai ẩn $x, y$, ta được: \\\\ $\\begin{cases} x = %s \\\\ y = %s \\end{cases} \\Rightarrow N\\left(%s;%s;0\\right)$."""
        % (
            xa,
            ya,
            za,
            xb,
            yb,
            zb,
            xb,
            yb,
            zb,
            xc,
            yc,
            zc,
            str_xn,
            str_yn,
            str_xn,
            str_yn,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tọa độ điểm D để ABCD là hình thang có đáy AD và S_ABCD = 3 * S_ABC[cite: 20]
    vdc_da_1_d = (
        "\\True Tọa độ điểm $D$ để $ABCD$ là hình thang có đáy $AD$ và diện tích tứ giác $ABCD$ bằng $3$ lần diện tích tam giác $ABC$ là $D(m;n;p)$. Khi đó $m + n + p = %s$"
        % (sum_mnp)
    )
    vdc_da_1_s = (
        "Tọa độ điểm $D$ để $ABCD$ là hình thang có đáy $AD$ và diện tích tứ giác $ABCD$ bằng $3$ lần diện tích tam giác $ABC$ là $D(m;n;p)$. Khi đó $m + n + p = %s$"
        % (sum_mnp_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì $ABCD$ là hình thang có đáy $AD$ nên hai cạnh đáy $AD // BC$. \\\\ Khi đó khoảng cách từ $A$ đến đường thẳng $BC$ bằng khoảng cách từ $D$ đến đường thẳng $BC$, gọi khoảng cách này là $h$. \\\\ Diện tích hình thang $ABCD$ là: \\\\ $S_{ABCD} = \\frac{(AD + BC) \\cdot h}{2} = \\frac{AD \\cdot h}{2} + \\frac{BC \\cdot h}{2} = S_{ACD} + S_{ABC}$. \\\\ Theo giả thiết: $S_{ABCD} = 3 S_{ABC} \\Leftrightarrow S_{ACD} + S_{ABC} = 3 S_{ABC} \\Leftrightarrow S_{ACD} = 2 S_{ABC} \\Leftrightarrow AD = 2 BC$. \\\\ Vì $ABCD$ là hình thang với hai đáy $AD, BC$ nên hai vectơ $\\vec{AD}$ và $\\vec{BC}$ cùng hướng, do đó: \\\\ $\\vec{AD} = 2\\vec{BC}$. \\\\ Ta có $\\vec{BC} = (x_C - x_B; y_C - y_B; z_C - z_B) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Gọi $D(m;n;p)$, ta có: \\\\ $\\vec{AD} = (m - x_A; n - y_A; p - z_A) = (m - (%s); n - (%s); p - (%s))$. \\\\ Từ $\\vec{AD} = 2\\vec{BC}$, suy ra: \\\\ $\\begin{cases} m - (%s) = 2 \\cdot (%s) = %s \\\\ n - (%s) = 2 \\cdot (%s) = %s \\\\ p - (%s) = 2 \\cdot (%s) = %s \\end{cases} \\Leftrightarrow \\begin{cases} m = %s + (%s) = %s \\\\ n = %s + (%s) = %s \\\\ p = %s + (%s) = %s \\end{cases} \\Rightarrow D(%s;%s;%s)$. \\\\ Khi đó giá trị của $m + n + p = (%s) + (%s) + (%s) = %s$."""
        % (
            xc,
            xb,
            yc,
            yb,
            zc,
            zb,
            bc_x,
            bc_y,
            bc_z,
            xa,
            ya,
            za,
            xa,
            bc_x,
            2 * bc_x,
            ya,
            bc_y,
            2 * bc_y,
            za,
            bc_z,
            2 * bc_z,
            xa,
            2 * bc_x,
            xd,
            ya,
            2 * bc_y,
            yd,
            za,
            2 * bc_z,
            zd,
            xd,
            yd,
            zd,
            xd,
            yd,
            zd,
            sum_mnp,
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
    