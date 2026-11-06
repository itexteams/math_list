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


def bt_dang29_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo các thông số cơ bản (có thể random)
            k = 3 # số lần tung
            tu_so = 3
            mau_so = 4
            p_biased = Rational(tu_so, mau_so)
            p_fair = Rational(1, 2)

            # Tính toán các giá trị xác suất để dùng trong lời giải
            prob_B_A = p_fair**k
            prob_B_notA = p_biased**k
            prob_B = Rational(1, 2) * prob_B_A + Rational(1, 2) * prob_B_notA
            prob_A_B = (Rational(1, 2) * prob_B_A) / prob_B
            prob_notA_B = 1 - prob_A_B

            # Tính xác suất câu d (lần thứ 4 ngửa)
            prob_C = p_fair * prob_A_B + p_biased * prob_notA_B

            # Định dạng số thập phân dùng dấu phẩy
            def format_decimal(value, precision=2):
                res = round(float(value), precision)
                return str(res).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Giả sử có một đồng xu cân bằng (fair coin) và một đồng xu thiên lệch (biased coin) mà mặt ngửa (heads) xuất hiện với xác suất $%s$. Một người chơi ngẫu nhiên chọn một trong hai đồng xu và tung nó %s lần. Gọi $A$ là biến cố: "Người chơi chọn đồng xu cân bằng", $B$ là biến cố: "Ba lần tung đồng xu đều xuất hiện mặt ngửa".''' 
                             %(latex(p_biased), k))

            ########################################################################
            # Nhận biết (Câu a)
            ########################################################################
            nb_da_1_d = '\\True $P(A) = \\frac{1}{2}$'
            nb_da_1_s = '$P(A) = \\frac{1}{4}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Vì người chơi chọn ngẫu nhiên một trong hai đồng xu (một cân bằng và một thiên lệch), nên xác suất chọn được đồng xu cân bằng là $P(A) = \\frac{1}{2}$.''')

            ########################################################################
            # Thông hiểu (Câu b)
            ########################################################################
            val_b = latex(prob_B_A)
            th_da_1_d = '\\True $P(B|A) = %s$' % val_b
            th_da_1_s = '$P(B|A) = \\frac{3}{8}$' # Sai vì 3/8 là của đồng xu kia nếu tung 1 lần...
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Vì biến cố $A$ đã xảy ra, tức là chọn được đồng xu cân bằng nên xác suất để mỗi lần xuất hiện mặt ngửa là $\\frac{1}{2}$, do đó xác suất biến cố $B$ với điều kiện biến cố $A$ đã xảy ra là $P(B|A) = \\left( \\frac{1}{2} \\right)^%s = %s$.''' % (k, val_b))

            ########################################################################
            # Vận dụng (Câu c)
            ########################################################################
            val_c_float = format_decimal(prob_A_B, 2)
            vd_da_1_d = '\\True Xác suất để người đó chọn được đồng xu cân bằng biết rằng kết quả ba lần tung đều xuất hiện mặt ngửa là %s (kết quả làm tròn đến hàng phần trăm)' % val_c_float
            vd_da_1_s = 'Xác suất để người đó chọn được đồng xu cân bằng biết rằng kết quả ba lần tung đều xuất hiện mặt ngửa là 0,50'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có: $P(B) = P(A).P(B|A) + P(\\overline{A}).P(B|\\overline{A}) = \\frac{1}{2}.\\frac{1}{8} + \\frac{1}{2}.\\left(\\frac{3}{4}\\right)^3 = \\frac{35}{128}$. \\\\
            Xác suất cần tìm là: $P(A|B) = \\frac{P(A).P(B|A)}{P(B)} = \\frac{\\frac{1}{2}.\\frac{1}{8}}{\\frac{35}{128}} = \\frac{8}{35} \\approx %s$.''' % val_c_float)

            ########################################################################
            # Vận dụng cao (Câu d)
            ########################################################################
            val_d_float = format_decimal(prob_C, 2)
            vdc_da_1_d = '\\True Biết rằng đồng xu được chọn tung ba lần đều xuất hiện mặt ngửa, xác suất người chơi đó tung lần thứ tư tiếp tục xuất hiện mặt ngửa là %s (kết quả làm tròn đến hàng phần trăm)' % val_d_float
            vdc_da_1_s = 'Biết rằng đồng xu được chọn tung ba lần đều xuất hiện mặt ngửa, xác suất người chơi đó tung lần thứ tư tiếp tục xuất hiện mặt ngửa là 0,50'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Vì $P(A|B) = \\frac{8}{35}$ nên $P(\\overline{A}|B) = 1 - \\frac{8}{35} = \\frac{27}{35}$. \\\\
            Gọi $C$ là biến cố "tung lần thứ tư tiếp tục xuất hiện mặt ngửa". \\\\
            $P(C) = P(C|A).P(A|B) + P(C|\\overline{A}).P(\\overline{A}|B) = \\frac{1}{2}.\\frac{8}{35} + \\frac{3}{4}.\\frac{27}{35} = \\frac{97}{140} \\approx %s$.''' % val_d_float)

            # --- PHẦN LOGIC CHỌN ĐÁP ÁN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # --- XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

