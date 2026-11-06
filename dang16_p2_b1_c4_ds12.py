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


def bt_dang16_p2_b1_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ đổi dấu chấm thành dấu phẩy cho số thập phân
            def f_com(value):
                return str(value).replace('.', ',')

            # --- BƯỚC 1: NGHIÊN CỨU VÀ RANDOM DỮ LIỆU ---
            # Tỷ lệ học sinh nữ (A)
            pA_pct = random.randint(50, 65)  # Ví dụ: 58%
            pA = pA_pct / 100
            p_notA = (100 - pA_pct) / 100

            # Tỷ lệ nữ tham gia CLB Toán (B|A)
            pB_A_pct = random.randint(8, 15) # Ví dụ: 10%
            pB_A = pB_A_pct / 100

            # Tỷ lệ nam tham gia CLB Toán (B|notA)
            pB_notA_pct = random.randint(12, 20) # Ví dụ: 16%
            pB_notA = pB_notA_pct / 100

            # Tính xác suất đầy đủ P(B)
            pB = pA * pB_A + p_notA * pB_notA # Ví dụ: 0,58*0,1 + 0,42*0,16 = 0,1252

            # Tính xác suất hậu nghiệm P(A|B)
            pA_B = (pA * pB_A) / pB
            pA_B_round = round(pA_B, 2)

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Trong một trường THPT tỷ lệ học sinh nữ là $%s\\%%$. Tỷ lệ học sinh nữ và học sinh nam tham gia CLB Toán học lần lượt là: $%s\\%%$ và $%s\\%%$. Chọn ngẫu nhiên một học sinh của trường. Xét các biến cố: $A$ là biến cố "Học sinh được chọn là học sinh nữ", $B$ là biến cố "Học sinh được chọn tham gia CLB Toán học".''' 
                             % (pA_pct, pB_A_pct, pB_notA_pct))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Xác suất chọn được học sinh là nữ là: $P(A) = %s$' % f_com(pA)
            nb_da_1_s = 'Xác suất chọn được học sinh là nữ là: $P(A) = %s$' % f_com(round(p_notA, 2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Xác suất chọn được học sinh là nữ là: $P(A) = %s\\%% = %s$.''' 
                            % (pA_pct, f_com(pA)))

            list_nb_1 = [nb_da_1]; list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Xác suất chọn được học sinh tham gia CLB Toán học, biết rằng học sinh đó là nam, là $P(B / \\overline{A}) = %s$' % f_com(pB_notA)
            th_da_1_s = 'Xác suất chọn được học sinh tham gia CLB Toán học, biết rằng học sinh đó là nam, là $P(B / \\overline{A}) = %s$' % f_com(pB_A)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Xác suất chọn được học sinh tham gia CLB Toán học, biết rằng học sinh đó là nam, là: $P(B / \\overline{A}) = %s\\%% = %s$.''' 
                            % (pB_notA_pct, f_com(pB_notA)))

            list_th_1 = [th_da_1]; list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng ############################################
            pB_val = round(pB, 4)
            vd_da_1_d = '\\True Xác suất chọn được học sinh tham gia CLB Toán học là: $P(B) = %s$' % f_com(pB_val)
            vd_da_1_s = 'Xác suất chọn được học sinh tham gia CLB Toán học là: $P(B) = %s$' % f_com(round(pB_val + 0.01, 4))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xác suất chọn được học sinh tham gia CLB Toán học là: \\\\ $P(B) = P(A) \\cdot P(B|A) + P(\\overline{A}) \\cdot P(B|\\overline{A}) = %s \\cdot %s + %s \\cdot %s = %s$.''' 
                            % (f_com(pA), f_com(pB_A), f_com(p_notA), f_com(pB_notA), f_com(pB_val)))

            list_vd_1 = [vd_da_1]; list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Khi một bạn tham gia CLB Toán thì xác suất bạn đó là nữ là: $P(A / B) = %s$. (kết quả làm tròn đến hàng phần trăm)' % f_com(pA_B_round)
            vdc_da_1_s = 'Khi một bạn tham gia CLB Toán thì xác suất bạn đó là nữ là: $P(A / B) = %s$. (kết quả làm tròn đến hàng phần trăm)' % f_com(round(pA_B_round + 0.02, 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có: $P(A / B) = \\dfrac{P(A \\cap B)}{P(B)} = \\dfrac{P(A) \\cdot P(B|A)}{P(B)} = \\dfrac{%s \\cdot %s}{%s} \\approx %s$.''' 
                             % (f_com(pA), f_com(pB_A), f_com(pB_val), f_com(pA_B_round)))

            list_vdc_1 = [vdc_da_1]; list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # --- BƯỚC 3: KIỂM TRA ĐIỀU KIỆN 1-3 ĐÁP ÁN ĐÚNG ---
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

            # Gán lại giá trị cuối cùng sau khi thỏa mãn điều kiện
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # --- BƯỚC 4: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

