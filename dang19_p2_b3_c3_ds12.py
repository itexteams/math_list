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


def bt_dang19_p2_b3_c3_ds12(self):
                # Khai báo biến
                x = symbols('x')

                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn k là điểm giao nhau sao cho sqrt(k) là số nguyên để hình vẽ đẹp
                k_val = random.choice([1, 4])
                # m = k * sqrt(k) để y = sqrt(x) và y = x^2/m giao nhau tại (k, sqrt(k))
                m_val = int(k_val * sqrt(k_val))

                f_expr = sqrt(x)
                g_expr = x**2 / m_val

                # Tính toán các giá trị toán học
                dien_tich_S = integrate(f_expr - g_expr, (x, 0, k_val))
                v1_val = pi * integrate(f_expr**2, (x, 0, k_val))
                v2_val = pi * integrate(g_expr**2, (x, 0, k_val))
                v_total = v1_val - v2_val

                # Cấu hình TikZ động
                scale = 4.0 / k_val
                tikz_code = r"""\begin{tikzpicture}[scale=%s, >=stealth, x=1cm, y=1cm]
                    \draw[->] (-0.5,0) -- (%s,0) node[below] {$x$};
                    \draw[->] (0,-0.5) -- (0,%s) node[left] {$y$};
                    \draw[fill=yellow!50, domain=0:%s, samples=100] plot (\x, {sqrt(\x)}) -- plot [domain=%s:0] (\x, {(\x)^2/%s}) -- cycle;
                    \draw[domain=0:%s, samples=100, thick] plot (\x, {sqrt(\x)}) node[above right, scale=0.7] {$y=\sqrt{x}$};
                    \draw[domain=0:%s, samples=100, thick] plot (\x, {(\x)^2/%s}) node[below right, scale=0.7] {$y=\frac{x^2}{%s}$};
                    \draw[dashed] (%s,0) -- (%s,%s);
                    \node[below, scale=0.8] at (%s,0) {$%s$};
                    \node[below left, scale=0.8] at (0,0) {$O$};
                \end{tikzpicture}""" % (scale, k_val+1, sqrt(k_val)+1, k_val, k_val, m_val, k_val+0.3, k_val+0.3, m_val, m_val, k_val, k_val, sqrt(k_val), k_val, k_val)

                # Nội dung câu hỏi theo phong cách immini
                noidungcauhoi = (r'''\immini{Xét hình phẳng $(H)$ giới hạn bởi các đường $y=\sqrt{x}$, $y=\frac{x^2}{%s}$ và hai đường thẳng $x=0, x=%s$. Gọi $V$ là thể tích khối tròn xoay tạo thành khi quay hình phẳng $(H)$ quanh trục $Ox$.}{%s}''' 
                                % (m_val, k_val, tikz_code))

                ########################################################################
                # a) Nhận biết: Công thức diện tích
                ########################################################################
                nb_da_1_d = r'''\True Diện tích hình phẳng là $S = \int_0^{%s} \left( \sqrt{x} - \frac{x^2}{%s} \right) \text{d}x = %s$''' % (k_val, m_val, latex(dien_tich_S))
                nb_da_1_s = r'''Diện tích hình phẳng là $S = \int_0^{%s} \left( \sqrt{x} + \frac{x^2}{%s} \right) \text{d}x$''' % (k_val, m_val)
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                loigiai_nb_1 = r'''Trên đoạn $[0;%s]$, đồ thị $y=\sqrt{x}$ nằm phía trên $y=\frac{x^2}{%s}$ nên $S = \int_0^{%s} \left( \sqrt{x} - \frac{x^2}{%s} \right) \text{d}x = %s$.''' % (k_val, m_val, k_val, m_val, latex(dien_tich_S))

                ########################################################################
                # b) Thông hiểu: Thể tích khối V1
                ########################################################################
                th_da_1_d = r'''\True Thể tích khối tròn xoay sinh ra khi quay $y=\sqrt{x}$ quanh $Ox$ trên $[0;%s]$ là $V_1 = %s$''' % (k_val, latex(v1_val))
                th_da_1_s = r'''Thể tích khối tròn xoay sinh ra khi quay $y=\sqrt{x}$ quanh $Ox$ trên $[0;%s]$ là $V_1 = %s$''' % (k_val, latex(2*v1_val))
                list_th_da_1 = [th_da_1_d, th_da_1_s]
                loigiai_th_1 = r'''Ta có $V_1 = \pi \int_0^{%s} (\sqrt{x})^2 \text{d}x = \pi \frac{x^2}{2} \bigg|_0^{%s} = %s$.''' % (k_val, k_val, latex(v1_val))

                ########################################################################
                # c) Vận dụng: Thể tích khối V2
                ########################################################################
                vd_da_1_d = r'''\True Thể tích khối tròn xoay sinh ra khi quay $y=\frac{x^2}{%s}$ quanh $Ox$ trên $[0;%s]$ là $V_2 = %s$''' % (m_val, k_val, latex(v2_val))
                vd_da_1_s = r'''Thể tích khối tròn xoay sinh ra khi quay $y=\frac{x^2}{%s}$ quanh $Ox$ trên $[0;%s]$ là $V_2 = %s$''' % (m_val, k_val, latex(v2_val/2))
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                loigiai_vd_1 = r'''Ta có $V_2 = \pi \int_0^{%s} \left( \frac{x^2}{%s} \right)^2 \text{d}x = \frac{\pi}{%s} \frac{x^5}{5} \bigg|_0^{%s} = %s$.''' % (k_val, m_val, m_val**2, k_val, latex(v2_val))

                ########################################################################
                # d) Vận dụng cao: Thể tích tổng V
                ########################################################################
                vdc_da_1_d = r'''\True Thể tích khối tròn xoay cần tính là $V = V_1 - V_2 = %s$''' % (latex(v_total))
                vdc_da_1_s = r'''Thể tích khối tròn xoay cần tính là $V = V_1 + V_2 = %s$''' % (latex(v1_val + v2_val))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                loigiai_vdc_1 = r'''Thể tích vật thể tròn xoay khi quay hình phẳng giới hạn bởi hai đồ thị quanh trục $Ox$ là $V = |V_1 - V_2| = %s - %s = %s$.''' % (latex(v1_val), latex(v2_val), latex(v_total))

                # --- Trình bày kết quả và chọn đáp án ---
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    ans_a = random.choice(list_nb_da_1)
                    ans_b = random.choice(list_th_da_1)
                    ans_c = random.choice(list_vd_da_1)
                    ans_d = random.choice(list_vdc_da_1)
                    if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                        break

                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + 
                    '\n\\choiceTFn \n'
                    '{' + str(ans_a) + '}\n'
                    '{' + str(ans_b) + '}\n'
                    '{' + str(ans_c) + '}\n'
                    '{' + str(ans_d) + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + str(loigiai_nb_1) + '\n'
                    '\\item ' + str(loigiai_th_1) + '\n'
                    '\\item ' + str(loigiai_vd_1) + '\n'
                    '\\item ' + str(loigiai_vdc_1) + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n \\end{minipage}\n\n')

                return content

