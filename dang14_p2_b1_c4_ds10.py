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


def bt_dang14_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 3: Suy nghĩ tìm cách random bài toán
            # Random hệ số m để hàm số có dạng f(x) = (x - m)/(x + m)
            m = random.randint(1, 5)
            tu = x - m
            mau = x + m
            f_x = tu / mau

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x) = %s$.''' % (latex(f_x)))

            ########################################################################
            # a) Nhận biết: Tính f(0)
            f0_val = f_x.subs(x, 0)
            nb_da_1_d = r'\True $f(0) = %s$' % (latex(f0_val))
            nb_da_1_s = r'$f(0) = %s$' % (latex(m))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''$f(0) = \frac{0 - %s}{0 + %s} = %s$.''' % (m, m, latex(f0_val)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # b) Thông hiểu: Tập xác định
            th_da_1_d = r'Tập xác định $\mathscr{D} = (-\infty; -%s)$' % (m) # Sai (thiếu khoảng)
            th_da_1_s = r'\True Tập xác định $\mathscr{D} = \mathbb{R} \setminus \{-%s\}$' % (m)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Điều kiện $x + %s \neq 0 \Leftrightarrow x \neq -%s$. Vậy $\mathscr{D} = (-\infty; -%s) \cup (-%s; +\infty)$.''' 
                            % (m, m, m, m))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # c) Vận dụng: Tính đơn điệu
            vd_da_1_d = r'\True Hàm số đồng biến trên từng khoảng xác định'
            vd_da_1_s = r'Hàm số đồng biến trên $(-\infty; %s)$' % (m)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Với $x_1, x_2 \in \mathscr{D}$ sao cho $x_1 \neq x_2$. Xét biểu thức $M = \frac{f(x_1) - f(x_2)}{x_1 - x_2} = \frac{%s}{(x_1 + %s)(x_2 + %s)}$. Với mọi $x_1, x_2$ cùng thuộc một khoảng xác định thì $(x_1 + %s)(x_2 + %s) > 0$ nên hàm số đồng biến trên từng khoảng $(-\infty; -%s)$ và $(-%s; +\infty)$.''' 
                            % (2*m, m, m, m, m, m, m))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # d) Vận dụng cao: Giá trị nguyên
            vdc_da_1_d = r'\True Tồn tại các số nguyên $x$ để $f(x)$ là số nguyên'
            vdc_da_1_s = r'Tồn tại 10 số nguyên $x$ để $f(x)$ là số nguyên'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''$f(x) = \frac{x + %s - %s}{x + %s} = 1 - \frac{%s}{x + %s} \in \mathbb{Z}$ khi $x + %s$ là ước nguyên của %s. Vậy tồn tại các giá trị nguyên $x$ để $f(x)$ nguyên.''' 
                             % (m, 2*m, m, 2*m, m, m, 2*m))
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
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list để xử lý shuffle giống mẫu
            shuffled_answers_nb, shuffled_solutions_nb = [nb_da_1], [loigiai_nb_1]
            shuffled_answers_th, shuffled_solutions_th = [th_da_1], [loigiai_th_1]
            shuffled_answers_vd, shuffled_solutions_vd = [vd_da_1], [loigiai_vd_1]
            shuffled_answers_vdc, shuffled_solutions_vdc = [vdc_da_1], [loigiai_vdc_1]

            # Xuất câu hỏi với đáp án và lời giải đúng mẫu content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' 
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

