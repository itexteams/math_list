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


def bt_dang4_p2_b1_c2_ds12(self):
    # Hàm hỗ trợ chuyển đổi phân số sang định dạng LaTeX
    def to_latex(val):
        if isinstance(val, frac):
            if val.denominator == 1:
                return str(val.numerator)
            else:
                return f"\\frac{{{val.numerator}}}{{{val.denominator}}}"
        return str(val)

    # Random mốc thời gian bắt đầu (ví dụ: 10, 15, hoặc 20)
    m = random.choice([10, 15, 20])
    h = 5 # Độ rộng lớp

    # Các khoảng thời gian
    edges = [m, m+h, m+2*h, m+3*h, m+4*h, m+5*h]
    khoang_str = [f"[{edges[i]}; {edges[i+1]})" for i in range(5)]

    # Tên ngẫu nhiên
    name1 = "Bác " + random.choice(["Bình", "Hùng", "Sơn", "Minh"])
    name2 = "Bác " + random.choice(["An", "Cường", "Dũng", "Tuấn"])

    # Tạo tần số ngẫu nhiên cho người 1 (Dữ liệu phân tán, giống Bác Bình)
    # Đảm bảo khoảng đầu và cuối luôn > 0 để khoảng biến thiên = 25
    f1_1 = random.randint(2, 6)
    f1_5 = random.randint(1, 4)
    rem1 = 30 - f1_1 - f1_5
    f1_2 = random.randint(8, 14)
    f1_3 = random.randint(5, rem1 - f1_2 - 1)
    f1_4 = rem1 - f1_2 - f1_3
    f1 = [f1_1, f1_2, f1_3, f1_4, f1_5]

    # Tạo tần số ngẫu nhiên cho người 2 (Dữ liệu tập trung, giống Bác An)
    # Thường khoảng đầu và cuối bằng 0
    f2_1 = 0
    f2_5 = 0
    f2_2 = random.randint(18, 25)
    f2_3 = random.randint(3, 30 - f2_2 - 1)
    f2_4 = 30 - f2_2 - f2_3
    f2 = [f2_1, f2_2, f2_3, f2_4, f2_5]

    # Hàm tính toán Tứ phân vị (Đã sửa lỗi)
    def get_quartile(freqs, edges, p):
        N = 30
        # Thêm int() để chuyển tử số (vd: 75.0) thành số nguyên (75) 
        # để hàm frac() không bị lỗi
        pos_val = frac(int(N * p * 10), 10) 

        cf = 0
        for i in range(5):
            cf_next = cf + freqs[i]
            if pos_val <= cf_next:
                L = edges[i]
                f = freqs[i]
                # Công thức Q = L + (pos - cf) / f * h
                Q = L + frac(pos_val - cf, 1) / f * h
                return Q, i, cf
            cf = cf_next
        return 0, 0, 0

    # Tính toán các giá trị
    # Mức độ Nhận biết: Khoảng biến thiên Người 1
    # Vì f1_1 > 0 và f1_5 > 0 nên min thuộc [m; m+5), max thuộc [m+20; m+25)
    range_1 = edges[5] - edges[0] 

    # Mức độ Thông hiểu: Khoảng tứ phân vị của Người 2
    Q1_2, idx1_2, cf1_2 = get_quartile(f2, edges, 0.25)
    Q3_2, idx3_2, cf3_2 = get_quartile(f2, edges, 0.75)
    IQR2 = Q3_2 - Q1_2

    # Mức độ Vận dụng: Tứ phân vị thứ 3 của Người 1
    Q1_1, idx1_1, cf1_1 = get_quartile(f1, edges, 0.25)
    Q3_1, idx3_1, cf3_1 = get_quartile(f1, edges, 0.75)
    IQR1 = Q3_1 - Q1_1

    # Mức độ Vận dụng cao: So sánh IQR
    is_1_greater = IQR1 > IQR2

    # Nội dung câu hỏi
    noidungcauhoi = (f'''Biểu đồ thống kê thời gian tập thể dục buổi sáng mỗi ngày trong tháng của {name1} và {name2} được cho bởi bảng số liệu sau:
    \\begin{{center}}
    \\begin{{tabular}}{{|c|c|c|c|c|c|}}
    \\hline
    Thời gian (phút) & ${khoang_str[0]}$ & ${khoang_str[1]}$ & ${khoang_str[2]}$ & ${khoang_str[3]}$ & ${khoang_str[4]}$ \\\\
    \\hline
    {name1} & {f1[0]} & {f1[1]} & {f1[2]} & {f1[3]} & {f1[4]} \\\\
    \\hline
    {name2} & {f2[0]} & {f2[1]} & {f2[2]} & {f2[3]} & {f2[4]} \\\\
    \\hline
    \\end{{tabular}}
    \\end{{center}}''')

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = f'\\True Khoảng biến thiên của mẫu số liệu ghép nhóm về thời gian tập thể dục của {name1} là {range_1} (phút)'
    nb_da_1_s = f'Khoảng biến thiên của mẫu số liệu ghép nhóm về thời gian tập thể dục của {name1} là {range_1 - 5} (phút)'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = f'Khoảng biến thiên của mẫu số liệu ghép nhóm của {name1} là: $R = {edges[5]} - {edges[0]} = {range_1}$.'
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = f'\\True Khoảng tứ phân vị của mẫu số liệu ghép nhóm của {name2} là: $\\Delta_Q = {to_latex(IQR2)}$'
    th_da_1_s = f'Khoảng tứ phân vị của mẫu số liệu ghép nhóm của {name2} là: $\\Delta_Q = {to_latex(IQR2 + frac(1,2))}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = (f'''Cỡ mẫu $n = 30$. Tứ phân vị thứ nhất của {name2} thuộc nhóm ${khoang_str[idx1_2]}$. \\\\
    $Q_1 = {edges[idx1_2]} + \\frac{{7,5 - {cf1_2}}}{{{f2[idx1_2]}}}.5 = {to_latex(Q1_2)}$. \\\\
    Tứ phân vị thứ ba của {name2} thuộc nhóm ${khoang_str[idx3_2]}$. \\\\
    $Q_3 = {edges[idx3_2]} + \\frac{{22,5 - {cf3_2}}}{{{f2[idx3_2]}}}.5 = {to_latex(Q3_2)}$. \\\\
    Khoảng tứ phân vị của {name2} là: $\\Delta_Q = {to_latex(Q3_2)} - {to_latex(Q1_2)} = {to_latex(IQR2)}$.''')
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = f'\\True Tứ phân vị thứ ba của mẫu số liệu ghép nhóm của {name1} là: $Q_3\' = {to_latex(Q3_1)}$'
    vd_da_1_s = f'Tứ phân vị thứ ba của mẫu số liệu ghép nhóm của {name1} là: $Q_3\' = {to_latex(Q3_1 + frac(3,4))}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = (f'''Cỡ mẫu $n = 30$. Tứ phân vị thứ ba của {name1} thuộc nhóm ${khoang_str[idx3_1]}$. \\\\
    Do đó, tứ phân vị thứ ba của mẫu số liệu ghép nhóm là: $Q_3\' = {edges[idx3_1]} + \\frac{{22,5 - {cf3_1}}}{{{f1[idx3_1]}}}.5 = {to_latex(Q3_1)}$.''')
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao ############################################
    if is_1_greater:
        vdc_da_1_d = f'\\True Khoảng tứ phân vị về thời gian tập thể dục mỗi ngày của {name1} lớn hơn {name2}'
        vdc_da_1_s = f'Khoảng tứ phân vị về thời gian tập thể dục mỗi ngày của {name2} lớn hơn {name1}'
    else:
        vdc_da_1_d = f'\\True Khoảng tứ phân vị về thời gian tập thể dục mỗi ngày của {name2} lớn hơn {name1}'
        vdc_da_1_s = f'Khoảng tứ phân vị về thời gian tập thể dục mỗi ngày của {name1} lớn hơn {name2}'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = (f'''Tứ phân vị thứ nhất của {name1} thuộc nhóm ${khoang_str[idx1_1]}$. \\\\
    $Q_1\' = {edges[idx1_1]} + \\frac{{7,5 - {cf1_1}}}{{{f1[idx1_1]}}}.5 = {to_latex(Q1_1)}$. \\\\
    Khoảng tứ phân vị của {name1} là: $\\Delta_Q\' = {to_latex(Q3_1)} - {to_latex(Q1_1)} = {to_latex(IQR1)}$. \\\\
    Vì ${to_latex(IQR1)} {">" if is_1_greater else "<"} {to_latex(IQR2)}$ nên khoảng tứ phân vị của {name1 if is_1_greater else name2} lớn hơn.''')
    list_vdc_2 = [loigiai_vdc_1]

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

    # Đóng gói và xáo trộn
    list_nb_1 = [nb_da_1]; combined_nb = list(zip(list_nb_1, list_nb_2)); random.shuffle(combined_nb); shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    list_th_1 = [th_da_1]; combined_th = list(zip(list_th_1, list_th_2)); random.shuffle(combined_th); shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    list_vd_1 = [vd_da_1]; combined_vd = list(zip(list_vd_1, list_vd_2)); random.shuffle(combined_vd); shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    list_vdc_1 = [vdc_da_1]; combined_vdc = list(zip(list_vdc_1, list_vdc_2)); random.shuffle(combined_vdc); shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Format chữ Đúng/Sai cho lời giải
    def prefix_solution(answer, solution):
        if '\\True' in answer:
            return 'Đúng. ' + solution
        return 'Sai. ' + solution

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth}\n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n'
        '\\choiceTFn\n'
        '{' + str(shuffled_answers_nb[0]) + '}\n'
        '{' + str(shuffled_answers_th[0]) + '}\n'
        '{' + str(shuffled_answers_vd[0]) + '}\n'
        '{' + str(shuffled_answers_vdc[0]) + '}\n'
        '\\loigiai{\n'
        '\\begin{enumEX}[a)]{1}\n'
        '\\item ' + prefix_solution(shuffled_answers_nb[0], shuffled_solutions_nb[0]) + '\n'
        '\\item ' + prefix_solution(shuffled_answers_th[0], shuffled_solutions_th[0]) + '\n'
        '\\item ' + prefix_solution(shuffled_answers_vd[0], shuffled_solutions_vd[0]) + '\n'
        '\\item ' + prefix_solution(shuffled_answers_vdc[0], shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}}\n'
        '\\end{ex}\n'
        '\\end{minipage}\n\n')
    return content

