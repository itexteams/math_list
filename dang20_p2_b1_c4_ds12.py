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


def bt_dang20_p2_b1_c4_ds12(self):
            # Khai báo biến
            def generate_data():
                while True:
                    T = random.randint(80, 110)
                    M = random.randint(45, T - 30)
                    F = T - M
                    H = random.randint(H_min := max(M, F), T - 2) # Giả định số đạt giải cao
                    MH = random.randint(40, min(M, H) - 5)
                    FH = H - MH
                    if FH > 0 and FH < F:
                        return T, M, F, H, MH, FH

            T, M, F, H, MH, FH = generate_data()

            # --- Nội dung câu hỏi ---
            noidungcauhoi = ('''Một trường THPT Chuyên cử một đội tuyển gồm %s học sinh tham dự kỳ thi Học sinh giỏi cấp Quốc gia. Đội tuyển có cả học sinh nam và học sinh nữ. Sau kỳ thi, kết quả thống kê cho thấy có %s học sinh đạt huy chương. Thông tin chi tiết như sau:\\\\
            - Trong tổng số %s học sinh, có %s học sinh nam và %s học sinh nữ.\\\\
            - Trong số %s học sinh đạt huy chương, có %s học sinh nam.\\\\
            Chọn ngẫu nhiên một học sinh từ đội tuyển sau khi cuộc thi kết thúc.''' 
            %(latex(T), latex(H), latex(T), latex(M), latex(F), latex(H), latex(MH)))

            ########################################################################
            # Nhận biết (Câu a) ############################################
            p_a_true = Rational(F, T)
            p_a_false = Rational(M, T)

            nb_da_1_d = '\\True Xác suất chọn được một học sinh nữ là $%s$' % (latex(p_a_true))
            nb_da_1_s = 'Xác suất chọn được một học sinh nữ là $%s$' % (latex(p_a_false))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Số học sinh nữ là $n(F) = %s$. Không gian mẫu $n(\\Omega) = %s$. \\\\ Xác suất chọn được một học sinh nữ: $P(F) = \\frac{n(F)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.''' 
                            % (latex(F), latex(T), latex(F), latex(T), latex(p_a_true)))

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            p_b_true = Rational(MH, T)
            p_b_false = Rational(FH, T)

            th_da_1_d = '\\True Xác suất chọn được một học sinh nam đạt huy chương là $%s$' % (latex(p_b_true))
            th_da_1_s = 'Xác suất chọn được một học sinh nam đạt huy chương là $%s$' % (latex(p_b_false))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Số học sinh nam đạt huy chương là $n(N \\cap H) = %s$. \\\\ Xác suất chọn được một học sinh nam đạt huy chương: $P(N \\cap H) = \\frac{n(N \\cap H)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.''' 
                            % (latex(MH), latex(MH), latex(T), latex(p_b_true)))

            ########################################################################
            # Vận dụng (Câu c) ############################################
            p_c_true = Rational(MH, M)
            p_c_false = Rational(MH, H)

            vd_da_1_d = '\\True Biết rằng học sinh được chọn là nam, xác suất học sinh đó đạt huy chương là $%s$' % (latex(p_c_true))
            vd_da_1_s = 'Biết rằng học sinh được chọn là nam, xác suất học sinh đó đạt huy chương là $%s$' % (latex(p_c_false))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xác suất học sinh đạt huy chương, biết rằng học sinh đó là nam: \\\\ $P(H|N) = \\frac{P(N \\cap H)}{P(N)} = \\frac{%s/%s}{%s/%s} = \\frac{%s}{%s} = %s$.''' 
                            % (latex(MH), latex(T), latex(M), latex(T), latex(MH), latex(M), latex(p_c_true)))

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            p_d_true = Rational(FH, H)
            p_d_false = Rational(FH, T)

            vdc_da_1_d = '\\True Biết rằng học sinh được chọn đã đạt huy chương, xác suất học sinh đó là nữ là $%s$' % (latex(p_d_true))
            vdc_da_1_s = 'Biết rằng học sinh được chọn đã đạt huy chương, xác suất học sinh đó là nữ là $%s$' % (latex(p_d_false))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Số học sinh nữ đạt huy chương là $n(F \\cap H) = n(H) - n(N \\cap H) = %s - %s = %s$. \\\\ Xác suất học sinh là nữ, biết rằng học sinh đó đã đạt huy chương: \\\\ $P(F|H) = \\frac{P(F \\cap H)}{P(H)} = \\frac{%s/%s}{%s/%s} = \\frac{%s}{%s} = %s$.''' 
                             % (latex(H), latex(MH), latex(FH), latex(FH), latex(T), latex(H), latex(T), latex(FH), latex(H), latex(p_d_true)))

            # --- Phần Logic chọn số đáp án Đúng/Sai (từ 1 đến 3) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán và trộn (Shuffle)
            combined_nb = list(zip([nb_da_1], list_nb_2))
            combined_th = list(zip([th_da_1], list_th_2))
            combined_vd = list(zip([vd_da_1], list_vd_2))
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # --- Xuất kết quả ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + 
                '\n \\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                'Kí hiệu: \n'
                '$N$: Học sinh được chọn là nam; $F$: Học sinh được chọn là nữ. \\\\'
                '$H$: Học sinh được chọn đạt huy chương. \\\\'
                'Tổng số học sinh (không gian mẫu): $n(\\Omega) = ' + latex(T) + '$. \\\\'
                'Thông tin từ đề bài: $n(N) = ' + latex(M) + '; n(F) = ' + latex(F) + '; n(H) = ' + latex(H) + '; n(N \\cap H) = ' + latex(MH) + '$. \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

