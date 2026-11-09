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


def bt_dang31_p2_b2_c1_hh12(self):
    # Random toạ độ các đỉnh A, B, C, Q của hình hộp ABCD.MNPQ
    # Các cặp đỉnh tương ứng cạnh bên: AM, BN, CP, DQ
    while True:
        xa = random.randint(-4, 4)
        ya = 0  # Chọn tung độ bằng 0 như bài gốc
        za = random.randint(-3, 3)
    
        xb = random.choice([-3, -2, -1, 1, 2, 3])
        yb = random.randint(1, 4)
        zb = random.choice([-3, -2, -1, 1, 2, 3])
    
        xc = random.randint(-4, 4)
        yc = 0
        zc = random.randint(-3, 3)
    
        # Đỉnh Q tương ứng với đỉnh D (cạnh bên DQ song song và cùng hướng AM)
        xq = random.randint(-4, 4)
        yq = random.randint(1, 5)
        zq = random.randint(-4, 4)
    
        # Vectơ AB, AC
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        # Kiểm tra ba điểm A, B, C không thẳng hàng
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
        ):
            break
    
    # 1. Tâm O của hình bình hành ABCD là trung điểm của AC và BD
    # 2. Điểm B: có xB != 0 hoặc zB != 0 nên B không thuộc trục Oy (vì điểm thuộc Oy phải có x = z = 0)
    # 3. Tọa độ đỉnh D: Vì ABCD là hình bình hành nên:
    # vecto AB = vecto DC <=> D = C - AB = C + A - B
    xd = xc + xa - xb
    yd = yc + ya - yb
    zd = zc + za - zb
    
    # Tọa độ D sai (đổi dấu cao độ như đề bài gốc)
    zd_s = -zd if zd != 0 else zd + 2
    
    # 4. Tọa độ đỉnh M:
    # Trong hình hộp ABCD.MNPQ, các cạnh bên là AM, BN, CP, DQ
    # Do đó vecto AM = vecto DQ = (xQ - xD; yQ - yD; zQ - zD)
    # => M = A + vecto DQ = (xA + xQ - xD; yA + yQ - yD; zA + zQ - zD)
    xm = xa + xq - xd
    ym = ya + yq - yd
    zm = za + zq - zd
    
    # Tọa độ M sai (thay đổi cao độ như đề bài gốc)
    zm_s = zm + random.choice([-4, -3, 3, 4])
    
    # Nội dung câu hỏi[cite: 27]
    noidungcauhoi = (
        """Cho hình hộp $ABCD.MNPQ$ có $O$ là tâm hình bình hành $ABCD$ có các đỉnh $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s), Q(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xq, yq, zq)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: O là trung điểm của AC[cite: 27]
    nb_da_1_d = "\\True $O$ là trung điểm của $AC$"
    nb_da_1_s = "$O$ là trung điểm của $AB$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = """Vì tứ giác $ABCD$ là hình bình hành và $O$ là tâm của hình bình hành nên $O$ là giao điểm của hai đường chéo $AC$ và $BD$. \\\\ Do đó $O$ là trung điểm của đoạn thẳng $AC$ và đoạn thẳng $BD$."""
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: B thuộc trục Oy[cite: 27]
    th_da_1_d = "\\True $B$ không thuộc trục $Oy$"
    th_da_1_s = "$B$ thuộc trục $Oy$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Một điểm thuộc trục $Oy$ khi và chỉ khi hoành độ và cao độ của nó đều bằng $0$. \\\\ Tọa độ điểm $B$ là $B(%s;%s;%s)$ có hoành độ $x_B = %s \\neq 0$ và cao độ $z_B = %s \\neq 0$. \\\\ Do đó điểm $B$ không thuộc trục $Oy$."""
        % (xb, yb, zb, xb, zb)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Tọa độ điểm D[cite: 27]
    vd_da_1_d = "\\True $D(%s;%s;%s)$" % (xd, yd, zd)
    vd_da_1_s = "$D(%s;%s;%s)$" % (xd, yd, zd_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $ABCD$ là hình bình hành nên: \\\\ $\\vec{AB} = \\vec{DC} \\Leftrightarrow \\begin{cases} x_B - x_A = x_C - x_D \\\\ y_B - y_A = y_C - y_D \\\\ z_B - z_A = z_C - z_D \\end{cases} \\Leftrightarrow \\begin{cases} x_D = x_C + x_A - x_B = %s + (%s) - (%s) = %s \\\\ y_D = y_C + y_A - y_B = %s + (%s) - (%s) = %s \\\\ z_D = z_C + z_A - z_B = %s + (%s) - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $D$ là $D(%s;%s;%s)$."""
        % (
            xc,
            xa,
            xb,
            xd,
            yc,
            ya,
            yb,
            yd,
            zc,
            za,
            zb,
            zd,
            xd,
            yd,
            zd,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tọa độ điểm M[cite: 27]
    vdc_da_1_d = "\\True $M(%s;%s;%s)$" % (xm, ym, zm)
    vdc_da_1_s = "$M(%s;%s;%s)$" % (xm, ym, zm_s)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    dq_x = xq - xd
    dq_y = yq - yd
    dq_z = zq - zd
    
    loigiai_vdc_1 = (
        """Trong hình hộp $ABCD.MNPQ$, các cạnh bên đôi một song song và bằng nhau, suy ra $\\vec{AM} = \\vec{DQ}$. \\\\ Ta có $\\vec{DQ} = (x_Q - x_D; y_Q - y_D; z_Q - z_D) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$. \\\\ Gọi tọa độ điểm $M(x_M; y_M; z_M)$, ta có: \\\\ $\\begin{cases} x_M - x_A = %s \\\\ y_M - y_A = %s \\\\ z_M - z_A = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_M = x_A + (%s) = %s + (%s) = %s \\\\ y_M = y_A + (%s) = %s + (%s) = %s \\\\ z_M = z_A + (%s) = %s + (%s) = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $M$ là $M(%s;%s;%s)$."""
        % (
            xq,
            xd,
            yq,
            yd,
            zq,
            zd,
            dq_x,
            dq_y,
            dq_z,
            dq_x,
            dq_y,
            dq_z,
            dq_x,
            xa,
            dq_x,
            xm,
            dq_y,
            ya,
            dq_y,
            ym,
            dq_z,
            za,
            dq_z,
            zm,
            xm,
            ym,
            zm,
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
    