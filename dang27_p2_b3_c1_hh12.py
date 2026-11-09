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


def bt_dang27_p2_b3_c1_hh12(self):
    # 2. Khoảng cách hình chiếu lên (Oxy) là số nguyên đẹp (bộ ba Pythagore 3-4-5)
    while True:
        xa = random.randint(-2, 2)
        ya = random.randint(-4, 0)
        za = random.choice([-5, -4, -3])
    
        # Khoảng cách hình chiếu d_xy = 5 bằng cách chọn dx, dy là 3, 4
        dx = random.choice([-3, 3])
        dy = random.choice([-4, 4])
    
        xb = xa + dx
        yb = ya + dy
        zb = random.choice([2, 3, 4])
    
        # Tích có hướng [OA, OB]
        # OA = (xa, ya, za), OB = (xb, yb, zb)
        cp_x = ya * zb - za * yb
        cp_y = za * xb - xa * zb
        cp_z = xa * yb - ya * xb
    
        oa_sq = xa**2 + ya**2 + za**2
        ob_sq = xb**2 + yb**2 + zb**2
    
        # Đảm bảo cp_z khác 0 và tính toán rõ ràng
        if cp_z != 0 and cp_x != 0 and cp_y != 0:
            break
    
    # Độ dài MN
    d_mn = random.choice([2, 3])
    
    # 1. OA + OB
    oa_val = math.sqrt(oa_sq)
    ob_val = math.sqrt(ob_sq)
    sum_oa_ob = oa_val + ob_val
    bound_oa_ob = int(sum_oa_ob)
    is_sum_oa_ob_gt = sum_oa_ob > bound_oa_ob
    
    # 2. Vectơ u = (a; b; cp_z) cùng vuông góc với OA và OB
    # => u cùng phương với [OA, OB]. Vì cao độ bằng cp_z nên u = [OA, OB]
    # Do đó a = cp_x, b = cp_y
    u_a = cp_x
    u_b = cp_y
    val_expr_b = u_a + 2 * u_b
    bound_expr_b = val_expr_b - random.choice([1, 2])
    is_expr_b_gt = val_expr_b > bound_expr_b
    
    # 3. Điểm A' đối xứng với A qua mặt phẳng (Oxy)
    # Giữ nguyên x, y và đổi dấu z => A'(xa; ya; -za)
    xa_prime = xa
    ya_prime = ya
    za_prime = -za
    
    xa_prime_s = xa
    ya_prime_s = -ya
    za_prime_s = -za
    
    # 4. Giá trị lớn nhất của |AM - BN|:
    # Vì A và B nằm về hai phía đối với (Oxy), gọi A' là điểm đối xứng của A qua (Oxy)
    # Ta có AM = A'M, nên |AM - BN| = |A'M - BN|.
    # Tịnh tiến B theo vectơ v = NM (|v| = MN = d_mn, v // (Oxy)) thành B1 => BN = B1*M
    # |A'M - BN| = |A'M - B1*M| <= A'B1.
    # Trong đó A'B1^2 = (zA' - zB)^2 + A0B10^2
    # A0B10 <= A0B0 + B0B10 = d_xy + d_mn
    d_xy = int(math.isqrt(dx**2 + dy**2))
    max_d_xy = d_xy + d_mn
    diff_z_sq = (za_prime - zb) ** 2
    max_dist_sq = diff_z_sq + max_d_xy**2
    str_max_true = latex(sp.sqrt(max_dist_sq))
    
    # Giá trị sai thường gặp (ví dụ nhầm sang dấu cộng hoặc tính sai)
    max_dist_sq_s = max_dist_sq + random.choice([8, 10, -8])
    str_max_false = latex(sp.sqrt(max_dist_sq_s))
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hai điểm $A(%s;%s;%s)$ và $B(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: OA + OB > bound_oa_ob
    if is_sum_oa_ob_gt:
        nb_da_1_d = "\\True $OA + OB > %s$" % (bound_oa_ob)
        nb_da_1_s = "$OA + OB < %s$" % (bound_oa_ob)
    else:
        nb_da_1_d = "\\True $OA + OB < %s$" % (bound_oa_ob)
        nb_da_1_s = "$OA + OB > %s$" % (bound_oa_ob)
    
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ điểm $A(%s;%s;%s)$ và $B(%s;%s;%s)$, suy ra: \\\\ $OA = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} \\approx %s$. \\\\ $OB = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} \\approx %s$. \\\\ Khi đó: $OA + OB = \\sqrt{%s} + \\sqrt{%s} \\approx %s$. \\\\ Vì $%s %s %s$ nên mệnh đề là %s."""
        % (
            xa,
            ya,
            za,
            xb,
            yb,
            zb,
            xa,
            ya,
            za,
            oa_sq,
            str(round(oa_val, 2)).replace(".", ","),
            xb,
            yb,
            zb,
            ob_sq,
            str(round(ob_val, 2)).replace(".", ","),
            oa_sq,
            ob_sq,
            str(round(sum_oa_ob, 2)).replace(".", ","),
            str(round(sum_oa_ob, 2)).replace(".", ","),
            ">" if is_sum_oa_ob_gt else "<",
            bound_oa_ob,
            "đúng" if "\\True" in nb_da_1 else "sai",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Vector u = (a; b; cp_z) cùng vuông góc với OA, OB
    if is_expr_b_gt:
        th_da_1_d = (
            "\\True Vectơ $\\vec{u} = (a;b;%s)$ cùng vuông góc với hai vectơ $\\vec{OA}, \\vec{OB}$ thì $a + 2b > %s$"
            % (cp_z, bound_expr_b)
        )
        th_da_1_s = (
            "Vectơ $\\vec{u} = (a;b;%s)$ cùng vuông góc với hai vectơ $\\vec{OA}, \\vec{OB}$ thì $a + 2b < %s$"
            % (cp_z, bound_expr_b)
        )
    else:
        th_da_1_d = (
            "\\True Vectơ $\\vec{u} = (a;b;%s)$ cùng vuông góc với hai vectơ $\\vec{OA}, \\vec{OB}$ thì $a + 2b < %s$"
            % (cp_z, bound_expr_b)
        )
        th_da_1_s = (
            "Vectơ $\\vec{u} = (a;b;%s)$ cùng vuông góc với hai vectơ $\\vec{OA}, \\vec{OB}$ thì $a + 2b > %s$"
            % (cp_z, bound_expr_b)
        )
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có $\\vec{OA} = (%s;%s;%s)$ và $\\vec{OB} = (%s;%s;%s)$. \\\\ Vectơ cùng vuông góc với cả hai vectơ $\\vec{OA}$ và $\\vec{OB}$ cùng phương với tích có hướng $[\vec{OA}, \vec{OB}]$: \\\\ $[\\vec{OA}, \\vec{OB}] = \\left( \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & %s \\\\ %s & %s \\end{vmatrix} \\right) = (%s;%s;%s)$. \\\\ Vì vectơ $\\vec{u} = (a;b;%s)$ có cao độ bằng $%s$ nên $\\vec{u} = [\\vec{OA}, \\vec{OB}] = (%s;%s;%s)$. \\\\ Do đó ta có: $a = %s$ và $b = %s$. \\\\ Suy ra: $a + 2b = %s + 2 \\cdot (%s) = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            xa,
            ya,
            za,
            xb,
            yb,
            zb,
            ya,
            za,
            yb,
            zb,
            za,
            xa,
            zb,
            xb,
            xa,
            ya,
            xb,
            yb,
            cp_x,
            cp_y,
            cp_z,
            cp_z,
            cp_z,
            cp_x,
            cp_y,
            cp_z,
            u_a,
            u_b,
            u_a,
            u_b,
            val_expr_b,
            val_expr_b,
            ">" if is_expr_b_gt else "<",
            bound_expr_b,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Gọi A' đối xứng với A qua mặt phẳng (Oxy) thì A'
    nb_da_3_d = (
        "\\True Gọi $A'$ đối xứng với $A$ qua mặt phẳng $(Oxy)$ thì $A'(%s;%s;%s)$"
        % (xa_prime, ya_prime, za_prime)
    )
    nb_da_3_s = (
        "Gọi $A'$ đối xứng với $A$ qua mặt phẳng $(Oxy)$ thì $A'(%s;%s;%s)$"
        % (xa_prime_s, ya_prime_s, za_prime_s)
    )
    list_vd_da_1 = [nb_da_3_d, nb_da_3_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Điểm đối xứng của điểm $A(%s;%s;%s)$ qua mặt phẳng tọa độ $(Oxy)$ sẽ giữ nguyên hoành độ, tung độ và đổi dấu cao độ. \\\\ Do đó ta được tọa độ điểm $A'$ là $A'(%s;%s;%s)$."""
        % (
            xa,
            ya,
            za,
            xa_prime,
            ya_prime,
            za_prime,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Giá trị lớn nhất của |AM - BN|
    vdc_da_1_d = (
        "\\True Xét hai điểm $M$ và $N$ thay đổi thuộc mặt phẳng $(Oxy)$ sao cho $MN = %s$. Giá trị lớn nhất của $|AM - BN|$ bằng $%s$"
        % (d_mn, str_max_true)
    )
    vdc_da_1_s = (
        "Xét hai điểm $M$ và $N$ thay đổi thuộc mặt phẳng $(Oxy)$ sao cho $MN = %s$. Giá trị lớn nhất của $|AM - BN|$ bằng $%s$"
        % (d_mn, str_max_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Nhận xét: Điểm $A(%s;%s;%s)$ có $z_A = %s < 0$ và điểm $B(%s;%s;%s)$ có $z_B = %s > 0$ nên hai điểm $A, B$ nằm về hai phía khác nhau đối với mặt phẳng $(Oxy)$. \\\\ Lấy điểm $A'(%s;%s;%s)$ đối xứng với $A$ qua $(Oxy)$, khi đó với mọi điểm $M \\in (Oxy)$ ta luôn có $AM = A'M$. \\\\ Do đó: $|AM - BN| = |A'M - BN|$. \\\\ Thực hiện phép tịnh tiến theo vectơ $\\vec{u} = \\vec{NM}$ (với độ dài $|\\vec{u}| = MN = %s$ và $\\vec{u}$ song song hoặc nằm trong mặt phẳng $(Oxy)$): \\\\ Điểm $B$ biến thành điểm $B_1$, khi đó $\\vec{BB_1} = \\vec{NM} \\Rightarrow BN = B_1M$. \\\\ Áp dụng bất đẳng thức tam giác trong tam giác $A'MB_1$, ta có: \\\\ $|A'M - BN| = |A'M - B_1M| \\le A'B_1$. \\\\ Gọi $A_0(%s;%s;0)$ và $B_0(%s;%s;0)$ lần lượt là hình chiếu của $A'$ và $B$ lên mặt phẳng $(Oxy)$, ta có: \\\\ $A_0B_0 = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2} = %s$. \\\\ Hình chiếu $B_{10}$ của $B_1$ lên mặt phẳng $(Oxy)$ thỏa mãn $\\vec{B_0B_{10}} = \\vec{u}$, suy ra $B_0B_{10} = %s$. \\\\ Áp dụng bất đẳng thức tam giác trong mặt phẳng $(Oxy)$: \\\\ $A_0B_{10} \\le A_0B_0 + B_0B_{10} = %s + %s = %s$. \\\\ Khi đó độ dài đoạn $A'B_1$ đạt giá trị lớn nhất là: \\\\ $A'B_1 = \\sqrt{(z_{A'} - z_B)^2 + A_0B_{10}^2} \\le \\sqrt{(%s - (%s))^2 + %s^2} = \\sqrt{%s + %s} = %s$. \\\\ Đẳng thức xảy ra khi các điểm thẳng hàng theo đúng thứ tự. \\\\ Vậy giá trị lớn nhất của biểu thức $|AM - BN|$ bằng $%s$."""
        % (
            xa,
            ya,
            za,
            za,
            xb,
            yb,
            zb,
            zb,
            xa_prime,
            ya_prime,
            za_prime,
            d_mn,
            xa,
            ya,
            xb,
            yb,
            xb,
            xa,
            yb,
            ya,
            d_xy,
            d_mn,
            d_xy,
            d_mn,
            max_d_xy,
            za_prime,
            zb,
            max_d_xy,
            diff_z_sq,
            max_d_xy**2,
            str_max_true,
            str_max_true,
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
    