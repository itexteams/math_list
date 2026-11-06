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


def bt_dang15_p2_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn tham số ngẫu nhiên
            ten = random.choice(['Bà Hoa', 'Ông Nam', 'Bà Lan', 'Ông Minh', 'Bà Mai'])
            ten_ngan = ten.split()[0]

            A = random.choice([100, 150, 200, 250, 300])
            r_pct = random.choice([4, 5, 6, 7, 8])
            r_val = r_pct / 100.0
            r_str = ("0,0" + str(r_pct)) if r_pct < 10 else ("0," + str(r_pct))

            n1 = 1
            n2 = 2
            n3 = randint(12, 15)
            n4 = randint(16, 20)

            # Tính toán giá trị đúng
            t1 = A * (1 + r_val / 12)**n1
            t2 = A * (1 + r_val / 12)**n2
            t3 = A * (1 + r_val / 12)**n3
            t4 = A * (1 + r_val / 12)**n4

            t1_str = f"{t1:.2f}".replace('.', ',')
            t2_str = f"{t2:.2f}".replace('.', ',')
            t3_str = f"{t3:.2f}".replace('.', ',')
            t4_str = f"{t4:.2f}".replace('.', ',')

            # Tạo các giá trị sai
            t1_w_str = f"{t1 + 0.5:.2f}".replace('.', ',')
            t2_w_str = f"{t2 + 0.8:.2f}".replace('.', ',')
            t3_w_str = f"{t3 - 1.5:.2f}".replace('.', ',')
            t4_w_str = f"{t4 + 1.0:.2f}".replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''%s gửi vào một ngân hàng số tiền %s triệu đồng với lãi suất %s\\%% một năm theo hình thức lãi kép, kì hạn 1 tháng. Số tiền (triệu đồng) của %s sau $n$ tháng được tính theo công thức $T_n = %s\\left(1 + \\frac{%s}{12}\\right)^n$.'''
                             % (ten, A, r_pct, ten, A, r_str))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Sau %s tháng, số tiền %s nhận được là khoảng %s (triệu đồng)' % (n1, ten, t1_str)
            nb_da_1_s = 'Sau %s tháng, số tiền %s nhận được là khoảng %s (triệu đồng)' % (n1, ten, t1_w_str)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Sau %s tháng ($n = %s$), số tiền %s nhận được là $T_%s = %s \\cdot \\left(1 + \\frac{%s}{12}\\right)^{%s} \\approx %s$ (triệu đồng).'''
                            % (n1, n1, ten, n1, A, r_str, n1, t1_str))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Sau %s tháng, số tiền %s nhận được là khoảng %s (triệu đồng)' % (n2, ten_ngan, t2_str)
            th_da_1_s = 'Sau %s tháng, số tiền %s nhận được là khoảng %s (triệu đồng)' % (n2, ten_ngan, t2_w_str)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Sau %s tháng ($n = %s$), số tiền %s nhận được là $T_%s = %s \\cdot \\left(1 + \\frac{%s}{12}\\right)^{%s} \\approx %s$ (triệu đồng).'''
                            % (n2, n2, ten_ngan, n2, A, r_str, n2, t2_str))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Sau %s tháng, số tiền %s nhận được là khoảng %s (triệu đồng)' % (n3, ten_ngan, t3_str)
            vd_da_1_s = 'Sau %s tháng, số tiền %s nhận được là khoảng %s (triệu đồng)' % (n3, ten_ngan, t3_w_str)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Sau %s tháng ($n = %s$), số tiền %s nhận được là $T_{%s} = %s \\cdot \\left(1 + \\frac{%s}{12}\\right)^{%s} \\approx %s$ (triệu đồng).'''
                            % (n3, n3, ten_ngan, n3, A, r_str, n3, t3_str))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Sau %s tháng, số tiền %s nhận được là khoảng %s (triệu đồng)' % (n4, ten_ngan, t4_str)
            vdc_da_1_s = 'Sau %s tháng, số tiền %s nhận được là khoảng %s (triệu đồng)' % (n4, ten_ngan, t4_w_str)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Sau %s tháng ($n = %s$), số tiền %s nhận được là $T_{%s} = %s \\cdot \\left(1 + \\frac{%s}{12}\\right)^{%s} \\approx %s$ (triệu đồng).'''
                             % (n4, n4, ten_ngan, n4, A, r_str, n4, t4_str))

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

            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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

