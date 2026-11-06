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


def bt_dang16_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random bài toán
            # Hàm f(x) = sqrt(a - sin(x))
            a = random.choice([2, 3, 4])
            # Hàm g(x) = sqrt(3)*sin(x) - cos(x) + c
            c = randint(1, 4)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=\\sqrt{%s-\\sin x}$ và $g(x)=\\sqrt{3}\\sin x-\\cos x+%s$. Khi đó:'''
                             %(latex(a), latex(c)))

            ########################################################################
            # Nhận biết ############################################
            max_f_val = sqrt(a + 1)
            nb_da_1_d = '\\True Giá trị lớn nhất của hàm số $f(x)$ bằng $%s$' %(latex(max_f_val))
            nb_da_1_s = 'Giá trị lớn nhất của hàm số $f(x)$ bằng $%s$' %(latex(sqrt(a)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có $-1 \\le \\sin x \\le 1 \\Leftrightarrow -1 \\le -\\sin x \\le 1 \\Leftrightarrow %s-1 \\le %s-\\sin x \\le %s+1 \\Leftrightarrow %s \\le %s-\\sin x \\le %s$. \\\\'''
                            '''Do đó $\\sqrt{%s} \\le \\sqrt{%s-\\sin x} \\le \\sqrt{%s} \\Leftrightarrow \\sqrt{%s} \\le f(x) \\le %s$. \\\\'''
                            '''Vậy giá trị lớn nhất của hàm số $f(x)$ bằng $%s$.'''
                            %(latex(a), latex(a), latex(a), latex(a-1), latex(a), latex(a+1), latex(a-1), latex(a), latex(a+1), latex(a-1), latex(max_f_val), latex(max_f_val)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            min_f_val = sqrt(a - 1)
            th_da_1_d = '\\True Giá trị nhỏ nhất của hàm số $f(x)$ bằng $%s$' %(latex(min_f_val))
            th_da_1_s = 'Giá trị nhỏ nhất của hàm số $f(x)$ bằng $0$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Từ đánh giá $-1 \\le \\sin x \\le 1 \\Leftrightarrow %s \\le %s-\\sin x \\le %s$. \\\\'''
                            '''Suy ra $\\sqrt{%s} \\le \\sqrt{%s-\\sin x} \\le \\sqrt{%s} \\Leftrightarrow %s \\le f(x) \\le \\sqrt{%s}$. \\\\'''
                            '''Vậy giá trị nhỏ nhất của hàm số $f(x)$ bằng $%s$.'''
                            %(latex(a-1), latex(a), latex(a+1), latex(a-1), latex(a), latex(a+1), latex(min_f_val), latex(a+1), latex(min_f_val)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            max_g_val = 2 + c
            vd_da_1_d = '\\True Giá trị lớn nhất của hàm số $g(x)$ bằng $%s$' %(latex(max_g_val))
            vd_da_1_s = 'Giá trị lớn nhất của hàm số $g(x)$ bằng $%s$' %(latex(sqrt(3) + c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta biến đổi hàm số $g(x) = 2\\left( \\frac{\\sqrt{3}}{2}\\sin x - \\frac{1}{2}\\cos x \\right) + %s = 2\\sin\\left( x - \\frac{\\pi}{6} \\right) + %s$. \\\\'''
                            '''Vì $-1 \\le \\sin\\left( x - \\frac{\\pi}{6} \\right) \\le 1 \\Leftrightarrow -2 \\le 2\\sin\\left( x - \\frac{\\pi}{6} \\right) \\le 2 \\Leftrightarrow -2+%s \\le g(x) \\le 2+%s$. \\\\'''
                            '''Do đó $%s \\le g(x) \\le %s$. \\\\'''
                            '''Vậy giá trị lớn nhất của hàm số $g(x)$ bằng $%s$.'''
                            %(latex(c), latex(c), latex(c), latex(c), latex(c-2), latex(max_g_val), latex(max_g_val)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            min_g_val = c - 2
            vdc_da_1_d = '\\True Giá trị nhỏ nhất của hàm số $g(x)$ bằng $%s$' %(latex(min_g_val))
            vdc_da_1_s = 'Giá trị nhỏ nhất của hàm số $g(x)$ bằng $%s$' %(latex(-c))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Từ phép biến đổi $g(x) = 2\\sin\\left( x - \\frac{\\pi}{6} \\right) + %s$, ta luôn có: \\\\'''
                             '''$-2 + %s \\le g(x) \\le 2 + %s \\Leftrightarrow %s \\le g(x) \\le %s$. \\\\'''
                             '''Vậy giá trị nhỏ nhất của hàm số $g(x)$ bằng $%s$.'''
                             %(latex(c), latex(c), latex(c), latex(min_g_val), latex(2+c), latex(min_g_val)))

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

