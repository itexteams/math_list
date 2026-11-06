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


def bt_dang32_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khởi tạo biến
            x = symbols('x')

            # B1: Random thông số bài toán
            # f(x) = sqrt(x-1) + k khi x >= 1
            # f(x) = (x^2 - m) / (x+n) khi x < 1
            k = random.randint(1, 5) # Trong ảnh k = 2
            m = random.randint(2, 6) # Trong ảnh m = 4
            n = 1                    # Giữ n=1 để có điểm không xác định tại x = -1

            # Hàm số hiển thị trong đề bài
            f_tren = sqrt(x - 1) + k
            f_duoi = (x**2 - m) / (x + n)

            noidungcauhoi = r'''Cho hàm số $y = f(x) = \begin{cases} %s & \text{khi } x \ge 1 \\ %s & \text{khi } x < 1 \end{cases}$.''' % (latex(f_tren), latex(f_duoi))

            ########################################################################
            # Nhận biết: Kiểm tra tính xác định tại x = 2
            ########################################################################
            val_x2 = 2
            nb_da_1_d = r'\True Với $x \ge 1$ thì hàm số $f(x) = %s$ xác định nên hàm số xác định tại $x = %s$' % (latex(f_tren), val_x2)
            nb_da_1_s = r'Với $x \ge 1$ thì hàm số $f(x) = %s$ không xác định tại $x = %s$' % (latex(f_tren), val_x2)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''Với $x \ge 1$ thì hàm số $f(x) = \sqrt{x-1} + %s$ xác định với mọi $x \ge 1$, do đó hàm số xác định tại $x = 2$.''' % (k)
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Kiểm tra điểm A(1; y)
            ########################################################################
            f_1 = k # f(1) = sqrt(1-1) + k = k
            y_sai = Rational(-3, 2)
            th_da_1_d = r'\True Ta có $f(1) = %s$ nên điểm $A\left( 1; %s \right)$ không thuộc đồ thị hàm số' % (f_1, latex(y_sai))
            th_da_1_s = r'Ta có $f(1) = %s$ nên điểm $A\left( 1; %s \right)$ thuộc đồ thị hàm số' % (f_1, f_1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''Ta có $f(1) = \sqrt{1-1} + %s = %s$. Vì $f(1) \neq %s$ nên điểm $A\left( 1; %s \right)$ không thuộc đồ thị hàm số.''' % (k, f_1, latex(y_sai), latex(y_sai))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Điểm không xác định
            ########################################################################
            vd_da_1_d = r'\True Với $x < 1$ hàm số $f(x) = %s$ không xác định tại $x = -1$' % (latex(f_duoi))
            vd_da_1_s = r'\True Với $x < 1$ hàm số $f(x) = %s$ xác định tại mọi $x < 1$' % (latex(f_duoi)) # Đánh dấu \True giả để logic xáo trộn bên dưới
            # Chỉnh lại logic đúng/sai thực tế
            vd_da_1_s = vd_da_1_s.replace(r'\True ', '') 

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'''Với $x < 1$ hàm số $f(x) = \frac{x^2 - %s}{x + 1}$ có mẫu số bằng $0$ khi $x = -1$ (thỏa mãn $x < 1$), nên hàm số không xác định tại $x = -1$.''' % (m)
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Tính tổng f(0) + f(2)
            ########################################################################
            f_0 = -m # (0^2 - m) / (0 + 1) = -m
            f_2 = 1 + k # sqrt(2-1) + k = 1 + k
            tong = f_0 + f_2

            vdc_da_1_d = r'\True $f(0) + f(2) = %s$' % (tong)
            vdc_da_1_s = r'$f(0) + f(2) = %s$' % (tong + random.randint(1, 3))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''Ta có $f(0) = \frac{0^2 - %s}{0 + 1} = -%s$ và $f(2) = \sqrt{2-1} + %s = %s$. Do đó $f(0) + f(2) = -%s + %s = %s$.''' % (m, m, k, f_2, m, f_2, tong)
            list_vdc_2 = [loigiai_vdc_1]

            # --- Phần Logic xáo trộn và xuất nội dung (Giữ đúng mẫu) ---

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Đóng gói để in
            shuffled_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
            shuffled_solutions = [list_nb_2[0], list_th_2[0], list_vd_2[0], list_vdc_2[0]]

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

