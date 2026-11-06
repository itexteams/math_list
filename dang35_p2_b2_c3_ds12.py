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


def bt_dang35_p2_b2_c3_ds12(self):
    # Sinh ngẫu nhiên các giá trị cho các ý a, c, d
    while True:
        # Cho ý a:
        val_b_a = random.choice([1, 2, 3, -1, -2, -3])
        int_a_true = 2 * val_b_a
        int_a_false = int_a_true + random.choice([-2, -1, 1, 2])

        # Cho ý c và d:
        # Cho tích phân \int_0^2 f(x)dx = I_cd => 2B = I_cd => B = I_cd / 2
        b_cd_true = random.choice([-3, -2, -1, 1, 2, 3])
        I_cd = 2 * b_cd_true
        b_cd_false = -b_cd_true  # Giá trị sai thường gặp (nhầm dấu)

        # Cho điều kiện f'(1) = k_deriv => -A*pi = k_deriv => A = -k_deriv / pi
        k_deriv = random.choice([-4, -3, -2, 2, 3, 4])
        A_num = -k_deriv
        # A = A_num / pi
        break

    # Nội dung câu hỏi
    noidungcauhoi = '''Cho hàm số $f(x) = A\\sin\\pi x + B$ với $A, B$ là hằng số. '''

    #########################################################################
    # Nhận biết: Ý a) Khi A = \pi, B = ... thì \int_0^2 f(x) dx = ...
    #########################################################################
    nb_da_1_d = '\\True Khi $A = \\pi, B = %s$ thì $\\int_0^2 f(x) \\mathrm{d}x = %s$' % (latex(val_b_a), latex(int_a_true))
    nb_da_1_s = 'Khi $A = \\pi, B = %s$ thì $\\int_0^2 f(x) \\mathrm{d}x = %s$' % (latex(val_b_a), latex(int_a_false))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Khi $A = \\pi$ và $B = %s$, ta có $f(x) = \\pi\\sin\\pi x + %s$.\\\\ Khi đó $\\int_0^2 f(x) \\mathrm{d}x = \\int_0^2 (\\pi\\sin\\pi x + %s) \\mathrm{d}x = \\left. \\left( -\\cos\\pi x + %s x \\right) \\right|_0^2 = (-\\cos 2\\pi + %s) - (-\\cos 0) = %s$.''' % (latex(val_b_a), latex(val_b_a), latex(val_b_a), latex(val_b_a), latex(2 * val_b_a), latex(int_a_true)))
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    #########################################################################
    # Thông hiểu: Ý b) \int_0^2 f(x) dx = 2B hoặc sai là -2B
    #########################################################################
    th_da_1_d = '\\True $\\int_0^2 f(x) \\mathrm{d}x = 2B$'
    th_da_1_s = '$\\int_0^2 f(x) \\mathrm{d}x = -2B$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = '''Ta có:\\\\ $\\int_0^2 f(x) \\mathrm{d}x = \\int_0^2 (A\\sin\\pi x + B) \\mathrm{d}x = \\left. \\left( -\\frac{A}{\\pi}\\cos\\pi x + Bx \\right) \\right|_0^2 = \\left(-\\frac{A}{\\pi}\\cos 2\\pi + 2B\\right) - \\left(-\\frac{A}{\\pi}\\cos 0 + 0\\right) = -\\frac{A}{\\pi} + 2B + \\frac{A}{\\pi} = 2B$.'''
    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    #########################################################################
    # Vận dụng: Ý c) Nếu \int_0^2 f(x) dx = I_cd thì B = ...
    #########################################################################
    da_c_val_true = latex(b_cd_true)
    da_c_val_false = latex(b_cd_false)

    vd_da_1_d = '\\True Nếu $\\int_0^2 f(x) \\mathrm{d}x = %s$ thì $B = %s$' % (latex(I_cd), da_c_val_true)
    vd_da_1_s = 'Nếu $\\int_0^2 f(x) \\mathrm{d}x = %s$ thì $B = %s$' % (latex(I_cd), da_c_val_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Theo câu trên, ta có $\\int_0^2 f(x) \\mathrm{d}x = 2B$.\\\\ Do đó, nếu $\\int_0^2 f(x) \\mathrm{d}x = %s$ thì $2B = %s \\Leftrightarrow B = %s$.''' % (latex(I_cd), latex(I_cd), da_c_val_true))
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    #########################################################################
    # Vận dụng cao: Ý d) Số A, B thỏa mãn điều kiện f'(1) = k_deriv và \int_0^2 f(x) dx = I_cd lần lượt là ...
    #########################################################################
    tex_A_true = '\\frac{%s}{\\pi}' % (latex(A_num)) if A_num != 1 and A_num != -1 else ('\\frac{1}{\\pi}' if A_num == 1 else '-\\frac{1}{\\pi}')
    tex_A_false = '\\frac{%s}{\\pi}' % (latex(-A_num)) if -A_num != 1 and -A_num != -1 else ('\\frac{1}{\\pi}' if -A_num == 1 else '-\\frac{1}{\\pi}')

    vdc_da_1_d = '\\True Số $A, B$ thỏa mãn điều kiện $f\'(1) = %s$ và $\\int_0^2 f(x) \\mathrm{d}x = %s$ lần lượt là $%s$ và $%s$' % (latex(k_deriv), latex(I_cd), tex_A_true, da_c_val_true)
    vdc_da_1_s = 'Số $A, B$ thỏa mãn điều kiện $f\'(1) = %s$ và $\\int_0^2 f(x) \\mathrm{d}x = %s$ lần lượt là $%s$ và $%s$' % (latex(k_deriv), latex(I_cd), tex_A_false, da_c_val_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Ta có $f\'(x) = (A\\sin\\pi x + B)\' = A\\pi\\cos\\pi x$.\\\\ Suy ra $f\'(1) = A\\pi\\cos\\pi = -A\\pi$.\\\\ Theo giả thiết $f\'(1) = %s \\Leftrightarrow -A\\pi = %s \\Leftrightarrow A = %s$.\\\\ Lại có $\\int_0^2 f(x) \\mathrm{d}x = 2B = %s \\Leftrightarrow B = %s$.\\\\ Vậy $A = %s$ và $B = %s$.''' % (latex(k_deriv), latex(k_deriv), tex_A_true, latex(I_cd), da_c_val_true, tex_A_true, da_c_val_true))
    list_vdc_2 = [loigiai_vdc_1]

    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi có từ 1 đến 3 đáp án đúng
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content

