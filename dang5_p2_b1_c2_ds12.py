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


def bt_dang5_p2_b1_c2_ds12(self):
    # Hàm hỗ trợ định dạng số thập phân, tự động thay dấu chấm bằng dấu phẩy
    def fmt(val):
        s = f"{val:.3f}".rstrip('0').rstrip('.')
        if s == '': s = '0'
        return s.replace('.', ',')

    # Random các thông số cơ bản của mẫu số liệu
    a = random.choice([7.0, 8.0, 8.4, 9.0, 10.0])  # Giá trị khởi đầu
    h = random.choice([0.2, 0.4, 0.5])             # Độ dài mỗi nhóm
    a_vals = [round(a + i*h, 1) for i in range(6)]
    a_str = [fmt(x) for x in a_vals]

    # Random tần số các nhóm, khống chế để tổng N = 100 
    # và đảm bảo Q1 luôn rơi vào nhóm 3, Q3 luôn rơi vào nhóm 4
    m1 = random.randint(3, 7)
    m2 = random.randint(10, 15)
    m3 = random.randint(22, 28)
    m5 = random.randint(10, 16)
    m4 = 100 - (m1 + m2 + m3 + m5)
    N = 100

    # Tính tần số tích luỹ
    cf1 = m1
    cf2 = m1 + m2
    cf3 = cf2 + m3
    cf4 = cf3 + m4
    cf5 = 100

    # Khoảng biến thiên
    R = round(5 * h, 1)

    # Tính Q1, Q3 và Delta_Q (chính xác theo toán học)
    Q1 = a_vals[2] + ((25 - cf2) / m3) * h
    Q3 = a_vals[3] + ((75 - cf3) / m4) * h
    DeltaQ = Q3 - Q1

    # Tính khoảng ngoại lệ
    outlier_lower = Q1 - 1.5 * DeltaQ
    outlier_upper = Q3 + 1.5 * DeltaQ

    # Nội dung câu hỏi
    noidungcauhoi = (f'''Kết quả đo chiều cao của 100 cây keo 3 năm tuổi tại một nông trường được cho ở bảng sau:
    \\begin{{center}}
    \\begin{{tabular}}{{|c|c|c|c|c|c|}}
    \\hline
    Chiều cao (m) & $[{a_str[0]}; {a_str[1]})$ & $[{a_str[1]}; {a_str[2]})$ & $[{a_str[2]}; {a_str[3]})$ & $[{a_str[3]}; {a_str[4]})$ & $[{a_str[4]}; {a_str[5]})$ \\\\
    \\hline
    Số cây & {m1} & {m2} & {m3} & {m4} & {m5} \\\\
    \\hline
    \\end{{tabular}}
    \\end{{center}}''')

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = f'\\True Khoảng biến thiên của mẫu số liệu ghép nhóm: ${fmt(R)}$m'
    nb_da_1_s = f'Khoảng biến thiên của mẫu số liệu ghép nhóm: ${fmt(R + h)}$m'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = f'Khoảng biến thiên của mẫu số liệu ghép nhóm: ${fmt(a_vals[5])} - {fmt(a_vals[0])} = {fmt(R)}\\ (m)$'
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = f'\\True Tứ phân vị thứ ba của mẫu số liệu ghép nhóm là: $Q_3 = {fmt(Q3)}$'
    th_da_1_s = f'Tứ phân vị thứ ba của mẫu số liệu ghép nhóm là: $Q_3 = {fmt(Q3 + random.choice([0.5, 0.25, 0.1]))}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = (f'''Cỡ mẫu $n = 100$; \\\\
    Gọi $x_1; x_2; \\dots; x_{{100}}$ là mẫu số liệu gốc được xếp theo thứ tự không giảm. \\\\
    Ta có: $x_1; \\dots; x_{{{cf1}}} \\in [{a_str[0]}; {a_str[1]})$; $x_{{{cf1+1}}}; \\dots; x_{{{cf2}}} \\in [{a_str[1]}; {a_str[2]})$; $x_{{{cf2+1}}}; \\dots; x_{{{cf3}}} \\in [{a_str[2]}; {a_str[3]})$; $x_{{{cf3+1}}}; \\dots; x_{{{cf4}}} \\in [{a_str[3]}; {a_str[4]})$; $x_{{{cf4+1}}}; \\dots; x_{{{100}}} \\in [{a_str[4]}; {a_str[5]})$ \\\\
    Tứ phân vị thứ ba của mẫu số liệu gốc là $\\frac{{1}}{{2}}(x_{{75}} + x_{{76}}) \\in [{a_str[3]}; {a_str[4]})$. Do đó, tứ phân vị thứ ba của mẫu số liệu ghép nhóm là: $Q_3 = {fmt(a_vals[3])} + \\frac{{\\frac{{3 \\cdot 100}}{{4}} - ({m1}+{m2}+{m3})}}{{{m4}}}({fmt(a_vals[4])} - {fmt(a_vals[3])}) = {fmt(Q3)}$''')
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = f'\\True Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = {fmt(DeltaQ)}$'
    vd_da_1_s = f'Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = {fmt(DeltaQ + round(random.uniform(0.1, 0.5), 2))}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = (f'''Tứ phân vị thứ nhất của mẫu số liệu gốc là $\\frac{{1}}{{2}}(x_{{25}} + x_{{26}}) \\in [{a_str[2]}; {a_str[3]})$. Do đó, tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là: $Q_1 = {fmt(a_vals[2])} + \\frac{{\\frac{{100}}{{4}} - ({m1}+{m2})}}{{{m3}}}({fmt(a_vals[3])} - {fmt(a_vals[2])}) = {fmt(Q1)}$ \\\\
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = Q_3 - Q_1 = {fmt(Q3)} - {fmt(Q1)} = {fmt(DeltaQ)}$''')
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao ############################################
    target_val = a_vals[0]
    is_outlier = (target_val < outlier_lower) or (target_val > outlier_upper)
    if is_outlier:
        vdc_da_1_d = f'\\True Trong 100 cây keo trên có 1 cây cao {fmt(target_val)} m. Thì chiều cao của cây keo này là giá trị ngoại lệ'
        vdc_da_1_s = f'Trong 100 cây keo trên có 1 cây cao {fmt(target_val)} m. Thì chiều cao của cây keo này không phải là giá trị ngoại lệ'
        kl_text = f"Vậy cây cao {fmt(target_val)} m là giá trị ngoại lệ."
    else:
        vdc_da_1_d = f'\\True Trong 100 cây keo trên có 1 cây cao {fmt(target_val)} m. Thì chiều cao của cây keo này không phải là giá trị ngoại lệ'
        vdc_da_1_s = f'Trong 100 cây keo trên có 1 cây cao {fmt(target_val)} m. Thì chiều cao của cây keo này là giá trị ngoại lệ'
        kl_text = f"Vậy cây cao {fmt(target_val)} m không phải là giá trị ngoại lệ."

    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = (f'''Giá trị $x$ trong mẫu số liệu là giá trị ngoại lệ nếu $x > Q_3 + 1,5\\Delta_Q$ hoặc $x < Q_1 - 1,5\\Delta_Q$ \\\\
    Hay $x > {fmt(Q3)} + 1,5 \\cdot {fmt(DeltaQ)} = {fmt(outlier_upper)}$ hoặc $x < {fmt(Q1)} - 1,5 \\cdot {fmt(DeltaQ)} = {fmt(outlier_lower)}$ \\\\
    {kl_text}''')
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Vòng lặp đảm bảo có từ 1 đến 3 đáp án đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
            break

    shuffled_answers_nb = [nb_da_1]
    shuffled_solutions_nb = list_nb_2
    shuffled_answers_th = [th_da_1]
    shuffled_solutions_th = list_th_2
    shuffled_answers_vd = [vd_da_1]
    shuffled_solutions_vd = list_vd_2
    shuffled_answers_vdc = [vdc_da_1]
    shuffled_solutions_vdc = list_vdc_2

    # Xuất kết quả chuẩn theo format LaTeX
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
        '\\end{ex}\n\\end{minipage}\n\n')
    return content

