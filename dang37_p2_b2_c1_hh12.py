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


def bt_dang37_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu tam giác ABC vuông tại A trong mặt phẳng y = y0[cite: 23]
    while True:
        xa = random.randint(-4, 4)
        y0 = random.randint(4, 7)  # y0 > 3 để phục vụ mệnh đề d[cite: 23]
        za = random.randint(-4, 2)
    
        # Chọn dx khác 0 và dz là số chẵn khác 0 để K có cao độ nguyên đẹp[cite: 23]
        dx = random.choice([-3, -2, -1, 1, 2, 3])
        dz = random.choice([-4, -2, 2, 4])
    
        xb = xa + dx
        yb = y0
        zb = za
    
        xc = xa
        yc = y0
        zc = za + dz
    
        # Cao độ trọng tâm G = za + dz/3, tính tổng z[cite: 23]
        sum_zg = za + zb + zc
        zg_val = Rational(sum_zg, 3)
    
        # Tránh trường hợp zg = 0 để khẳng định cao độ dương/âm rõ ràng[cite: 23]
        if zg_val != 0:
            break
    
    # 1. Trọng tâm G của tam giác ABC: zG = sum_zg / 3[cite: 23]
    is_zg_positive = zg_val > 0
    str_zg = format_fraction_latex(sum_zg, 3)
    
    # 2. cos B = |BA . BC| / (|BA| * |BC|)[cite: 23]
    # BA = (-dx; 0; 0), BC = (-dx; 0; dz)
    # BA . BC = dx^2, |BA| = |dx|, |BC| = sqrt(dx^2 + dz^2)
    # cos B = |dx| / sqrt(dx^2 + dz^2) = 1 / sqrt(1 + (dz/dx)^2)
    len_ba_sq = dx**2
    len_bc_sq = dx**2 + dz**2
    dot_ba_bc = dx**2
    
    # Giá trị chính xác của cos B dưới dạng căn thức
    cos_b_val = float(math.sqrt(len_ba_sq) / math.sqrt(len_bc_sq))
    
    # Chọn một mẫu số so sánh d_comp sao cho khẳng định cos B > 1/sqrt(d_comp) có tính đúng/sai rõ ràng[cite: 23]
    # Ta có cos B = sqrt(len_ba_sq / len_bc_sq)
    # Chọn d_comp:
    d_comp = len_bc_sq - 2 if len_bc_sq > 2 else len_bc_sq + 2
    # So sánh cos B với 1/sqrt(d_comp):
    # cos B > 1/sqrt(d_comp) <=> len_ba_sq / len_bc_sq > 1 / d_comp <=> len_ba_sq * d_comp > len_bc_sq
    cos_b_gt_comp = (len_ba_sq * d_comp) > len_bc_sq
    
    # 3. Điểm K trên mặt phẳng (Oxz) cách đều ba điểm A, B, C:
    # K thuộc (Oxz) => yK = 0[cite: 23].
    # Do yA = yB = yC = y0, tam giác ABC vuông tại A nên tâm đường tròn ngoại tiếp tam giác ABC trong mặt phẳng y = y0
    # là trung điểm của cạnh huyền BC: M_BC = (xa + dx/2; y0; za + dz/2)[cite: 23].
    # Hình chiếu vuông góc của M_BC lên (Oxz) chính là K(xa + dx/2; 0; za + dz/2)[cite: 23].
    # Khi đó khoảng cách từ K đến (Oxy) là d(K, (Oxy)) = |zK| = |za + dz/2|[cite: 23].
    zk_val = za + dz // 2
    dist_k_oxy = abs(zk_val)
    dist_k_oxy_s = dist_k_oxy + random.choice([1, 2])
    
    # 4. Điểm H là chân đường cao kẻ từ A của tam giác ABC:
    # Vì cả 3 điểm A, B, C đều có tung độ bằng y0 nên tam giác ABC nằm trong mặt phẳng song song với (Oxz) có phương trình y = y0[cite: 23].
    # Do đó chân đường cao H cũng có tung độ yH = y0[cite: 23].
    bound_yh = y0 - 1  # Vì yH = y0 > y0 - 1 nên luôn đúng[cite: 23]
    bound_yh_s = y0 + 1
    
    # Nội dung câu hỏi[cite: 23]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$ cho ba điểm $A(%s;%s;%s); B(%s;%s;%s); C(%s;%s;%s)$."""
        % (xa, y0, za, xb, y0, zb, xc, y0, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Trọng tâm tam giác ABC có cao độ dương[cite: 23]
    if is_zg_positive:
        nb_da_1_d = "\\True Trọng tâm tam giác $ABC$ có cao độ dương"
        nb_da_1_s = "Trọng tâm tam giác $ABC$ có cao độ âm"
    else:
        nb_da_1_d = "\\True Trọng tâm tam giác $ABC$ có cao độ âm"
        nb_da_1_s = "Trọng tâm tam giác $ABC$ có cao độ dương"
    
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$. Cao độ của điểm $G$ là: \\\\ $z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s$. \\\\ Vì $%s %s 0$ nên mệnh đề khẳng định cao độ của trọng tâm tam giác $ABC$ %s là đúng."""
        % (
            za,
            zb,
            zc,
            str_zg,
            str_zg,
            ">" if is_zg_positive else "<",
            "dương" if is_zg_positive else "âm",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: cos B > 1/sqrt(d_comp)[cite: 23]
    if cos_b_gt_comp:
        th_da_1_d = "\\True $\\cos B > \\frac{1}{\\sqrt{%s}}$" % (d_comp)
        th_da_1_s = "$\\cos B < \\frac{1}{\\sqrt{%s}}$" % (d_comp)
    else:
        th_da_1_d = "\\True $\\cos B < \\frac{1}{\\sqrt{%s}}$" % (d_comp)
        th_da_1_s = "$\\cos B > \\frac{1}{\\sqrt{%s}}$" % (d_comp)
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có $\\vec{BA} = (x_A - x_B; y_A - y_B; z_A - z_B) = (%s; 0; 0) \\Rightarrow BA = \\sqrt{(%s)^2} = %s$. \\\\ $\\vec{BC} = (x_C - x_B; y_C - y_B; z_C - z_B) = (%s; 0; %s) \\Rightarrow BC = \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Tích vô hướng: $\\vec{BA} \\cdot \\vec{BC} = (%s) \\cdot (%s) + 0 + 0 = %s$. \\\\ Do đó: $\\cos B = \\frac{\\vec{BA} \\cdot \\vec{BC}}{|\\vec{BA}| \\cdot |\\vec{BC}|} = \\frac{%s}{%s \\cdot \\sqrt{%s}} = \\frac{1}{\\sqrt{%s}}$. \\\\ So sánh $\\frac{1}{\\sqrt{%s}}$ với $\\frac{1}{\\sqrt{%s}}$, ta thấy $\\cos B %s \\frac{1}{\\sqrt{%s}}$."""
        % (
            -dx,
            -dx,
            abs(dx),
            -dx,
            dz,
            -dx,
            dz,
            len_bc_sq,
            -dx,
            -dx,
            dot_ba_bc,
            dot_ba_bc,
            abs(dx),
            len_bc_sq,
            len_bc_sq // (len_ba_sq) if len_bc_sq % len_ba_sq == 0 else len_bc_sq,
            len_bc_sq // (len_ba_sq) if len_bc_sq % len_ba_sq == 0 else len_bc_sq,
            d_comp,
            ">" if cos_b_gt_comp else "<",
            d_comp,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Điểm K trên mặt phẳng (Oxz) sao cho K cách đều ba điểm A, B, C thì K cách (Oxy) một khoảng bằng dist_k_oxy[cite: 23]
    nb_da_3_d = (
        "\\True Điểm $K$ trên mặt phẳng tọa độ $(Oxz)$ sao cho $K$ cách đều ba điểm $A, B, C$ thì $K$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$"
        % (dist_k_oxy)
    )
    nb_da_3_s = (
        "Điểm $K$ trên mặt phẳng tọa độ $(Oxz)$ sao cho $K$ cách đều ba điểm $A, B, C$ thì $K$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$"
        % (dist_k_oxy_s)
    )
    list_vd_da_1 = [nb_da_3_d, nb_da_3_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    str_xk = format_fraction_latex(2 * xa + dx, 2)
    
    loigiai_vd_1 = (
        """Vì điểm $K$ thuộc mặt phẳng tọa độ $(Oxz)$ nên tọa độ của $K$ có dạng $K(x; 0; z)$. \\\\ Ta có: \\\\ $KA^2 = (x - (%s))^2 + (0 - %s)^2 + (z - (%s))^2 = (x - (%s))^2 + (z - (%s))^2 + %s$. \\\\ $KB^2 = (x - (%s))^2 + (0 - %s)^2 + (z - (%s))^2 = (x - (%s))^2 + (z - (%s))^2 + %s$. \\\\ $KC^2 = (x - (%s))^2 + (0 - %s)^2 + (z - (%s))^2 = (x - (%s))^2 + (z - (%s))^2 + %s$. \\\\ Để điểm $K$ cách đều ba điểm $A, B, C$ thì: \\\\ $\\begin{cases} KA^2 = KB^2 \\\\ KA^2 = KC^2 \\end{cases} \\Leftrightarrow \\begin{cases} (x - (%s))^2 = (x - (%s))^2 \\\\ (z - (%s))^2 = (z - (%s))^2 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ z = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $K$ là $K\\left(%s; 0; %s\\right)$. \\\\ Khoảng cách từ điểm $K$ đến mặt phẳng $(Oxy)$ là: \\\\ $d(K, (Oxy)) = |z_K| = |%s| = %s$."""
        % (
            xa,
            y0,
            za,
            xa,
            za,
            y0**2,
            xb,
            y0,
            zb,
            xb,
            zb,
            y0**2,
            xc,
            y0,
            zc,
            xc,
            zc,
            y0**2,
            xa,
            xb,
            za,
            zc,
            str_xk,
            zk_val,
            str_xk,
            zk_val,
            zk_val,
            dist_k_oxy,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm H là chân đường cao kẻ từ A của tam giác ABC thì H có tung độ lớn hơn bound_yh[cite: 23]
    vdc_da_1_d = (
        "\\True Điểm $H$ là chân đường cao kẻ từ $A$ của tam giác $ABC$ thì $H$ có tung độ lớn hơn $%s$"
        % (bound_yh)
    )
    vdc_da_1_s = (
        "Điểm $H$ là chân đường cao kẻ từ $A$ của tam giác $ABC$ thì $H$ có tung độ lớn hơn $%s$"
        % (bound_yh_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Nhận xét rằng cả ba điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$ và $C(%s;%s;%s)$ đều có tung độ bằng $%s$. \\\\ Do đó toàn bộ tam giác $ABC$ nằm trong mặt phẳng có phương trình $y = %s$ (song song với mặt phẳng tọa độ $(Oxz)$). \\\\ Vì $H$ là chân đường cao kẻ từ đỉnh $A$ xuống cạnh $BC$ nên điểm $H$ thuộc đường thẳng $BC$, suy ra điểm $H$ cũng nằm trong mặt phẳng $y = %s$. \\\\ Do đó tung độ của điểm $H$ là $y_H = %s$. \\\\ Vì $%s > %s$ nên khẳng định điểm $H$ có tung độ lớn hơn $%s$ là đúng."""
        % (
            xa,
            y0,
            za,
            xb,
            y0,
            zb,
            xc,
            y0,
            zc,
            y0,
            y0,
            y0,
            y0,
            y0,
            bound_yh,
            bound_yh,
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
    