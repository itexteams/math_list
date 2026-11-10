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


def bt_dang58_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C sao cho tam giác ABC vuông tại A[cite: 22]
    # AB song song với trục Ox: AB = (ab_x; 0; 0) với ab_x != 0[cite: 22]
    # AC vuông góc với AB: AC = (0; 0; ac_z) hoặc (0; ac_y; ac_z) vuông góc với Ox[cite: 22]
    # Như đề bài gốc: AB song song Ox (cùng y, cùng z), AC cùng x, cùng y (song song Oz)[cite: 22]
    while True:
        xa = random.randint(2, 5)
        ya = random.randint(2, 5)
        za = random.randint(-3, 2)
    
        # AB song song Ox
        ab_x = random.choice([-2, -1, 1, 2])
        xb = xa + ab_x
        yb = ya
        zb = za
    
        # AC song song Oz (hoặc vuông góc Ox)
        ac_z = random.choice([2, 3, 4, 5])
        xc = xa
        yc = ya
        zc = za + ac_z
    
        # Diện tích S_ABC = 1/2 * |ab_x| * |ac_z|[cite: 22]
        s_abc = Rational(abs(ab_x) * abs(ac_z), 2)
    
        # Điểm M thỏa mãn: MA - 2*MB + 3*MC = 0[cite: 22]
        # <=> (1 - 2 + 3) OM = OA - 2*OB + 3*OC <=> 2*OM = OA - 2*OB + 3*OC[cite: 22]
        zm_num = za - 2 * zb + 3 * zc
        if zm_num % 2 == 0:
            zm_val = zm_num // 2
    
            # Điểm N thuộc Ox: N(n; 0; 0). AN = (n - xa; -ya; -za)[cite: 22]
            # AN vuông góc AB: AN . AB = (n - xa) * ab_x + (-ya)*0 + (-za)*0 = 0[cite: 22]
            # Do ab_x != 0 nên n = xa => ON = |xa| = xa (do xa > 0)[cite: 22]
            on_val = xa
            break
    
    # 1. Khẳng định a: Tam giác ABC là tam giác vuông (luôn đúng theo cấu trúc)[cite: 22]
    
    # 2. Khẳng định b: Diện tích tam giác ABC[cite: 22]
    str_s_true = format_fraction_latex(s_abc.p, s_abc.q)
    s_abc_false = s_abc + random.choice([-1, 1])
    if s_abc_false <= 0:
        s_abc_false = s_abc + 2
    str_s_false = format_fraction_latex(s_abc_false.p, s_abc_false.q)
    
    # 3. Khẳng định c: Điểm M có cao độ bằng zm_val[cite: 22]
    zm_false = zm_val + random.choice([-2, -1, 1, 2])
    
    # 4. Khẳng định d: Điểm N thuộc trục Ox sao cho AN vuông góc AB thì ON = on_val[cite: 22]
    on_false = on_val + random.choice([-2, -1, 1, 2])
    if on_false <= 0:
        on_false = on_val + 3
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A(%s;%s;%s); B(%s;%s;%s); C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Tam giác ABC là tam giác vuông[cite: 22]
    nb_da_1_d = "\\True Tam giác $ABC$ là tam giác vuông"
    nb_da_1_s = "Tam giác $ABC$ là tam giác đều"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ các vectơ: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;0;0)$. \\\\ $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (0;0;%s)$. \\\\ Xét tích vô hướng của hai vectơ $\\vec{AB}$ và $\\vec{AC}$: \\\\ $\\vec{AB} \\cdot \\vec{AC} = (%s) \\cdot 0 + 0 \\cdot 0 + 0 \\cdot (%s) = 0 \\Rightarrow AB \\perp AC$. \\\\ Do đó tam giác $ABC$ là tam giác vuông tại $A$."""
        % (
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            ab_x,
            xc,
            xa,
            yc,
            ya,
            zc,
            za,
            ac_z,
            ab_x,
            ac_z,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: S_{ABC} = ...[cite: 22]
    th_da_1_d = "\\True $S_{ABC} = %s$" % (str_s_true)
    th_da_1_s = "$S_{ABC} = %s$" % (str_s_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì tam giác $ABC$ vuông tại $A$ nên diện tích tam giác $ABC$ được tính theo công thức: \\\\ $S_{ABC} = \\frac{1}{2} AB \\cdot AC$. \\\\ Ta có: \\\\ $AB = |\\vec{AB}| = \\sqrt{(%s)^2 + 0^2 + 0^2} = %s$. \\\\ $AC = |\\vec{AC}| = \\sqrt{0^2 + 0^2 + (%s)^2} = %s$. \\\\ Do đó diện tích tam giác $ABC$ là: \\\\ $S_{ABC} = \\frac{1}{2} \\cdot %s \\cdot %s = %s$."""
        % (
            ab_x,
            abs(ab_x),
            ac_z,
            abs(ac_z),
            abs(ab_x),
            abs(ac_z),
            str_s_true,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Điểm M thỏa mãn MA - 2MB + 3MC = 0 thì M có cao độ bằng zm_val[cite: 22]
    vd_da_1_d = (
        "\\True Điểm $M$ thoả mãn $\\vec{MA} - 2\\vec{MB} + 3\\vec{MC} = \\vec{0}$ thì $M$ có cao độ bằng $%s$"
        % (zm_val)
    )
    vd_da_1_s = (
        "Điểm $M$ thoả mãn $\\vec{MA} - 2\\vec{MB} + 3\\vec{MC} = \\vec{0}$ thì $M$ có cao độ bằng $%s$"
        % (zm_false)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có hệ thức vectơ: \\\\ $\\vec{MA} - 2\\vec{MB} + 3\\vec{MC} = \\vec{0} \\Leftrightarrow (\\vec{OA} - \\vec{OM}) - 2(\\vec{OB} - \\vec{OM}) + 3(\\vec{OC} - \\vec{OM}) = \\vec{0}$ \\\\ $\\Leftrightarrow 2\\vec{OM} = \\vec{OA} - 2\\vec{OB} + 3\\vec{OC} \\Leftrightarrow \\vec{OM} = \\frac{\\vec{OA} - 2\\vec{OB} + 3\\vec{OC}}{2}$. \\\\ Suy ra cao độ của điểm $M$ là: \\\\ $z_M = \\frac{z_A - 2z_B + 3z_C}{2} = \\frac{%s - 2 \\cdot (%s) + 3 \\cdot (%s)}{2} = \\frac{%s}{2} = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            za,
            zb,
            zc,
            zm_num,
            zm_val,
            zm_val,
            "=" if "\\True" in vd_da_1 else "\\neq",
            zm_val if "\\True" in vd_da_1 else zm_false,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Điểm N thuộc trục Ox sao cho AN vuông góc với AB thì ON = on_val[cite: 22]
    vdc_da_1_d = (
        "\\True Điểm $N$ thuộc trục $Ox$ sao cho $AN$ vuông góc với $AB$ thì $ON = %s$"
        % (on_val)
    )
    vdc_da_1_s = (
        "Điểm $N$ thuộc trục $Ox$ sao cho $AN$ vuông góc với $AB$ thì $ON = %s$"
        % (on_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì điểm $N$ thuộc trục $Ox$ nên tọa độ của điểm $N$ có dạng $N(n;0;0)$. \\\\ Khi đó tọa độ của vectơ $\\vec{AN}$ là: \\\\ $\\vec{AN} = (x_N - x_A; y_N - y_A; z_N - z_A) = (n - %s; -%s; -%s) = (n - %s; %s; %s)$. \\\\ Mặt khác, ta có $\\vec{AB} = (%s;0;0)$. \\\\ Đường thẳng $AN$ vuông góc với đường thẳng $AB$ khi và chỉ khi: \\\\ $\\vec{AN} \\cdot \\vec{AB} = 0 \\Leftrightarrow (n - %s) \\cdot (%s) + (%s) \\cdot 0 + (%s) \\cdot 0 = 0$ \\\\ $\\Leftrightarrow (%s)(n - %s) = 0 \\Leftrightarrow n = %s$. \\\\ Suy ra tọa độ điểm $N$ là $N(%s;0;0)$. \\\\ Khi đó khoảng cách từ gốc tọa độ $O$ đến điểm $N$ là: \\\\ $ON = |n| = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            xa,
            ya,
            za,
            xa,
            -ya,
            -za,
            ab_x,
            xa,
            ab_x,
            -ya,
            -za,
            ab_x,
            xa,
            xa,
            xa,
            on_val,
            on_val,
            "=" if "\\True" in vdc_da_1 else "\\neq",
            on_val if "\\True" in vdc_da_1 else on_false,
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
    