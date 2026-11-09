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


def bt_dang29_p2_b3_c1_hh12(self):
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
        xa = random.randint(-3, 3)
        ya = random.randint(1, 4)
        za = random.randint(1, 4)
    
        xb = random.randint(-3, 3)
        yb = random.randint(-4, 0)
        zb = random.randint(1, 5)
    
        # Đảm bảo A + C chẵn để tọa độ trung điểm AC nguyên đẹp
        xc = random.randint(1, 5)
        yc = random.randint(-2, 3)
        zc = random.randint(-4, 1)
    
        if (xa + xc) % 2 != 0:
            xc += 1
        if (ya + yc) % 2 != 0:
            yc += 1
        if (za + zc) % 2 != 0:
            zc += 1
    
        # Vectơ AB, AC
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        # Tích có hướng [AB, AC] để tính diện tích và bán kính ngoại tiếp
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        cp_sq = cp_x**2 + cp_y**2 + cp_z**2
    
        # Độ dài các cạnh
        len_ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        len_ac_sq = ac_x**2 + ac_y**2 + ac_z**2
        len_bc_sq = (xc - xb) ** 2 + (yc - yb) ** 2 + (zc - zb) ** 2
    
        if (
            cp_sq > 0
            and len_ab_sq > 0
            and len_ac_sq > 0
            and len_bc_sq > 0
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # 1. Trung điểm của đoạn thẳng AC: M(xm_mid; ym_mid; zm_mid)[cite: 26]
    xm_mid = (xa + xc) // 2
    ym_mid = (ya + yc) // 2
    zm_mid = (za + zc) // 2
    
    # Tọa độ sai của trung điểm M[cite: 26]
    xm_mid_s = xm_mid
    ym_mid_s = ym_mid
    zm_mid_s = zm_mid + random.choice([-2, -1, 1, 2])
    
    # 2. Độ dài đoạn thẳng AB = \sqrt{len_ab_sq}[cite: 26]
    str_ab_true = latex(sp.sqrt(len_ab_sq))
    str_ab_false = latex(sp.sqrt(len_ab_sq + random.choice([-3, -2, 2, 3])))
    
    # 3. Để C là trọng tâm tam giác ABM thì M = 3C - A - B[cite: 26]
    xm_grav = 3 * xc - xa - xb
    ym_grav = 3 * yc - ya - yb
    zm_grav = 3 * zc - za - zb
    
    # Tọa độ sai của M[cite: 26]
    xm_grav_s = xm_grav + random.choice([-2, 2])
    ym_grav_s = ym_grav
    zm_grav_s = zm_grav
    
    # 4. Bán kính đường tròn ngoại tiếp tam giác ABC: R = (AB * AC * BC) / (4 * S_ABC)[cite: 26]
    # S_ABC = 1/2 * sqrt(cp_sq) => R = (AB * AC * BC) / (2 * sqrt(cp_sq))
    len_ab = math.sqrt(len_ab_sq)
    len_ac = math.sqrt(len_ac_sq)
    len_bc = math.sqrt(len_bc_sq)
    area_abc = 0.5 * math.sqrt(cp_sq)
    r_val = (len_ab * len_ac * len_bc) / (4.0 * area_abc)
    
    # Làm tròn 2 chữ số thập phân theo ROUND_HALF_UP
    r_rounded = Decimal(str(r_val)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    str_r_true = str(r_rounded).replace(".", ",")
    
    r_rounded_s = Decimal(str(r_val + 0.5)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    str_r_false = str(r_rounded_s).replace(".", ",")
    
    # Nội dung câu hỏi[cite: 26]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho tam giác $ABC$ với $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$. $M$ là trung điểm của cạnh $AC$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Trung điểm của đoạn thẳng AC[cite: 26]
    nb_da_1_d = "\\True Trung điểm của đoạn thẳng $AC$ là $M(%s;%s;%s)$" % (
        xm_mid,
        ym_mid,
        zm_mid,
    )
    nb_da_1_s = "Trung điểm của đoạn thẳng $AC$ là $M(%s;%s;%s)$" % (
        xm_mid_s,
        ym_mid_s,
        zm_mid_s,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Gọi $M$ là trung điểm của đoạn thẳng $AC$. Khi đó tọa độ điểm $M$ thỏa mãn: \\\\ $\\begin{cases} x_M = \\frac{x_A + x_C}{2} = \\frac{%s + (%s)}{2} = %s \\\\ y_M = \\frac{y_A + y_C}{2} = \\frac{%s + (%s)}{2} = %s \\\\ z_M = \\frac{z_A + z_C}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases}$ \\\\ Vậy trung điểm của đoạn thẳng $AC$ là $M(%s;%s;%s)$."""
        % (
            xa,
            xc,
            xm_mid,
            ya,
            yc,
            ym_mid,
            za,
            zc,
            zm_mid,
            xm_mid,
            ym_mid,
            zm_mid,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Độ dài đoạn thẳng AB[cite: 26]
    th_da_1_d = "\\True $AB = %s$" % (str_ab_true)
    th_da_1_s = "$AB = %s$" % (str_ab_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Độ dài đoạn thẳng $AB$ là: \\\\ $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s$."""
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
            str_ab_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Để C là trọng tâm tam giác ABM thì tọa độ M[cite: 26]
    vd_da_1_d = (
        "\\True Để $C$ là trọng tâm tam giác $ABM$ thì tọa độ $M(%s;%s;%s)$"
        % (xm_grav, ym_grav, zm_grav)
    )
    vd_da_1_s = (
        "Để $C$ là trọng tâm tam giác $ABM$ thì tọa độ $M(%s;%s;%s)$"
        % (xm_grav_s, ym_grav_s, zm_grav_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Điểm $C$ là trọng tâm của tam giác $ABM$ khi và chỉ khi: \\\\ $\\begin{cases} x_C = \\frac{x_A + x_B + x_M}{3} \\\\ y_C = \\frac{y_A + y_B + y_M}{3} \\\\ z_C = \\frac{z_A + z_B + z_M}{3} \\end{cases} \\Leftrightarrow \\begin{cases} x_M = 3x_C - x_A - x_B = 3 \\cdot (%s) - (%s) - (%s) = %s \\\\ y_M = 3y_C - y_A - y_B = 3 \\cdot (%s) - (%s) - (%s) = %s \\\\ z_M = 3z_C - z_A - z_B = 3 \\cdot (%s) - (%s) - (%s) = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $M$ là $M(%s;%s;%s)$."""
        % (
            xc,
            xa,
            xb,
            xm_grav,
            yc,
            ya,
            yb,
            ym_grav,
            zc,
            za,
            zb,
            zm_grav,
            xm_grav,
            ym_grav,
            zm_grav,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Bán kính đường tròn ngoại tiếp tam giác ABC[cite: 26]
    vdc_da_1_d = (
        "\\True Tam giác $ABC$ có bán kính đường tròn ngoại tiếp $R \\approx %s$"
        % (str_r_true)
    )
    vdc_da_1_s = (
        "Tam giác $ABC$ có bán kính đường tròn ngoại tiếp $R \\approx %s$"
        % (str_r_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (%s;%s;%s) \\Rightarrow AB = \\sqrt{%s}$. \\\\ $\\vec{AC} = (%s;%s;%s) \\Rightarrow AC = \\sqrt{%s}$. \\\\ $\\vec{BC} = (%s;%s;%s) \\Rightarrow BC = \\sqrt{%s}$. \\\\ Tích có hướng của hai vectơ $\\vec{AB}$ và $\\vec{AC}$ là: \\\\ $[\\vec{AB}, \\vec{AC}] = (%s;%s;%s) \\Rightarrow \\left|[\\vec{AB}, \\vec{AC}]\\right| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Diện tích tam giác $ABC$ là: \\\\ $S_{ABC} = \\frac{1}{2} \\left|[\\vec{AB}, \\vec{AC}]\\right| = \\frac{\\sqrt{%s}}{2}$. \\\\ Bán kính đường tròn ngoại tiếp tam giác $ABC$ là: \\\\ $R = \\frac{AB \\cdot AC \\cdot BC}{4 S_{ABC}} = \\frac{\\sqrt{%s} \\cdot \\sqrt{%s} \\cdot \\sqrt{%s}}{2 \\sqrt{%s}} \\approx %s$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            len_ab_sq,
            ac_x,
            ac_y,
            ac_z,
            len_ac_sq,
            xc - xb,
            yc - yb,
            zc - zb,
            len_bc_sq,
            cp_x,
            cp_y,
            cp_z,
            cp_x,
            cp_y,
            cp_z,
            cp_sq,
            cp_sq,
            len_ab_sq,
            len_ac_sq,
            len_bc_sq,
            cp_sq,
            str_r_true,
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
    