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


def bt_dang18_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            m_sym = symbols('m')

            # --- BƯỚC 1: RANDOM CÁC THÔNG SỐ CƠ BẢN ---
            # Random hoành độ đỉnh x_I dương để giống hình mẫu (thường chọn 1, 2, 3)
            x_i = random.randint(1, 3) 
            a_val = -1 # Giữ a = -1 để bề lõm hướng xuống như hình
            b_val = -2 * a_val * x_i
            c_num = random.randint(1, 5) # Hệ số tự do c
            k_m = random.randint(2, 5)   # Hệ số của m (ví dụ 4m)

            # Hàm số gốc: y = ax^2 + bx + c - km*m
            f_x = a_val*x**2 + b_val*x + c_num - k_m*m_sym

            # Nội dung câu hỏi
            noidungcauhoi = ("Cho hàm số bậc hai $y = %s$ có đồ thị là Parabol $(P_m)$." 
                             % (latex(f_x)))

            ########################################################################
            # a) Nhận biết: Trục đối xứng
            truc_ds = x_i
            nb_da_1_d = '\\True Trục đối xứng của đồ thị hàm số là đường thẳng $x = %s$' % (latex(truc_ds))
            nb_da_1_s = 'Trục đối xứng của đồ thị hàm số là đường thẳng $x = %s$' % (latex(truc_ds + 1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ("Ta có $-\\frac{b}{2a} = %s \\Rightarrow x = %s$ là trục đối xứng của hàm số bậc hai." 
                            % (latex(truc_ds), latex(truc_ds)))

            ########################################################################
            # b) Thông hiểu: Sự biến thiên với m = 1
            m_val_th = 1
            f_x_th = f_x.subs(m_sym, m_val_th)
            th_da_1_d = '\\True Với $m=%s$, hàm số đồng biến trên $(-\\infty; %s)$ và nghịch biến trên $(%s; +\\infty)$' % (m_val_th, latex(truc_ds), latex(truc_ds))
            th_da_1_s = 'Với $m=%s$, hàm số nghịch biến trên $(-\\infty; %s)$ và đồng biến trên $(%s; +\\infty)$' % (m_val_th, latex(truc_ds), latex(truc_ds))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ("Với $m=%s$ ta có $y = %s$. Vì $a = %s < 0$ nên hàm số đồng biến trên khoảng $(-\\infty; %s)$ và nghịch biến trên khoảng $(%s; +\\infty)$." 
                            % (m_val_th, latex(f_x_th), a_val, latex(truc_ds), latex(truc_ds)))

            ########################################################################
            # c) Vận dụng: Giao điểm với d: y = (b/2)x
            k_d = Rational(b_val, 2)
            # PT: ax^2 + bx + c - km*m = kx <=> -x^2 + (b-k)x + c - km*m = 0
            # Delta = (b-k)^2 - 4(-1)(c - km*m)
            vd_val_m = Rational((b_val - k_d)**2 + 4*c_num, 4*k_m)
            vd_da_1_d = '\\True Đường thẳng $d: y = %sx$ cắt $(P_m)$ tại hai điểm phân biệt khi $m < %s$' % (latex(k_d), latex(vd_val_m))
            vd_da_1_s = 'Đường thẳng $d: y = %sx$ cắt $(P_m)$ tại hai điểm phân biệt khi $m > %s$' % (latex(k_d), latex(vd_val_m))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ("Hoành độ giao điểm của đường thẳng $d: y = %sx$ và đồ thị $(P_m)$ là nghiệm phương trình: $%s = %sx \\Leftrightarrow x^2 + %sx + %s = 0$. Đường thẳng cắt đồ thị tại hai điểm phân biệt khi $\\Delta > 0 \\Leftrightarrow m < %s$." 
                            % (latex(k_d), latex(f_x), latex(k_d), latex(k_d - b_val), latex(k_m*m_sym - c_num), latex(vd_val_m)))

            ########################################################################
            # d) Vận dụng cao: Max trên đoạn [x1, x2] nằm bên trái trục đối xứng
            x_range = [truc_ds - 5, truc_ds - 2]
            max_val_target = random.randint(5, 15)
            y_at_x_max = f_x.subs(x, x_range[1])
            m_sol = solve(y_at_x_max - max_val_target, m_sym)[0]

            vdc_da_1_d = '\\True Trên đoạn $[%s; %s]$, giá trị lớn nhất của hàm số bằng %s khi $m = %s$' % (x_range[0], x_range[1], max_val_target, latex(m_sol))
            vdc_da_1_s = 'Trên đoạn $[%s; %s]$, giá trị lớn nhất của hàm số bằng %s khi $m = %s$' % (x_range[0], x_range[1], max_val_target, latex(m_sol + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            y_dinh = f_x.subs(x, truc_ds)
            tikz_bbt = ("""\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[lgt=1.2,espcl=2.5,deltacl=0.5]{$x$/1,$y$/2}{$-\\infty$,$%s$,$+\\infty$}
            \\tkzTabVar{-/$-\\infty$,+/$%s$,-/$-\\infty$}
            \\end{tikzpicture}
            \\end{center}""" % (latex(truc_ds), latex(y_dinh)))

            loigiai_vdc_1 = ("Ta có bảng biến thiên: \n %s \n Vì đoạn $[%s; %s]$ nằm bên trái trục đối xứng $x=%s$, hàm số đồng biến trên đoạn này. Do đó $M = \\max_{[%s;%s]} y = y(%s) = %s$. Theo bài ra $%s = %s \\Leftrightarrow m = %s$." 
                            % (tikz_bbt, x_range[0], x_range[1], latex(truc_ds), x_range[0], x_range[1], x_range[1], latex(y_at_x_max), latex(y_at_x_max), max_val_target, latex(m_sol)))

            # --- LOGIC CHỌN ĐÁP ÁN ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # --- XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

