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


def bt_dang21_p2_b2_c4_ds12(self):
            # Khai báo biến
            # b: Xác suất chặn nhầm (ví dụ 2% - 5%)

            p_val = random.choice([4, 5, 6, 8]) # %
            a_val = random.choice([90, 92, 94, 95]) # %
            b_val = random.choice([2, 3, 4]) # %

            # Chuyển sang số thập phân và phân số để tính toán chính xác
            p = Rational(p_val, 100)
            a = Rational(a_val, 100)
            b = Rational(b_val, 100)

            # Các xác suất thành phần phục vụ lời giải
            # P(A) = p, P(not A) = 1-p
            # P(B|A) = a, P(B|not A) = b
            p_not_a = 1 - p
            p_b = p * a + p_not_a * b
            p_a_b = (p * a) / p_b
            p_not_a_not_b = (p_not_a * (1 - b)) / (1 - p_b)

            # Nội dung câu hỏi gốc
            noidungcauhoi = (r'''Một nhà mạng viễn thông đang triển khai hệ thống phát hiện và chặn các số điện thoại thực hiện cuộc gọi lừa đảo. Tuy nhiên, do hệ thống chưa hoàn hảo, nó có thể chặn nhầm một số điện thoại hợp lệ hoặc bỏ sót một số điện thoại lừa đảo. Hệ thống hoạt động với các thông số sau:
            +Tỷ lệ số điện thoại lừa đảo trong hệ thống: %s\%%.
            +Xác suất hệ thống phát hiện đúng và chặn một số điện thoại lừa đảo: %s\%%.
            +Xác suất hệ thống chặn nhầm một số điện thoại hợp lệ: %s\%%.
            Chọn ngẫu nhiên một số điện thoại đã được thử nghiệm hệ thống.''' 
                             %(p_val, a_val, b_val))

            # Định nghĩa các biến biến cố cho lời giải
            bien_co = r'''Gọi $A$ là biến cố "Số điện thoại được chọn là số lừa đảo", $B$ là biến cố "Số điện thoại bị chặn". 
            Ta có $P(A)=%s$, $P(\overline{A})=%s$, $P(B|A)=%s$, $P(B|\overline{A})=%s$.''' % (latex(p), latex(p_not_a), latex(a), latex(b))

            ########################################################################
            # NHẬN BIẾT
            nb_da_1_d = r'\True Biết rằng số điện thoại đó là số lừa đảo, xác suất để số điện thoại đó bị chặn là $%s$' % (latex(a))
            nb_da_1_s = r'Biết rằng số điện thoại đó là số lừa đảo, xác suất để số điện thoại đó bị chặn là $%s$' % (latex(b))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''Xác suất số điện thoại bị chặn khi biết nó là số lừa đảo chính là $P(B|A) = %s$.''' % (latex(a))

            ########################################################################
            # THÔNG HIỂU
            th_da_1_d = r'\True Xác suất để một số điện thoại bất kỳ bị chặn là $%s$' % (latex(p_b))
            th_da_1_s = r'Xác suất để một số điện thoại bất kỳ bị chặn là $%s$' % (latex(p * a))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''Áp dụng công thức xác suất đầy đủ: $P(B) = P(A) \cdot P(B|A) + P(\overline{A}) \cdot P(B|\overline{A}) = %s \cdot %s + %s \cdot %s = %s$.''' % (latex(p), latex(a), latex(p_not_a), latex(b), latex(p_b))

            ########################################################################
            # VẬN DỤNG
            vd_da_1_d = r'\True Biết rằng một số điện thoại bị chặn, xác suất để số điện thoại đó là số lừa đảo bằng $%s$' % (latex(p_a_b))
            vd_da_1_s = r'Biết rằng một số điện thoại bị chặn, xác suất để số điện thoại đó là số lừa đảo bằng $%s$' % (latex(p_b))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'''Áp dụng công thức Bayes: $P(A|B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{P(A) \cdot P(B|A)}{P(B)} = \dfrac{%s \cdot %s}{%s} = %s$.''' % (latex(p), latex(a), latex(p_b), latex(p_a_b))

            ########################################################################
            # VẬN DỤNG CAO
            vdc_da_1_d = r'\True Biết rằng một số điện thoại không bị chặn, xác suất để số điện thoại đó là số hợp lệ bằng $%s$' % (latex(p_not_a_not_b))
            vdc_da_1_s = r'Biết rằng một số điện thoại không bị chặn, xác suất để số điện thoại đó là số hợp lệ bằng $%s$' % (latex(Rational(1,2)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''Ta cần tính $P(\overline{A}|\overline{B})$. Ta có $P(\overline{B}) = 1 - P(B) = 1 - %s = %s$. 
            \\ $P(\overline{A} \cap \overline{B}) = P(\overline{A}) \cdot P(\overline{B}|\overline{A}) = %s \cdot (1 - %s) = %s$.
            \\ Suy ra $P(\overline{A}|\overline{B}) = \dfrac{P(\overline{A} \cap \overline{B})}{P(\overline{B})} = \dfrac{%s}{%s} = %s$.''' % (latex(p_b), latex(1-p_b), latex(p_not_a), latex(b), latex(p_not_a*(1-b)), latex(p_not_a*(1-b)), latex(1-p_b), latex(p_not_a_not_b))

            # --- Xử lý Logic Chọn đáp án ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # --- XUẤT NỘI DUNG ---
            # Vẽ biểu đồ Ven bằng TikZ
            tikz_venn = r'''\begin{tikzpicture}[scale=0.8]
              \draw (0,0) circle (1.5) node[left=1cm] {Lừa đảo};
              \draw (1.5,0) circle (1.5) node[right=1cm] {Bị chặn};
              \node at (0,0) {$%s\%%$};
              \node at (0.75,0) {$A \cap B$};
            \end{tikzpicture}''' % (p_val)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n' +
                str(bien_co) + '\n' +
                '\\begin{center}\n' + tikz_venn + '\n\\end{center}\n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

