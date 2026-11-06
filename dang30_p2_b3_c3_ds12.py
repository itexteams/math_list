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


def bt_dang30_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Random cận trên m và hệ số k trong e^(kx)
            m = random.randint(1, 3) 
            k = 1 # Để giữ nguyên form sqrt(e^x) như ảnh, ta chọn k=1. Nếu muốn khó hơn có thể chọn k=odd
            bt_mu = k*x
            f = sqrt(exp(bt_mu))
            f_sq = exp(bt_mu)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Gọi $(H)$ là hình phẳng giới hạn bởi các đường $y = f(x) = \sqrt{e^{%s}}, y = 0, x = 0, x = %s$.''' 
                             % (latex(bt_mu), latex(m)))

            ########################################################################
            # Nhận biết: Nguyên hàm f^2(x)
            ########################################################################
            res_a = integrate(f_sq, x)
            # Đáp án
            nb_da_1_d = r'\True $\int f^2(x) \text{d}x = %s + C$' % (latex(res_a))
            nb_da_1_s = r'$\int f^2(x) \text{d}x = %s + C$' % (latex(f_sq)) # Sai do quên lấy nguyên hàm
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''Ta có $\int f^2(x) \text{d}x = \int e^{%s} \text{d}x = %s + C$.''' % (latex(bt_mu), latex(res_a))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Nguyên hàm f(x)
            ########################################################################
            res_b = integrate(f, x)
            th_da_1_d = r'\True $\int f(x) \text{d}x = %s + C$' % (latex(res_b))
            th_da_1_s = r'$\int f(x) \text{d}x = \frac{\sqrt{e^{%s}}}{\ln \sqrt{e}} + C$' % (latex(bt_mu)) # Sai định dạng hoặc thiếu hệ số
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''Ta có $\int f(x) \text{d}x = \int e^{\frac{%s}{2}x} \text{d}x = %s + C$.''' % (latex(k), latex(res_b))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Diện tích S
            ########################################################################
            S_val = integrate(f, (x, 0, m))
            vd_da_1_d = r'\True Diện tích hình phẳng $(H)$ bằng $S = %s$' % (latex(S_val))
            vd_da_1_s = r'Diện tích hình phẳng $(H)$ bằng $S = %s$' % (latex(S_val/2)) # Sai số liệu
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'''Diện tích hình phẳng là $S = \int_0^{%s} \sqrt{e^{%s}} \text{d}x = \left. %s \right|_0^{%s} = %s$.''' % (latex(m), latex(bt_mu), latex(res_b), latex(m), latex(S_val))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Thể tích V
            ########################################################################
            V_val = pi * integrate(f_sq, (x, 0, m))
            vdc_da_1_d = r'\True Thể tích khối tròn xoay khi quay $(H)$ quanh $Ox$ là $V = %s$' % (latex(V_val))
            vdc_da_1_s = r'Thể tích khối tròn xoay khi quay $(H)$ quanh $Ox$ là $V = %s$' % (latex(integrate(f_sq, (x, 0, m)))) # Thiếu pi
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''Thể tích khối tròn xoay là $V = \pi \int_0^{%s} [f(x)]^2 \text{d}x = \pi \int_0^{%s} e^{%s} \text{d}x = \pi \left. %s \right|_0^{%s} = %s$.''' % (latex(m), latex(m), latex(bt_mu), latex(res_a), latex(m), latex(V_val))
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(list_nb_2[0]) + '\n'
                '\\item ' + str(list_th_2[0]) + '\n'
                '\\item ' + str(list_vd_2[0]) + '\n'
                '\\item ' + str(list_vdc_2[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

