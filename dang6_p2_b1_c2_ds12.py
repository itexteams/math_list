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


def bt_dang6_p2_b1_c2_ds12(self):
    def format_val(val):
        if val.denominator == 1:
            return str(val.numerator)
        return latex(val)

    # Random cỡ mẫu chung N (ví dụ 100)
    N = 100

    # Random số liệu khu vực A
    a1 = random.randint(5, 15)
    a2 = random.randint(20, 30)
    a3 = random.randint(25, 35)
    a5 = random.randint(5, 10)
    a4 = N - (a1 + a2 + a3 + a5)

    # Random số liệu khu vực B
    b1 = random.randint(40, 50)
    b2 = random.randint(35, 45)
    b3 = random.randint(5, 15)
    b5 = 0
    b4 = N - (b1 + b2 + b3 + b5)

    # Tích lũy A
    cfa1 = a1
    cfa2 = a1 + a2
    cfa3 = cfa2 + a3
    cfa4 = cfa3 + a4
    cfa5 = N

    # Tích lũy B
    cfb1 = b1
    cfb2 = b1 + b2
    cfb3 = cfb2 + b3
    cfb4 = cfb3 + b4
    cfb5 = N

    # Khoảng biến thiên
    R_A = 34 - 19
    R_B = 31 - 19 # Nhóm cuối cùng có dữ liệu là [28;31) vì b5 = 0

    # Tính Q1, Q3 cho A
    h = 3
    pos_q1 = Rational(N, 4)
    pos_q3 = Rational(3*N, 4)

    # Tính Q1_A (thường nằm ở nhóm 2: [22;25))
    L_Q1A = 22
    Q1A_val = Rational(L_Q1A) + (pos_q1 - Rational(cfa1)) / Rational(a2) * Rational(h)

    # Tính Q3_A (thường nằm ở nhóm 4: [28;31))
    L_Q3A = 28
    Q3A_val = Rational(L_Q3A) + (pos_q3 - Rational(cfa3)) / Rational(a4) * Rational(h)

    Delta_QA = Q3A_val - Q1A_val
    Delta_QA_fake = Delta_QA + Rational(random.choice([-1, 1])*random.randint(1, 5), random.randint(2, 5))

    # Tính Q1, Q3 cho B
    # Q1_B (thường nằm ở nhóm 1: [19;22))
    L_Q1B = 19
    Q1B_val = Rational(L_Q1B) + (pos_q1 - 0) / Rational(b1) * Rational(h)

    # Q3_B (thường nằm ở nhóm 2: [22;25))
    L_Q3B = 22
    Q3B_val = Rational(L_Q3B) + (pos_q3 - Rational(cfb1)) / Rational(b2) * Rational(h)

    Delta_QB = Q3B_val - Q1B_val


    noidungcauhoi = ('''Giả sử kết quả khảo sát hai khu vực $A$ và $B$ về độ tuổi kết hôn của một số phụ nữ vừa lập gia đình được cho ở bảng sau:
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|c|}
    \\hline
    Tuổi kết hôn & $[19; 22)$ & $[22; 25)$ & $[25; 28)$ & $[28; 31)$ & $[31; 34)$ \\\\
    \\hline
    Số phụ nữ khu vực $A$ & %s & %s & %s & %s & %s \\\\
    \\hline
    Số phụ nữ khu vực $B$ & %s & %s & %s & %s & %s \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (a1, a2, a3, a4, a5, b1, b2, b3, b4, b5))

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Khoảng biến thiên của mẫu số liệu ghép nhóm ứng với khu vực A là: $%s$ (tuổi)' % R_A
    nb_da_1_s = 'Khoảng biến thiên của mẫu số liệu ghép nhóm ứng với khu vực A là: $%s$ (tuổi)' % (R_A + random.randint(1, 3))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Khoảng biến thiên của mẫu số liệu ghép nhóm ứng với khu vực A là: $34 - 19 = %s$ (tuổi)''' % R_A)
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Khoảng biến thiên của mẫu số liệu ghép nhóm ứng với khu vực B là: $%s$ (tuổi)' % R_B
    th_da_1_s = 'Khoảng biến thiên của mẫu số liệu ghép nhóm ứng với khu vực B là: $%s$ (tuổi)' % (R_B + random.randint(1, 3))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Khoảng biến thiên của mẫu số liệu ghép nhóm ứng với khu vực B là: $31 - 19 = %s$ (tuổi)''' % R_B)
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu ghép nhóm ứng với khu vực A là: $%s$ (tuổi)' % format_val(Delta_QA)
    vd_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu ghép nhóm ứng với khu vực A là: $%s$ (tuổi)' % format_val(Delta_QA_fake)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    # Format vị trí Q1, Q3 cho A
    pos_Q1_val = N / 4
    if pos_Q1_val.is_integer():
        q1_idx_A = f"\\frac{{1}}{{2}}(x_{{{int(pos_Q1_val)}}} + x_{{{int(pos_Q1_val)+1}}})"
    else:
        q1_idx_A = f"x_{{{int(pos_Q1_val) + 1}}}"

    pos_Q3_val = 3 * N / 4
    if pos_Q3_val.is_integer():
        q3_idx_A = f"\\frac{{1}}{{2}}(x_{{{int(pos_Q3_val)}}} + x_{{{int(pos_Q3_val)+1}}})"
    else:
        q3_idx_A = f"x_{{{int(pos_Q3_val) + 1}}}"

    loigiai_vd_1 = ('''Cỡ mẫu $n = %s$ \\\\
    Gọi $x_1; x_2; \\dots; x_{%s}$ là mẫu số liệu gốc về độ tuổi kết hôn của phụ nữ ở khu vực A được xếp theo thứ tự không giảm. \\\\
    Ta có: $x_1, \\dots, x_{%s} \\in [19; 22)$; $x_{%s}, \\dots, x_{%s} \\in [22; 25)$; $x_{%s}, \\dots, x_{%s} \\in [25; 28)$; $x_{%s}, \\dots, x_{%s} \\in [28; 31)$; $x_{%s}, \\dots, x_{%s} \\in [31; 34)$. \\\\
    Tứ phân vị thứ nhất của mẫu số liệu gốc là $%s \\in [22; 25)$. Do đó, tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là: $Q_1 = 22 + \\frac{\\frac{%s}{4} - %s}{%s}(25 - 22) = %s$ \\\\
    Tứ phân vị thứ ba của mẫu số liệu gốc là $%s \\in [28; 31)$. Do đó, tứ phân vị thứ ba của mẫu số liệu ghép nhóm là: $Q_3 = 28 + \\frac{\\frac{3 \\cdot %s}{4} - %s}{%s}(31 - 28) = %s$ \\\\
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = Q_3 - Q_1 = %s$''' 
    % (N, N, cfa1, cfa1+1, cfa2, cfa2+1, cfa3, cfa3+1, cfa4, cfa4+1, N, q1_idx_A, N, cfa1, a2, format_val(Q1A_val), q3_idx_A, N, cfa3, a4, format_val(Q3A_val), format_val(Delta_QA)))
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao ############################################
    if Delta_QB < Delta_QA:
        vdc_true_statement = "Nếu so sánh theo khoảng tứ phân vị thì phụ nữ ở khu vực B có độ tuổi kết hôn đồng đều hơn"
        vdc_false_statement = "Nếu so sánh theo khoảng tứ phân vị thì phụ nữ ở khu vực A có độ tuổi kết hôn đồng đều hơn"
        loigiai_vdc_1_ketluan = "Có $\\Delta_Q' < \\Delta_Q$ nên phụ nữ ở khu vực B có độ tuổi kết hôn đồng đều hơn."
    else:
        vdc_true_statement = "Nếu so sánh theo khoảng tứ phân vị thì phụ nữ ở khu vực A có độ tuổi kết hôn đồng đều hơn"
        vdc_false_statement = "Nếu so sánh theo khoảng tứ phân vị thì phụ nữ ở khu vực B có độ tuổi kết hôn đồng đều hơn"
        loigiai_vdc_1_ketluan = "Có $\\Delta_Q < \\Delta_Q'$ nên phụ nữ ở khu vực A có độ tuổi kết hôn đồng đều hơn."

    vdc_da_1_d = '\\True ' + vdc_true_statement
    vdc_da_1_s = vdc_false_statement
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]


    if pos_Q1_val.is_integer():
        q1_idx_B = f"\\frac{{1}}{{2}}(y_{{{int(pos_Q1_val)}}} + y_{{{int(pos_Q1_val)+1}}})"
    else:
        q1_idx_B = f"y_{{{int(pos_Q1_val) + 1}}}"

    if pos_Q3_val.is_integer():
        q3_idx_B = f"\\frac{{1}}{{2}}(y_{{{int(pos_Q3_val)}}} + y_{{{int(pos_Q3_val)+1}}})"
    else:
        q3_idx_B = f"y_{{{int(pos_Q3_val) + 1}}}"

    loigiai_vdc_1 = ('''Gọi $y_1; y_2; \\dots; y_{%s}$ là mẫu số liệu gốc về độ tuổi kết hôn của phụ nữ ở khu vực B được xếp theo thứ tự không giảm. \\\\
    Ta có: $y_1, \\dots, y_{%s} \\in [19; 22)$; $y_{%s}, \\dots, y_{%s} \\in [22; 25)$; $y_{%s}, \\dots, y_{%s} \\in [25; 28)$; $y_{%s}, \\dots, y_{%s} \\in [28; 31)$. \\\\
    Tứ phân vị thứ nhất của mẫu số liệu gốc là $%s \\in [19; 22)$. Do đó, tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là: $Q_1' = 19 + \\frac{\\frac{%s}{4} - 0}{%s}(22 - 19) = %s$ \\\\
    Tứ phân vị thứ ba của mẫu số liệu gốc là $%s \\in [22; 25)$. Do đó, tứ phân vị thứ ba của mẫu số liệu ghép nhóm là: $Q_3' = 22 + \\frac{\\frac{3 \\cdot %s}{4} - %s}{%s}(25 - 22) = %s$ \\\\
    Ta có $\\Delta_Q' = Q_3' - Q_1' = %s$. %s''' 
    % (N, cfb1, cfb1+1, cfb2, cfb2+1, cfb3, cfb3+1, cfb4, q1_idx_B, N, b1, format_val(Q1B_val), q3_idx_B, N, cfb1, b2, format_val(Q3B_val), format_val(Delta_QB), loigiai_vdc_1_ketluan))
    list_vdc_2 = [loigiai_vdc_1]


    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da = random.choice(list_nb_da_1)
        th_da = random.choice(list_th_da_1)
        vd_da = random.choice(list_vd_da_1)
        vdc_da = random.choice(list_vdc_da_1)
        answers = [nb_da, th_da, vd_da, vdc_da]
        if 1 <= count_true_answers(answers) <= 3:
            break

    shuffled_answers_nb = [nb_da]
    shuffled_solutions_nb = list_nb_2
    shuffled_answers_th = [th_da]
    shuffled_solutions_th = list_th_2
    shuffled_answers_vd = [vd_da]
    shuffled_solutions_vd = list_vd_2
    shuffled_answers_vdc = [vdc_da]
    shuffled_solutions_vdc = list_vdc_2

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

