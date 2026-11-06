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


def bt_dang16_p2_b3_c3_ds12(self):
                # Khai báo biến
                x = symbols('x')

                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Chọn x0 là hoành độ điểm tiếp xúc (nguyên để số đẹp)
                x0 = random.randint(1, 2)
                # Chọn a là đỉnh Parabol (a > x0^2 để Parabol cắt Ox)
                a_val = x0**2 + random.randint(1, 3)

                # f(x) = -x^2 + a
                f = -x**2 + a_val
                # Tiếp tuyến g(x) tại x0: g(x) = f'(x0)(x-x0) + f(x0)
                # f'(x) = -2x => m = -2*x0
                m_val = -2 * x0
                # n = f(x0) - m*x0 = (-x0^2 + a) - (-2*x0)*x0 = x0^2 + a
                n_val = x0**2 + a_val
                g = m_val*x + n_val

                # --- Hình vẽ TikZ ---
                hinh_ve = r'''\begin{center}
                \begin{tikzpicture}[>=stealth, x=1cm, y=1cm, scale=0.8]
                    \draw[->] (-2.5,0) -- (2.5,0) node[below] {$x$};
                    \draw[->] (0,-1) -- (0,%s) node[left] {$y$};
                    \draw (0,0) node[below left] {$O$};
                    \draw[line width=1.2pt, smooth, samples=100, domain=-2.2:2.2] plot(\x, {-(\x)^2+%s});
                    \draw[line width=1pt, domain=-0.2:%s] plot(\x, {%s*\x+%s});
                    \fill[yellow!50] (0,%s) -- plot[domain=0:%s] (\x, {-(\x)^2+%s}) -- (%s,%s) -- (0,%s) -- cycle;
                    \draw (0,%s) node[left] {$%s$};
                    \fill (%s,%s) circle (1.5pt) node[right] {$A$};
                    \node at (-1.5, 1) {$y = f(x)$};
                    \node at (1.5, %s) {$y = g(x)$};
                \end{tikzpicture}
                \end{center}''' % (a_val + 2, a_val, x0 + 0.8, m_val, n_val, 
                                a_val, x0, a_val, x0, m_val*x0+n_val, n_val, 
                                n_val, n_val, x0, m_val*x0+n_val, a_val + 1)

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Parabol $(P): y = f(x) = -x^2 + %s$ tiếp xúc với đường thẳng $y = g(x) = %s$ tại điểm $A$ như hình vẽ bên.''' 
                                % (a_val, latex(g)) + hinh_ve)

                ########################################################################
                # Nhận biết ############################################
                I_g = integrate(g, x)
                nb_da_1_d = r'\True $\int g(x) \text{d}x = %s + C$' % latex(I_g)
                nb_da_1_s = r'$\int g(x) \text{d}x = %s + C$' % latex(I_g + x)
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = r'''Ta có $\int g(x) \text{d}x = \int (%s) \text{d}x = %s + C$.''' % (latex(g), latex(I_g))
                list_nb_2 = [loigiai_nb_1]

                ########################################################################
                # Thông hiểu ############################################
                th_da_1_d = r'\True Tham số $a = %s$' % a_val
                th_da_1_s = r'Tham số $a = %s$' % (a_val + 1)
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = (r"Parabol $y=-x^2+a$ tiếp xúc với $y=%s$ khi hệ $\begin{cases} -x^2+a = %s \\ -2x = %s \end{cases}$ có nghiệm. "
                                r"Giải hệ ta được $x = %s \Rightarrow a = %s$." % (latex(g), latex(g), m_val, x0, a_val))
                list_th_2 = [loigiai_th_1]

                ########################################################################
                # Vận dụng ############################################
                roots = solve(f, x)
                x_r = max(roots)
                S_ox = integrate(f, (x, -x_r, x_r))
                vd_da_1_d = r'\True Diện tích hình phẳng giới hạn bởi $(P)$ và trục hoành là $S = %s$' % latex(S_ox)
                vd_da_1_s = r'Diện tích hình phẳng giới hạn bởi $(P)$ và trục hoành là $S = %s$' % latex(S_ox / 2)
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = (r"Hoành độ giao điểm của $f(x)$ với $Ox$ là $-x^2+%s=0 \Leftrightarrow x = \pm %s$. "
                                r"Diện tích $S = \int_{-%s}^{%s} |%s| \text{d}x = %s$." 
                                % (a_val, latex(x_r), latex(x_r), latex(x_r), latex(f), latex(S_ox)))
                list_vd_2 = [loigiai_vd_1]

                ########################################################################
                # Vận dụng cao ############################################
                S_shaded = integrate(abs(f - g), (x, 0, x0))
                vdc_da_1_d = r'\True Diện tích miền tô đậm bằng $%s$' % latex(S_shaded)
                vdc_da_1_s = r'Diện tích miền tô đậm bằng $%s$' % latex(S_shaded + Rational(1,2))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = (r"Miền tô đậm giới hạn bởi $y=f(x), y=g(x)$, $x=0$ và $x=%s$. "
                                r"Diện tích $S = \int_{0}^{%s} |f(x)-g(x)| \text{d}x = %s$." % (x0, x0, latex(S_shaded)))
                list_vdc_2 = [loigiai_vdc_1]

                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                # Vòng lặp đảm bảo số lượng đáp án đúng từ 1 đến 3
                while True:
                    nb_da_1 = random.choice(list_nb_da_1)
                    th_da_1 = random.choice(list_th_da_1)
                    vd_da_1 = random.choice(list_vd_da_1)
                    vdc_da_1 = random.choice(list_vdc_da_1)
                    answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                    if 1 <= count_true_answers(answers) <= 3:
                        break

                # Đồng bộ hóa list theo phong cách dang15
                list_nb_1 = [nb_da_1]; combined_nb = list(zip(list_nb_1, list_nb_2))
                list_th_1 = [th_da_1]; combined_th = list(zip(list_th_1, list_th_2))
                list_vd_1 = [vd_da_1]; combined_vd = list(zip(list_vd_1, list_vd_2))
                list_vdc_1 = [vdc_da_1]; combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                random.shuffle(combined_nb); shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
                random.shuffle(combined_th); shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
                random.shuffle(combined_vd); shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
                random.shuffle(combined_vdc); shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

                # Xuất nội dung
                content = (r'\begin{minipage}{\textwidth} ' + '\n'
                    r'\begin{ex}' + '\n' + str(noidungcauhoi) + '\n'
                    r'\choiceTFn ' + '\n'
                    '{' + str(shuffled_answers_nb[0]) + '}\n'
                    '{' + str(shuffled_answers_th[0]) + '}\n'
                    '{' + str(shuffled_answers_vd[0]) + '}\n'
                    '{' + str(shuffled_answers_vdc[0]) + '}\n'
                    r'\loigiai{ ' + '\n'
                    r'\begin{enumEX}[a)]{1} ' + '\n'
                    r'\item ' + str(shuffled_solutions_nb[0]) + '\n'
                    r'\item ' + str(shuffled_solutions_th[0]) + '\n'
                    r'\item ' + str(shuffled_solutions_vd[0]) + '\n'
                    r'\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                    r'\end{enumEX}} ' + '\n'
                    r'\end{ex}' + '\n' + r'\end{minipage}' + '\n\n')
                return content

