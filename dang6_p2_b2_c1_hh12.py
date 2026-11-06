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


def bt_dang6_p2_b2_c1_hh12(self):
    # Hàm phụ trợ để format vectơ i, j, k chuẩn toán học (ẩn hệ số 1, -1, 0)
    def format_ijk(x, y, z):
        res = ""
        # Xử lý i
        if x == 1: res += "\\vec{i}"
        elif x == -1: res += "-\\vec{i}"
        elif x != 0: res += f"{x}\\vec{{i}}"

        # Xử lý j
        if y == 1: res += "+\\vec{j}" if x != 0 else "\\vec{j}"
        elif y == -1: res += "-\\vec{j}"
        elif y > 0: res += f"+{y}\\vec{{j}}" if x != 0 else f"{y}\\vec{{j}}"
        elif y < 0: res += f"{y}\\vec{{j}}"

        # Xử lý k
        if z == 1: res += "+\\vec{k}" if (x != 0 or y != 0) else "\\vec{k}"
        elif z == -1: res += "-\\vec{k}"
        elif z > 0: res += f"+{z}\\vec{{k}}" if (x != 0 or y != 0) else f"{z}\\vec{{k}}"
        elif z < 0: res += f"{z}\\vec{{k}}"

        if res == "": res = "\\vec{0}"
        return res

    # Khai báo biến
    a1, a2, a3 = random.sample([i for i in range(-5, 6) if i != 0], 3)
    xA, yA, zA = [random.randint(-5, 5) for _ in range(3)]

    # Random vector b không cùng phương với a và các hệ số khác 0 để lập tỉ số dễ nhìn
    while True:
        b1, b2, b3 = [random.choice([i for i in range(-5, 6) if i != 0]) for _ in range(3)]
        # Kiểm tra điều kiện không cùng phương (tỉ lệ chéo khác nhau)
        if (a1 * b2 != a2 * b1) or (a1 * b3 != a3 * b1):
            break

    # Nội dung câu hỏi
    noidungcauhoi = f"Trong không gian $Oxyz$, cho hai vectơ $\\vec{{a}}=({a1};{a2};{a3})$, $\\vec{{b}}=({b1};{b2};{b3})$ và điểm $A({xA};{yA};{zA})$."

    ######################################################################## Nhận biết ############################################
    # Xử lý chuỗi ijk cho vec a
    str_vec_a_true = format_ijk(a1, a2, a3)
    str_vec_a_false = format_ijk(-a1, a2, a3) # Cố tình sai dấu hệ số đầu

    # Các đáp án
    nb_da_1_d = f"\\True $\\vec{{a}} = {str_vec_a_true}$"
    nb_da_1_s = f"$\\vec{{a}} = {str_vec_a_false}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = f"Ta có vectơ $\\vec{{a}}=({a1};{a2};{a3}) \\Rightarrow \\vec{{a}} = {str_vec_a_true}$."
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ######################################################################## Thông hiểu ############################################
    # Tính toán điểm B (Đúng là A + vec_a, Sai cố tình lấy A - vec_a)
    xB_t, yB_t, zB_t = xA + a1, yA + a2, zA + a3
    xB_s, yB_s, zB_s = xA - a1, yA - a2, zA - a3

    # Các đáp án
    th_da_1_d = f"\\True Tọa độ điểm $B({xB_t}; {yB_t}; {zB_t})$ thì $\\vec{{a}} = \\overrightarrow{{AB}}$"
    th_da_1_s = f"Tọa độ điểm $B({xB_s}; {yB_s}; {zB_s})$ thì $\\vec{{a}} = \\overrightarrow{{AB}}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = (f"Vì $\\vec{{a}} = \\overrightarrow{{AB}} \\Leftrightarrow "
                    f"\\begin{{cases}} {a1} = x_B - ({xA}) \\\\ {a2} = y_B - ({yA}) \\\\ {a3} = z_B - ({zA}) \\end{{cases}} \\Leftrightarrow "
                    f"\\begin{{cases}} x_B = {xB_t} \\\\ y_B = {yB_t} \\\\ z_B = {zB_t} \\end{{cases}} \\Rightarrow B({xB_t}; {yB_t}; {zB_t})$.")
    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = "\\True Hai vectơ $\\vec{a}$ và $\\vec{b}$ không cùng phương"
    vd_da_1_s = "Hai vectơ $\\vec{a}$ và $\\vec{b}$ cùng phương"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    # Tìm 2 tỉ số khác nhau để minh họa lời giải
    if a1*b2 != a2*b1:
        phan_so_str = f"\\dfrac{{{a1}}}{{{b1}}} \\neq \\dfrac{{{a2}}}{{{b2}}}"
    elif a2*b3 != a3*b2:
        phan_so_str = f"\\dfrac{{{a2}}}{{{b2}}} \\neq \\dfrac{{{a3}}}{{{b3}}}"
    else:
        phan_so_str = f"\\dfrac{{{a1}}}{{{b1}}} \\neq \\dfrac{{{a3}}}{{{b3}}}"

    # Nội dung lời giải
    loigiai_vd_1 = f"Vì ${phan_so_str}$ nên hai vectơ $\\vec{{a}}$ và $\\vec{{b}}$ không cùng phương."
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################
    # Sinh điểm M ngẫu nhiên
    xM, yM, zM = random.randint(-4, 4), random.randint(-4, 4), random.randint(-4, 4)
    # Tính vec AM đúng và sai
    am_x_t, am_y_t, am_z_t = xM - xA, yM - yA, zM - zA
    str_am_true = format_ijk(am_x_t, am_y_t, am_z_t)
    str_am_false = format_ijk(-am_x_t, -am_y_t, -am_z_t) # Tính nhầm thành vec MA

    # Các đáp án
    vdc_da_1_d = f"\\True Cho $M({xM}; {yM}; {zM})$ thì $\\overrightarrow{{AM}} = {str_am_true}$"
    vdc_da_1_s = f"Cho $M({xM}; {yM}; {zM})$ thì $\\overrightarrow{{AM}} = {str_am_false}$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = f"Ta có: $M({xM}; {yM}; {zM}) \\longrightarrow \\overrightarrow{{AM}} = ({am_x_t}; {am_y_t}; {am_z_t}) = {str_am_true}$."
    list_vdc_2 = [loigiai_vdc_1]

    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
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
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
    str(noidungcauhoi)+ 
        '\n\\choiceTFn \n'
       '{'+str(shuffled_answers_nb[0])+'}\n'
       '{'+str(shuffled_answers_th[0])+'}\n'
       '{'+str(shuffled_answers_vd[0])+'}\n'
       '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

