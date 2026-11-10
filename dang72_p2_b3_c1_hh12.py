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


def bt_dang72_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    while True:
        xa = random.choice([1, 2, 3])
        ya = 0
        za = 0
    
        xb = 0
        yb = random.choice([2, 3, 4])
        zb = 0
    
        xc = 0
        yc = 0
        zc = random.choice([3, 6])  # Chia hết cho 3[cite: 21]
    
        # AC^2 = xa^2 + zc^2[cite: 21]
        ac_sq = xa**2 + zc**2
    
        # Trọng tâm G: zG = (0 + 0 + zc) / 3[cite: 21]
        zg = zc // 3
    
        # Thể tích V_OABC = (xa * yb * zc) / 6[cite: 21]
        v_num = xa * yb * zc
        v_rat = Rational(v_num, 6)
        v_float = float(v_rat)
    
        # Hệ số vế phải của phương trình mặt cầu trong câu d: R^2 = 2 * xa^2[cite: 21]
        r_sq = 2 * (xa**2)
    
        if ac_sq > 0:
            break
    
    # 1. Khẳng định a: AC = sqrt(ac_sq)[cite: 21]
    str_ac_true = latex(sp.sqrt(ac_sq))
    str_ac_false = latex(sp.sqrt(ac_sq + random.choice([-2, -1, 1, 2])))
    if str_ac_false == str_ac_true:
        str_ac_false = "\\sqrt{10}"[cite: 21]
    
    # 2. Khẳng định b: Trọng tâm tam giác ABC có cao độ bằng zg[cite: 21]
    zg_false = zg + random.choice([-1, 1])
    
    # 3. Khẳng định c: V_OABC > sqrt(2)[cite: 21]
    val_sqrt2 = math.sqrt(2)
    is_v_gt_sqrt2 = v_float > val_sqrt2
    
    # 4. Khẳng định d: Hệ thức (x + xa)^2 + (y - yb)^2 + (z - zc)^2 = r_sq[cite: 21]
    str_sign_x = "+ %s" % (xa) if xa > 0 else "- %s" % (-xa)
    str_sign_y = "- %s" % (yb) if yb > 0 else "+ %s" % (-yb)
    str_sign_z = "- %s" % (zc) if zc > 0 else "+ %s" % (-zc)
    
    str_d_true = "(x %s)^2 + (y %s)^2 + (z %s)^2 = %s" % (
        str_sign_x,
        str_sign_y,
        str_sign_z,
        r_sq,
    )
    
    r_sq_false = r_sq + random.choice([-2, -1, 1, 2])
    if r_sq_false <= 0:
        r_sq_false = r_sq + 3
    str_d_false = "(x %s)^2 + (y %s)^2 + (z %s)^2 = %s" % (
        str_sign_x,
        str_sign_y,
        str_sign_z,
        r_sq_false,
    )
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho ba điểm $A(%s;0;0), C(0;0;%s), B(0;%s;0)$."""
        % (xa, zc, yb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Độ dài đoạn AC[cite: 21]
    nb_da_1_d = "\\True $AC = %s$" % (str_ac_true)
    nb_da_1_s = "$AC = %s$" % (str_ac_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Khoảng cách giữa hai điểm $A(%s;0;0)$ và $C(0;0;%s)$ là: \\\\ $AC = \\sqrt{(x_C - x_A)^2 + (y_C - y_A)^2 + (z_C - z_A)^2} = \\sqrt{(0 - %s)^2 + (0 - 0)^2 + (%s - 0)^2} = \\sqrt{%s} = %s$."""
        % (
            xa,
            zc,
            xa,
            zc,
            ac_sq,
            str_ac_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Trọng tâm tam giác ABC có cao độ bằng zg[cite: 21]
    th_da_1_d = (
        "\\True Trọng tâm tam giác $ABC$ có cao độ bằng $%s$" % (zg)
    )
    th_da_1_s = (
        "Trọng tâm tam giác $ABC$ có cao độ bằng $%s$" % (zg_false)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$. Cao độ của điểm $G$ là: \\\\ $z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{0 + 0 + %s}{3} = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            zc,
            zg,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Thể tích khối tứ diện OABC > sqrt(2)[cite: 21]
    if is_v_gt_sqrt2:
        vd_da_1_d = "\\True $V_{OABC} > \\sqrt{2}$"
        vd_da_1_s = "$V_{OABC} < \\sqrt{2}$"
    else:
        vd_da_1_d = "\\True $V_{OABC} < \\sqrt{2}$"
        vd_da_1_s = "$V_{OABC} > \\sqrt{2}$"
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    str_v_val = format_fraction_latex(v_rat.p, v_rat.q)
    
    loigiai_vd_1 = (
        """Vì ba điểm $A \\in Ox, B \\in Oy, C \\in Oz$ nên tứ diện $OABC$ có ba cạnh $OA, OB, OC$ đôi một vuông góc tại gốc tọa độ $O$. \\\\ Độ dài các cạnh là: $OA = %s, OB = %s, OC = %s$. \\\\ Thể tích khối tứ diện $OABC$ là: \\\\ $V_{OABC} = \\frac{1}{6} OA \\cdot OB \\cdot OC = \\frac{1}{6} \\cdot %s \\cdot %s \\cdot %s = %s \\approx %s$. \\\\ Ta có $\\sqrt{2} \\approx 1,41$. \\\\ Vì $%s %s \\sqrt{2}$ nên khẳng định là %s."""
        % (
            xa,
            yb,
            zc,
            xa,
            yb,
            zc,
            str_v_val,
            str(round(v_float, 2)).replace(".", ","),
            str_v_val,
            ">" if is_v_gt_sqrt2 else "<",
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tồn tại điểm M(x;y;z) thỏa mãn MA^2 = MB^2 + MC^2 thì ...[cite: 21]
    vdc_da_1_d = (
        "\\True Tồn tại điểm $M(x;y;z)$ thỏa mãn $MA^2 = MB^2 + MC^2$ thì ta có hệ thức $%s$"
        % (str_d_true)
    )
    vdc_da_1_s = (
        "Tồn tại điểm $M(x;y;z)$ thỏa mãn $MA^2 = MB^2 + MC^2$ thì ta có hệ thức $%s$"
        % (str_d_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Với điểm $M(x;y;z)$, ta có bình phương khoảng cách: \\\\ $MA^2 = (x - %s)^2 + y^2 + z^2 = x^2 - %sx + %s + y^2 + z^2$. \\\\ $MB^2 = x^2 + (y - %s)^2 + z^2 = x^2 + y^2 - %sy + %s + z^2$. \\\\ $MC^2 = x^2 + y^2 + (z - %s)^2 = x^2 + y^2 + z^2 - %sz + %s$. \\\\ Khi đó: \\\\ $MA^2 = MB^2 + MC^2 \\Leftrightarrow (x - %s)^2 + y^2 + z^2 = \\left[x^2 + (y - %s)^2 + z^2\\right] + \\left[x^2 + y^2 + (z - %s)^2\\right]$ \\\\ $\\Leftrightarrow x^2 - %sx + %s + y^2 + z^2 = 2x^2 + 2y^2 + 2z^2 - %sy - %sz + %s$ \\\\ $\\Leftrightarrow x^2 + y^2 + z^2 + %sx - %sy - %sz + %s = 0$ \\\\ $\\Leftrightarrow (x %s)^2 + (y %s)^2 + (z %s)^2 = %s^2 + %s^2 + %s^2 - (%s) = %s$. \\\\ Do đó hệ thức thỏa mãn là $%s$. Mệnh đề là %s."""
        % (
            xa,
            2 * xa,
            xa**2,
            yb,
            2 * yb,
            yb**2,
            zc,
            2 * zc,
            zc**2,
            xa,
            yb,
            zc,
            2 * xa,
            xa**2,
            2 * yb,
            2 * zc,
            yb**2 + zc**2,
            2 * xa,
            2 * yb,
            2 * zc,
            yb**2 + zc**2 - xa**2,
            str_sign_x,
            str_sign_y,
            str_sign_z,
            xa,
            yb,
            zc,
            yb**2 + zc**2 - xa**2,
            r_sq,
            str_d_true,
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
    