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


def bt_dang21_p2_b2_c1_hh12(self):
    # Random toạ độ ba đỉnh A, B, C không thẳng hàng của tam giác đáy và đỉnh B'
    while True:
        xa = random.randint(-3, 3)
        ya = random.randint(1, 4)
        za = random.randint(-3, 3)
    
        xb = random.randint(1, 4)
        yb = random.randint(-3, 1)
        zb = random.randint(-3, 3)
    
        xc = random.randint(-4, 0)
        yc = random.randint(1, 4)
        zc = random.randint(-7, -1)
    
        # Vectơ cạnh bên v = BB'
        vx = random.randint(5, 10)
        vy = random.randint(-2, 2)
        vz = random.randint(8, 15)
    
        xb_p = xb + vx
        yb_p = yb + vy
        zb_p = zb + vz
    
        # Kiểm tra tam giác ABC không suy biến
        ab_x, ab_y, ab_z = xb - xa, yb - ya, zb - za
        ac_x, ac_y, ac_z = xc - xa, yc - ya, zc - za
    
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # 1. Toạ độ vectơ BB' = (vx; vy; vz)
    # Vectơ BB' sai (ví dụ nhầm thành B - B')
    bb_x_s = -vx
    bb_y_s = -vy
    bb_z_s = -vz
    
    # 2. Toạ độ điểm A': Vì ABC.A'B'C' là hình lăng trụ nên AA' = BB' => A' = A + BB'
    xa_p = xa + vx
    ya_p = ya + vy
    za_p = za + vz
    
    # Toạ độ sai của A' (ví dụ nhầm thành A - BB')
    xa_p_s = xa - vx
    ya_p_s = ya - vy
    za_p_s = za - vz
    
    # 3. Toạ độ điểm C': CC' = BB' => C' = C + BB'
    xc_p = xc + vx
    yc_p = yc + vy
    zc_p = zc + vz
    
    # Toạ độ sai của C'
    xc_p_s = xc_p + random.choice([-3, 3])
    yc_p_s = yc_p + random.choice([-2, 2])
    zc_p_s = zc_p + random.choice([-4, 4])
    
    # 4. ABCD.A'B'C'D' là hình hộp:
    # ABCD là hình bình hành <=> vecto AB = vecto DC <=> D = C - AB = C + A - B
    xd = xc + xa - xb
    yd = yc + ya - yb
    zd = zc + za - zb
    
    # D' = D + BB'
    xd_p = xd + vx
    yd_p = yd + vy
    zd_p = zd + vz
    
    # Toạ độ sai của D, D'
    xd_s = xd + random.choice([-2, 2])
    yd_s = yd
    zd_s = zd
    
    # Chuỗi TikZ vẽ hình lăng trụ tam giác đúng 100% như ảnh mẫu
    hinh_ve_tikz = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (C) at (-0.8,2.5);
    \\coordinate (A) at (2.2,2.5);
    \\coordinate (B) at (0.5,1.5);
    \\coordinate (C') at (-1.5,0.5);
    \\coordinate (A') at (1.5,0.5);
    \\coordinate (B') at (-0.2,-0.5);
    \\draw[line width=1pt] (C)--(A)--(B)--(C) (C)--(C') (B)--(B') (A)--(A') (C')--(B')--(A');
    \\draw[line width=1pt, dashed] (C')--(A');
    \\fill (A) circle (1pt) node[above right] {$A$};
    \\fill (B) circle (1pt) node[below right] {$B$};
    \\fill (C) circle (1pt) node[above left] {$C$};
    \\fill (A') circle (1pt) node[below right] {$A'$};
    \\fill (B') circle (1pt) node[below left] {$B'$};
    \\fill (C') circle (1pt) node[left] {$C'$};
    \\end{tikzpicture}
    \\end{center}"""
    
    # Nội dung câu hỏi (đặt hình vẽ lên đề bài theo yêu cầu)
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho hình lăng trụ tam giác $ABC.A'B'C'$ có $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$ và $B'(%s;%s;%s)$. %s"""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xb_p, yb_p, zb_p, hinh_ve_tikz)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tọa độ của BB'
    nb_da_1_d = "\\True Tọa độ của $\\vec{BB'} = (%s;%s;%s)$" % (vx, vy, vz)
    nb_da_1_s = "Tọa độ của $\\vec{BB'} = (%s;%s;%s)$" % (bb_x_s, bb_y_s, bb_z_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có tọa độ của vectơ $\\vec{BB'}$ là: \\\\ $\\vec{BB'} = (x_{B'} - x_B; y_{B'} - y_B; z_{B'} - z_B) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xb_p, xb, yb_p, yb, zb_p, zb, vx, vy, vz)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Tọa độ điểm A'
    th_da_1_d = "\\True Tọa độ điểm $A'(%s;%s;%s)$" % (xa_p, ya_p, za_p)
    th_da_1_s = "Tọa độ điểm $A'(%s;%s;%s)$" % (xa_p_s, ya_p_s, za_p_s)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $ABC.A'B'C'$ là hình lăng trụ tam giác nên ta có $\\vec{AA'} = \\vec{BB'} = (%s;%s;%s)$. \\\\ Gọi tọa độ điểm $A'(x_{A'}; y_{A'}; z_{A'})$, suy ra: \\\\ $\\begin{cases} x_{A'} - x_A = %s \\\\ y_{A'} - y_A = %s \\\\ z_{A'} - z_A = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_{A'} = x_A + (%s) = %s + (%s) = %s \\\\ y_{A'} = y_A + (%s) = %s + (%s) = %s \\\\ z_{A'} = z_A + (%s) = %s + (%s) = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $A'$ là $A'(%s;%s;%s)$."""
        % (
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
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Tọa độ điểm C'
    vd_da_1_d = "\\True Tọa độ điểm $C'(%s;%s;%s)$" % (xc_p, yc_p, zc_p)
    vd_da_1_s = "Tọa độ điểm $C'(%s;%s;%s)$" % (xc_p_s, yc_p_s, zc_p_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $ABC.A'B'C'$ là hình lăng trụ tam giác nên ta có $\\vec{CC'} = \\vec{BB'} = (%s;%s;%s)$. \\\\ Gọi tọa độ điểm $C'(x_{C'}; y_{C'}; z_{C'})$, suy ra: \\\\ $\\begin{cases} x_{C'} = x_C + (%s) = %s + (%s) = %s \\\\ y_{C'} = y_C + (%s) = %s + (%s) = %s \\\\ z_{C'} = z_C + (%s) = %s + (%s) = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $C'$ là $C'(%s;%s;%s)$."""
        % (
            vx,
            vy,
            vz,
            vx,
            xc,
            vx,
            xc_p,
            vy,
            yc,
            vy,
            yc_p,
            vz,
            zc,
            vz,
            zc_p,
            xc_p,
            yc_p,
            zc_p,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: ABCD.A'B'C'D' là hình hộp khi D(...) và D'(...)
    vdc_da_1_d = (
        "\\True $ABCD.A'B'C'D'$ là hình hộp khi $D(%s;%s;%s)$ và $D'(%s;%s;%s)$"
        % (xd, yd, zd, xd_p, yd_p, zd_p)
    )
    vdc_da_1_s = (
        "$ABCD.A'B'C'D'$ là hình hộp khi $D(%s;%s;%s)$ và $D'(%s;%s;%s)$"
        % (xd_s, yd_s, zd_s, xd_p, yd_p, zd_p)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Để $ABCD.A'B'C'D'$ là hình hộp thì đáy $ABCD$ phải là hình bình hành và $DD'$ là cạnh bên song song, bằng các cạnh bên còn lại. \\\\ Tứ giác $ABCD$ là hình bình hành khi và chỉ khi: \\\\ $\\vec{AB} = \\vec{DC} \\Leftrightarrow (x_B - x_A; y_B - y_A; z_B - z_A) = (x_C - x_D; y_C - y_D; z_C - z_D)$ \\\\ $\\Leftrightarrow \\begin{cases} x_D = x_C - (x_B - x_A) = %s - (%s) = %s \\\\ y_D = y_C - (y_B - y_A) = %s - (%s) = %s \\\\ z_D = z_C - (z_B - z_A) = %s - (%s) = %s \\end{cases} \\Rightarrow D(%s;%s;%s)$. \\\\ Mặt khác, $\\vec{DD'} = \\vec{BB'} = (%s;%s;%s)$, suy ra tọa độ điểm $D'$ là: \\\\ $\\begin{cases} x_{D'} = x_D + (%s) = %s + (%s) = %s \\\\ y_{D'} = y_D + (%s) = %s + (%s) = %s \\\\ z_{D'} = z_D + (%s) = %s + (%s) = %s \\end{cases} \\Rightarrow D'(%s;%s;%s)$. \\\\ Vậy $ABCD.A'B'C'D'$ là hình hộp khi $D(%s;%s;%s)$ và $D'(%s;%s;%s)$."""
        % (
            xc,
            ab_x,
            xd,
            yc,
            ab_y,
            yd,
            zc,
            ab_z,
            zd,
            xd,
            yd,
            zd,
            vx,
            vy,
            vz,
            vx,
            xd,
            vx,
            xd_p,
            vy,
            yd,
            vy,
            yd_p,
            vz,
            zd,
            vz,
            zd_p,
            xd_p,
            yd_p,
            zd_p,
            xd,
            yd,
            zd,
            xd_p,
            yd_p,
            zd_p,
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
    