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


def bt_dang26_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ chuyển dấu chấm thành dấu phẩy cho số thập phân
            def f_n(val):
                return str(val).replace('.', ',')

            # B3 - Suy nghĩ tìm cách random bài toán:
            # Ta sẽ random tỷ lệ trẻ em (pA), từ đó tính ra người lớn (100-pA).
            # Random các tỷ lệ thành phần của trẻ em (pB_A, pC_A, pD_A) sao cho tổng = 100.
            # Random các tỷ lệ thành phần của người lớn (pB_notA, pC_notA, pD_notA) sao cho tổng = 100.

            # Thiết lập thông số random
            pA = random.choice([60, 70, 80]) # Tỷ lệ trẻ em
            p_notA = 100 - pA

            # Trẻ em: B (thích+đi tiếp), C (thích+không đi), D (không thích+không đi)
            pB_A = random.choice([40, 50, 60])
            pC_A = random.choice([20, 30])
            pD_A = 100 - pB_A - pC_A

            # Người lớn:
            pB_notA = random.choice([10, 20])
            pC_notA = 10
            pD_notA = 100 - pB_notA - pC_notA

            # Chuyển sang số thập phân để tính toán
            P_A = pA / 100
            P_notA = p_notA / 100
            PB_condA = pB_A / 100
            PC_condA = pC_A / 100
            PD_condA = pD_A / 100
            PB_condNotA = pB_notA / 100
            PC_condNotA = pC_notA / 100
            PD_condNotA = pD_notA / 100

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khảo sát những người xem bộ phim hoạt hình vừa được phát hành cho thấy %s\\%% người xem là trẻ em và %s\\%% là người lớn. Trong số các trẻ em đến xem phim có %s\\%% yêu thích bộ phim và khẳng định sẽ đi xem tiếp phần 2; %s\\%% yêu thích bộ phim nhưng sẽ không xem tiếp phần 2; %s\\%% còn lại không thích bộ phim và không đi xem tiếp phần 2. Trong số những người lớn đi xem phim có %s\\%% yêu thích bộ phim và khẳng định sẽ đi xem tiếp phần 2; %s\\%% yêu thích bộ phim nhưng sẽ không xem tiếp phần 2; %s\\%% còn lại không thích bộ phim và không đi xem tiếp phần 2. Chọn ngẫu nhiên 1 người đã xem phim.''' 
                             %(pA, p_notA, pB_A, pC_A, pD_A, pB_notA, pC_notA, pD_notA))

            # Các tính toán đáp án đúng
            val_a = PB_condA + PC_condA
            P_C = PC_condA * P_A + PC_condNotA * P_notA
            P_D = PD_condA * P_A + PD_condNotA * P_notA
            val_b = round(P_C + P_D, 2)
            P_B = PB_condA * P_A + PB_condNotA * P_notA
            val_c = round((PB_condA * P_A) / P_B, 3)
            P_B_or_C = P_B + P_C
            val_d = round(P_C / P_B_or_C, 2)

            ########################################################################
            # Nhận biết
            nb_da_1_d = '\\True Biết người được chọn là trẻ em, xác suất để người đó yêu thích bộ phim là %s.' %(f_n(val_a))
            nb_da_1_s = 'Biết người được chọn là trẻ em, xác suất để người đó yêu thích bộ phim là %s.' %(f_n(round(val_a - 0.24, 2)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Gọi $A$ là biến cố: "Người được chọn là trẻ em", suy ra $\\overline{A}$ là biến cố "Người được chọn là người lớn".\\\\ 
            Gọi $B$ là biến cố: "Người được chọn thích và xem tiếp bộ phim".\\\\ 
            Gọi $C$ là biến cố: "Người được chọn thích và không xem tiếp bộ phim".\\\\ 
            Biết người được chọn là trẻ em, xác suất để người đó yêu thích bộ phim là: 
            $P((B \\cup C)|A) = \\frac{P((B \\cup C) \\cap A)}{P(A)} = \\frac{P(B \\cap A) + P(C \\cap A)}{P(A)} = \\frac{%s \\cdot %s + %s \\cdot %s}{%s} = %s$.''' 
            %(f_n(PB_condA), f_n(P_A), f_n(PC_condA), f_n(P_A), f_n(P_A), f_n(val_a)))

            ########################################################################
            # Thông hiểu
            th_da_1_d = '\\True Xác suất để người đó không xem tiếp phần 2 là %s' %(f_n(val_b))
            th_da_1_s = 'Xác suất để người đó không xem tiếp phần 2 là %s' %(f_n(round(val_b + 0.1, 2)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('''Gọi $D$ là biến cố: "Người được chọn không thích và không xem tiếp bộ phim".\\\\ 
            Người không xem tiếp phần 2 thuộc biến cố $C \\cup D$.\\\\ 
            Ta có $P(C \\cup D) = P(C \\cup D | A)P(A) + P(C \\cup D | \\overline{A})P(\\overline{A})$\\\\ 
            $= (%s + %s) \\cdot %s + (%s + %s) \\cdot %s = %s$.''' 
            %(f_n(PC_condA), f_n(PD_condA), f_n(P_A), f_n(PC_condNotA), f_n(PD_condNotA), f_n(P_notA), f_n(val_b)))

            ########################################################################
            # Vận dụng
            vd_da_1_d = '\\True Biết người đó sẽ xem tiếp phần 2, xác suất để người đó là trẻ em lớn hơn %s' %(f_n(round(val_c - 0.004, 2)))
            vd_da_1_s = 'Biết người đó sẽ xem tiếp phần 2, xác suất để người đó là trẻ em nhỏ hơn %s' %(f_n(round(val_c - 0.1, 2)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Ta phải tính xác suất có điều kiện $P(A|B) = \\frac{P(AB)}{P(B)}$.\\\\ 
            Tính $P(AB) = P(B|A)P(A) = %s \\cdot %s = %s$.\\\\ 
            Tính $P(B) = P(B|A)P(A) + P(B|\\overline{A})P(\\overline{A}) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\ 
            Vậy $P(A|B) = \\frac{%s}{%s} \\approx %s$.''' 
            %(f_n(PB_condA), f_n(P_A), f_n(round(PB_condA*P_A, 4)), f_n(PB_condA), f_n(P_A), f_n(PB_condNotA), f_n(P_notA), f_n(round(P_B, 2)), f_n(round(PB_condA*P_A, 4)), f_n(round(P_B, 2)), f_n(val_c)))

            ########################################################################
            # Vận dụng cao
            vdc_da_1_d = '\\True Biết người đó yêu thích bộ phim, xác suất để người đó không xem tiếp phần 2 là %s' %(f_n(val_d))
            vdc_da_1_s = 'Biết người đó yêu thích bộ phim, xác suất để người đó không xem tiếp phần 2 là %s' %(f_n(round(val_d + 0.15, 2)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = ('''Người yêu thích bộ phim là biến cố $B \\cup C$, người không xem tiếp là biến cố $C$.\\\\ 
            Cần tính $P(C | B \\cup C) = \\frac{P(C \\cap (B \\cup C))}{P(B \\cup C)} = \\frac{P(C)}{P(B \\cup C)}$.\\\\ 
            Ta có $P(C) = P(C|A)P(A) + P(C|\\overline{A})P(\\overline{A}) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\ 
            $P(B \\cup C) = P(B \\cup C|A)P(A) + P(B \\cup C|\\overline{A})P(\\overline{A}) = (%s + %s)%s + (%s + %s)%s = %s$.\\\\ 
            Xác suất cần tìm là $\\frac{%s}{%s} \\approx %s$.''' 
            %(f_n(PC_condA), f_n(P_A), f_n(PC_condNotA), f_n(P_notA), f_n(round(P_C, 2)), f_n(PB_condA), f_n(PC_condA), f_n(P_A), f_n(PB_condNotA), f_n(PC_condNotA), f_n(P_notA), f_n(round(P_B_or_C, 2)), f_n(round(P_C, 2)), f_n(round(P_B_or_C, 2)), f_n(val_d)))

            # Hàm kiểm tra số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp chọn bộ đáp án
            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    break

            shuffled_answers = [d1, d2, d3, d4]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung (không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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

