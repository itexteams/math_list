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


def bt_dang57_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu các đỉnh hình hộp ABCD.A'B'C'D'[cite: 21]
    # A, B, D xác định đáy ABCD là hình bình hành => C = B + D - A[cite: 21]
    # C' xác định vectơ cạnh bên CC' => AA' = BB' = DD' = CC' = C' - C[cite: 21]
    # A' = A + CC' = A + C' - C = A + C' - (B + D - A) = 2A + C' - B - D[cite: 21]
    while True:
        xa = random.randint(1, 3)
        ya = random.randint(0, 2)
        za = random.randint(1, 3)
    
        # AB và AD không cùng phương[cite: 21]
        ab_x = random.choice([1, 2, -1])
        ab_y = random.choice([1, 2])
        ab_z = random.choice([1, -1, 2])
    
        ad_x = random.choice([0, 1, -1])
        ad_y = random.choice([-2, -1, 1])
        ad_z = 0  # Chọn ad_z = 0 để AD có thành phần bằng 0 đẹp như mẫu[cite: 21]
    
        # Kiểm tra tính không cùng phương của AB và AD[cite: 21]
        cp_base_x = ab_y * ad_z - ab_z * ad_y
        cp_base_y = ab_z * ad_x - ab_x * ad_z
        cp_base_z = ab_x * ad_y - ab_y * ad_x
    
        if cp_base_x == 0 and cp_base_y == 0 and cp_base_z == 0:
            continue
    
        xb = xa + ab_x
        yb = ya + ab_y
        zb = za + ab_z
    
        xd = xa + ad_x
        yd = ya + ad_y
        zd = za + ad_z
    
        # C = B + D - A[cite: 21]
        xc = xb + xd - xa
        yc = yb + yd - ya
        zc = zb + zd - za
    
        # Vectơ đường cao / cạnh bên CC' không nằm trong mặt đáy (ABCD)[cite: 21]
        cc_x = random.choice([1, 2, 3])
        cc_y = random.choice([2, 3, 4])
        cc_z = random.choice([-6, -5, -4, 4, 5])
    
        # Tích hỗn tạp khác 0 để là hình hộp thật sự[cite: 21]
        mix_prod = cp_base_x * cc_x + cp_base_y * cc_y + cp_base_z * cc_z
        if mix_prod == 0:
            continue
    
        xc_prime = xc + cc_x
        yc_prime = yc + cc_y
        zc_prime = zc + cc_z
    
        # Tọa độ điểm A': A' = A + CC'[cite: 21]
        xa_prime = xa + cc_x
        ya_prime = ya + cc_y
        za_prime = za + cc_z
    
        # Độ dài OC[cite: 21]
        oc_sq = xc**2 + yc**2 + zc**2
        str_oc_true = latex(sp.sqrt(oc_sq))
    
        # Tổng a + b + c của A'(a; b; c)[cite: 21]
        sum_a_prime = xa_prime + ya_prime + za_prime
        is_sum_even = sum_a_prime % 2 == 0
    
        break
    
    # 1. Tọa độ vectơ AD = (xd - xa; yd - ya; zd - za)[cite: 21]
    ad_true_x = xd - xa
    ad_true_y = yd - ya
    ad_true_z = zd - za
    
    ad_false_x = ad_true_x + 1
    ad_false_y = ad_true_y
    ad_false_z = ad_true_z
    
    # 2. Khẳng định b: A'C' + D'D > A'C[cite: 21]
    # Trong hình hộp, CC' = D'D, A'C' = AC. Trong tam giác A'CC', theo bất đẳng thức tam giác:
    # A'C' + CC' > A'C <=> A'C' + D'D > A'C (luôn đúng do A', C', C không thẳng hàng)[cite: 21]
    
    # 3. Khẳng định c: OC = sqrt(oc_sq)[cite: 21]
    oc_sq_false = oc_sq + random.choice([-2, -1, 1, 2])
    str_oc_false = latex(sp.sqrt(oc_sq_false))
    if str_oc_false == str_oc_true:
        str_oc_false = "2\\sqrt{2}"
    
    # 4. Khẳng định d: A'(a;b;c) thì a + b + c là số tự nhiên chẵn hay lẻ[cite: 21]
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian $Oxyz$ cho hình hộp $ABCD.A'B'C'D'$ biết $A(%s;%s;%s), B(%s;%s;%s), D(%s;%s;%s), C'(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xd, yd, zd, xc_prime, yc_prime, zc_prime)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Vectơ AD[cite: 21]
    nb_da_1_d = "\\True $\\vec{AD} = (%s;%s;%s)$" % (ad_true_x, ad_true_y, ad_true_z)
    nb_da_1_s = "$\\vec{AD} = (%s;%s;%s)$" % (ad_false_x, ad_false_y, ad_false_z)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ của vectơ $\\vec{AD}$ là: \\\\ $\\vec{AD} = (x_D - x_A; y_D - y_A; z_D - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (
            xd,
            xa,
            yd,
            ya,
            zd,
            za,
            ad_true_x,
            ad_true_y,
            ad_true_z,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: A'C' + D'D > A'C[cite: 21]
    th_da_1_d = "\\True $A'C' + D'D > A'C$"
    th_da_1_s = "$A'C' + D'D < A'C$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $ABCD.A'B'C'D'$ là hình hộp nên các cạnh bên đôi một song song và bằng nhau, suy ra $D'D = C'C$. \\\\ Xét tam giác $A'C'C$, theo bất đẳng thức tam giác ta luôn có: \\\\ $A'C' + C'C > A'C$. \\\\ Thay $C'C = D'D$ vào bất đẳng thức trên, ta được: \\\\ $A'C' + D'D > A'C$. \\\\ Do đó khẳng định là đúng."""
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: OC = ...[cite: 21]
    vd_da_1_d = "\\True $OC = %s$" % (str_oc_true)
    vd_da_1_s = "$OC = %s$" % (str_oc_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $ABCD$ là hình bình hành nên ta có: \\\\ $\\vec{AB} = \\vec{DC} \\Leftrightarrow (x_B - x_A; y_B - y_A; z_B - z_A) = (x_C - x_D; y_C - y_D; z_C - z_D)$ \\\\ $\\Leftrightarrow \\begin{cases} x_C = x_B + x_D - x_A = %s + (%s) - (%s) = %s \\\\ y_C = y_B + y_D - y_A = %s + (%s) - (%s) = %s \\\\ z_C = z_B + z_D - z_A = %s + (%s) - (%s) = %s \\end{cases} \\Rightarrow C(%s;%s;%s)$. \\\\ Khoảng cách từ gốc tọa độ $O(0;0;0)$ đến điểm $C$ là: \\\\ $OC = \\sqrt{x_C^2 + y_C^2 + z_C^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
        % (
            xb,
            xd,
            xa,
            xc,
            yb,
            yd,
            ya,
            yc,
            zb,
            zd,
            za,
            zc,
            xc,
            yc,
            zc,
            xc,
            yc,
            zc,
            oc_sq,
            str_oc_true,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Với A'(a;b;c) thì a + b + c là một số tự nhiên chẵn/lẻ[cite: 21]
    if is_sum_even:
        vdc_da_1_d = (
            "\\True Với $A'(a;b;c)$ thì khi đó $a + b + c$ là một số tự nhiên chẵn"
        )
        vdc_da_1_s = (
            "Với $A'(a;b;c)$ thì khi đó $a + b + c$ là một số tự nhiên lẻ"
        )
    else:
        vdc_da_1_d = (
            "\\True Với $A'(a;b;c)$ thì khi đó $a + b + c$ là một số tự nhiên lẻ"
        )
        vdc_da_1_s = (
            "Với $A'(a;b;c)$ thì khi đó $a + b + c$ là một số tự nhiên chẵn"
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có vectơ cạnh bên $\\vec{CC'}$ có tọa độ là: \\\\ $\\vec{CC'} = (x_{C'} - x_C; y_{C'} - y_C; z_{C'} - z_C) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Vì $ABCD.A'B'C'D'$ là hình hộp nên $\\vec{AA'} = \\vec{CC'}$. \\\\ Suy ra tọa độ của điểm $A'(a;b;c)$ thỏa mãn: \\\\ $\\begin{cases} a - x_A = %s \\\\ b - y_A = %s \\\\ c - z_A = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s + (%s) = %s \\\\ b = %s + (%s) = %s \\\\ c = %s + (%s) = %s \\end{cases} \\Rightarrow A'(%s;%s;%s)$. \\\\ Khi đó giá trị của biểu thức $a + b + c$ là: \\\\ $a + b + c = %s + (%s) + (%s) = %s$. \\\\ Vì $%s$ là một số tự nhiên %s nên khẳng định là %s."""
        % (
            xc_prime,
            xc,
            yc_prime,
            yc,
            zc_prime,
            zc,
            cc_x,
            cc_y,
            cc_z,
            cc_x,
            cc_y,
            cc_z,
            xa,
            cc_x,
            xa_prime,
            ya,
            cc_y,
            ya_prime,
            za,
            cc_z,
            za_prime,
            xa_prime,
            ya_prime,
            za_prime,
            xa_prime,
            ya_prime,
            za_prime,
            sum_a_prime,
            sum_a_prime,
            "chẵn" if is_sum_even else "lẻ",
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
    