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


def bt_dang6_p2_b3_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            n = randint(4, 6)  # Số mũ khai triển (ví dụ từ 4 đến 6)
            b = randint(1, 2)  # Hằng số trong (x + b)^n
            m = randint(2, 3)  # Số dùng cho biểu thức tổng ở câu (d)

            # Tính toán các giá trị phục vụ lời giải
            coeff_xn_minus_1 = n * (b**1) # Hệ số của x^(n-1)
            constant_term = b**n # Số hạng không chứa x
            sum_all_coeffs = 2**n if b == 1 else (1 + b)**n # Tổng các hệ số
            generalized_sum = (m + b)**n # Giá trị của biểu thức ở câu (d)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khai triển $\\left( x+%s \\right)^{%s}$.''' 
                             %(latex(b), latex(n)))

            ########################################################################
            # Nhận biết ############################################
            # Hệ số của x^(n-1)
            nb_da_1_d = '\\True Hệ số của $x^{%s}$ là $%s$' %(latex(n-1), latex(coeff_xn_minus_1))
            nb_da_1_s = 'Hệ số của $x^{%s}$ là $%s$' %(latex(n-1), latex(coeff_xn_minus_1 + 1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Số hạng tổng quát trong khai triển là $T_{k+1} = C_{%s}^{k} \\cdot x^{%s-k} \\cdot %s^{k}$.\\\\
            Để tìm hệ số của $x^{%s}$, ta chọn $%s-k = %s \\Rightarrow k = 1$.\\\\
            Vậy hệ số là $C_{%s}^{1} \\cdot %s^{1} = %s$.'''
                            %(latex(n), latex(n), latex(b), latex(n-1), latex(n), latex(n-1), latex(n), latex(b), latex(coeff_xn_minus_1)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Số hạng không chứa x
            th_da_1_d = '\\True Số hạng không chứa $x$ là $%s$' %(latex(constant_term))
            th_da_1_s = 'Số hạng không chứa $x$ là $%s$' %(latex(n))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Số hạng không chứa $x$ ứng với số hạng có $x^0$, tức là $%s-k = 0 \\Rightarrow k = %s$.\\\\
            Giá trị số hạng đó là $C_{%s}^{%s} \\cdot %s^{%s} = %s$.'''
                            %(latex(n), latex(n), latex(n), latex(n), latex(b), latex(n), latex(constant_term)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Tổng các hệ số C_n^k
            sum_str = " + ".join(["C_{%s}^{%s}" % (n, i) for i in range(n + 1)])
            vd_da_1_d = '\\True $%s = %s$' %(sum_str, latex(2**n)) if b == 1 else 'Tổng các hệ số là $%s$' %(latex(sum_all_coeffs))
            vd_da_1_s = '$%s = %s$' %(sum_str, latex(3**n))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Thay $x=1$ vào khai triển $\\left( x+1 \\right)^{%s} = C_{%s}^{0}x^{%s} + C_{%s}^{1}x^{%s-1} + \\dots + C_{%s}^{%s}$.\\\\
            Ta được $2^{%s} = C_{%s}^{0} + C_{%s}^{1} + \\dots + C_{%s}^{%s}$.\\\\
            Vậy tổng các hệ số là $%s$.'''
                            %(latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(2**n)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Tổng trọng số m^(n-k)
            weighted_sum_str = " + ".join(["%s C_{%s}^{%s}" % (latex(m**(n-i)) if n-i > 1 else (latex(m) if n-i == 1 else ""), n, i) for i in range(n + 1)])
            vdc_da_1_d = '\\True $%s = %s$' %(weighted_sum_str, latex(generalized_sum))
            vdc_da_1_s = '$%s = %s$' %(weighted_sum_str, latex(2**n))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Xét khai triển $\\left( x+%s \\right)^{%s} = C_{%s}^{0}x^{%s} + C_{%s}^{1}x^{%s-1} \\cdot %s + \\dots + C_{%s}^{%s}%s^{%s}$.\\\\
            Thay $x=%s$ vào hai vế, ta có:\\\\
            $\\left( %s+%s \\right)^{%s} = C_{%s}^{0} \\cdot %s^{%s} + C_{%s}^{1} \\cdot %s^{%s-1} \\cdot %s + \\dots + C_{%s}^{%s} \\cdot %s^{%s}$.\\\\
            Suy ra giá trị biểu thức bằng $%s^{%s} = %s$.'''
                             %(latex(b), latex(n), latex(n), latex(n), latex(n), latex(n), latex(b), latex(n), latex(n), latex(b), latex(n),
                               latex(m), latex(m), latex(b), latex(n), latex(n), latex(m), latex(n), latex(n), latex(m), latex(n), latex(b), latex(n), latex(n), latex(b), latex(n),
                               latex(m+b), latex(n), latex(generalized_sum)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lại list sau khi thỏa mãn điều kiện
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

