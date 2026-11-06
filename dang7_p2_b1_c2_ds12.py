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


def bt_dang7_p2_b1_c2_ds12(self):
    # Hàm trợ giúp format số thập phân hoặc phân số
    def format_val(val):
        if val.denominator == 1:
            return str(val.numerator)
        return latex(val)

    # Random các tần số m1, m2, m3, m4, m5, m6
    m1 = random.randint(15, 25)
    m2 = random.randint(30, 45)
    m3 = random.randint(20, 35)
    m4 = random.randint(5, 12)
    m5 = random.randint(3, 8)
    m6 = random.randint(1, 3)

    n = m1 + m2 + m3 + m4 + m5 + m6

    # Tính toán các giá trị tích luỹ
    cf1 = m1
    cf2 = m1 + m2
    cf3 = m1 + m2 + m3
    cf4 = cf3 + m4
    cf5 = cf4 + m5
    cf6 = n

    # Tính Q1
    # Vị trí Q1 là n/4. Kiểm tra nhóm chứa Q1. Giả sử luôn rơi vào nhóm 2: [18; 21) để đơn giản hóa logic sinh đề, 
    # hoặc tính tổng quát. Với các giá trị random trên, n/4 thường khoảng 25, nên rơi vào nhóm 2.
    L_Q1 = 18
    h = 3
    Q1_val = Rational(L_Q1) + (Rational(n, 4) - Rational(cf1)) / Rational(m2) * Rational(h)
    Q1_fake = Q1_val + Rational(random.choice([-1, 1])*random.randint(1, 5), random.randint(2, 7))

    # Tính Q3
    # Vị trí Q3 là 3n/4. Thường khoảng 75, rơi vào nhóm 3: [21; 24)
    L_Q3 = 21
    Q3_val = Rational(L_Q3) + (Rational(3*n, 4) - Rational(cf2)) / Rational(m3) * Rational(h)

    # Tính Delta_Q
    Delta_Q_val = Q3_val - Q1_val
    Delta_Q_fake = Delta_Q_val + Rational(random.choice([-1, 1])*random.randint(1, 10), random.randint(10, 20))

    # Tính giá trị ngoại lệ trên: Q3 + 1.5 * Delta_Q
    outlier_threshold = Q3_val + Rational(3, 2) * Delta_Q_val

    # Nội dung câu hỏi
    noidungcauhoi = ('''Hằng ngày ông Thắng đều đi xe buýt từ nhà đến cơ quan. Dưới đây là bảng thống kê thời gian của %s lần ông Thắng đi xe buýt từ nhà đến cơ quan.
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|c|c|}
    \\hline
    Thời gian (phút) & $[15; 18)$ & $[18; 21)$ & $[21; 24)$ & $[24; 27)$ & $[27; 30)$ & $[30; 33)$ \\\\
    \\hline
    Số lượt & %s & %s & %s & %s & %s & %s \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (n, m1, m2, m3, m4, m5, m6))

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Cỡ mẫu $n = %s$.' % n
    nb_da_1_s = 'Cỡ mẫu $n = %s$.' % (n + random.randint(1, 10))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Cỡ mẫu $n = %s + %s + %s + %s + %s + %s = %s$.
    Gọi $x_1; x_2; \\dots; x_{%s}$ là mẫu số liệu gốc gồm thời gian %s lần đi xe buýt của ông Thắng.
    Ta có: $x_1, \\dots, x_{%s} \\in [15; 18)$; $x_{%s}, \\dots, x_{%s} \\in [18; 21)$; $x_{%s}, \\dots, x_{%s} \\in [21; 24)$; $x_{%s}, \\dots, x_{%s} \\in [24; 27)$; $x_{%s}, \\dots, x_{%s} \\in [27; 30)$; $x_{%s}, \\dots, x_{%s} \\in [30; 33)$.''' 
    % (m1, m2, m3, m4, m5, m6, n, n, n, cf1, cf1+1, cf2, cf2+1, cf3, cf3+1, cf4, cf4+1, cf5, cf5+1, cf6))
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là $Q_1 = %s$.' % format_val(Q1_val)
    th_da_1_s = 'Tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là $Q_1 = %s$.' % format_val(Q1_fake)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    # Vị trí Q1
    pos_Q1 = n / 4
    if pos_Q1.is_integer():
        q1_idx_str = f"\\frac{{1}}{{2}}(x_{{{int(pos_Q1)}}} + x_{{{int(pos_Q1)+1}}})"
    else:
        q1_idx_str = f"x_{{{int(pos_Q1) + 1}}}"

    loigiai_th_1 = ('''Tứ phân vị thứ nhất của mẫu số liệu gốc là $%s \\in [18; 21)$. Do đó, tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là $Q_1 = 18 + \\frac{\\frac{%s}{4} - %s}{%s}(21 - 18) = %s$.''' 
    % (q1_idx_str, n, cf1, m2, format_val(Q1_val)))
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu ghép nhóm là $\\Delta_Q = %s$' % format_val(Delta_Q_val)
    vd_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu ghép nhóm là $\\Delta_Q = %s$' % format_val(Delta_Q_fake)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    # Vị trí Q3
    pos_Q3 = 3 * n / 4
    if pos_Q3.is_integer():
        q3_idx_str = f"\\frac{{1}}{{2}}(x_{{{int(pos_Q3)}}} + x_{{{int(pos_Q3)+1}}})"
    else:
        q3_idx_str = f"x_{{{int(pos_Q3) + 1}}}"

    loigiai_vd_1 = ('''Tứ phân vị thứ ba của mẫu số liệu gốc là $%s \\in [21; 24)$. Do đó, tứ phân vị thứ ba của mẫu số liệu ghép nhóm là $Q_3 = 21 + \\frac{\\frac{3 \\cdot %s}{4} - %s}{%s}(24 - 21) = %s$. \\\\
    Vậy khoảng tứ phân vị của mẫu số liệu ghép nhóm là $\\Delta_Q = %s - %s = %s$.''' 
    % (q3_idx_str, n, cf2, m3, format_val(Q3_val), format_val(Q3_val), format_val(Q1_val), format_val(Delta_Q_val)))
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao ############################################
    # Kiểm tra xem outlier_threshold có nhỏ hơn 30 hay không để kết luận giá trị >29 có phải outlier không
    if outlier_threshold < 30:
        vdc_true_statement = "Biết rằng trong %s lần đi trên, chỉ có đúng một lần ông Thắng đi hết hơn 29 phút. Thời gian của lần đi đó là giá trị ngoại lệ của mẫu số liệu ghép nhóm." % n
        vdc_false_statement = "Biết rằng trong %s lần đi trên, chỉ có đúng một lần ông Thắng đi hết hơn 29 phút. Thời gian của lần đi đó không phải là giá trị ngoại lệ của mẫu số liệu ghép nhóm." % n
        loigiai_vdc_1 = ('''Trong lần duy nhất ông Thắng đi hết hơn 29 phút, thời gian đi của ông thuộc nhóm $[30; 33)$. Vì $Q_3 + 1,5\\Delta_Q = %s + 1,5 \\cdot %s = %s < 30$ nên thời gian của lần ông Thắng đi hết hơn 29 phút là giá trị ngoại lệ của mẫu số liệu ghép nhóm.''' 
        % (format_val(Q3_val), format_val(Delta_Q_val), format_val(outlier_threshold)))
    else:
        vdc_true_statement = "Biết rằng trong %s lần đi trên, chỉ có đúng một lần ông Thắng đi hết hơn 29 phút. Thời gian của lần đi đó không phải là giá trị ngoại lệ của mẫu số liệu ghép nhóm." % n
        vdc_false_statement = "Biết rằng trong %s lần đi trên, chỉ có đúng một lần ông Thắng đi hết hơn 29 phút. Thời gian của lần đi đó là giá trị ngoại lệ của mẫu số liệu ghép nhóm." % n
        loigiai_vdc_1 = ('''Trong lần duy nhất ông Thắng đi hết hơn 29 phút, thời gian đi của ông thuộc nhóm $[30; 33)$. Vì $Q_3 + 1,5\\Delta_Q = %s + 1,5 \\cdot %s = %s \\ge 30$ nên chưa đủ cơ sở để kết luận thời gian của lần đi này (có thể là 29.5) là giá trị ngoại lệ. Tuy nhiên, nếu thời gian đi $> %s$ thì mới chắc chắn là ngoại lệ.''' 
        % (format_val(Q3_val), format_val(Delta_Q_val), format_val(outlier_threshold), format_val(outlier_threshold)))

    vdc_da_1_d = '\\True ' + vdc_true_statement
    vdc_da_1_s = vdc_false_statement
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
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

