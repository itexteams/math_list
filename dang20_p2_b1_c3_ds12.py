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


def bt_dang20_p2_b1_c3_ds12(self):
            # Khai báo biến
            # ==================== KHAI BÁO BIẾN NGẪU NHIÊN ====================
            a_val = random.randint(2, 5) # Hệ số cho câu a
            k_c = random.randint(2, 4)   # Hằng số tự do cho câu c
            m_c = random.randint(2, 5)   # Hệ số cho 1/x^2 câu c
            n_d = random.randint(2, 5)   # Hệ số cho câu d

            # Nội dung câu hỏi tổng quát
            noidungcauhoi = r'''Xét tính đúng sai của các mệnh đề sau về nguyên hàm.'''

            # ==================== NHẬN BIẾT (Câu a) ====================
            nb_da_1_d = r'\True $\int %s e^x \text{d}x = %s e^x + C$' % (latex(a_val), latex(a_val))
            nb_da_1_s = r'$\int %s e^x \text{d}x = e^x + C$' % (latex(a_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'''Ta có $\int %s e^x \text{d}x = %s \int e^x \text{d}x = %s e^x + C$.''' % (latex(a_val), latex(a_val), latex(a_val))
            list_nb_2 = [loigiai_nb_1]

            # ==================== THÔNG HIỂU (Câu b) ====================
            # Chỉ hiển thị: Nguyên hàm = Kết quả cuối
            th_da_1_d = r'\True $\int \sin \frac{x}{2} \cdot \cos \frac{x}{2} \text{d}x = -\frac{1}{2} \cos x + C$'
            th_da_1_s = r'$\int \sin \frac{x}{2} \cdot \cos \frac{x}{2} \text{d}x = -\cos x + C$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r'''Sử dụng công thức nhân đôi: $\sin \frac{x}{2} \cos \frac{x}{2} = \frac{1}{2} \sin x$. \\ 
            Khi đó $\int \sin \frac{x}{2} \cos \frac{x}{2} \text{d}x = \frac{1}{2} \int \sin x \text{d}x = -\frac{1}{2} \cos x + C$.'''
            list_th_2 = [loigiai_th_1]

            # ==================== VẬN DỤNG (Câu c) ====================
            # Chỉ hiển thị: Nguyên hàm = Kết quả cuối
            ket_qua_c = r'x - %s \ln |x| - \frac{%s}{x}' % (latex(k_c), latex(m_c))
            ket_qua_c_sai = r'x - %s \ln |x| + \frac{%s}{x}' % (latex(k_c), latex(m_c))

            vd_da_1_d = r'\True $\int \frac{x^2 - %s x + %s}{x^2} \text{d}x = %s + C$' % (latex(k_c), latex(m_c), ket_qua_c)
            vd_da_1_s = r'$\int \frac{x^2 - %s x + %s}{x^2} \text{d}x = %s + C$' % (latex(k_c), latex(m_c), ket_qua_c_sai)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'''Ta tách phân thức: $\frac{x^2 - %s x + %s}{x^2} = 1 - \frac{%s}{x} + \frac{%s}{x^2}$. \\
            Nguyên hàm thu được là: $x - %s \ln |x| - \frac{%s}{x} + C$.''' % (latex(k_c), latex(m_c), latex(k_c), latex(m_c), latex(k_c), latex(m_c))
            list_vd_2 = [loigiai_vd_1]

            # ==================== VẬN DỤNG CAO (Câu d) ====================
            # Chỉ hiển thị: Nguyên hàm = Kết quả cuối
            n_minus_1 = n_d - 1

            vdc_da_1_d = r'\True $\int (%s + \cot^2 x) \text{d}x = %s x - \cot x + C$' % (latex(n_d), latex(n_minus_1))
            vdc_da_1_s = r'$\int (%s + \cot^2 x) \text{d}x = %s x - \cot x + C$' % (latex(n_d), latex(n_d))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r'''Ta có hằng đẳng thức $1 + \cot^2 x = \frac{1}{\sin^2 x} \Rightarrow \cot^2 x = \frac{1}{\sin^2 x} - 1$. \\
            Khi đó: $\int (%s + \cot^2 x) \text{d}x = \int (%s + \frac{1}{\sin^2 x} - 1) \text{d}x = \int (%s + \frac{1}{\sin^2 x}) dx = %s x - \cot x + C$.''' % (latex(n_d), latex(n_d), latex(n_minus_1), latex(n_minus_1))
            list_vdc_2 = [loigiai_vdc_1]

            # ==================== KIỂM TRA ĐIỀU KIỆN ĐÚNG/SAI ====================
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Xuất nội dung theo mẫu LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

