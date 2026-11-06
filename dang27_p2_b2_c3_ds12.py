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


def bt_dang27_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # B1: Nghiên cứu đề bài và khởi tạo giá trị ngẫu nhiên
            # f(x) liên tục trên [-2, 3]
            low = -2
            high = 3
            val_int = randint(10, 20)      # Giá trị tích phân từ -2 đến 3
            f_high = randint(25, 40)       # Giá trị F(3)
            f_low = f_high - val_int       # Giá trị F(-2) vì F(3) - F(-2) = val_int

            k_mul = randint(2, 4)          # Hệ số k cho câu a
            f_zero = randint(5, 15)        # Giá trị F(0) cho câu d
            val_int_part = f_zero - f_low  # Tích phân từ -2 đến 0 là F(0) - F(-2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)$ liên tục trên đoạn $[%s;%s]$. Giả sử $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(%s) = %s$. Biết rằng $\\int_{%s}^{%s} f(x) \\mathrm{d}x = %s$.''' 
                             % (latex(low), latex(high), latex(high), latex(f_high), latex(low), latex(high), latex(val_int)))

            ########################################################################
            # Nhận biết (Câu a - Tính chất tuyến tính)
            ########################################################################
            nb_da_1_d = '\\True $\\int_{%s}^{%s} %s f(x) \\mathrm{d}x = %s$' % (latex(low), latex(high), latex(k_mul), latex(k_mul * val_int))
            nb_da_1_s = '$\\int_{%s}^{%s} %s f(x) \\mathrm{d}x = %s$' % (latex(low), latex(high), latex(k_mul), latex(val_int // k_mul))

            # Lời giải câu a
            loigiai_nb_1 = ('''Ta có $\\int_{%s}^{%s} %s f(x) \\mathrm{d}x = %s \\cdot \\int_{%s}^{%s} f(x) \\mathrm{d}x = %s \\cdot %s = %s$.''' 
                            % (latex(low), latex(high), latex(k_mul), latex(k_mul), latex(low), latex(high), latex(k_mul), latex(val_int), latex(k_mul * val_int)))

            ########################################################################
            # Thông hiểu (Câu b - Đảo cận tích phân)
            ########################################################################
            th_da_1_d = '\\True $\\int_{%s}^{%s} f(x) \\mathrm{d}x = %s$' % (latex(high), latex(low), latex(-val_int))
            th_da_1_s = '$\\int_{%s}^{%s} f(x) \\mathrm{d}x = %s$' % (latex(high), latex(low), latex(val_int))

            # Lời giải câu b
            loigiai_th_1 = ('''Áp dụng tính chất đổi cận: $\\int_{%s}^{%s} f(x) \\mathrm{d}x = -\\int_{%s}^{%s} f(x) \\mathrm{d}x = -(%s) = %s$.''' 
                            % (latex(high), latex(low), latex(low), latex(high), latex(val_int), latex(-val_int)))

            ########################################################################
            # Vận dụng (Câu c - Tìm F(-2))
            ########################################################################
            vd_da_1_d = '\\True Giá trị của $F(%s)$ bằng $%s$' % (latex(low), latex(f_low))
            vd_da_1_s = 'Giá trị của $F(%s)$ bằng $%s$' % (latex(low), latex(f_high + val_int))

            # Lời giải câu c
            loigiai_vd_1 = ('''Ta có $\\int_{%s}^{%s} f(x) \\mathrm{d}x = F(%s) - F(%s)$. \\\\ Suy ra $F(%s) = F(%s) - \\int_{%s}^{%s} f(x) \\mathrm{d}x = %s - %s = %s$.''' 
                            % (latex(low), latex(high), latex(high), latex(low), latex(low), latex(high), latex(low), latex(high), latex(f_high), latex(val_int), latex(f_low)))

            ########################################################################
            # Vận dụng cao (Câu d - Tích phân đoạn con)
            ########################################################################
            vdc_da_1_d = '\\True Nếu $F(0) = %s$ thì $\\int_{%s}^{0} f(x) \\mathrm{d}x = %s$' % (latex(f_zero), latex(low), latex(val_int_part))
            vdc_da_1_s = 'Nếu $F(0) = %s$ thì $\\int_{%s}^{0} f(x) \\mathrm{d}x = %s$' % (latex(f_zero), latex(low), latex(f_zero + f_low))

            # Lời giải câu d
            loigiai_vdc_1 = ('''Theo câu c, ta có $F(%s) = %s$. \\\\ Khi đó $\\int_{%s}^{0} f(x) \\mathrm{d}x = F(0) - F(%s) = %s - %s = %s$.''' 
                             % (latex(low), latex(f_low), latex(low), latex(low), latex(f_zero), latex(f_low), latex(val_int_part)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi chọn ngẫu nhiên được từ 1 đến 3 đáp án đúng
            while True:
                nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
                th_da_1 = random.choice([th_da_1_d, th_da_1_s])
                vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
                vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán danh sách lời giải (theo thứ tự các câu a, b, c, d cố định)
            solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(solutions[0]) + '\n'
                '\\item ' + str(solutions[1]) + '\n'
                '\\item ' + str(solutions[2]) + '\n'
                '\\item ' + str(solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

