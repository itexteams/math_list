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


def bt_dang27_p1_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random 5 mức sản lượng liên tiếp
                start_x = randint(15, 25)
                x_vals = [start_x + i for i in range(5)]

                # Random tần số cho từng mức sản lượng
                n_vals = [randint(4, 15) for _ in range(5)]

                # Tổng số thửa ruộng
                N = sum(n_vals)

                # Tính toán chính xác bằng Decimal
                N_dec = Decimal(N)

                # Tính giá trị trung bình
                sum_nx = sum(Decimal(n) * Decimal(x) for n, x in zip(n_vals, x_vals))
                mean_dec = sum_nx / N_dec

                # Tính phương sai
                sum_var = sum(Decimal(n) * (Decimal(x) - mean_dec)**2 for n, x in zip(n_vals, x_vals))
                variance_dec = sum_var / N_dec

                # Tính độ lệch chuẩn
                std_dec = variance_dec.sqrt()

                # Làm tròn các giá trị trung gian (để hiển thị)
                mean_str = str(mean_dec.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                variance_str = str(variance_dec.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # Đáp án đúng (độ lệch chuẩn làm tròn đến hàng phần mười)
                kq_round = std_dec.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_round).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = [
                    '$%s$' % str(kq_round + Decimal('0.1')).replace('.', ','),
                    '$%s$' % str(kq_round - Decimal('0.1')).replace('.', ','),
                    '$%s$' % str(kq_round + Decimal('1.0')).replace('.', ','),
                    '$%s$' % str(kq_round - Decimal('1.0')).replace('.', ','),
                    '$%s$' % str(kq_round + Decimal('0.2')).replace('.', ','),
                    '$%s$' % str(kq_round - Decimal('0.2')).replace('.', ',')
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Chuỗi Bảng tần số LaTeX
                bang_tan_so = ('''\\begin{center}
                \\begin{tabular}{|l|c|c|c|c|c|}
                \\hline
                Sản lượng & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
                \\hline
                Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
                \\hline
                \\end{tabular}
                \\end{center}''' % (
                    x_vals[0], x_vals[1], x_vals[2], x_vals[3], x_vals[4],
                    n_vals[0], n_vals[1], n_vals[2], n_vals[3], n_vals[4]
                ))

                # Câu hỏi
                noidungcauhoi = ('''Sản lượng lúa (đơn vị: tạ) của $%s$ thửa ruộng thí nghiệm có cùng diện tích được trình bày trong bảng tần số sau đây:
                %s
                Độ lệch chuẩn của mẫu số liệu đã cho \\textit{Kết quả làm tròn đến hàng phần mười} là''' % (N, bang_tan_so))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Sản lượng trung bình của $%s$ thửa ruộng là: \\\\
                $\\overline{x} = \\frac{1}{%s}(%s \\cdot %s + %s \\cdot %s + %s \\cdot %s + %s \\cdot %s + %s \\cdot %s) = %s$ (tạ)\\\\
                Phương sai: $s^2 = \\frac{1}{%s} \\left[ n_1(x_1 - \\overline{x})^2 + n_2(x_2 - \\overline{x})^2 + \\dots + n_5(x_5 - \\overline{x})^2 \\right] = %s$.\\\\
                Độ lệch chuẩn: $s = \\sqrt{s^2} = \\sqrt{%s} \\approx %s$ (tạ).''' % (
                    N, N,
                    n_vals[0], x_vals[0], n_vals[1], x_vals[1], n_vals[2], x_vals[2], n_vals[3], x_vals[3], n_vals[4], x_vals[4],
                    mean_str,
                    N, variance_str,
                    variance_str, kq
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

