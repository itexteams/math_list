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


def bt_dang39_p2_b2_c1_hh12(self):
    # Sinh ngẫu nhiên dữ liệu hình hộp ABCD.A'B'C'D' với các đỉnh A, B, D, C'
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(-3, 3)
    
        xb = random.randint(-3, 3)
        yb = random.randint(-3, 3)
        zb = random.randint(-3, 3)
    
        xd = random.randint(-3, 3)
        yd = random.randint(-3, 3)
        zd = random.randint(-3, 3)
    
        # Vectơ AB, AD
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ad_x = xd - xa
        ad_y = yd - ya
        ad_z = zd - za
    
        # Kiểm tra đáy ABCD không suy biến (AB không cùng phương AD)
        cp_x = ab_y * ad_z - ab_z * ad_y
        cp_y = ab_z * ad_x - ab_x * ad_z
        cp_z = ab_x * ad_y - ab_y * ad_x
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xd, yd, zd)
        ):
            # Vectơ cạnh bên AA' = (vx, vy, vz)
            vx = random.randint(1, 5)
            vy = random.randint(1, 5)
            vz = random.choice([-6, -5, -4, 4, 5, 6])
    
            # Đỉnh A' = A + (vx, vy, vz)
            xa_p = xa + vx
            ya_p = ya + vy
            za_p = za + vz
    
            # Đáy hình bình hành: C = B + D - A
            xc = xb + xd - xa
            yc = yb + yd - ya
            zc = zb + zd - za
    
            # C' = C + (vx, vy, vz) = A + AB + AD + AA'
            xc_p = xc + vx
            yc_p = yc + vy
            zc_p = zc + vz
    
            # Đảm bảo yc_p khác 0 để hình chiếu trên Oy rõ ràng
            if yc_p != 0 and xc_p != 0 and zc_p != 0:
                break
    
    # 1. Vectơ AB = (ab_x; ab_y; ab_z)
    # Vectơ sai (đổi dấu hoặc nhầm thành A - B)
    ab_x_s = -ab_x
    ab_y_s = -ab_y
    ab_z_s = -ab_z
    
    # 2. Hình chiếu vuông góc của C'(xc_p; yc_p; zc_p) trên trục Oy là N(0; yc_p; 0)
    xn_proj = 0
    yn_proj = yc_p
    zn_proj = 0
    
    # Tọa độ sai của hình chiếu (ví dụ giữ nguyên hoành độ)
    xn_proj_s = xc_p
    yn_proj_s = yc_p
    zn_proj_s = 0
    
    # 3. Quy tắc hình hộp: vecto AB + vecto AD + vecto AA' = vecto AC'
    # Mệnh đề đúng là đẳng thức vecto AB + vecto AD + vecto AA' = vecto AC'
    # Mệnh đề sai là thay AC' bằng CA' hoặc AB'
    
    # 4. Tọa độ điểm A' có hoành độ bằng xa_p
    xa_p_true = xa_p
    xa_p_false = xa_p + random.choice([-2, -1, 1, 2])
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hình hộp $ABCD.A'B'C'D'$ có các đỉnh $A(%s;%s;%s)$, $B(%s;%s;%s)$, $D(%s;%s;%s)$, $C'(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xd, yd, zd, xc_p, yc_p, zc_p)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ AB
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (ab_x_s, ab_y_s, ab_z_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ của vectơ $\\vec{AB}$ là: \\\\ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xb, xa, yb, ya, zb, za, ab_x, ab_y, ab_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Điểm C' có hình chiếu vuông góc trên trục Oy là N(0; yc_p; 0)
    th_da_1_d = (
        "\\True Điểm $C'(%s;%s;%s)$ có hình chiếu vuông góc trên trục $Oy$ là điểm $N(%s;%s;%s)$"
        % (xc_p, yc_p, zc_p, xn_proj, yn_proj, zn_proj)
    )
    th_da_1_s = (
        "Điểm $C'(%s;%s;%s)$ có hình chiếu vuông góc trên trục $Oy$ là điểm $N(%s;%s;%s)$"
        % (xc_p, yc_p, zc_p, xn_proj_s, yn_proj_s, zn_proj_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Hình chiếu vuông góc của điểm $C'(%s;%s;%s)$ lên trục $Oy$ giữ nguyên tung độ, hoành độ và cao độ bằng $0$. \\\\ Do đó ta được điểm $N(0;%s;0)$."""
        % (xc_p, yc_p, zc_p, yc_p)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Quy tắc hình hộp
    vd_da_1_d = "\\True $\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AC'}$"
    vd_da_1_s = "$\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{CA'}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = """Theo quy tắc hình hộp, với ba cạnh xuất phát từ đỉnh $A$ là $AB, AD, AA'$ và đường chéo xuất phát từ đỉnh $A$ là $AC'$, ta luôn có hệ thức vectơ: \\\\ $\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AC'}$."""
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm A' có hoành độ bằng xa_p
    vdc_da_1_d = "\\True Điểm $A'$ có hoành độ bằng $%s$" % (xa_p_true)
    vdc_da_1_s = "Điểm $A'$ có hoành độ bằng $%s$" % (xa_p_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    ac_p_x = xc_p - xa
    ac_p_y = yc_p - ya
    ac_p_z = zc_p - za
    
    loigiai_vdc_1 = (
        """Theo quy tắc hình hộp, ta có: \\\\ $\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AC'} \\Leftrightarrow \\vec{AA'} = \\vec{AC'} - \\vec{AB} - \\vec{AD}$. \\\\ Ta có: \\\\ $\\vec{AC'} = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ $\\vec{AB} = (%s;%s;%s)$. \\\\ $\\vec{AD} = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Suy ra: \\\\ $\\vec{AA'} = (%s - (%s) - (%s); %s - (%s) - (%s); %s - (%s) - (%s)) = (%s;%s;%s)$. \\\\ Gọi $A'(x_{A'}; y_{A'}; z_{A'})$, suy ra: \\\\ $\\begin{cases} x_{A'} - x_A = %s \\\\ y_{A'} - y_A = %s \\\\ z_{A'} - z_A = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_{A'} = %s + (%s) = %s \\\\ y_{A'} = %s + (%s) = %s \\\\ z_{A'} = %s + (%s) = %s \\end{cases} \\Rightarrow A'(%s;%s;%s)$. \\\\ Vậy điểm $A'$ có hoành độ bằng $%s$."""
        % (
            xc_p,
            xa,
            yc_p,
            ya,
            zc_p,
            za,
            ac_p_x,
            ac_p_y,
            ac_p_z,
            ab_x,
            ab_y,
            ab_z,
            xd,
            xa,
            yd,
            ya,
            zd,
            za,
            ad_x,
            ad_y,
            ad_z,
            ac_p_x,
            ab_x,
            ad_x,
            ac_p_y,
            ab_y,
            ad_y,
            ac_p_z,
            ab_z,
            ad_z,
            vx,
            vy,
            vz,
            vx,
            vy,
            vz,
            xa,
            vx,
            xa_p,
            ya,
            vy,
            ya_p,
            za,
            vz,
            za_p,
            xa_p,
            ya_p,
            za_p,
            xa_p_true,
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
    