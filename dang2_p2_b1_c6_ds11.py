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


def bt_dang2_p2_b1_c6_ds11(self):
            # Khai báo biến
            x = symbols('x')
            a = randint(5, 9) # Số hs khối 10
            b = randint(5, 9) # Số hs khối 11
            c = randint(2, 4) # Số hs được chọn

            # Tính toán các giá trị tổ hợp (dùng math.comb để tránh lỗi NameError)
            n_omega = math.comb(a + b, c)
            n_a = math.comb(a, c)
            n_b = math.comb(b, c)

            p_a = Rational(n_a, n_omega)
            p_b = Rational(n_b, n_omega)
            p_c = p_a + p_b

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Một đội tình nguyện gồm $%s$ học sinh khối $10$ và $%s$ học sinh khối $11$. Chọn ngẫu nhiên $%s$ học sinh trong đội. Gọi các biến cố: \\
            $A$ là biến cố "Các học sinh được chọn đều thuộc khối $10$". \\
            $B$ là biến cố "Các học sinh được chọn đều thuộc khối $11$". \\
            $C$ là biến cố "Các học sinh được chọn đều thuộc cùng một khối".''' 
            %(latex(a), latex(b), latex(c)))

            # --- NHẬN BIẾT ---
            nb_da_1_d = '\\True Xác suất của biến cố $A$ là $P(A)=%s$' %(latex(p_a))
            nb_da_1_s = 'Xác suất của biến cố $A$ là $P(A)=%s$' %(latex(1-p_a))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số phần tử của không gian mẫu là $n(\\Omega)=C_{%s}^{%s}=%s$. \\\\
            Số cách chọn ra $%s$ học sinh khối $10$ là $n(A)=C_{%s}^{%s}=%s$. \\\\
            Xác suất của biến cố $A$ là $P(A)=\\frac{n(A)}{n(\\Omega)}=\\frac{%s}{%s}=%s$.'''
            %(latex(a+b), latex(c), latex(n_omega), latex(c), latex(a), latex(c), latex(n_a), latex(n_a), latex(n_omega), latex(p_a)))

            # --- THÔNG HIỂU ---
            th_da_1_d = '\\True $C=A \\cup B$'
            th_da_1_s = '$C=A \\cap B$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Biến cố $C$ xảy ra khi các học sinh được chọn cùng thuộc khối $10$ (biến cố $A$) hoặc cùng thuộc khối $11$ (biến cố $B$). Vậy $C=A \\cup B$.''')

            # --- VẬN DỤNG ---
            vd_da_1_d = '\\True $P(C)=P(A)+P(B)$'
            vd_da_1_s = '$P(C)=P(A) \\cdot P(B)$' 
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Vì $A$ và $B$ là hai biến cố xung khắc nên ta có $P(C)=P(A \\cup B)=P(A)+P(B)$.''')

            # --- VẬN DỤNG CAO ---
            vdc_da_1_d = '\\True Xác suất của biến cố $C$ là $P(C)=%s$' %(latex(p_c))
            vdc_da_1_s = 'Xác suất của biến cố $C$ là $P(C)=%s$' %(latex(1-p_c))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Số cách chọn ra $%s$ học sinh khối $11$ là $n(B)=C_{%s}^{%s}=%s$. \\\\
            Xác suất của biến cố $B$ là $P(B)=\\frac{n(B)}{n(\\Omega)}=\\frac{%s}{%s}=%s$. \\\\
            Suy ra $P(C)=P(A)+P(B)=%s+%s=%s$.'''
            %(latex(c), latex(b), latex(c), latex(n_b), latex(n_b), latex(n_omega), latex(p_b), latex(p_a), latex(p_b), latex(p_c)))

            # Vòng lặp chọn đáp án sao cho có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = sum('\\True' in ans for ans in answers)
                if 1 <= true_count <= 3:
                    break

            # Tách riêng list lời giải để chuẩn bị xáo trộn theo mẫu
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp và xáo trộn (theo mẫu zip của bạn)
            combined_nb = list(zip([nb_da_1], list_nb_2))
            combined_th = list(zip([th_da_1], list_th_2))
            combined_vd = list(zip([vd_da_1], list_vd_2))
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            s_ans_nb, s_sol_nb = zip(*combined_nb)
            s_ans_th, s_sol_th = zip(*combined_th)
            s_ans_vd, s_sol_vd = zip(*combined_vd)
            s_ans_vdc, s_sol_vdc = zip(*combined_vdc)

            # Xuất nội dung theo mẫu minipage
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(s_ans_nb[0]) + '}\n'
                '{' + str(s_ans_th[0]) + '}\n'
                '{' + str(s_ans_vd[0]) + '}\n'
                '{' + str(s_ans_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(s_sol_nb[0]) + '\n'
                '\\item ' + str(s_sol_th[0]) + '\n'
                '\\item ' + str(s_sol_vd[0]) + '\n'
                '\\item ' + str(s_sol_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')

            return content

