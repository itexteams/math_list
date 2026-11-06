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


def bt_dang19_p2_b1_c3_ds12(self):
                # Khai báo biến ngẫu nhiên
                x = symbols('x')
                a = random.randint(2, 5)  # Cơ số cho hàm mũ
                b = random.randint(2, 6)  # Hệ số cho hàm cos

                # Nội dung câu hỏi
                noidungcauhoi = r'''Xét tính đúng sai của các khẳng định sau về nguyên hàm:'''

                ########################################################################
                # Nhận biết: Nguyên hàm hàm mũ cơ bản
                ########################################################################
                nb_da_1_d = r'\True $\int (%s^x + e^x)\,\text{d}x = \frac{%s^x}{\ln %s} + e^x + C$' % (latex(a), latex(a), latex(a))
                nb_da_1_s = r'$\int (%s^x + e^x)\,\text{d}x = %s^x \cdot \ln %s + e^x + C$' % (latex(a), latex(a), latex(a))
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = r'Ta có $\int %s^x \,\text{d}x = \frac{%s^x}{\ln %s} + C$ và $\int e^x \,\text{d}x = e^x + C$.' % (latex(a), latex(a), latex(a))

                ########################################################################
                # Thông hiểu: Nguyên hàm hỗn hợp lượng giác và mũ
                ########################################################################
                th_da_1_d = r'\True $\int (%s \cos x - %s^x)\,\text{d}x = %s \sin x - \frac{%s^x}{\ln %s} + C$' % (latex(b), latex(a), latex(b), latex(a), latex(a))
                th_da_1_s = r'$\int (%s \cos x - %s^x)\,\text{d}x = %s \sin x - %s^x + C$' % (latex(b), latex(a), latex(b), latex(a))
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = r'Ta có $\int (%s \cos x - %s^x)\,\text{d}x = %s \sin x - \frac{%s^x}{\ln %s} + C$.' % (latex(b), latex(a), latex(b), latex(a), latex(a))

                ########################################################################
                # Vận dụng: Hạ bậc cos^2
                ########################################################################
                vd_da_1_d = r'\True $\int \cos^2 \frac{x}{2} \,\text{d}x = \frac{1}{2}x + \frac{1}{2}\sin x + C$'
                vd_da_1_s = r'$\int \cos^2 \frac{x}{2} \,\text{d}x = \frac{1}{2}x + \sin x + C$'
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = r'Sử dụng công thức hạ bậc: $\cos^2 \frac{x}{2} = \frac{1+\cos x}{2}$. Khi đó $\int \frac{1+\cos x}{2} \,\text{d}x = \frac{1}{2}x + \frac{1}{2}\sin x + C$.'

                ########################################################################
                # Vận dụng cao: Nguyên hàm tan^2
                ########################################################################
                vdc_da_1_d = r'\True $\int \tan^2 x \,\text{d}x = \tan x - x + C$'
                vdc_da_1_s = r'$\int \tan^2 x \,\text{d}x = \tan x + x + C$'
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = r'Ta có $\tan^2 x = \frac{1}{\cos^2 x} - 1$. Suy ra $\int (\frac{1}{\cos^2 x} - 1) \,\text{d}x = \tan x - x + C$.'

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

