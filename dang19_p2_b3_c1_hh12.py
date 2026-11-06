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


def bt_dang19_p2_b3_c1_hh12(self):
    x_sym, y_sym = symbols('x y')
    while True:
        dx_base, dy_base = random.choice([(3,4), (4,3)])
        vt_AB_x = dx_base * random.choice([1, -1])
        vt_AB_y = dy_base * random.choice([1, -1])
        z_A = 5 * random.choice([1, -1])
        x_A = random.randint(-3, 3)
        y_A = random.randint(-3, 3)
        vt_AB_z = random.choice([-3, -2, 2, 3])
        x_B = x_A + vt_AB_x
        y_B = y_A + vt_AB_y
        z_B = z_A + vt_AB_z
        x_G, y_G, z_G = random.randint(-2, 2), random.randint(-2, 2), random.randint(-2, 2)
        x_C = 3*x_G - x_A - x_B
        y_C = 3*y_G - y_A - y_B
        z_C = 3*z_G - z_A - z_B
        sum_C = x_C + y_C + z_C
        k_val = random.choice([-2, -1, 2, 3])
        z_M = z_A + k_val * vt_AB_z
        x_M = x_A + k_val * vt_AB_x
        y_M = y_A + k_val * vt_AB_y
        sum_M = x_M + y_M
        x_N = Rational(x_A * z_A + vt_AB_x * vt_AB_z, z_A)
        y_N = Rational(y_A * z_A + vt_AB_y * vt_AB_z, z_A)
        sum_N = x_N + y_N
        if sum_N != sum_N + random.choice([1, 2]):
            break
    noidungcauhoi = ('''Trong không gian $Oxyz$, cho véctơ $\\overrightarrow{OA}=(%s;%s;%s)$ và điểm $B(%s;%s;%s)$.'''%(x_A, y_A, z_A, x_B, y_B, z_B))
    nb_da_1_d = '\\True Tọa độ của điểm $A$ là $(%s;%s;%s)$' %(x_A, y_A, z_A)
    nb_da_1_s = 'Tọa độ của điểm $A$ là $(%s;%s;%s)$' %(x_A, -y_A, z_A)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = ('''Ta có tọa độ của điểm $A$ là $(%s;%s;%s)$.'''%(x_A, y_A, z_A))
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_da_1_d = '\\True Gọi $C(a;b;c)$ thỏa mãn $\\Delta ABC$ nhận $G(%s;%s;%s)$ làm trọng tâm. Khi đó $a+b+c=%s$' %(x_G, y_G, z_G, sum_C)
    th_da_1_s = 'Gọi $C(a;b;c)$ thỏa mãn $\\Delta ABC$ nhận $G(%s;%s;%s)$ làm trọng tâm. Khi đó $a+b+c=%s$' %(x_G, y_G, z_G, sum_C + random.choice([1, -1, 2]))
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = ('''$G$ là trọng tâm $\\Delta ABC \\Leftrightarrow \\begin{cases} %s = \\frac{%s+%s+x_c}{3} \\\\ %s = \\frac{%s+%s+y_c}{3} \\\\ %s = \\frac{%s+%s+z_c}{3} \\end{cases} \\Leftrightarrow \\begin{cases} x_c = %s \\\\ y_c = %s \\\\ z_c = %s \\end{cases} \\Rightarrow C(%s;%s;%s)$.\\\\ Suy ra $a+b+c = %s$.'''%(x_G, x_A, x_B, y_G, y_A, y_B, z_G, z_A, z_B, x_C, y_C, z_C, x_C, y_C, z_C, sum_C))
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_da_1_d = '\\True Nếu $A,B,M(x;y;%s)$ thẳng hàng thì tổng $x+y=%s$' %(z_M, sum_M)
    vd_da_1_s = 'Nếu $A,B,M(x;y;%s)$ thẳng hàng thì tổng $x+y=%s$' %(z_M, sum_M + random.choice([-2, -1, 1, 2]))
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = ('''Ta có $\\overrightarrow{AB}=(%s;%s;%s)$, $\\overrightarrow{AM}=(x-(%s);y-(%s);%s)$.\\\\ Ba điểm $A,B,M$ thẳng hàng khi và chỉ khi $\\overrightarrow{AM} = k\\overrightarrow{AB} \\Leftrightarrow \\begin{cases} x-(%s) = k \\cdot (%s) \\\\ y-(%s) = k \\cdot (%s) \\\\ %s = k \\cdot (%s) \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\\\ k = %s \\end{cases}$.\\\\ Suy ra $x+y=%s$.'''%(vt_AB_x, vt_AB_y, vt_AB_z, x_A, y_A, z_M - z_A, x_A, vt_AB_x, y_A, vt_AB_y, z_M - z_A, vt_AB_z, x_M, y_M, k_val, sum_M))
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vdc_da_1_d = '\\True Cho $N \\in (Oxy)$ để $\\Delta ABN$ vuông cân tại $A$. Tổng hoành độ và tung độ của điểm $N$ bằng $%s$' %(latex(sum_N))
    vdc_da_1_s = 'Cho $N \\in (Oxy)$ để $\\Delta ABN$ vuông cân tại $A$. Tổng hoành độ và tung độ của điểm $N$ bằng $%s$' %(latex(sum_N + random.choice([frac(1,5), frac(2,5), 1])))
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    m_val = Rational(-vt_AB_x, vt_AB_y)
    rhs_val = vt_AB_x * x_A + vt_AB_y * y_A + z_A * vt_AB_z
    n_val = Rational(rhs_val, vt_AB_y)
    y_expr_str = latex(m_val * x_sym + n_val)
    n_prime = n_val - y_A
    A_eq = 1 + m_val**2
    B_eq = 2 * m_val * n_prime - 2 * x_A
    C_eq = x_A**2 + n_prime**2 - vt_AB_z**2
    AB_sq = vt_AB_x**2 + vt_AB_y**2 + vt_AB_z**2
    y_sub_str = latex(m_val * x_sym + n_prime)
    quad_eq_str = latex(A_eq * x_sym**2 + B_eq * x_sym + C_eq)
    eq1_lhs_str = latex(vt_AB_x * x_sym + vt_AB_y * y_sym)
    loigiai_vdc_1 = ('''Ta có $N \\in (Oxy) \\Rightarrow N(x;y;0)$ suy ra $\\overrightarrow{AN}=(x-(%s);y-(%s);%s)$, $\\overrightarrow{AB}=(%s;%s;%s)$.\\\\ Ta có $\\Delta ABN$ vuông cân tại $A \\Leftrightarrow \\begin{cases} \\overrightarrow{AN} \\perp \\overrightarrow{AB} \\; (1) \\\\ AN = AB \\; (2) \\end{cases}$.\\\\ $(1) \\Leftrightarrow \\overrightarrow{AN} \\perp \\overrightarrow{AB} \\Leftrightarrow %s(x-(%s)) + %s(y-(%s)) + (%s)(%s) = 0 \\Leftrightarrow %s = %s \\Leftrightarrow y = %s$.\\\\ $(2) \\Leftrightarrow AN^2 = AB^2 \\Leftrightarrow (x-(%s))^2 + (y-(%s))^2 + %s = %s$.\\\\ $\\Leftrightarrow (x-(%s))^2 + \\left(%s\\right)^2 = %s \\Leftrightarrow %s = 0 \\Leftrightarrow x = %s$.\\\\ Suy ra $y = %s \\Rightarrow N\\left(%s; %s; 0\\right)$. Vậy $x_N + y_N = %s$.'''%(x_A, y_A, -z_A, vt_AB_x, vt_AB_y, vt_AB_z, vt_AB_x, x_A, vt_AB_y, y_A, -z_A, vt_AB_z, eq1_lhs_str, rhs_val, y_expr_str, x_A, y_A, z_A**2, AB_sq, x_A, y_sub_str, vt_AB_z**2, quad_eq_str, latex(x_N), latex(y_N), latex(x_N), latex(y_N), latex(sum_N)))
    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
            break
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
    content = ('\\begin{minipage}{\\textwidth} \n''\\begin{ex}\n'+str(noidungcauhoi)+ '\n''\\choiceTFn \n''{'+str(shuffled_answers_nb[0])+'}\n''{'+str(shuffled_answers_th[0])+'}\n''{'+str(shuffled_answers_vd[0])+'}\n''{'+str(shuffled_answers_vdc[0])+'}\n''\\loigiai{ \n''\\begin{enumEX}[a)]{1} \n''\\item '+str(shuffled_solutions_nb[0])+'\n''\\item '+str(shuffled_solutions_th[0])+'\n''\\item '+str(shuffled_solutions_vd[0])+'\n''\\item '+str(shuffled_solutions_vdc[0])+'\n''\\end{enumEX}} \n''\\end{ex}\n \\end{minipage}\n\n').replace('+ -', '-')
    return content

