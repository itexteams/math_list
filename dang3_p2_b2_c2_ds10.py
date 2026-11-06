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


def bt_dang3_p2_b2_c2_ds10(self):
    # Khai báo biến ký hiệu
    x, y = symbols('x y')

    # ------------------------------------------------------------------------
    # HÀM BỔ TRỢ XỬ LÝ TEXT: Định dạng thay số tránh lỗi "+ -" hoặc "- -"
    # ------------------------------------------------------------------------
    def fmt_subst(a_coef, x_val, b_coef, y_val):
        def wrap(val):
            return f"({val})" if val < 0 else str(val)

        str_a = f"({a_coef})" if a_coef < 0 else str(a_coef)
        part1 = f"{str_a} \\cdot {wrap(x_val)}"

        if b_coef < 0:
            part2 = f"- {-b_coef} \\cdot {wrap(y_val)}"
        else:
            part2 = f"+ {b_coef} \\cdot {wrap(y_val)}"

        return f"{part1} {part2}"

    # ------------------------------------------------------------------------
    # TẠO ĐỀ BÀI NGẪU NHIÊN (ĐẢM BẢO KHÔNG BAO GIỜ TREO)
    # ------------------------------------------------------------------------
    # Hai đường thẳng cắt nhau: a*e != b*d
    while True:
        a = random.choice([-3, -2, -1, 1, 2, 3])
        b = random.choice([-3, -2, -1, 1, 2, 3])
        d = random.choice([-3, -2, -1, 1, 2, 3])
        e = random.choice([-3, -2, -1, 1, 2, 3])
        if a * e != b * d:
            break

    # Chọn trước một nghiệm nguyên (x0, y0)
    x0, y0 = random.randint(-3, 3), random.randint(-3, 3)
    val1_0 = a * x0 + b * y0
    val2_0 = d * x0 + e * y0

    # Sinh c < val1_0 và f > val2_0 để chắc chắn (x0, y0) là nghiệm của hệ (tránh treo vòng lặp)
    c = val1_0 - random.randint(1, 4)
    f = val2_0 + random.randint(1, 4)

    eq1 = a * x + b * y
    eq2 = d * x + e * y

    # Nội dung câu hỏi
    noidungcauhoi = (f'''Cho hệ bất phương trình $(I) \\begin{{cases}} {latex(eq1)} > {c} \\\\ {latex(eq2)} < {f} \\end{{cases}}$. Xét tính đúng sai của các mệnh đề sau:''')

    ######################################## Nhận biết ########################################
    # Các đáp án và lời giải tương ứng
    nb_da_1_d = '\\True Hệ $(I)$ có nghiệm'
    nb_lg_1_d = (f'''Thay cặp số $({x0}; {y0})$ vào hệ $(I)$ ta được: '''
                 f'''$\\begin{{cases}} {fmt_subst(a, x0, b, y0)} = {val1_0} > {c} \\\\ {fmt_subst(d, x0, e, y0)} = {val2_0} < {f} \\end{{cases}}$ (thỏa mãn). '''
                 f'''Do đó hệ $(I)$ có nghiệm.''')

    nb_da_1_s = 'Hệ $(I)$ vô nghiệm'
    nb_lg_1_s = (f'''Mệnh đề sai vì hệ $(I)$ có nghiệm, ví dụ cặp số $({x0}; {y0})$ thỏa mãn hệ: '''
                 f'''$\\begin{{cases}} {fmt_subst(a, x0, b, y0)} = {val1_0} > {c} \\\\ {fmt_subst(d, x0, e, y0)} = {val2_0} < {f} \\end{{cases}}$.''')

    list_nb_choices = [(nb_da_1_d, nb_lg_1_d), (nb_da_1_s, nb_lg_1_s)]

    ######################################## Thông hiểu ########################################
    # Kiểm tra một điểm P ngẫu nhiên
    xp, yp = random.randint(-4, 4), random.randint(-4, 4)
    val1_p = a * xp + b * yp
    val2_p = d * xp + e * yp
    is_p_solution = (val1_p > c) and (val2_p < f)

    if is_p_solution:
        th_da_1_d = f'\\True Cặp số $({xp}; {yp})$ là nghiệm của hệ $(I)$'
        th_lg_1_d = (f'''Thay cặp số $({xp}; {yp})$ vào hệ $(I)$ ta được '''
                     f'''$\\begin{{cases}} {fmt_subst(a, xp, b, yp)} = {val1_p} > {c} \\text{{ (đúng)}} \\\\ {fmt_subst(d, xp, e, yp)} = {val2_p} < {f} \\text{{ (đúng)}} \\end{{cases}}$ '''
                     f'''nên cặp số $({xp}; {yp})$ là nghiệm của hệ $(I)$.''')

        th_da_1_s = f'Cặp số $({xp}; {yp})$ không là nghiệm của hệ $(I)$'
        th_lg_1_s = th_lg_1_d + ' Do đó mệnh đề trên là sai.'
    else:
        th_da_1_d = f'\\True Cặp số $({xp}; {yp})$ không là nghiệm của hệ $(I)$'
        sai_lydo_p = f"{fmt_subst(a, xp, b, yp)} = {val1_p} > {c}" if not (val1_p > c) else f"{fmt_subst(d, xp, e, yp)} = {val2_p} < {f}"
        th_lg_1_d = f'''Vì thay $({xp}; {yp})$ vào hệ ta có ${sai_lydo_p}$ (sai) nên cặp số $({xp}; {yp})$ không là nghiệm của hệ $(I)$.'''

        th_da_1_s = f'Cặp số $({xp}; {yp})$ là nghiệm của hệ $(I)$'
        th_lg_1_s = th_lg_1_d + ' Do đó mệnh đề trên là sai.'

    list_th_choices = [(th_da_1_d, th_lg_1_d), (th_da_1_s, th_lg_1_s)]

    ######################################## Vận dụng ########################################
    # Kiểm tra điểm K ngẫu nhiên khác O
    xk, yk = random.choice([-3, -2, -1, 1, 2, 3]), random.choice([-3, -2, -1, 1, 2, 3])
    val1_k = a * xk + b * yk
    val2_k = d * xk + e * yk
    is_k_solution = (val1_k > c) and (val2_k < f)

    if is_k_solution:
        vd_da_1_d = f'\\True Miền nghiệm của hệ $(I)$ chứa điểm $K({xk}; {yk})$'
        vd_lg_1_d = (f'''Thay tọa độ điểm $K({xk}; {yk})$ vào hệ $(I)$ ta được '''
                     f'''$\\begin{{cases}} {fmt_subst(a, xk, b, yk)} = {val1_k} > {c} \\text{{ (đúng)}} \\\\ {fmt_subst(d, xk, e, yk)} = {val2_k} < {f} \\text{{ (đúng)}} \\end{{cases}}$ '''
                     f'''nên miền nghiệm của hệ $(I)$ chứa điểm $K({xk}; {yk})$.''')

        vd_da_1_s = f'Miền nghiệm của hệ $(I)$ không chứa điểm $K({xk}; {yk})$'
        vd_lg_1_s = vd_lg_1_d + ' Do đó mệnh đề trên là sai.'
    else:
        vd_da_1_d = f'\\True Miền nghiệm của hệ $(I)$ không chứa điểm $K({xk}; {yk})$'
        sai_lydo_k = f"{fmt_subst(a, xk, b, yk)} = {val1_k} > {c}" if not (val1_k > c) else f"{fmt_subst(d, xk, e, yk)} = {val2_k} < {f}"
        vd_lg_1_d = f'''Vì thay tọa độ điểm $K$ vào hệ ta có ${sai_lydo_k}$ (sai) nên miền nghiệm của hệ $(I)$ không chứa điểm $K({xk}; {yk})$.'''

        vd_da_1_s = f'Miền nghiệm của hệ $(I)$ chứa điểm $K({xk}; {yk})$'
        vd_lg_1_s = vd_lg_1_d + ' Do đó mệnh đề trên là sai.'

    list_vd_choices = [(vd_da_1_d, vd_lg_1_d), (vd_da_1_s, vd_lg_1_s)]

    ######################################## Vận dụng cao ########################################
    # Kiểm tra gốc tọa độ O(0; 0)
    is_o_solution = (0 > c) and (0 < f)

    if is_o_solution:
        vdc_da_1_d = '\\True Miền nghiệm của hệ $(I)$ chứa gốc tọa độ $O$'
        vdc_lg_1_d = f'''Vì thay tọa độ $(0; 0)$ vào hệ ta được $0 > {c}$ (đúng) và $0 < {f}$ (đúng) nên miền nghiệm của hệ $(I)$ chứa gốc tọa độ $O$.'''

        vdc_da_1_s = 'Miền nghiệm của hệ $(I)$ không chứa gốc tọa độ $O$'
        vdc_lg_1_s = vdc_lg_1_d + ' Do đó mệnh đề trên là sai.'
    else:
        vdc_da_1_d = '\\True Miền nghiệm của hệ $(I)$ không chứa gốc tọa độ $O$'
        sai_lydo_o = f"0 > {c}" if not (0 > c) else f"0 < {f}"
        vdc_lg_1_d = f'''Vì thay tọa độ $(0; 0)$ vào hệ ta có ${sai_lydo_o}$ (sai) nên miền nghiệm của hệ $(I)$ không chứa gốc tọa độ $O$.'''

        vdc_da_1_s = 'Miền nghiệm của hệ $(I)$ chứa gốc tọa độ $O$'
        vdc_lg_1_s = vdc_lg_1_d + ' Do đó mệnh đề trên là sai.'

    list_vdc_choices = [(vdc_da_1_d, vdc_lg_1_d), (vdc_da_1_s, vdc_lg_1_s)]

    # ------------------------------------------------------------------------
    # ĐẢM BẢO SỐ LƯỢNG MỆNH ĐỀ ĐÚNG TỪ 1 ĐẾN 3
    # ------------------------------------------------------------------------
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        sel_nb = random.choice(list_nb_choices)
        sel_th = random.choice(list_th_choices)
        sel_vd = random.choice(list_vd_choices)
        sel_vdc = random.choice(list_vdc_choices)

        answers = [sel_nb[0], sel_th[0], sel_vd[0], sel_vdc[0]]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào danh sách theo đúng mẫu cấu trúc
    list_nb_1 = [sel_nb[0]]
    list_nb_2 = [sel_nb[1]]

    list_th_1 = [sel_th[0]]
    list_th_2 = [sel_th[1]]

    list_vd_1 = [sel_vd[0]]
    list_vd_2 = [sel_vd[1]]

    list_vdc_1 = [sel_vdc[0]]
    list_vdc_2 = [sel_vdc[1]]

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

    # Xuất câu hỏi với đáp án và lời giải
    content = (
        '\\begin{minipage}{\\textwidth}\n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n'
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

