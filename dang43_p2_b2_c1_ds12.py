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


def bt_dang43_p2_b2_c1_ds12(self):
    # Khai báo biến
    x = symbols('x')

    # Random các tham số sao cho nghiệm và kết quả lợi nhuận lớn nhất ra số đẹp
    while True:
        b = random.randint(2, 5)
        c = random.choice([80000, 90000, 100000, 110000, 120000])
        d = random.randint(3, 6)
        P = random.randint(30, 40)
        R_add = random.choice([80000, 90000, 100000])

        # B = Hệ số của x trong hàm lợi nhuận L(x)
        B = P - d + b
        # C_L = Hệ số tự do trong hàm lợi nhuận L(x)
        C_L = R_add - c

        # Đảm bảo lợi nhuận lớn nhất là số nguyên (chia hết cho 4 sau khi quy đổi)
        if B % 2 == 0 and (250000 * B**2 + 1000 * C_L) > 0:
            break

    # Tính toán các biểu thức
    coeff_x = d - b
    if coeff_x > 0:
        str_coeff_x = "+ %sx" % coeff_x
        str_coeff_x_loigiai = "+ %s" % coeff_x
    elif coeff_x < 0:
        str_coeff_x = "- %sx" % (-coeff_x)
        str_coeff_x_loigiai = "- %s" % (-coeff_x)
    else:
        str_coeff_x = ""
        str_coeff_x_loigiai = ""

    f_coeff_x = coeff_x + random.choice([-2, -1, 1, 2])
    if f_coeff_x == 0:
        f_coeff_x = 1
    if f_coeff_x > 0:
        f_str_coeff_x = "+ %sx" % f_coeff_x
    else:
        f_str_coeff_x = "- %sx" % (-f_coeff_x)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Một tạp chí được bán với giá $%s$ nghìn đồng một cuốn. Chi phí xuất bản $x$ cuốn tạp chí (bao gồm: Lương cán bộ, công nhân viên, giấy in, ...) được cho bởi công thức $C(x) = 0,001x^2 - %sx + %s$ được tính theo đơn vị nghìn đồng. Chi phí phát hành cho mỗi cuốn là $%s$ nghìn đồng.'''
                     % (P, b, c, d))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Tổng chi phí $T(x)$ (xuất bản và phát hành) cho $x$ cuốn tạp chí là $T(x) = 0,001x^2 %s + %s$ (nghìn đồng)' % (str_coeff_x, c)
    nb_da_1_s = 'Tổng chi phí $T(x)$ (xuất bản và phát hành) cho $x$ cuốn tạp chí là $T(x) = 0,001x^2 %s + %s$ (nghìn đồng)' % (f_str_coeff_x, c)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Tổng chi phí xuất bản và phát hành $x$ cuốn tạp chí là:\\\\
    $T(x) = C(x) + %sx = (0,001x^2 - %sx + %s) + %sx = 0,001x^2 %s + %s$ (nghìn đồng).'''
                    % (d, b, c, d, str_coeff_x, c))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ######################################################################## Thông hiểu ############################################
    # Tính toán cho câu b
    M_val = 10 + coeff_x + int(c / 10000)
    M_vnd = M_val * 1000
    M_vnd_false = M_vnd + random.choice([-2000, 2000, 4000])

    # Các đáp án
    th_da_1_d = '\\True Tỉ số $M(x) = \\frac{T(x)}{x}$ được gọi là chi phí trung bình cho một cuốn tạp chí khi xuất bản $x$ cuốn. Chi phí trung bình cho một cuốn tạp chí khi xuất bản $10000$ cuốn là $%s$ đồng' % (M_vnd)
    th_da_1_s = 'Tỉ số $M(x) = \\frac{T(x)}{x}$ được gọi là chi phí trung bình cho một cuốn tạp chí khi xuất bản $x$ cuốn. Chi phí trung bình cho một cuốn tạp chí khi xuất bản $10000$ cuốn là $%s$ đồng' % (M_vnd_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Ta có $M(x) = \\frac{T(x)}{x} = \\frac{0,001x^2 %s + %s}{x} = 0,001x %s + \\frac{%s}{x}$.\\\\
    Khi $x=10000$, ta có $M(10000) = 0,001 \\cdot 10000 %s + \\frac{%s}{10000} = 10 %s + %s = %s$ (nghìn đồng) = $%s$ đồng.'''
                    % (str_coeff_x, c, str_coeff_x_loigiai, c, str_coeff_x_loigiai, c, str_coeff_x_loigiai, int(c/10000), M_val, M_vnd))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################
    # Tính toán cho câu c
    R_add_trieu = int(R_add / 1000)
    sqrt_delta_prime = math.sqrt(250000 * B**2 + 1000 * C_L)
    x1 = 500 * B - sqrt_delta_prime
    x2 = 500 * B + sqrt_delta_prime

    lower_true = math.floor(x1) + 1
    upper_true = math.ceil(x2) - 1

    lower_false = lower_true - random.choice([10, 20])
    upper_false = upper_true + random.choice([50, 100])

    if C_L > 0:
        str_C_L = "+ %s" % C_L
    elif C_L < 0:
        str_C_L = "- %s" % (-C_L)
    else:
        str_C_L = ""

    # Các đáp án
    vd_da_1_d = '\\True Biết rằng các khoản thu bao gồm tiền bán tạp chí và $%s$ triệu nhận được từ quảng cáo và sự trợ giúp cho báo chí. Giả sử số cuốn in ra đều được bán hết. Khi đó nhà máy nên in từ $%s$ đến $%s$ cuốn thì có lãi' % (R_add_trieu, lower_true, upper_true)
    vd_da_1_s = 'Biết rằng các khoản thu bao gồm tiền bán tạp chí và $%s$ triệu nhận được từ quảng cáo và sự trợ giúp cho báo chí. Giả sử số cuốn in ra đều được bán hết. Khi đó nhà máy nên in từ $%s$ đến $%s$ cuốn thì có lãi' % (R_add_trieu, lower_false, upper_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Doanh thu khi bán $x$ cuốn tạp chí và nhận tài trợ là: $R(x) = %sx + %s$ (nghìn đồng).\\\\
    Lợi nhuận nhà máy thu được là $L(x) = R(x) - T(x) = %sx + %s - (0,001x^2 %s + %s) = -0,001x^2 + %sx %s$.\\\\
    Để nhà máy có lãi thì $L(x) > 0 \\Leftrightarrow -0,001x^2 + %sx %s > 0 \\Leftrightarrow %s < x < %s$.\\\\
    Vì $x$ là số nguyên, do đó nhà máy nên in từ $%s$ đến $%s$ cuốn thì có lãi.'''
                    % (P, R_add, P, R_add, str_coeff_x, c, B, str_C_L, B, str_C_L, round(x1, 2), round(x2, 2), lower_true, upper_true))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################
    # Tính toán cho câu d
    L_max = 250 * B**2 + C_L
    L_max_trieu = int(L_max / 1000)
    L_max_false = L_max_trieu + random.choice([5, 10, 20])
    x_max = 500 * B

    # Các đáp án
    vdc_da_1_d = '\\True Số tiền lãi lớn nhất mà nhà máy xuất bản và bán hết $x$ cuốn tạp chí có thể đạt được là $%s$ triệu đồng' % (L_max_trieu)
    vdc_da_1_s = 'Số tiền lãi lớn nhất mà nhà máy xuất bản và bán hết $x$ cuốn tạp chí có thể đạt được là $%s$ triệu đồng' % (L_max_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Xét hàm số biểu diễn lợi nhuận $L(x) = -0,001x^2 + %sx %s$.\\\\
    Đây là một parabol có bề lõm quay xuống dưới, hàm số đạt giá trị lớn nhất tại đỉnh $x = \\frac{-%s}{2 \\cdot (-0,001)} = %s$.\\\\
    Khi đó lợi nhuận lớn nhất là $L(%s) = -0,001 \\cdot (%s)^2 + %s \\cdot (%s) %s = %s$ (nghìn đồng) = $%s$ triệu đồng.'''
                     % (B, str_C_L, B, x_max, x_max, x_max, B, x_max, str_C_L, L_max, L_max_trieu))

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
        '\\begin{ex}\n' +
    str(noidungcauhoi) + 
        '\n\\choiceTFn \n'
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
        '\\end{ex}\n\\end{minipage}\n\n')
    return content

