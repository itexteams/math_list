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


def bt_dang28_p2_b1_c3_ds12(self):
            # Khai báo biến
            x = symbols('x')

            # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM ---
            # Giả sử f(x) có dạng: 4x^2 + n
            # Khi đó (x + k)f(x) = (x + k)(4x^2 + n) = 4x^3 + 4kx^2 + nx + nk
            # Nguyên hàm sẽ là: x^4 + (4k/3)x^3 + (n/2)x^2 + nkx + C
            # Để a = 4k/3 là số nguyên, ta chọn k là bội của 3.

            k = random.choice([3, 6, 9])
            n = random.choice([1, 3, 5, 7])
            a_val = Rational(4 * k, 3)
            n_chia_2 = Rational(n, 2)
            nk = n * k

            # Biểu thức vế phải của giả thiết (F(x))
            F_x = x**4 + a_val * x**3 + n_chia_2 * x**2 + nk * x

            # Hàm số f(x) thực tế sau khi giải: f(x) = 4x^2 + n
            f_real = 4*x**2 + n

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (r'''Cho hàm số $y = f(x)$ thỏa mãn $\int (x + %s)f(x)\text{d}x = x^4 + ax^3 + %s x^2 + %s x + C_1, (a \in \mathbb{R})$.''' 
                             % (latex(k), latex(n_chia_2), latex(nk)))

            ########################################################################
            # Nhận biết: Tìm giá trị của a
            ########################################################################
            val_a_dung = a_val
            val_a_sai = a_val + random.choice([-1, 1, 2])

            nb_da_1_d = r'\True Giá trị của tham số $a$ bằng $%s$' % latex(val_a_dung)
            nb_da_1_s = r'Giá trị của tham số $a$ bằng $%s$' % latex(val_a_sai)

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = (r'''Đạo hàm hai vế giả thiết ta có: $(x + %s)f(x) = 4x^3 + 3ax^2 + %s x + %s$. \\
            Thay $x = -%s$ vào hai vế: $0 = 4(-%s)^3 + 3a(-%s)^2 + %s(-%s) + %s \Rightarrow a = %s$.''' 
                            % (latex(k), latex(n), latex(nk), latex(k), latex(k), latex(k), latex(n), latex(k), latex(nk), latex(val_a_dung)))

            ########################################################################
            # Thông hiểu: Giá trị f(0)
            ########################################################################
            f0_dung = n
            f0_sai = n + 1
            th_da_1_d = r'\True Giá trị $f(0) = %s$' % latex(f0_dung)
            th_da_1_s = r'Giá trị $f(0) = %s$' % latex(f0_sai)

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = (r'''Với $a = %s$, ta có $(x + %s)f(x) = 4x^3 + %s x^2 + %s x + %s = (x + %s)(4x^2 + %s)$. \\
            Suy ra $f(x) = 4x^2 + %s$. Vậy $f(0) = %s$.''' 
                            % (latex(val_a_dung), latex(k), latex(3*val_a_dung), latex(n), latex(nk), latex(k), latex(n), latex(n), latex(f0_dung)))

            ########################################################################
            # Vận dụng: Giá trị f(a)
            ########################################################################
            fa_dung = 4*(val_a_dung**2) + n
            fa_sai = 4*(val_a_dung**2) - n
            vd_da_1_d = r'\True Giá trị $f(a) = %s$' % latex(fa_dung)
            vd_da_1_s = r'Giá trị $f(a) = %s$' % latex(fa_sai)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = (r'''Ta có $f(x) = 4x^2 + %s$. Với $a = %s$, ta có $f(%s) = 4 \cdot (%s)^2 + %s = %s$.''' 
                            % (latex(n), latex(val_a_dung), latex(val_a_dung), latex(val_a_dung), latex(n), latex(fa_dung)))

            ########################################################################
            # Vận dụng cao: Nguyên hàm của f(x)
            ########################################################################
            nguyen_ham = integrate(f_real, x)
            vdc_da_1_d = r'\True Một nguyên hàm của $f(x)$ là $F(x) = %s$' % latex(nguyen_ham)
            vdc_da_1_s = r'Một nguyên hàm của $f(x)$ là $F(x) = %s$' % latex(nguyen_ham + x**2)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = (r'''Ta có $\int f(x)\text{d}x = \int (4x^2 + %s)\text{d}x = %s + C$.''' 
                             % (latex(n), latex(nguyen_ham)))

            # --- LOGIC CHỌN ĐÁP ÁN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

