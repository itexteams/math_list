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


def bt_dang5_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Nghiên cứu đề bài và thiết lập thông số ngẫu nhiên
            # Chọn hai nghiệm m, n là số nguyên dương để đảm bảo tính chất giống trong ảnh
            m = random.randint(1, 2)
            n = m + random.randint(1, 2) # Để n luôn lớn hơn m (giống 2 và 3 trong ảnh)

            # Tam thức f(x) = -x^2 + (m+n)x - m*n
            a_coeff = -1
            b_coeff = m + n
            c_coeff = -m * n
            f_x = a_coeff*x**2 + b_coeff*x + c_coeff

            # Các giá trị tính toán cho lời giải
            delta = b_coeff**2 - 4*a_coeff*c_coeff
            k_solutions = n**2 - m**2 + 1 # Số nghiệm tự nhiên cho câu d
            test_val = m - 1 # Một giá trị để kiểm tra câu c

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tam thức bậc hai $f(x)=%s$.''' 
                             %(latex(f_x)))

            ########################################################################
            # Nhận biết (Câu a) ############################################
            nb_da_1_d = 'Vì $a = %s < 0$ và $\\Delta = %s > 0$ nên $f(x)$ không thể luôn âm với mọi $x \\in \\mathbb{R}$' % (latex(a_coeff), latex(delta))
            nb_da_1_s = 'Vì $a = %s < 0$ nên $f(x)$ có giá trị âm với mọi $x \\in \\mathbb{R}$' % (latex(a_coeff))

            list_nb_da_1 = [nb_da_1_s] # Giữ nguyên khẳng định sai như trong đề bài gốc
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Tam thức bậc hai $f(x)$ có $a=%s < 0$ và $\\Delta = %s^2 - 4(%s)(%s) = %s > 0$. \\\\
                            Do $\\Delta > 0$ nên tam thức có hai nghiệm phân biệt $x_1 = %s, x_2 = %s$. \\\\
                            Vậy khẳng định $f(x) < 0$ với mọi $x \\in \\mathbb{R}$ là sai (vì $f(x) > 0$ trong khoảng hai nghiệm).'''
                            %(latex(a_coeff), latex(b_coeff), latex(a_coeff), latex(c_coeff), latex(delta), latex(m), latex(n)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            th_da_1_d = '\\True $f(x)$ không âm nếu $x \\in (%s; %s)$' % (latex(m), latex(n))
            th_da_1_s = '$f(x)$ không âm nếu $x \\in (-\\infty; %s)$' % (latex(m))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Dựa vào quy tắc xét dấu tam thức bậc hai: "Trong trái, ngoài cùng". \\\\
                            Với $a = %s < 0$, $f(x) \\geq 0$ khi $x$ nằm trong đoạn giữa hai nghiệm $[%s; %s]$. \\\\
                            Do đó, trên khoảng $(%s; %s)$, $f(x)$ luôn nhận giá trị dương (không âm).'''
                            %(latex(a_coeff), latex(m), latex(n), latex(m), latex(n)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng (Câu c) ############################################
            vd_da_1_d = '\\True $f(x) < 0$ nếu $x \\in (%s; %s)$' % (latex(test_val - 1), latex(test_val))
            vd_da_1_s = '$f(x) < 0$ nếu $x \\in (%s; %s)$' % (latex(m), latex(n))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Khoảng hai nghiệm là $(%s; %s)$. Với $x < %s$ hoặc $x > %s$ thì $f(x) < 0$. \\\\
                            Vì khoảng $(%s; %s)$ nằm hoàn toàn bên ngoài khoảng hai nghiệm nên $f(x) < 0$ trên khoảng này.'''
                            %(latex(m), latex(n), latex(m), latex(n), latex(test_val - 1), latex(test_val)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            vdc_da_1_d = '\\True Tập nghiệm của bất phương trình $f(\\sqrt{x}) \\geq 0$ có %s nghiệm tự nhiên' % (latex(k_solutions))
            vdc_da_1_s = 'Tập nghiệm của bất phương trình $f(\\sqrt{x}) \\geq 0$ có %s nghiệm tự nhiên' % (latex(k_solutions + 1))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xét bất phương trình $f(\\sqrt{x}) \\geq 0$. Điều kiện: $x \\geq 0$. \\\\
                             Đặt $t = \\sqrt{x} \\geq 0$, ta có $f(t) \\geq 0 \\Leftrightarrow -t^2 + %st - %s \\geq 0$. \\\\
                             Giải bất phương trình bậc hai ta được: $%s \\leq t \\leq %s$. \\\\
                             Suy ra $%s \\leq \\sqrt{x} \\leq %s \\Leftrightarrow %s \\leq x \\leq %s$. \\\\
                             Các nghiệm tự nhiên là: $x \\in \\{%s, \\dots, %s\\}$. \\\\
                             Số nghiệm tự nhiên là: $%s - %s + 1 = %s$ nghiệm.'''
                             %(latex(b_coeff), latex(abs(c_coeff)), latex(m), latex(n), latex(m), latex(n), latex(m**2), latex(n**2),
                               latex(m**2), latex(n**2), latex(n**2), latex(m**2), latex(k_solutions)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Logic xáo trộn và xuất nội dung (B2)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            shuffled_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

