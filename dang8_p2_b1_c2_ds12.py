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


def bt_dang8_p2_b1_c2_ds12(self):
    # Hàm hỗ trợ định dạng số thập phân thành chuỗi dùng dấu phẩy
    def fmt(val, decimals=4):
        s = f"{val:.{decimals}f}".rstrip('0').rstrip('.')
        if s == '': s = '0'
        return s.replace('.', ',')

    # Cấu hình các nhóm (intervals) và giá trị đại diện
    intervals = [(3, 6), (6, 9), (9, 12), (12, 15), (15, 18)]
    x_c = [4.5, 7.5, 10.5, 13.5, 16.5]
    h = 3

    # Random tần số (đảm bảo nhóm 2 có tần số lớn nhất để là nhóm chứa Mốt)
    m1 = random.randint(20, 30)
    m2 = random.randint(50, 65)
    m3 = random.randint(35, 48)
    m4 = random.randint(25, 35)
    m5 = random.randint(5, 15)

    freqs = [m1, m2, m3, m4, m5]
    N = sum(freqs)

    # Tần số tích luỹ
    cf = []
    current_sum = 0
    for f in freqs:
        current_sum += f
        cf.append(current_sum)

    # a) Số trung bình
    sum_fx = sum([f * x for f, x in zip(freqs, x_c)])
    mean_val = sum_fx / N
    mean_str = fmt(mean_val, 4)
    mean_fake_str = fmt(mean_val + random.choice([0.5, -0.5, 1.0]), 4)

    # b) Mốt (rơi vào nhóm 2: [6;9))
    idx_mo = 1
    L_mo = intervals[idx_mo][0]
    f_mo = freqs[idx_mo]
    f_prev = freqs[idx_mo - 1]
    f_next = freqs[idx_mo + 1]

    Mo_val = L_mo + ((f_mo - f_prev) / ((f_mo - f_prev) + (f_mo - f_next))) * h
    Mo_str = fmt(Mo_val, 4)
    Mo_fake_str = fmt(Mo_val + random.choice([0.25, -0.25, 0.5]), 4)

    # c) Khoảng biến thiên
    R = 18 - 3
    R_fake = random.choice([12, 14, 16])

    # d) Tứ phân vị thứ ba Q3 (dành cho 25% hộ tiêu thụ cao nhất)
    # Vị trí Q3 là 3N/4
    pos_q3 = 3 * N / 4
    # Thường Q3 sẽ rơi vào nhóm 3 hoặc 4. Ta viết tổng quát để tìm nhóm chứa Q3
    idx_q3 = 0
    while idx_q3 < len(cf) and cf[idx_q3] < pos_q3:
        idx_q3 += 1

    L_q3 = intervals[idx_q3][0]
    cf_prev_q3 = cf[idx_q3 - 1] if idx_q3 > 0 else 0
    f_q3 = freqs[idx_q3]

    Q3_val = L_q3 + ((pos_q3 - cf_prev_q3) / f_q3) * h
    Q3_str = fmt(Q3_val, 2)
    Q3_fake_str = fmt(Q3_val + random.choice([-1.5, -0.5, 1.2]), 2)


    # Nội dung câu hỏi
    noidungcauhoi = ('''Một công ty cung cấp nước sạch thống kê lượng nước các hộ gia đình trong một khu vực tiêu thụ trong một tháng ở bảng sau:
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|c|}
    \\hline
    Lượng nước tiêu thụ ($m^3$) & $[3; 6)$ & $[6; 9)$ & $[9; 12)$ & $[12; 15)$ & $[15; 18)$ \\\\
    \\hline
    Số hộ gia đình & %s & %s & %s & %s & %s \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (m1, m2, m3, m4, m5))

    ######################################################################## Nhận biết (Hỏi Trung bình) ############################################
    nb_da_1_d = '\\True Số trung bình của mẫu số liệu ghép nhóm đã cho là $%s$' % mean_str
    nb_da_1_s = 'Số trung bình của mẫu số liệu ghép nhóm đã cho là $%s$' % mean_fake_str
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    # Chuỗi tính toán trung bình
    mean_calc = " + ".join([f"{f} \\cdot {str(x).replace('.', ',')}" for f, x in zip(freqs, x_c)])

    loigiai_nb_1 = ('''Cỡ mẫu $n = %s$. Bảng tần số ghép nhóm của mẫu số liệu trên như sau:
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|c|}
    \\hline
    Lượng nước tiêu thụ ($m^3$) & $[3; 6)$ & $[6; 9)$ & $[9; 12)$ & $[12; 15)$ & $[15; 18)$ \\\\
    \\hline
    Giá trị đại diện & 4,5 & 7,5 & 10,5 & 13,5 & 16,5 \\\\
    \\hline
    Số hộ gia đình & %s & %s & %s & %s & %s \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    Số trung bình của mẫu số liệu ghép nhóm đã cho là 
    $\\overline{x} = \\frac{1}{%s}(%s) = %s$.''' 
    % (N, m1, m2, m3, m4, m5, N, mean_calc, mean_str))
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu (Hỏi Mốt) ############################################
    th_da_1_d = '\\True Mốt của mẫu số liệu là $M_o = %s$' % Mo_str
    th_da_1_s = 'Mốt của mẫu số liệu là $M_o = %s$' % Mo_fake_str
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Nhóm chứa mốt của mẫu số liệu ghép nhóm trên là nhóm $[6; 9)$. \\\\
    Do đó: $u_m = 6; n_m = %s; n_{m-1} = %s; n_{m+1} = %s; u_{m+1} = 9$. \\\\
    Mốt của mẫu số liệu là $M_o = 6 + \\frac{(%s - %s)}{(%s - %s) + (%s - %s)} \\cdot (9 - 6) = %s$.''' 
    % (f_mo, f_prev, f_next, f_mo, f_prev, f_mo, f_prev, f_mo, f_next, Mo_str))
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng (Khoảng biến thiên) ############################################
    vd_da_1_d = '\\True Khoảng biến thiên của mẫu số liệu ghép nhóm đã cho là $%s$' % R
    vd_da_1_s = 'Khoảng biến thiên của mẫu số liệu ghép nhóm đã cho là $%s$' % R_fake
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Khoảng biến thiên của mẫu số liệu là: $R = 18 - 3 = %s$''' % R)
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao (Hỏi Q3) ############################################
    vdc_da_1_d = '\\True Công ty muốn gửi một thông báo khuyến nghị tiết kiệm nước đến 25\\%% các hộ gia đình có lượng nước tiêu thụ cao nhất. Khi đó công ty nên gửi thông báo tiết kiệm nước đến các hộ gia đình có lượng nước tiêu thụ từ $%s m^3$ nước trở lên' % Q3_str
    vdc_da_1_s = 'Công ty muốn gửi một thông báo khuyến nghị tiết kiệm nước đến 25\\%% các hộ gia đình có lượng nước tiêu thụ cao nhất. Khi đó công ty nên gửi thông báo tiết kiệm nước đến các hộ gia đình có lượng nước tiêu thụ từ $%s m^3$ nước trở lên' % Q3_fake_str
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    pos_q3_val = 3 * N / 4
    if pos_q3_val.is_integer():
        q3_idx = f"\\frac{{1}}{{2}}(x_{{{int(pos_q3_val)}}} + x_{{{int(pos_q3_val)+1}}})"
    else:
        q3_idx = f"x_{{{int(pos_q3_val) + 1}}}"

    interval_str = f"[{intervals[idx_q3][0]}; {intervals[idx_q3][1]})"

    loigiai_vdc_1 = ('''25\\%% các hộ gia đình có lượng nước tiêu thụ cao nhất có lượng nước tiêu thụ không nhỏ hơn $Q_3$, với $Q_3$ là tứ phân vị thứ ba của mẫu số liệu. \\\\
    Tứ phân vị thứ ba của dãy số liệu $x_1; x_2; \\dots; x_{%s}$ là $%s$. \\\\
    Do phần tử này thuộc nhóm $%s$ nên tứ phân vị thứ ba của mẫu số liệu là \\\\
    $Q_3 = %s + \\frac{\\frac{%s \\cdot 3}{4} - %s}{%s} \\cdot %s \\approx %s$ \\\\
    Vậy công ty nên gửi thông báo tiết kiệm nước đến các hộ gia đình có lượng nước tiêu thụ từ $%s m^3$ nước trở lên.''' 
    % (N, q3_idx, interval_str, L_q3, N, cf_prev_q3, f_q3, h, Q3_str, Q3_str))
    list_vdc_2 = [loigiai_vdc_1]


    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Đảm bảo số lượng câu đúng từ 1 đến 3
    while True:
        nb_da = random.choice(list_nb_da_1)
        th_da = random.choice(list_th_da_1)
        vd_da = random.choice(list_vd_da_1)
        vdc_da = random.choice(list_vdc_da_1)
        answers = [nb_da, th_da, vd_da, vdc_da]
        if 1 <= count_true_answers(answers) <= 3:
            break

    list_nb_1 = [nb_da]
    list_th_1 = [th_da]
    list_vd_1 = [vd_da]
    list_vdc_1 = [vdc_da]

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

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + ' \n'
        '\\choiceTFn \n'
        '{' + str(shuffled_answers_nb[0]) + '}\n'
        '{' + str(shuffled_answers_th[0]) + '}\n'
        '{' + str(shuffled_answers_vd[0]) + '}\n'
        '{' + str(shuffled_answers_vdc[0]) + '}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n\\end{minipage}\n\n').replace('\\frac','\\dfrac')
    return content

