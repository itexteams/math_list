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


def bt_dang37_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu tam giác ABC sao cho AC = 2*AB với AB, AC nguyên đẹp
    # AB = (u1, u2, u3), AC = (v1, v2, v3) sao cho |AC| = 2*|AB|
    while True:
        xa = random.randint(-2, 2)
        ya = 0  # Chọn ya = 0, za = 0 như bài gốc để tính toán chân phương
        za = 0
    
        # Chọn vectơ AB sao cho độ dài |AB| là số nguyên đẹp (ví dụ độ dài bằng 3)
        ab_options = [
            (1, -2, 2),
            (2, -1, 2),
            (2, 2, -1),
            (1, 2, -2),
            (-1, 2, 2),
            (2, -2, 1),
        ]
        ab_x, ab_y, ab_z = random.choice(ab_options)
        len_ab = 3
        len_ab_sq = 9
    
        xb = xa + ab_x
        yb = ya + ab_y
        zb = za + ab_z
    
        # Chọn vectơ AC sao cho |AC| = 2 * len_ab = 6, không cùng phương AB
        # Vector có độ dài 6, ví dụ (2, 4, -4) hoặc hoán vị
        ac_options = [
            (2, 4, -4),
            (4, 2, -4),
            (2, -4, 4),
            (-4, 4, 2),
            (4, 4, -2),
            (-2, 4, 4),
        ]
        ac_x, ac_y, ac_z = random.choice(ac_options)
        len_ac = 6
        len_ac_sq = 36
    
        xc = xa + ac_x
        yc = ya + ac_y
        zc = za + ac_z
    
        # Kiểm tra không thẳng hàng
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        if cp_x != 0 or cp_y != 0 or cp_z != 0:
            break
    
    # 1. Khẳng định a: AC = 2*AB (Luôn đúng theo cấu trúc sinh)[cite: 23]
    # 2. Khẳng định b: Trọng tâm G của tam giác ABC cách gốc tọa độ O một khoảng OG
    xg_num = xa + xb + xc
    yg_num = ya + yb + yc
    zg_num = za + zb + zc
    og_sq = Rational(xg_num**2 + yg_num**2 + zg_num**2, 9)
    og_val = math.sqrt(float(og_sq))
    
    bound_og = 3
    is_og_lt_3 = og_val < bound_og
    
    # 3. Khẳng định c: M(a;b;c) thỏa mãn MA + MB - 3MC = 0 <=> M = 3C - A - B[cite: 23]
    # M = 3C - A - B
    xm = 3 * xc - xa - xb
    ym = 3 * yc - ya - yb
    zm = 3 * zc - za - zb
    is_zm_gt_3 = zm > 3
    
    # 4. Khẳng định d: D là chân đường phân giác trong kẻ từ A của tam giác ABC[cite: 23]
    # Theo tính chất đường phân giác: DB / DC = AB / AC = 1/2 => vecto DB = - 1/2 vecto DC
    # <=> 2 * DB = - DC <=> 2(B - D) = D - C <=> 3D = 2B + C <=> D = (2B + C) / 3[cite: 23]
    xd_num = 2 * xb + xc
    yd_num = 2 * yb + yc
    zd_num = 2 * zb + zc
    
    xd_val = Rational(xd_num, 3)
    yd_val = Rational(yd_num, 3)
    zd_val = Rational(zd_num, 3)
    
    od_sq_num = xd_num**2 + yd_num**2 + zd_num**2
    # OD = sqrt(od_sq_num) / 3
    od_sym = sp.sqrt(od_sq_num) / 3
    str_od_true = latex(od_sym)
    str_od_false = "\\frac{\\sqrt{%s}}{3}" % (od_sq_num + random.choice([-5, -3, 3, 5]))
    
    # Nội dung câu hỏi[cite: 23]
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho tam giác $ABC$ có tọa độ các đỉnh $A(%s;%s;%s)$, $B(%s;%s;%s)$ và $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: AC = 2AB[cite: 23]
    nb_da_1_d = "\\True $AC = 2AB$"
    nb_da_1_s = "$AC = AB$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Độ dài các đoạn thẳng: \\\\ $AB = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ $AC = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ Vì $AC = %s = 2 \\cdot %s = 2AB$ nên khẳng định $AC = 2AB$ là đúng."""
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
            ab_y,
            ab_z,
            len_ab_sq,
            len_ab,
            ac_x,
            ac_y,
            ac_z,
            len_ac_sq,
            len_ac,
            len_ac,
            len_ab,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Trọng tâm tam giác ABC cách gốc tọa độ một khoảng nhỏ hơn 3[cite: 23]
    if is_og_lt_3:
        th_da_1_d = (
            "\\True Trọng tâm tam giác $ABC$ cách gốc tọa độ một khoảng nhỏ hơn $3$"
        )
        th_da_1_s = (
            "Trọng tâm tam giác $ABC$ cách gốc tọa độ một khoảng lớn hơn $3$"
        )
    else:
        th_da_1_d = (
            "\\True Trọng tâm tam giác $ABC$ cách gốc tọa độ một khoảng lớn hơn $3$"
        )
        th_da_1_s = (
            "Trọng tâm tam giác $ABC$ cách gốc tọa độ một khoảng nhỏ hơn $3$"
        )
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    str_xg = format_fraction_latex(xg_num, 3)
    str_yg = format_fraction_latex(yg_num, 3)
    str_zg = format_fraction_latex(zg_num, 3)
    
    loigiai_th_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$. Khi đó tọa độ của điểm $G$ là: \\\\ $\\begin{cases} x_G = \\frac{x_A + x_B + x_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ y_G = \\frac{y_A + y_B + y_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\end{cases} \\Rightarrow G\\left(%s;%s;%s\\right)$. \\\\ Khoảng cách từ điểm $G$ đến gốc tọa độ $O(0;0;0)$ là: \\\\ $OG = \\sqrt{x_G^2 + y_G^2 + z_G^2} = \\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2 + \\left(%s\\right)^2} = %s \\approx %s$. \\\\ Vì $%s %s 3$ nên khẳng định là %s."""
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
            str_xg,
            str_yg,
            str_zg,
            latex(sp.sqrt(og_sq)),
            str(round(og_val, 2)).replace(".", ","),
            str(round(og_val, 2)).replace(".", ","),
            "<" if is_og_lt_3 else ">",
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Điểm M thỏa mãn MA + MB - 3MC = 0 thì M có cao độ lớn hơn 3[cite: 23]
    if is_zm_gt_3:
        vd_da_1_d = (
            "\\True Gọi $M(a;b;c)$ là điểm thoả mãn $\\vec{MA} + \\vec{MB} - 3\\vec{MC} = \\vec{0}$ thì $M$ có cao độ lớn hơn $3$"
        )
        vd_da_1_s = (
            "Gọi $M(a;b;c)$ là điểm thoả mãn $\\vec{MA} + \\vec{MB} - 3\\vec{MC} = \\vec{0}$ thì $M$ có cao độ nhỏ hơn $3$"
        )
    else:
        vd_da_1_d = (
            "\\True Gọi $M(a;b;c)$ là điểm thoả mãn $\\vec{MA} + \\vec{MB} - 3\\vec{MC} = \\vec{0}$ thì $M$ có cao độ nhỏ hơn $3$"
        )
        vd_da_1_s = (
            "Gọi $M(a;b;c)$ là điểm thoả mãn $\\vec{MA} + \\vec{MB} - 3\\vec{MC} = \\vec{0}$ thì $M$ có cao độ lớn hơn $3$"
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có hệ thức: \\\\ $\\vec{MA} + \\vec{MB} - 3\\vec{MC} = \\vec{0} \\Leftrightarrow (\\vec{OA} - \\vec{OM}) + (\\vec{OB} - \\vec{OM}) - 3(\\vec{OC} - \\vec{OM}) = \\vec{0}$ \\\\ $\\Leftrightarrow \\vec{OM} = 3\\vec{OC} - \\vec{OA} - \\vec{OB}$. \\\\ Suy ra tọa độ của điểm $M(a;b;c)$ là: \\\\ $\\begin{cases} a = 3x_C - x_A - x_B = 3 \\cdot (%s) - (%s) - (%s) = %s \\\\ b = 3y_C - y_A - y_B = 3 \\cdot (%s) - (%s) - (%s) = %s \\\\ c = 3z_C - z_A - z_B = 3 \\cdot (%s) - (%s) - (%s) = %s \\end{cases} \\Rightarrow M(%s;%s;%s)$. \\\\ Cao độ của điểm $M$ là $c = %s$. \\\\ Vì $%s %s 3$ nên khẳng định là %s."""
        % (
            xc,
            xa,
            xb,
            xm,
            yc,
            ya,
            yb,
            ym,
            zc,
            za,
            zb,
            zm,
            xm,
            ym,
            zm,
            zm,
            zm,
            ">" if is_zm_gt_3 else "<",
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Điểm D là chân đường phân giác kẻ từ A thì OD = ...[cite: 23]
    vdc_da_1_d = (
        "\\True Điểm $D$ là chân đường phân giác kẻ từ $A$ thì $OD = %s$"
        % (str_od_true)
    )
    vdc_da_1_s = (
        "Điểm $D$ là chân đường phân giác kẻ từ $A$ thì $OD = %s$"
        % (str_od_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_xd = format_fraction_latex(xd_num, 3)
    str_yd = format_fraction_latex(yd_num, 3)
    str_zd = format_fraction_latex(zd_num, 3)
    
    loigiai_vdc_1 = (
        """Vì $D$ là chân đường phân giác trong góc $A$ của tam giác $ABC$ trên cạnh $BC$ nên theo tính chất đường phân giác, ta có: \\\\ $\\frac{DB}{DC} = \\frac{AB}{AC} = \\frac{%s}{%s} = \\frac{1}{2} \\Rightarrow DC = 2 DB$. \\\\ Vì điểm $D$ nằm giữa hai điểm $B$ và $C$ nên hai vectơ $\\vec{DB}$ và $\\vec{DC}$ ngược hướng, suy ra: \\\\ $\\vec{DB} = -\\frac{1}{2}\\vec{DC} \\Leftrightarrow 2\\vec{DB} + \\vec{DC} = \\vec{0} \\Leftrightarrow 2(B - D) + (C - D) = \\vec{0} \\Leftrightarrow 3D = 2B + C \\Leftrightarrow D = \\frac{2B + C}{3}$. \\\\ Tọa độ điểm $D$ là: \\\\ $\\begin{cases} x_D = \\frac{2x_B + x_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\\\ y_D = \\frac{2y_B + y_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\\\ z_D = \\frac{2z_B + z_C}{3} = \\frac{2 \\cdot (%s) + (%s)}{3} = %s \\end{cases} \\Rightarrow D\\left(%s;%s;%s\\right)$. \\\\ Khi đó độ dài đoạn thẳng $OD$ là: \\\\ $OD = \\sqrt{x_D^2 + y_D^2 + z_D^2} = \\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2 + \\left(%s\\right)^2} = \\sqrt{\\frac{%s}{9}} = %s$."""
        % (
            len_ab,
            len_ac,
            xb,
            xc,
            str_xd,
            yb,
            yc,
            str_yd,
            zb,
            zc,
            str_zd,
            str_xd,
            str_yd,
            str_zd,
            str_xd,
            str_yd,
            str_zd,
            od_sq_num,
            str_od_true,
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
    