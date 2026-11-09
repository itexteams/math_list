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


def bt_dang30_p2_b2_c1_hh12(self):
    # Random dữ liệu hình hộp ABCD.A'B'C'D' với các đỉnh A, B, D, C'
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(-3, 3)
        za = random.randint(-3, 3)
    
        xb = random.randint(-3, 3)
        yb = random.randint(-3, 3)
        zb = random.randint(-3, 3)
    
        # Đỉnh D
        xd = random.choice([-3, -2, -1, 1, 2, 3])
        yd = 0  # Chọn tung độ bằng 0 như bài gốc để câu hình chiếu lên Ox rõ nét
        zd = random.choice([-3, -2, -1, 1, 2, 3])
    
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
            break
    
    # Vì ABCD là hình bình hành nên:
    # vecto AC = vecto AB + vecto AD <=> C = B + D - A
    xc = xb + xd - xa
    yc = yb + yd - ya
    zc = zb + zd - za
    
    # Chọn vectơ cạnh bên AA' = CC' = v
    vx = random.randint(1, 5)
    vy = random.randint(1, 5)
    vz = random.randint(1, 5)
    
    # Đỉnh C' = C + v
    xc_p = xc + vx
    yc_p = yc + vy
    zc_p = zc + vz
    
    # 1. Vectơ OC = (xc; yc; zc)
    # Vectơ OC sai (ví dụ đổi dấu)
    xc_s = -xc if xc != 0 else 1
    yc_s = -yc if yc != 0 else 2
    zc_s = zc
    
    # 2. Hình chiếu vuông góc của đỉnh D(xd; yd; zd) trên trục Ox là H(xd; 0; 0)
    # Chú ý ở đề gốc đặt tên điểm chiếu là C(xd; 0; 0)
    xd_proj = xd
    yd_proj = 0
    zd_proj = 0
    
    # Tọa độ sai của hình chiếu
    xd_proj_s = 0
    yd_proj_s = yd
    zd_proj_s = zd
    
    # 3. Tọa độ điểm C: C(xc; yc; zc)
    # Tọa độ C sai
    c_sai_x = xc + random.choice([-1, 1])
    c_sai_y = yc
    c_sai_z = zc
    
    # 4. Tọa độ điểm A':
    # Ta có vecto CC' = C' - C = (vx; vy; vz)
    # Vì ABCD.A'B'C'D' là hình hộp nên vecto AA' = vecto CC' = (vx; vy; vz)
    # => A' = A + CC' = (xa + vx; ya + vy; za + vz)
    xa_p = xa + vx
    ya_p = ya + vy
    za_p = za + vz
    
    # Tọa độ sai của A'
    xa_p_s = xa + vx + random.choice([-2, 2])
    ya_p_s = ya + vy
    za_p_s = za + vz
    
    # Nội dung câu hỏi[cite: 26]
    noidungcauhoi = (
        """Cho hình hộp $ABCD.A'B'C'D'$ có $A(%s;%s;%s)$, $B(%s;%s;%s)$, $D(%s;%s;%s)$, $C'(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xd, yd, zd, xc_p, yc_p, zc_p)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Vectơ OC[cite: 26]
    nb_da_1_d = "\\True $\\vec{OC} = (%s;%s;%s)$" % (xc, yc, zc)
    nb_da_1_s = "$\\vec{OC} = (%s;%s;%s)$" % (xc_s, yc_s, zc_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Vì $ABCD$ là hình bình hành nên theo quy tắc hình bình hành ta có: \\\\ $\\vec{AC} = \\vec{AB} + \\vec{AD} \\Leftrightarrow C - A = (B - A) + (D - A) \\Leftrightarrow C = B + D - A$. \\\\ Suy ra tọa độ điểm $C$ là: \\\\ $\\begin{cases} x_C = x_B + x_D - x_A = %s + (%s) - (%s) = %s \\\\ y_C = y_B + y_D - y_A = %s + (%s) - (%s) = %s \\\\ z_C = z_B + z_D - z_A = %s + (%s) - (%s) = %s \\end{cases} \\Rightarrow C(%s;%s;%s)$. \\\\ Do đó ta có $\\vec{OC} = (%s;%s;%s)$."""
        % (
            xb,
            xd,
            xa,
            xc,
            yb,
            yd,
            ya,
            yc,
            zb,
            zd,
            za,
            zc,
            xc,
            yc,
            zc,
            xc,
            yc,
            zc,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Hình chiếu vuông góc của đỉnh D trên trục Ox[cite: 26]
    th_da_1_d = (
        "\\True Hình chiếu vuông góc của đỉnh $D$ trên trục $Ox$ có tọa độ là $(%s;%s;%s)$"
        % (xd_proj, yd_proj, zd_proj)
    )
    th_da_1_s = (
        "Hình chiếu vuông góc của đỉnh $D$ trên trục $Ox$ có tọa độ là $(%s;%s;%s)$"
        % (xd_proj_s, yd_proj_s, zd_proj_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Hình chiếu vuông góc của điểm $D(%s;%s;%s)$ lên trục $Ox$ giữ nguyên hoành độ, tung độ và cao độ bằng $0$. \\\\ Do đó tọa độ hình chiếu của đỉnh $D$ trên trục $Ox$ là $(%s;0;0)$."""
        % (xd, yd, zd, xd)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Tọa độ điểm C[cite: 26]
    vd_da_1_d = "\\True $C(%s;%s;%s)$" % (xc, yc, zc)
    vd_da_1_s = "$C(%s;%s;%s)$" % (c_sai_x, c_sai_y, c_sai_z)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $ABCD$ là hình bình hành nên: \\\\ $\\vec{AB} = \\vec{DC} \\Leftrightarrow \\begin{cases} x_B - x_A = x_C - x_D \\\\ y_B - y_A = y_C - y_D \\\\ z_B - z_A = z_C - z_D \\end{cases} \\Leftrightarrow \\begin{cases} x_C = x_B - x_A + x_D = %s - (%s) + (%s) = %s \\\\ y_C = y_B - y_A + y_D = %s - (%s) + (%s) = %s \\\\ z_C = z_B - z_A + z_D = %s - (%s) + (%s) = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $C$ là $C(%s;%s;%s)$."""
        % (
            xb,
            xa,
            xd,
            xc,
            yb,
            ya,
            yd,
            yc,
            zb,
            za,
            zd,
            zc,
            xc,
            yc,
            zc,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tọa độ điểm A'[cite: 26]
    vdc_da_1_d = "\\True $A'(%s;%s;%s)$" % (xa_p, ya_p, za_p)
    vdc_da_1_s = "$A'(%s;%s;%s)$" % (xa_p_s, ya_p_s, za_p_s)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có tọa độ của vectơ $\\vec{CC'}$ là: \\\\ $\\vec{CC'} = (x_{C'} - x_C; y_{C'} - y_C; z_{C'} - z_C) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Vì $ABCD.A'B'C'D'$ là hình hộp nên các cạnh bên đôi một song song và bằng nhau, suy ra $\\vec{AA'} = \\vec{CC'} = (%s;%s;%s)$. \\\\ Gọi tọa độ điểm $A'$ là $A'(x_{A'}; y_{A'}; z_{A'})$, ta có: \\\\ $\\begin{cases} x_{A'} - x_A = %s \\\\ y_{A'} - y_A = %s \\\\ z_{A'} - z_A = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_{A'} = x_A + %s = %s + (%s) = %s \\\\ y_{A'} = y_A + %s = %s + (%s) = %s \\\\ z_{A'} = z_A + %s = %s + (%s) = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $A'$ là $A'(%s;%s;%s)$."""
        % (
            xc_p,
            xc,
            yc_p,
            yc,
            zc_p,
            zc,
            vx,
            vy,
            vz,
            vx,
            vy,
            vz,
            vx,
            vy,
            vz,
            vx,
            xa,
            vx,
            xa_p,
            vy,
            ya,
            vy,
            ya_p,
            vz,
            za,
            vz,
            za_p,
            xa_p,
            ya_p,
            za_p,
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
    