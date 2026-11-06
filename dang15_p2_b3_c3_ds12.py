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


def bt_dang15_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # x0 là giao điểm dương với Ox. 
            x0 = random.randint(3,5)
            # m là hoành độ giao điểm với đường thẳng y = k (m nguyên và 0 < m < x0)
            m = random.randint(2, x0 - 1)

            # Tính các thông số: Parabol y = -x^2 + c
            c_val = x0**2
            a_val = -1
            # k là giá trị y tại x = m: k = -m^2 + c_val
            k_val = c_val - m**2

            f_x = a_val*x**2 + c_val
            g_x = f_x - k_val 

            # --- Hình vẽ TikZ ---
            # Lưu ý: Toàn bộ dấu % trong TikZ đã được xử lý để tránh lỗi định dạng
            hinh_ve = r"""\begin{center}
            \begin{tikzpicture}[>=stealth, scale=0.5]
                \draw[fill=yellow!40, draw=none] (0,%s) -- plot[domain=0:%s, samples=100] (\x,{%s-(\x)^2}) -- (%s,%s) -- cycle;
                \draw[->] (-%s,0) -- (%s,0) node[below] {$x$};
                \draw[->] (0,-1) -- (0,%s) node[left] {$y$};
                \node at (-0.4,-0.4) {$O$};
                \draw[thick, samples=100, domain=-%s:%s] plot (\x,{%s-(\x)^2});
                \draw[thick] (-%s,%s) -- (%s,%s) node[right] {$y = %s$};
                \draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s);
                \fill (0,%s) circle (1.5pt) node[above right] {$%s$};
                \fill (0,%s) circle (1.5pt) node[left] {$%s$};
                \fill (%s,0) circle (1.5pt) node[below] {$%s$};
                \fill (-%s,0) circle (1.5pt) node[below] {$-%s$};
                \node at (%s, %s) {$S$};
            \end{tikzpicture}
            \end{center}""" % (k_val, m, c_val, m, k_val, 
                   x0+1.5, x0+1.5, c_val+1.5, 
                   x0+0.5, x0+0.5, c_val, 
                   x0+0.5, k_val, x0+1, k_val, k_val,
                   m, m, m, k_val,
                   c_val, c_val,
                   k_val, k_val,
                   x0, x0,
                   x0, x0,
                   m/2, k_val + (c_val-k_val)/2)

            # Nội dung câu hỏi
            noidungcauhoi = (r"Parabol $(P): y = f(x)$ có đồ thị cắt đường thẳng $y = %s$ tại $2$ điểm như hình vẽ." % k_val + hinh_ve)

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = r'\True Phương trình Parabol $(P)$ là $y = %s$' % latex(f_x)
            nb_da_1_s = r'Phương trình Parabol $(P)$ là $y = %s x^2 + %s$' % (latex(a_val), latex(k_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (r"Gọi $(P): y = ax^2 + bx + c$. Dựa vào hình vẽ, $(P)$ đi qua $(-%s; 0), (%s; 0), (0; %s)$. "
                            r"Suy ra $a=%s, b=0, c=%s$. Vậy $(P): y = %s$." 
                            % (x0, x0, c_val, a_val, c_val, latex(f_x)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            area_ox = integrate(f_x, (x, -x0, x0))
            th_da_1_d = r'\True Diện tích hình phẳng giới hạn bởi $(P)$ và trục hoành là $S_0 = %s$' % latex(area_ox)
            th_da_1_s = r'Diện tích hình phẳng giới hạn bởi $(P)$ và trục hoành là $S_0 = %s$' % latex(area_ox / 2)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = (r"Diện tích giới hạn bởi $(P)$ và trục hoành là $S_0 = \int_{-%s}^{%s} |%s| \text{d}x = %s$." 
                            % (x0, x0, latex(f_x), latex(area_ox)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = r'\True Hoành độ giao điểm của $(P)$ và đường thẳng $y = %s$ là $x = \pm %s$' % (k_val, m)
            vd_da_1_s = r'Hoành độ giao điểm của $(P)$ và đường thẳng $y = %s$ là $x = \pm %s$' % (k_val, x0)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (r"Hoành độ giao điểm của $(P)$ và $y = %s$ là nghiệm: $%s = %s \Leftrightarrow x = \pm %s$." 
                            % (k_val, latex(f_x), k_val, m))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            area_s = integrate(g_x, (x, 0, m))
            vdc_da_1_d = r'\True Diện tích miền tô đậm là $S = %s$' % latex(area_s)
            vdc_da_1_s = r'Diện tích miền tô đậm là $S = %s$' % latex(area_s + 1)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (r"Diện tích miền tô đậm: $S = \int_{0}^{%s} (f(x) - %s) \text{d}x = \int_{0}^{%s} (%s) \text{d}x = %s$." 
                             % (m, k_val, m, latex(g_x), latex(area_s)))
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lại vào list và trộn (theo đúng mẫu)
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

