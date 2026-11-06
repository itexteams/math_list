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


def bt_dang10_p2_b2_c3_ds12(self):
            # --- KHAI BÁO BIẾN NGẪU NHIÊN ---
            x, m, n = symbols('x m n') # Khai báo thêm m, n dạng ký hiệu
            a_val = randint(-5, 5)
            # Chọn b chẵn để n thường là số nguyên/hữu tỉ đẹp
            b_val = 2 * randint(-3, 3) 
            if b_val == 0: b_val = -2
            S_val = randint(-2, 2)

            # Tính toán n dựa trên tích phân từ 1 đến 2 của (bx + n) = S_val
            n_val = S_val - Rational(3 * b_val, 2)

            # Tính toán m dựa trên tính liên tục tại x = 1: 1 + a + m = b + n
            m_val = b_val + n_val - a_val - 1

            # Hàm số chứa tham số m, n (để hiển thị đề bài và thiết lập phương trình)
            f_left_sym = x**2 + a_val*x + m
            f_right_sym = b_val*x + n

            # Hàm số thực tế đã thay số m_val, n_val (để tính toán Vận dụng, Vận dụng cao)
            f_left = x**2 + a_val*x + m_val
            f_right = b_val*x + n_val

            # Nội dung câu hỏi (in ra dạng tham số m, n)
            noidungcauhoi = (r"""Cho hàm số $f(x) = \begin{cases} %s & \text{khi } x < 1 \\ %s & \text{khi } x \ge 1 \end{cases}$ (với $m, n$ là các tham số thực) liên tục trên $\mathbb{R}$ và thỏa mãn $\displaystyle \int_1^2 f(x) \text{d}x = %s$.""" 
                             % (latex(f_left_sym), latex(f_right_sym), latex(S_val)))

            ########################################################################
            # Nhận biết ############################################################
            n_wrong = n_val + random.choice([-1, 1, 2])
            nb_da_1_d = r'\True Giá trị của tham số $n$ bằng $%s$' % (latex(n_val))
            nb_da_1_s = r'Giá trị của tham số $n$ bằng $%s$' % (latex(n_wrong))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (r'''Trên đoạn $[1;2]$, ta có $f(x) = %s$. Ta có: $\int_1^2 f(x) \text{d}x = \int_1^2 (%s) \text{d}x = \left( %s \right) \Big|_1^2 = %s$. Theo giả thiết $\int_1^2 f(x) \text{d}x = %s \Rightarrow %s = %s \Rightarrow n = %s$.''' 
                            % (latex(f_right_sym), latex(f_right_sym), latex(integrate(f_right_sym, x)), 
                            latex(Rational(3*b_val, 2) + n), latex(S_val), 
                            latex(Rational(3*b_val, 2) + n), latex(S_val), latex(n_val)))
            list_nb_2 = [loigiai_nb_1]

            # Xáo trộn Nhận biết
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ###########################################################
            m_wrong = m_val + random.choice([-1, 1, 2])
            th_da_1_d = r'\True Giá trị của tham số $m$ bằng $%s$' % (latex(m_val))
            th_da_1_s = r'Giá trị của tham số $m$ bằng $%s$' % (latex(m_wrong))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = (r'''Vì hàm số liên tục trên $\mathbb{R}$ nên liên tục tại $x=1$. Ta có $\lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} (%s) = %s$ và $\lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} (%s) = %s$. Để hàm số liên tục tại $x=1$ thì $%s = %s \Rightarrow m = %s$.''' 
                            % (latex(f_left_sym), latex(1 + a_val + m), latex(f_right_sym), 
                            latex(b_val + n_val), latex(1 + a_val + m), latex(b_val + n_val), latex(m_val)))
            list_th_2 = [loigiai_th_1]

            # Xáo trộn Thông hiểu
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng #############################################################
            c_val = -1
            f_c = f_left.subs(x, c_val)
            f_c_wrong = f_c + random.randint(1, 3)
            vd_da_1_d = r'\True Giá trị $f(%s) = %s$' % (c_val, latex(f_c))
            vd_da_1_s = r'Giá trị $f(%s) = %s$' % (c_val, latex(f_c_wrong))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (r'''Với $x < 1$, thế $m = %s$ ta có $f(x) = %s$. Do đó $f(%s) = (%s)^2 %s \cdot (%s) %s = %s$.''' 
                            % (latex(m_val), latex(f_left), c_val, c_val, ("+" + str(a_val) if a_val > 0 else str(a_val)), c_val, ("+" + str(m_val) if m_val > 0 else str(m_val)), latex(f_c)))
            list_vd_2 = [loigiai_vd_1]

            # Xáo trộn Vận dụng
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao #########################################################
            I_01 = integrate(f_left, (x, 0, 1))
            I_total = I_01 + S_val
            I_wrong = I_total + Rational(1, 2)
            vdc_da_1_d = r'\True Tích phân $\int_0^2 f(x) \text{d}x = %s$' % (latex(I_total))
            vdc_da_1_s = r'Tích phân $\int_0^2 f(x) \text{d}x = %s$' % (latex(I_wrong))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (r'''Ta có $\int_0^2 f(x) \text{d}x = \int_0^1 f(x) \text{d}x + \int_1^2 f(x) \text{d}x = \int_0^1 (%s) \text{d}x + %s = \left(%s\right) \Big|_0^1 + %s = %s$.''' 
                             % (latex(f_left), latex(S_val), latex(integrate(f_left, x)), 
                                latex(S_val), latex(I_total)))
            list_vdc_2 = [loigiai_vdc_1]

            # Xáo trộn Vận dụng cao
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # --- KIỂM TRA SỐ LƯỢNG ĐÁP ÁN ĐÚNG (1-3) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    shuffled_answers_nb = [nb_sel]
                    shuffled_answers_th = [th_sel]
                    shuffled_answers_vd = [vd_sel]
                    shuffled_answers_vdc = [vdc_sel]
                    break

            # --- XUẤT NỘI DUNG ---
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
                       '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content

