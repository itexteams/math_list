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


def bt_dang19_p2_b1_c4_ds12(self):
            # Khai báo biến
            # Random tổng số học sinh N là bội của 300 để P(T) = 2/3
            k = random.randint(1, 3)
            N = 600 * k
            n_T = 400 * k
            n_notT = N - n_T

            # Tỉ lệ giỏi toán (p1, p2) chuyển thành Rational để tính toán phân số
            p1_val = random.choice([60, 70, 80])
            p2_val = random.choice([5, 10, 15])

            # Chuyển tỉ lệ phần trăm sang phân số Rational
            p_G_T_rat = Rational(p1_val, 100)
            p_G_notT_rat = Rational(p2_val, 100)

            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy cho phần giả thiết
            def format_decimal(value):
                return str(float(value)).replace('.', ',')

            # Tính toán các giá trị xác suất dưới dạng Rational
            prob_T = Rational(n_T, N)
            prob_notT = 1 - prob_T

            # P(G) = P(G|T).P(T) + P(G|notT).P(notT)
            prob_G = p_G_T_rat * prob_T + p_G_notT_rat * prob_notT

            # P(T|G) = (P(G|T).P(T)) / P(G)
            prob_T_G = (p_G_T_rat * prob_T) / prob_G
            percent_T_G_approx = round(float(prob_T_G) * 100)

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Trong cuộc khảo sát ngẫu nhiên %s học sinh về việc "thích học" hay "không thích học" môn toán. Kết quả thống kê như sau: có %s học sinh trả lời "thích học" và %s học sinh trả lời "không thích học". Thực tế cho thấy tỉ lệ học sinh "giỏi toán" tương ứng với những cách trả lời "thích học" và "không thích học" lần lượt là %s\\%% và %s\\%%.\\\\
            Gọi $T$ là biến cố "Học sinh được phỏng vấn trả lời thích học môn toán".\\\\
            Gọi $G$ là biến cố "Học sinh được phỏng vấn giỏi toán".''' 
            % (N, n_T, n_notT, p1_val, p2_val))

            ########################################################################
            # a) Nhận biết: P(T) và P(not T)
            ########################################################################
            nb_da_1_d = '\\True Xác suất $P(T)=%s$ và $P(\\overline{T})=%s$' % (latex(prob_T), latex(prob_notT))
            nb_da_1_s = 'Xác suất $P(T)=%s$ và $P(\\overline{T})=%s$' % (latex(prob_notT), latex(prob_T))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Ta có $P(T) = \\frac{%s}{%s} = %s \\Rightarrow P(\\overline{T}) = 1 - P(T) = %s$.''' 
                            % (n_T, N, latex(prob_T), latex(prob_notT)))

            ########################################################################
            # b) Thông hiểu: Xác suất điều kiện
            ########################################################################
            th_da_1_d = '\\True Xác suất có điều kiện $P(G|T)=%s$, $P(G|\\overline{T})=%s$' % (latex(p_G_T_rat), latex(p_G_notT_rat))
            th_da_1_s = 'Xác suất có điều kiện $P(G|T)=%s$, $P(G|\\overline{T})=%s$' % (latex(p_G_notT_rat), latex(p_G_T_rat))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Theo đề bài ta có: $P(G|T) = %s\\%% = %s$, $P(G|\\overline{T}) = %s\\%% = %s$.''' 
                            % (p1_val, latex(p_G_T_rat), p2_val, latex(p_G_notT_rat)))

            ########################################################################
            # c) Vận dụng: Công thức xác suất đầy đủ (Kết quả Rational)
            ########################################################################
            vd_da_1_d = '\\True Xác suất $P(G)=%s$' % latex(prob_G)
            vd_da_1_s = 'Xác suất $P(G)=%s$' % latex(prob_G + Rational(1, 20))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có: $P(G) = P(GT) + P(G\\overline{T}) = P(G|T).P(T) + P(G|\\overline{T}).P(\\overline{T}) = %s.%s + %s.%s = %s$.''' 
                            % (latex(p_G_T_rat), latex(prob_T), latex(p_G_notT_rat), latex(prob_notT), latex(prob_G)))

            ########################################################################
            # d) Vận dụng cao: Công thức Bayes (Kết quả Rational)
            ########################################################################
            vdc_da_1_d = '\\True Trong số những người giỏi toán, xác suất người đó thích học là $P(T|G)=%s$' % latex(prob_T_G)
            vdc_da_1_s = 'Trong số những người giỏi toán, xác suất người đó thích học là $P(T|G)=%s$' % latex(prob_T_G * Rational(4, 5))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có: $P(T|G) = \\frac{P(TG)}{P(G)} = \\frac{P(G|T).P(T)}{P(G)} = \\frac{%s.%s}{%s} = %s \\approx %s\\%%$.''' 
                             % (latex(p_G_T_rat), latex(prob_T), latex(prob_G), latex(prob_T_G), percent_T_G_approx))

            # --- LOGIC KIỂM TRA SỐ ĐÁP ÁN ĐÚNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # --- XUẤT NỘI DUNG ---
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

