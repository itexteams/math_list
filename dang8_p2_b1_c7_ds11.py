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


def bt_dang8_p2_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            def format_latex(expr):
                """Hàm xử lý các quy tắc LaTeX đặc thù: dấu ngoặc, dấu phẩy, song song"""
                s = latex(expr)
                s = s.replace('\\left(', '(').replace('\\right)', ')') 
                s = s.replace('(', '\\left(').replace(')', '\\right)')
                s = s.replace('.', ',')
                s = s.replace('||', '//')
                return s

            # BƯỚC 1: NGẪU NHIÊN HÓA HÀM SỐ y = ax^2 + bx + c
            a = random.choice([-2, -1, 1, 2])
            b = randint(-4, 4)
            while b == 0: b = randint(-4, 4)
            c = randint(-5, 5)
            f = a*x**2 + b*x + c
            f_prime = diff(f, x)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=%s$ có đồ thị $(C)$.''' 
                             %(format_latex(f)))

            ########################################################################
            # Nhận biết ############################################
            x0 = randint(-2, 2)
            k_correct = f_prime.subs(x, x0)
            k_wrong = k_correct + random.choice([-2, 1, 2])

            nb_da_1_d = '\\True Hệ số góc của tiếp tuyến của $(C)$ tại điểm có hoành độ $x_0=%s$ thuộc $(C)$ là $%s$' %(format_latex(x0), format_latex(k_correct))
            nb_da_1_s = 'Hệ số góc của tiếp tuyến của $(C)$ tại điểm có hoành độ $x_0=%s$ thuộc $(C)$ là $%s$' %(format_latex(x0), format_latex(k_wrong))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có $y'=%s$. Hệ số góc của tiếp tuyến tại $x_0=%s$ là $k=y'\\left( %s \\right)=%s$.'''
                            %(format_latex(f_prime), format_latex(x0), format_latex(x0), format_latex(k_correct)))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            if a > 0:
                y0 = c - (b**2 // (4*a)) + randint(1, 3)
            else:
                y0 = c - (b**2 // (4*a)) - randint(1, 3)

            sols = solve(f - y0, x)
            num_sols = len(sols)

            th_da_1_d = '\\True Có %s phương trình tiếp tuyến của đồ thị hàm số tại điểm có tung độ $y_0=%s$ thuộc $(C)$' %(num_sols, format_latex(y0))
            th_da_1_s = 'Có %s phương trình tiếp tuyến của đồ thị hàm số tại điểm có tung độ $y_0=%s$ thuộc $(C)$' %(num_sols + 1, format_latex(y0))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Xét phương trình hoành độ tiếp điểm: $%s = %s \\Leftrightarrow %s = 0$. \\\\ Phương trình có %s nghiệm phân biệt tương ứng với %s tiếp điểm, do đó có %s tiếp tuyến.'''
                            %(format_latex(f), format_latex(y0), format_latex(expand(f - y0)), num_sols, num_sols, num_sols))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            k_target = 2*a*randint(-2, 2) + b
            xc = Rational(k_target - b, 2*a)
            yc = f.subs(x, xc)
            pttt_c = expand(k_target*(x - xc) + yc)

            vd_da_1_d = '\\True Phương trình tiếp tuyến của đồ thị hàm số biết hệ số góc tiếp tuyến bằng $%s$ là $y=%s$' %(format_latex(k_target), format_latex(pttt_c))
            vd_da_1_s = 'Phương trình tiếp tuyến của đồ thị hàm số biết hệ số góc tiếp tuyến bằng $%s$ là $y=%s$' %(format_latex(k_target), format_latex(expand(pttt_c + 2)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Gọi $x_0$ là hoành độ tiếp điểm. Ta có $y'\\left( x_0 \\right)=%s \\Leftrightarrow %s = %s \\Leftrightarrow x_0 = %s$. \\\\ Với $x_0 = %s \\Rightarrow y_0 = %s$. \\\\ Phương trình tiếp tuyến là $y = %s\\left( x - %s \\right) + %s \\Leftrightarrow y = %s$.'''
                            %(format_latex(k_target), format_latex(f_prime), format_latex(k_target), format_latex(xc), format_latex(xc), format_latex(yc), format_latex(k_target), format_latex(xc), format_latex(yc), format_latex(pttt_c)))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            m_para = randint(-5, 5)
            while m_para == k_target or m_para == b: m_para = randint(-5, 5)
            n_val = randint(-10, 10)

            xd = Rational(m_para - b, 2*a)
            yd = f.subs(x, xd)
            pttt_d = expand(m_para*(x - xd) + yd)

            vdc_da_1_d = '\\True Phương trình tiếp tuyến của đồ thị hàm số biết tiếp tuyến đó song song với đường thẳng $y=%sx+%s$ là $y=%s$' %(format_latex(m_para), format_latex(n_val), format_latex(pttt_d))
            vdc_da_1_s = 'Phương trình tiếp tuyến của đồ thị hàm số biết tiếp tuyến đó song song với đường thẳng $y=%sx+%s$ là $y=%sx+%s$' %(format_latex(m_para), format_latex(n_val), format_latex(m_para), format_latex(expand(yd + 5)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Tiếp tuyến song song với đường thẳng $y=%sx+%s$ nên có hệ số góc $k=%s$. \\\\ Ta có $y'\\left( x_0 \\right)=%s \\Leftrightarrow %s=%s \\Leftrightarrow x_0=%s$. \\\\ Với $x_0=%s \\Rightarrow y_0=%s$. \\\\ Phương trình tiếp tuyến là $y=%s\\left( x-%s \\right)+%s \\Leftrightarrow y=%s$.'''
                             %(format_latex(m_para), format_latex(n_val), format_latex(m_para), format_latex(m_para), format_latex(f_prime), format_latex(m_para), format_latex(xd), format_latex(xd), format_latex(yd), format_latex(m_para), format_latex(xd), format_latex(yd), format_latex(pttt_d)))
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
                '\n\\choiceTFn \n'
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

            # Chỉnh sửa cuối cùng cho dấu +- và --
            content = content.replace('+ -', '- ').replace('- -', '+ ')
            return content

