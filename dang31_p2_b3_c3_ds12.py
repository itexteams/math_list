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


def bt_dang31_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Nghiên cứu đề bài và tạo biến ngẫu nhiên
            # Trong đề bài mẫu, hệ số k = 2. Ta cho k chạy ngẫu nhiên từ 2 đến 5.
            k = random.randint(2, 5)

            f1 = k * x
            f2 = k * x**2 - 4 * k * x + 4 * k # Tương đương k(x-2)^2

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x)=\begin{cases} %s &\text{khi } x \leq 1 \\ %s &\text{khi } x > 1 \end{cases}$. Gọi $(H)$ là hình phẳng giới hạn bởi đồ thị hàm số $f(x)$ và trục hoành.''' 
                             % (latex(f1), latex(f2)))

            ########################################################################
            # a) Nhận biết: Giao điểm với trục Ox
            ########################################################################
            # Giao điểm: x=0 (thuộc khoảng <=1) và x=2 (thuộc khoảng >1) -> 2 điểm
            nb_da_1_d = r'\True Đồ thị hàm số cắt trục $Ox$ tại $2$ điểm phân biệt.'
            nb_da_1_s = r'Đồ thị hàm số cắt trục $Ox$ tại $3$ điểm phân biệt.'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''Với $x \leq 1, %s = 0 \Leftrightarrow x=0$ (nhận). \\
                            Với $x > 1, %s = 0 \Leftrightarrow x=2$ (nhận). \\
                            Vậy đồ thị cắt trục hoành tại 2 điểm phân biệt.''' % (latex(f1), latex(f2)))

            ########################################################################
            # b) Thông hiểu: Tích phân từ -2 đến 2
            ########################################################################
            val_tp = integrate(f1, (x, -2, 1)) + integrate(f2, (x, 1, 2))
            th_da_1_d = r'\True $\int_{-2}^{2} f(x) \text{d}x = %s$.' % (latex(val_tp))
            th_da_1_s = r'$\int_{-2}^{2} f(x) \text{d}x = %s$.' % (latex(-val_tp))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (r'''Ta có $\int_{-2}^{2} f(x) \text{d}x = \int_{-2}^{1} (%s) \text{d}x + \int_{1}^{2} (%s) \text{d}x = %s$.''' 
                            % (latex(f1), latex(f2), latex(val_tp)))

            ########################################################################
            # c) Vận dụng: Diện tích hình phẳng (H)
            ########################################################################
            # Diện tích giới hạn bởi f(x) và Ox từ x=0 đến x=2
            val_S = integrate(f1, (x, 0, 1)) + integrate(f2, (x, 1, 2))
            vd_da_1_d = r'\True Diện tích hình phẳng $(H)$ bằng $S = \int_{0}^{1} %s \text{d}x + \int_{1}^{2} (%s) \text{d}x = %s$.' % (latex(f1), latex(f2), latex(val_S))
            vd_da_1_s = r'Diện tích hình phẳng $(H)$ bằng $S = \int_{0}^{1} %s \text{d}x + \int_{1}^{2} (%s) \text{d}x = %s$.' % (latex(f1), latex(f2), latex(val_S + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''Hình phẳng $(H)$ giới hạn bởi đồ thị và trục hoành nên cận từ $0$ đến $2$. \\
                            $S = \int_{0}^{1} |%s| \text{d}x + \int_{1}^{2} |%s| \text{d}x = %s$.''' 
                            % (latex(f1), latex(f2), latex(val_S)))

            ########################################################################
            # d) Vận dụng cao: Thể tích khối tròn xoay
            ########################################################################
            val_V = pi * (integrate(f1**2, (x, 0, 1)) + integrate(f2**2, (x, 1, 2)))
            vdc_da_1_d = r'\True Thể tích khối tròn xoay thu được khi quay $(H)$ quanh trục $Ox$ là $V = %s$.' % (latex(val_V))
            vdc_da_1_s = r'Thể tích khối tròn xoay thu được khi quay $(H)$ quanh trục $Ox$ là $V = \frac{8\pi}{3}$.' # Giá trị sai lấy từ ảnh gốc
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Thể tích vật thể tròn xoay: \\
                             $V = \pi \int_{0}^{1} (%s)^2 \text{d}x + \pi \int_{1}^{2} (%s)^2 \text{d}x = %s$.''' 
                             % (latex(f1), latex(f2), latex(val_V)))

            # --- Xử lý logic chọn đáp án Đúng/Sai để đảm bảo có từ 1-3 câu đúng ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    break

            # Gán kết quả cuối cùng
            shuffled_answers = [d1, d2, d3, d4]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo mẫu LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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

