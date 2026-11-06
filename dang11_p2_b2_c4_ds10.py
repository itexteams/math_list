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


def bt_dang11_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Để đảm bảo hình dáng giống bài mẫu, ta chọn a > 0 và Parabol có 2 nghiệm phân biệt
            x = symbols('x')
            a = 1 
            # Chọn đỉnh x_I = -b/(2a) là số nguyên để lời giải đẹp
            x_I = random.randint(1, 4)
            b = -2 * a * x_I
            # Chọn c sao cho delta > 0 (có 2 nghiệm) và c là số nguyên
            # y_I = a*x_I^2 + b*x_I + c. Để y_I âm thì c < -a*x_I^2 - b*x_I
            c = a * x_I**2 + b * x_I + random.randint(1, 3) # Ở đây chọn c để có nghiệm đẹp hoặc thực tế
            # Để giống bài mẫu y = x^2 - 4x + 3, ta có thể fix hoặc random nhẹ:
            a = 1
            b = -4
            c = 3
            f = a*x**2 + b*x + c

            # Tính toán các thông số
            trục_dx = -Rational(b, 2*a)
            y_min = a*(trục_dx**2) + b*trục_dx + c
            x1 = 1
            x2 = 3
            # Trong bài mẫu: x^2 - 4x + 3 = 0 có nghiệm 1 và 3. AB = |x2 - x1| = 2
            # Khoảng cách từ I(2;-1) đến AB (trục Ox) là |y_I| = 1
            # S = 1/2 * 1 * 2 = 1

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho Parabol $(P): y = %s$.''' % (latex(f)))

            ########################################################################
            # Nhận biết: Trục đối xứng
            nb_da_1_d = '\\True Trục đối xứng của đồ thị là đường thẳng $x = %s$' % (latex(trục_dx))
            nb_da_1_s = 'Trục đối xứng của đồ thị là đường thẳng $x = %s$' % (latex(-trục_dx))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Trục đối xứng của đồ thị là đường thẳng $x = -\\frac{b}{2a} = -\\frac{%s}{2.%s} = %s$.''' 
                            % (b, a, latex(trục_dx)))

            ########################################################################
            # Thông hiểu: Tọa độ đỉnh
            th_da_1_d = '\\True Tọa độ đỉnh của Parabol là $I(%s; %s)$' % (latex(trục_dx), latex(y_min))
            th_da_1_s = 'Tọa độ đỉnh của Parabol là $I(%s; %s)$' % (latex(y_min), latex(trục_dx))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('''Ta có $x = %s \\Rightarrow y(%s) = %s$. Do đó $I(%s; %s)$.''' 
                            % (latex(trục_dx), latex(trục_dx), latex(y_min), latex(trục_dx), latex(y_min)))

            ########################################################################
            # Vận dụng: Giá trị nhỏ nhất
            vd_da_1_d = '\\True Giá trị nhỏ nhất của hàm số là $%s$' % (latex(y_min))
            vd_da_1_s = 'Giá trị nhỏ nhất của hàm số là $%s$' % (latex(trục_dx))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Vì hệ số $a = %s > 0$ nên bề lõm hướng lên trên, giá trị nhỏ nhất của hàm số là $y(%s) = %s$.''' 
                            % (a, latex(trục_dx), latex(y_min)))

            ########################################################################
            # Vận dụng cao: Diện tích tam giác IAB
            S = Rational(1, 2) * abs(y_min) * abs(x2 - x1)
            vdc_da_1_d = '\\True Diện tích tam giác $IAB$ bằng $%s$ (với $A, B$ là giao điểm của $(P)$ với trục hoành)' % (latex(S))
            vdc_da_1_s = 'Diện tích tam giác $IAB$ bằng $%s$' % (latex(S + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có $%s = 0 \\Leftrightarrow \\left[ \\begin{aligned} &x=%s \\Rightarrow A(%s;0) \\\\ &x=%s \\Rightarrow B(%s;0) \\end{aligned} \\right.$. \\\\ Ta có $S_{\\Delta IAB} = \\frac{1}{2} d(I, AB) \\cdot AB = \\frac{1}{2} d(I, Ox) \\cdot AB = \\frac{1}{2} \\cdot %s \\cdot %s = %s$.''' 
                             % (latex(f), x1, x1, x2, x2, latex(abs(y_min)), abs(x2-x1), latex(S)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

