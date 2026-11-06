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


def bt_dang16_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Ta random phương trình lượng giác sin x = m với m thuộc các giá trị đặc biệt âm.
            # Danh sách các bộ dữ liệu ngẫu nhiên gồm: (giá trị m, góc lượng giác tương ứng alpha)
            list_random = [
                (Rational(-1, 2), Rational(-1, 6)),    # sin x = -1/2 tương ứng alpha = -pi/6
                (-sqrt(2)/2, Rational(-1, 4)),          # sin x = -sqrt(2)/2 tương ứng alpha = -pi/4
                (-sqrt(3)/2, Rational(-1, 3))           # sin x = -sqrt(3)/2 tương ứng alpha = -pi/3
            ]

            val_m, alpha_frac = random.choice(list_random)

            # Các giá trị toán học phục vụ lời giải và đáp án
            alpha_duong = abs(alpha_frac)
            alpha_bu = 1 - alpha_frac if alpha_frac < 0 else 1 + alpha_frac # pi - alpha = pi - (-pi/6) = 7pi/6
            nghiem_am_max = alpha_frac # nghiệm âm lớn nhất luôn là alpha vì alpha nằm trong khoảng (-pi/2; 0)

            # Chuyển đổi sang chuỗi latex để hiển thị
            str_m = latex(val_m)
            str_alpha = latex(alpha_frac) + '\\pi' if alpha_frac != -1 else '-\\pi'
            str_alpha_duong = latex(alpha_duong) + '\\pi'
            str_alpha_bu = latex(alpha_bu) + '\\pi'

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình lượng giác $\\sin x = %s$, khi đó:''' % (str_m))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Phương trình tương đương $\\sin x = \\sin\\left( %s \\right)$' % (str_alpha)
            nb_da_1_s = 'Phương trình tương đương $\\sin x = \\sin\\left( %s \\right)$' % (str_alpha_duong)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có $\\sin\\left( %s \\right) = %s$. Do đó phương trình $\\sin x = %s$ tương đương với $\\sin x = \\sin\\left( %s \\right)$.''' 
                            % (str_alpha, str_m, str_m, str_alpha))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Phương trình có nghiệm là: $x = %s + k2\\pi; x = %s + k2\\pi (k \\in \\mathbb{Z})$' % (str_alpha, str_alpha_bu)
            th_da_1_s = 'Phương trình có nghiệm là: $x = %s + k2\\pi; x = -%s + k2\\pi (k \\in \\mathbb{Z})$' % (str_alpha, str_alpha_bu)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Áp dụng công thức nghiệm của phương trình lượng giác cơ bản đối với hàm số sin:\\\\
            $\\sin x = \\sin\\left( %s \\right) \\Leftrightarrow \\left[\\begin{aligned} & x = %s + k2\\pi \\\\ & x = \\pi - \\left( %s \\right) + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & x = %s + k2\\pi \\\\ & x = %s + k2\\pi \\end{aligned}\\right. (k \\in \\mathbb{Z})$.''' 
                            % (str_alpha, str_alpha, str_alpha, str_alpha, str_alpha_bu))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Phương trình có nghiệm âm lớn nhất bằng $%s$' % (str_alpha)
            vd_da_1_s = 'Phương trình có nghiệm âm lớn nhất bằng $%s$' % (latex(alpha_frac - 2) + '\\pi')
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Từ hai họ nghiệm $x = %s + k2\\pi$ và $x = %s + k2\\pi$, ta tìm các nghiệm âm:\\\\
            - Họ nghiệm thứ nhất cho các nghiệm âm khi $k \\le 0$, nghiệm âm lớn nhất ứng với $k=0$ là $x = %s$.\\\\
            - Họ nghiệm thứ hai cho các nghiệm âm khi $k \\le -1$, nghiệm âm lớn nhất ứng với $k=-1$ là $x = %s - 2\\pi = %s$.\\\\
            So sánh hai giá trị, ta thấy $%s > %s$, do đó nghiệm âm lớn nhất của phương trình là $%s$.''' 
                            % (str_alpha, str_alpha_bu, str_alpha, str_alpha_bu, latex(alpha_bu - 2) + '\\pi', str_alpha, latex(alpha_bu - 2) + '\\pi', str_alpha))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Số nghiệm của phương trình trong khoảng $(-\\pi;\\pi)$ là hai nghiệm'
            vdc_da_1_s = 'Số nghiệm của phương trình trong khoảng $(-\\pi;\\pi)$ là ba nghiệm'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Xét các nghiệm thuộc khoảng $(-\\pi;\\pi)$:\\\\
            - Với họ nghiệm $x = %s + k2\\pi$, ta có $-\\pi < %s + k2\\pi < \\pi \\Leftrightarrow -1 < %s + 2k < 1 \\Leftrightarrow k=0$, thu được $1$ nghiệm là $x = %s$.\\\\
            - With họ nghiệm $x = %s + k2\\pi$, ta có $-\\pi < %s + k2\\pi < \\pi \\Leftrightarrow -1 < %s + 2k < 1 \\Leftrightarrow k=-1$, thu được $1$ nghiệm là $x = %s$.\\\\
            Vậy phương trình có tất cả hai nghiệm nằm trong khoảng $(-\\pi;\\pi)$.''' 
                             % (str_alpha, str_alpha, latex(2*alpha_frac), str_alpha, str_alpha_bu, str_alpha_bu, latex(2*alpha_bu), latex(alpha_bu - 2) + '\\pi'))

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

