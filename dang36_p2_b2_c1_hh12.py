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


def bt_dang36_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu 3 điểm A, B, C không thẳng hàng
    while True:
        xa = random.randint(-4, 4)
        ya = random.randint(-3, 3)
        za = random.randint(-4, 4)
    
        xb = random.randint(-4, 4)
        yb = random.randint(-3, 3)
        zb = random.randint(-4, 4)
    
        xc = random.randint(-4, 4)
        yc = random.randint(-3, 3)
        zc = random.randint(-4, 4)
    
        # Đảm bảo tổng hoành độ của tam giác ABC chia hết cho 3 để khoảng cách đến (Oyz) là số nguyên đẹp
        if (xa + xb + xc) % 3 != 0 or (xa + xb + xc) == 0:
            continue
    
        # Vectơ BA và BC
        ba_x = xa - xb
        ba_y = ya - yb
        ba_z = za - zb
    
        bc_x = xc - xb
        bc_y = yc - yb
        bc_z = zc - zb
    
        # Kiểm tra ba điểm A, B, C không thẳng hàng
        cp_x = ba_y * bc_z - ba_z * bc_y
        cp_y = ba_z * bc_x - ba_x * bc_z
        cp_z = ba_x * bc_y - ba_y * bc_x
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # 1. Vectơ BA = (ba_x; ba_y; ba_z)[cite: 22]
    # Vectơ BA sai (ví dụ nhầm thành vectơ AB = B - A)[cite: 22]
    ba_x_s = -ba_x
    ba_y_s = -ba_y
    ba_z_s = -ba_z
    
    # 2. Trọng tâm G của tam giác ABC:
    # Hoành độ xG = (xa + xb + xc) / 3
    # Khoảng cách từ G đến mặt phẳng (Oyz): d(G, (Oyz)) = |xG|[cite: 22]
    xg_val = (xa + xb + xc) // 3
    dist_g_oyz = abs(xg_val)
    dist_g_oyz_s = dist_g_oyz + random.choice([1, 2])
    
    # 3. Tâm đối xứng của hai điểm A, B là trung điểm M của đoạn AB:
    # Hoành độ xM = (xa + xb) / 2[cite: 22]
    xm_num = xa + xb
    str_xm = format_fraction_latex(xm_num, 2)
    # Khẳng định sai: đổi giá trị hoặc nhầm dấu[cite: 22]
    str_xm_s = format_fraction_latex(-xm_num, 2) if xm_num != 0 else "1"
    
    # 4. ABCD là hình bình hành <=> vecto AB = vecto DC <=> D = C - AB = C + A - B[cite: 22]
    # Hoặc vecto AD = vecto BC <=> D = A + BC = A + C - B[cite: 22]
    xd = xa + xc - xb
    yd = ya + yc - yb
    zd = za + zc - zb
    
    # Giá trị biểu thức T = a^2 + b^2 + c^2[cite: 22]
    t_val = xd**2 + yd**2 + zd**2
    is_t_div_6 = t_val % 6 == 0
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$ cho $3$ điểm $A(%s;%s;%s); B(%s;%s;%s)$ và $C(%s;%s;%s)$. Giả sử $D(a;b;c)$ là đỉnh còn lại của hình bình hành $ABCD$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ BA[cite: 22]
    nb_da_1_d = "\\True $\\vec{BA} = (%s;%s;%s)$" % (ba_x, ba_y, ba_z)
    nb_da_1_s = "$\\vec{BA} = (%s;%s;%s)$" % (ba_x_s, ba_y_s, ba_z_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ của vectơ $\\vec{BA}$ là: \\\\ $\\vec{BA} = (x_A - x_B; y_A - y_B; z_A - z_B) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xa, xb, ya, yb, za, zb, ba_x, ba_y, ba_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Trọng tâm tam giác ABC cách mặt phẳng (Oyz) một khoảng bằng dist_g_oyz[cite: 22]
    th_da_1_d = (
        "\\True Trọng tâm tam giác $ABC$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (dist_g_oyz)
    )
    th_da_1_s = (
        "Trọng tâm tam giác $ABC$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (dist_g_oyz_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$. Khi đó hoành độ của điểm $G$ là: \\\\ $x_G = \\frac{x_A + x_B + x_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s$. \\\\ Mặt phẳng $(Oyz)$ có phương trình là $x = 0$. \\\\ Khoảng cách từ trọng tâm $G$ của tam giác $ABC$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(G, (Oyz)) = |x_G| = |%s| = %s$."""
        % (xa, xb, xc, xg_val, xg_val, dist_g_oyz)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Hai điểm A, B có tâm đối xứng là điểm có hoành độ bằng str_xm[cite: 22]
    vd_da_1_d = (
        "\\True Hai điểm $A, B$ có tâm đối xứng là điểm có hoành độ bằng $%s$"
        % (str_xm)
    )
    vd_da_1_s = (
        "Hai điểm $A, B$ có tâm đối xứng là điểm có hoành độ bằng $%s$"
        % (str_xm_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Tâm đối xứng của hai điểm $A$ và $B$ chính là trung điểm $M$ của đoạn thẳng $AB$. \\\\ Hoành độ của trung điểm $M$ là: \\\\ $x_M = \\frac{x_A + x_B}{2} = \\frac{%s + (%s)}{2} = %s$. \\\\ Vậy tâm đối xứng của hai điểm $A, B$ là điểm có hoành độ bằng $%s$."""
        % (xa, xb, str_xm, str_xm)
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Giá trị biểu thức T = a^2 + b^2 + c^2 là một số tự nhiên chia hết cho 6[cite: 22]
    if is_t_div_6:
        vdc_da_1_d = (
            "\\True Giá trị biểu thức $T = a^2 + b^2 + c^2$ là một số tự nhiên chia hết cho $6$"
        )
        vdc_da_1_s = (
            "Giá trị biểu thức $T = a^2 + b^2 + c^2$ là một số tự nhiên không chia hết cho $6$"
        )
    else:
        vdc_da_1_d = (
            "\\True Giá trị biểu thức $T = a^2 + b^2 + c^2$ là một số tự nhiên không chia hết cho $6$"
        )
        vdc_da_1_s = (
            "Giá trị biểu thức $T = a^2 + b^2 + c^2$ là một số tự nhiên chia hết cho $6$"
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_div_explain = (
        "chia hết cho $6$" if is_t_div_6 else "không chia hết cho $6$"
    )
    
    loigiai_vdc_1 = (
        """Vì tứ giác $ABCD$ là hình bình hành nên ta có: \\\\ $\\vec{AD} = \\vec{BC} \\Leftrightarrow \\begin{cases} x_D - x_A = x_C - x_B \\\\ y_D - y_A = y_C - y_B \\\\ z_D - z_A = z_C - z_B \\end{cases} \\Leftrightarrow \\begin{cases} a = x_D = x_A + x_C - x_B = %s + (%s) - (%s) = %s \\\\ b = y_D = y_A + y_C - y_B = %s + (%s) - (%s) = %s \\\\ c = z_D = z_A + z_C - z_B = %s + (%s) - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $D$ là $D(%s;%s;%s)$. \\\\ Khi đó giá trị của biểu thức $T = a^2 + b^2 + c^2$ là: \\\\ $T = (%s)^2 + (%s)^2 + (%s)^2 = %s + %s + %s = %s$. \\\\ Vì $%s$ %s nên mệnh đề được khẳng định là %s."""
        % (
            xa,
            xc,
            xb,
            xd,
            ya,
            yc,
            yb,
            yd,
            za,
            zc,
            zb,
            zd,
            xd,
            yd,
            zd,
            xd,
            yd,
            zd,
            xd**2,
            yd**2,
            zd**2,
            t_val,
            t_val,
            str_div_explain,
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
    