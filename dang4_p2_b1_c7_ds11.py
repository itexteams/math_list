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


def bt_dang4_p2_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x, x0 = symbols('x x0')

            # B3 - Random bài toán
            a = randint(1, 4)  # Hệ số của x^2
            b = randint(1, 6)  # Hệ số tự do
            k = randint(2, 5)  # Điểm x0 cụ thể để tính f'(k)

            # Hàm số f(x) = ax^2 + b
            f_x = a*x**2 + b
            f_x0 = a*x0**2 + b
            f_prime_expr = 2*a*x0
            f_prime_k = 2*a*k

            # Nội dung câu hỏi
            noidungcauhoi = ('''Dùng định nghĩa tìm đạo hàm của hàm số $y = %s$ trên tập xác định.''' 
                             % (latex(f_x)))

            ########################################################################
            # Nhận biết - Định nghĩa đạo hàm
            nb_da_1_d = '\\True $f\'\\left(x_0\\right) = \\lim_{x \\to x_0} \\frac{f\\left(x\\right)-f\\left(x_0\\right)}{x-x_0}$'
            nb_da_1_s = '$f\'\\left(x_0\\right) = \\frac{f\\left(x\\right)-f\\left(x_0\\right)}{x-x_0}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Theo định nghĩa, đạo hàm của hàm số $y=f\\left(x\\right)$ tại điểm $x_0$ là \\\\ $f\'\\left(x_0\\right) = \\lim_{x \\to x_0} \\frac{f\\left(x\\right)-f\\left(x_0\\right)}{x-x_0}$.''')

            ########################################################################
            # Thông hiểu - Tính đạo hàm tổng quát
            th_da_1_d = '\\True $f\'\\left(x_0\\right) = \\lim_{x \\to x_0} \\frac{f\\left(x\\right)-f\\left(x_0\\right)}{x-x_0} = %s$' % (latex(f_prime_expr))
            th_da_1_s = '$f\'\\left(x_0\\right) = \\lim_{x \\to x_0} \\frac{f\\left(x\\right)-f\\left(x_0\\right)}{x-x_0} = %s x_0 + %s$' % (latex(2*a), latex(b))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Ta có $f\'\\left(x_0\\right) = \\lim_{x \\to x_0} \\frac{\\left(%s\\right) - \\left(%s\\right)}{x-x_0}$ \\\\
                            $= \\lim_{x \\to x_0} \\frac{%s\\left(x^2-x_0^2\\right)}{x-x_0} = \\lim_{x \\to x_0} %s\\left(x+x_0\\right) = %s$.''' 
                            % (latex(f_x), latex(f_x0), latex(a), latex(a), latex(f_prime_expr)))

            ########################################################################
            # Vận dụng - Tính giá trị tại 1 điểm
            vd_da_1_d = '\\True $f\'\\left(%s\\right) = %s$' % (latex(k), latex(f_prime_k))
            vd_da_1_s = '$f\'\\left(%s\\right) = %s$' % (latex(k), latex(a*k**2 + b))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Thay $x_0 = %s$ vào biểu thức đạo hàm tổng quát, ta được \\\\ $f\'\\left(%s\\right) = %s \\cdot %s = %s$.''' 
                            % (latex(k), latex(k), latex(2*a), latex(k), latex(f_prime_k)))

            ########################################################################
            # Vận dụng cao - Tính tổng đạo hàm tại k và -k
            vdc_da_1_d = '\\True $f\'\\left(%s\\right) + f\'\\left(-%s\\right) = 0$' % (latex(k), latex(k))
            vdc_da_1_s = '$f\'\\left(%s\\right) + f\'\\left(-%s\\right) = %s$' % (latex(k), latex(k), latex(2*f_prime_k))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Ta có $f\'\\left(x_0\\right) = %s x_0$. \\\\
                             Suy ra $f\'\\left(-%s\\right) = %s \\cdot \\left(-%s\\right) = -%s$. \\\\
                             Vậy $f\'\\left(%s\\right) + f\'\\left(-%s\\right) = %s + \\left(-%s\\right) = 0$.''' 
                             % (latex(2*a), latex(k), latex(2*a), latex(k), latex(f_prime_k), 
                                latex(k), latex(k), latex(f_prime_k), latex(f_prime_k)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán vào list để xáo trộn lời giải tương ứng (nếu cần)
            list_nb_1, list_nb_2 = [nb_sel], [loigiai_nb_1]
            list_th_1, list_th_2 = [th_sel], [loigiai_th_1]
            list_vd_1, list_vd_2 = [vd_sel], [loigiai_vd_1]
            list_vdc_1, list_vdc_2 = [vdc_sel], [loigiai_vdc_1]

            shuffled_answers_nb, shuffled_solutions_nb = zip(*list(zip(list_nb_1, list_nb_2)))
            shuffled_answers_th, shuffled_solutions_th = zip(*list(zip(list_th_1, list_th_2)))
            shuffled_answers_vd, shuffled_solutions_vd = zip(*list(zip(list_vd_1, list_vd_2)))
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*list(zip(list_vdc_1, list_vdc_2)))

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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

