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


def bt_dang22_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    while True:
        xa = random.choice([1, 2, -1, -2])
        ya = random.choice([1, 2, 3])
        za = 0  # Chọn zA = 0 để bài toán tương tự gốc, khoảng cách AC nhỏ nhất là |xA|
    
        # Chọn vectơ AB = (u1, u2, u3)
        u1 = random.choice([3, 4, -3, -4])
        u2 = random.choice([-2, 2, -1, 1])
        u3 = random.choice([3, 4, -3, -4])
    
        xb = xa + u1
        yb = ya + u2
        zb = za + u3
    
        lab_sq = u1**2 + u2**2 + u3**2
        # Cần |AB| nguyên để phép tính căn thức đẹp
        lab = int(math.isqrt(lab_sq))
        if lab * lab != lab_sq:
            continue
    
        # Đặt Y = t - ya. AC^2 = xa^2 + Y^2 + za^2 = xa^2 + Y^2
        # AB . AC = -u1*xa + u2*Y = u2*Y - u1*xa
        # Phương trình: \sqrt{2} * (u2*Y - u1*xa) = -lab * \sqrt{xa^2 + Y^2}
        # Bình phương: 2 * (u2*Y - u1*xa)^2 = lab^2 * (xa^2 + Y^2)
        # <=> 2*(u2^2 Y^2 - 2*u1*u2*xa Y + u1^2 xa^2) = lab^2 Y^2 + lab^2 xa^2
        # <=> (2*u2^2 - lab^2) Y^2 - 4*u1*u2*xa Y + (2*u1^2 - lab^2) xa^2 = 0
        A_eq = 2 * u2**2 - lab_sq
        B_eq = -4 * u1 * u2 * xa
        C_eq = (2 * u1**2 - lab_sq) * (xa**2)
    
        delta = B_eq**2 - 4 * A_eq * C_eq
        if delta > 0:
            sqrt_delta = int(math.isqrt(delta))
            if sqrt_delta * sqrt_delta == delta:
                # Hai nghiệm Y1, Y2
                y_sol1 = Rational(-B_eq + sqrt_delta, 2 * A_eq)
                y_sol2 = Rational(-B_eq - sqrt_delta, 2 * A_eq)
    
                # Kiểm tra điều kiện AB . AC < 0: u2*Y - u1*xa < 0
                valid_t = []
                for y_s in [y_sol1, y_sol2]:
                    if u2 * y_s - u1 * xa < 0:
                        valid_t.append(y_s + ya)
    
                if len(valid_t) == 2 and valid_t[0] != valid_t[1]:
                    t_vals = sorted(valid_t, reverse=True)
                    val_a = t_vals[0]
                    val_b = t_vals[1]
                    break
    
    # 1. Vectơ AB = (u1; u2; u3)[cite: 21]
    ab_true_x = u1
    ab_true_y = u2
    ab_true_z = u3
    
    ab_s_x = u1
    ab_s_y = -u2
    ab_s_z = u3
    
    # 2. Độ dài đoạn thẳng AC nhỏ nhất khi C là hình chiếu của A trên Oy: C_0(0; yA; 0)[cite: 21]
    # min(AC) = \sqrt{xA^2 + zA^2} = |xA| (vì zA = 0)[cite: 21]
    min_ac = abs(xa)
    min_ac_s = min_ac + 1
    
    # 3. Giá trị biểu thức 5a + 14b (với hệ số được điều chỉnh tương ứng)[cite: 21]
    # a = val_a, b = val_b (a > b)[cite: 21]
    str_val_a = format_fraction_latex(val_a.p, val_a.q)
    str_val_b = format_fraction_latex(val_b.p, val_b.q)
    
    c1_coef = 5
    c2_coef = 14
    val_expr = c1_coef * val_a + c2_coef * val_b
    str_val_expr = format_fraction_latex(val_expr.p, val_expr.q)
    bound_expr = int(val_expr) - 1
    is_expr_gt = val_expr > bound_expr
    
    # 4. Bán kính đường tròn ngoại tiếp R_ABC = BC / (2 * sin 135^\circ) = BC / \sqrt{2}[cite: 21]
    # C có tung độ lớn hơn yA (tương ứng t = val_a > ya)[cite: 21]
    # C_1 = (0; val_a; 0)
    bc_x = -xb
    bc_y = val_a - yb
    bc_z = -zb
    bc_len_sq = bc_x**2 + bc_y**2 + bc_z**2
    
    r_abc_sym = sp.sqrt(bc_len_sq) / sp.sqrt(2)
    str_r_abc = latex(r_abc_sym)
    str_r_abc_s = "\\frac{1}{2}"
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A(%s;%s;%s), B(%s;%s;%s)$. $C$ là điểm nằm trên trục $Oy$ sao cho góc giữa hai vectơ $\\vec{AB}, \\vec{AC}$ bằng $135^\\circ$. Biết rằng tung độ của các điểm $C$ thỏa mãn yêu cầu lần lượt là $a, b (a > b)$."""
        % (xa, ya, za, xb, yb, zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ AB[cite: 21]
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_true_x, ab_true_y, ab_true_z)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (ab_s_x, ab_s_y, ab_s_z)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ của vectơ $\\vec{AB}$ là: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            ab_true_x,
            ab_true_y,
            ab_true_z,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Độ dài đoạn thẳng AC nhỏ nhất bằng min_ac[cite: 21]
    th_da_1_d = "\\True Độ dài đoạn thẳng $AC$ nhỏ nhất bằng $%s$" % (min_ac)
    th_da_1_s = "\\True Độ dài đoạn thẳng $AC$ nhỏ nhất bằng $%s$" % (min_ac_s)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì điểm $C$ nằm trên trục $Oy$ nên tọa độ của điểm $C$ có dạng $C(0;t;0)$ với $t \\in \\mathbb{R}$. \\\\ Khi đó độ dài đoạn thẳng $AC$ là: \\\\ $AC = \\sqrt{(0 - %s)^2 + (t - %s)^2 + (0 - %s)^2} = \\sqrt{%s + (t - %s)^2}$. \\\\ Vì $(t - %s)^2 \\ge 0$ với mọi $t$ nên $AC \\ge \\sqrt{%s} = %s$. \\\\ Đẳng thức xảy ra khi $t = %s$. \\\\ Vậy độ dài đoạn thẳng $AC$ nhỏ nhất bằng $%s$."""
        % (
            xa,
            ya,
            za,
            xa**2 + za**2,
            ya,
            ya,
            xa**2 + za**2,
            min_ac,
            ya,
            min_ac,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Giá trị biểu thức 5a + 14b lớn hơn bound_expr[cite: 21]
    if is_expr_gt:
        vd_da_1_d = "\\True Giá trị biểu thức $5a + 14b$ lớn hơn $%s$" % (bound_expr)
        vd_da_1_s = "Giá trị biểu thức $5a + 14b$ nhỏ hơn $%s$" % (bound_expr)
    else:
        vd_da_1_d = "\\True Giá trị biểu thức $5a + 14b$ nhỏ hơn $%s$" % (bound_expr)
        vd_da_1_s = "Giá trị biểu thức $5a + 14b$ lớn hơn $%s$" % (bound_expr)
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Điểm $C(0;t;0) \\in Oy$, suy ra $\\vec{AC} = (-%s; t - %s; -%s)$. \\\\ Ta có $AB = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s$, $AC = \\sqrt{%s + (t - %s)^2}$. \\\\ Tích vô hướng: $\\vec{AB} \\cdot \\vec{AC} = (%s) \\cdot (-%s) + (%s) \\cdot (t - %s) + (%s) \\cdot (-%s) = %s(t - %s) - (%s)$. \\\\ Theo giả thiết, góc giữa $\\vec{AB}$ và $\\vec{AC}$ bằng $135^\\circ$ nên: \\\\ $\\cos(\\vec{AB}, \\vec{AC}) = \\cos 135^\\circ \\Leftrightarrow \\frac{\\vec{AB} \\cdot \\vec{AC}}{|\\vec{AB}| \\cdot |\\vec{AC}|} = -\\frac{1}{\\sqrt{2}}$ \\\\ $\\Leftrightarrow \\sqrt{2}(\\vec{AB} \\cdot \\vec{AC}) = -%s\\sqrt{%s + (t - %s)^2}$. \\\\ Bình phương hai vế và giải phương trình với điều kiện $\\vec{AB} \\cdot \\vec{AC} < 0$, ta tìm được hai giá trị của $t$ là $t = %s$ và $t = %s$. \\\\ Vì $a > b$ nên $a = %s$ và $b = %s$. \\\\ Khi đó giá trị của biểu thức là: $5a + 14b = 5 \\cdot (%s) + 14 \\cdot (%s) = %s$. \\\\ Do $%s %s %s$ nên mệnh đề được khẳng định là %s."""
        % (
            xa,
            ya,
            za,
            ab_true_x,
            ab_true_y,
            ab_true_z,
            lab,
            xa**2 + za**2,
            ya,
            ab_true_x,
            xa,
            ab_true_y,
            ya,
            ab_true_z,
            za,
            ab_true_y,
            ya,
            ab_true_x * xa + ab_true_z * za,
            lab,
            xa**2 + za**2,
            ya,
            str_val_a,
            str_val_b,
            str_val_a,
            str_val_b,
            str_val_a,
            str_val_b,
            str_val_expr,
            str_val_expr,
            ">" if is_expr_gt else "<",
            bound_expr,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Nếu điểm C có tung độ lớn hơn ya thì bán kính đường tròn ngoại tiếp tam giác ABC[cite: 21]
    vdc_da_1_d = (
        "\\True Nếu điểm $C$ có tung độ lớn hơn $%s$ thì tam giác $ABC$ có bán kính đường tròn ngoại tiếp $R_{ABC} = %s$"
        % (ya, str_r_abc)
    )
    vdc_da_1_s = (
        "Nếu điểm $C$ có tung độ lớn hơn $%s$ thì tam giác $ABC$ có bán kính đường tròn ngoại tiếp $R_{ABC} = %s$"
        % (ya, str_r_abc_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Nếu điểm $C$ có tung độ lớn hơn $%s$ thì $t = a = %s$, tức là $C(0;%s;0)$. \\\\ Khi đó độ dài cạnh $BC$ là: \\\\ $BC = \\sqrt{(0 - %s)^2 + (%s - %s)^2 + (0 - %s)^2} = %s$. \\\\ Áp dụng định lí sin trong tam giác $ABC$, ta có: \\\\ $\\frac{BC}{\\sin A} = 2 R_{ABC} \\Leftrightarrow \\frac{BC}{\\sin 135^\\circ} = 2 R_{ABC} \\Leftrightarrow R_{ABC} = \\frac{BC}{2 \\sin 135^\\circ} = \\frac{BC}{\\sqrt{2}}$. \\\\ Thay độ dài $BC$ vào, ta được bán kính đường tròn ngoại tiếp là $R_{ABC} = %s$."""
        % (
            ya,
            str_val_a,
            str_val_a,
            xb,
            str_val_a,
            yb,
            zb,
            latex(sp.sqrt(bc_len_sq)),
            str_r_abc,
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
    