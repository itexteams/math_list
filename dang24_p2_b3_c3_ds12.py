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


def bt_dang24_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1-Nghiên cứu: 
            # Hàm số có dạng f(x) = -x^2 + a^2
            # Giao điểm Ox: x = a và x = -a
            # Thể tích: V = pi * tích phân từ -a đến a của (-x^2 + a^2)^2 dx
            # V = 16*a^5*pi / 15

            # B3-Suy nghĩ tìm cách random: Chọn ngẫu nhiên a trong khoảng [1, 3]
            a_val = random.randint(1, 3)
            m_val = a_val**2
            f_x = -x**2 + m_val

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x) = %s$.''' % (latex(f_x)))

            ########################################################################
            # Nhận biết: Phương trình hoành độ giao điểm
            nb_da_1_d = r'\True Hoành độ giao điểm của đồ thị hàm số $y=f(x)$ và $Ox$ là nghiệm của phương trình $f(x)=0$'
            nb_da_1_s = r'''Hoành độ giao điểm của đồ thị hàm số $y=f(x)$ và $Ox$ là nghiệm của phương trình $f'(x)=0$'''
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'Hoành độ giao điểm của đồ thị với trục hoành là nghiệm phương trình $f(x)=0 \Leftrightarrow -x^2 + %s = 0$.' % (m_val)

            ########################################################################
            # Thông hiểu: Số điểm cắt trục hoành
            th_da_1_d = r'\True Đồ thị hàm số cắt trục hoành tại hai điểm phân biệt'
            th_da_1_s = r'Đồ thị hàm số cắt trục hoành tại một điểm duy nhất'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r'Phương trình $-x^2 + %s = 0 \Leftrightarrow x = \pm %s$, nên đồ thị cắt $Ox$ tại hai điểm.' % (m_val, a_val)

            ########################################################################
            # Vận dụng: Công thức thể tích (Lưu ý dùng \text{d}x)
            formula_correct = r'V = \pi \int_{-%s}^{%s} \left( %s \right)^2 \text{d}x' % (a_val, a_val, latex(f_x))
            formula_wrong = r'V = \pi \int_{-%s}^{%s} \left( %s \right) \text{d}x' % (a_val, a_val, latex(f_x))

            vd_da_1_d = r'\True Nếu $D$ là hình phẳng giới hạn bởi đồ thị và trục $Ox$ thì thể tích khối tròn xoay khi quay $D$ quanh $Ox$ là $%s$' % (formula_correct)
            vd_da_1_s = r'Nếu $D$ là hình phẳng giới hạn bởi đồ thị và trục $Ox$ thì thể tích khối tròn xoay khi quay $D$ quanh $Ox$ là $%s$' % (formula_wrong)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'Công thức tính thể tích khối tròn xoay quay quanh trục $Ox$ là $V = \pi \int_{a}^{b} [f(x)]^2 \text{d}x$.'

            ########################################################################
            # Vận dụng cao: Giá trị thể tích cụ thể
            v_calc = Rational(16 * a_val**5, 15)
            v_latex = r'\frac{%s\pi}{15}' % (16 * a_val**5) if (16 * a_val**5) % 15 != 0 else r'%s\pi' % (16 * a_val**5 // 15)

            vdc_da_1_d = r'\True Thể tích khối tròn xoay thu được có giá trị là $V = %s$' % v_latex
            vdc_da_1_s = r'Thể tích khối tròn xoay thu được có giá trị là $V = \frac{%s\pi}{15}$' % (8 * a_val**5) # Sai hệ số
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r'Ta có $V = \pi \int_{-%s}^{%s} (-x^2 + %s)^2 \text{d}x = \pi \int_{-%s}^{%s} (x^4 - %sx^2 + %s) \text{d}x = %s$.' % (a_val, a_val, m_val, a_val, a_val, 2*m_val, m_val**2, v_latex)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chọn bộ đáp án thỏa mãn 1-3 câu đúng
            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất kết quả theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + ans_nb + '}\n'
                '{' + ans_th + '}\n'
                '{' + ans_vd + '}\n'
                '{' + ans_vdc + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

