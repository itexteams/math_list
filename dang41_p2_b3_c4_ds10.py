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


def bt_dang41_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Nghiên cứu đề bài và tạo biến random
            # Tạo biểu thức x^2 - 2mx + n sao cho biệt thức Delta' < 0 để luôn dương
            # x^2 - 2x + 5 có m = 1, n = 5. Ta chọn m ngẫu nhiên, sau đó chọn n > m^2.
            m = random.randint(1, 4)
            n = m**2 + random.randint(1, 5)
            val_limit = random.randint(30, 60) # Random giới hạn số nghiệm (ví dụ 40)

            # Biểu thức trong căn: x^2 - 2mx + n
            f_trong_can = x**2 - 2*m*x + n

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho bất phương trình $(x - \\sqrt{x})\\sqrt{%s} \\geq 0$. ''' 
                             % (latex(f_trong_can)))

            ########################################################################
            # Nhận biết
            nb_da_1_d = '\\True Điều kiện xác định của bất phương trình là $x \\geq 0$'
            nb_da_1_s = 'Điều kiện xác định của bất phương trình là $x > 0$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Điều kiện xác định của bất phương trình là $\\begin{cases} x \\geq 0 \\\\ %s \\geq 0 \\end{cases}$. Vì $%s = (x-%s)^2 + %s > 0$ với mọi $x$, nên điều kiện xác định là $x \\geq 0$.'''
                            % (latex(f_trong_can), latex(f_trong_can), m, n - m**2))

            ########################################################################
            # Thông hiểu
            th_da_1_d = '\\True $%s > 0, \\forall x \\in \\mathbb{R}$' % (latex(f_trong_can))
            th_da_1_s = '$%s \\geq 0$ chỉ đúng khi $x \\geq 0$' % (latex(f_trong_can))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Biểu thức $%s$ có $\\Delta\' = (%s)^2 - 1 \\cdot %s = %s < 0$ và hệ số $a=1>0$, nên $%s > 0$ với mọi $x \\in \\mathbb{R}$.'''
                            % (latex(f_trong_can), -m, n, m**2 - n, latex(f_trong_can)))

            ########################################################################
            # Vận dụng
            # Tạo phương án nhiễu bằng cách thay đổi hệ số trước căn x
            he_so_nhieu = random.choice([2, 3, 4])
            vd_da_1_d = 'Bất phương trình tương đương với bất phương trình $x - %s\\sqrt{x} \\geq 0$' % (he_so_nhieu)
            vd_da_1_s = '\\True Bất phương trình tương đương với bất phương trình $x - \\sqrt{x} \\geq 0$ trên tập xác định'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì $\\sqrt{%s} > 0$ với mọi $x$, nên bất phương trình đã cho tương đương với $x - \\sqrt{x} \\geq 0$. Khẳng định "$x - %s\\sqrt{x} \\geq 0$" là sai.'''
                            % (latex(f_trong_can), he_so_nhieu))

            ########################################################################
            # Vận dụng cao
            vdc_da_1_d = 'Số nghiệm nguyên nhỏ hơn %s của bất phương trình là $%s$' % (val_limit, val_limit - 1)
            vdc_da_1_s = '\\True Số nghiệm nguyên nhỏ hơn %s của bất phương trình là $%s$' % (val_limit, val_limit)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có $x - \\sqrt{x} \\geq 0 \\Leftrightarrow \\sqrt{x}(\\sqrt{x} - 1) \\geq 0 \\Leftrightarrow \\left[ \\begin{array}{l} \\sqrt{x} = 0 \\\\ \\sqrt{x} \\geq 1 \\end{array} \\right. \\Leftrightarrow \\left[ \\begin{array}{l} x = 0 \\\\ x \\geq 1 \\end{array} \\right.$. \\\\ Các nghiệm nguyên nhỏ hơn %s là $x \\in \\{0, 1, 2, \\dots, %s\\}$. Vậy có %s nghiệm nguyên (bao gồm số 0).''' 
                             % (val_limit, val_limit - 1, val_limit))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

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

