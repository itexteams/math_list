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


def bt_dang37_p2_b3_c3_ds12(self):
                # Khai báo biến symbolic
                x = symbols('x')

                # Bước 1: Thiết lập thông số (Sử dụng k=1 theo hình vẽ gốc)
                k_val = 1
                f = exp(x)
                g = x**2 - 1

                # Tính toán các giá trị hỗ trợ lời giải
                v1_exact = pi * integrate(f**2, (x, -k_val, k_val))
                v1_approx = str(round(float(v1_exact.evalf()), 1)).replace('.', ',')

                v2_exact = pi * integrate(g**2, (x, -k_val, k_val))
                v2_latex = latex(v2_exact).replace('pi', r'\pi')

                s_exact = integrate(f - g, (x, -k_val, k_val))
                s_final_latex = latex(together(s_exact))
                nguyen_ham_s = integrate(f - g, x)

                # Bước 2: Tạo đồ thị minh họa (TikZ) theo phong cách dang22
                tikz_graph = r"""\begin{center}
                \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round, >=stealth]
                    \draw[fill=yellow!30, samples=100, domain=-1:1] plot (\x, {exp(\x)}) -- plot[domain=1:-1] (\x, {(\x)^2-1}) -- cycle;
                    \draw[->] (-2,0) -- (2.5,0) node[below] {$x$};
                    \draw[->] (0,-1.5) -- (0,3.5) node[left] {$y$};
                    \draw[dashed] (-1,0) -- (-1,0.36) (1,0) -- (1,2.71);
                    \draw[thick, red, domain=-1.5:1.2] plot (\x, {exp(\x)}) node[right] {$y=e^x$};
                    \draw[thick, blue, domain=-1.6:1.6] plot (\x, {(\x)^2-1}) node[above] {$y=x^2-1$};
                    \node[below left] at (0,0) {$O$};
                    \node[below] at (-1,0) {$-1$};
                    \node[below] at (1,0) {$1$};
                \end{tikzpicture}
                \end{center}"""

                noidungcauhoi = (r'''Cho các hình phẳng: $(H_1)$ giới hạn bởi $y = e^x, x = \pm 1, y=0$; $(H_2)$ giới hạn bởi $y = x^2 - 1, x = \pm 1, y=0$ và $(H)$ là hình phẳng giới hạn bởi đồ thị hai hàm số $y = e^x, y = x^2 - 1$ và các đường thẳng $x = \pm 1$ như hình vẽ:''' + tikz_graph)

                ########################################################################
                # Nhận biết: Công thức diện tích H1
                ########################################################################
                nb_da_1_d = r'\True Công thức tính diện tích hình phẳng $(H_1)$ là $S_1 = \int_{-1}^{1} e^x \text{d}x$.'
                nb_da_1_s = r'Công thức tính diện tích hình phẳng $(H_1)$ là $S_1 = \pi \int_{-1}^{1} e^x \text{d}x$.'
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = r"Vì $e^x > 0$ trên $[-1; 1]$ nên diện tích $S_1 = \int_{-1}^{1} |e^x| \text{d}x = \int_{-1}^{1} e^x \text{d}x$."

                ########################################################################
                # Thông hiểu: Thể tích V1 (quay H1)
                ########################################################################
                th_da_1_d = r'\True Thể tích khối tròn xoay khi quay $(H_1)$ quanh trục hoành là $V_1 \approx %s$.' % v1_approx
                th_da_1_s = r'Thể tích khối tròn xoay khi quay $(H_1)$ quanh trục hoành là $V_1 \approx 22,8$.'
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = r"Ta có $V_1 = \pi \int_{-1}^{1} (e^x)^2 \text{d}x = \pi \int_{-1}^{1} e^{2x} \text{d}x = \frac{\pi}{2} e^{2x} \Big|_{-1}^{1} \approx %s$." % v1_approx

                ########################################################################
                # Vận dụng: Thể tích V2 (quay H2)
                ########################################################################
                vd_da_1_d = r'\True Thể tích khối tròn xoay khi quay $(H_2)$ quanh trục hoành là $V_2 = %s$.' % v2_latex
                vd_da_1_s = r'Thể tích khối tròn xoay khi quay $(H_2)$ quanh trục hoành là $V_2 = \frac{8\pi}{15}$.'
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = r"Ta có $V_2 = \pi \int_{-1}^{1} (x^2-1)^2 \text{d}x = \pi \int_{-1}^{1} (x^4 - 2x^2 + 1) \text{d}x = %s$." % v2_latex

                ########################################################################
                # Vận dụng cao: Diện tích hình phẳng H
                ########################################################################
                vdc_da_1_d = r'\True Diện tích hình phẳng $(H)$ là $S = %s$.' % s_final_latex
                vdc_da_1_s = r'Diện tích hình phẳng $(H)$ là $S = \frac{3e^2 - 4e - 3}{3e}$.'
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = (r"Dựa vào đồ thị, trên $[-1; 1]$ ta có $e^x \ge x^2-1$. "
                                r"Diện tích $S = \int_{-1}^{1} (e^x - x^2 + 1) \text{d}x = (%s) \Big|_{-1}^{1} = %s$." 
                                % (latex(nguyen_ham_s), s_final_latex))

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

