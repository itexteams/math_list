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


def bt_dang28_p1_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số hộ gia đình từ 15 đến 25
                n = randint(15, 25)

                # Random số con, dùng weights để mô phỏng thực tế (nhiều nhà có 1, 2, 3 con; ít nhà có 0 hoặc >4 con)
                data = random.choices([0, 1, 2, 3, 4, 5, 6, 7], weights=[10, 30, 35, 15, 5, 3, 1, 1], k=n)

                # Chuỗi dữ liệu hiển thị (cách nhau bởi khoảng trắng lớn)
                data_str = " \\quad ".join(map(str, data))

                # Tính toán chính xác bằng Decimal
                n_dec = Decimal(n)
                mean_dec = sum(Decimal(val) for val in data) / n_dec
                variance_dec = sum((Decimal(val) - mean_dec)**2 for val in data) / n_dec
                std_dec = variance_dec.sqrt()

                # Làm tròn giá trị trung bình và phương sai (để hiển thị lời giải đẹp hơn, có thể làm tròn đến 2 hoặc 3 chữ số)
                mean_str = str(mean_dec.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP).normalize()).replace('.', ',')
                variance_str = str(variance_dec.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP).normalize()).replace('.', ',')

                # Đáp án đúng (độ lệch chuẩn làm tròn đến hàng phần trăm - 2 chữ số thập phân)
                kq_round = std_dec.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq_round).replace('.', ',')

                # Các đáp án trắc nghiệm nhiễu (lệch 0.01, 0.1, 0.02...)
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = [
                    '$%s$' % str(kq_round + Decimal('0.01')).replace('.', ','),
                    '$%s$' % str(kq_round - Decimal('0.01')).replace('.', ','),
                    '$%s$' % str(kq_round + Decimal('0.10')).replace('.', ','),
                    '$%s$' % str(kq_round - Decimal('0.10')).replace('.', ','),
                    '$%s$' % str(kq_round + Decimal('0.02')).replace('.', ','),
                    '$%s$' % str(kq_round - Decimal('0.02')).replace('.', ',')
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Số liệu sau đây cho biết số con được sinh ra trong $%s$ hộ gia đình được khảo sát ở một địa phương:
                \\begin{center}
                %s
                \\end{center}
                Độ lệch chuẩn của mẫu số liệu đã cho \\textit{Kết quả làm tròn đến hàng phần trăm} bằng''' % (n, data_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Giá trị trung bình của mẫu là: $\\overline{x} = \\frac{%s + %s + \\dots + %s + %s}{%s} = %s$ (con). \\\\
                Phương sai là: $s^2 = \\frac{1}{%s} \\left[ (x_1 - \\overline{x})^2 + (x_2 - \\overline{x})^2 + \\dots + (x_{%s} - \\overline{x})^2 \\right] = %s$. \\\\
                Độ lệch chuẩn: $s = \\sqrt{s^2} \\approx %s$ (con).''' % (
                    data[0], data[1], data[-2], data[-1], n, mean_str,
                    n, n, variance_str,
                    kq
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

