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


def bt_dang19_p2_b2_c1_hh12(self):
    # Để ba điểm A, B, M thẳng hàng có toạ độ x, y nguyên thì (zm - za) phải chia hết cho (zb - za)
    while True:
        xa = random.randint(-4, 4)
        ya = random.randint(-4, 4)
        za = random.randint(1, 5)
    
        zm = random.choice([0, 1, 2])
        # Chọn hệ số k_align để AM = k_align * AB khi thẳng hàng (k_align != 0 và k_align != 1)
        k_align = random.choice([-2, -1, 2, 3])
    
        # zm - za = k_align * (zb - za) => zb - za phải là số nguyên khác 0
        # Ta chọn delta_z sao cho zm - za = k_align * delta_z
        delta_z = random.choice([-2, -1, 1, 2])
        za = zm - k_align * delta_z
        zb = za + delta_z
    
        xb = random.randint(-4, 4)
        yb = random.randint(-4, 4)
    
        # Đảm bảo vectơ AB khác vectơ 0
        if (xb != xa or yb != ya) and zb != za:
            break
    
    # 1. Vectơ AB = (ab_x; ab_y; ab_z)
    ab_x = xb - xa
    ab_y = yb - ya
    ab_z = zb - za
    
    # 2. Vectơ AM khi cho trước giá trị (x0; y0)
    x0 = random.randint(-3, 3)
    y0 = random.randint(-3, 3)
    am_x_val = x0 - xa
    am_y_val = y0 - ya
    am_z_val = zm - za
    
    # Vectơ AM sai
    am_y_val_s = am_y_val + random.choice([-2, 2])
    
    
    k_c = -2
    # Tính thử nếu chỉ giải theo 2 toạ độ đầu:
    # x_c_calc = (xb - k_c * xa) / (1 - k_c)
    # y_c_calc = (yb - k_c * ya) / (1 - k_c)
    x_c_sample = random.randint(-4, 4)
    y_c_sample = random.randint(-4, 4)
    
    # 4. Mệnh đề d: Ba điểm A, B, M thẳng hàng khi x = xd, y = yd
    # Điều kiện: vecto AM = k_align * vecto AB
    xd_true = xa + k_align * ab_x
    yd_true = ya + k_align * ab_y
    
    # Toạ độ sai (ví dụ sai dấu x hoặc đổi số)
    xd_false = -xd_true if xd_true != 0 else xd_true + 2
    yd_false = yd_true
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho ba điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$; $M(x;y;%s)$."""
        % (xa, ya, za, xb, yb, zb, zm)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ AB
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (-ab_x, -ab_y, ab_z)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xb, xa, yb, ya, zb, za, ab_x, ab_y, ab_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Vectơ AM khi x = x0; y = y0
    th_da_1_d = "\\True $\\vec{AM} = (%s;%s;%s)$ khi $x = %s; y = %s$" % (
        am_x_val,
        am_y_val,
        am_z_val,
        x0,
        y0,
    )
    th_da_1_s = "$\\vec{AM} = (%s;%s;%s)$ khi $x = %s; y = %s$" % (
        am_x_val,
        am_y_val_s,
        am_z_val,
        x0,
        y0,
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Với $x = %s; y = %s$, ta có tọa độ điểm $M(%s;%s;%s)$. \\\\ Khi đó vectơ $\\vec{AM} = (x_M - x_A; y_M - y_A; z_M - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (
            x0,
            y0,
            x0,
            y0,
            zm,
            x0,
            xa,
            y0,
            ya,
            zm,
            za,
            am_x_val,
            am_y_val,
            am_z_val,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Vectơ BM = k_c * vecto AM
    # So sánh cao độ hai vế:
    # Vế trái có cao độ: zm - zb
    # Vế phải có cao độ: k_c * (zm - za)
    bm_z_val = zm - zb
    am_z_mult = k_c * am_z_val
    is_c_possible = bm_z_val == am_z_mult
    
    if is_c_possible:
        # Nếu thỏa mãn cao độ thì giải tìm x, y đúng
        xc_true = (xb - k_c * xa) // (1 - k_c)
        yc_true = (yb - k_c * ya) // (1 - k_c)
        vd_da_1_d = "\\True $\\vec{BM} = %s\\vec{AM}$ khi $x = %s; y = %s$" % (
            k_c,
            xc_true,
            yc_true,
        )
        vd_da_1_s = "$\\vec{BM} = %s\\vec{AM}$ khi $x = %s; y = %s$" % (
            k_c,
            xc_true + 1,
            yc_true,
        )
    else:
        # Không thể xảy ra do cao độ không khớp
        vd_da_1_d = (
            "\\True Không tồn tại các số thực $x, y$ để $\\vec{BM} = %s\\vec{AM}$"
            % (k_c)
        )
        vd_da_1_s = "$\\vec{BM} = %s\\vec{AM}$ khi $x = %s; y = %s$" % (
            k_c,
            x_c_sample,
            y_c_sample,
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có $\\vec{BM} = (x - (%s); y - (%s); %s - (%s)) = (x - (%s); y - (%s); %s)$ \\\\ và $\\vec{AM} = (x - (%s); y - (%s); %s - (%s)) = (x - (%s); y - (%s); %s)$. \\\\ Suy ra %s\\vec{AM} có cao độ là $%s \\cdot (%s) = %s$. \\\\ So sánh cao độ của hai vectơ trong đẳng thức $\\vec{BM} = %s\\vec{AM}$, ta có $%s \\neq %s$, do đó đẳng thức không thể xảy ra với mọi $x, y$."""
        % (
            xb,
            yb,
            zm,
            zb,
            xb,
            yb,
            bm_z_val,
            xa,
            ya,
            zm,
            za,
            xa,
            ya,
            am_z_val,
            k_c,
            k_c,
            am_z_val,
            am_z_mult,
            k_c,
            bm_z_val,
            am_z_mult,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Ba điểm A, B, M thẳng hàng
    vdc_da_1_d = "\\True Ba điểm $A, B, M$ thẳng hàng khi $x = %s; y = %s$" % (
        xd_true,
        yd_true,
    )
    vdc_da_1_s = "Ba điểm $A, B, M$ thẳng hàng khi $x = %s; y = %s$" % (
        xd_false,
        yd_false,
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có $\\vec{AB} = (%s;%s;%s)$ và $\\vec{AM} = (x - (%s); y - (%s); %s - (%s)) = (x - (%s); y - (%s); %s)$. \\\\ Ba điểm $A, B, M$ thẳng hàng khi và chỉ khi hai vectơ $\\vec{AM}$ và $\\vec{AB}$ cùng phương: \\\\ $\\Leftrightarrow \\frac{x - (%s)}{%s} = \\frac{y - (%s)}{%s} = \\frac{%s}{%s} = %s$ \\\\ $\\Leftrightarrow \\begin{cases} x - (%s) = %s \\cdot (%s) = %s \\\\ y - (%s) = %s \\cdot (%s) = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$ \\\\ Vậy ba điểm $A, B, M$ thẳng hàng khi $x = %s; y = %s$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            xa,
            ya,
            zm,
            za,
            xa,
            ya,
            am_z_val,
            xa,
            ab_x,
            ya,
            ab_y,
            am_z_val,
            ab_z,
            k_align,
            xa,
            k_align,
            ab_x,
            k_align * ab_x,
            ya,
            k_align,
            ab_y,
            k_align * ab_y,
            xd_true,
            yd_true,
            xd_true,
            yd_true,
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
    