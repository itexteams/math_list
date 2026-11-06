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


def bt_dang12_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến và tạo bài toán ngẫu nhiên
            x = symbols('x')
            a = randint(1, 3)
            b = randint(1, 3)
            c = randint(1, 2)
            d = randint(1, 2)

            # F(x) = a*x^2 + b*x, G(x) = c*x^4 + d*x^3
            F_expr = a*x**2 + b*x
            G_expr = c*x**4 + d*x**3

            # f(x) và g(x) là đạo hàm
            f_func = diff(F_expr, x)
            g_func = diff(G_expr, x)

            # Tính các giá trị tích phân
            val_int_g = integrate(g_func, (x, 0, 1))
            val_int_fg = integrate(f_func * g_func, (x, 0, 1))

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho $\int f(x) \text{d}x = %s + C_1$ và $\int g(x) \text{d}x = %s + C_2$.''' 
                             % (latex(F_expr), latex(G_expr)))

            ########################################################################
            # Nhận biết: Tìm f(x)
            nb_da_1_d = r'\True Ta có $f(x) = %s$' % (latex(f_func))
            nb_da_1_s = r'Ta có $f(x) = %s$' % (latex(f_func + randint(1,3)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Ta có $\int f(x) \text{d}x = %s + C_1 \Rightarrow f(x) = (%s)' = %s$.''' 
                            % (latex(F_expr), latex(F_expr), latex(f_func)))

            ########################################################################
            # Thông hiểu: Tìm g(x)
            th_da_1_d = r'\True Ta có $g(x) = %s$' % (latex(g_func))
            th_da_1_s = r'Ta có $g(x) = %s$' % (latex(diff(G_expr, x, 2))) # Đạo hàm cấp 2 là sai
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Ta có $\int g(x) \text{d}x = %s + C_2 \Rightarrow g(x) = (%s)' = %s$.''' 
                            % (latex(G_expr), latex(G_expr), latex(g_func)))

            ########################################################################
            # Vận dụng: Tích phân g(x) từ 0 đến 1
            vd_da_1_d = r'\True Giá trị của $\int_{0}^{1} g(x) \text{d}x = %s$' % (latex(val_int_g))
            vd_da_1_s = r'Giá trị của $\int_{0}^{1} g(x) \text{d}x = %s$' % (latex(val_int_g + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Ta có $\int_{0}^{1} g(x) \text{d}x = \left. (%s) \right|_{0}^{1} = %s$.''' 
                            % (latex(G_expr), latex(val_int_g)))

            ########################################################################
            # Vận dụng cao: Tích phân f(x)*g(x) từ 0 đến 1
            vdc_da_1_d = r'\True Giá trị của $\int_{0}^{1} f(x)g(x) \text{d}x = %s$' % (latex(val_int_fg))
            vdc_da_1_s = r'Giá trị của $\int_{0}^{1} f(x)g(x) \text{d}x = %s$' % (latex(val_int_fg + Rational(1, 2)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Ta có $\int_{0}^{1} f(x)g(x) \text{d}x = \int_{0}^{1} (%s)(%s) \text{d}x = %s$.''' 
                             % (latex(f_func), latex(g_func), latex(val_int_fg)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list để lấy lời giải tương ứng
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(list_nb_1[0])+'}\n'
                '{'+str(list_th_1[0])+'}\n'
                '{'+str(list_vd_1[0])+'}\n'
                '{'+str(list_vdc_1[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(list_nb_2[0])+'\n'
                '\\item '+str(list_th_2[0])+'\n'
                '\\item '+str(list_vd_2[0])+'\n'
                '\\item '+str(list_vdc_2[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

