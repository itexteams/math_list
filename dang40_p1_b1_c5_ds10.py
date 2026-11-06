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


def bt_dang40_p1_b1_c5_ds10(self):
            # Khai báo biến
            # Tổng cộng 6 chữ số, trong đó có 0, hai số chẵn khác 0 và ba số lẻ.

            list_odds = [1, 3, 5, 7, 9]
            list_evens = [2, 4, 6, 8]

            # Chọn ngẫu nhiên bộ số
            selected_odds = random.sample(list_odds, 3) # Ví dụ: [1, 3, 5]
            selected_evens = random.sample(list_evens, 2) # Ví dụ: [2, 8]
            digits = [0] + selected_odds + selected_evens
            digits.sort()

            # Chọn chữ số lẻ bắt buộc phải có mặt (target_digit)
            target_digit = random.choice(selected_odds)

            # Chuỗi hiển thị tập hợp số
            digits_str = ", ".join(map(str, digits))

            # Tính toán số lượng trường hợp (logic tổ hợp)
            # Gọi số cần tìm là abcd. Điều kiện: d lẻ, a != 0, các chữ số đôi một khác nhau, có mặt target_digit.

            # Trường hợp 1: a = target_digit
            # d có (số lượng số lẻ - 1) cách chọn (vì d lẻ và d != a)
            # b có (tổng số - 2) cách chọn
            # c có (tổng số - 3) cách chọn
            c1_a = 1
            c1_d = len(selected_odds) - 1
            c1_b = len(digits) - 2
            c1_c = len(digits) - 3
            case1 = c1_a * c1_d * c1_b * c1_c

            # Trường hợp 2: b = target_digit
            # d có (số lượng số lẻ - 1) cách chọn (vì d lẻ và d != target_digit)
            # a có (tổng số - 3) cách chọn (vì a != 0, a != target_digit, a != d)
            # c có (tổng số - 3) cách chọn
            c2_b = 1
            c2_d = len(selected_odds) - 1
            c2_a = len(digits) - 3
            c2_c = len(digits) - 3
            case2 = c2_a * c2_b * c2_c * c2_d

            # Trường hợp 3: c = target_digit
            # Tương tự TH2
            c3_c = 1
            c3_d = len(selected_odds) - 1
            c3_a = len(digits) - 3
            c3_b = len(digits) - 3
            case3 = c3_a * c3_b * c3_c * c3_d

            # Trường hợp 4: d = target_digit
            # a có (tổng số - 2) cách chọn (vì a != 0, a != target_digit)
            # b có (tổng số - 2) cách chọn
            # c có (tổng số - 3) cách chọn
            c4_d = 1
            c4_a = len(digits) - 2
            c4_b = len(digits) - 2
            c4_c = len(digits) - 3
            case4 = c4_a * c4_b * c4_c * c4_d

            # Tổng kết quả
            total_kq = case1 + case2 + case3 + case4

            # B4: Điều chỉnh phương án sai
            da_dung = "$%s$ số." % (total_kq)
            list_wrong = []
            while len(list_wrong) < 3:
                offset = random.choice([-12, 12, 24, -24, 36, -36, 48, 60])
                wrong_val = total_kq + offset
                if wrong_val > 0 and wrong_val != total_kq:
                    option = "$%s$ số." % (wrong_val)
                    if option not in list_wrong:
                        list_wrong.append(option)

            list_options = ["\\True " + da_dung] + list_wrong
            random.shuffle(list_options)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Từ các chữ số $%s$ có thể lập được bao nhiêu số tự nhiên lẻ có bốn chữ số đôi một khác nhau và phải có mặt chữ số $%s$?'''
                             % (latex(digits_str), latex(target_digit)))

            # Nội dung lời giải (Viết chi tiết, không viết tắt)
            loigiai = ('''Gọi số tự nhiên có bốn chữ số khác nhau là $\\overline{abcd}$. \\\\
            Do số cần lập là số lẻ và phải có mặt chữ số $%s$ nên ta có các trường hợp sau: \\\\
            \\textbf{Trường hợp 1:} $a = %s$, khi đó số có dạng $\\overline{%s bcd}$. \\\\
            Có $%s$ cách chọn $d$ (chọn từ các số lẻ còn lại). \\\\
            Có $%s$ cách chọn $b$. \\\\
            Có $%s$ cách chọn $c$. \\\\
            Theo quy tắc nhân có: $1 \\cdot %s \\cdot %s \\cdot %s = %s$. \\\\
            \\textbf{Trường hợp 2:} $b = %s$, khi đó số có dạng $\\overline{a %s cd}$. \\\\
            Có $%s$ cách chọn $d$. \\\\
            Có $%s$ cách chọn $a$ ($a \\neq 0, a \\neq %s, a \\neq d$). \\\\
            Có $%s$ cách chọn $c$. \\\\
            Theo quy tắc nhân có: $%s \\cdot 1 \\cdot %s \\cdot %s = %s$. \\\\
            \\textbf{Trường hợp 3:} $c = %s$, khi đó số có dạng $\\overline{ab %s d}$. \\\\
            Có $%s$ cách chọn $d$. \\\\
            Có $%s$ cách chọn $a$. \\\\
            Có $%s$ cách chọn $b$. \\\\
            Theo quy tắc nhân có: $%s \\cdot %s \\cdot 1 \\cdot %s = %s$. \\\\
            \\textbf{Trường hợp 4:} $d = %s$, khi đó số có dạng $\\overline{abc %s}$. \\\\
            Có $%s$ cách chọn $a$ ($a \\neq 0, a \\neq %s$). \\\\
            Có $%s$ cách chọn $b$. \\\\
            Có $%s$ cách chọn $c$. \\\\
            Theo quy tắc nhân có: $%s \\cdot %s \\cdot %s \\cdot 1 = %s$. \\\\
            Theo quy tắc cộng, ta có: $%s + %s + %s + %s = %s$ số.'''
                       % (latex(target_digit), latex(target_digit), latex(target_digit),
                          latex(c1_d), latex(c1_b), latex(c1_c), latex(c1_b), latex(c1_c), latex(c1_d), latex(case1),
                          latex(target_digit), latex(target_digit),
                          latex(c2_d), latex(c2_a), latex(target_digit), latex(c2_c), 
                          latex(c2_a), latex(c2_c), latex(c2_d), latex(case2),
                          latex(target_digit), latex(target_digit),
                          latex(c3_d), latex(c3_a), latex(c3_b),
                          latex(c3_a), latex(c3_b), latex(c3_d), latex(case3),
                          latex(target_digit), latex(target_digit),
                          latex(c4_a), latex(target_digit), latex(c4_b), latex(c4_c),
                          latex(c4_a), latex(c4_b), latex(c4_c), latex(case4),
                          latex(case1), latex(case2), latex(case3), latex(case4), latex(total_kq)))

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_options[0]) + '}\n'
                       '{' + str(list_options[1]) + '}\n'
                       '{' + str(list_options[2]) + '}\n'
                       '{' + str(list_options[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

