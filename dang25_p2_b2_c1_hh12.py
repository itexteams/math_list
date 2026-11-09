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


def bt_dang25_p2_b2_c1_hh12(self):
    # Sinh ngẫu nhiên dữ liệu cho bốn điểm A, B, C, G
    while True:
        # Điểm A có tung độ khác 0 để khoảng cách đến (Oxz) dương
        xa = random.randint(-4, 4)
        ya = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
        za = random.randint(-5, 8)
    
        # Chọn vectơ đơn giản u và hệ số k_u > 0 để AB = k_u * u cùng hướng
        u1 = random.choice([-2, -1, 1, 2])
        u2 = random.choice([-2, -1, 1, 2])
        u3 = random.choice([-2, -1, 1, 2])
        k_u = random.choice([2, 3, 4])
    
        # Toạ độ điểm B = A + k_u * u
        xb = xa + k_u * u1
        yb = ya + k_u * u2
        zb = za + k_u * u3
    
        # Toạ độ điểm C
        xc = random.randint(-5, 5)
        yc = random.randint(-5, 5)
        zc = random.randint(1, 10)
    
        # Toạ độ điểm G
        xg = random.randint(-4, 4)
        yg = random.randint(-4, 4)
        zg = random.randint(3, 8)
    
        # Kiểm tra ba điểm A, B, C không thẳng hàng
        ab_x, ab_y, ab_z = xb - xa, yb - ya, zb - za
        ac_x, ac_y, ac_z = xc - xa, yc - ya, zc - za
    
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        # Điểm D sao cho G là trọng tâm tam giác BCD: D = 3G - B - C
        zd = 3 * zg - zb - zc
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # 1. Vectơ AB = (ab_x; ab_y; ab_z) = k_u * (u1; u2; u3)
    # 2. Khoảng cách từ A(xa; ya; za) đến mặt phẳng (Oxz): d(A, (Oxz)) = |ya|
    dist_a_oxz = abs(ya)
    dist_a_oxz_s = dist_a_oxz + random.choice([1, 2])
    
    # 3. Điểm M đối xứng với điểm A qua B => B là trung điểm AM => M = 2B - A
    xm = 2 * xb - xa
    ym = 2 * yb - ya
    zm = 2 * zb - za
    
    ym_s = ym + random.choice([-3, -2, 2, 3])
    
    # 4. G là trọng tâm tam giác BCD => D = 3G - B - C
    xd = 3 * xg - xb - xc
    yd = 3 * yg - yb - yc
    zd = 3 * zg - zb - zc
    
    # Mốc so sánh cho cao độ của D
    bound_zd = zd - 1
    bound_zd_s = zd + 1
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho bốn điểm $A(%s;%s;%s); B(%s;%s;%s); C(%s;%s;%s); G(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xg, yg, zg)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vector u = (u1; u2; u3) cùng hướng với vector AB
    nb_da_1_d = "\\True Vector $\\vec{u} = (%s;%s;%s)$ cùng hướng với vector $\\vec{AB}$" % (
        u1,
        u2,
        u3,
    )
    nb_da_1_s = "Vector $\\vec{u} = (%s;%s;%s)$ ngược hướng với vector $\\vec{AB}$" % (
        u1,
        u2,
        u3,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Mặt khác $\\vec{AB} = %s \\cdot (%s;%s;%s) = %s\\vec{u}$. \\\\ Vì %s > 0 nên vector $\\vec{u}$ cùng hướng với vector $\\vec{AB}$."""
        % (
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            ab_x,
            ab_y,
            ab_z,
            k_u,
            u1,
            u2,
            u3,
            k_u,
            k_u,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Điểm A cách mặt phẳng (Oxz) một khoảng bằng dist_a_oxz
    th_da_1_d = (
        "\\True Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oxz)$ một khoảng bằng $%s$"
        % (xa, ya, za, dist_a_oxz)
    )
    th_da_1_s = (
        "Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oxz)$ một khoảng bằng $%s$"
        % (xa, ya, za, dist_a_oxz_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Mặt phẳng $(Oxz)$ có phương trình là $y = 0$. \\\\ Khoảng cách từ điểm $A(%s;%s;%s)$ đến mặt phẳng $(Oxz)$ là: \\\\ $d(A, (Oxz)) = |y_A| = |%s| = %s$."""
        % (xa, ya, za, ya, dist_a_oxz)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Điểm M đối xứng với điểm A qua B thì M có tung độ bằng ym
    vd_da_1_d = (
        "\\True Điểm $M$ đối xứng với điểm $A$ qua $B$ thì $M$ có tung độ bằng $%s$"
        % (ym)
    )
    vd_da_1_s = (
        "Điểm $M$ đối xứng với điểm $A$ qua $B$ thì $M$ có tung độ bằng $%s$"
        % (ym_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì điểm $M$ đối xứng với điểm $A$ qua $B$ nên $B$ là trung điểm của đoạn thẳng $AM$. \\\\ Do đó ta có: \\\\ $\\begin{cases} x_B = \\frac{x_A + x_M}{2} \\\\ y_B = \\frac{y_A + y_M}{2} \\\\ z_B = \\frac{z_A + z_M}{2} \\end{cases} \\Leftrightarrow \\begin{cases} x_M = 2x_B - x_A = 2 \\cdot (%s) - (%s) = %s \\\\ y_M = 2y_B - y_A = 2 \\cdot (%s) - (%s) = %s \\\\ z_M = 2z_B - z_A = 2 \\cdot (%s) - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $M$ là $M(%s;%s;%s)$, do đó điểm $M$ có tung độ bằng $%s$."""
        % (
            xb,
            xa,
            xm,
            yb,
            ya,
            ym,
            zb,
            za,
            zm,
            xm,
            ym,
            zm,
            ym,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Nếu tồn tại điểm D sao cho G là trọng tâm của tam giác BCD thì D có cao độ lớn hơn bound_zd
    vdc_da_1_d = (
        "\\True Nếu tồn tại điểm $D$ sao cho $G$ là trọng tâm của tam giác $BCD$ thì $D$ có cao độ lớn hơn $%s$"
        % (bound_zd)
    )
    vdc_da_1_s = (
        "Nếu tồn tại điểm $D$ sao cho $G$ là trọng tâm của tam giác $BCD$ thì $D$ có cao độ lớn hơn $%s$"
        % (bound_zd_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì điểm $G$ là trọng tâm của tam giác $BCD$ nên tọa độ của $G$ thỏa mãn: \\\\ $\\begin{cases} x_G = \\frac{x_B + x_C + x_D}{3} \\\\ y_G = \\frac{y_B + y_C + y_D}{3} \\\\ z_G = \\frac{z_B + z_C + z_D}{3} \\end{cases} \\Leftrightarrow \\begin{cases} x_D = 3x_G - x_B - x_C = 3 \\cdot (%s) - (%s) - (%s) = %s \\\\ y_D = 3y_G - y_B - y_C = 3 \\cdot (%s) - (%s) - (%s) = %s \\\\ z_D = 3z_G - z_B - z_C = 3 \\cdot (%s) - (%s) - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $D$ là $D(%s;%s;%s)$. \\\\ Cao độ của điểm $D$ là $z_D = %s > %s$."""
        % (
            xg,
            xb,
            xc,
            xd,
            yg,
            yb,
            yc,
            yd,
            zg,
            zb,
            zc,
            zd,
            xd,
            yd,
            zd,
            zd,
            bound_zd,
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
    