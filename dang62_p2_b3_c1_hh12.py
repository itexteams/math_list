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


def bt_dang62_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    while True:
        xa = random.randint(6, 12)
        ya = random.randint(4, 9)
        za = random.randint(15, 30)
    
        yb = ya - random.randint(2, 5)
    
        # Khoảng cách d(A, (Oyz)) = xa[cite: 21]
        bound_a = xa - random.choice([1, 2, 3])
    
        # OA^2
        oa_sq = xa**2 + ya**2 + za**2
    
        # Giá trị nhỏ nhất của AB là min_ab = |ya - yb|[cite: 21]
        min_ab = abs(ya - yb)
    
        # T = a - 2b + c tại M(0; ya; za) là val_t = za - 2*ya[cite: 21]
        val_t = za - 2 * ya
    
        if val_t > 0 and min_ab >= 2:
            break
    
    # 1. Khẳng định a: Điểm A cách mặt phẳng (Oyz) một khoảng lớn hơn bound_a[cite: 21]
    dist_a_oyz = xa
    is_dist_gt = dist_a_oyz > bound_a
    
    # 2. Khẳng định b: OA = sqrt(oa_sq)[cite: 21]
    oa_sym = sp.sqrt(oa_sq)
    str_oa_true = latex(oa_sym)
    
    # Tạo giá trị sai cho OA[cite: 21]
    oa_false_sq = oa_sq + random.choice([-25, -20, 20, 25])
    if oa_false_sq <= 0:
        oa_false_sq = oa_sq + 15
    str_oa_false = latex(sp.sqrt(oa_false_sq))
    if str_oa_false == str_oa_true:
        str_oa_false = "6\\sqrt{29}"[cite: 21]
    
    # 3. Khẳng định c: AB >= min_ab[cite: 21]
    min_ab_s = min_ab + random.choice([-1, 1])
    
    # 4. Khẳng định d: T = a - 2b + c là một số tự nhiên chia hết cho 5[cite: 21]
    is_t_div_5 = (val_t % 5 == 0)
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$ cho hai điểm $A(%s;%s;%s), B(%s;%s;b)$. Gọi $M(a;b;c)$ là điểm trên mặt phẳng $(Oyz)$."""
        % (xa, ya, za, xa, yb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm A cách mặt phẳng (Oyz) một khoảng lớn hơn bound_a[cite: 21]
    if is_dist_gt:
        nb_da_1_d = (
            "\\True Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng lớn hơn $%s$"
            % (xa, ya, za, bound_a)
        )
        nb_da_1_s = (
            "Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng nhỏ hơn $%s$"
            % (xa, ya, za, bound_a)
        )
    else:
        nb_da_1_d = (
            "\\True Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng nhỏ hơn $%s$"
            % (xa, ya, za, bound_a)
        )
        nb_da_1_s = (
            "Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oyz)$ một khoảng lớn hơn $%s$"
            % (xa, ya, za, bound_a)
        )
    
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng tọa độ $(Oyz)$ có phương trình là $x = 0$. \\\\ Khoảng cách từ điểm $A(%s;%s;%s)$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(A, (Oyz)) = |x_A| = |%s| = %s$. \\\\ Vì $%s %s %s$ nên mệnh đề là %s."""
        % (
            xa,
            ya,
            za,
            xa,
            dist_a_oyz,
            dist_a_oyz,
            ">" if is_dist_gt else "<",
            bound_a,
            "đúng" if "\\True" in nb_da_1 else "sai",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: OA = str_oa_true[cite: 21]
    th_da_1_d = "\\True $OA = %s$" % (str_oa_true)
    th_da_1_s = "$OA = %s$" % (str_oa_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Khoảng cách từ gốc tọa độ $O(0;0;0)$ đến điểm $A(%s;%s;%s)$ là: \\\\ $OA = \\sqrt{x_A^2 + y_A^2 + z_A^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            xa,
            ya,
            za,
            xa,
            ya,
            za,
            oa_sq,
            str_oa_true,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: AB >= min_ab[cite: 21]
    vd_da_1_d = "\\True $AB \\ge %s$" % (min_ab)
    vd_da_1_s = "$AB \\ge %s$" % (min_ab_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có tọa độ điểm $A(%s;%s;%s)$ và điểm $B(%s;%s;b)$. \\\\ Độ dài đoạn thẳng $AB$ được tính theo công thức: \\\\ $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} = \\sqrt{(%s - %s)^2 + (%s - %s)^2 + (b - %s)^2}$ \\\\ $= \\sqrt{0 + (%s)^2 + (b - %s)^2} = \\sqrt{%s + (b - %s)^2}$. \\\\ Vì $(b - %s)^2 \\ge 0$ với mọi số thực $b$ nên: \\\\ $AB = \\sqrt{%s + (b - %s)^2} \\ge \\sqrt{%s} = %s$. \\\\ Dấu đẳng thức xảy ra khi $b = %s$. \\\\ Do đó khẳng định là %s."""
        % (
            xa,
            ya,
            za,
            xa,
            yb,
            xa,
            xa,
            yb,
            ya,
            za,
            yb - ya,
            za,
            (yb - ya) ** 2,
            za,
            za,
            (yb - ya) ** 2,
            za,
            (yb - ya) ** 2,
            min_ab,
            za,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Khi AM ngắn nhất thì T = a - 2b + c là số tự nhiên chia hết cho 5[cite: 21]
    if is_t_div_5:
        vdc_da_1_d = (
            "\\True Khi độ dài đoạn $AM$ ngắn nhất thì giá trị biểu thức $T = a - 2b + c$ là một số tự nhiên chia hết cho $5$"
        )
        vdc_da_1_s = (
            "Khi độ dài đoạn $AM$ ngắn nhất thì giá trị biểu thức $T = a - 2b + c$ là một số tự nhiên không chia hết cho $5$"
        )
    else:
        vdc_da_1_d = (
            "\\True Khi độ dài đoạn $AM$ ngắn nhất thì giá trị biểu thức $T = a - 2b + c$ là một số tự nhiên không chia hết cho $5$"
        )
        vdc_da_1_s = (
            "Khi độ dài đoạn $AM$ ngắn nhất thì giá trị biểu thức $T = a - 2b + c$ là một số tự nhiên chia hết cho $5$"
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì điểm $M(a;b;c)$ nằm trên mặt phẳng tọa độ $(Oyz)$ nên hoành độ của điểm $M$ luôn bằng $0$, tức là $a = 0$, do đó $M(0;b;c)$. \\\\ Khi đó độ dài đoạn thẳng $AM$ là: \\\\ $AM = \\sqrt{(0 - %s)^2 + (b - %s)^2 + (c - %s)^2} = \\sqrt{%s + (b - %s)^2 + (c - %s)^2}$. \\\\ Nhận thấy $(b - %s)^2 \\ge 0$ và $(c - %s)^2 \\ge 0$ với mọi $b, c$. \\\\ Do đó $AM \\ge \\sqrt{%s} = %s$. \\\\ Độ dài đoạn thẳng $AM$ ngắn nhất khi $M$ là hình chiếu vuông góc của điểm $A$ lên mặt phẳng $(Oyz)$, tức là: \\\\ $\\begin{cases} a = 0 \\\\ b = y_A = %s \\\\ c = z_A = %s \\end{cases} \\Rightarrow M(0;%s;%s)$. \\\\ Khi đó giá trị của biểu thức $T$ là: \\\\ $T = a - 2b + c = 0 - 2 \\cdot (%s) + (%s) = %s$. \\\\ Vì $%s$ %s chia hết cho $5$ nên khẳng định là %s."""
        % (
            xa,
            ya,
            za,
            xa**2,
            ya,
            za,
            ya,
            za,
            xa**2,
            xa,
            ya,
            za,
            ya,
            za,
            ya,
            za,
            val_t,
            val_t,
            "là một số tự nhiên" if is_t_div_5 else "không",
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
    