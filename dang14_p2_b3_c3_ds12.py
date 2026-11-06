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


def bt_dang14_p2_b3_c3_ds12(self):
                # Khai báo biến
                x = symbols('x')

                # Thiết lập tham số random
                a_val = random.randint(2, 4)
                k = a_val**2  # Để nghiệm x = 0, x = ±a đẹp

                f = x**3
                g = k*x

                # Nội dung câu hỏi
                noidungcauhoi = r'''Cho hai hàm số $f(x) = %s$ và $g(x) = %s$.''' % (latex(f), latex(g))

                ########################################################################
                # a) Nhận biết: Nguyên hàm của f(x)
                ########################################################################
                int_f = integrate(f, x)
                nb_da_1_d = r'''\True $\int f(x) \text{d}x = %s + C$''' % (latex(int_f))
                nb_da_1_s = r'''$\int f(x) \text{d}x = %s + C$''' % (latex(x**4 + Rational(1, 2)))
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = r'''Ta có $\int f(x) \text{d}x = \int %s \text{d}x = %s + C$.''' % (latex(f), latex(int_f))

                ########################################################################
                # b) Thông hiểu: Nguyên hàm của f(x)*g(x)
                ########################################################################
                fg = simplify(f * g)
                int_fg = integrate(fg, x)
                th_da_1_d = r'''\True $\int f(x) \cdot g(x) \text{d}x = %s + C$''' % (latex(int_fg))
                th_da_1_s = r'''$\int f(x) \cdot g(x) \text{d}x = %s + C$''' % (latex(fg + x))
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = r'''Ta có $\int f(x) \cdot g(x) \text{d}x = \int %s \text{d}x = %s + C$.''' % (latex(fg), latex(int_fg))

                ########################################################################
                # c) Vận dụng: Diện tích giới hạn bởi f(x) và trục hoành
                ########################################################################
                s_c = integrate(Abs(f), (x, -1, 2))
                vd_da_1_d = r'''\True Diện tích hình phẳng giới hạn bởi các đường $x = -1, x = 2, y = 0, y = f(x)$ bằng $%s$''' % (latex(s_c))
                vd_da_1_s = r'''Diện tích hình phẳng giới hạn bởi các đường $x = -1, x = 2, y = 0, y = f(x)$ bằng $%s$''' % (latex(Rational(15, 4)))
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = r'''Diện tích cần tìm là $S = \int_{-1}^{2} |x^3| \text{d}x = \int_{-1}^{0} (-x^3) \text{d}x + \int_{0}^{2} x^3 \text{d}x = %s$.''' % (latex(s_c))

                ########################################################################
                # d) Vận dụng cao: Diện tích giới hạn bởi f(x) và g(x)
                ########################################################################
                h_func = f - g
                s_d = integrate(Abs(h_func), (x, -a_val, a_val))

                vdc_da_1_d = r'''\True Diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y=f(x)$ và $y=g(x)$ là $S = %s$''' % (latex(s_d))
                vdc_da_1_s = r'''Diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y=f(x)$ và $y=g(x)$ là $S = %s$''' % (latex(s_d + 1))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = (r'''Hoành độ giao điểm: $x^3 - %sx = 0 \Leftrightarrow x \in \{-%s; 0; %s\}$. \\ '''
                                 r'''Diện tích $S = \int_{-%s}^{%s} |x^3 - %sx| \text{d}x = %s$.''' 
                                 % (k, a_val, a_val, a_val, a_val, k, latex(s_d)))

                ########################################################################
                # Logic chọn đáp án Đúng/Sai (1-3 câu đúng)
                ########################################################################
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    ans_a = random.choice(list_nb_da_1)
                    ans_b = random.choice(list_th_da_1)
                    ans_c = random.choice(list_vd_da_1)
                    ans_d = random.choice(list_vdc_da_1)

                    if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                        shuffled_answers = [ans_a, ans_b, ans_c, ans_d]
                        break

                # Xuất nội dung theo style dang13
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choiceTFn \n'
                    '{' + str(shuffled_answers[0]) + '}\n'
                    '{' + str(shuffled_answers[1]) + '}\n'
                    '{' + str(shuffled_answers[2]) + '}\n'
                    '{' + str(shuffled_answers[3]) + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + str(loigiai_nb_1) + '\n'
                    '\\item ' + str(loigiai_th_1) + '\n'
                    '\\item ' + str(loigiai_vd_1) + '\n'
                    '\\item ' + str(loigiai_vdc_1) + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n \\end{minipage} \n\n')

                return content

