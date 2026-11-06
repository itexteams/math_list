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


def bt_dang11_p2_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x, a, b, m0, n0 = symbols('x a b m_0 n_0')

            # B3-Suy nghĩ tìm cách random bài toán
            # Random các hệ số của hàm số bậc hai k*x^2 + m*x tại điểm x0
            k = random.randint(1, 3)
            m = random.randint(1, 4)
            x0 = random.randint(1, 2)

            # Hàm số f(x) = k*x^2 + m*x khi x >= x0
            f_right = k*x**2 + m*x
            val_f_x0 = k*x0**2 + m*x0  # Giá trị f(x0) và giới hạn bên phải

            # Tính toán giá trị a, b để hàm số có đạo hàm tại x0
            # 1. Liên tục: a*x0 + b = val_f_x0
            # 2. Có đạo hàm: f'(x0+) = f'(x0-) => 2*k*x0 + m = a
            val_a = 2*k*x0 + m
            val_b = val_f_x0 - val_a * x0

            # Giá trị m0, n0 tương ứng
            val_m0 = val_a
            val_n0 = val_b
            val_sum_mn = val_m0 + val_n0

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f\\left( x \\right) = \\begin{cases} %s x^2 + %s x & \\text{khi } x \\ge %s \\\\ ax + b & \\text{khi } x < %s \\end{cases}$.''' 
                             %(latex(k), latex(m), latex(x0), latex(x0)))

            ########################################################################
            # Nhận biết (a) - Giới hạn bên phải
            nb_da_1_d = '\\True $\\lim_{x \\to %s^+} f\\left( x \\right) = %s$' %(latex(x0), latex(val_f_x0))
            nb_da_1_s = '$\\lim_{x \\to %s^+} f\\left( x \\right) = %s$' %(latex(x0), latex(val_f_x0 + 1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có $\\lim_{x \\to %s^+} f\\left( x \\right) = \\lim_{x \\to %s^+} \\left( %s x^2 + %s x \\right) = %s$.'''
                            %(latex(x0), latex(x0), latex(k), latex(m), latex(val_f_x0)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu (b) - Giới hạn bên trái
            th_da_1_d = '\\True $\\lim_{x \\to %s^-} f\\left( x \\right) = %s a + b$' %(latex(x0), latex(x0) if x0 != 1 else '')
            th_da_1_s = '$\\lim_{x \\to %s^-} f\\left( x \\right) = %s a - b$' %(latex(x0), latex(x0) if x0 != 1 else '')
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Ta có $\\lim_{x \\to %s^-} f\\left( x \\right) = \\lim_{x \\to %s^-} \\left( ax + b \\right) = %s a + b$.'''
                            %(latex(x0), latex(x0), latex(x0) if x0 != 1 else ''))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng (c) - So sánh m0 và n0
            # Kiểm tra điều kiện thực tế của val_n0 và val_m0 để tạo đáp án đúng/sai
            if val_n0 > val_m0:
                vd_da_1_d = '\\True Hàm số có đạo hàm tại $x = %s$ khi $a = m_0, b = n_0$, khi đó: $n_0 > m_0$' %(latex(x0))
                vd_da_1_s = 'Hàm số có đạo hàm tại $x = %s$ khi $a = m_0, b = n_0$, khi đó: $n_0 < m_0$' %(latex(x0))
            else:
                vd_da_1_d = '\\True Hàm số có đạo hàm tại $x = %s$ khi $a = m_0, b = n_0$, khi đó: $n_0 \\le m_0$' %(latex(x0))
                vd_da_1_s = 'Hàm số có đạo hàm tại $x = %s$ khi $a = m_0, b = n_0$, khi đó: $n_0 > m_0$' %(latex(x0))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Để hàm số có đạo hàm tại $x = %s$, trước hết hàm số phải liên tục tại $x = %s$. \\\\
                            Ta có $f\\left( %s \\right) = %s$. Để hàm số liên tục thì $\\lim_{x \\to %s^-} f\\left( x \\right) = f\\left( %s \\right) \\Leftrightarrow %s a + b = %s$ (1). \\\\
                            Mặt khác, ta cần $f\'\\left( %s^+ \\right) = f\'\\left( %s^- \\right)$. \\\\
                            Ta có $f\'\\left( %s^+ \\right) = 2 \\cdot %s \\cdot %s + %s = %s$ và $f\'\\left( %s^- \\right) = a$. \\\\
                            Suy ra $a = %s$. Thay vào (1) ta được $b = %s$. \\\\
                            Vậy $m_0 = %s$ và $n_0 = %s$.'''
                            %(latex(x0), latex(x0), latex(x0), latex(val_f_x0), latex(x0), latex(x0), latex(x0) if x0 != 1 else '', latex(val_f_x0),
                              latex(x0), latex(x0), latex(x0), latex(k), latex(x0), latex(m), latex(val_m0), latex(x0), 
                              latex(val_m0), latex(val_n0), latex(val_m0), latex(val_n0)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao (d) - Tổng m0 + n0
            vdc_da_1_d = '\\True Hàm số có đạo hàm tại $x = %s$ khi $a = m_0, b = n_0$, khi đó: $n_0 + m_0 = %s$' %(latex(x0), latex(val_sum_mn))
            vdc_da_1_s = 'Hàm số có đạo hàm tại $x = %s$ khi $a = m_0, b = n_0$, khi đó: $n_0 + m_0 = %s$' %(latex(x0), latex(val_sum_mn + 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Dựa trên kết quả ở câu trên, ta có $m_0 = %s$ và $n_0 = %s$. \\\\
                            Khi đó $n_0 + m_0 = %s + %s = %s$.'''
                            %(latex(val_m0), latex(val_n0), latex(val_n0), latex(val_m0), latex(val_sum_mn)))
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

            # Gán lại và xáo trộn theo mẫu
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi (Sử dụng nhãn a) b) c) d) cho lời giải)
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

