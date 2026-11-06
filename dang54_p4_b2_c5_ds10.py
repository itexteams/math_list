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


def bt_dang54_p4_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            # Random số lượng bạn nam và bạn nữ (tương ứng với số ghế mỗi dãy)
            lis_n = [3, 4, 5]
            n = random.choice(lis_n)

            # Tính toán các giá trị trung gian cho lời giải
            steps_loigiai = ""
            total_ways_calc = 1
            for i in range(n, 0, -1):
                cach_ghe_day1 = 2 * i
                cach_ghe_day2 = i
                total_ways_calc *= (cach_ghe_day1 * cach_ghe_day2)
                steps_loigiai += "Chọn 1 bạn ngồi vào ghế số $%s$ dãy 1: $%s$ cách. Có $%s$ cách chọn 1 bạn ngồi vào ghế số $%s$ dãy 2 (phải khác giới tính với bạn ở dãy 1).\\\\ \n" % (latex(n - i + 1), latex(cach_ghe_day1), latex(cach_ghe_day2), latex(n - i + 1))

            # Kết quả đúng theo định dạng n! * n! * 2^n
            da_correct = '$%s! \\cdot %s! \\cdot 2^{%s}$' % (latex(n), latex(n), latex(n))

            # Các đáp án trắc nghiệm
            s = [
                '$%s! \\cdot %s! \\cdot 2$' % (latex(n), latex(n)),
                '$%s! \\cdot 2^{%s}$' % (latex(n), latex(n)),
                '$%s! \\cdot %s!$' % (latex(n), latex(n)),
                '$%s! \\cdot 2$' % (latex(n)),
                '$2 \\cdot %s!$' % (latex(n)),
                '$%s \\cdot %s! \\cdot %s!$' % (latex(2*n), latex(n), latex(n))
            ]

            # Đảm bảo không trùng đáp án đúng
            if da_correct in s:
                s.remove(da_correct)

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Tạo bảng dữ liệu bằng TikZ (Tabular)
            header_row = 'Dãy 1'
            footer_row = 'Dãy 2'
            for i in range(1, n + 1):
                header_row += ' & Ghế số %s' % i
                footer_row += ' & Ghế số %s' % i

            tikz_table = (
                '\\begin{center}\n'
                '\\begin{tabular}{|' + 'c|' * (n + 1) + '}\n'
                '\\hline\n'
                '%s \\\\ \\hline\n'
                '%s \\\\ \\hline\n'
                '\\end{tabular}\n'
                '\\end{center}'
            ) % (header_row, footer_row)

            # Câu hỏi
            noidungcauhoi = ('''Cho hai dãy ghế được xếp như sau:
            %s
            Xếp $%s$ bạn nam và $%s$ bạn nữ vào hai dãy ghế trên. Hai người được gọi là ngồi đối diện với nhau nếu ngồi ở hai dãy và có cùng vị trí ghế. Tìm số cách xếp để mỗi bạn nam ngồi đối diện với một bạn nữ.'''
                             % (tikz_table, latex(n), latex(n)))

            # Các đáp án
            da_d = ('\\True ' + str(da_correct))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = ('''Để mỗi bạn nam ngồi đối diện với một bạn nữ, ta thực hiện xếp các bạn vào từng cặp ghế đối diện (ghế cùng số ở hai dãy):\\\\
            %s
            Tổng số cách xếp là:\\\\
            $ \\left( %s \\cdot %s \\right) \\cdot \\left( %s \\cdot %s \\right) \\cdot \\dots \\cdot \\left( 2 \\cdot 1 \\right) = \\left( %s \\cdot %s \\cdot \\dots \\cdot 1 \\right) \\cdot \\left( %s \\cdot %s \\cdot \\dots \\cdot 2 \\right) $\\\\
            $= %s! \\cdot \\left( 2^{%s} \\cdot %s! \\right) = %s! \\cdot %s! \\cdot 2^{%s}$.'''
                       % (steps_loigiai, 
                          latex(2*n), latex(n), latex(2*n-2), latex(n-1), 
                          latex(n), latex(n-1), 
                          latex(2*n), latex(2*n-2),
                          latex(n), latex(n), latex(n), latex(n), latex(n), latex(n)))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

