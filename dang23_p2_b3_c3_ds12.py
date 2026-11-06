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


def bt_dang23_p2_b3_c3_ds12(self):
                # Khai báo biến symbolic
                x = symbols('x')

                # Bước 1: Random các thông số bài toán
                a = random.randint(2, 5) 
                k = random.randint(1, 2)
                f = a * exp(-x)

                # Tính toán các giá trị
                primitive = integrate(f, x) 
                definite_integral_val = integrate(f, (x, 0, k)) 
                volume_expr = pi * integrate(f**2, (x, 0, k))

                # Bước 2: Tạo đồ thị minh họa (TikZ) để đồng bộ phong cách với dang22
                tikz_graph = r"""\begin{center}
                \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round, >=stealth]
                    \draw[fill=yellow!30, samples=100, domain=0:""" + str(k) + r"""] plot (\x, {""" + str(a) + r"""*exp(-\x)}) -- (""" + str(k) + r""",0) -- (0,0) -- cycle;
                    \draw[thick, samples=100, domain=-0.5:""" + str(k+1) + r"""] plot (\x, {""" + str(a) + r"""*exp(-\x)});
                    \draw[->] (-1,0) -- (""" + str(k+1.5) + r""",0) node[below] {$x$};
                    \draw[->] (0,-0.5) -- (0,""" + str(a+0.5) + r""") node[left] {$y$};
                    \draw[dashed] (""" + str(k) + r""",0) node[below] {$""" + str(k) + r"""$} -- (""" + str(k) + r""",""" + str(float(a*exp(-k))) + r""");
                    \node at (0.2,-0.2) {$O$};
                    \node at (0.8,""" + str(a/2) + r""") {$y=f(x)$};
                \end{tikzpicture}
                \end{center}"""

                noidungcauhoi = r"Cho hình phẳng $(H)$ giới hạn bởi đồ thị hàm số $y = f(x) = %s e^{-x}$, trục hoành, trục tung và đường thẳng $x = %s$ như hình vẽ sau:" % (latex(a), latex(k)) + tikz_graph

                ########################################################################
                # Nhận biết: Nguyên hàm
                ########################################################################
                nb_da_1_d = r'\True $\int f(x) \text{d}x = %s + C$.' % latex(primitive)
                nb_da_1_s = r'$\int f(x) \text{d}x = %s e^{-x} + C$.' % latex(a)
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = r"Ta có $\int %s e^{-x} \text{d}x = %s \int e^{-x} \text{d}x = -%s e^{-x} + C = %s + C$." % (latex(a), latex(a), latex(a), latex(primitive))

                ########################################################################
                # Thông hiểu: Tích phân xác định
                ########################################################################
                th_da_1_d = r'\True $\int_{0}^{%s} f(x) \text{d}x = %s$.' % (latex(k), latex(definite_integral_val))
                th_da_1_s = r'$\int_{0}^{%s} f(x) \text{d}x = %s$.' % (latex(k), latex(a * (exp(-k) - 1)))
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = r"Sử dụng công thức Newton-Leibniz: $\int_{0}^{%s} %s e^{-x} \text{d}x = \left( %s \right) \Big|_{0}^{%s} = %s$." % (latex(k), latex(a), latex(primitive), latex(k), latex(definite_integral_val))

                ########################################################################
                # Vận dụng: Diện tích hình phẳng
                ########################################################################
                vd_da_1_d = r'\True Diện tích $S$ của hình phẳng $(H)$ là $S = %s$.' % latex(definite_integral_val)
                vd_da_1_s = r'Diện tích $S$ của hình phẳng $(H)$ là $S = %s$.' % latex(definite_integral_val * 2)
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = r"Vì $f(x) = %s e^{-x} > 0$ với mọi $x \in [0; %s]$, nên diện tích hình phẳng là $S = \int_{0}^{%s} f(x) \text{d}x = %s$." % (latex(a), latex(k), latex(k), latex(definite_integral_val))

                ########################################################################
                # Vận dụng cao: Thể tích khối tròn xoay
                ########################################################################
                vdc_da_1_d = r'\True Thể tích khối tròn xoay khi quay $(H)$ quanh trục hoành là $V = %s$.' % latex(volume_expr)
                vdc_da_1_s = r'Thể tích khối tròn xoay khi quay $(H)$ quanh trục hoành là $V = %s$.' % latex(definite_integral_val * pi)
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                v_int_expr = integrate(f**2, x)
                loigiai_vdc_1 = r"Thể tích khối tròn xoay tạo thành là $V = \pi \int_{0}^{%s} [f(x)]^2 \text{d}x = \pi \int_{0}^{%s} %s e^{-2x} \text{d}x = \pi \left( %s \right) \Big|_{0}^{%s} = %s$." % (latex(k), latex(k), latex(a**2), latex(v_int_expr), latex(k), latex(volume_expr))

                ########################################################################
                # Logic chọn Đúng/Sai (từ 1 đến 3 câu đúng)
                ########################################################################
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    nb_da = random.choice(list_nb_da_1)
                    th_da = random.choice(list_th_da_1)
                    vd_da = random.choice(list_vd_da_1)
                    vdc_da = random.choice(list_vdc_da_1)

                    answers = [nb_da, th_da, vd_da, vdc_da]
                    if 1 <= count_true_answers(answers) <= 3:
                        break

                # Bước cuối: Xuất nội dung theo mẫu LaTeX của dang22
                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choiceTFn \n'
                    '{' + nb_da + '}\n'
                    '{' + th_da + '}\n'
                    '{' + vd_da + '}\n'
                    '{' + vdc_da + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + loigiai_nb_1 + '\n'
                    '\\item ' + loigiai_th_1 + '\n'
                    '\\item ' + loigiai_vd_1 + '\n'
                    '\\item ' + loigiai_vdc_1 + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n'
                    '\\end{minipage} \n\n')

                return content

