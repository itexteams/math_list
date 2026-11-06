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


def bt_dang46_p2_b2_c1_ds12(self):
    # Khai báo biến
    t = symbols('t')        
    while True:
        M_val = random.choice([80, 100, 120, 150, 160, 200]) # Số lượng tối đa M
        # Chọn A là một số nguyên dương > 1
        m_base = random.choice([2, 3, 4, 5])
        A_val = m_base**2 # để ln(A) = 2*ln(m_base)
        k_num, k_den = 1, 2 # k = 0,5
        k_val_str = '0,5'
        k_val_sym = Rational(1, 2)

        break

    # Biểu thức N(t)
    # Viết công thức hiển thị dạng LaTeX: N(t) = \frac{M}{1 + A e^{-0,5t}}
    M_half = M_val // 2
    v_max_val = Rational(M_val, 8) # k*M/4 = (1/2)*M/4 = M/8
    if v_max_val.q == 1:
        v_max_str = str(v_max_val.p)
    else:
        v_max_float = float(v_max_val)
        v_max_str = str(v_max_float).replace('.', ',')

    t_crit_coef = 2 # hệ số trước ln(A_val)
    t_crit_expr_A = '%s\\ln %s' % (t_crit_coef, A_val) # ví dụ: 2\ln 9
    t_crit_expr_base = '%s\\ln %s' % (2 * t_crit_coef, m_base) # ví dụ: 4\ln 3
    t_wrong_expr = '%s\\ln %s' % (t_crit_coef, m_base) # ví dụ: 2\ln 3 (như câu a trong đề gốc)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Một phòng thí nghiệm sinh học nghiên cứu sự phát triển của một quần thể vi khuẩn trong môi trường nuôi cấy đặc biệt. Số lượng vi khuẩn (tính bằng triệu con) sau thời gian $t$ (giờ) ($t \\ge 0$) được mô phỏng bởi công thức $N(t) = \\frac{%s}{1 + %s \\mathrm{e}^{-%st}}$. Tốc độ sinh trưởng của quần thể vi khuẩn tại thời điểm $t$ được xác định bởi đạo hàm $N'(t)$.''' % (M_val, A_val, k_val_str))

    #############################################################################
    # Ý a: Nhận biết / Thông hiểu về thời điểm đạt tốc độ sinh trưởng lớn nhất
    # Mệnh đề gốc: "Tại thời điểm t = 2 ln 3 (giờ), tốc độ sinh trưởng của quần thể vi khuẩn đạt giá trị lớn nhất." -> SAI (giá trị đúng là 4 ln 3 hoặc 2 ln 9)
    nb_da_1_d = '\\True Tại thời điểm $t = %s$ (giờ), tốc độ sinh trưởng của quần thể vi khuẩn đạt giá trị lớn nhất' % (t_crit_expr_A)
    nb_da_1_s = 'Tại thời điểm $t = %s$ (giờ), tốc độ sinh trưởng của quần thể vi khuẩn đạt giá trị lớn nhất' % (t_wrong_expr)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Ta có $N'(t) = \\frac{%s \\cdot %s \\mathrm{e}^{-%st}}{(1 + %s \\mathrm{e}^{-%st})^2} = \\frac{%s \\mathrm{e}^{-%st}}{(1 + %s \\mathrm{e}^{-%st})^2}$. \\\\ Đặt $u = \\mathrm{e}^{-%st}$ ($u > 0$). Xét hàm số $f(u) = \\frac{u}{(1 + %s u)^2}$. \\\\ Ta có $f'(u) = \\frac{1 - %s u}{(1 + %s u)^3} = 0 \\Leftrightarrow u = \\frac{1}{%s}$. \\\\ Khi đó $\\mathrm{e}^{-%st} = \\frac{1}{%s} \\Leftrightarrow %st = \\ln %s \\Leftrightarrow t = %s$ (giờ). \\\\ Vậy tốc độ sinh trưởng đạt cực đại tại thời điểm $t = %s$ (hay $t = %s$).''' % (
        M_val, k_val_str, k_val_str, A_val, k_val_str,
        str(float(M_val * Rational(1, 2))).replace('.0', '').replace('.', ','), k_val_str, A_val, k_val_str,
        k_val_str, A_val, A_val, A_val, A_val,
        k_val_str, A_val, k_val_str, A_val, t_crit_expr_A,
        t_crit_expr_A, t_crit_expr_base
    ))
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    #############################################################################
    # Ý b: Thời gian để số lượng vi khuẩn vượt ngưỡng M/2 triệu con
    # N(t) > M/2 <=> 1 + A*e^(-0.5t) < 2 <=> e^(-0.5t) < 1/A <=> 0.5t > ln(A) <=> t > 2*ln(A)
    # Mệnh đề gốc: "Kể từ thời điểm ban đầu, cần nhiều hơn 2 ln 9 giờ để số lượng vi khuẩn đạt trên 50 triệu con." -> ĐÚNG
    th_da_1_d = '\\True Kể từ thời điểm ban đầu, cần nhiều hơn $%s$ giờ để số lượng vi khuẩn đạt trên $%s$ triệu con' % (t_crit_expr_A, M_half)
    th_da_1_s = 'Kể từ thời điểm ban đầu, cần nhiều hơn $%s$ giờ để số lượng vi khuẩn đạt trên $%s$ triệu con' % (t_wrong_expr, M_half)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Số lượng vi khuẩn đạt trên $%s$ triệu con khi và chỉ khi: \\\\ $N(t) > %s \\Leftrightarrow \\frac{%s}{1 + %s \\mathrm{e}^{-%st}} > %s \\Leftrightarrow 1 + %s \\mathrm{e}^{-%st} < 2 \\Leftrightarrow \\mathrm{e}^{-%st} < \\frac{1}{%s} \\Leftrightarrow %st > \\ln %s \\Leftrightarrow t > %s$. \\\\ Do đó, cần nhiều hơn $%s$ giờ để số lượng vi khuẩn vượt quá $%s$ triệu con.''' % (
        M_half, M_half, M_val, A_val, k_val_str, M_half, A_val, k_val_str, k_val_str, A_val, k_val_str, A_val, t_crit_expr_A, t_crit_expr_A, M_half
    ))
    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    #############################################################################
    # Ý c: Giới hạn số lượng vi khuẩn tối đa lâu dài (lim khi t -> +oo)
    # Mệnh đề gốc: "Số lượng vi khuẩn tối đa mà môi trường nuôi cấy này có thể duy trì lâu dài không vượt quá 100 triệu con." -> ĐÚNG (vì lim N(t) = 100 và N(t) < 100 với mọi t)
    vd_da_1_d = '\\True Số lượng vi khuẩn tối đa mà môi trường nuôi cấy này có thể duy trì lâu dài không vượt quá $%s$ triệu con' % (M_val)
    vd_da_1_s = 'Số lượng vi khuẩn tối đa mà môi trường nuôi cấy này có thể duy trì lâu dài có thể vượt quá $%s$ triệu con' % (M_val)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Vì $t \\ge 0$ nên $\\mathrm{e}^{-%st} > 0$, suy ra $1 + %s \\mathrm{e}^{-%st} > 1$, dẫn đến $N(t) = \\frac{%s}{1 + %s \\mathrm{e}^{-%st}} < %s$. \\\\ Mặt khác, $\\lim_{t \\to +\\infty} N(t) = \\lim_{t \\to +\\infty} \\frac{%s}{1 + %s \\mathrm{e}^{-%st}} = \\frac{%s}{1 + 0} = %s$. \\\\ Do đó, số lượng vi khuẩn tối đa mà môi trường nuôi cấy có thể duy trì lâu dài không vượt quá $%s$ triệu con.''' % (
        k_val_str, A_val, k_val_str, M_val, A_val, k_val_str, M_val,
        M_val, A_val, k_val_str, M_val, M_val, M_val
    ))
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    #############################################################################
    # Ý d: Tốc độ sinh trưởng lớn nhất
    # N'(t)_max = k * M / 4 = 0.5 * M / 4 = M / 8
    # Mệnh đề gốc: "Tốc độ sinh trưởng lớn nhất của quần thể vi khuẩn trong quá trình nuôi cấy là 12,5 triệu con/giờ." -> ĐÚNG (với M = 100)
    wrong_v_max_str = str(float(v_max_val * 2)).replace('.0', '').replace('.', ',')
    vdc_da_1_d = '\\True Tốc độ sinh trưởng lớn nhất của quần thể vi khuẩn trong quá trình nuôi cấy là $%s$ triệu con/giờ' % (v_max_str)
    vdc_da_1_s = 'Tốc độ sinh trưởng lớn nhất của quần thể vi khuẩn trong quá trình nuôi cấy là $%s$ triệu con/giờ' % (wrong_v_max_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Tốc độ sinh trưởng đạt cực đại khi $u = \\frac{1}{%s}$ (tức $t = %s$). \\\\ Khi đó: \\\\ $N'(t)_{\\max} = \\frac{%s \\cdot \\frac{1}{%s}}{(1 + %s \\cdot \\frac{1}{%s})^2} = \\frac{%s}{2^2} = %s$ (triệu con/giờ).''' % (
        A_val, t_crit_expr_A,
        str(float(M_val * Rational(1, 2))).replace('.0', '').replace('.', ','), A_val, A_val, A_val,
        str(float(Rational(M_val, 2))).replace('.0', '').replace('.', ','), v_max_str
    ))
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

    # Gán lại vào danh sách
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

    # Xuất câu hỏi với đáp án và lời giải đã được định dạng
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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
        '\\end{ex}\n'
        '\\end{minipage}\n\n')
    return content

