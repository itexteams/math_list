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


def bt_dang23_p2_b2_c1_hh10(self):
    # Khai báo biến và random số liệu
    a = random.randint(3, 8)
    b = random.randint(4, 9)
    while a == b:
        b = random.randint(4, 9)

    angles = [30, 45, 60, 120]
    C_deg = random.choice(angles)
    C_rad = sp.pi * sp.Rational(C_deg, 180)

    # Tính toán các đại lượng chính xác bằng sympy
    cos_C = sp.cos(C_rad)
    c_sq = sp.simplify(a**2 + b**2 - 2 * a * b * cos_C)
    c_exact = sp.simplify(sp.sqrt(c_sq))

    chuvi = sp.simplify(a + b + c_exact)
    chuvi_false = sp.simplify(a + b + c_exact + random.choice([-2, -1, 1, 2]))

    # Tính góc A xấp xỉ - SỬA LỖI CHIA SYMPY Ở ĐÂY
    cos_A_expr = (b**2 + c_sq - a**2) / (2 * b * c_exact)
    cos_A_val = float(cos_A_expr.evalf()) 

    if cos_A_val > 1: cos_A_val = 1
    if cos_A_val < -1: cos_A_val = -1
    A_deg = round(math.degrees(math.acos(cos_A_val)))

    # Tính đường phân giác l_c
    l_c_exact = sp.simplify(2 * a * b * sp.cos(C_rad / 2) / (a + b))
    l_c_false = sp.simplify(l_c_exact * sp.Rational(1, 2))

    # Nội dung câu hỏi
    noidungcauhoi = '''Cho tam giác $ABC$ có $a = %s, \\widehat{C} = %s^\\circ, b = %s$.''' % (a, C_deg, b)

    # ####################################################################### Nhận biết ############################################
    nb_da_1_d = '\\True Độ dài cạnh $AB$ được tính bằng công thức $c^2 = a^2 + b^2 - 2ab \\cos \\widehat{C}$.'
    nb_da_1_s = 'Độ dài cạnh $AB$ được tính bằng công thức $c^2 = a^2 + b^2 + 2ab \\cos \\widehat{C}$.'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = '''Theo định lý côsin trong tam giác, độ dài cạnh $AB$ (tức là cạnh $c$) bình phương bằng $c^2 = a^2 + b^2 - 2ab \\cos \\widehat{C}$.'''
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    # ####################################################################### Thông hiểu ############################################
    th_da_1_d = '\\True Chu vi tam giác $ABC$ bằng $%s$.' % (sp.latex(chuvi))  
    th_da_1_s = 'Chu vi tam giác $ABC$ bằng $%s$.' % (sp.latex(chuvi_false))   
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = ('''Áp dụng định lý côsin, ta có: $c^2 = a^2 + b^2 - 2ab \\cos \\widehat{C} = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ = %s$. \\\\
    Suy ra $c = %s$. \\\\
    Chu vi tam giác $ABC$ là $P = a + b + c = %s + %s + %s = %s$.'''       
    % (a, b, a, b, C_deg, sp.latex(c_sq), sp.latex(c_exact), a, b, sp.latex(c_exact), sp.latex(chuvi)))
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    # ####################################################################### Vận dụng ############################################
    vd_da_1_d = '\\True Góc $\\widehat{BAC}$ xấp xỉ bằng $%s^\\circ$.' % (A_deg)  
    vd_da_1_s = 'Góc $\\widehat{BAC}$ xấp xỉ bằng $%s^\\circ$.' % (A_deg + random.choice([-5, -2, 2, 5]))  
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = ('''Áp dụng hệ quả của định lý côsin, ta có: \\\\
    $\\cos A = \\frac{b^2 + c^2 - a^2}{2bc} = \\frac{%s^2 + (%s)^2 - %s^2}{2 \\cdot %s \\cdot %s} \\approx %s$. \\\\
    Suy ra $\\widehat{BAC} \\approx %s^\\circ$.'''  
    % (b, sp.latex(c_exact), a, b, sp.latex(c_exact), round(cos_A_val, 4), A_deg))
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    # ####################################################################### Vận dụng cao ############################################
    vdc_da_1_d = '\\True Độ dài đường phân giác trong góc $C$ của tam giác $ABC$ bằng $%s$.' % (sp.latex(l_c_exact)) 
    vdc_da_1_s = 'Độ dài đường phân giác trong góc $C$ của tam giác $ABC$ bằng $%s$.' % (sp.latex(l_c_false)) 
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = ('''Gọi $l_c$ là độ dài đường phân giác trong góc $C$. Ta có công thức: \\\\
    $l_c = \\frac{2ab \\cos \\frac{C}{2}}{a + b} = \\frac{2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ}{%s + %s} = %s$.'''
    % (a, b, C_deg // 2, a, b, sp.latex(l_c_exact)))
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
        str(noidungcauhoi) + '\n' +
        '\\choiceTFn \n' +
        '{' + str(shuffled_answers_nb[0]) + '}\n' +
        '{' + str(shuffled_answers_th[0]) + '}\n' +
        '{' + str(shuffled_answers_vd[0]) + '}\n' +
        '{' + str(shuffled_answers_vdc[0]) + '}\n' +
        '\\loigiai{ \n' +
        '\\begin{enumEX}[a)]{1} \n' +
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
        '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
        '\\end{enumEX}} \n' +
        '\\end{ex}\n\\end{minipage} \n\n') 
    return content

