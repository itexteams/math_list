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


def bt_dang26_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # ----------------- BƯỚC 1: RANDOM THÔNG SỐ -----------------
            n = random.choice([3, 5]) 
            k = random.choice([-1, -2, -3]) 
            f = x**n - exp(k*x)

            x_start = -1
            x_end = 1
            m = random.randint(1, 5)

            G_expr = integrate(f, x) 

            # ----------------- NỘI DUNG CÂU HỎI -----------------
            noidungcauhoi = (r'''Cho hàm số $f(x)=%s$. Gọi $(H)$ là hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$, trục hoành và hai đường thẳng $x = %s; x = %s$.''' 
                             % (latex(f), latex(x_start), latex(x_end)))

            # ----------------- NHẬN BIẾT (Câu a) -----------------
            nb_da_1_d = r'\True Nguyên hàm của hàm số là $G(x) = %s + C$' % latex(G_expr)
            nb_da_1_s = r'Nguyên hàm của hàm số là $G(x) = %s + C$' % latex(integrate(x**n + exp(k*x), x))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = r'''Nguyên hàm của hàm số là $G(x) = \int \left( %s \right) \text{d}x = %s + C$.''' % (latex(f), latex(G_expr))

            # ----------------- THÔNG HIỂU (Câu b) -----------------
            th_da_1_d = r'\True Diện tích hình phẳng $(H)$ bằng $S = \int_{%s}^{%s} \left| %s \right| \text{d}x$' % (latex(x_start), latex(x_end), latex(f))
            th_da_1_s = r'Diện tích hình phẳng $(H)$ bằng $S = \int_{%s}^{%s} \left( %s \right) \text{d}x$' % (latex(x_start), latex(x_end), latex(f))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = r'''Công thức tính diện tích hình phẳng giới hạn bởi đồ thị $y=f(x)$, trục hoành và $x=a, x=b$ là $S = \int_{a}^{b} |f(x)| \text{d}x$.'''

            # ----------------- VẬN DỤNG (Câu c - Thay đổi dấu thập phân tại đây) -----------------
            V_exact = pi * integrate(f**2, (x, x_start, x_end))
            V_num = round(float(N(V_exact)), 1)
            # Chuyển dấu chấm thành dấu phẩy cho hiển thị
            V_str = str(V_num).replace('.', ',')

            # Tạo giá trị sai cho câu nhiễu và đổi dấu phẩy
            V_num_s = round(V_num/3.14, 1)
            V_str_s = str(V_num_s).replace('.', ',')

            vd_da_1_d = r'\True Thể tích khối tròn xoay tạo thành khi quay $(H)$ quanh trục $Ox$ là $V  \approx %s$' % (V_str)
            vd_da_1_s = r'Thể tích khối tròn xoay tạo thành khi quay $(H)$ quanh trục $Ox$ là $V  \approx %s$' % (V_str_s)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'''Thể tích khối tròn xoay là $V = \pi \int_{%s}^{%s} [f(x)]^2 \text{d}x = \pi \int_{%s}^{%s} \left( %s \right)^2 \text{d}x \approx %s$.''' % (latex(x_start), latex(x_end), latex(x_start), latex(x_end), latex(f), V_str)

            # ----------------- VẬN DỤNG CAO (Câu d) -----------------
            C_val = m - G_expr.subs(x, 0)
            F_final = G_expr + C_val

            vdc_da_1_d = r'\True Biết $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(0)=%s$ thì $F(x) = %s$' % (m, latex(F_final))
            vdc_da_1_s = r'Biết $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(0)=%s$ thì $F(x) = %s + %s$' % (m, latex(G_expr), m + 1)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Vì $F(x)$ là nguyên hàm của $f(x)$ nên $F(x) = %s + C$. \\ Với $F(0)=%s \Leftrightarrow %s + C = %s \Leftrightarrow C = %s$. \\ Vậy $F(x) = %s$.''' 
                            % (latex(G_expr), m, latex(G_expr.subs(x, 0)), m, latex(C_val), latex(F_final)))

            # ----------------- XỬ LÝ TRỘN & XUẤT -----------------
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1); th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1); vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3: break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

