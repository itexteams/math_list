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


def bt_dang10_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Tìm các giá trị ngẫu nhiên để tạo bài toán mới tương tự
            a1 = randint(2, 5) # Hệ số câu a: y = a1*sin(x)

            a2 = randint(2, 4) # Hệ số câu b: y = a2*cos(x) - b2
            b2 = randint(1, 3)

            c3 = randint(2025, 2035) # Hệ số câu c: y = c3 - a3*cos(x)
            a3 = randint(2, 6)

            a4 = randint(2, 4) # Hệ số câu d: y = sin^2(x) + a4*sin(x) - b4 (chọn sao cho đỉnh parbol nằm ngoài hoặc trong khoảng khảo sát)
            b4 = randint(1, 3)

            # Nội dung câu hỏi tung ra đề bài tổng quát
            noidungcauhoi = ('''Các mệnh đề sau đúng hay sai?''')

            ########################################################################
            # Nhận biết (Ý a) ############################################
            # Hàm số y = a1*sin(x) có tập giá trị T = [-a1, a1]
            nb_da_1_d = '\\True Hàm số $y = %s\\sin x$ có tập giá trị là $T = [-%s; %s]$' %(latex(a1), latex(a1), latex(a1))
            nb_da_1_s = 'Hàm số $y = %s\\sin x$ có tập giá trị là $T = [0; %s]$' %(latex(a1), latex(a1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có $-1 \\le \\sin x \\le 1 \\Leftrightarrow -%s \\le %s\\sin x \\le %s$.\\\\'''
                            '''Do đó, tập giá trị của hàm số là $T = [-%s; %s]$.''' 
                            %(latex(a1), latex(a1), latex(a1), latex(a1), latex(a1)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Ý b) ############################################
            # Hàm số y = a2*cos(x) - b2 có tập giá trị T = [-a2 - b2, a2 - b2]
            min_b = -a2 - b2
            max_b = a2 - b2
            th_da_1_d = '\\True Hàm số $y = %s\\cos x - %s$ có tập giá trị là $T = [-%s; %s]$' %(latex(a2), latex(b2), latex(abs(min_b)), latex(max_b) if max_b >= 0 else '-%s'%latex(abs(max_b)))
            th_da_1_s = 'Hàm số $y = %s\\cos x - %s$ có tập giá trị là $T = [-%s; %s]$' %(latex(a2), latex(b2), latex(a2), latex(a2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Ta có $-1 \\le \\cos x \\le 1 \\Leftrightarrow -%s \\le %s\\cos x \\le %s \\Leftrightarrow -%s - %s \\le %s\\cos x - %s \\le %s - %s \\Leftrightarrow %s \\le y \\le %s$.\\\\'''
                            '''Do đó, tập giá trị của hàm số là $T = [%s; %s]$.'''
                            %(latex(a2), latex(a2), latex(a2), latex(a2), latex(b2), latex(a2), latex(b2), latex(a2), latex(b2), latex(min_b), latex(max_b), latex(min_b), latex(max_b)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng (Ý c) ############################################
            # Hàm số y = c3 - a3*cos(x) có tập giá trị T = [c3 - a3, c3 + a3]
            min_c = c3 - a3
            max_c = c3 + a3
            vd_da_1_d = '\\True Hàm số $y = %s - %s\\cos x$ có tập giá trị là $T = [%s; %s]$' %(latex(c3), latex(a3), latex(min_c), latex(max_c))
            vd_da_1_s = 'Hàm số $y = %s - %s\\cos x$ có tập giá trị là $T = [-%s; %s]$' %(latex(c3), latex(a3), latex(a3), latex(a3))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta có $-1 \\le \\cos x \\le 1 \\Leftrightarrow -%s \\le -%s\\cos x \\le %s \\Leftrightarrow %s - %s \\le %s - %s\\cos x \\le %s + %s \\Leftrightarrow %s \\le y \\le %s$.\\\\'''
                            '''Do đó, tập giá trị của hàm số là $T = [%s; %s]$.'''
                            %(latex(a3), latex(a3), latex(a3), latex(c3), latex(a3), latex(c3), latex(a3), latex(c3), latex(a3), latex(min_c), latex(max_c), latex(min_c), latex(max_c)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao (Ý d) ############################################
            # Hàm số y = sin^2(x) + a4*sin(x) - b4. Đặt t = sin(x), t thuộc [-1; 1]
            # Xét f(t) = t^2 + a4*t - b4 trên [-1; 1]. Hoành độ đỉnh t_I = -a4/2.
            # Do a4 >= 2 nên t_I <= -1. Hàm số đồng biến trên [-1; 1].
            # Giá trị nhỏ nhất tại t = -1: f(-1) = 1 - a4 - b4
            # Giá trị lớn nhất tại t = 1: f(1) = 1 + a4 - b4
            min_d = 1 - a4 - b4
            max_d = 1 + a4 - b4

            vdc_da_1_d = '\\True Hàm số $y = \\sin^2 x + %s\\sin x - %s$ có tập giá trị là $T = [%s; %s]$' %(latex(a4), latex(b4), latex(min_d), latex(max_d))
            vdc_da_1_s = 'Hàm số $y = \\sin^2 x + %s\\sin x - %s$ có tập giá trị là $T = [-%s; %s]$' %(latex(a4), latex(b4), latex(a4+b4), latex(a4+b4))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Đặt $t = \\sin x$, với $t \\in [-1; 1]$. Hàm số trở thành $y = t^2 + %st - %s$.\\\\'''
                             '''Xét hàm số $f(t) = t^2 + %st - %s$ trên đoạn $[-1; 1]$.\\\\'''
                             '''Hàm số có hoành độ đỉnh là $t_I = -\\frac{%s}{2} \\le -1$, do đó hàm số đồng biến trên đoạn $[-1; 1]$.\\\\'''
                             '''Ta có: $f(-1) = (-1)^2 + %s(-1) - %s = %s$ và $f(1) = 1^2 + %s(1) - %s = %s$.\\\\'''
                             '''Suy ra $%s \\le y \\le %s$. Vậy tập giá trị của hàm số là $T = [%s; %s]$.'''
                             %(latex(a4), latex(b4), latex(a4), latex(b4), latex(a4), latex(a4), latex(b4), latex(min_d), latex(a4), latex(b4), latex(max_d), latex(min_d), latex(max_d), latex(min_d), latex(max_d)))

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

            # Gán lại vào danh sách sau khi kiểm tra điều kiện
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

