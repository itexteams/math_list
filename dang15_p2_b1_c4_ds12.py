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


def bt_dang15_p2_b1_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ chuyển số thập phân sang chuỗi có dấu phẩy
            def format_decimal(value):
                s = str(float(value)).replace('.', ',')
                if s.endswith(',0'):
                    s = s[:-2]
                return s

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Random các giá trị phần trăm đầu vào
            pA_val = random.choice([20, 30, 40, 50])        # % HS tham gia CLB thể thao
            pBgA_val = random.choice([60, 70, 80])         # % HS trong CLB biết bơi
            pBgnA_val = random.choice([10, 15, 20, 25])    # % HS ngoài CLB biết bơi

            # Tính toán các giá trị xác suất
            prob_A = Rational(pA_val, 100)
            prob_notA = 1 - prob_A
            prob_BgA = Rational(pBgA_val, 100)
            prob_BgnA = Rational(pBgnA_val, 100)

            # P(B) = P(A).P(B|A) + P(not A).P(B|not A)
            prob_B = prob_A * prob_BgA + prob_notA * prob_BgnA

            # P(A|B) = P(A).P(B|A) / P(B)
            prob_AgB = (prob_A * prob_BgA) / prob_B

            # Chuyển sang định dạng hiển thị (dấu phẩy)
            str_pA = format_decimal(prob_A)
            str_pnotA = format_decimal(prob_notA)
            str_pBgA = format_decimal(prob_BgA)
            str_pBgnA = format_decimal(prob_BgnA)
            str_pB = format_decimal(prob_B)
            str_pAgB = format_decimal(prob_AgB)

            # --- B2: Viết lại bài toán theo mẫu code ---

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tại một trường THPT có %s\\%% học sinh tham gia câu lạc bộ thể thao. Trong số những học sinh này có %s\\%% học sinh biết bơi. Ngoài ra, có %s\\%% số học sinh không tham gia câu lạc bộ thể thao cũng biết bơi. Chọn ngẫu nhiên một học sinh của trường. Xét các biến cố: $A$: "Chọn được học sinh thuộc câu lạc bộ thể thao"; $B$: "Chọn được học sinh biết bơi".''' 
                             % (pA_val, pBgA_val, pBgnA_val))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Xác suất chọn được học sinh thuộc câu lạc bộ thể thao là $P(A) = %s$' % str_pA
            nb_da_1_s = 'Xác suất chọn được học sinh thuộc câu lạc bộ thể thao là $P(A) = %s$' % format_decimal(1 - prob_A)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Do trường THPT có %s\\%% học sinh tham gia câu lạc bộ thể thao nên $P(A) = %s$.''' % (pA_val, str_pA))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Xác suất chọn được học sinh biết bơi, biết học sinh đó không thuộc câu lạc bộ thể thao là $P(B|\\bar{A}) = %s$' % str_pBgnA
            th_da_1_s = 'Xác suất chọn được học sinh biết bơi, biết học sinh đó không thuộc câu lạc bộ thể thao là $P(B|\\bar{A}) = %s$' % str_pBgA
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Do %s\\%% số học sinh không tham gia câu lạc bộ thể thao cũng biết bơi nên $P(B|\\bar{A}) = %s$.''' % (pBgnA_val, str_pBgnA))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Xác suất chọn được học sinh biết bơi là $P(B) = %s$' % str_pB
            vd_da_1_s = 'Xác suất chọn được học sinh biết bơi là $P(B) = %s$' % format_decimal(prob_A * prob_BgA)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Vì trong số học sinh tham gia câu lạc bộ thể thao, có %s\\%% học sinh biết bơi nên $P(B|A) = %s$. \\\\
            Xác suất học sinh không tham gia câu lạc bộ thể thao là $P(\\bar{A}) = 1 - P(A) = %s$. \\\\
            Xác suất chọn được học sinh biết bơi là: \\\\
            $P(B) = P(A) \\cdot P(B|A) + P(\\bar{A}) \\cdot P(B|\\bar{A})$ \\\\
            $= %s \\cdot %s + %s \\cdot %s = %s$.''' 
                            % (pBgA_val, str_pBgA, str_pnotA, str_pA, str_pBgA, str_pnotA, str_pBgnA, str_pB))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Giả sử chọn được học sinh biết bơi. Xác suất chọn được học sinh thuộc câu lạc bộ thể thao là $P(A|B) = %s$' % str_pAgB
            vdc_da_1_s = 'Giả sử chọn được học sinh biết bơi. Xác suất chọn được học sinh thuộc câu lạc bộ thể thao là $P(A|B) = %s$' % str_pBgA
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Xác suất chọn được học sinh thuộc câu lạc bộ thể thao khi biết học sinh đó biết bơi là: \\\\
            $P(A|B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{P(A) \\cdot P(B|A)}{P(B)} = \\frac{%s \\cdot %s}{%s} = %s$.''' 
                             % (str_pA, str_pBgA, str_pB, str_pAgB))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào danh sách để xuất
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi
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

