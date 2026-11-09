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


def bt_dang26_p2_b3_c1_hh12(self):
    # Sinh ngẫu nhiên dữ liệu hình hộp ABCD.A'B'C'D'
    # Chọn các kích thước cạnh a_val, b_val, h_val là số nguyên dương chẵn để tâm I có tọa độ nguyên đẹp
    # A(0;0;0), B(a;0;0), D(0;b;0), D'(0;b;h)
    while True:
        a_val = random.choice([2, 4])
        b_val = random.choice([2, 4])
        h_val = random.choice([2, 4])
    
        xa, ya, za = 0, 0, 0
        xb, yb, zb = a_val, 0, 0
        xd, yd, zd = 0, b_val, 0
        xd_p, yd_p, zd_p = 0, b_val, h_val
    
        # Đáy ABCD là hình chữ nhật: C = (a_val, b_val, 0)
        xc, yc, zc = a_val, b_val, 0
    
        # Vectơ DD' = (0, 0, h_val)
        # A' = (0, 0, h_val), B' = (a_val, 0, h_val), C' = (a_val, b_val, h_val)
        xa_p, ya_p, za_p = 0, 0, h_val
        xb_p, yb_p, zb_p = a_val, 0, h_val
        xc_p, yc_p, zc_p = a_val, b_val, h_val
    
        # Tâm I là trung điểm đường chéo AC'
        # I = ((0+a_val)/2; (0+b_val)/2; (0+h_val)/2)
        xi = a_val // 2
        yi = b_val // 2
        zi = h_val // 2
    
        # Vectơ AB' = (a_val, 0, h_val)
        # Vectơ BD = (-a_val, b_val, 0)
        # Tích vô hướng AB' . BD = -a_val^2
        # |AB'| = sqrt(a_val^2 + h_val^2), |BD| = sqrt(a_val^2 + b_val^2)
        # cos(AB', BD) = (-a_val^2) / (sqrt(a_val^2 + h_val^2) * sqrt(a_val^2 + b_val^2))
        dot_prod = -a_val**2
        len_ab_p_sq = a_val**2 + h_val**2
        len_bd_sq = a_val**2 + b_val**2
    
        # Tính góc chính xác bằng độ nếu cos ra giá trị đặc biệt (-1/2 => 120 độ)
        # Nếu a_val == b_val == h_val: cos = -a^2 / (2a^2) = -1/2 => góc bằng 120 độ
        cos_val = Rational(dot_prod, 1) / (
            sp.sqrt(len_ab_p_sq) * sp.sqrt(len_bd_sq)
        )
        is_120_deg = a_val == b_val and b_val == h_val
    
        if a_val > 0 and b_val > 0 and h_val > 0:
            break
    
    # 1. Tọa độ điểm A': A'(0; 0; h_val)[cite: 23]
    xa_p_s = 0
    ya_p_s = 0
    za_p_s = h_val + random.choice([-1, 1])
    
    # 2. Tâm I của hình hộp: I(xi; yi; zi)[cite: 23]
    # Tọa độ sai: ví dụ giữ nguyên h_val như đề gốc I(1; 1; 2) khi h_val = 2[cite: 23]
    xi_s = xi
    yi_s = yi
    zi_s = h_val if zi != h_val else zi + 1
    
    # 3. Góc giữa hai vectơ (AB', BD)[cite: 23]
    # Nếu a = b = h thì góc đúng là 120^\circ[cite: 23]
    angle_str = "120^\\circ"
    angle_str_s = "60^\\circ" if is_120_deg else "120^\\circ"
    
    # 4. Điểm J thuộc mặt phẳng (Oxz) sao cho JC' ngắn nhất:
    # Đoạn JC' ngắn nhất khi J là hình chiếu vuông góc của C'(xc_p; yc_p; zc_p) trên mặt phẳng (Oxz)[cite: 23]
    # Tọa độ hình chiếu: J(xc_p; 0; zc_p) = (a_val; 0; h_val)[cite: 23]
    xj_true = a_val
    yj_true = 0
    zj_true = h_val
    
    # Tọa độ sai (đổi giá trị cao độ như đề gốc J(2; 0; 1) khi h_val = 2)[cite: 23]
    xj_s = a_val
    yj_s = 0
    zj_s = h_val // 2 if h_val % 2 == 0 and h_val // 2 != h_val else h_val + 1
    
    # Nội dung câu hỏi[cite: 23]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hình hộp $ABCD.A'B'C'D'$. Biết tọa độ các điểm $A(%s;%s;%s); B(%s;%s;%s); D(%s;%s;%s); D'(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xd, yd, zd, xd_p, yd_p, zd_p)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ điểm A'[cite: 23]
    nb_da_1_d = "\\True Tọa độ điểm $A'$ là $A'(%s;%s;%s)$" % (xa_p, ya_p, za_p)
    nb_da_1_s = "Tọa độ điểm $A'$ là $A'(%s;%s;%s)$" % (xa_p_s, ya_p_s, za_p_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Trong hình hộp $ABCD.A'B'C'D'$, ta có đẳng thức vectơ: \\\\ $\\vec{AA'} = \\vec{DD'} = (x_{D'} - x_D; y_{D'} - y_D; z_{D'} - z_D) = (%s - %s; %s - %s; %s - %s) = (0;0;%s)$. \\\\ Vì $A(%s;%s;%s)$ là gốc tọa độ nên tọa độ của điểm $A'$ là $A'(%s;%s;%s)$."""
        % (
            xd_p,
            xd,
            yd_p,
            yd,
            zd_p,
            zd,
            h_val,
            xa,
            ya,
            za,
            xa_p,
            ya_p,
            za_p,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Tâm I của hình hộp có tọa độ[cite: 23]
    th_da_1_d = "\\True Tâm $I$ của hình hộp có tọa độ là $I(%s;%s;%s)$" % (
        xi,
        yi,
        zi,
    )
    th_da_1_s = "Tâm $I$ của hình hộp có tọa độ là $I(%s;%s;%s)$" % (
        xi_s,
        yi_s,
        zi_s,
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì đáy $ABCD$ là hình bình hành nên: \\\\ $\\vec{AC} = \\vec{AB} + \\vec{AD} \\Rightarrow C(x_B + x_D - x_A; y_B + y_D - y_A; z_B + z_D - z_A) = (%s;%s;0)$. \\\\ Theo quy tắc hình hộp, tọa độ đỉnh $C'$ là: \\\\ $C' = C + \\vec{AA'} = (%s;%s;%s)$. \\\\ Tâm $I$ của hình hộp chính là trung điểm của đường chéo $AC'$, do đó: \\\\ $\\begin{cases} x_I = \\frac{x_A + x_{C'}}{2} = \\frac{0 + %s}{2} = %s \\\\ y_I = \\frac{y_A + y_{C'}}{2} = \\frac{0 + %s}{2} = %s \\\\ z_I = \\frac{z_A + z_{C'}}{2} = \\frac{0 + %s}{2} = %s \\end{cases} \\Rightarrow I(%s;%s;%s)$."""
        % (
            a_val,
            b_val,
            a_val,
            b_val,
            h_val,
            a_val,
            xi,
            b_val,
            yi,
            h_val,
            zi,
            xi,
            yi,
            zi,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Góc (AB', BD) bằng 120^\circ[cite: 23]
    if is_120_deg:
        vd_da_1_d = (
            "\\True Góc $(\\vec{AB'}, \\vec{BD})$ bằng $120^\\circ$"
        )
        vd_da_1_s = (
            "Góc $(\\vec{AB'}, \\vec{BD})$ bằng $60^\\circ$"
        )
    else:
        vd_da_1_d = (
            "\\True Góc $(\\vec{AB'}, \\vec{BD})$ có cosin bằng $%s$"
            % (latex(cos_val))
        )
        vd_da_1_s = (
            "Góc $(\\vec{AB'}, \\vec{BD})$ bằng $120^\\circ$"
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có $\\vec{BB'} = \\vec{AA'} = (0;0;%s) \\Rightarrow B'(%s;0;%s)$. \\\\ Tọa độ các vectơ: \\\\ $\\vec{AB'} = (%s;0;%s) \\Rightarrow |\\vec{AB'}| = \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $\\vec{BD} = (x_D - x_B; y_D - y_B; z_D - z_B) = (-%s;%s;0) \\Rightarrow |\\vec{BD}| = \\sqrt{(-%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Tích vô hướng: \\\\ $\\vec{AB'} \\cdot \\vec{BD} = (%s) \\cdot (-%s) + 0 \\cdot (%s) + (%s) \\cdot 0 = -%s$. \\\\ Khi đó: \\\\ $\\cos(\\vec{AB'}, \\vec{BD}) = \\frac{\\vec{AB'} \\cdot \\vec{BD}}{|\\vec{AB'}| \\cdot |\\vec{BD}|} = \\frac{-%s}{\\sqrt{%s} \\cdot \\sqrt{%s}} = %s$. \\\\ Do đó $(\\vec{AB'}, \\vec{BD}) %s$."""
        % (
            h_val,
            a_val,
            h_val,
            a_val,
            h_val,
            a_val,
            h_val,
            len_ab_p_sq,
            a_val,
            b_val,
            a_val,
            b_val,
            len_bd_sq,
            a_val,
            a_val,
            b_val,
            h_val,
            a_val**2,
            a_val**2,
            len_ab_p_sq,
            len_bd_sq,
            latex(cos_val),
            "= 120^\\circ" if is_120_deg else "\\neq 120^\\circ",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm J thuộc mặt phẳng (Oxz) sao cho JC' ngắn nhất[cite: 23]
    vdc_da_1_d = (
        "\\True Điểm $J$ thuộc mặt phẳng $(Oxz)$ sao cho đoạn $JC'$ ngắn nhất có tọa độ là $J(%s;%s;%s)$"
        % (xj_true, yj_true, zj_true)
    )
    vdc_da_1_s = (
        "Điểm $J$ thuộc mặt phẳng $(Oxz)$ sao cho đoạn $JC'$ ngắn nhất có tọa độ là $J(%s;%s;%s)$"
        % (xj_s, yj_s, zj_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Tọa độ đỉnh $C'$ của hình hộp là $C'(%s;%s;%s)$. \\\\ Với điểm $J$ bất kỳ nằm trên mặt phẳng tọa độ $(Oxz)$, độ dài đoạn thẳng $JC'$ đạt giá trị nhỏ nhất khi và chỉ khi $J$ là hình chiếu vuông góc của điểm $C'$ lên mặt phẳng $(Oxz)$. \\\\ Khi chiếu vuông góc lên mặt phẳng $(Oxz)$, ta giữ nguyên hoành độ và cao độ, tung độ bằng $0$. \\\\ Do đó tọa độ điểm $J$ cần tìm là $J(%s;0;%s)$."""
        % (
            xc_p,
            yc_p,
            zc_p,
            xc_p,
            zc_p,
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
        "\\end{ex}\n \\end{minipage}\n\n")
    return content
    