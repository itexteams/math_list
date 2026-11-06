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


def bt_dang28_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # p1: tỉ lệ sản lượng phân xưởng I (%), p2: phân xưởng II
                p1_val = random.choice([30, 40, 50, 25, 45])
                p2_val = 100 - p1_val

                # d1, d2: tỉ lệ phế phẩm tương ứng (%)
                d1_val = random.choice([1, 2, 3])
                d2_val = random.choice([2, 4, 5])

                # Chuyển sang số thập phân để tính toán
                P_B = Rational(p1_val, 100)
                P_notB = Rational(p2_val, 100)
                P_A_B = Rational(d1_val, 100)
                P_A_notB = Rational(d2_val, 100)

                # Tính xác suất đầy đủ P(A)
                P_A = P_B * P_A_B + P_notB * P_A_notB

                # Tính xác suất hậu nghiệm P(B|A) theo công thức Bayes
                kq_frac = (P_B * P_A_B) / P_A

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_float = float(kq_frac)
                kq_dec = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Định dạng dấu phẩy cho số thập phân
                def format_vn(val):
                    return str(val).replace('.', ',')

                kq_str = format_vn(kq_dec)

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                du = ['$%s$' % (kq_str)]
                da = du[0]

                s = set()
                while len(s) < 3:
                    sai = kq_dec + Decimal(str(random.choice([-0.1, 0.1, -0.05, 0.05, 0.12, -0.08])))
                    if sai > 0 and sai < 1 and sai != kq_dec:
                        s.add('$%s$' % (format_vn(sai)))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # B2: Viết lại nội dung câu hỏi
                noidungcauhoi = (
                    'Một nhà máy có hai phân xưởng $I$ và $II$ tương ứng làm ra $%s\\%%$ và $%s\\%%$ sản phẩm của nhà máy. '
                    'Biết rằng tỷ lệ phế phẩm của hai phân xưởng $I$ và $II$ tương ứng là $%s\\%%$ và $%s\\%%$. '
                    'Chọn ngẫu nhiên một sản phẩm của nhà máy thì thấy nó là phế phẩm. '
                    'Xác suất để sản phẩm đó thuộc phân xưởng $I$ là bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                    % (latex(p1_val), latex(p2_val), latex(d1_val), latex(d2_val))
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (không viết tắt)
                loigiai = (
                    'Gọi $A$ là biến cố "sản phẩm lấy ra là phế phẩm".\\\\ '
                    'Gọi $B$ là biến cố "sản phẩm lấy ra thuộc phân xưởng $I$".\\\\ '
                    'Theo dữ kiện bài toán, xác suất để sản phẩm lấy ra thuộc phân xưởng $I$ biết rằng sản phẩm đó là phế phẩm, ta cần tính $P(B|A)$.\\\\ '
                    'Theo công thức Bayes: $P(B|A) = \\frac{P(B).P(A|B)}{P(A)}$.\\\\ '
                    'Ta có: $P(B) = %s\\%% = %s$. $P(A|B) = %s\\%% = %s$.\\\\ '
                    '$P(A) = P(B).P(A|B) + P(\\overline{B}).P(A|\\overline{B}) = %s.%s + %s.%s = %s$.\\\\ '
                    'Vậy $P(B|A) = \\frac{P(B).P(A|B)}{P(A)} = \\frac{%s.%s}{%s} = %s \\approx %s$.'
                    % (
                        latex(p1_val), format_vn(float(P_B)), 
                        latex(d1_val), format_vn(float(P_A_B)),
                        format_vn(float(P_B)), format_vn(float(P_A_B)), 
                        format_vn(float(P_notB)), format_vn(float(P_A_notB)), 
                        format_vn(float(P_A)),
                        format_vn(float(P_B)), format_vn(float(P_A_B)), 
                        format_vn(float(P_A)),
                        latex(kq_frac), kq_str
                    )
                )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

            # Xuất câu trắc nghiệm (không dùng raw string r)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

