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


def bt_dang24_p2_b3_c1_hh12(self):
    # Hàm biểu diễn vectơ OC với thứ tự các vectơ đơn vị i, k, j bị tráo đổi tạo bẫy[cite: 21]
    def format_ikj(c1, c2, c3):
        # c1 tương ứng i, c2 tương ứng j, c3 tương ứng k
        # Biểu diễn theo thứ tự i, k, j như đề gốc: 4\vec{i} - \vec{k} + \vec{j}
        res = ""
        # Thành phần i
        if c1 == 1:
            res += "\\vec{i}"
        elif c1 == -1:
            res += "-\\vec{i}"
        elif c1 != 0:
            res += "%s\\vec{i}" % c1
    
        # Thành phần k
        if c3 == 1:
            res += "+\\vec{k}" if res else "\\vec{k}"
        elif c3 == -1:
            res += "-\\vec{k}"
        elif c3 > 0:
            res += "+%s\\vec{k}" % c3 if res else "%s\\vec{k}" % c3
        elif c3 < 0:
            res += "%s\\vec{k}" % c3
    
        # Thành phần j
        if c2 == 1:
            res += "+\\vec{j}" if res else "\\vec{j}"
        elif c2 == -1:
            res += "-\\vec{j}"
        elif c2 > 0:
            res += "+%s\\vec{j}" % c2 if res else "%s\\vec{j}" % c2
        elif c2 < 0:
            res += "%s\\vec{j}" % c2
    
        return res
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C không thẳng hàng
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(-3, 3)
    
        xb = random.randint(-3, 3)
        yb = random.randint(-3, 3)
        zb = random.randint(-3, 3)
    
        # Đảm bảo yc != zc để bẫy hoán vị k và j phát huy tác dụng[cite: 21]
        xc = random.randint(2, 5)
        yc = random.choice([1, 2, 3])
        zc = random.choice([-3, -2, -1])
    
        # Vectơ AB, AC[cite: 21]
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        # Tích có hướng [AB, AC] để tính diện tích hình bình hành ABCD[cite: 21]
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        cp_sq = cp_x**2 + cp_y**2 + cp_z**2
    
        # Độ dài các cạnh
        len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        len_ac_sq = ac_x**2 + ac_y**2 + ac_z**2
        len_bc_sq = (xc - xb) ** 2 + (yc - yb) ** 2 + (zc - zb) ** 2
    
        # Tích vô hướng AB . AC để tính cosin góc BAC[cite: 21]
        dot_ab_ac = ab_x * ac_x + ab_y * ac_y + ab_z * ac_z
    
        if (
            cp_sq > 0
            and len_ab_sq > 0
            and len_ac_sq > 0
            and (xa, ya, za) != (xb, yb, zb)
        ):
            break
    
    # Chuỗi biểu diễn vectơ OC đảo thứ tự k trước j[cite: 21]
    str_vec_oc = format_ikj(xc, yc, zc)
    
    # 1. Tọa độ điểm C đúng: C(xc; yc; zc)[cite: 21]
    # Tọa độ điểm C sai: nhầm theo thứ tự xuất hiện i, k, j -> C(xc; zc; yc)[cite: 21]
    xc_s = xc
    yc_s = zc
    zc_s = yc
    
    # 2. Vectơ AB = (ab_x; ab_y; ab_z) và so sánh BC > sqrt(bound_bc_sq)[cite: 21]
    # Chọn mốc so sánh cho BC
    bound_bc_sq = len_bc_sq - random.choice([2, 4, 6])
    if bound_bc_sq <= 0:
        bound_bc_sq = len_bc_sq + 4
    is_bc_gt = len_bc_sq > bound_bc_sq
    str_bound_bc = latex(sp.sqrt(bound_bc_sq))
    
    # 3. Cosin của góc BAC = (AB . AC) / (|AB| * |AC|)[cite: 21]
    cos_bac_sym = Rational(dot_ab_ac, 1) / (sp.sqrt(len_ab_sq) * sp.sqrt(len_ac_sq))
    str_cos_bac = latex(cos_bac_sym)
    # Đáp án sai cho cos BAC (nhầm giá trị hoặc phân số)[cite: 21]
    str_cos_bac_s = (
        "\\frac{1}{9}"
        if str_cos_bac != "\\frac{1}{9}"
        else "\\frac{1}{\\sqrt{3}}"
    )
    
    # 4. Tồn tại điểm D để ABCD là hình bình hành thì S_ABCD = |[AB, AC]| = sqrt(cp_sq)[cite: 21]
    s_abcd_sq = cp_sq
    str_s_abcd = latex(sp.sqrt(s_abcd_sq))
    # Chọn mốc so sánh diện tích s_comp_sq
    comp_s_sq = s_abcd_sq - random.choice([2, 4, 6])
    if comp_s_sq <= 0:
        comp_s_sq = s_abcd_sq + 4
    is_s_gt = s_abcd_sq > comp_s_sq
    str_comp_s = latex(sp.sqrt(comp_s_sq))
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hai điểm $A(%s;%s;%s); B(%s;%s;%s)$ và vectơ $\\vec{OC} = %s$."""
        % (xa, ya, za, xb, yb, zb, str_vec_oc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ điểm C[cite: 21]
    nb_da_1_d = "\\True Tọa độ điểm $C$ là $C(%s;%s;%s)$" % (xc, yc, zc)
    nb_da_1_s = "Tọa độ điểm $C$ là $C(%s;%s;%s)$" % (xc_s, yc_s, zc_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có $\\vec{OC} = %s = %s\\vec{i} + (%s)\\vec{j} + (%s)\\vec{k}$. \\\\ Theo định nghĩa tọa độ vectơ, ta có $\\vec{OC} = (%s;%s;%s)$ nên tọa độ điểm $C$ là $C(%s;%s;%s)$."""
        % (
            str_vec_oc,
            xc,
            yc,
            zc,
            xc,
            yc,
            zc,
            xc,
            yc,
            zc,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Tọa độ vectơ AB và so sánh BC[cite: 21]
    if is_bc_gt:
        th_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$ và $BC > %s$" % (
            ab_x,
            ab_y,
            ab_z,
            str_bound_bc,
        )
        th_da_1_s = "$\\vec{AB} = (%s;%s;%s)$ và $BC < %s$" % (
            ab_x,
            ab_y,
            ab_z,
            str_bound_bc,
        )
    else:
        th_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$ và $BC < %s$" % (
            ab_x,
            ab_y,
            ab_z,
            str_bound_bc,
        )
        th_da_1_s = "$\\vec{AB} = (%s;%s;%s)$ và $BC > %s$" % (
            ab_x,
            ab_y,
            ab_z,
            str_bound_bc,
        )
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Độ dài đoạn thẳng $BC$ là: \\\\ $BC = \\sqrt{(x_C - x_B)^2 + (y_C - y_B)^2 + (z_C - z_B)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{%s} = %s$. \\\\ Vì $%s %s %s$ nên $\\sqrt{%s} %s \\sqrt{%s} = %s$, tức là $BC %s %s$."""
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
            xb,
            yc,
            yb,
            zc,
            zb,
            len_bc_sq,
            latex(sp.sqrt(len_bc_sq)),
            len_bc_sq,
            ">" if is_bc_gt else "<",
            bound_bc_sq,
            len_bc_sq,
            ">" if is_bc_gt else "<",
            bound_bc_sq,
            str_bound_bc,
            ">" if is_bc_gt else "<",
            str_bound_bc,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Cosin của góc BAC[cite: 21]
    vd_da_1_d = "\\True Cosin của góc $\\widehat{BAC}$ là $%s$" % (str_cos_bac)
    vd_da_1_s = "Cosin của góc $\\widehat{BAC}$ là $%s$" % (str_cos_bac_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có $\\vec{AB} = (%s;%s;%s) \\Rightarrow AB = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s) \\Rightarrow AC = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Tích vô hướng của hai vectơ: \\\\ $\\vec{AB} \\cdot \\vec{AC} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$. \\\\ Do đó cosin của góc $\\widehat{BAC}$ là: \\\\ $\\cos\\widehat{BAC} = \\cos(\\vec{AB}, \\vec{AC}) = \\frac{\\vec{AB} \\cdot \\vec{AC}}{|\\vec{AB}| \\cdot |\\vec{AC}|} = \\frac{%s}{\\sqrt{%s} \\cdot \\sqrt{%s}} = %s$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            ab_x,
            ab_y,
            ab_z,
            len_ab_sq,
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
            str_cos_bac,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tồn tại điểm D trong hệ trục tọa độ để ABCD là hình bình hành thì S_ABCD > str_comp_s[cite: 21]
    if is_s_gt:
        vdc_da_1_d = (
            "\\True Tồn tại điểm $D$ trong hệ trục tọa độ để $ABCD$ là hình bình hành thì $S_{ABCD} > %s$"
            % (str_comp_s)
        )
        vdc_da_1_s = (
            "Tồn tại điểm $D$ trong hệ trục tọa độ để $ABCD$ là hình bình hành thì $S_{ABCD} < %s$"
            % (str_comp_s)
        )
    else:
        vdc_da_1_d = (
            "\\True Tồn tại điểm $D$ trong hệ trục tọa độ để $ABCD$ là hình bình hành thì $S_{ABCD} < %s$"
            % (str_comp_s)
        )
        vdc_da_1_s = (
            "Tồn tại điểm $D$ trong hệ trục tọa độ để $ABCD$ là hình bình hành thì $S_{ABCD} > %s$"
            % (str_comp_s)
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    xd = xc + xa - xb
    yd = yc + ya - yb
    zd = zc + za - zb
    
    loigiai_vdc_1 = (
        """Tứ giác $ABCD$ là hình bình hành khi và chỉ khi: \\\\ $\\vec{AD} = \\vec{BC} \\Leftrightarrow D = A + \\vec{BC} \\Rightarrow D(%s;%s;%s)$. \\\\ Do ba điểm $A, B, C$ không thẳng hàng nên luôn tồn tại duy nhất điểm $D(%s;%s;%s)$ thỏa mãn. \\\\ Ta có tích có hướng của hai vectơ: \\\\ $[\\vec{AB}, \\vec{AC}] = \\left( \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix} \\right) = (%s;%s;%s)$. \\\\ Diện tích của hình bình hành $ABCD$ là: \\\\ $S_{ABCD} = \\left|[\\vec{AB}, \\vec{AC}]\\right| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ So sánh với $%s = \\sqrt{%s}$, vì $%s %s %s$ nên $S_{ABCD} %s %s$."""
        % (
            xd,
            yd,
            zd,
            xd,
            yd,
            zd,
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
            s_abcd_sq,
            str_s_abcd,
            str_comp_s,
            comp_s_sq,
            s_abcd_sq,
            ">" if is_s_gt else "<",
            comp_s_sq,
            ">" if is_s_gt else "<",
            str_comp_s,
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
    