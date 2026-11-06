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


def bt_dang18_p2_b1_c3_ds12(self):
            # Khai báo biến
            # Khởi tạo các số ngẫu nhiên để biến đổi bài toán
            k = random.randint(2, 9)      # Hệ số cho câu a
            m = random.randint(2, 9)      # Hệ số cho câu b
            n = random.randint(2, 6)      # Hệ số tử số câu c
            p = random.randint(2, 9)      # Hệ số tự do câu c
            a_coeff = random.randint(2, 5) # Hệ số sin câu d
            b_coeff = random.randint(2, 5) # Hệ số 1/x câu d

            # Nội dung câu hỏi gốc (giữ nguyên yêu cầu xét tính đúng sai)
            noidungcauhoi = r'''Xét tính đúng sai của các mệnh đề sau về nguyên hàm.'''

            ########################################################################
            # a) Nhận biết: Nguyên hàm cos(kx)
            ########################################################################
            # Đáp án
            nb_da_1_d = r'\True $\int %s\cos x \, \text{d}x = %s\sin x + C$' % (k, k)
            nb_da_1_s = r'$\int %s\cos x \, \text{d}x = %s\sin x + C$' % (k, -k)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Lời giải
            loigiai_nb_1 = r'Ta có $\int %s\cos x \, \text{d}x = %s\sin x + C$.' % (k, k)

            ########################################################################
            # b) Thông hiểu: Nguyên hàm m/x
            ########################################################################
            # Đáp án
            th_da_1_d = r'\True $\int \frac{%s}{x} \, \text{d}x = %s \ln|x| + C$' % (m, m)
            th_da_1_s = r'$\int \frac{%s}{x} \, \text{d}x = %s \ln x + C$' % (m, m) # Thiếu trị tuyệt đối
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Lời giải
            loigiai_th_1 = r'$\int \frac{%s}{x} \, \text{d}x = %s \int \frac{1}{x} \, \text{d}x = %s \ln|x| + C$.' % (m, m, m)

            ########################################################################
            # c) Vận dụng: Nguyên hàm (nx + p)/x
            ########################################################################
            # Đáp án
            vd_da_1_d = r'\True $\int \frac{%sx + %s}{x} \, \text{d}x = %sx + %s \ln|x| + C$' % (n, p, n, p)
            vd_da_1_s = r'$\int \frac{%sx + %s}{x} \, \text{d}x = %s + %s \ln|x| + C$' % (n, p, n, p) # Sai vì thiếu x ở số hạng đầu
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Lời giải
            loigiai_vd_1 = r'$\int \frac{%sx + %s}{x} \, \text{d}x = \int \left( %s + \frac{%s}{x} \right) \text{d}x = %sx + %s \ln|x| + C$.' % (n, p, n, p, n, p)

            ########################################################################
            # d) Vận dụng cao: Tổng hợp sinx và 1/x
            ########################################################################
            # Đáp án
            vdc_da_1_d = r'\True $\int \left( %s \sin x + \frac{%s}{x} \right) \text{d}x = -%s \cos x + %s \ln|x| + C$' % (a_coeff, b_coeff, a_coeff, b_coeff)
            vdc_da_1_s = r'$\int \left( %s \sin x + \frac{%s}{x} \right) \text{d}x = %s \cos x + %s \ln|x| + C$' % (a_coeff, b_coeff, a_coeff, b_coeff) # Sai dấu cos
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Lời giải
            loigiai_vdc_1 = r'$\int %s \sin x \, \text{d}x = -%s \cos x + C$ và $\int \frac{%s}{x} \, \text{d}x = %s \ln|x| + C$.' % (a_coeff, a_coeff, b_coeff, b_coeff)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chọn ngẫu nhiên các mệnh đề đúng/sai (đảm bảo có 1-3 câu đúng)
            while True:
                choice_nb = random.choice(list_nb_da_1)
                choice_th = random.choice(list_th_da_1)
                choice_vd = random.choice(list_vd_da_1)
                choice_vdc = random.choice(list_vdc_da_1)

                current_answers = [choice_nb, choice_th, choice_vd, choice_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất nội dung theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(choice_nb) + '}\n'
                '{' + str(choice_th) + '}\n'
                '{' + str(choice_vd) + '}\n'
                '{' + str(choice_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

