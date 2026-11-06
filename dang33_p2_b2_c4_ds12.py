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


def bt_dang33_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy và làm tròn
            def fmt(num):
                # Làm tròn đến 4 chữ số thập phân để tránh sai số máy tính
                s = str(round(float(num), 4))
                if s.endswith('.0'):
                    s = s[:-2]
                return s.replace('.', ',')

            # 1. Khởi tạo các thông số ngẫu nhiên cho bài toán
            # p_A: Tỉ lệ bài viết đạo văn (%)
            # p_correct: Tỉ lệ phát hiện đúng nếu là đạo văn (%)
            # p_false_alarm: Tỉ lệ báo nhầm nếu là chính chủ (%)

            p_A_val = random.randint(1, 3)  # 1% đến 3%
            p_notA_val = 100 - p_A_val
            p_correct_val = random.randint(95, 99) # 95% đến 99%
            p_false_alarm_val = random.randint(2, 5) # 2% đến 5%

            # Chuyển sang số thập phân để tính toán
            P_A = p_A_val / 100
            P_notA = p_notA_val / 100
            P_B_given_A = p_correct_val / 100
            P_B_given_notA = p_false_alarm_val / 100

            # Tính toán các giá trị xác suất thành phần
            P_AnB = P_A * P_B_given_A
            P_notAnB = P_notA * P_B_given_notA
            P_B = P_AnB + P_notAnB
            P_A_cond_B = P_AnB / P_B

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hệ thống AI được sử dụng để kiểm tra đạo văn trong các bài viết học sinh nộp. Theo thống kê: có $%s\\%%$ bài viết là đạo văn, $%s\\%%$ bài viết là chính chủ (không đạo văn). Phần mềm kiểm tra có độ chính xác như sau: Nếu bài viết là đạo văn, phần mềm phát hiện đúng với xác suất $%s\\%%$; Nếu bài viết là chính chủ, phần mềm nhầm là đạo văn với xác suất $%s\\%%$. Kiểm tra ngẫu nhiên một bài viết của học sinh nộp.
            Gọi $A$ là biến cố: "Bài viết thực sự là đạo văn".
            Gọi $B$ là biến cố: "Phần mềm báo bài viết là đạo văn".''' 
            % (fmt(p_A_val), fmt(p_notA_val), fmt(p_correct_val), fmt(p_false_alarm_val)))

            ########################################################################
            # a) Xác suất P(B)
            pb_val_true = fmt(P_B)
            pb_val_false = fmt(P_B + 0.01)
            nb_da_1_d = '\\True Xác suất $P(B) = %s$' % pb_val_true
            nb_da_1_s = 'Xác suất $P(B) = %s$' % pb_val_false
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Do $A$ và $\\bar{A}$ là một hệ đầy đủ, theo công thức xác suất đầy đủ ta có: \\\\
            Xác suất $P(B) = P(A \\cap B) + P(\\bar{A} \\cap B) = P(A) \\cdot P(B|A) + P(\\bar{A}) \\cdot P(B|\\bar{A})$ \\\\
            $= %s \\cdot %s + %s \\cdot %s = %s$.''' 
            % (fmt(P_A), fmt(P_B_given_A), fmt(P_notA), fmt(P_B_given_notA), fmt(P_B)))

            ########################################################################
            # b) Xác suất P(A) và P(not A)
            th_da_1_d = '\\True Xác suất $P(A) = %s$ và $P(\\bar{A}) = %s$' % (fmt(P_A), fmt(P_notA))
            th_da_1_s = 'Xác suất $P(A) = %s$ và $P(\\bar{A}) = %s$' % (fmt(P_notA), fmt(P_A))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Từ giả thiết ta có: Tỉ lệ đạo văn là $%s\\%%$ nên $P(A) = %s$. \\\\
            Tỉ lệ chính chủ là $%s\\%%$ nên $P(\\bar{A}) = 1 - P(A) = %s$.''' 
            % (fmt(p_A_val), fmt(P_A), fmt(p_notA_val), fmt(P_notA)))

            ########################################################################
            # c) Xác suất có điều kiện P(A|B)
            pacond_val_true = fmt(P_A_cond_B)
            pacond_val_false = fmt(0.7) if P_A_cond_B != 0.7 else fmt(0.5)
            vd_da_1_d = '\\True Xác suất có điều kiện $P(A | B) = %s$' % pacond_val_true
            vd_da_1_s = 'Xác suất có điều kiện $P(A | B) = %s$' % pacond_val_false
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Xác suất có điều kiện $P(A | B) = \\dfrac{P(A \\cap B)}{P(B)} = \\dfrac{%s \\cdot %s}{%s} \\approx %s$.''' 
            % (fmt(P_A), fmt(P_B_given_A), fmt(P_B), fmt(P_A_cond_B)))

            ########################################################################
            # d) So sánh khả năng
            # So sánh P(notA | B) và P(A | B) tương đương so sánh P(notA \cap B) và P(A \cap B)
            if P_notAnB > P_AnB:
                vdc_da_1_d = '\\True Trong số những bài viết bị phần mềm cảnh báo là đạo văn, có nhiều khả năng là bài viết chính chủ hơn là đạo văn'
                vdc_da_1_s = 'Trong số những bài viết bị phần mềm cảnh báo là đạo văn, có nhiều khả năng là bài viết đạo văn hơn là chính chủ'
            else:
                vdc_da_1_d = '\\True Trong số những bài viết bị phần mềm cảnh báo là đạo văn, có nhiều khả năng là bài viết đạo văn hơn là chính chủ'
                vdc_da_1_s = 'Trong số những bài viết bị phần mềm cảnh báo là đạo văn, có nhiều khả năng là bài viết chính chủ hơn là đạo văn'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Ta có các xác suất thành phần của biến cố $B$: \\\\
            Xác suất bài đạo văn bị báo lỗi: $P(A \\cap B) = %s \\cdot %s = %s$. \\\\
            Xác suất bài chính chủ bị báo nhầm: $P(\\bar{A} \\cap B) = %s \\cdot %s = %s$. \\\\
            Vì $%s > %s$ nên trong số bài bị cảnh báo, khả năng là bài %s cao hơn.''' 
            % (fmt(P_A), fmt(P_B_given_A), fmt(P_AnB), 
               fmt(P_notA), fmt(P_B_given_notA), fmt(P_notAnB),
               fmt(max(P_AnB, P_notAnB)), fmt(min(P_AnB, P_notAnB)),
               "chính chủ" if P_notAnB > P_AnB else "đạo văn"))

            ########################################################################
            # Xử lý chọn đáp án đảm bảo từ 1 đến 3 câu đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_da_1, th_da_1, vd_da_1, vdc_da_1]) <= 3:
                    break

            # Đóng gói lời giải (giữ nguyên thứ tự a, b, c, d tương ứng với nội dung)
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

