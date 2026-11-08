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


def bt_dang14_p2_b2_c1_hh12(self):
    # Random toạ độ ba điểm A, B, C không thẳng hàng
    # Cố tình chọn yA + yB + yC = 0 để tung độ trọng tâm bằng 0 (khớp bản chất câu hỏi)
    while True:
        xa = random.randint(-4, 4)
        ya = random.choice([-3, -2, -1, 1, 2, 3])
        za = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    
        xb = random.randint(-4, 4)
        yb = random.choice([-3, -2, -1, 1, 2, 3])
        zb = random.randint(-5, 5)
    
        xc = random.randint(-4, 4)
        yc = -(ya + yb)
        zc = random.randint(-5, 5)
    
        # Tọa độ các vectơ AB, AC
        ab_x, ab_y, ab_z = xb - xa, yb - ya, zb - za
        ac_x, ac_y, ac_z = xc - xa, yc - ya, zc - za
    
        # Tích có hướng [AB, AC] để kiểm tra ba điểm không thẳng hàng
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
    
    # 1. Vectơ AB = (ab_x; ab_y; ab_z)
    # 2. Khoảng cách từ A(xa; ya; za) đến mặt phẳng (Oxy): d(A, (Oxy)) = |za|
    dist_A_Oxy = abs(za)
    dist_A_Oxy_s = abs(za) + random.choice([1, 2])
    
    # 3. Tung độ trọng tâm G của tam giác ABC:
    # yG = (ya + yb + yc) / 3 = 0
    
    # 4. Tứ giác ABCD là hình bình hành <=> vecto AB = vecto DC <=> D = C - AB = C + A - B
    xd = xc + xa - xb
    yd = yc + ya - yb
    zd = zc + za - zb
    
    # Mốc so sánh cho cao độ của D (chọn mốc zd - 1 để khẳng định 'lớn hơn zd - 1' là đúng)
    bound_zd = zd - 1
    bound_zd_s = zd + 1
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho ba điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$ và $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Vectơ AB
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (-ab_x, -ab_y, -ab_z)
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
    # Khẳng định b: Điểm A cách mặt phẳng (Oxy) một khoảng bằng ...
    th_da_1_d = (
        "\\True Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$"
        % (xa, ya, za, dist_A_Oxy)
    )
    th_da_1_s = (
        "Điểm $A(%s;%s;%s)$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$"
        % (xa, ya, za, dist_A_Oxy_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Mặt phẳng $(Oxy)$ có phương trình là $z = 0$. \\\\ Khoảng cách từ điểm $A(%s;%s;%s)$ đến mặt phẳng $(Oxy)$ là: \\\\ $d(A, (Oxy)) = |z_A| = |%s| = %s$."""
        % (xa, ya, za, za, dist_A_Oxy)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Trọng tâm tam giác ABC có tung độ bằng 0
    vd_da_1_d = "\\True Trọng tâm tam giác $ABC$ có tung độ bằng $0$"
    vd_da_1_s = "Trọng tâm tam giác $ABC$ có tung độ bằng $1$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Tung độ của trọng tâm tam giác $ABC$ được tính theo công thức: \\\\ $y_G = \\frac{y_A + y_B + y_C}{3} = \\frac{%s + (%s) + (%s)}{3} = 0$. \\\\ Vậy trọng tâm tam giác $ABC$ có tung độ bằng $0$."""
        % (ya, yb, yc)
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tồn tại điểm D sao cho tứ giác ABCD là hình bình hành thì D có cao độ lớn hơn ...
    vdc_da_1_d = (
        "\\True Tồn tại điểm $D$ sao cho tứ giác $ABCD$ là hình bình hành thì $D$ có cao độ lớn hơn $%s$"
        % (bound_zd)
    )
    vdc_da_1_s = (
        "Tồn tại điểm $D$ sao cho tứ giác $ABCD$ là hình bình hành thì $D$ có cao độ lớn hơn $%s$"
        % (bound_zd_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi tọa độ điểm $D$ là $D(x_D; y_D; z_D)$. \\\\ Để tứ giác $ABCD$ là hình bình hành thì: \\\\ $\\vec{AB} = \\vec{DC} \\Leftrightarrow (x_B - x_A; y_B - y_A; z_B - z_A) = (x_C - x_D; y_C - y_D; z_C - z_D)$ \\\\ $\\Leftrightarrow \\begin{cases} x_C - x_D = %s \\\\ y_C - y_D = %s \\\\ z_C - z_D = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_D = x_C - (%s) = %s - (%s) = %s \\\\ y_D = y_C - (%s) = %s - (%s) = %s \\\\ z_D = z_C - (%s) = %s - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $D$ là $D(%s;%s;%s)$. \\\\ Do đó điểm $D$ có cao độ $z_D = %s > %s$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            ab_x,
            xc,
            ab_x,
            xd,
            ab_y,
            yc,
            ab_y,
            yd,
            ab_z,
            zc,
            ab_z,
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
    