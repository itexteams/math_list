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


def bt_dang81_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số mũ chẵn n
                n = random.choice([2020, 2022, 2024, 2026, 2028])

                # Cặp số a, b sao cho cơ số chứa giá trị âm và trị tuyệt đối lớn nhất nằm ở biên dương (a+b)
                # Ví dụ chọn a = 3, b = 5 -> 3 - 5 = -2 và 3 + 5 = 8 = 2^3
                # Để lũy thừa đưa về cơ số 2 đẹp mắt, ta chọn a và b sao cho a + b = 8 (2^3) hoặc 4 (2^2) hoặc 16 (2^4)
                # Ta chọn tổng bằng 8: (a, b) có thể là (3, 5), (1, 7), (2, 6)
                a, b = random.choice([(3, 5), (1, 7), (2, 6)])

                cang_duoi = a - b
                cang_tren = a + b

                # Ở đây cơ số là lũy thừa của 2: 8 = 2^3
                # Lũy thừa lớn nhất: 8^n = (2^3)^n = 2^(3n)
                mu_M = 3 * n

                # Tính toán các giá trị
                m_val = 0
                M_val = '2^{%s}' % (mu_M)

                # Đáp án đúng: M + m = 2^(3n) + 0 = 2^(3n)
                da = '2^{%s}' % (mu_M)
                du = ['$%s$' % (da)]
                da_choice = random.choice(du)

                # Các đáp án nhiễu theo cấu trúc bài toán gốc
                s = [
                    '$2^{%s}\\left(1 + 2^{%s}\\right)$' % (n, 2*n),
                    '$2^{%s}$' % (n),
                    '$2^{%s}$' % (2*n),
                    '$2^{%s}$' % (mu_M + n),
                    '$2^{%s}$' % (mu_M - n)
                ]
                if da in s:
                    s.remove(da)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Giá trị lớn nhất, giá trị nhỏ nhất của hàm số $y = (%s - %s\\sin x)^{%s}$ là $M$, $m$. Khi đó giá trị $M + m$ là'''
                                 % (latex(a), latex(b), latex(n)))

                # Lời giải chi tiết từng bước theo đúng mẫu gốc
                loigiai = ('''Vì $%s \\le %s - %s\\sin x \\le %s$ nên suy ra $0 \\le (%s - %s\\sin x)^{%s} \\le %s^{%s} = 2^{%s}$.\\\\
                           Do đó $m = 0$ và $M = 2^{%s}$.\\\\
                           Vậy $M + m = 2^{%s}$.'''
                           % (latex(cang_duoi), latex(a), latex(b), latex(cang_tren), latex(a), latex(b), latex(n), latex(cang_tren), latex(n), latex(mu_M),
                              latex(mu_M), latex(mu_M)))

            # Các đáp án định dạng trắc nghiệm
            da_d = ('\\True ' + str(da_choice))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Trộn ngẫu nhiên thứ tự các phương án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm đúng định dạng khung chương trình mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

