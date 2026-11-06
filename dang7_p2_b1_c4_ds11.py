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


def bt_dang7_p2_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến n cho dãy số
            n = symbols('n')

            # B3: Suy nghĩ tìm cách random bài toán
            # Chọn A cho u_n (thường là số nguyên dương)
            A = randint(1, 10) 
            # Chọn k để tạo ra kết quả đẹp cho câu d (a^2 = k^2)
            k = randint(1, 4)
            B = -2 * (k**2) # Ví dụ: k=2 => B=-8 như trong đề mẫu

            # Biểu thức dãy số
            u_n_expr = sqrt(n**2 + A*n) - n
            v_n_expr = sqrt(n**2 + B*n) - n

            # Tính toán các giới hạn để làm lời giải đúng
            lim_u = Rational(A, 2)
            lim_v = Rational(B, 2)
            val_a = k # Nghiệm câu d là a = +/- k

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hai dãy số $(u_n)$ và $(v_n)$ với $u_n = \sqrt{n^2 + %s n} - n$ và $v_n = \sqrt{n^2 %s n} - n$.''' 
                             % (latex(A), latex(B)))

            ########################################################################
            # Nhận biết: Tính lim(u_n)
            ########################################################################
            nb_da_1_d = r'\True $\lim_{n \to +\infty} u_n = %s$' % (latex(lim_u))
            nb_da_1_s = r'$\lim_{n \to +\infty} u_n = %s$' % (latex(A)) # Sai do quên chia 2
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''$\lim_{n \to +\infty} \left( \sqrt{n^2 + %s n} - n \right) = \lim_{n \to +\infty} \frac{%s n}{\sqrt{n^2 + %s n} + n} = \lim_{n \to +\infty} \frac{%s}{\sqrt{1 + \frac{%s}{n}} + 1} = %s$.'''
                            % (latex(A), latex(A), latex(A), latex(A), latex(A), latex(lim_u)))

            ########################################################################
            # Thông hiểu: Tính lim(v_n)
            ########################################################################
            th_da_1_d = r'\True $\lim_{n \to +\infty} v_n = %s$' % (latex(lim_v))
            th_da_1_s = r'$\lim_{n \to +\infty} v_n = %s$' % (latex(B)) # Sai do quên chia 2
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (r'''$\lim_{n \to +\infty} \left( \sqrt{n^2 %s n} - n \right) = \lim_{n \to +\infty} \frac{%s n}{\sqrt{n^2 %s n} + n} = \lim_{n \to +\infty} \frac{%s}{\sqrt{1 %s \frac{%s}{n}} + 1} = %s$.'''
                            % (latex(B), latex(B), latex(B), latex(B), latex(B), latex(abs(B)), latex(lim_v)))

            ########################################################################
            # Vận dụng: Tính lim(u_n / n)
            ########################################################################
            vd_da_1_d = r'\True $\lim_{n \to +\infty} \frac{u_n}{n} = 0$'
            vd_da_1_s = r'$\lim_{n \to +\infty} \frac{u_n}{n} = %s$' % (latex(lim_u))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''$\lim_{n \to +\infty} \frac{u_n}{n} = \lim_{n \to +\infty} \frac{\sqrt{n^2 + %s n} - n}{n} = \lim_{n \to +\infty} \left( \sqrt{1 + \frac{%s}{n}} - 1 \right) = 0$.'''
                            % (latex(A), latex(A)))

            ########################################################################
            # Vận dụng cao: Tìm a để lim(v_n + a^2) = 0
            ########################################################################
            vdc_da_1_d = r'\True $\lim_{n \to +\infty} (v_n + a^2) = 0 \Leftrightarrow a = \pm %s$' % (latex(val_a))
            vdc_da_1_s = r'$\lim_{n \to +\infty} (v_n + a^2) = 0 \Leftrightarrow a = \pm %s$' % (latex(val_a**2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''$\lim_{n \to +\infty} (v_n + a^2) = \lim_{n \to +\infty} v_n + a^2 = %s + a^2$. \\
            Để $\lim_{n \to +\infty} (v_n + a^2) = 0 \Leftrightarrow %s + a^2 = 0 \Leftrightarrow a^2 = %s \Leftrightarrow a = \pm %s$.'''
                             % (latex(lim_v), latex(lim_v), latex(-lim_v), latex(val_a)))

            # --- Phần điều kiện số đáp án đúng (từ 1 đến 3) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    break

            # Xuất nội dung theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

