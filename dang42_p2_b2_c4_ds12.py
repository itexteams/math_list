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


def bt_dang42_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Tổng số người khảo sát
            N = 200
            # Số trẻ em (A) và người lớn (not A)
            n_A = random.choice([140, 150, 120, 160])
            n_notA = N - n_A

            p_A = Rational(n_A, N)
            p_notA = Rational(n_notA, N)

            # Phân phối xác suất (Sử dụng Rational cho chính xác)
            # c1: Thích & Xem tiếp; c2: Thích & Không xem tiếp; c3: Không thích & Không xem tiếp
            dist_child = random.choice([(50, 30, 20), (60, 20, 20), (40, 40, 20)])
            c1, c2, c3 = [Rational(v, 100) for v in dist_child]

            dist_adult = random.choice([(20, 10, 70), (10, 20, 70), (30, 10, 60)])
            a1, a2, a3 = [Rational(v, 100) for v in dist_adult]

            # Các xác suất điều kiện
            p_B_given_A = c1 + c2
            p_C_given_A = c1
            p_B_given_notA = a1 + a2
            p_C_given_notA = a1

            # Câu c: P(C) và P(A|C)
            p_C = p_A * p_C_given_A + p_notA * p_C_given_notA
            p_A_given_C = (p_A * p_C_given_A) / p_C

            # Câu d: P(B) và P(notC | B)
            p_B = p_A * p_B_given_A + p_notA * p_B_given_notA
            p_notC_and_B = p_A * c2 + p_notA * a2
            p_notC_given_B = p_notC_and_B / p_B

            # ------------------------------------------------------------------------
            # NỘI DUNG CÂU HỎI
            # ------------------------------------------------------------------------

            noidungcauhoi = ('''Khảo sát %s người xem bộ phim hoạt hình về thể loại trinh thám vừa được phát hành cho thấy %s người xem là trẻ em và %s người xem là người lớn. Trong số các trẻ em đến xem phim có %s\\%% yêu thích bộ phim và khẳng định sẽ đi xem tiếp phần 2; %s\\%% yêu thích bộ phim nhưng sẽ không xem tiếp phần 2; %s\\%% còn lại không thích bộ phim và không xem tiếp phần 2. Trong số những người lớn đi xem phim có %s\\%% yêu thích bộ phim và khẳng định sẽ đi xem tiếp phần 2; %s\\%% yêu thích bộ phim nhưng sẽ không xem tiếp phần 2; %s\\%% còn lại không thích bộ phim và không xem tiếp phần 2.\\\\
            Gọi $A$ là biến cố: "Người được chọn là trẻ em".\\\\
            $B$ là biến cố: "Người được chọn yêu thích bộ phim".\\\\
            $C$ là biến cố: "Người được chọn sẽ đi xem tiếp phần 2".\\\\
            Chọn ngẫu nhiên 1 người đã xem phim.''' 
            % (N, n_A, n_notA, dist_child[0], dist_child[1], dist_child[2], dist_adult[0], dist_adult[1], dist_adult[2]))

            # ------------------------------------------------------------------------
            # ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT (DẠNG PHÂN SỐ)
            # ------------------------------------------------------------------------

            # --- a) Nhận biết ---
            nb_da_d = '\\True $P(A) = %s; P(\\bar{A}) = %s$' % (latex(p_A), latex(p_notA))
            nb_da_s = '$P(A) = %s; P(\\bar{A}) = %s$' % (latex(p_notA), latex(p_A))
            loigiai_nb = 'Ta có $P(A) = \\frac{%s}{%s} = %s; P(\\bar{A}) = \\frac{%s}{%s} = %s$.' % (n_A, N, latex(p_A), n_notA, N, latex(p_notA))

            # --- b) Thông hiểu ---
            th_da_d = '\\True $P(B|A) = %s$' % latex(p_B_given_A)
            th_da_s = '$P(B|A) = %s$' % latex(p_B_given_notA)
            loigiai_th = 'Ta có $P(B|A) = P((B \\cap C)|A) + P((B \\cap \\bar{C})|A) = %s + %s = %s$.' % (latex(c1), latex(c2), latex(p_B_given_A))

            # --- c) Vận dụng ---
            # So sánh với 35/41 (~0.85) như đề gốc
            threshold = Rational(35, 41)
            is_greater = p_A_given_C > threshold
            text_cmp = 'lớn hơn' if is_greater else 'nhỏ hơn hoặc bằng'
            vd_da_d = '\\True Biết người đó sẽ xem tiếp phần 2 của bộ phim, xác suất để người đó là trẻ em %s $%s$' % (text_cmp, latex(threshold))
            vd_da_s = 'Biết người đó sẽ xem tiếp phần 2 của bộ phim, xác suất để người đó là trẻ em %s $%s$' % ('nhỏ hơn' if is_greater else 'lớn hơn', latex(threshold))

            loigiai_vd = ('''Biết người đó sẽ xem tiếp phần 2 của bộ phim, xác suất để người đó là trẻ em là $P(A|C)$.\\\\
            Áp dụng công thức Bayes ta có: $P(A|C) = \\frac{P(A).P(C|A)}{P(C)}$.\\\\
            Mà $P(C|A) = %s$ và $P(C) = P(A)P(C|A) + P(\\bar{A})P(C|\\bar{A}) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\
            Vậy $P(A|C) = \\frac{%s \\cdot %s}{%s} = %s$.''' 
            % (latex(c1), latex(p_A), latex(c1), latex(p_notA), latex(a1), latex(p_C), 
               latex(p_A), latex(c1), latex(p_C), latex(p_A_given_C)))

            # --- d) Vận dụng cao ---
            vdc_da_d = '\\True Biết người đó yêu thích bộ phim, xác suất để người đó không xem tiếp phần 2 là $%s$' % latex(p_notC_given_B)
            vdc_da_s = 'Biết người đó yêu thích bộ phim, xác suất để người đó không xem tiếp phần 2 là $%s$' % latex(p_notC_given_B + Rational(1, 10))

            loigiai_vdc = ('''Biết người đó yêu thích bộ phim, xác suất để người đó không xem tiếp phần 2 là $P(\\bar{C}|B)$.\\\\
            Ta có $P(\\bar{C}|B) = \\frac{P(\\bar{C} \\cap B)}{P(B)}$.\\\\
            Áp dụng công thức xác suất toàn phần ta có:\\\\
            $P(\\bar{C} \\cap B) = P(A)P((\\bar{C} \\cap B)|A) + P(\\bar{A})P((\\bar{C} \\cap B)|\\bar{A}) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\
            Ta có $P(B|A) = %s$ và $P(B|\\bar{A}) = %s$.\\\\
            Áp dụng công thức xác suất toàn phần: \\\\ $P(B) = P(A).P(B|A) + P(\\bar{A}).P(B|\\bar{A}) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\
            Vậy $P(\\bar{C}|B) = \\frac{%s}{%s} = %s$.''' 
            % (latex(p_A), latex(c2), latex(p_notA), latex(a2), latex(p_notC_and_B),
               latex(p_B_given_A), latex(p_B_given_notA),
               latex(p_A), latex(p_B_given_A), latex(p_notA), latex(p_B_given_notA), latex(p_B),
               latex(p_notC_and_B), latex(p_B), latex(p_notC_given_B)))

            # ------------------------------------------------------------------------
            # XỬ LÝ NGẪU NHIÊN ĐÁP ÁN (ĐÚNG/SAI)
            # ------------------------------------------------------------------------

            def get_shuffled_pair(da_d, da_s, lg):
                lst = [da_d, da_s]
                chosen = random.choice(lst)
                return chosen, lg

            while True:
                ans_a, sol_a = get_shuffled_pair(nb_da_d, nb_da_s, loigiai_nb)
                ans_b, sol_b = get_shuffled_pair(th_da_d, th_da_s, loigiai_th)
                ans_c, sol_c = get_shuffled_pair(vd_da_d, vd_da_s, loigiai_vd)
                ans_d, sol_d = get_shuffled_pair(vdc_da_d, vdc_da_s, loigiai_vdc)

                true_count = sum('\\True' in ans for ans in [ans_a, ans_b, ans_c, ans_d])
                if 1 <= true_count <= 3:
                    break

            # ------------------------------------------------------------------------
            # XUẤT NỘI DUNG
            # ------------------------------------------------------------------------

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sol_a) + '\n'
                '\\item ' + str(sol_b) + '\n'
                '\\item ' + str(sol_c) + '\n'
                '\\item ' + str(sol_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

