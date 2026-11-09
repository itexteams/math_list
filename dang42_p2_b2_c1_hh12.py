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


def bt_dang42_p2_b2_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm E, F, K không thẳng hàng[cite: 28]
    while True:
        xe = random.randint(-4, 4)
        ye = random.choice([-4, -3, -2, 2, 3, 4])
        ze = random.choice([-4, -3, -2, 2, 3, 4])
    
        xf = random.randint(-4, 4)
        yf = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        zf = random.choice([-5, -4, -3, 3, 4, 5])
    
        xk = random.randint(-4, 4)
        yk = random.randint(-4, 4)
        zk = random.randint(-4, 4)
    
        # Đảm bảo tổng cao độ ze + zf + zk chia hết cho 3 để cao độ G là số nguyên đẹp[cite: 28]
        if (ze + zf + zk) % 3 != 0:
            continue
    
        # Vectơ EK và EF
        ek_x = xk - xe
        ek_y = yk - ye
        ek_z = zk - ze
    
        ef_x = xf - xe
        ef_y = yf - ye
        ef_z = zf - ze
    
        # Kiểm tra ba điểm E, F, K không thẳng hàng[cite: 28]
        cp_x = ek_y * ef_z - ek_z * ef_y
        cp_y = ek_z * ef_x - ek_x * ef_z
        cp_z = ek_x * ef_y - ek_y * ef_x
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xe, ye, ze) != (xf, yf, zf)
            and (xe, ye, ze) != (xk, yk, zk)
            and (xf, yf, zf) != (xk, yk, zk)
        ):
            break
    
    # 1. Vectơ EK = (ek_x; ek_y; ek_z)[cite: 28]
    # Vectơ sai (đổi dấu hoặc nhầm thành E - K)
    ek_x_s = -ek_x
    ek_y_s = ek_y
    ek_z_s = -ek_z
    
    # 2. Hình chiếu vuông góc của E(xe; ye; ze) trên mặt phẳng (Oxy): E'(xe; ye; 0)[cite: 28]
    xe_proj = xe
    ye_proj = ye
    ze_proj = 0
    
    # Tọa độ sai của hình chiếu (ví dụ chiếu lên trục Ox: E'(xe; 0; 0) như đề gốc)[cite: 28]
    xe_proj_s = xe
    ye_proj_s = 0
    ze_proj_s = 0
    
    # 3. M là điểm đối xứng với F qua gốc tọa độ O => O là trung điểm FM:
    # FM = 2 * OF = 2 * \sqrt{xf^2 + yf^2 + zf^2}[cite: 28]
    of_sq = xf**2 + yf**2 + zf**2
    str_fm_true = "2\\sqrt{%s}" % of_sq
    str_fm_false = "\\sqrt{%s}" % of_sq
    
    # 4. Tam giác ABC thỏa mãn vecto(AE) + vecto(BF) + vecto(CK) = 0[cite: 28]
    # <=> (E - A) + (F - B) + (K - C) = 0 <=> (A + B + C) = (E + F + K)
    # Gọi G là trọng tâm tam giác ABC: G = (A + B + C)/3 = (E + F + K)/3[cite: 28]
    zg = (ze + zf + zk) // 3
    zg_false = zg + random.choice([-2, -1, 1, 2])
    
    # Nội dung câu hỏi[cite: 28]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho ba điểm $E(%s;%s;%s)$, $F(%s;%s;%s)$, $K(%s;%s;%s)$."""
        % (xe, ye, ze, xf, yf, zf, xk, yk, zk)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Vectơ EK[cite: 28]
    nb_da_1_d = "\\True $\\vec{EK} = (%s;%s;%s)$" % (ek_x, ek_y, ek_z)
    nb_da_1_s = "$\\vec{EK} = (%s;%s;%s)$" % (ek_x_s, ek_y_s, ek_z_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ của vectơ $\\vec{EK}$ là: \\\\ $\\vec{EK} = (x_K - x_E; y_K - y_E; z_K - z_E) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xk, xe, yk, ye, zk, ze, ek_x, ek_y, ek_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Hình chiếu vuông góc của E trên mặt phẳng (Oxy)[cite: 28]
    th_da_1_d = (
        "\\True Hình chiếu vuông góc của điểm $E(%s;%s;%s)$ trên mặt phẳng $(Oxy)$ là điểm $E'(%s;%s;%s)$"
        % (xe, ye, ze, xe_proj, ye_proj, ze_proj)
    )
    th_da_1_s = (
        "Hình chiếu vuông góc của điểm $E(%s;%s;%s)$ trên mặt phẳng $(Oxy)$ là điểm $E'(%s;%s;%s)$"
        % (xe, ye, ze, xe_proj_s, ye_proj_s, ze_proj_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Hình chiếu vuông góc của điểm $E(%s;%s;%s)$ lên mặt phẳng tọa độ $(Oxy)$ giữ nguyên hoành độ và tung độ, cao độ bằng $0$. \\\\ Do đó ta được tọa độ hình chiếu là $E'(%s;%s;0)$."""
        % (xe, ye, ze, xe, ye)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: M đối xứng với F qua gốc tọa độ O thì FM = 2\sqrt{of_sq}[cite: 28]
    vd_da_1_d = (
        "\\True $M$ là điểm đối xứng với $F(%s;%s;%s)$ qua gốc tọa độ thì $FM = %s$"
        % (xf, yf, zf, str_fm_true)
    )
    vd_da_1_s = (
        "$M$ là điểm đối xứng với $F(%s;%s;%s)$ qua gốc tọa độ thì $FM = %s$"
        % (xf, yf, zf, str_fm_false)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    xm = -xf
    ym = -yf
    zm = -zf
    
    loigiai_vd_1 = (
        """Vì điểm $M$ đối xứng với điểm $F(%s;%s;%s)$ qua gốc tọa độ $O(0;0;0)$ nên $O$ là trung điểm của đoạn thẳng $FM$. \\\\ Tọa độ điểm $M$ là $M(-x_F; -y_F; -z_F) = M(%s;%s;%s)$. \\\\ Khoảng cách giữa hai điểm $F$ và $M$ là: \\\\ $FM = 2 \\cdot OF = 2 \\cdot \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s$."""
        % (
            xf,
            yf,
            zf,
            xm,
            ym,
            zm,
            xf,
            yf,
            zf,
            str_fm_true,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tam giác ABC thỏa mãn AE + BF + CK = 0 thì trọng tâm G có cao độ bằng zg[cite: 28]
    vdc_da_1_d = (
        "\\True Tam giác $ABC$ thỏa mãn $\\vec{AE} + \\vec{BF} + \\vec{CK} = \\vec{0}$ thì trọng tâm $G$ của tam giác $ABC$ có cao độ bằng $%s$"
        % (zg)
    )
    vdc_da_1_s = (
        "Tam giác $ABC$ thỏa mãn $\\vec{AE} + \\vec{BF} + \\vec{CK} = \\vec{0}$ thì trọng tâm $G$ của tam giác $ABC$ có cao độ bằng $%s$"
        % (zg_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$. Khi đó ta có hệ thức vectơ: \\\\ $\\vec{GA} + \\vec{GB} + \\vec{GC} = \\vec{0}$. \\\\ Theo giả thiết: \\\\ $\\vec{AE} + \\vec{BF} + \\vec{CK} = \\vec{0} \\Leftrightarrow (\\vec{GE} - \\vec{GA}) + (\\vec{GF} - \\vec{GB}) + (\\vec{GK} - \\vec{GC}) = \\vec{0}$ \\\\ $\\Leftrightarrow (\\vec{GE} + \\vec{GF} + \\vec{GK}) - (\\vec{GA} + \\vec{GB} + \\vec{GC}) = \\vec{0} \\Leftrightarrow \\vec{GE} + \\vec{GF} + \\vec{GK} = \\vec{0}$. \\\\ Do đó $G$ cũng chính là trọng tâm của tam giác $EFK$. \\\\ Suy ra cao độ của trọng tâm $G$ là: \\\\ $z_G = \\frac{z_E + z_F + z_K}{3} = \\frac{%s + (%s) + (%s)}{3} = \\frac{%s}{3} = %s$."""
        % (
            ze,
            zf,
            zk,
            ze + zf + zk,
            zg,
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
    