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


def bt_dang14_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các tham số để sinh đề bài biến thể mới tương tự bài gốc
            # a là hệ số góc (a = 1 ứng với bài mẫu gốc, a = 2 ứng với góc nhân đôi)
            a = random.choice([1, 2])
            # n là số mũ của cot(ax)
            n = random.choice([2, 3])

            # Nội dung câu hỏi
            if a == 1:
                noidungcauhoi = ('''Cho hàm số $f(x) = \\tan x$ và $g(x) = \\cot^{%s} x - \\frac{\\sin 2x}{2}$. Khi đó:''' % (latex(n)))
            else:
                noidungcauhoi = ('''Cho hàm số $f(x) = \\tan 2x$ và $g(x) = \\cot^{%s} 2x - \\frac{\\sin 4x}{2}$. Khi đó:''' % (latex(n)))

            ########################################################################
            # Nhận biết (Ý a) ############################################
            # Tập xác định của f(x) = tan(ax) là D = R \ {pi/(2a) + k*pi/a}
            if a == 1:
                nb_da_1_d = '\\True Tập xác định hàm số $f(x)$: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                nb_da_1_s = 'Tập xác định hàm số $f(x)$: $D = \\mathbb{R} \\setminus \\left\\{ k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                loigiai_nb_1 = ('''Hàm số $f(x) = \\tan x$ xác định khi $\\cos x \\ne 0 \\Leftrightarrow x \\ne \\frac{\\pi}{2} + k\\pi$ ($k \\in \\mathbb{Z}$).\\\\'''
                                '''Do đó, tập xác định của hàm số $f(x)$ là $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$.''')
            else:
                nb_da_1_d = '\\True Tập xác định hàm số $f(x)$: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{4} + \\frac{k\\pi}{2} \\mid k \\in \\mathbb{Z} \\right\\}$'
                nb_da_1_s = 'Tập xác định hàm số $f(x)$: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                loigiai_nb_1 = ('''Hàm số $f(x) = \\tan 2x$ xác định khi $\\cos 2x \\ne 0 \\Leftrightarrow 2x \\ne \\frac{\\pi}{2} + k\\pi \\Leftrightarrow x \\ne \\frac{\\pi}{4} + \\frac{k\\pi}{2}$ ($k \\in \\mathbb{Z}$).\\\\'''
                                '''Do đó, tập xác định của hàm số $f(x)$ là $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{4} + \\frac{k\\pi}{2} \\mid k \\in \\mathbb{Z} \\right\\}$.''')

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Ý b) ############################################
            # Tính tuần hoàn của f(x). f(x) = tan(ax) là hàm tuần hoàn (mệnh đề trong ảnh khẳng định không tuần hoàn -> Sai)
            if a == 1:
                th_da_1_d = 'Hàm số $f(x)$ là hàm không tuần hoàn'
                th_da_1_s = '\\True Hàm số $f(x)$ là hàm tuần hoàn'
                loigiai_th_1 = ('''Hàm số $f(x) = \\tan x$ có tính chất tuần hoàn với chu kỳ $T = \\pi$. Do đó khẳng định hàm số không tuần hoàn là sai.''')
            else:
                th_da_1_d = 'Hàm số $f(x)$ là hàm không tuần hoàn'
                th_da_1_s = '\\True Hàm số $f(x)$ là hàm tuần hoàn'
                loigiai_th_1 = ('''Hàm số $f(x) = \\tan 2x$ có tính chất tuần hoàn với chu kỳ $T = \\frac{\\pi}{2}$. Do đó khẳng định hàm số không tuần hoàn là sai.''')

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng (Ý c) ############################################
            # Tập xác định của g(x). Hàm cot(ax) xác định khi sin(ax) != 0 <=> ax != k*pi <=> x != k*pi/a. Thành phần sin(2ax) luôn xác định.
            if a == 1:
                vd_da_1_d = '\\True Tập xác định hàm số $g(x)$: $D = \\mathbb{R} \\setminus \\left\\{ k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                vd_da_1_s = 'Tập xác định hàm số $g(x)$: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                loigiai_vd_1 = ('''Hàm số $g(x) = \\cot^{%s} x - \\frac{\\sin 2x}{2}$ có thành phần $\\frac{\\sin 2x}{2}$ luôn xác định trên $\\mathbb{R}$, còn thành phần $\\cot^{%s} x$ xác định khi $\\sin x \\ne 0 \\Leftrightarrow x \\ne k\\pi$ ($k \\in \\mathbb{Z}$).\\\\'''
                                '''Do đó, tập xác định của hàm số $g(x)$ là $D = \\mathbb{R} \\setminus \\left\\{ k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$.''' % (latex(n), latex(n)))
            else:
                vd_da_1_d = '\\True Tập xác định hàm số $g(x)$: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{k\\pi}{2} \\mid k \\in \\mathbb{Z} \\right\\}$'
                vd_da_1_s = 'Tập xác định hàm số $g(x)$: $D = \\mathbb{R} \\setminus \\left\\{ k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                loigiai_vd_1 = ('''Hàm số $g(x) = \\cot^{%s} 2x - \\frac{\\sin 4x}{2}$ có thành phần $\\frac{\\sin 4x}{2}$ luôn xác định trên $\\mathbb{R}$, còn thành phần $\\cot^{%s} 2x$ xác định khi $\\sin 2x \\ne 0 \\Leftrightarrow 2x \\ne k\\pi \\Leftrightarrow x \\ne \\frac{k\\pi}{2}$ ($k \\in \\mathbb{Z}$).\\\\'''
                                '''Do đó, tập xác định của hàm số $g(x)$ là $D = \\mathbb{R} \\setminus \\left\\{ \\frac{k\\pi}{2} \\mid k \\in \\mathbb{Z} \\right\\}$.''' % (latex(n), latex(n)))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao (Ý d) ############################################
            # Hàm số g(x) là hàm tuần hoàn. Chu kỳ của cot^n(ax) là pi/a, chu kỳ của sin(2ax) là 2pi/(2a) = pi/a. Vậy g(x) tuần hoàn với T = pi/a.
            if a == 1:
                vdc_da_1_d = '\\True Hàm số $g(x)$ là hàm tuần hoàn'
                vdc_da_1_s = 'Hàm số $g(x)$ là hàm không tuần hoàn'
                loigiai_vdc_1 = ('''Hàm số $g(x) = \\cot^{%s} x - \\frac{\\sin 2x}{2}$ gồm hai hàm thành phần:\\\\'''
                                 '''Hàm số $\\cot^{%s} x$ là hàm số tuần hoàn với chu kỳ $T_1 = \\pi$.\\\\'''
                                 '''Hàm số $\\frac{\\sin 2x}{2}$ là hàm số tuần hoàn với chu kỳ $T_2 = \\frac{2\\pi}{2} = \\pi$.\\\\'''
                                 '''Do đó, hàm số $g(x)$ tổng hợp lại là một hàm số tuần hoàn với chu kỳ chung $T = \\pi$.''' % (latex(n), latex(n)))
            else:
                vdc_da_1_d = '\\True Hàm số $g(x)$ là hàm tuần hoàn'
                vdc_da_1_s = 'Hàm số $g(x)$ là hàm không tuần hoàn'
                loigiai_vdc_1 = ('''Hàm số $g(x) = \\cot^{%s} 2x - \\frac{\\sin 4x}{2}$ gồm hai hàm thành phần:\\\\'''
                                 '''Hàm số $\\cot^{%s} 2x$ là hàm số tuần hoàn với chu kỳ $T_1 = \\frac{\\pi}{2}$.\\\\'''
                                 '''Hàm số $\\frac{\\sin 4x}{2}$ là hàm số tuần hoàn với chu kỳ $T_2 = \\frac{2\\pi}{4} = \\frac{\\pi}{2}$.\\\\'''
                                 '''Do đó, hàm số $g(x)$ tổng hợp lại là một hàm số tuần hoàn với chu kỳ chung $T = \\frac{\\pi}{2}$.''' % (latex(n), latex(n)))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp lọc điều kiện đạt yêu cầu đảm bảo số lượng đáp án đúng nằm trong khoảng [1, 3]
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán đồng bộ lại danh sách sau khi đã kiểm tra xong bộ lọc điều kiện
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

            # Xuất câu hỏi và lời giải định dạng chuẩn theo mẫu khung chương trình đề ra
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
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

