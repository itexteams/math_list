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


def bt_dang36_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Random hai biên m và n (m < n)
            m = random.randint(-2, 0)
            n = random.randint(1, 2)

            # Nội dung hình vẽ TikZ (Dynamic dựa trên m và n)
            tikz_image = r"""\begin{center}
            \begin{tikzpicture}[>=stealth, x=1.5cm, y=1cm, scale=0.8]
                \draw[->] (%(xmin)f,0) -- (%(xmax)f,0) node[below] {$x$};
                \draw[->] (0,-0.5) -- (0,%(ymax)f) node[left] {$y$};
                \draw (0,0) node[below left] {$O$};
                \fill[yellow!40, domain=%(m)d:%(n)d, samples=100] (%(m)d,0) -- plot (\x, {exp(\x)}) -- (%(n)d,0) -- cycle;
                \draw[thick, color=red, domain=%(xmin)f:%(xmax)f, samples=100] plot (\x, {exp(\x)}) node[above] {$y=e^x$};
                \draw[->] (%(xmin)f,0) -- (%(xmax)f,0) node[below] {$x$};
                \draw[->] (0,-0.5) -- (0,%(ymax)f) node[left] {$y$};
                \draw (%(m)d,0.1) -- (%(m)d,-0.1) node[below] {$%(m)d$};
                \draw (%(n)d,0.1) -- (%(n)d,-0.1) node[below] {$%(n)d$};
            \end{tikzpicture}
            \end{center}""" % {'xmin': m-0.5, 'xmax': n+0.2, 'ymax': math.exp(n)+0.5, 'm': m, 'n': n}

            # B2: Viết lại bài toán theo mẫu code python
            noidungcauhoi = (r"Cho đồ thị hàm số $y = e^x$ và hình được tô màu như dưới đây." + tikz_image)

            ########################################################################
            # a) Nhận biết: Các đường giới hạn
            nb_da_1_d = r'\True Hình phẳng đó giới hạn bởi bốn đường $y = e^x$, trục hoành và hai đường thẳng $x = %s$, $x = %s$.' % (m, n)
            nb_da_1_s = r'Hình phẳng đó giới hạn bởi bốn đường $y = e^x$, trục tung và hai đường thẳng $x = %s$, $x = %s$.' % (m, n)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'Dựa vào hình vẽ, hình phẳng giới hạn bởi $y=e^x, y=0, x=%s, x=%s$.' % (m, n)

            ########################################################################
            # b) Thông hiểu: Công thức diện tích
            th_da_1_d = r'\True Ta có diện tích hình phẳng $S = \int_{%s}^{%s} \left| e^x \right| \text{d}x = \int_{%s}^{%s} e^x \text{d}x$.' % (m, n, m, n)
            th_da_1_s = r'Ta có diện tích hình phẳng $S = \int_{%s}^{%s} e^{2x} \text{d}x$.' % (m, n)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r'Công thức tính diện tích là $S = \int_{a}^{b} |f(x)| \text{d}x$. Do $e^x > 0$ nên $S = \int_{%s}^{%s} e^x \text{d}x$.' % (m, n)

            ########################################################################
            # c) Vận dụng: Tính toán diện tích
            area_val = exp(n) - exp(m)
            area_latex = latex(area_val)

            vd_da_1_d = r'\True Diện tích hình phẳng $S = %s$.' % area_latex
            vd_da_1_s = r'Diện tích hình phẳng $S = e^{%s} + e^{%s}$.' % (n, m)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'Ta có $S = \int_{%s}^{%s} e^x \text{d}x = e^x \Big|_{%s}^{%s} = %s$.' % (m, n, m, n, area_latex)

            ########################################################################
            # d) Vận dụng cao: Thể tích khối tròn xoay
            # V = pi * integral( (e^x)^2 ) dx = pi/2 * (e^2n - e^2m)
            vol_expr = (pi/2) * (exp(2*n) - exp(2*m))
            vol_latex = latex(vol_expr)

            vdc_da_1_d = r'\True Thể tích khối tròn xoay khi quay hình phẳng đó quanh trục $Ox$ là $V = %s$.' % vol_latex
            vdc_da_1_s = r'Thể tích khối tròn xoay khi quay hình phẳng đó quanh trục $Ox$ là $V = \pi \left( e^{%s} - e^{%s} \right)$.' % (2*n, 2*m)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r'Thể tích $V = \pi \int_{%s}^{%s} (e^x)^2 \text{d}x = \pi \int_{%s}^{%s} e^{2x} \text{d}x = \pi \left( \frac{1}{2} e^{2x} \right) \Big|_{%s}^{%s} = %s$.' % (m, n, m, n, m, n, vol_latex)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Đóng gói và xáo trộn (giữ đúng cấu trúc mẫu của bạn)
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo định dạng minipage và ex
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + 
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

