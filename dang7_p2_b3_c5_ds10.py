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


def bt_dang7_p2_b3_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Bước 1: Random thông số bài toán
            # Chọn số m để có sqrt(m) và số mũ n
            list_m = [2, 3, 5, 6]
            m = random.choice(list_m)
            n = 5 # Giữ nguyên bậc 5 như đề bài hoặc có thể random trong khoảng [4, 6]
            a_val = sqrt(m)

            # Biểu thức P = (x - sqrt(m))^n
            # Lưu ý: Viết dưới dạng (x + (-sqrt(m))) để dễ tính toán hệ số
            P = (x - a_val)**n
            P_expanded = expand(P)

            # Hàm lấy hệ số của x^k trong khai triển
            def get_coeff(expr, variable, power):
                return expr.coeff(variable, power)

            # Tính toán các hệ số thực tế để làm đáp án đúng
            coeff_x4 = get_coeff(P_expanded, x, 4)
            coeff_x3 = get_coeff(P_expanded, x, 3)
            coeff_x2 = get_coeff(P_expanded, x, 2)
            coeff_x1 = get_coeff(P_expanded, x, 1)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khai triển $P = \\left( x - \\sqrt{%s} \\right)^{%s}$.''' 
                             %(latex(m), latex(n)))

            ########################################################################
            # Nhận biết (Câu a - Hệ số của x^4)
            ########################################################################
            val_a_true = coeff_x4
            val_a_false = -coeff_x4 if coeff_x4 != 0 else 5
            nb_da_1_d = '\\True Hệ số của $x^4$ trong khai triển là $%s$' %(latex(val_a_true))
            nb_da_1_s = 'Hệ số của $x^4$ trong khai triển là $%s$' %(latex(val_a_false))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số hạng tổng quát trong khai triển là $T_{k+1} = C_{%s}^k \\cdot x^{%s-k} \\cdot \\left( -\\sqrt{%s} \\right)^k$. \\\\
            Để có $x^4$ thì $%s-k = 4 \\Rightarrow k = 1$. \\\\
            Hệ số là $C_{%s}^1 \\cdot \\left( -\\sqrt{%s} \\right)^1 = %s$.'''
                            %(latex(n), latex(n), latex(m), latex(n), latex(n), latex(m), latex(val_a_true)))

            ########################################################################
            # Thông hiểu (Câu b - Hệ số của x^2)
            ########################################################################
            val_b_true = coeff_x2
            val_b_false = -coeff_x2 if coeff_x2 != 0 else 10
            th_da_1_d = '\\True Hệ số của $x^2$ trong khai triển là $%s$' %(latex(val_b_true))
            th_da_1_s = 'Hệ số của $x^2$ trong khai triển là $%s$' %(latex(val_b_false))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Để có $x^2$ thì $%s-k = 2 \\Rightarrow k = 3$. \\\\
            Hệ số là $C_{%s}^3 \\cdot \\left( -\\sqrt{%s} \\right)^3 = %s \\cdot \\left( -%s\\sqrt{%s} \\right) = %s$.'''
                            %(latex(n), latex(n), latex(m), latex(binomial(n, 3)), latex(m), latex(m), latex(val_b_true)))

            ########################################################################
            # Vận dụng (Câu c - Hệ số của x^3)
            ########################################################################
            val_c_true = coeff_x3
            val_c_false = val_c_true + 5
            list_vd_da_1 = ['\\True Hệ số của $x^3$ trong khai triển là $%s$' %(latex(val_c_true)),
                            'Hệ số của $x^3$ trong khai triển là $%s$' %(latex(val_c_false))]

            loigiai_vd_1 = ('''Để có $x^3$ thì $%s-k = 3 \\Rightarrow k = 2$. \\\\
            Hệ số là $C_{%s}^2 \\cdot \\left( -\\sqrt{%s} \\right)^2 = %s \\cdot %s = %s$.'''
                            %(latex(n), latex(n), latex(m), latex(binomial(n, 2)), latex(m), latex(val_c_true)))

            ########################################################################
            # Vận dụng cao (Câu d - Hệ số của x)
            ########################################################################
            val_d_true = coeff_x1
            val_d_false = val_d_true - 10
            list_vdc_da_1 = ['\\True Hệ số của $x$ trong khai triển là $%s$' %(latex(val_d_true)),
                             'Hệ số của $x$ trong khai triển là $%s$' %(latex(val_d_false))]

            loigiai_vdc_1 = ('''Để có $x$ thì $%s-k = 1 \\Rightarrow k = 4$. \\\\
            Hệ số là $C_{%s}^4 \\cdot \\left( -\\sqrt{%s} \\right)^4 = %s \\cdot %s = %s$.'''
                             %(latex(n), latex(n), latex(m), latex(binomial(n, 4)), latex(m**2), latex(val_d_true)))

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

            # Gán lại vào list để giữ cấu trúc mẫu
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

