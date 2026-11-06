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


def bt_dang34_p2_b3_c3_ds12(self):
                # Khai báo biến symbolic
                x = symbols('x')

                # Bước 1: Random các thông số bài toán
                # f(x) = a(x^2 - 1), g(x) = c(1 - x^2)
                a = random.randint(2, 4)
                c = random.randint(1, 3)

                f = a * (x**2 - 1)
                g = c * (1 - x**2)

                # Tính toán các giá trị toán học
                # Thể tích f quanh Ox: pi * a^2 * (16/15)
                vol_f_val = integrate(pi * f**2, (x, -1, 1))
                vol_f_tex = latex(vol_f_val).replace('pi', r'\pi')

                # Thể tích g quanh Ox: pi * c^2 * (16/15)
                vol_g_val = integrate(pi * g**2, (x, -1, 1))
                vol_g_tex = latex(vol_g_val).replace('pi', r'\pi')

                # Diện tích hình phẳng D: (a+c) * (4/3)
                area_val = integrate(Abs(f - g), (x, -1, 1))
                area_tex = latex(area_val)

                # Bước 2: Tạo đồ thị minh họa (TikZ) theo phong cách dang22
                # f(x) hướng lên, g(x) hướng xuống. Giao tại x = -1 và x = 1.
                tikz_graph = r"""\begin{center}
                \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round, >=stealth]
                    % Tô màu phần hình phẳng
                    \draw[fill=yellow!30, samples=100, domain=-1:1] plot (\x, {""" + str(a) + r"""*((\x)^2-1)}) -- plot[domain=1:-1] (\x, {""" + str(c) + r"""*(1-(\x)^2)}) -- cycle;
                    % Vẽ đồ thị f(x)
                    \draw[thick, samples=100, domain=-1.5:1.5] plot (\x, {""" + str(a) + r"""*((\x)^2-1)}) node[right] {$y=f(x)$};
                    % Vẽ đồ thị g(x)
                    \draw[thick, samples=100, domain=-1.5:1.5] plot (\x, {""" + str(c) + r"""*(1-(\x)^2)}) node[right] {$y=g(x)$};
                    % Trục tọa độ
                    \draw[->] (-2.5,0) -- (2.5,0) node[below] {$x$};
                    \draw[->] (0,-""" + str(a+0.5) + r""") -- (0,""" + str(c+0.5) + r""") node[left] {$y$};
                    % Điểm giao và gốc tọa độ
                    \node at (-1,-0.3) {$-1$};
                    \node at (1,-0.3) {$1$};
                    \node at (0.2,0.2) {$O$};
                \end{tikzpicture}
                \end{center}"""

                noidungcauhoi = r"Cho hình phẳng $(D)$ giới hạn bởi đồ thị hai hàm số $y = f(x) = %s$ và $y = g(x) = %s$ như hình vẽ bên dưới:" % (latex(f), latex(g)) + tikz_graph

                ########################################################################
                # Nhận biết: Hoành độ giao điểm
                ########################################################################
                nb_da_1_d = r'\True Phương trình hoành độ giao điểm của hai đồ thị hàm số là $x = \pm 1$.'
                nb_da_1_s = r'Phương trình hoành độ giao điểm của hai đồ thị hàm số là $x = 0; x = \pm 2$.'
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = r"Xét phương trình hoành độ giao điểm: $%s = %s \Leftrightarrow %s(x^2 - 1) = 0 \Leftrightarrow x = \pm 1$." % (latex(f), latex(g), a + c)

                ########################################################################
                # Thông hiểu: Thể tích f(x) quay quanh Ox
                ########################################################################
                th_da_1_d = r'\True Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi $y=f(x)$ và $Ox$ quanh $Ox$ là $V = %s$.' % (vol_f_tex)
                th_da_1_s = r'Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi $y=f(x)$ và $Ox$ quanh $Ox$ là $V = %s$.' % (latex(vol_f_val/2).replace('pi', r'\pi'))
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = r"Thể tích khối tròn xoay tạo bởi $f(x)$ là $V = \pi \int_{-1}^{1} [f(x)]^2 \text{d}x = \pi \int_{-1}^{1} [%s]^2 \text{d}x = %s$." % (latex(f), vol_f_tex)

                ########################################################################
                # Vận dụng: Thể tích g(x) quay quanh Ox
                ########################################################################
                vd_da_1_d = r'\True Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi $y=g(x)$ và $Ox$ quanh $Ox$ là $V = %s$.' % (vol_g_tex)
                vd_da_1_s = r'Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi $y=g(x)$ và $Ox$ quanh $Ox$ là $V = %s$.' % (latex(vol_g_val + pi).replace('pi', r'\pi'))
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = r"Thể tích khối tròn xoay tạo bởi $g(x)$ là $V = \pi \int_{-1}^{1} [g(x)]^2 \text{d}x = \pi \int_{-1}^{1} [%s]^2 \text{d}x = %s$." % (latex(g), vol_g_tex)

                ########################################################################
                # Vận dụng cao: Diện tích hình phẳng (D)
                ########################################################################
                vdc_da_1_d = r'\True Diện tích hình phẳng $(D)$ được tính theo công thức $S = %s$.' % (area_tex)
                vdc_da_1_s = r'Diện tích hình phẳng $(D)$ được tính theo công thức $S = %s$.' % (latex(area_val + Rational(1, 3)))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = r"Diện tích hình phẳng giới hạn bởi hai đồ thị là $S = \int_{-1}^{1} |f(x) - g(x)| \text{d}x = \int_{-1}^{1} |%s - (%s)| \text{d}x = %s$." % (latex(f), latex(g), area_tex)

                ########################################################################
                # Logic chọn Đúng/Sai (từ 1 đến 3 câu đúng)
                ########################################################################
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    ans_a = random.choice(list_nb_da_1)
                    ans_b = random.choice(list_th_da_1)
                    ans_c = random.choice(list_vd_da_1)
                    ans_d = random.choice(list_vdc_da_1)

                    answers = [ans_a, ans_b, ans_c, ans_d]
                    if 1 <= count_true_answers(answers) <= 3:
                        break

                # Bước cuối: Xuất nội dung theo mẫu LaTeX của dang22
                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choiceTFn \n'
                    '{' + ans_a + '}\n'
                    '{' + ans_b + '}\n'
                    '{' + ans_c + '}\n'
                    '{' + ans_d + '}\n'
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

