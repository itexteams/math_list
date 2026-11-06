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


def bt_dang34_p1_b1_c2_hh12(self):
            # Khai báo biến
            def get_random_coeffs():
                coeffs_pool = [-3, -2, -4, 4, 2, 3,-5,5]
                return random.sample(coeffs_pool, 3)

            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo các vectơ pháp tuyến ngẫu nhiên
                n_P = get_random_coeffs()
                n_Q = get_random_coeffs()

                # Tạo các hằng số ngẫu nhiên
                d_P = random.randint(-5, 5)
                d_Q = random.randint(-5, 5)

                # Tính toán các giá trị cần thiết
                dot_product = n_P[0] * n_Q[0] + n_P[1] * n_Q[1] + n_P[2] * n_Q[2]
                abs_dot_product = abs(dot_product)

                mag_n_P = sqrt(n_P[0]**2 + n_P[1]**2 + n_P[2]**2)
                mag_n_Q = sqrt(n_Q[0]**2 + n_Q[1]**2 + n_Q[2]**2)

                cos_alpha_val = abs_dot_product / (mag_n_P * mag_n_Q)

                # Chuẩn bị đáp án và các đáp án sai
                # Sửa lỗi: Không dùng Rational vì cos_alpha_val có thể là số vô tỉ
                kq = latex(cos_alpha_val).replace('.',',')
                da = '$%s$' % (kq)

                # Các đáp án trắc nghiệm sai
                s = [
                    '$%s$' % (latex(cos_alpha_val + Rational(1, 10))),
                    '$%s$' % (latex(cos_alpha_val - Rational(1, 10))),
                    '$%s$' % (latex(cos_alpha_val + Rational(1, 5))),
                    '$%s$' % (latex(cos_alpha_val - Rational(1, 5))),
                    '$%s$' % (latex(abs_dot_product / (mag_n_P * mag_n_Q + 1))),
                    '$%s$' % (latex(abs_dot_product / (mag_n_P * mag_n_Q - 1)))
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong không gian $Oxyz$, gọi $\\alpha$ là góc giữa hai mặt phẳng $(P): %sx + %sy + %sz + %s = 0$ và $(Q): %sx + %sy + %sz + %s = 0$. Giá trị $\\cos \\alpha$ là''' % (latex(n_P[0]), latex(n_P[1]), latex(n_P[2]), latex(d_P), latex(n_Q[0]), latex(n_Q[1]), latex(n_Q[2]), latex(d_Q)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Mặt phẳng $(P)$ có vectơ pháp tuyến $\\overrightarrow{n}_P=(%s; %s; %s)$. \\\\
            Mặt phẳng $(Q)$ có vectơ pháp tuyến $\\overrightarrow{n}_Q=(%s; %s; %s)$. \\\\
            Ta có $\\cos \\alpha = \\frac{|\\overrightarrow{n}_P \\cdot \\overrightarrow{n}_Q|}{|\\overrightarrow{n}_P| \\cdot |\\overrightarrow{n}_Q|} = \\frac{|(%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s)|}{\\sqrt{%s^2 + (%s)^2 + (%s)^2} \\cdot \\sqrt{%s^2 + (%s)^2 + %s^2}} = \\frac{%s}{%s \\cdot %s} =$ %s.'''
                        % (latex(n_P[0]), latex(n_P[1]), latex(n_P[2]),
                           latex(n_Q[0]), latex(n_Q[1]), latex(n_Q[2]),
                           latex(n_P[0]), latex(n_Q[0]), latex(n_P[1]), latex(n_Q[1]), latex(n_P[2]), latex(n_Q[2]),
                           latex(n_P[0]), latex(n_P[1]), latex(n_P[2]),
                           latex(n_Q[0]), latex(n_Q[1]), latex(n_Q[2]),
                           abs_dot_product, latex(mag_n_P), latex(mag_n_Q), da))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content

