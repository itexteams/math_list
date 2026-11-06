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


def bt_dang11_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến symbols
            x = symbols('x')

            # --- Bước 1: Khởi tạo dữ liệu ngẫu nhiên cho bài toán ---
            # Giả sử tích phân f(x) từ 1 đến 3 là X_val, g(x) từ 1 đến 3 là Y_val
            # Ta chọn X_val và Y_val trước để kết quả luôn là số nguyên đẹp
            X_val = randint(1, 6)
            Y_val = randint(1, 6)

            # Các hệ số cố định theo đề bài trong ảnh: 
            # PT1: 1*f(x) + 3*g(x) = res1
            # PT2: 2*f(x) - 1*g(x) = res2
            a1, b1 = 1, 3
            a2, b2 = 2, -1

            res1 = a1 * X_val + b1 * Y_val
            res2 = a2 * X_val + b2 * Y_val

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho $f, g$ là hai hàm liên tục trên đoạn $[1;3]$ thỏa mãn: $\int\limits_{1}^{3} [f(x) + %s g(x)] \text{d}x = %s$ và $\int\limits_{1}^{3} [2f(x) - g(x)] \text{d}x = %s$.''' 
                             % (latex(b1), latex(res1), latex(res2)))

            ########################################################################
            # Nhận biết: Kiểm tra tính chất tuyến tính của tích phân
            ########################################################################
            nb_da_1_d = r'\True $\int\limits_{1}^{3} [f(x) + %s g(x)] \text{d}x = \int\limits_{1}^{3} f(x) \text{d}x + %s \int\limits_{1}^{3} g(x) \text{d}x$' % (latex(b1), latex(b1))
            nb_da_1_s = r'$\int\limits_{1}^{3} [f(x) + %s g(x)] \text{d}x = \int\limits_{1}^{3} f(x) \text{d}x + \int\limits_{1}^{3} g(x) \text{d}x$' % (latex(b1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'''Sử dụng tính chất tuyến tính của tích phân:\\
                $\int [af(x) + bg(x)] \text{d}x = a\int f(x) \text{d}x + b\int g(x) \text{d}x$.'''

            ########################################################################
            # Thông hiểu: Giải hệ phương trình tìm tích phân f và g
            ########################################################################
            th_da_1_d = r'\True Giá trị của $\int\limits_{1}^{3} f(x) \text{d}x = %s$ và $\int\limits_{1}^{3} g(x) \text{d}x = %s$' % (latex(X_val), latex(Y_val))
            th_da_1_s = r'Giá trị của $\int\limits_{1}^{3} f(x) \text{d}x = %s$ và $\int\limits_{1}^{3} g(x) \text{d}x = %s$' % (latex(Y_val), latex(X_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Đặt $X = \int\limits_{1}^{3} f(x) \text{d}x, Y = \int\limits_{1}^{3} g(x) \text{d}x$. \\
            Ta có hệ phương trình: $\begin{cases} X + 3Y = %s \\ 2X - Y = %s \end{cases} \Leftrightarrow \begin{cases} X = %s \\ Y = %s \end{cases}$.''' 
                            % (latex(res1), latex(res2), latex(X_val), latex(Y_val)))

            ########################################################################
            # Vận dụng: Tính tổng f(x) + g(x)
            ########################################################################
            val_sum = X_val + Y_val
            vd_da_1_d = r'\True $\int\limits_{1}^{3} [f(x) + g(x)] \text{d}x = %s$' % (latex(val_sum))
            vd_da_1_s = r'$\int\limits_{1}^{3} [f(x) + g(x)] \text{d}x = %s$' % (latex(val_sum + randint(1,3)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'''Ta có $\int\limits_{1}^{3} [f(x) + g(x)] \text{d}x = \int\limits_{1}^{3} f(x) \text{d}x + \int\limits_{1}^{3} g(x) \text{d}x = %s + %s = %s$.''' % (latex(X_val), latex(Y_val), latex(val_sum))

            ########################################################################
            # Vận dụng cao: Tính tổ hợp phức tạp hơn 2f(x) + g(x)
            ########################################################################
            val_complex = 2 * X_val + Y_val
            vdc_da_1_d = r'\True $\int\limits_{1}^{3} [2f(x) + g(x)] \text{d}x = %s$' % (latex(val_complex))
            vdc_da_1_s = r'$\int\limits_{1}^{3} [2f(x) + g(x)] \text{d}x = %s$' % (latex(val_complex - 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r'''Ta có $\int\limits_{1}^{3} [2f(x) + g(x)] \text{d}x = 2\int\limits_{1}^{3} f(x) \text{d}x + \int\limits_{1}^{3} g(x) \text{d}x = 2(%s) + %s = %s$.''' % (latex(X_val), latex(Y_val), latex(val_complex))

            # --- Bước 2: Xử lý xáo trộn và logic True/False ---

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lời giải tương ứng
            sol_nb = loigiai_nb_1
            sol_th = loigiai_th_1
            sol_vd = loigiai_vd_1
            sol_vdc = loigiai_vdc_1

            # Xuất nội dung theo mẫu LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sol_nb) + '\n'
                '\\item ' + str(sol_th) + '\n'
                '\\item ' + str(sol_vd) + '\n'
                '\\item ' + str(sol_vdc) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

