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


def bt_dang12_p2_b3_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Bước 1: Random thông số bài toán
            # Chọn số mũ n là số chẵn (để giữ tính chất tương tự bài mẫu n=4)
            n = random.choice([4, 6]) 
            expr = (x + 1)**n - (x - 1)**n
            expr_expanded = expand(expr)

            # Tính toán các thông số để làm đáp án
            # 1. Số hạng tự do (hệ số của x^0)
            so_hang_tu_do = expr_expanded.coeff(x, 0) # Luôn bằng 0 với n chẵn

            # 2. Hệ số của x
            he_so_x = expr_expanded.coeff(x, 1) # Với n=4 là 8, n=6 là 12

            # 3. Tổng các hệ số (thay x = 1)
            tong_he_so = expr_expanded.subs(x, 1) # Với n=4 là 16, n=6 là 2^6 - 0 = 64

            # Nội dung câu hỏi
            noidungcauhoi = ('''Xét khai triển biểu thức $P\\left( x \\right) = \\left( x+1 \\right)^{%s} - \\left( x-1 \\right)^{%s}$.''' 
                             %(latex(n), latex(n)))

            ########################################################################
            # Nhận biết ############################################
            # Câu a: Số hạng tự do
            nb_da_1_d = '\\True Số hạng tự do trong khai triển bằng $%s$' % (latex(so_hang_tu_do))
            nb_da_1_s = 'Số hạng tự do trong khai triển bằng $%s$' % (latex(random.choice([1, 2, -1])))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Số hạng tự do trong khai triển là $P\\left( 0 \\right) = \\left( 0+1 \\right)^{%s} - \\left( 0-1 \\right)^{%s} = 1 - 1 = %s$.''' 
                            % (latex(n), latex(n), latex(so_hang_tu_do)))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Câu b: Hệ số của x
            th_da_1_d = '\\True Hệ số của $x$ trong khai triển là $%s$' % (latex(he_so_x))
            th_da_1_s = 'Hệ số của $x$ trong khai triển là $%s$' % (latex(-he_so_x))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            # Giải thích tìm hệ số x: C_n^{n-1}*x*1^1 - C_n^{n-1}*x*(-1)^1 = 2*n*x
            loigiai_th_1 = ('''Hệ số của $x$ trong khai triển $\\left( x+1 \\right)^{%s}$ là $C_{%s}^{%s} = %s$. \\\\
            Hệ số của $x$ trong khai triển $\\left( x-1 \\right)^{%s}$ là $C_{%s}^{%s} \\cdot \\left( -1 \\right)^{%s} = -%s$. \\\\
            Vậy hệ số của $x$ trong $P\\left( x \\right)$ là $%s - \\left( -%s \\right) = %s$.''' 
                            % (latex(n), latex(n), latex(n-1), latex(n), 
                               latex(n), latex(n), latex(n-1), latex(n-1), latex(n),
                               latex(n), latex(n), latex(he_so_x)))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Câu c: Tổng các hệ số
            vd_da_1_d = '\\True Tổng các hệ số trong khai triển bằng $%s$' % (latex(tong_he_so))
            vd_da_1_s = 'Tổng các hệ số trong khai triển bằng $%s$' % (latex(tong_he_so - 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Tổng các hệ số của đa thức $P\\left( x \\right)$ bằng $P\\left( 1 \\right)$. \\\\
            Ta có $P\\left( 1 \\right) = \\left( 1+1 \\right)^{%s} - \\left( 1-1 \\right)^{%s} = 2^{%s} = %s$.''' 
                            % (latex(n), latex(n), latex(n), latex(tong_he_so)))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Câu d: P(x) > 0 khi x > 0
            vdc_da_1_d = '\\True $P\\left( x \\right) > 0$ khi $x \\in \\left( 0; +\\infty \\right)$'
            vdc_da_1_s = '$P\\left( x \\right) < 0$ khi $x \\in \\left( 0; +\\infty \\right)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Với $x > 0$, ta có $x+1 > |x-1|$ (vì $x+1 > x-1$ và $x+1 > 1-x \\Leftrightarrow 2x > 0$ luôn đúng). \\\\
            Do đó $\\left( x+1 \\right)^{%s} > \\left( x-1 \\right)^{%s}$ với mọi $x > 0$ (do $%s$ là số chẵn). \\\\
            Suy ra $P\\left( x \\right) = \\left( x+1 \\right)^{%s} - \\left( x-1 \\right)^{%s} > 0$ với mọi $x \\in \\left( 0; +\\infty \\right)$.''' 
                             % (latex(n), latex(n), latex(n), latex(n), latex(n)))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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

            # Gán lại vào list để xuất bản
            shuffled_answers_nb = [nb_da_1]
            shuffled_answers_th = [th_da_1]
            shuffled_answers_vd = [vd_da_1]
            shuffled_answers_vdc = [vdc_da_1]

            # Xuất câu hỏi
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

