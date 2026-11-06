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


def bt_dang22_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- NGHIÊN CỨU VÀ TÌM CÁCH RANDOM ---
            # Phương trình dạng: (sqrt(x^2 + bx + c) - (mx - m))^2 + (2 - sqrt(x + 3))^2 = 0
            # Nghiệm chung luôn là x = 1.
            m_val = random.choice([2, 3]) 
            b_val = random.choice([2, 4, 6])
            c_val = -b_val - 1

            # Biểu thức toán học
            expr_radical = sqrt(x**2 + b_val*x + c_val)
            expr_linear = m_val*x - m_val
            expr_fixed_radical = sqrt(x + 3)

            # Tính nghiệm thứ 2 của pt: sqrt(x^2 + bx + c) = mx - m
            # <=> (m^2 - 1)x^2 - (2m^2 + b)x + (m^2 - c) = 0
            A_q = m_val**2 - 1
            B_q = -(2*m_val**2 + b_val)
            C_q = m_val**2 - c_val
            roots_list = solve(A_q*x**2 + B_q*x + C_q, x)
            x2_val = next(r for r in roots_list if r != 1)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $\\left( %s - %s \\right)^2 + \\left( 2 - %s \\right)^2 = 0$. (*)''' 
                             %(latex(expr_radical), latex(expr_linear), latex(expr_fixed_radical)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Điều kiện xác định của phương trình (*) là $x \\ge -3$'
            nb_da_1_s = 'Điều kiện xác định của phương trình (*) là $x \\ge 1$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Điều kiện xác định của phương trình là $\\begin{cases} x^2 + %sx %s \\ge 0 \\\\ x + 3 \\ge 0 \\end{cases} \\Leftrightarrow x \\ge %s$. Tuy nhiên, để biểu thức có nghĩa trong tập số thực, ta xét điều kiện căn thức đứng độc lập là $x \\ge -3$.''' 
                            %(latex(b_val), latex(c_val), latex(-3)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Tập nghiệm của phương trình (*) là $S = \\{1\\}$'
            th_da_1_s = 'Phương trình (*) có 3 nghiệm phân biệt'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Ta có: $\\left( %s - %s \\right)^2 + \\left( 2 - %s \\right)^2 = 0 \\Leftrightarrow \\begin{cases} %s - %s = 0 \\\\ 2 - %s = 0 \\end{cases}$.\\\\
            Phương trình $2 - %s = 0 \\Leftrightarrow %s = 2 \\Leftrightarrow x + 3 = 4 \\Leftrightarrow x = 1$.'''
                            %(latex(expr_radical), latex(expr_linear), latex(expr_fixed_radical), latex(expr_radical), latex(expr_linear), latex(expr_fixed_radical), latex(expr_fixed_radical), latex(expr_fixed_radical)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Nghiệm của phương trình (*) nhỏ hơn 2'
            vd_da_1_s = '$x = %s$ là nghiệm của phương trình (*)' %(latex(x2_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Giải phương trình: $%s - %s = 0 \\Leftrightarrow %s = %s$ (2).\\\\
            Bình phương hai vế phương trình (2) với điều kiện $%s \\ge 0 \\Leftrightarrow x \\ge 1$, ta có:\\\\
            $x^2 + %sx %s = %s \\Leftrightarrow %sx^2 %sx + %s = 0 \\Leftrightarrow x = 1$ hoặc $x = %s$.'''
                            %(latex(expr_radical), latex(expr_linear), latex(expr_radical), latex(expr_linear), latex(expr_linear), latex(b_val), latex(c_val), latex(expr_linear**2), latex(A_q), latex(B_q), latex(C_q), latex(x2_val)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Phương trình (*) có duy nhất một nghiệm thực'
            vdc_da_1_s = 'Phương trình (*) có vô số nghiệm'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Tuy nhiên chỉ có $x = 1$ thỏa mãn phương trình $2 - \\sqrt{x+3} = 0$.\\\\
            Vậy tập nghiệm của phương trình ban đầu là $S = \\{1\\}$.''' )
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

            # Gán lại vào list để xử lý nội dung
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải (phần content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

