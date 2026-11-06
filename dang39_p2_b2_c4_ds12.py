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


def bt_dang39_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy và làm tròn
            def format_num(val, precision=5):
                if isinstance(val, float):
                    # Làm tròn theo độ chính xác yêu cầu
                    val = round(val, precision)
                    # Chuyển thành chuỗi và thay dấu chấm bằng dấu phẩy
                    s = str(val)
                    if s.endswith('.0'):
                        s = s[:-2]
                    return s.replace('.', ',')
                return str(val)

            # B1 & B3: Nghiên cứu đề bài và thiết lập thông số ngẫu nhiên
            # Tỉ lệ nhiễm virus (P(V))
            p_v_val = random.choice([0.01, 0.015, 0.02]) 
            p_v_pct = format_num(p_v_val * 100)

            # Tỉ lệ dương tính thật (Độ nhạy - P(DT|V))
            p_dt_v_val = random.randint(750, 850) / 1000.0
            p_dt_v_pct = format_num(p_dt_v_val * 100)

            # Tỉ lệ âm tính thật (Độ đặc hiệu - P(AT|K))
            p_at_k_val = random.randint(985, 995) / 1000.0
            p_at_k_pct = format_num(p_at_k_val * 100)

            # Các giá trị tính toán để làm lời giải và đáp án
            p_k_val = 1 - p_v_val
            p_at_v_val = 1 - p_dt_v_val
            p_dt_k_val = 1 - p_at_k_val
            p_dt_val = p_dt_v_val * p_v_val + p_dt_k_val * p_k_val
            p_v_dt_val = (p_dt_v_val * p_v_val) / p_dt_val

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một loại xét nghiệm nhanh cúm mùa cho kết quả dương tính với %s\\%% các ca thực sự nhiễm virus và kết quả âm tính với %s\\%% các ca thực sự không nhiễm virus. Giả sử tỉ lệ người nhiễm virus cúm mùa trong một cộng đồng là %s\\%%. Xét tính đúng sai của các khẳng định sau:''' 
                             %(p_dt_v_pct, p_at_k_pct, p_v_pct))

            ########################################################################
            # Nhận biết: Xác suất âm tính giả P(AT|V)
            ########################################################################
            ans_nb_correct = p_at_v_val
            ans_nb_wrong = round(p_at_v_val - 0.008, 2) # Tạo giá trị sai gần giống

            nb_da_1_d = '\\True Xác suất xét nghiệm cho kết quả âm tính của các ca thực sự nhiễm virus là: %s' % format_num(ans_nb_correct)
            nb_da_1_s = 'Xác suất xét nghiệm cho kết quả âm tính của các ca thực sự nhiễm virus là: %s' % format_num(ans_nb_wrong)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Xác suất xét nghiệm cho kết quả âm tính của các ca thực sự nhiễm virus là: $P(AT|V) = 1 - P(DT|V) = 1 - %s = %s$.''' 
                            % (format_num(p_dt_v_val), format_num(ans_nb_correct)))

            ########################################################################
            # Thông hiểu: Xác suất dương tính giả P(DT|K)
            ########################################################################
            ans_th_correct = p_dt_k_val
            ans_th_wrong = round(p_dt_k_val + 0.005, 3)

            th_da_1_d = '\\True Xác suất xét nghiệm cho kết quả dương tính của các ca thực sự không nhiễm virus là: %s' % format_num(ans_th_correct)
            th_da_1_s = 'Xác suất xét nghiệm cho kết quả dương tính của các ca thực sự không nhiễm virus là: %s' % format_num(ans_th_wrong)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Xác suất xét nghiệm cho kết quả dương tính của các ca thực sự không nhiễm virus là: $P(DT|K) = 1 - P(AT|K) = 1 - %s\\%% = %s$.''' 
                            % (p_at_k_pct, format_num(ans_th_correct)))

            ########################################################################
            # Vận dụng: Xác suất xét nghiệm dương tính P(DT)
            ########################################################################
            ans_vd_correct = p_dt_val
            ans_vd_wrong = round(p_dt_val - 0.001, 4)

            vd_da_1_d = '\\True Xác suất người làm xét nghiệm có kết quả dương tính là: %s' % format_num(ans_vd_correct)
            vd_da_1_s = 'Xác suất người làm xét nghiệm có kết quả dương tính là: %s' % format_num(ans_vd_wrong)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Xác suất người làm xét nghiệm có kết quả dương tính là: \\\\ $P(DT) = P(DT|V) \\cdot P(V) + P(DT|K) \\cdot P(K) = %s \\cdot %s + %s \\cdot %s = %s$.''' 
                            % (format_num(p_dt_v_val), format_num(p_v_val), format_num(p_dt_k_val), format_num(p_k_val), format_num(ans_vd_correct)))

            ########################################################################
            # Vận dụng cao: Xác suất thực sự bệnh khi biết dương tính P(V|DT)
            ########################################################################
            ans_vdc_correct = round(p_v_dt_val, 2)
            ans_vdc_wrong = round(p_v_dt_val - 0.1, 2)

            vdc_da_1_d = '\\True Biết rằng đã có kết quả chuẩn đoán là dương tính, xác suất để người đó thực sự bị bệnh là %s (làm tròn đến hàng phần trăm)' % format_num(ans_vdc_correct)
            vdc_da_1_s = 'Biết rằng đã có kết quả chuẩn đoán là dương tính, xác suất để người đó thực sự bị bệnh là %s (làm tròn đến hàng phần trăm)' % format_num(ans_vdc_wrong)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Sử dụng định lý Bayes, xác suất để người có kết quả dương tính thực sự bị bệnh là: \\\\ $P(V|DT) = \\frac{P(DT|V) \\cdot P(V)}{P(DT)} = \\frac{%s \\cdot %s}{%s} = \\frac{%s}{%s} \\approx %s$.''' 
                             % (format_num(p_dt_v_val), format_num(p_v_val), format_num(p_dt_val), format_num(p_dt_v_val*p_v_val), format_num(p_dt_val), format_num(ans_vdc_correct)))

            # Logic chọn đáp án để có từ 1 đến 3 câu đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_final = random.choice(list_nb_da_1)
                th_da_final = random.choice(list_th_da_1)
                vd_da_final = random.choice(list_vd_da_1)
                vdc_da_final = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_da_final, th_da_final, vd_da_final, vdc_da_final]) <= 3:
                    break

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_final) + '}\n'
                '{' + str(th_da_final) + '}\n'
                '{' + str(vd_da_final) + '}\n'
                '{' + str(vdc_da_final) + '}\n'
                '\\loigiai{ \n'
                'Gọi $V$ là biến cố người nhiễm virus, $K$ là biến cố người không nhiễm virus. \\\\ \n'
                'Theo bài ra ta có: $P(V) = ' + format_num(p_v_val) + '$; $P(K) = 1 - P(V) = ' + format_num(p_k_val) + '$. \\\\ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

