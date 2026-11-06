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


def bt_dang36_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Để tập xác định là R, ta chọn c=1 và |d| > 1, ví dụ d = -2 hoặc -3
            c = 1
            d = random.choice([-2, -3, 2, 3])
            a = random.randint(1, 3)
            b = random.randint(-2, 2)
            if a*d - b*c == 0:
                b = b + 1 # Tránh hàm hằng

            # Tính các giá trị
            val_x_0 = Rational(a + b, c + d)

            # GTLN, GTNN
            # Đặt t = cos(x), t in [-1, 1]. y(t) = (a*t + b) / (t + d)
            # y'(t) = (ad - b) / (t+d)^2. Luôn mang một dấu.
            # GTLN, GTNN sẽ đạt tại các biên t = 1 và t = -1
            val_1 = Rational(a + b, c + d)
            val_minus_1 = Rational(-a + b, -c + d)

            if val_1 > val_minus_1:
                M = val_1
                m = val_minus_1
            else:
                M = val_minus_1
                m = val_1

            # Cho c) phương trình y = k vô nghiệm
            # (a*cos x + b) / (cos x + d) = k <=> (a-k)cos x = k*d - b <=> cos x = (k*d - b) / (a-k)
            # Chọn k sao cho |(k*d - b) / (a-k)| > 1
            # Thử k = 1: cos x = (d - b) / (a - 1)
            k = 1
            if a == 1:
                k = 2 # Tránh mẫu số 0
            val_cos_k = Rational(k*d - b, a - k)
            if abs(val_cos_k) > 1:
                c_is_true = True
                str_c = "vô nghiệm"
            else:
                c_is_true = False
                str_c = "có nghiệm"

            # Tính biểu thức 9M + m hoặc k_M * M + m
            k_M = random.randint(2, 5)
            val_d = k_M * M + m

            # Chuẩn bị chuỗi LaTeX cho hàm số
            if a == 1:
                str_tu = "\\cos x"
            elif a == -1:
                str_tu = "-\\cos x"
            else:
                str_tu = "%s \\cos x" % latex(a)

            if b > 0:
                str_tu += " + %s" % latex(b)
            elif b < 0:
                str_tu += " - %s" % latex(-b)

            str_mau = "\\cos x"
            if d > 0:
                str_mau += " + %s" % latex(d)
            elif d < 0:
                str_mau += " - %s" % latex(-d)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = \\frac{%s}{%s}$.'''
                             % (str_tu, str_mau))

            ########################################################################
            # Nhận biết
            # Các đáp án
            nb_da_1_d = '\\True Đồ thị hàm số đã cho đi qua điểm $\\left(0; %s\\right)$' % latex(val_x_0)
            nb_da_1_s = 'Đồ thị hàm số đã cho đi qua điểm $\\left(0; %s\\right)$' % latex(val_x_0 + 1)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Thay $x = 0$ vào hàm số ta được $y = \\frac{%s \\cdot \\cos 0 + %s}{\\cos 0 + %s} = \\frac{%s}{%s} = %s$.\\\\
            Vậy đồ thị hàm số đi qua điểm $\\left(0; %s\\right)$.'''
                            % (a, b, d, a+b, c+d, latex(val_x_0), latex(val_x_0)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu
            # Các đáp án
            th_da_1_d = '\\True Hàm số đã cho là hàm số chẵn và có tập xác định $\\mathbb{R}$'
            th_da_1_s = 'Hàm số đã cho là hàm số lẻ và có tập xác định $\\mathbb{R}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Vì $\\cos x \\in [-1; 1]$ nên $\\cos x + %s \\neq 0, \\forall x \\in \\mathbb{R}$. Do đó tập xác định của hàm số là $\\mathscr{D} = \\mathbb{R}$.\\\\
            Với mọi $x \\in \\mathbb{R}$, ta có $-x \\in \\mathbb{R}$ và $y(-x) = \\frac{%s \\cos(-x) + %s}{\\cos(-x) + %s} = \\frac{%s \\cos x + %s}{\\cos x + %s} = y(x)$.\\\\
            Vậy hàm số đã cho là hàm số chẵn.'''
                            % (d, a, b, d, a, b, d))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng
            # Các đáp án
            if c_is_true:
                vd_da_1_d = '\\True Phương trình $y = %s$ vô nghiệm' % k
                vd_da_1_s = 'Phương trình $y = %s$ có nghiệm' % k
            else:
                vd_da_1_d = '\\True Phương trình $y = %s$ có nghiệm' % k
                vd_da_1_s = 'Phương trình $y = %s$ vô nghiệm' % k

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            if c_is_true:
                loigiai_vd_1 = ('''Ta có $y = %s \\Leftrightarrow \\frac{%s}{%s} = %s \\Leftrightarrow %s = %s(\\cos x + %s) \\Leftrightarrow %s \\cos x = %s \\Leftrightarrow \\cos x = %s$.\\\\
            Vì $\\left|%s\\right| > 1$ nên phương trình vô nghiệm.'''
                                % (k, str_tu, str_mau, k, str_tu, k, d, a-k, k*d-b, latex(val_cos_k), latex(val_cos_k)))
            else:
                 loigiai_vd_1 = ('''Ta có $y = %s \\Leftrightarrow \\frac{%s}{%s} = %s \\Leftrightarrow %s = %s(\\cos x + %s) \\Leftrightarrow %s \\cos x = %s \\Leftrightarrow \\cos x = %s$.\\\\
            Vì $\\left|%s\\right| \\le 1$ nên phương trình có nghiệm.'''
                                % (k, str_tu, str_mau, k, str_tu, k, d, a-k, k*d-b, latex(val_cos_k), latex(val_cos_k)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao
            # Các đáp án
            vdc_da_1_d = '\\True Gọi $M, m$ tương ứng là giá trị lớn nhất và giá trị nhỏ nhất của hàm số thì $%s M + m = %s$' % (k_M, latex(val_d))
            vdc_da_1_s = 'Gọi $M, m$ tương ứng là giá trị lớn nhất và giá trị nhỏ nhất của hàm số thì $%s M + m = %s$' % (k_M, latex(val_d + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Đặt $t = \\cos x, t \\in [-1; 1]$. Xét hàm số $f(t) = \\frac{%s t + %s}{t + %s}$ trên đoạn $[-1; 1]$.\\\\
            Đạo hàm $f'(t) = \\frac{%s \\cdot %s - %s \\cdot 1}{(t + %s)^2} = \\frac{%s}{(t + %s)^2}$. Hàm số đơn điệu trên $[-1; 1]$.\\\\
            Ta có $f(1) = %s, f(-1) = %s$.\\\\
            Suy ra $M = \\max_{[-1; 1]} f(t) = %s, m = \\min_{[-1; 1]} f(t) = %s$.\\\\
            Vậy $%s M + m = %s \\cdot (%s) + (%s) = %s$.'''
                             % (a, b, d, a, d, b, d, a*d-b, d, latex(val_1), latex(val_minus_1), latex(M), latex(m), k_M, k_M, latex(M), latex(m), latex(val_d)))

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
            return content

