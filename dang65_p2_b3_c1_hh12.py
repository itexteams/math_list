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


def bt_dang65_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C sao cho tam giác ABC vuông tại B[cite: 24]:
    # BA . BC = 0[cite: 24]
    # Khi tam giác ABC vuông tại B, tâm đường tròn ngoại tiếp I là trung điểm cạnh huyền AC: I = (A + C) / 2[cite: 24]
    # Để tọa độ I hữu tỉ đẹp (hoặc nguyên), ta chọn A và C[cite: 24]
    while True:
        xb = random.randint(2, 6)
        yb = random.randint(1, 5)
        zb = random.randint(1, 5)
    
        # Chọn vectơ BA và BC vuông góc nhau tại B[cite: 24]
        # BA = (ba_x; ba_y; ba_z), BC = (bc_x; bc_y; bc_z) với ba_x*bc_x + ba_y*bc_y + ba_z*bc_z = 0[cite: 24]
        ba_x = random.choice([1, 2, -1, -2])
        ba_y = random.choice([-2, -1, 1, 2])
        ba_z = random.choice([1, 2, 3, -1, -2])
    
        # Tìm BC vuông góc với BA[cite: 24]
        found_c = False
        for bc_x in range(-8, 9):
            if bc_x == 0:
                continue
            for bc_y in range(-6, 7):
                rem = -(ba_x * bc_x + ba_y * bc_y)
                if ba_z != 0 and rem % ba_z == 0:
                    bc_z = rem // ba_z
                    if -8 <= bc_z <= 8 and (bc_x, bc_y, bc_z) != (0, 0, 0):
                        # Kiểm tra hai vectơ không cùng phương[cite: 24]
                        if (
                            ba_y * bc_z - ba_z * bc_y != 0
                            or ba_z * bc_x - ba_x * bc_z != 0
                        ):
                            found_c = True
                            break
            if found_c:
                break
    
        if not found_c:
            continue
    
        # Tọa độ điểm A và C: A = B + BA, C = B + BC[cite: 24]
        xa = xb + ba_x
        ya = yb + ba_y
        za = zb + ba_z
    
        xc = xb + bc_x
        yc = yb + bc_y
        zc = zb + bc_z
    
        # Điểm N đối xứng với A qua B: B là trung điểm AN => N = 2B - A[cite: 24]
        xn = 2 * xb - xa
        yn = 2 * yb - ya
        zn = 2 * zb - za
    
        # Tâm đường tròn ngoại tiếp I là trung điểm của AC[cite: 24]:
        # a = (xa + xc)/2, b = (ya + yc)/2, c = (za + zc)/2[cite: 24]
        xi_num = xa + xc
        yi_num = ya + yc
        zi_num = za + zc
    
        # Giá trị biểu thức T = a + 2b + c = (xi_num + 2*yi_num + zi_num) / 2[cite: 24]
        t_val = Rational(xi_num + 2 * yi_num + zi_num, 2)
    
        # Đảm bảo điểm B có xB != yB để tạo phương án sai cho khoảng cách đến (Oyz)[cite: 24]
        if xb != yb and xb > 0:
            break
    
    # 1. Khẳng định a: Điểm B cách mặt phẳng (Oyz) một khoảng bằng |xB|[cite: 24]
    dist_b_oyz = abs(xb)
    dist_b_oyz_s = yb if yb != dist_b_oyz and yb > 0 else dist_b_oyz + 1
    
    # 2. Khẳng định b: Điểm N đối xứng với điểm A qua B thì N có hoành độ bằng xn[cite: 24]
    xn_true = xn
    xn_false = xn + random.choice([-2, -1, 1, 2])
    
    # 3. Khẳng định c: Tam giác ABC vuông tại B (luôn đúng do BA . BC = 0)[cite: 24]
    
    # 4. Khẳng định d: Điểm I(a;b;c) là tâm đường tròn ngoại tiếp tam giác ABC thì a + 2b + c > bound[cite: 24]
    bound_d_val = 2 * math.sqrt(2)
    str_bound_d = "2\\sqrt{2}"
    is_t_gt_bound = float(t_val) > bound_d_val
    
    str_ai = format_fraction_latex(xi_num, 2)
    str_bi = format_fraction_latex(yi_num, 2)
    str_ci = format_fraction_latex(zi_num, 2)
    str_t_val = format_fraction_latex(t_val.p, t_val.q)
    
    # Nội dung câu hỏi[cite: 24]
    noidungcauhoi = (
        """Trong không gian $Oxyz$ cho các điểm $A(%s;%s;%s); B(%s;%s;%s); C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm B cách mặt phẳng (Oyz) một khoảng bằng dist_b_oyz[cite: 24]
    nb_da_1_d = (
        "\\True Điểm $B(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (xb, yb, zb, dist_b_oyz)
    )
    nb_da_1_s = (
        "Điểm $B(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng bằng $%s$"
        % (xb, yb, zb, dist_b_oyz_s)
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng tọa độ $(Oyz)$ có phương trình là $x = 0$. \\\\ Khoảng cách từ điểm $B(%s;%s;%s)$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(B, (Oyz)) = |x_B| = |%s| = %s$."""
        % (
            xb,
            yb,
            zb,
            xb,
            dist_b_oyz,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Điểm N đối xứng với điểm A qua B thì N có hoành độ bằng xn[cite: 24]
    th_da_1_d = (
        "\\True Điểm $N$ đối xứng với điểm $A$ qua $B$ thì $N$ có hoành độ bằng $%s$"
        % (xn_true)
    )
    th_da_1_s = (
        "Điểm $N$ đối xứng với điểm $A$ qua $B$ thì $N$ có hoành độ bằng $%s$"
        % (xn_false)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì điểm $N$ đối xứng với điểm $A$ qua điểm $B$ nên $B$ là trung điểm của đoạn thẳng $AN$. \\\\ Ta có: \\\\ $x_B = \\frac{x_A + x_N}{2} \\Leftrightarrow x_N = 2x_B - x_A = 2 \\cdot (%s) - (%s) = %s$. \\\\ Do đó điểm $N$ có hoành độ bằng $%s$."""
        % (
            xb,
            xa,
            xn_true,
            xn_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Tam giác ABC vuông tại B[cite: 24]
    vd_da_1_d = "\\True Tam giác $ABC$ vuông tại $B$"
    vd_da_1_s = "Tam giác $ABC$ vuông tại $A$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{BA} = (x_A - x_B; y_A - y_B; z_A - z_B) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ $\\vec{BC} = (x_C - x_B; y_C - y_B; z_C - z_B) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Xét tích vô hướng của hai vectơ: \\\\ $\\vec{BA} \\cdot \\vec{BC} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s + (%s) + (%s) = 0$. \\\\ Vì $\\vec{BA} \\cdot \\vec{BC} = 0$ nên $\\vec{BA} \\perp \\vec{BC}$, hay $BA \\perp BC$. \\\\ Do đó tam giác $ABC$ là tam giác vuông tại $B$."""
        % (
            xa,
            xb,
            ya,
            yb,
            za,
            zb,
            ba_x,
            ba_y,
            ba_z,
            xc,
            xb,
            yc,
            yb,
            zc,
            zb,
            bc_x,
            bc_y,
            bc_z,
            ba_x,
            bc_x,
            ba_y,
            bc_y,
            ba_z,
            bc_z,
            ba_x * bc_x,
            ba_y * bc_y,
            ba_z * bc_z,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm I(a;b;c) là tâm đường tròn ngoại tiếp tam giác ABC thì a + 2b + c > 2\sqrt{2}[cite: 24]
    if is_t_gt_bound:
        vdc_da_1_d = (
            "\\True Điểm $I(a;b;c)$ là tâm đường tròn ngoại tiếp tam giác $ABC$ thì $a + 2b + c > %s$"
            % (str_bound_d)
        )
        vdc_da_1_s = (
            "Điểm $I(a;b;c)$ là tâm đường tròn ngoại tiếp tam giác $ABC$ thì $a + 2b + c < %s$"
            % (str_bound_d)
        )
    else:
        vdc_da_1_d = (
            "\\True Điểm $I(a;b;c)$ là tâm đường tròn ngoại tiếp tam giác $ABC$ thì $a + 2b + c < %s$"
            % (str_bound_d)
        )
        vdc_da_1_s = (
            "Điểm $I(a;b;c)$ là tâm đường tròn ngoại tiếp tam giác $ABC$ thì $a + 2b + c > %s$"
            % (str_bound_d)
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì tam giác $ABC$ vuông tại $B$ nên tâm đường tròn ngoại tiếp $I$ của tam giác $ABC$ chính là trung điểm của cạnh huyền $AC$. \\\\ Tọa độ của điểm $I(a;b;c)$ là: \\\\ $\\begin{cases} a = \\frac{x_A + x_C}{2} = \\frac{%s + (%s)}{2} = %s \\\\ b = \\frac{y_A + y_C}{2} = \\frac{%s + (%s)}{2} = %s \\\\ c = \\frac{z_A + z_C}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases} \\Rightarrow I\\left(%s;%s;%s\\right)$. \\\\ Khi đó giá trị của biểu thức $a + 2b + c$ là: \\\\ $a + 2b + c = %s + 2 \\cdot \\left(%s\\right) + %s = %s \\approx %s$. \\\\ Ta có $%s \\approx 2,83$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            xa,
            xc,
            str_ai,
            ya,
            yc,
            str_bi,
            za,
            zc,
            str_ci,
            str_ai,
            str_bi,
            str_ci,
            str_ai,
            str_bi,
            str_ci,
            str_t_val,
            str(round(float(t_val), 2)).replace(".", ","),
            str_bound_d,
            str(round(float(t_val), 2)).replace(".", ","),
            ">" if is_t_gt_bound else "<",
            str_bound_d,
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
    