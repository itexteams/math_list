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


def bt_dang7_p2_b3_c4_ds11(self):
            # Khai báo biến
            # Khởi tạo biến x
            x = symbols('x')


            def generate_problem():
                c = randint(1, 5)        # Điểm xét tính liên tục
                k = randint(-5, 5)       # Nghiệm còn lại của tử số (để giới hạn là c - k)
                while k == c: k = randint(-5, 5)

                m = randint(1, 3)        # Hệ số m của hàm bậc nhất bên dưới
                n = (c - k) - m * c      # Tính n để hàm số liên tục

                tu_so = expand((x - c) * (x - k))
                mau_so = x - c
                f_c_expr = m * x + n
                limit_val = c - k

                return c, k, tu_so, mau_so, f_c_expr, m, n, limit_val

            c, k, tu_so, mau_so, f_c_expr, m, n, limit_val = generate_problem()

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $f(x) = \begin{cases} \dfrac{%s}{%s} & \text{khi } x \neq %s \\ %s & \text{khi } x = %s \end{cases}$.''' % (
                latex(tu_so), latex(mau_so), latex(c), latex(f_c_expr), latex(c)
            )

            ########################################################################
            # Nhận biết: Tập xác định
            nb_da_1_d = r'\True Tập xác định của hàm số là $\mathscr{D}=\mathbb{R}$'
            nb_da_1_s = r'Tập xác định của hàm số là $\mathscr{D}=\mathbb{R} \setminus \{%s\}$' % latex(c)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'Hàm số xác định với mọi $x \neq %s$. Tại $x = %s$, $f(%s) = %s$. Vậy $\mathscr{D}=\mathbb{R}$.' % (latex(c), latex(c), latex(c), latex(limit_val))

            ########################################################################
            # Thông hiểu: Tính giới hạn và giá trị tại điểm
            th_da_1_d = r'\True Ta có $\lim_{x \to %s} f(x) = %s$ và $f(%s) = %s$' % (latex(c), latex(limit_val), latex(c), latex(limit_val))
            th_da_1_s = r'Ta có $\lim_{x \to %s} f(x) = %s$ và $f(%s) = %s$' % (latex(c), latex(limit_val + 1), latex(c), latex(limit_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r'Ta có $\lim_{x \to %s} f(x) = \lim_{x \to %s} \dfrac{(x-%s)(x-%s)}{x-%s} = \lim_{x \to %s} (x-%s) = %s$. Mặt khác $f(%s) = %s$.' % (
                latex(c), latex(c), latex(c), latex(k), latex(c), latex(c), latex(k), latex(limit_val), latex(c), latex(limit_val)
            )

            ########################################################################
            # Vận dụng: Tính liên tục tại điểm x = c
            vd_da_1_d = r'\True Hàm số liên tục tại điểm $x = %s$' % latex(c)
            vd_da_1_s = r'Hàm số gián đoạn tại điểm $x = %s$' % latex(c)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'Vì $\lim_{x \to %s} f(x) = f(%s) = %s$ nên hàm số liên tục tại $x = %s$.' % (latex(c), latex(c), latex(limit_val), latex(c))

            ########################################################################
            # Vận dụng cao: Tính liên tục trên R
            vdc_da_1_d = r'\True Hàm số liên tục trên $\mathbb{R}$'
            vdc_da_1_s = r'Hàm số chỉ liên tục trên các khoảng $(-\infty; %s)$ và $(%s; +\infty)$' % (latex(c), latex(c))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r'Với $x \neq %s$, $f(x)$ là hàm phân thức hữu tỉ nên liên tục trên $(-\infty; %s)$ và $(%s; +\infty)$. Kết hợp với tính liên tục tại $x = %s$, suy ra hàm số liên tục trên $\mathbb{R}$.' % (
                latex(c), latex(c), latex(c), latex(c)
            )

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp xáo trộn đáp án đúng/sai
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Xuất kết quả
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choiceTFn \n'
                '{' + nb_sel + '}\n'
                '{' + th_sel + '}\n'
                '{' + vd_sel + '}\n'
                '{' + vdc_sel + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

