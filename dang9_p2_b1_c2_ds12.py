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


def bt_dang9_p2_b1_c2_ds12(self):
    # Hàm hỗ trợ định dạng số thập phân, tự động thay dấu chấm bằng dấu phẩy
    def fmt(val):
        s = f"{val:.2f}".rstrip('0').rstrip('.')
        if s == '': s = '0'
        return s.replace('.', ',')

    def fmt_rational(val):
        return fmt(float(val))

    # Các mốc điểm và khoảng
    intervals = [(6.5, 7.0), (7.0, 7.5), (7.5, 8.0), (8.0, 8.5), (8.5, 9.0), (9.0, 9.5), (9.5, 10.0)]
    x_c = [6.75, 7.25, 7.75, 8.25, 8.75, 9.25, 9.75] # Giá trị đại diện
    h = 0.5 # Độ dài nhóm

    # Random tần số (đảm bảo tổng N khoảng 80-100)
    # Chọn nhóm 4 (8.0-8.5) có tần số lớn nhất để là nhóm chứa Mốt
    m4 = random.randint(22, 28) 
    m1 = random.randint(5, 10)
    m2 = random.randint(8, 14)
    m3 = random.randint(14, 20)
    m5 = random.randint(10, 15)
    m6 = random.randint(5, 9)
    m7 = random.randint(2, 6)

    freqs = [m1, m2, m3, m4, m5, m6, m7]
    N = sum(freqs)

    # Tần số tích luỹ
    cf = []
    current_sum = 0
    for f in freqs:
        current_sum += f
        cf.append(current_sum)

    # 1. Khoảng biến thiên
    R = 10.0 - 6.5
    R_fake = random.choice([3, 4, 4.5])

    # 2. Số trung bình
    sum_fx = sum([f * x for f, x in zip(freqs, x_c)])
    mean_val = sum_fx / N
    mean_str = fmt(mean_val)
    mean_fake_str = fmt(mean_val + random.choice([0.1, -0.1, 0.2, -0.2]))

    # 3. Mốt (nhóm 4)
    idx_mo = 3
    L_mo = intervals[idx_mo][0]
    f_mo = freqs[idx_mo]
    f_prev = freqs[idx_mo - 1]
    f_next = freqs[idx_mo + 1]

    Mo_val = L_mo + ((f_mo - f_prev) / ((f_mo - f_prev) + (f_mo - f_next))) * h
    Mo_str = fmt(Mo_val)
    Mo_fake_str = fmt(Mo_val + random.choice([-0.2, -0.1, 0.1, 0.2]))

    # 4. Các tứ phân vị
    # Q1: vị trí N/4 (thường rơi vào nhóm 3: 7.5-8.0)
    pos_q1 = N / 4
    idx_q1 = 2
    L_q1 = intervals[idx_q1][0]
    cf_prev_q1 = cf[idx_q1 - 1]
    f_q1 = freqs[idx_q1]
    Q1_val = L_q1 + ((pos_q1 - cf_prev_q1) / f_q1) * h

    # Q2 (Trung vị): vị trí N/2 (thường rơi vào nhóm 4: 8.0-8.5)
    pos_q2 = N / 2
    idx_q2 = 3
    L_q2 = intervals[idx_q2][0]
    cf_prev_q2 = cf[idx_q2 - 1]
    f_q2 = freqs[idx_q2]
    Q2_val = L_q2 + ((pos_q2 - cf_prev_q2) / f_q2) * h

    # Q3: vị trí 3N/4 (thường rơi vào nhóm 5: 8.5-9.0)
    pos_q3 = 3 * N / 4
    idx_q3 = 4
    L_q3 = intervals[idx_q3][0]
    cf_prev_q3 = cf[idx_q3 - 1]
    f_q3 = freqs[idx_q3]
    Q3_val = L_q3 + ((pos_q3 - cf_prev_q3) / f_q3) * h

    Delta_Q = Q3_val - Q1_val
    Delta_Q_str = fmt(Delta_Q)
    Delta_Q_fake_str = fmt(Delta_Q + random.choice([0.5, 1.0, -0.5]))


    # Nội dung câu hỏi
    noidungcauhoi = ('''Thống kê điểm trung bình môn Toán của một số học sinh lớp 11 được cho ở bảng sau:
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|c|c|c|}
    \\hline
    Khoảng điểm & $[6,5; 7)$ & $[7; 7,5)$ & $[7,5; 8)$ & $[8; 8,5)$ & $[8,5; 9)$ & $[9; 9,5)$ & $[9,5; 10)$ \\\\
    \\hline
    Tần số & %s & %s & %s & %s & %s & %s & %s \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (m1, m2, m3, m4, m5, m6, m7))

    ######################################################################## Nhận biết ############################################
    if R == 3.5:
        r_str = "3,5"
    else:
        r_str = fmt(R)

    nb_da_1_d = '\\True Khoảng biến thiên của mẫu số liệu là $R = %s$' % r_str
    nb_da_1_s = 'Khoảng biến thiên của mẫu số liệu là $R = %s$' % fmt(R_fake)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Khoảng biến thiên của mẫu số liệu là $R = 10 - 6,5 = %s$''' % r_str)
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Số trung bình của mẫu số liệu xấp xỉ bằng: $%s$' % mean_str
    th_da_1_s = 'Số trung bình của mẫu số liệu xấp xỉ bằng: $%s$' % mean_fake_str
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    # Chuỗi phép tính số trung bình
    mean_calc_str = " + ".join([f"{fmt(x)} \\cdot {f}" for x, f in zip(x_c, freqs)])

    loigiai_th_1 = ('''Bảng giá trị đại diện:
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|c|c|c|}
    \\hline
    Khoảng điểm & $[6,5; 7)$ & $[7; 7,5)$ & $[7,5; 8)$ & $[8; 8,5)$ & $[8,5; 9)$ & $[9; 9,5)$ & $[9,5; 10)$ \\\\
    \\hline
    Giá trị đại diện & 6,75 & 7,25 & 7,75 & 8,25 & 8,75 & 9,25 & 9,75 \\\\
    \\hline
    Tần số & %s & %s & %s & %s & %s & %s & %s \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    Số trung bình của mẫu số liệu xấp xỉ bằng:
    $ \\frac{%s}{%s} \\approx %s $''' % (m1, m2, m3, m4, m5, m6, m7, mean_calc_str, N, mean_str))
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Mốt của mẫu số liệu là: $%s$' % Mo_str
    vd_da_1_s = 'Mốt của mẫu số liệu là: $%s$' % Mo_fake_str
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Nhóm chứa mốt của mẫu số liệu là: $[8; 8,5)$ \\\\
    Mốt của mẫu số liệu là: $M_0 = 8 + \\frac{%s - %s}{(%s - %s) + (%s - %s)} \\cdot (8,5 - 8) \\approx %s$''' 
    % (f_mo, f_prev, f_mo, f_prev, f_mo, f_next, Mo_str))
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = %s$' % Delta_Q_str
    vdc_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = %s$' % Delta_Q_fake_str
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    pos_q1_val = N / 4
    if pos_q1_val.is_integer():
        q1_idx = f"\\frac{{1}}{{2}}(x_{{{int(pos_q1_val)}}} + x_{{{int(pos_q1_val)+1}}})"
    else:
        q1_idx = f"x_{{{int(pos_q1_val) + 1}}}"

    pos_q2_val = N / 2
    if pos_q2_val.is_integer():
        q2_idx = f"\\frac{{1}}{{2}}(x_{{{int(pos_q2_val)}}} + x_{{{int(pos_q2_val)+1}}})"
    else:
        q2_idx = f"x_{{{int(pos_q2_val) + 1}}}"

    pos_q3_val = 3 * N / 4
    if pos_q3_val.is_integer():
        q3_idx = f"\\frac{{1}}{{2}}(x_{{{int(pos_q3_val)}}} + x_{{{int(pos_q3_val)+1}}})"
    else:
        q3_idx = f"x_{{{int(pos_q3_val) + 1}}}"

    loigiai_vdc_1 = ('''Cỡ mẫu $n = %s$. Gọi $x_1; x_2; \\dots; x_{%s}$ lần lượt là điểm của %s học sinh được xếp theo thứ tự không giảm. \\\\
    Do $x_1, \\dots, x_{%s} \\in [6,5; 7)$; $x_{%s}, \\dots, x_{%s} \\in [7; 7,5)$; $x_{%s}, \\dots, x_{%s} \\in [7,5; 8)$; $x_{%s}, \\dots, x_{%s} \\in [8; 8,5)$; $x_{%s}, \\dots, x_{%s} \\in [8,5; 9); \\dots$ \\\\
    Tứ phân vị thứ hai của dãy số liệu là $%s$ thuộc nhóm $[8; 8,5)$ nên tứ phân vị thứ hai của mẫu số liệu là $Q_2 = 8 + \\frac{\\frac{%s}{2} - %s}{%s}(8,5 - 8) \\approx %s$ \\\\
    Tứ phân vị thứ nhất của dãy số liệu là $%s$ thuộc nhóm $[7,5; 8)$ nên tứ phân vị thứ nhất của mẫu số liệu là $Q_1 = 7,5 + \\frac{\\frac{%s}{4} - %s}{%s}(8 - 7,5) \\approx %s$ \\\\
    Tứ phân vị thứ ba của dãy số liệu là $%s$ thuộc nhóm $[8,5; 9)$ nên tứ phân vị thứ ba của mẫu số liệu là $Q_3 = 8,5 + \\frac{\\frac{3 \\cdot %s}{4} - %s}{%s}(9 - 8,5) \\approx %s$ \\\\
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = Q_3 - Q_1 \\approx %s - %s = %s$''' 
    % (N, N, N, cf[0], cf[0]+1, cf[1], cf[1]+1, cf[2], cf[2]+1, cf[3], cf[3]+1, cf[4], 
       q2_idx, N, cf_prev_q2, f_q2, fmt(Q2_val),
       q1_idx, N, cf_prev_q1, f_q1, fmt(Q1_val),
       q3_idx, N, cf_prev_q3, f_q3, fmt(Q3_val),
       fmt(Q3_val), fmt(Q1_val), Delta_Q_str))
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Đảm bảo có từ 1 đến 3 đáp án đúng
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

