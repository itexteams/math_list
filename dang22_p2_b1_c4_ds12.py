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


def bt_dang22_p2_b1_c4_ds12(self):
            # Khai báo biến
            # Hàm định dạng số thập phân dùng dấu phẩy
            def format_num(val):
                return str(val).replace('.', ',')

            # Khởi tạo các giá trị xác suất ngẫu nhiên nhưng đảm bảo logic
            # P(A): xác suất dự án 1; P(B): xác suất dự án 2; P(AB): xác suất cả hai
            # Điều kiện: P(AB) <= min(P(A), P(B)) và P(A) + P(B) - P(AB) <= 1
            while True:
                pA = random.choice([0.4, 0.5, 0.6])
                pB = random.choice([0.5, 0.6, 0.7])
                pAB = random.choice([0.2, 0.3, 0.4])
                if pAB < min(pA, pB) and (pA + pB - pAB) <= 1:
                    # Đảm bảo không độc lập để giống bài mẫu
                    if pAB != round(pA * pB, 2):
                        break

            pnotA = round(1 - pA, 2)
            pB_given_notA = round((pB - pAB) / pnotA, 2)
            pB_given_A = round(pAB / pA, 2)
            p_exactly_one = round((pA - pAB) + (pB - pAB), 2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một công ty truyền thông đấu thầu 2 dự án. Khả năng thắng thầu dự án 1 là $%s$ và dự án 2 là $%s$. Khả năng thắng thầu cả hai dự án là $%s$. Gọi $A, B$ lần lượt là các biến cố thắng thầu dự án 1 và dự án 2.''' 
                             %(format_num(pA), format_num(pB), format_num(pAB)))

            ########################################################################
            # Nhận biết - Câu a: Xác suất có điều kiện P(B|not A)
            ########################################################################
            nb_da_1_d = '\\True Biết công ty không thắng thầu dự án 1, xác suất để công ty thắng thầu dự án 2 là $%s$' % format_num(pB_given_notA)
            nb_da_1_s = 'Biết công ty không thắng thầu dự án 1, xác suất để công ty thắng thầu dự án 2 là $%s$' % format_num(pB_given_A)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Ta có $P(B|\\bar{A}) = \\frac{P(B\\bar{A})}{P(\\bar{A})} = \\frac{P(B)-P(AB)}{1-P(A)} = \\frac{%s-%s}{1-%s} = %s$.''' 
                            %(format_num(pB), format_num(pAB), format_num(pA), format_num(pB_given_notA)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip([nb_da_1], list_nb_2))
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu - Câu b: Tính độc lập
            ########################################################################
            th_da_1_d = ' $A$ và $B$ là hai biến cố độc lập.' if pAB == round(pA*pB, 2) else '\\True $A$ và $B$ là hai biến cố không độc lập'
            th_da_1_s = '\\True $A$ và $B$ là hai biến cố độc lập.' if pAB == round(pA*pB, 2) else ' $A$ và $B$ là hai biến cố độc lập'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $P(A) \\cdot P(B) = %s \\cdot %s = %s$. Vì $P(AB) = %s %s P(A) \\cdot P(B)$ nên hai biến cố $A$ và $B$ %s độc lập.''' 
                            %(format_num(pA), format_num(pB), format_num(round(pA*pB, 2)), format_num(pAB), '=' if pAB == round(pA*pB, 2) else '\\neq', '' if pAB == round(pA*pB, 2) else 'không'))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip([th_da_1], list_th_2))
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng - Câu c: Xác suất có điều kiện P(B|A)
            ########################################################################
            vd_da_1_d = '\\True Biết công ty thắng thầu dự án 1, xác suất để công ty thắng thầu dự án 2 là $%s$' % format_num(pB_given_A)
            vd_da_1_s = 'Biết công ty thắng thầu dự án 1, xác suất để công ty thắng thầu dự án 2 là $%s$' % format_num(pB_given_notA)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có $P(B|A) = \\frac{P(AB)}{P(A)} = \\frac{%s}{%s} = %s$.''' 
                            %(format_num(pAB), format_num(pA), format_num(pB_given_A)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip([vd_da_1], list_vd_2))
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao - Câu d: Xác suất thắng đúng 1 dự án
            ########################################################################
            vdc_da_1_d = '\\True Xác suất để công ty thắng thầu đúng một dự án là $%s$' % format_num(p_exactly_one)
            vdc_da_1_s = 'Xác suất để công ty thắng thầu đúng một dự án là $%s$' % format_num(round(pA + pB - pAB, 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xác suất để công ty thắng thầu đúng một dự án là: \\\\ $P(A\\bar{B}) + P(\\bar{A}B) = P(A) - P(AB) + P(B) - P(AB) = %s - %s + %s - %s = %s$.''' 
                             %(format_num(pA), format_num(pAB), format_num(pB), format_num(pAB), format_num(p_exactly_one)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm soát số lượng đáp án đúng (từ 1 đến 3)
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Gán kết quả cuối cùng
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

