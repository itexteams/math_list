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


def bt_dang9_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Ngẫu nhiên hóa giá trị m (trong hình là số 2)
            # Chọn m để biểu thức đẹp, ví dụ m từ 2 đến 5
            m = random.randint(2, 5)
            k = 2 # Giữ hệ số x là 2 để giống hệt cấu trúc nguyên hàm x^2 trong ảnh
            f_x = exp(x) - k*x

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x)=e^x-%s x$ và $F(x)$ là một nguyên hàm của $f(x)$ trên $\mathbb{R}$.''' 
                             % (k))

            ########################################################################
            # a) Nhận biết: Kiểm tra đạo hàm tại điểm m
            ########################################################################
            val_fm = exp(m) - k*m
            nb_da_1_d = r'''\True $F'(%s) = f(%s) = e^{%s} - %s$''' % (m, m, m, k*m)
            nb_da_1_s = r'''$F'(%s) = f'(%s) = e^{%s} - %s$''' % (m, m, m, k) # Sai vì nhầm sang f'(x)

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = r'''Ta có $F'(x) = f(x), \forall x \in \mathbb{R} \Rightarrow F'(%s) = f(%s) = e^{%s} - %s$.''' % (m, m, m, k*m)

            ########################################################################
            # b) Thông hiểu: Nguyên hàm cơ bản
            ########################################################################
            # Nguyên hàm là e^x - x^2 + C
            th_da_1_d = r'\True $\int f(x) \text{d}x = e^x - x^2 + C$'
            th_da_1_s = r'$\int f(x) \text{d}x = e^x - 2x^2 + C$' # Sai hệ số

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = r'''$\int f(x) \text{d}x = \int (e^x - 2x) \text{d}x = e^x - x^2 + C$.'''

            ########################################################################
            # c) Vận dụng: Tích phân xác định
            ########################################################################
            # Tích phân từ 0 đến m: (e^m - m^2) - (e^0 - 0) = e^m - m^2 - 1
            tp_result = exp(m) - m**2 - 1
            vd_da_1_d = r'\True $\int_{0}^{%s} f(x) \text{d}x = e^{%s} - %s$' % (m, m, m**2 + 1)
            vd_da_1_s = r'$\int_{0}^{%s} f(x) \text{d}x = e^{%s} - %s$' % (m, m, m**2) # Sai vì quên -1

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = (r'''$\int_{0}^{%s} f(x) \text{d}x = (e^x - x^2) \Big|_0^{%s} = (e^{%s} - %s) - (e^0 - 0) = e^{%s} - %s$.''' 
                            % (m, m, m, m**2, m, m**2 + 1))

            ########################################################################
            # d) Vận dụng cao: Diện tích hình phẳng
            ########################################################################
            # Với f(x) = e^x - 2x, hàm luôn dương trên các đoạn [0, m] (m>0)
            vdc_da_1_d = r'\True Diện tích hình phẳng $(H)$ giới hạn bởi đồ thị hàm số $y=f(x)$, trục hoành và hai đường thẳng $x=0, x=%s$ bằng $e^{%s} - %s$' % (m, m, m**2 + 1)
            vdc_da_1_s = r'Diện tích hình phẳng $(H)$ giới hạn bởi đồ thị hàm số $y=f(x)$, trục hoành và hai đường thẳng $x=0, x=%s$ bằng $e^{%s} + %s$' % (m, m, m**2 + 1)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = (r'''$S = \int_{0}^{%s} |f(x)| \text{d}x = \int_{0}^{%s} |e^x - 2x| \text{d}x = e^{%s} - %s$.''' 
                             % (m, m, m, m**2 + 1))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số lượng đáp án đúng từ 1 đến 3
            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

