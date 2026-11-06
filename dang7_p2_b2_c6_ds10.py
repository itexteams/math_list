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


def bt_dang7_p2_b2_c6_ds10(self):
            # Khai báo biến
            # k là số chấm được chọn (trong hình là 6)
            k = 6 
            # S là mốc tổng số chấm (trong hình là 9)
            S = 9

            # Tính toán không gian mẫu
            n_omega = 36

            # --- Câu a: Số chấm bằng nhau ---
            # Các cặp: (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) -> 6 kết quả
            n_a = 6
            p_a_dung = Rational(n_a, n_omega) # 1/6

            # --- Câu b: Có đúng một mặt k chấm ---
            # Các cặp: (k, 1..5) và (1..5, k) -> 5 + 5 = 10 kết quả
            n_b = 10
            p_b_dung = Rational(n_b, n_omega) # 5/18

            # --- Câu c: Có ít nhất một mặt k chấm ---
            # Các cặp: (k, 1..6) và (1..5, k) -> 6 + 5 = 11 kết quả
            n_c = 11
            p_c_dung = Rational(n_c, n_omega) # 11/36

            # --- Câu d: Tổng số chấm nhỏ hơn S ---
            count_d = 0
            list_d = []
            for i in range(1, 7):
                for j in range(1, 7):
                    if i + j < S:
                        count_d += 1
                        list_d.append((i, j))
            p_d_dung = Rational(count_d, n_omega) # Với S=9 là 26/36 = 13/18

            # ------------------------------------------------------------------------
            # Nhận biết: Xác suất 2 mặt bằng nhau
            # ------------------------------------------------------------------------
            nb_da_1_d = '\\True Xác suất để "Số chấm xuất hiện trên hai mặt bằng nhau" bằng $%s$' % (latex(p_a_dung))
            nb_da_1_s = 'Xác suất để "Số chấm xuất hiện trên hai mặt bằng nhau" bằng $%s$' % (latex(Rational(1, 12)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Không gian mẫu khi gieo hai con xúc xắc là $n(\\Omega) = 6 \\cdot 6 = 36$. \\\\
            Gọi $A$ là biến cố "Số chấm xuất hiện trên hai mặt bằng nhau". \\\\
            Các kết quả thuận lợi cho $A$ là: $\\left\\{ (1;1), (2;2), (3;3), (4;4), (5;5), (6;6) \\right\\} \\Rightarrow n(A) = 6$. \\\\
            Xác suất $P(A) = \\frac{6}{36} = %s$.''' % (latex(p_a_dung)))

            # ------------------------------------------------------------------------
            # Thông hiểu: Có đúng một mặt k chấm
            # ------------------------------------------------------------------------
            th_da_1_d = '\\True Xác suất để "Có đúng một mặt %s chấm xuất hiện" bằng $%s$' % (k, latex(p_b_dung))
            th_da_1_s = 'Xác suất để "Có đúng một mặt %s chấm xuất hiện" bằng $\\frac{5}{8}$' % (k)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Gọi $B$ là biến cố "Có đúng một mặt %s chấm xuất hiện". \\\\
            Các kết quả thuận lợi cho $B$ bao gồm: \\\\
            - Mặt thứ nhất là %s chấm, mặt thứ hai khác %s chấm: có $1 \\cdot 5 = 5$ kết quả. \\\\
            - Mặt thứ nhất khác %s chấm, mặt thứ hai là %s chấm: có $5 \\cdot 1 = 5$ kết quả. \\\\
            $\\Rightarrow n(B) = 5 + 5 = 10$. \\\\
            Xác suất $P(B) = \\frac{10}{36} = %s$.''' % (k, k, k, k, k, latex(p_b_dung)))

            # ------------------------------------------------------------------------
            # Vận dụng: Có ít nhất một mặt k chấm
            # ------------------------------------------------------------------------
            vd_da_1_d = '\\True Xác suất để "Có ít nhất một mặt %s chấm xuất hiện" bằng $%s$' % (k, latex(p_c_dung))
            vd_da_1_s = 'Xác suất để "Có ít nhất một mặt %s chấm xuất hiện" bằng $%s$' % (k, latex(Rational(5, 36)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Gọi $C$ là biến cố "Có ít nhất một mặt %s chấm xuất hiện". \\\\
            Biến cố đối $\\overline{C}$ là "Không có mặt %s chấm nào xuất hiện". \\\\
            Số kết quả thuận lợi cho $\\overline{C}$ là $5 \\cdot 5 = 25$ kết quả. \\\\
            Xác suất $P(\\overline{C}) = \\frac{25}{36}$. \\\\
            Xác suất $P(C) = 1 - P(\\overline{C}) = 1 - \\frac{25}{36} = %s$.''' % (k, k, latex(p_c_dung)))

            # ------------------------------------------------------------------------
            # Vận dụng cao: Tổng số chấm nhỏ hơn S
            # ------------------------------------------------------------------------
            vdc_da_1_d = '\\True Xác suất để "Tổng số chấm xuất hiện nhỏ hơn %s" bằng $%s$' % (S, latex(p_d_dung))
            vdc_da_1_s = 'Xác suất để "Tổng số chấm xuất hiện nhỏ hơn %s" bằng $\\frac{3}{14}$' % (S)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Gọi $D$ là biến cố "Tổng số chấm xuất hiện nhỏ hơn %s". \\\\
            Các trường hợp có thể xảy ra: \\\\
            - Tổng bằng 2: (1,1) (1 cặp) \\\\
            - Tổng bằng 3: (1,2), (2,1) (2 cặp) \\\\
            - Tổng bằng 4: (1,3), (2,2), (3,1) (3 cặp) \\\\
            - Tổng bằng 5: (1,4), (2,3), (3,2), (4,1) (4 cặp) \\\\
            - Tổng bằng 6: (1,5), (2,4), (3,3), (4,2), (5,1) (5 cặp) \\\\
            - Tổng bằng 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) (6 cặp) \\\\
            - Tổng bằng 8: (2,6), (3,5), (4,4), (5,3), (6,2) (5 cặp) \\\\
            Số kết quả thuận lợi là $n(D) = 1+2+3+4+5+6+5 = %s$. \\\\
            Xác suất $P(D) = \\frac{%s}{36} = %s$.''' % (S, count_d, count_d, latex(p_d_dung)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Gán lời giải tương ứng (trong bài này lời giải là cố định cho nội dung câu hỏi)
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Xuất nội dung
            noidungcauhoi = '''Gieo hai con xúc xắc cân đối và đồng nhất.'''

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

