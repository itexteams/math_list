
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


def bt_dang13_p2_b4_c2_hh10(self):
    def fmt_sqrt3(coef):
        if coef == 0:
            return '0'
        if coef == 1:
            return '\\sqrt{3}'
        if coef == -1:
            return '-\\sqrt{3}'
        return f'{coef}\\sqrt{{3}}'
    def fmt_pt(x_coef, y_val):
        if x_coef == 0:
            return f'(0;{y_val})'
        return f'\\left({fmt_sqrt3(x_coef)};{y_val}\\right)'
    k = random.choice([2, 3, 4, 5, 6])
    c = random.choice([-2, -1, 0, 0, 1, 2])
    yB = random.choice([-4, -3, -2, -1, 1, 2, 3, 4, 5])
    s = random.choice([-1, 1])
    yA = yB + s * k
    yC = yB
    xB_coef = c
    xA_coef = c + k
    xC_coef = c + 2 * k
    dy = yB - yA
    dy_sq = f'({dy})^2' if dy < 0 else f'{dy}^2'
    side = 2 * k
    s_coef = k * k
    pt_A = fmt_pt(xA_coef, yA)
    pt_B = fmt_pt(xB_coef, yB)
    pt_C = fmt_pt(xC_coef, yC)
    noidungcauhoi = f'Trong mặt phẳng tọa độ $Oxy$, cho $\\triangle ABC$ với $A{pt_A}$, $B{pt_B}$, $C{pt_C}$. Xét tính đúng sai của các khẳng định sau:\n'
    wrong_ac = random.choice([side + 2, side - 2, k, side + 4])
    nb_da_1_d = f'\\True $AC={side}$'
    nb_da_1_s = f'$AC={wrong_ac}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_v = random.choice(['B', 'C'])
    th_da_1_d = '\\True Tam giác $ABC$ cân tại $A$'
    th_da_1_s = f'Tam giác $ABC$ cân tại ${wrong_v}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_s = random.choice([f'{2 * s_coef}\\sqrt{{3}}', f'{s_coef + 2}\\sqrt{{3}}', f'{s_coef - 2}\\sqrt{{3}}', f'{s_coef}'])
    vd_da_1_d = f'\\True $S_{{\\triangle ABC}}={s_coef}\\sqrt{{3}}$'
    vd_da_1_s = f'$S_{{\\triangle ABC}}={wrong_s}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_ang = random.choice([45, 60, 120])
    vdc_da_1_d = '\\True $\\widehat{ABC}=30^\\circ$'
    vdc_da_1_s = f'$\\widehat{{ABC}}={wrong_ang}^\\circ$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
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
    tt_nb = 'Đúng' if '\\True' in nb_da_1 else 'Sai'
    tt_th = 'Đúng' if '\\True' in th_da_1 else 'Sai'
    tt_vd = 'Đúng' if '\\True' in vd_da_1 else 'Sai'
    tt_vdc = 'Đúng' if '\\True' in vdc_da_1 else 'Sai'
    loigiai_nb_1 = f'{tt_nb}: Ta có $\\overrightarrow{{AC}}=\\left({k}\\sqrt{{3}};{dy}\\right) \\Rightarrow AC=\\sqrt{{\\left({k}\\sqrt{{3}}\\right)^2+{dy_sq}}}={side}$.'
    loigiai_th_1 = f'{tt_th}: Ta có $\\overrightarrow{{AB}}=\\left(-{k}\\sqrt{{3}};{dy}\\right) \\Rightarrow AB=\\sqrt{{\\left(-{k}\\sqrt{{3}}\\right)^2+{dy_sq}}}={side}$, $AC={side}$ và $\\overrightarrow{{BC}}=\\left({2 * k}\\sqrt{{3}};0\\right) \\Rightarrow BC=\\sqrt{{\\left({2 * k}\\sqrt{{3}}\\right)^2+0^2}}={2 * k}\\sqrt{{3}}$. Ta thấy $AB=AC={side} \\neq BC$ nên tam giác $ABC$ cân tại $A$.'
    loigiai_vd_1 = f'{tt_vd}: Nửa chu vi tam giác là $p=\\dfrac{{AB+AC+BC}}{{2}}={k}\\left(2+\\sqrt{{3}}\\right)$.\\\\ Diện tích tam giác: $S_{{\\triangle ABC}}=\\sqrt{{p(p-AB)(p-AC)(p-BC)}}={s_coef}\\sqrt{{3}}$.'
    loigiai_vdc_1 = f'{tt_vdc}: Ta có $\\cos A=\\dfrac{{AB^2+AC^2-BC^2}}{{2AB\\cdot AC}}=\\dfrac{{{side}^2+{side}^2-\\left({2 * k}\\sqrt{{3}}\\right)^2}}{{2\\cdot {side}\\cdot {side}}}=-\\dfrac{{1}}{{2}} \\Rightarrow \\widehat{{BAC}}=120^\\circ$.\\\\ Vì tam giác $ABC$ cân tại $A$ nên $\\widehat{{ABC}}=\\widehat{{ACB}}=30^\\circ$.'
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    list_nb_2 = [loigiai_nb_1]
    list_th_2 = [loigiai_th_1]
    list_vd_2 = [loigiai_vd_1]
    list_vdc_2 = [loigiai_vdc_1]
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
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
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
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
