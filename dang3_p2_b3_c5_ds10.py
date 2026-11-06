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


def bt_dang3_p2_b3_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            # Random giá trị a trong căn bậc hai (ví dụ chọn 2, 3, 5 để căn thức đẹp)
            a_val = random.choice([2, 3, 5])
            n = 4 # Số mũ cố định theo đề bài

            # Các hệ số trong khai triển (x + sqrt(a))^4 = x^4 + 4*sqrt(a)*x^3 + 6*a*x^2 + 4*a*sqrt(a)*x + a^2
            he_so_x3 = 4 * sqrt(a_val)
            he_so_x2 = 6 * a_val
            he_so_x = 4 * a_val * sqrt(a_val)
            so_hang_tu_do = a_val**2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khai triển $\\left( x+\\sqrt{%s} \\right)^{%s}$.''' 
                             %(latex(a_val), latex(n)))

            ########################################################################
            # Nhận biết (Xét hệ số x^2)
            ########################################################################
            nb_da_1_d = '\\True Hệ số của $x^2$ là $%s$' %(latex(he_so_x2))
            nb_da_1_s = 'Hệ số của $x^2$ là $%s$' %(latex(he_so_x2 + 2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Số hạng tổng quát trong khai triển là $T_{k+1} = C_{%s}^k \\cdot x^{%s-k} \\cdot \\left( \\sqrt{%s} \\right)^k$.\\\\
            Để tìm hệ số của $x^2$, ta chọn $%s-k=2 \\Leftrightarrow k=2$.\\\\
            Hệ số là $C_4^2 \\cdot \\left( \\sqrt{%s} \\right)^2 = 6 \\cdot %s = %s$.'''
                            %(latex(n), latex(n), latex(a_val), latex(n), latex(a_val), latex(a_val), latex(he_so_x2)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu (Xét hệ số x^3)
            ########################################################################
            th_da_1_d = '\\True Hệ số của $x^3$ là $%s$' %(latex(he_so_x3))
            th_da_1_s = 'Hệ số của $x^3$ là $%s\\sqrt{%s}$' %(latex(6), latex(a_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Để tìm hệ số của $x^3$, ta chọn $%s-k=3 \\Leftrightarrow k=1$.\\\\
            Hệ số là $C_4^1 \\cdot \\left( \\sqrt{%s} \\right)^1 = 4\\sqrt{%s}$.'''
                            %(latex(n), latex(a_val), latex(a_val)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng (Xét hệ số x)
            ########################################################################
            vd_da_1_d = '\\True Hệ số của $x$ là $%s$' %(latex(he_so_x))
            vd_da_1_s = 'Hệ số của $x$ là $8\\sqrt{%s}$' %(latex(a_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Để tìm hệ số của $x$, ta chọn $%s-k=1 \\Leftrightarrow k=3$.\\\\
            Hệ số là $C_4^3 \\cdot \\left( \\sqrt{%s} \\right)^3 = 4 \\cdot %s\\sqrt{%s} = %s$.'''
                            %(latex(n), latex(a_val), latex(a_val), latex(a_val), latex(he_so_x)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao (Xét số hạng không chứa x)
            ########################################################################
            vdc_da_1_d = '\\True Số hạng không chứa $x$ trong khai triển trên bằng $%s$' %(latex(so_hang_tu_do))
            vdc_da_1_s = 'Số hạng không chứa $x$ trong khai triển trên bằng $%s$' %(latex(so_hang_tu_do + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Số hạng không chứa $x$ ứng với $x^0$, ta chọn $%s-k=0 \\Leftrightarrow k=4$.\\\\
            Giá trị số hạng đó là $C_4^4 \\cdot \\left( \\sqrt{%s} \\right)^4 = 1 \\cdot %s = %s$.'''
                             %(latex(n), latex(a_val), latex(a_val**2), latex(so_hang_tu_do)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp để đảm bảo có ít nhất 1 đáp án đúng và không quá 3 đáp án đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán vào list cuối cùng để xuất dữ liệu
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

