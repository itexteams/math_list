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


def bt_dang31_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (Dạng 1: Xác suất cổ phiếu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các giá trị xác suất dưới dạng phân số để đảm bảo tính toán chính xác
                # p1: P(X|Y_bar), p2: P(Y|X_bar), p3: P(X \cap Y)

                # Thiết lập bộ số để đảm bảo kết quả x, y nằm trong khoảng (0, 1)
                datasets = [
                    {'p1': Rational(3, 5), 'p2': Rational(2, 3), 'p3': Rational(1, 10)},
                    {'p1': Rational(1, 2), 'p2': Rational(1, 3), 'p3': Rational(1, 10)},
                    {'p1': Rational(2, 5), 'p2': Rational(1, 2), 'p3': Rational(1, 15)},
                    {'p1': Rational(4, 7), 'p2': Rational(3, 5), 'p3': Rational(1, 10)},
                    {'p1': Rational(1, 3), 'p2': Rational(1, 4), 'p3': Rational(1, 20)}
                ]

                data = random.choice(datasets)
                p1 = data['p1']
                p2 = data['p2']
                p3 = data['p3']

                # Giải hệ phương trình:
                # x = p3 + (1-y)*p1
                # y = p3 + (1-x)*p2
                x_sym, y_sym = symbols('x y')
                eq1 = Eq(x_sym, p3 + (1 - y_sym) * p1)
                eq2 = Eq(y_sym, p3 + (1 - x_sym) * p2)

                sol = solve((eq1, eq2), (x_sym, y_sym))
                x_val = sol[x_sym]
                y_val = sol[y_sym]

                # Xác suất cần tìm: P(X \cup Y) = P(X) + P(Y) - P(X \cap Y)
                ketqua_rat = x_val + y_val - p3

                # Chuyển đổi sang số thập phân, làm tròn 1 chữ số và thay dấu . bằng dấu ,
                kq_float = float(ketqua_rat)
                kq_dec = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',')

                # Tạo các phương án nhiễu
                da_dung = '$%s$' % kq_str

                def generate_distractors(correct_val):
                    offsets = [-0.1, 0.1, 0.2, -0.2, 0.3, -0.3]
                    s = []
                    for offset in offsets:
                        val = float(correct_val) + offset
                        if 0 < val < 1:
                            val_dec = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                            s.append('$%s$' % str(val_dec).replace('.', ','))
                    return list(set(s)) # Loại bỏ trùng lặp

                s_list = generate_distractors(kq_float)
                if da_dung in s_list: s_list.remove(da_dung)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = (
                    'Quan sát hai mã cổ phiếu $X$ và $Y$. Người ta nhận thấy trong mỗi phiên giao dịch, nếu cổ phiếu $Y$ không giảm thì cổ phiếu $X$ giảm giá với xác suất $%s$. '
                    'Ngược lại, nếu cổ phiếu $X$ không giảm thì cổ phiếu $Y$ giảm giá với xác suất $%s$. Hơn nữa, xác suất để cả hai cổ phiếu $X$ và $Y$ giảm giá trong cùng một ngày là $%s$. '
                    'Hỏi xác suất để có ít nhất một trong hai cổ phiếu giảm giá trong một phiên giao dịch là bao nhiêu?'
                    % (latex(p1), latex(p2), latex(p3))
                )

                # Hệ phương trình trong lời giải để hiển thị đẹp
                # Eq1: x = p3 + (1-y)p1 => x + p1*y = p3 + p1
                # Eq2: y = p3 + (1-x)p2 => p2*x + y = p3 + p2
                c1 = p3 + p1
                c2 = p3 + p2

                # Lời giải chi tiết
                loigiai = (
                    'Gọi $X$ là biến cố: "Cổ phiếu $X$ giảm giá trong phiên giao dịch".\\\\ '
                    'Gọi $Y$ là biến cố: "Cổ phiếu $Y$ giảm giá trong phiên giao dịch".\\\\ '
                    'Đặt $P(X) = x, P(Y) = y$.\\\\ '
                    'Theo bài ra $P(X|\\bar{Y}) = %s, P(Y|\\bar{X}) = %s, P(X \\cap Y) = %s$.\\\\ '
                    'Ta có $%s = P(X \\cap Y) = P(X) \\cdot P(Y|X) = P(Y) \\cdot P(X|Y)$.\\\\ '
                    'Lại có $P(X) = P(Y) \\cdot P(X|Y) + P(\\bar{Y}) \\cdot P(X|\\bar{Y}) \\Leftrightarrow x = %s + (1-y) \\cdot %s$ (1)\\\\ '
                    'và $P(Y) = P(X) \\cdot P(Y|X) + P(\\bar{X}) \\cdot P(Y|\\bar{X}) \\Leftrightarrow y = %s + (1-x) \\cdot %s$ (2)\\\\ '
                    'Từ (1) và (2) ta có hệ phương trình: '
                    '$\\begin{cases} x = %s + (1-y) \\cdot %s \\\\ y = %s + (1-x) \\cdot %s \\end{cases} \\Leftrightarrow '
                    '\\begin{cases} x = %s \\\\ y = %s \\end{cases}$.\\\\ '
                    'Xác suất có ít nhất một trong hai cổ phiếu giảm giá trong phiên giao dịch là\\\\ '
                    '$P(X \\cup Y) = P(X) + P(Y) - P(X \\cap Y) = %s + %s - %s = %s$.'
                    % (latex(p1), latex(p2), latex(p3), latex(p3), 
                       latex(p3), latex(p1), latex(p3), latex(p2),
                       latex(p3), latex(p1), latex(p3), latex(p2),
                       latex(x_val), latex(y_val),
                       latex(x_val), latex(y_val), latex(p3), kq_str)
                )
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

