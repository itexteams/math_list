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


def bt_dang4_p2_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            a_val = random.choice([2, 3, 4, 5]) 
            k_val = Rational(2, a_val - 1) # k sao cho -1/k = (1-a)/2

            # Biểu thức f(x)
            tu_f2 = x**2 - (a_val + 1)*x + a_val
            mau_f2 = x**2 - 1
            f_limit_right = Rational(1 - a_val, 2)

            # Biểu thức g(x) = x^2 + mx + n
            m = random.randint(-5, 5)
            n = random.randint(-5, 5)
            g_expr = x**2 + m*x + n
            g_val_1 = 1 + m + n

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $f(x) = \begin{cases} -%s & \text{khi } x \le 1 \\ \frac{%s}{%s} & \text{khi } x > 1 \end{cases}$ và $g(x) = %s$.''' % (
                latex(x/k_val), latex(tu_f2), latex(mau_f2), latex(g_expr)
            )

            ########################################################################
            # Nhận biết: Tính liên tục của f(x)
            nb_da_1_d = r'\True Hàm số $f(x)$ liên tục tại điểm $x_0 = 1$'
            nb_da_1_s = r'Hàm số $f(x)$ gián đoạn tại điểm $x_0 = 1$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'''Ta có: $f(1) = -%s$ và $\lim_{x \to 1^-} f(x) = -%s$. \\
            $\lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} \frac{(x-1)(x-%s)}{(x-1)(x+1)} = \lim_{x \to 1^+} \frac{x-%s}{x+1} = %s$. \\
            Vì $f(1) = \lim_{x \to 1} f(x) = %s$ nên hàm số liên tục tại $x_0=1$.''' % (
                latex(1/k_val), latex(1/k_val), a_val, a_val, latex(f_limit_right), latex(f_limit_right)
            )
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Tính liên tục của g(x)
            th_da_1_d = r'\True Hàm số $g(x)$ liên tục tại điểm $x_0 = 1$'
            th_da_1_s = r'Hàm số $g(x)$ không liên tục tại điểm $x_0 = 1$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r'''Hàm số $g(x) = %s$ là hàm đa thức nên liên tục trên $\mathbb{R}$, do đó liên tục tại $x_0=1$. \\
            Ta có $g(1) = %s$ và $\lim_{x \to 1} g(x) = %s$.''' % (latex(g_expr), g_val_1, g_val_1)
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Giới hạn f(x) khi x -> 1+
            vd_da_1_d = r'\True Giới hạn $\lim_{x \to 1^+} f(x) = %s$' % latex(f_limit_right)
            vd_da_1_s = r'Giới hạn $\lim_{x \to 1^+} f(x) = %s$' % latex(-f_limit_right)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'''$\lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} \frac{(x-1)(x-%s)}{(x-1)(x+1)} = \frac{1-%s}{1+1} = %s$.''' % (
                a_val, a_val, latex(f_limit_right)
            )
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Tính liên tục của tổng
            vdc_da_1_d = r'\True Hàm số $y = f(x) + g(x)$ liên tục tại điểm $x_0 = 1$'
            vdc_da_1_s = r'Hàm số $y = f(x) + g(x)$ gián đoạn tại điểm $x_0 = 1$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r'''Vì hàm số $f(x)$ và $g(x)$ đều liên tục tại $x_0 = 1$ nên tổng của chúng $y = f(x) + g(x)$ cũng liên tục tại $x_0 = 1$.'''
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung
            content = (r'\begin{minipage}{\textwidth}' + '\n' +
                r'\begin{ex}' + '\n' +
                str(noidungcauhoi) + '\n' +
                r'\choiceTFn' + '\n' +
                '{' + nb_da + '}\n' +
                '{' + th_da + '}\n' +
                '{' + vd_da + '}\n' +
                '{' + vdc_da + '}\n' +
                r'\loigiai{' + '\n' +
                r'\begin{enumEX}[a)]{1}' + '\n' +
                r'\item ' + loigiai_nb_1 + '\n' +
                r'\item ' + loigiai_th_1 + '\n' +
                r'\item ' + loigiai_vd_1 + '\n' +
                r'\item ' + loigiai_vdc_1 + '\n' +
                r'\end{enumEX}}' + '\n' +
                r'\end{ex}' + '\n' +
                r'\end{minipage}' + '\n')
            return content

