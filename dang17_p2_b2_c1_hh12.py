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


def bt_dang17_p2_b2_c1_hh12(self):
    # Hàm biểu diễn vectơ theo hệ vectơ đơn vị i, j, k
    def format_ijk_vector(x_val, y_val, z_val):
        terms = []
        # Thành phần i
        if x_val == 1:
            terms.append("\\vec{i}")
        elif x_val == -1:
            terms.append("-\\vec{i}")
        elif x_val != 0:
            terms.append("%s\\vec{i}" % x_val)
    
        # Thành phần j
        if y_val == 1:
            terms.append("+\\vec{j}" if terms else "\\vec{j}")
        elif y_val == -1:
            terms.append("-\\vec{j}")
        elif y_val > 0:
            terms.append("+%s\\vec{j}" % y_val if terms else "%s\\vec{j}" % y_val)
        elif y_val < 0:
            terms.append("%s\\vec{j}" % y_val)
    
        # Thành phần k
        if z_val == 1:
            terms.append("+\\vec{k}" if terms else "\\vec{k}")
        elif z_val == -1:
            terms.append("-\\vec{k}")
        elif z_val > 0:
            terms.append("+%s\\vec{k}" % z_val if terms else "%s\\vec{k}" % z_val)
        elif z_val < 0:
            terms.append("%s\\vec{k}" % z_val)
    
        if not terms:
            return "\\vec{0}"
        return "".join(terms)
    
    
    # Random toạ độ điểm A nằm trên trục Oz và điểm B
    while True:
        xa, ya = 0, 0
        za = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    
        xb = random.choice([-3, -2, -1, 1, 2, 3])
        yb = random.choice([-3, -2, -1, 1, 2, 3])
        zb = random.choice([-3, -2, -1, 1, 2, 3])
    
        # Khoảng cách OE (độ dài trên tia Ox)
        len_oe = random.randint(2, 6)
    
        # Vectơ AB
        ab_x = xb - xa
        ab_y = yb - ya
        ab_z = zb - za
    
        if ab_z != 0:
            break
    
    # 1. Vectơ AB = (ab_x; ab_y; ab_z)
    # 2. Biểu diễn vectơ OB theo các vectơ đơn vị i, j, k
    str_ob_true = format_ijk_vector(xb, yb, zb)
    # Dạng sai: đổi dấu toàn bộ các toạ độ
    str_ob_false = format_ijk_vector(-xb, -yb, -zb)
    
    # 3. ABOD là hình bình hành <=> vecto AB = vecto DO <=> O - D = B - A <=> D = A - B
    xd = xa - xb
    yd = ya - yb
    zd = za - zb
    
    # Toạ độ sai của D (nhầm sang D = B - A = vecto AB)
    xd_s = ab_x
    yd_s = ab_y
    zd_s = ab_z
    
    # 4. Điểm E thuộc tia Ox thỏa mãn OE = len_oe => E(len_oe; 0; 0)
    xe = len_oe
    ye = 0
    ze = 0
    
    # Tọa độ sai của E (nhầm sang tia đối Ox hoặc đặt nhầm trục)
    xe_s = -len_oe
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hai điểm $A(%s;%s;%s)$ và $B(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ AB
    nb_da_1_d = "\\True $\\vec{AB} = (%s;%s;%s)$" % (ab_x, ab_y, ab_z)
    nb_da_1_s = "$\\vec{AB} = (%s;%s;%s)$" % (-ab_x, -ab_y, -ab_z)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s - %s; %s - %s; %s - (%s)) = (%s;%s;%s)$."""
        % (xb, xa, yb, ya, zb, za, ab_x, ab_y, ab_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Vectơ OB phân tích theo các vectơ đơn vị
    th_da_1_d = "\\True $\\vec{OB} = %s$" % (str_ob_true)
    th_da_1_s = "$\\vec{OB} = %s$" % (str_ob_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì điểm $B$ có tọa độ là $B(%s;%s;%s)$ nên theo định nghĩa tọa độ của vectơ trong không gian ta có: \\\\ $\\vec{OB} = %s\\vec{i} + (%s)\\vec{j} + (%s)\\vec{k} = %s$."""
        % (xb, yb, zb, xb, yb, zb, str_ob_true)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Biết ABOD là hình bình hành, tọa độ điểm D
    vd_da_1_d = (
        "\\True Biết $ABOD$ hình bình hành, tọa độ điểm $D$ là $(%s;%s;%s)$"
        % (xd, yd, zd)
    )
    vd_da_1_s = (
        "Biết $ABOD$ hình bình hành, tọa độ điểm $D$ là $(%s;%s;%s)$"
        % (xd_s, yd_s, zd_s)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Gọi tọa độ điểm $D$ là $D(x_D; y_D; z_D)$. \\\\ Gốc tọa độ $O$ có tọa độ $O(0;0;0)$. \\\\ Tứ giác $ABOD$ là hình bình hành khi và chỉ khi: \\\\ $\\vec{AB} = \\vec{DO} \\Leftrightarrow (x_B - x_A; y_B - y_A; z_B - z_A) = (0 - x_D; 0 - y_D; 0 - z_D)$ \\\\ $\\Leftrightarrow \\begin{cases} -x_D = %s \\\\ -y_D = %s \\\\ -z_D = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_D = %s \\\\ y_D = %s \\\\ z_D = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $D$ là $(%s;%s;%s)$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            xd,
            yd,
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
    # Mệnh đề d: Biết điểm E thuộc tia Ox thỏa mãn OE = len_oe, tọa độ điểm E
    vdc_da_1_d = (
        "\\True Biết điểm $E$ thuộc tia $Ox$ thỏa mãn $OE = %s$, tọa độ điểm $E$ là $(%s;0;0)$"
        % (len_oe, xe)
    )
    vdc_da_1_s = (
        "Biết điểm $E$ thuộc tia $Ox$ thỏa mãn $OE = %s$, tọa độ điểm $E$ là $(%s;0;0)$"
        % (len_oe, xe_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì điểm $E$ thuộc trục $Ox$ nên tọa độ điểm $E$ có dạng $E(x_E; 0; 0)$. \\\\ Hơn nữa, điểm $E$ thuộc tia $Ox$ nên $x_E > 0$. \\\\ Ta có $OE = \\sqrt{x_E^2 + 0^2 + 0^2} = |x_E| = x_E$. \\\\ Theo giả thiết $OE = %s$, suy ra $x_E = %s$. \\\\ Vậy tọa độ điểm $E$ là $(%s;0;0)$."""
        % (len_oe, xe, xe)
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
    