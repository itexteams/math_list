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


def bt_dang7_p2_b3_c2_hh12(self):
            # Khai báo biến
            # Hàm xử lý định dạng số thập phân theo tiếng việt (dấu phẩy)
            def fmt_dec(val):
                if isinstance(val, float):
                    return f"{val:g}".replace('.', ',')
                return str(val).replace('.', ',')

            def format_fraction_simplification(num, den):
                val = Rational(num, den)
                val_latex = latex(val)
                if val_latex == f"\\frac{{{num}}}{{{den}}}":
                    return val_latex
                return f"\\frac{{{num}}}{{{den}}} = {val_latex}"

            def format_linear(a, b, var='t'):
                if b == 0: return latex(a)
                term_b = f"{latex(abs(b))}{var}"
                if abs(b) == 1:
                    term_b = var
                if a == 0:
                    return f"-{term_b}" if b < 0 else term_b
                sign = "+" if b > 0 else "-"
                return f"{latex(a)} {sign} {term_b}"

            def format_linear_delayed(a, b, t0):
                var = 't'
                if b == 0: return latex(a)
                abs_b = abs(b)
                term_b = f"{latex(abs_b)}({var}-{t0})"
                if abs_b == 1:
                    term_b = f"({var}-{t0})"
                if a == 0:
                    return f"-{term_b}" if b < 0 else term_b
                sign = "+" if b > 0 else "-"
                return f"{latex(a)} {sign} {term_b}"

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Các bộ vectơ hướng thỏa mãn tọa độ đẹp và độ dài nguyên để làm bài toán luôn tròn đẹp
            A_opts = [
                ({'v': (70, -10, 25), 'd': 75, 'speed': 12}),
                ({'v': (70, 10, 25), 'd': 75, 'speed': 15}),
                ({'v': (36, -48, 80), 'd': 100, 'speed': 15}),
                ({'v': (45, -60, 100), 'd': 125, 'speed': 20}),
                ({'v': (24, 32, 30), 'd': 50, 'speed': 10}),
                ({'v': (16, -12, 15), 'd': 25, 'speed': 10})
            ]

            B_opts = [
                ({'v': (60, 20, 15), 'd': 65, 'speed': 15}),
                ({'v': (60, -20, 15), 'd': 65, 'speed': 13}),
                ({'v': (20, 30, 60), 'd': 70, 'speed': 14}),
                ({'v': (-20, 30, 60), 'd': 70, 'speed': 21}),
                ({'v': (-40, 40, 70), 'd': 90, 'speed': 18})
            ]

            # Random cấu hình tới khi ra đc (từ 1 đến 3 đáp án đúng)
            while True:
                opt_A = random.choice(A_opts)
                opt_B = random.choice(B_opts)

                CA = opt_A['v']
                d_A = opt_A['d']
                v_A = opt_A['speed']

                CB = opt_B['v']
                d_B = opt_B['d']
                v_B = opt_B['speed']

                C_x = random.randint(10, 30)
                C_y = random.randint(10, 30)
                C_z = 0
                C = (C_x, C_y, C_z)

                A = (C_x + CA[0], C_y + CA[1], C_z + CA[2])
                B = (C_x + CB[0], C_y + CB[1], C_z + CB[2])

                t0 = random.choice([1, 2])

                AC = (-CA[0], -CA[1], -CA[2])
                BC = (-CB[0], -CB[1], -CB[2])

                # Mệnh đề a (Góc tấn công)
                sin_alpha_frac = Rational(CB[2], d_B)
                alpha_val = math.degrees(math.asin(CB[2] / d_B))

                diff = random.choice([-2, -1, 1, 2])
                X = int(alpha_val) + diff
                is_a_true = alpha_val > X

                # Mệnh đề b (Khoảng cách tại thời điểm B xuất phát)
                k = Rational(v_A, d_A)
                v_Ax = k * AC[0]
                v_Ay = k * AC[1]
                v_Az = k * AC[2]

                A_prime_x = A[0] + v_Ax * t0
                A_prime_y = A[1] + v_Ay * t0
                A_prime_z = A[2] + v_Az * t0

                dist_sq = (A_prime_x - B[0])**2 + (A_prime_y - B[1])**2 + (A_prime_z - B[2])**2
                dist = math.sqrt(float(dist_sq))
                dist_round = round(dist)

                dist_stmt = dist_round if random.choice([True, False]) else dist_round + random.choice([-2, -1, 1, 2])
                is_b_true = (dist_stmt == dist_round)

                # Mệnh đề c (Tốc độ trên trục Oz của chim A)
                V_z_actual = abs(v_Az)
                V_z_stmt = V_z_actual if random.choice([True, False]) else V_z_actual + random.choice([1, 2])
                is_c_true = (V_z_stmt == V_z_actual)

                # Mệnh đề d (Tốc độ bóng chim B)
                m = Rational(v_B, d_B)
                v_Bx = m * BC[0]
                v_By = m * BC[1]
                v_Bz = m * BC[2]

                v_bong_sq_exact = v_Bx**2 + v_By**2
                v_bong_exact = sqrt(v_bong_sq_exact)
                v_bong_approx = math.sqrt(float(v_bong_sq_exact))

                diff_d = random.choice([-0.2, -0.1, 0.1, 0.2])
                V_d = round(v_bong_approx + diff_d, 1)
                is_d_true = v_bong_approx > V_d

                # Trích xuất mệnh đề
                da_a_d = '\\True Góc tấn công của chim $B$ (góc tạo bởi đường bay và mặt nước) lớn hơn $%s^\\circ$' % X
                da_a_s = 'Góc tấn công của chim $B$ (góc tạo bởi đường bay và mặt nước) lớn hơn $%s^\\circ$' % X
                nb_da_1 = da_a_d if is_a_true else da_a_s

                da_b_d = '\\True Tại thời điểm chim $B$ bắt đầu lao xuống, khoảng cách giữa hai chim là $%s$ m (Kết quả làm tròn đến hàng đơn vị)' % dist_stmt
                da_b_s = 'Tại thời điểm chim $B$ bắt đầu lao xuống, khoảng cách giữa hai chim là $%s$ m (Kết quả làm tròn đến hàng đơn vị)' % dist_stmt
                th_da_1 = da_b_d if is_b_true else da_b_s

                da_c_d = '\\True Tốc độ của chim $A$ theo phương thẳng đứng ($Oz$) bằng $%s$ (m/s)' % latex(V_z_stmt)
                da_c_s = 'Tốc độ của chim $A$ theo phương thẳng đứng ($Oz$) bằng $%s$ (m/s)' % latex(V_z_stmt)
                vd_da_1 = da_c_d if is_c_true else da_c_s

                da_d_d = '\\True Giả sử mặt trời chiếu xuống con chim $B$ thì bóng con chim $B$ trên mặt nước di chuyển với tốc độ lớn hơn $%s$ (m/s)' % fmt_dec(V_d)
                da_d_s = 'Giả sử mặt trời chiếu xuống con chim $B$ thì bóng con chim $B$ trên mặt nước di chuyển với tốc độ lớn hơn $%s$ (m/s)' % fmt_dec(V_d)
                vdc_da_1 = da_d_d if is_d_true else da_d_s

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]

                if 1 <= count_true_answers(answers) <= 3:
                    break

            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            # Cấu hình đề bài
            noidungcauhoi = ('''Trong không gian $Oxyz$ cho trước với mặt nước phẳng lặng trùng với mặt phẳng $(Oxy)$, đơn vị trên mỗi trục là mét; có hai con chim bói cá ở các vị trí $A(%s;%s;%s)$ và $B(%s;%s;%s)$ trên các cành cây đang cùng ngắm mục tiêu là một chú cá đang bơi trên mặt hồ. Khi cá nằm im ở vị trí $C(%s; %s; %s)$ thì hai con chim quyết định tấn công mục tiêu của mình. Chim bói cá ở vị trí $A$ xuất phát trước con còn lại $%s$ giây và bay về phía con cá với vận tốc $%s$ (m/s); chim bói cá còn lại cũng tấn công mục tiêu với vận tốc $%s$ (m/s)''' %
                             (A[0], A[1], A[2], B[0], B[1], B[2], C[0], C[1], C[2], t0, v_A, v_B))

            # Cấu hình chi tiết các lời giải
            loigiai_nb_1 = ('''Mặt phẳng $(Oxy)$ có phương trình $z=0$ và $\\overrightarrow{BC} = (%s; %s; %s)$ \\\\
            Khi đó: $\\sin \\alpha = \\frac{|%s|}{\\sqrt{(%s)^2 + (%s)^2 + (%s)^2}} = %s \\Rightarrow \\alpha \\approx %s^\\circ %s %s^\\circ$ nên mệnh đề a) %s.''' %
                         (BC[0], BC[1], BC[2], BC[2], BC[0], BC[1], BC[2], latex(sin_alpha_frac),
                          fmt_dec(round(alpha_val, 2)),
                          '>' if is_a_true else '<', X,
                          'đúng' if is_a_true else 'sai'))

            A_t_x = format_linear(A[0], v_Ax)
            A_t_y = format_linear(A[1], v_Ay)
            A_t_z = format_linear(A[2], v_Az)

            B_t_x = format_linear_delayed(B[0], v_Bx, t0)
            B_t_y = format_linear_delayed(B[1], v_By, t0)
            B_t_z = format_linear_delayed(B[2], v_Bz, t0)

            k_str = format_fraction_simplification(v_A, d_A)
            m_str = format_fraction_simplification(v_B, d_B)

            loigiai_th_1 = ('''Ta có: $\\overrightarrow{AC} = (%s; %s; %s)$ nên $\\overrightarrow{v}_A = k.\\overrightarrow{AC} \\Leftrightarrow k = %s \\Rightarrow \\overrightarrow{v}_A = \\left( %s; %s; %s \\right)$ \\\\
            Vị trí của con chim $A$ tại thời điểm $t$ là: $A'\\left( %s; %s; %s \\right)$ \\\\
            Ta có: $\\overrightarrow{v}_B = m.\\overrightarrow{BC} \\Rightarrow m = %s$ nên $\\overrightarrow{v}_B = \\left( %s; %s; %s \\right)$ \\\\
            Do chim $A$ xuất phát trước $%s$ giây nên tọa độ của chim bói cá $B$ là:
            $$B\\left( %s; %s; %s \\right)$$
            Tại $t = %s$ thì khoảng cách $A'B = %s \\approx %s$ m nên mệnh đề b) %s.''' %
                         (AC[0], AC[1], AC[2], k_str, latex(v_Ax), latex(v_Ay), latex(v_Az),
                          A_t_x, A_t_y, A_t_z,
                          m_str, latex(v_Bx), latex(v_By), latex(v_Bz),
                          t0,
                          B_t_x, B_t_y, B_t_z,
                          t0, fmt_dec(round(dist, 4)), dist_round,
                          'đúng' if is_b_true else 'sai'))

            loigiai_vd_1 = ('''Ta có $v_{z_A} = |%s| = %s$ (m/s) nên mệnh đề c) %s.''' %
                         (latex(v_Az), latex(V_z_actual), 'đúng' if is_c_true else 'sai'))

            loigiai_vdc_1 = ('''Do bóng dưới nước thuộc $(Oxy)$ nên $\\overrightarrow{v}_{bong} = \\left( %s; %s; 0 \\right) \\Rightarrow |\\overrightarrow{v}_{bong}| = %s \\approx %s %s %s$ (m/s) nên mệnh đề d) %s.''' %
                         (latex(v_Bx), latex(v_By), latex(v_bong_exact), fmt_dec(round(v_bong_approx, 2)),
                          '>' if is_d_true else '<', fmt_dec(V_d), 'đúng' if is_d_true else 'sai'))

            # Xáo trộn đáp án để xuất file LaTeX
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

            # Xuất câu hỏi với đáp án và lời giải
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

