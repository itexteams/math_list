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


def bt_dang73_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C[cite: 22]
    # Nhận xét từ bài gốc: ba điểm cùng nằm trên mặt phẳng y = y0 (ở đề gốc là y = 4)[cite: 22]
    # A(xa; y0; za), B(xb; y0; za), C(xc; y0; zc) với AB cùng cao độ za[cite: 22]
    # Khi đó AB song song hoặc nằm trên đường thẳng z = za, y = y0; độ dài đáy AB = |xa - xb|, chiều cao h = |zc - za|[cite: 22]
    # Diện tích S_ABC = 1/2 * AB * |zc - za| = 1/2 * |xa - xb| * |zc - za|[cite: 22]
    while True:
        y0 = random.randint(3, 5)
        za = random.randint(-2, 0)
        zc = random.randint(3, 7)
    
        # Chiều dài đáy AB: |xa - xb| chẵn hoặc số nguyên đẹp để S_ABC nguyên[cite: 22]
        ab_len = random.choice([2, 4, 6])
        xa = random.randint(2, 5)
        xb = xa - ab_len
    
        # Điểm C nằm giữa về hoành độ hoặc tùy ý[cite: 22]
        xc = (xa + xb) // 2
    
        # Khoảng cách từ A đến gốc tọa độ O[cite: 22]
        oa_sq = xa**2 + y0**2 + za**2
        oa_val = math.sqrt(oa_sq)
    
        # Trọng tâm G: zG = (za + za + zc)/3 = (2*za + zc)/3[cite: 22]
        zg_num = 2 * za + zc
    
        # Diện tích S_ABC: đáy AB = ab_len, chiều cao h = zc - za[cite: 22]
        h_c = zc - za
        s_abc = (ab_len * h_c) // 2
    
        # M trên (Oxz) để MA^2 + MB^2 + MC^2 nhỏ nhất[cite: 22]
        # Ta có: MA^2 + MB^2 + MC^2 = 3*MG^2 + GA^2 + GB^2 + GC^2[cite: 22]
        # Đạt GTNN khi M là hình chiếu của G lên (Oxz) => M(xG; 0; zG)[cite: 22]
        # Cao độ của M chính là cao độ của G: zM = zG = (2*za + zc)/3[cite: 22]
        zg_val = Rational(zg_num, 3)
    
        if (
            (xa, y0, za) != (xb, y0, za)
            and (xa, y0, za) != (xc, y0, zc)
            and s_abc > 0
        ):
            break
    
    # 1. Khẳng định a: Điểm A cách gốc tọa độ một khoảng lớn hơn bound_oa[cite: 22]
    bound_oa = math.floor(oa_val)
    is_oa_gt = oa_val > bound_oa
    
    # 2. Khẳng định b: G có cao độ dương hay âm[cite: 22]
    is_zg_positive = zg_num > 0
    
    # 3. Khẳng định c: S_ABC có giá trị là một số nguyên lớn hơn / nhỏ hơn bound_s[cite: 22]
    bound_s = s_abc - random.choice([1, 2])
    is_s_gt = s_abc > bound_s
    
    # 4. Khẳng định d: Điểm M có cao độ nhỏ hơn / lớn hơn bound_zm[cite: 22]
    bound_zm = math.ceil(float(zg_val))
    if bound_zm == float(zg_val):
        bound_zm += 1
    is_zm_lt = float(zg_val) < bound_zm
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Trong không gian với hệ toạ độ $Oxyz$, cho 3 điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$."""
        % (xa, y0, za, xb, y0, za, xc, y0, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm A cách gốc tọa độ một khoảng lớn hơn bound_oa[cite: 22]
    if is_oa_gt:
        nb_da_1_d = (
            "\\True Điểm $A$ cách gốc tọa độ một khoảng lớn hơn $%s$" % (bound_oa)
        )
        nb_da_1_s = (
            "Điểm $A$ cách gốc tọa độ một khoảng nhỏ hơn $%s$" % (bound_oa)
        )
    else:
        nb_da_1_d = (
            "\\True Điểm $A$ cách gốc tọa độ một khoảng nhỏ hơn $%s$" % (bound_oa)
        )
        nb_da_1_s = (
            "Điểm $A$ cách gốc tọa độ một khoảng lớn hơn $%s$" % (bound_oa)
        )
    
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Khoảng cách từ gốc tọa độ $O(0;0;0)$ đến điểm $A(%s;%s;%s)$ là: \\\\ $OA = \\sqrt{x_A^2 + y_A^2 + z_A^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} \\approx %s$. \\\\ Vì $%s %s %s$ nên mệnh đề là %s."""
        % (
            xa,
            y0,
            za,
            xa,
            y0,
            za,
            oa_sq,
            str(round(oa_val, 2)).replace(".", ","),
            str(round(oa_val, 2)).replace(".", ","),
            ">" if is_oa_gt else "<",
            bound_oa,
            "đúng" if "\\True" in nb_da_1 else "sai",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: G có cao độ dương hay âm[cite: 22]
    if is_zg_positive:
        th_da_1_d = (
            "\\True Gọi $G$ là trọng tâm của tam giác $ABC$ thì $G$ có cao độ dương"
        )
        th_da_1_s = (
            "Gọi $G$ là trọng tâm của tam giác $ABC$ thì $G$ có cao độ âm"
        )
    else:
        th_da_1_d = (
            "\\True Gọi $G$ là trọng tâm của tam giác $ABC$ thì $G$ có cao độ âm"
        )
        th_da_1_s = (
            "Gọi $G$ là trọng tâm của tam giác $ABC$ thì $G$ có cao độ dương"
        )
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    str_zg_latex = format_fraction_latex(zg_num, 3)
    
    loigiai_th_1 = (
        """Tọa độ trọng tâm $G$ của tam giác $ABC$ có cao độ là: \\\\ $z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{(%s) + (%s) + (%s)}{3} = %s$. \\\\ Vì $z_G %s 0$ nên cao độ của $G$ là số %s. \\\\ Do đó mệnh đề là %s."""
        % (
            za,
            za,
            zc,
            str_zg_latex,
            ">" if is_zg_positive else "<",
            "dương" if is_zg_positive else "âm",
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: S_ABC có giá trị là một số nguyên lớn hơn / nhỏ hơn bound_s[cite: 22]
    if is_s_gt:
        vd_da_1_d = (
            "\\True $S_{ABC}$ có giá trị là một số nguyên lớn hơn $%s$" % (bound_s)
        )
        vd_da_1_s = (
            "$S_{ABC}$ có giá trị là một số nguyên nhỏ hơn $%s$" % (bound_s)
        )
    else:
        vd_da_1_d = (
            "\\True $S_{ABC}$ có giá trị là một số nguyên nhỏ hơn $%s$" % (bound_s)
        )
        vd_da_1_s = (
            "$S_{ABC}$ có giá trị là một số nguyên lớn hơn $%s$" % (bound_s)
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    # Tính tích có hướng [AB, AC] để tính diện tích chuẩn xác[cite: 22]
    ab_vec_x = xb - xa
    ab_vec_y = 0
    ab_vec_z = 0
    
    ac_vec_x = xc - xa
    ac_vec_y = 0
    ac_vec_z = zc - za
    
    cp_y = ab_vec_z * ac_vec_x - ab_vec_x * ac_vec_z  # Tọa độ tích có hướng chỉ có thành phần y[cite: 22]
    cp_len = abs(cp_y)
    
    loigiai_vd_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (%s - (%s); %s - (%s); %s - (%s)) = (%s;0;0)$. \\\\ $\\vec{AC} = (%s - (%s); %s - (%s); %s - (%s)) = (%s;0;%s)$. \\\\ Tích có hướng của hai vectơ $\\vec{AB}$ và $\\vec{AC}$ là: \\\\ $[\\vec{AB}, \\vec{AC}] = \\left( \\begin{vmatrix} 0 & 0 \\\\ 0 & %s \\end{vmatrix}; \\begin{vmatrix} 0 & %s \\\\ %s & %s \\end{vmatrix}; \\begin{vmatrix} %s & 0 \\\\ %s & 0 \\end{vmatrix} \\right) = (0; %s; 0)$. \\\\ Khi đó diện tích tam giác $ABC$ là: \\\\ $S_{ABC} = \\frac{1}{2} \\left|[\\vec{AB}, \\vec{AC}]\\right| = \\frac{1}{2} \\sqrt{0^2 + (%s)^2 + 0^2} = \\frac{1}{2} \\cdot %s = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            xb,
            xa,
            y0,
            y0,
            za,
            za,
            ab_vec_x,
            xc,
            xa,
            y0,
            y0,
            zc,
            za,
            ac_vec_x,
            ac_vec_z,
            ac_vec_z,
            ab_vec_x,
            ac_vec_z,
            ac_vec_x,
            ab_vec_x,
            ac_vec_x,
            cp_y,
            cp_y,
            cp_len,
            s_abc,
            s_abc,
            ">" if is_s_gt else "<",
            bound_s,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Tồn tại điểm M nằm trên mặt phẳng (Oxz) sao cho MA^2 + MB^2 + MC^2 nhỏ nhất, khi đó M có cao độ nhỏ hơn bound_zm[cite: 22]
    if is_zm_lt:
        vdc_da_1_d = (
            "\\True Tồn tại điểm $M$ nằm trên mặt phẳng $(Oxz)$ sao cho $MA^2 + MB^2 + MC^2$ nhỏ nhất, khi đó $M$ có cao độ nhỏ hơn $%s$"
            % (bound_zm)
        )
        vdc_da_1_s = (
            "Tồn tại điểm $M$ nằm trên mặt phẳng $(Oxz)$ sao cho $MA^2 + MB^2 + MC^2$ nhỏ nhất, khi đó $M$ có cao độ lớn hơn $%s$"
            % (bound_zm)
        )
    else:
        vdc_da_1_d = (
            "\\True Tồn tại điểm $M$ nằm trên mặt phẳng $(Oxz)$ sao cho $MA^2 + MB^2 + MC^2$ nhỏ nhất, khi đó $M$ có cao độ lớn hơn $%s$"
            % (bound_zm)
        )
        vdc_da_1_s = (
            "Tồn tại điểm $M$ nằm trên mặt phẳng $(Oxz)$ sao cho $MA^2 + MB^2 + MC^2$ nhỏ nhất, khi đó $M$ có cao độ nhỏ hơn $%s$"
            % (bound_zm)
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    xg_num = xa + xb + xc
    str_xg_latex = format_fraction_latex(xg_num, 3)
    
    loigiai_vdc_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$, ta có: \\\\ $G\\left(\\frac{x_A + x_B + x_C}{3}; \\frac{y_A + y_B + y_C}{3}; \\frac{z_A + z_B + z_C}{3}\\right) = G\\left(%s; %s; %s\\right)$. \\\\ Với điểm $M$ bất kì, ta có biến đổi vectơ: \\\\ $MA^2 + MB^2 + MC^2 = (\\vec{MG} + \\vec{GA})^2 + (\\vec{MG} + \\vec{GB})^2 + (\\vec{MG} + \\vec{GC})^2$ \\\\ $= 3MG^2 + 2\\vec{MG}(\\vec{GA} + \\vec{GB} + \\vec{GC}) + GA^2 + GB^2 + GC^2$ \\\\ $= 3MG^2 + GA^2 + GB^2 + GC^2$ (do $\\vec{GA} + \\vec{GB} + \\vec{GC} = \\vec{0}$). \\\\ Vì các điểm $A, B, C$ và $G$ cố định nên $GA^2 + GB^2 + GC^2$ không đổi, do đó biểu thức nhỏ nhất khi và chỉ khi $MG$ ngắn nhất. \\\\ Do điểm $M$ nằm trên mặt phẳng tọa độ $(Oxz)$ nên $MG$ ngắn nhất khi $M$ là hình chiếu vuông góc của điểm $G$ lên mặt phẳng $(Oxz)$. \\\\ Suy ra tọa độ điểm $M$ là $M(x_G; 0; z_G) = M\\left(%s; 0; %s\\right)$. \\\\ Cao độ của điểm $M$ là $z_M = %s \\approx %s$. \\\\ Vì $%s %s %s$ nên mệnh đề là %s."""
        % (
            str_xg_latex,
            y0,
            str_zg_latex,
            str_xg_latex,
            str_zg_latex,
            str_zg_latex,
            str(round(float(zg_val), 2)).replace(".", ","),
            str(round(float(zg_val), 2)).replace(".", ","),
            "<" if is_zm_lt else ">",
            bound_zm,
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
    