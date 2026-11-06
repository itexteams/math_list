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


def bt_dang12_p2_b1_c1_hh10(self):
    # Khai báo biến
    # Để tan^2 x + b tan x + c = (tan x - 1)(tan x + m) với m > 0 (tức c = -m < 0):
    m = random.choice([2, 3, 4, 5])
    c = -m
    b = m - 1  # Khi đó: tan^2 x + b*tan x + c = (tan x - 1)(tan x + m)

    # Định dạng chuỗi hiển thị cho b
    if b == 1:
        b_str = "+"
    elif b == -1:
        b_str = "-"
    elif b > 0:
        b_str = f"+ {b}"
    else:
        b_str = f"- {-b}"

    # Định dạng chuỗi hiển thị cho c
    if c > 0:
        c_str = f"+ {c}"
    else:
        c_str = f"- {-c}"

    cos_val = random.choice([Rational(1, 2), Rational(1, 3), Rational(2, 3)])

    if cos_val == Rational(1, 2):
        cos_str = "\\frac{1}{2}"
        cos_sq = Rational(1, 4)
        sin_sq = Rational(3, 4)
    elif cos_val == Rational(1, 3):
        cos_str = "\\frac{1}{3}"
        cos_sq = Rational(1, 9)
        sin_sq = Rational(8, 9)
    else:
        cos_str = "\\frac{2}{3}"
        cos_sq = Rational(4, 9)
        sin_sq = Rational(5, 9)

    tan_sq = sin_sq / cos_sq
    val_P_sq = (tan_sq + 2 * m * sp.sqrt(tan_sq) + m**2) / (1 + tan_sq)**2

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho biểu thức $P = \\frac{\\sin^2 x %s \\sin x \\cos x %s \\cos^2 x}{\\tan x - 1}$.'''
                     % (b_str, c_str))

    ########################################################################
    # Nhận biết ############################################
    nb_da_1_d = '\\True $\\frac{1}{\\cos^2 x} = \\tan^2 x + 1$'
    nb_da_1_s = '$\\frac{1}{\\cos^2 x} = \\cot^2 x + 1$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Theo hệ thức lượng cơ bản, ta có $\\frac{1}{\\cos^2 x} = \\frac{\\sin^2 x + \\cos^2 x}{\\cos^2 x} = \\tan^2 x + 1$.''')
    list_nb_2 = [loigiai_nb_1]

    ########################################################################
    # Thông hiểu ############################################
    th_da_1_d = '\\True Biểu thức $A = \\sin^2 x %s \\sin x \\cos x %s \\cos^2 x$ được viết lại $A = \\frac{\\tan^2 x %s \\tan x %s}{1 + \\tan^2 x}$' % (b_str, c_str, b_str, c_str)
    th_da_1_s = 'Biểu thức $A = \\sin^2 x %s \\sin x \\cos x %s \\cos^2 x$ được viết lại $A = \\frac{\\tan^2 x %s \\tan x %s}{1 + \\cot^2 x}$' % (b_str, c_str, b_str, c_str)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    # Đã sửa lỗi thừa số 1 ở cuối ngoặc: %s 1 -> %s
    loigiai_th_1 = ('''Ta có $A = \\cos^2 x \\left( \\frac{\\sin^2 x}{\\cos^2 x} %s \\frac{\\sin x \\cos x}{\\cos^2 x} %s \\right) \\\\
    = \\frac{1}{1 + \\tan^2 x} (\\tan^2 x %s \\tan x %s) = \\frac{\\tan^2 x %s \\tan x %s}{1 + \\tan^2 x}$.'''
               % (b_str, c_str, b_str, c_str, b_str, c_str))
    list_th_2 = [loigiai_th_1]

    ######################################################################## 
    # Vận dụng ############################################
    vd_da_1_d = '\\True Rút gọn biểu thức $P$ ta được $P = \\frac{\\tan x + %s}{1 + \\tan^2 x}$' % (m)
    vd_da_1_s = 'Rút gọn biểu thức $P$ ta được $P = \\frac{\\tan x - %s}{1 + \\tan^2 x}$' % (m)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Ta có $P = \\frac{\\tan^2 x %s \\tan x %s}{(1 + \\tan^2 x)(\\tan x - 1)} = \\frac{(\\tan x - 1)(\\tan x + %s)}{(1 + \\tan^2 x)(\\tan x - 1)} = \\frac{\\tan x + %s}{1 + \\tan^2 x}$.'''
               % (b_str, c_str, m, m))
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## 
    # Vận dụng cao ############################################
    vdc_da_1_d = '\\True Giá trị của biểu thức $P^2$ bằng $%s$ khi $\\cos x = %s$' % (latex(val_P_sq), cos_str)
    vdc_da_1_s = 'Giá trị của biểu thức $P^2$ bằng $%s$ khi $\\cos x = %s$' % (latex(val_P_sq + Rational(1, 2)), cos_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Khi $\\cos x = %s \\Rightarrow \\cos^2 x = %s \\Rightarrow \\sin^2 x = 1 - %s = %s$. \\\\
    Suy ra $\\tan^2 x = \\frac{\\sin^2 x}{\\cos^2 x} = %s$. \\\\
    Ta có $P^2 = \\frac{(\\tan x + %s)^2}{(1 + \\tan^2 x)^2} = \\frac{\\tan^2 x + 2 \\cdot %s \\tan x + %s}{(1 + \\tan^2 x)^2}$. \\\\
    Thế số: $P^2 = \\frac{%s + 2 \\cdot %s \\cdot \\sqrt{%s} + %s}{(1 + %s)^2} = %s$.'''
               % (cos_str, latex(cos_sq), latex(cos_sq), latex(sin_sq), latex(tan_sq), m, m, m**2, latex(tan_sq), m, latex(tan_sq), m**2, latex(tan_sq), latex(val_P_sq)))
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
        str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
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
        '\\end{ex}\n \\end{minipage}\n\n')
    return content

