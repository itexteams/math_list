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


def bt_dang21_p2_b3_c1_hh12(self):
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C không thẳng hàng
    while True:
        xa = random.randint(-4, 4)
        ya = random.randint(3, 6)
        za = random.randint(-3, 3)
    
        # Điểm B và C có cùng tung độ y_bc để câu c liên quan đến hình chiếu trên Oy[cite: 20]
        y_bc = random.randint(-2, 2)
    
        xb = random.choice([3, 4, 5, 6])
        yb = y_bc
        zb = random.randint(1, 4)
    
        xc = random.choice([1, 2, 3])
        yc = y_bc
        zc = random.randint(-4, -1)
    
        # Đảm bảo ba điểm A, B, C không thẳng hàng
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        ac_x = xc - xa
        ac_y = yc - ya
        ac_z = zc - za
    
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        ab_sq = ab_x**2 + ab_y**2 + ab_z**2
        ac_sq = ac_x**2 + ac_y**2 + ac_z**2
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and ab_sq != ac_sq
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
        ):
            break
    
    # 1. So sánh độ dài đoạn thẳng AB và AC[cite: 20]
    is_ab_gt_ac = ab_sq > ac_sq
    
    # 2. Hình chiếu của B lên trục Ox là (xb; 0; 0)[cite: 20]
    # Tọa độ sai: lấy nhầm tung độ hoặc số khác như đề gốc (yb; 0; 0)[cite: 20]
    xb_proj_s = yb if yb != xb else xb + 1
    
    # 3. Hình chiếu của B và C lên trục Oy[cite: 20]
    # Vì yB = yC nên hình chiếu của B và C lên trục Oy cùng là (0; y_bc; 0), tức là trùng nhau[cite: 20]
    
    # 4. Tập hợp điểm M thỏa mãn |MA + MB + MC| = k_val[cite: 20]
    k_val = random.choice([3, 5, 6, 9])
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$ cho ba điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Phát biểu a: So sánh AB và AC[cite: 20]
    if is_ab_gt_ac:
        nb_da_1_d = "\\True $AB > AC$"
        nb_da_1_s = "$AB < AC$"
    else:
        nb_da_1_d = "\\True $AB < AC$"
        nb_da_1_s = "$AB > AC$"
    
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có: \\\\ $AB = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $AC = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Vì $%s %s %s$ nên $\\sqrt{%s} %s \\sqrt{%s}$, suy ra $AB %s AC$."""
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
            ab_sq,
            xc,
            xa,
            yc,
            ya,
            zc,
            za,
            ac_x,
            ac_y,
            ac_z,
            ac_sq,
            ab_sq,
            ">" if is_ab_gt_ac else "<",
            ac_sq,
            ab_sq,
            ">" if is_ab_gt_ac else "<",
            ac_sq,
            ">" if is_ab_gt_ac else "<",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Phát biểu b: Tọa độ hình chiếu của B lên trục Ox[cite: 20]
    th_da_1_d = "\\True Tọa độ hình chiếu của $B$ lên trục $Ox$ là $(%s;0;0)$" % (xb)
    th_da_1_s = "Tọa độ hình chiếu của $B$ lên trục $Ox$ là $(%s;0;0)$" % (xb_proj_s)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Hình chiếu vuông góc của điểm $B(%s;%s;%s)$ lên trục $Ox$ giữ nguyên hoành độ, tung độ và cao độ bằng $0$. \\\\ Do đó hình chiếu của $B$ lên trục $Ox$ có tọa độ là $(%s;0;0)$."""
        % (xb, yb, zb, xb)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Phát biểu c: Hình chiếu của hai điểm B và C lên trục Oy[cite: 20]
    vd_da_1_d = "\\True Hình chiếu của hai điểm $B$ và $C$ lên trục $Oy$ trùng với nhau"
    vd_da_1_s = "Hình chiếu của hai điểm $B$ và $C$ lên trục $Oy$ không trùng với nhau"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Hình chiếu vuông góc của điểm $B(%s;%s;%s)$ lên trục $Oy$ là điểm $B'(0;%s;0)$. \\\\ Hình chiếu vuông góc của điểm $C(%s;%s;%s)$ lên trục $Oy$ là điểm $C'(0;%s;0)$. \\\\ Vì tung độ của $B$ và $C$ bằng nhau ($y_B = y_C = %s$) nên $B' \\equiv C'$. \\\\ Do đó hình chiếu của hai điểm $B$ và $C$ lên trục $Oy$ trùng với nhau."""
        % (xb, yb, zb, yb, xc, yc, zc, yc, y_bc)
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Phát biểu d: Có đúng một điểm M thỏa mãn |MA + MB + MC| = k_val[cite: 20]
    vdc_da_1_d = (
        "\\True Có vô số điểm $M$ thỏa mãn $\\left|\\vec{MA} + \\vec{MB} + \\vec{MC}\\right| = %s$"
        % (k_val)
    )
    vdc_da_1_s = (
        "Có đúng một điểm $M$ thỏa mãn $\\left|\\vec{MA} + \\vec{MB} + \\vec{MC}\\right| = %s$"
        % (k_val)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    radius_val = Rational(k_val, 3)
    if radius_val.q == 1:
        str_radius = str(radius_val.p)
    else:
        str_radius = "\\frac{%s}{%s}" % (radius_val.p, radius_val.q)
    
    loigiai_vdc_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$. Khi đó ta có: \\\\ $\\vec{MA} + \\vec{MB} + \\vec{MC} = 3\\vec{MG}$. \\\\ Suy ra: \\\\ $\\left|\\vec{MA} + \\vec{MB} + \\vec{MC}\\right| = %s \\Leftrightarrow \\left|3\\vec{MG}\\right| = %s \\Leftrightarrow 3 MG = %s \\Leftrightarrow MG = %s$. \\\\ Do đó tập hợp các điểm $M$ trong không gian là một mặt cầu tâm $G$ bán kính $R = %s$. \\\\ Vì vậy có vô số điểm $M$ thỏa mãn yêu cầu bài toán, mệnh đề khẳng định có đúng một điểm $M$ là sai."""
        % (k_val, k_val, k_val, str_radius, str_radius)
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
    