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


def bt_dang5_p2_b3_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random số mũ n là số chẵn để có số hạng không chứa x (số hạng chính giữa)
            n = random.choice([4, 6, 8])
            n_plus_1 = n + 1
            coeff_constant = binomial(n, n//2)
            coeff_x2 = binomial(n, (n-2)//2)
            coeff_xn = 1

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khai triển biểu thức $\\left( x + \\frac{1}{x} \\right)^{%s}$.''' 
                             %(latex(n)))

            ########################################################################
            # Nhận biết ############################################
            # Phát biểu về số lượng số hạng
            nb_da_1_d = '\\True Sau khi khai triển, biểu thức có %s số hạng' %(latex(n_plus_1))
            nb_da_1_s = 'Sau khi khai triển, biểu thức có %s số hạng' %(latex(n))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Nội dung lời giải
            loigiai_nb_1 = ('''Khai triển nhị thức Newton $(a+b)^n$ có $n+1$ số hạng. \\\\
                            Ở đây $n=%s$ nên có $%s+1=%s$ số hạng.'''
                            %(latex(n), latex(n), latex(n_plus_1)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Hệ số của x^n
            th_da_1_d = '\\True Hệ số của $x^{%s}$ là $1$' %(latex(n))
            th_da_1_s = 'Hệ số của $x^{%s}$ là $%s$' %(latex(n), latex(n))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Nội dung lời giải
            loigiai_th_1 = ('''Số hạng tổng quát trong khai triển là $T_{k+1} = C_{%s}^k x^{%s-k} \\left( \\frac{1}{x} \\right)^k = C_{%s}^k x^{%s-2k}$. \\\\
                            Để có $x^{%s}$, ta chọn $%s-2k=%s \\Leftrightarrow k=0$. \\\\
                            Hệ số là $C_{%s}^0 = 1$.'''
                            %(latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip([th_da_1], list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Hệ số của x^2
            vd_da_1_d = '\\True Hệ số của $x^2$ là $%s$' %(latex(coeff_x2))
            vd_da_1_s = 'Hệ số của $x^2$ là $\\frac{1}{%s}$' %(latex(coeff_x2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xét số hạng tổng quát $T_{k+1} = C_{%s}^k x^{%s-2k}$. \\\\
                            Để tìm hệ số của $x^2$, ta cho $%s-2k=2 \\Leftrightarrow 2k = %s \\Leftrightarrow k=%s$. \\\\
                            Hệ số cần tìm là $C_{%s}^{%s} = %s$.'''
                            %(latex(n), latex(n), latex(n), latex(n-2), latex((n-2)//2), latex(n), latex((n-2)//2), latex(coeff_x2)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip([vd_da_1], list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Số hạng không chứa x
            vdc_da_1_d = '\\True Số hạng không chứa $x$ là $%s$' %(latex(coeff_constant))
            vdc_da_1_s = 'Số hạng không chứa $x$ là $%s$' %(latex(n))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Số hạng không chứa $x$ ứng với $%s-2k=0 \\Leftrightarrow k=%s$. \\\\
                            Giá trị số hạng đó là $C_{%s}^{%s} = %s$.'''
                            %(latex(n), latex(n//2), latex(n), latex(n//2), latex(coeff_constant)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    shuffled_answers_nb = [nb_sel]
                    shuffled_answers_th = [th_sel]
                    shuffled_answers_vd = [vd_sel]
                    shuffled_answers_vdc = [vdc_sel]
                    break

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

