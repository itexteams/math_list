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


def bt_dang5_p2_b1_c6_ds11(self):
            # Khai báo biến
            def is_prime(n):
                if n < 2: return False
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0: return False
                return True

            # --- BƯỚC 1: RANDOM CÁC THÔNG SỐ ĐẦU VÀO ---
            n_total = random.randint(12, 20)  # Tổng số thẻ từ 12 đến 20
            k_a = random.randint(7, 11)       # Ngưỡng của biến cố A
            k_b = random.randint(8, 12)       # Ngưỡng của biến cố B

            # --- BƯỚC 2: TÍNH TOÁN CÁC TẬP HỢP ---
            S = list(range(1, n_total + 1))
            A = [x for x in S if x < k_a]
            B = [x for x in S if is_prime(x) and x < k_b]
            C = [x for x in S if x % 2 == 0]

            AB = sorted(list(set(A) & set(B)))
            BC = sorted(list(set(B) & set(C)))

            # Chuyển danh sách sang chuỗi LaTeX: {2; 3; 5}
            def to_latex_set(lst):
                return "{" + "; ".join(map(str, lst)) + "}"

            # Nội dung câu hỏi
            noidungcauhoi = r'''Một hộp đựng %s tấm thẻ cùng loại được đánh số từ $1$ đến $%s$. Rút ngẫu nhiên một tấm thẻ, quan sát số ghi trên thẻ.\\
            Gọi $A$ là biến cố "Số ghi trên tấm thẻ nhỏ hơn $%s$".\\
            $B$ là biến cố "Số ghi trên tấm thẻ là số nguyên tố nhỏ hơn $%s$".\\
            $C$ là biến cố "Số ghi trên tấm thẻ là số chẵn".''' % (n_total, n_total, k_a, k_b)

            ########################################################################
            # Mệnh đề (a) - Nhận biết: Về biến cố giao AB
            ########################################################################
            min_k = min(k_a, k_b)
            nb_da_1_d = r'\True $AB$ là biến cố "Số ghi trên tấm thẻ là số nguyên tố nhỏ hơn $%s$" ' % min_k
            nb_da_1_s = r'$AB$ là biến cố "Số ghi trên tấm thẻ là số chẵn nhỏ hơn $%s$" ' % k_a
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'''Ta có $A = \{%s\}$ và $B = \{%s\}$. \\
            Biến cố $AB = A \cap B = \{%s\}$. \\
            Vậy $AB$ là biến cố "Số ghi trên tấm thẻ là số nguyên tố nhỏ hơn $%s$".''' % (to_latex_set(A), to_latex_set(B), to_latex_set(AB), min_k)

            ########################################################################
            # Mệnh đề (b) - Thông hiểu: Về biến cố giao BC
            ########################################################################
            th_da_1_d = r'\True $BC$ là biến cố "Số ghi trên tấm thẻ là số nguyên tố chẵn nhỏ hơn $%s$" ' % k_b
            th_da_1_s = r'$BC$ là biến cố "Số ghi trên tấm thẻ là số lẻ nhỏ hơn $%s$" ' % k_b
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r'''Ta có $B = \{%s\}$ và $C = \{%s\}$. \\
            Biến cố $BC = B \cap C = \{%s\}$. \\
            Vậy $BC$ là biến cố "Số ghi trên tấm thẻ là số nguyên tố chẵn nhỏ hơn $%s$".''' % (to_latex_set(B), to_latex_set(C), to_latex_set(BC), k_b)

            ########################################################################
            # Mệnh đề (c) - Vận dụng: Số kết quả thuận lợi AB
            ########################################################################
            n_AB = len(AB)
            vd_da_1_d = r'\True Số kết quả thuận lợi cho biến cố $AB$ là $%s$' % n_AB
            vd_da_1_s = r'Số kết quả thuận lợi cho biến cố $AB$ là $%s$' % (n_AB + 1)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'''Vì $AB = %s$ nên số kết quả thuận lợi cho biến cố $AB$ là $n(AB) = %s$.''' % (to_latex_set(AB), n_AB)

            ########################################################################
            # Mệnh đề (d) - Vận dụng cao: Số kết quả thuận lợi BC
            ########################################################################
            n_BC = len(BC)
            vdc_da_1_d = r'\True Số kết quả thuận lợi cho biến cố $BC$ là $%s$' % n_BC
            vdc_da_1_s = r'Biến cố $BC$ là biến cố không thể' # (Vì n_BC luôn >= 1 do có số 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r'''Vì $BC = %s$ nên số kết quả thuận lợi cho biến cố $BC$ là $n(BC) = %s$.''' % (to_latex_set(BC), n_BC)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp để đảm bảo có từ 1 đến 3 câu đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            final_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            final_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # --- XUẤT KẾT QUẢ ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(final_answers[0]) + '}\n'
                '{' + str(final_answers[1]) + '}\n'
                '{' + str(final_answers[2]) + '}\n'
                '{' + str(final_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(final_solutions[0]) + '\n'
                '\\item ' + str(final_solutions[1]) + '\n'
                '\\item ' + str(final_solutions[2]) + '\n'
                '\\item ' + str(final_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

