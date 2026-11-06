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


def bt_dang13_p3_b2_c5_ds10(self):
            while True:
                # Hệ số a, b, c trong khoảng [-5, 5] để tránh tích quá lớn
                a = random.choice([x for x in range(-5, 6) if x not in [0, 1]])
                b = random.choice([x for x in range(-5, 6) if x not in [0, 1]])
                c = random.choice([x for x in range(-5, 6) if x not in [0, 1]])

                # Hoán vị P_n (n từ 2 đến 5, P_5 = 120)
                n1 = randint(2, 5)
                p = factorial(n1)

                # Chỉnh hợp A_n^k (Giới hạn n nhỏ vì chỉnh hợp tăng rất nhanh)
                k2 = randint(2, 4)
                nk2 = randint(0, 2)
                n2 = k2 + nk2
                ch = factorial(n2) // factorial(n2 - k2)

                # Tổ hợp C_n^k
                k3 = randint(2, 5)
                nk3 = randint(0, 3)
                n3 = k3 + nk3
                th = factorial(n3) // (factorial(k3) * factorial(n3 - k3))

                # Tính tổng
                kq_val = a * p + b * ch + c * th

                # Kiểm tra điều kiện đề bài: -999 < kq < 9999
                if -999 < kq_val < 9999:
                    kq = kq_val
                    break

            # Câu hỏi
            noidungcauhoi = '''Giá trị $%s \\mathrm{P}_{%s} + %s \\mathrm{A}_{%s}^{%s} + %s \\mathrm{C}_{%s}^{%s}$ bằng bao nhiêu?''' % (
                latex(a), latex(n1), latex(b), latex(n2), latex(k2), latex(c), latex(n3), latex(k3)
            )

            # Các đáp án
            da_d = '\\True $%s$' % (latex(kq))

            # Tạo đáp án nhiễu (đảm bảo không trùng và không quá lớn)
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, -10, 2, -2])
                nhieu = kq + offset
                if nhieu != kq:
                    s_set.add('$%s$' % (latex(nhieu)))

            list_1 = [da_d] + list(s_set)
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ( 'Giá trị $%s \\mathrm{P}_{%s} + %s \\mathrm{A}_{%s}^{%s} + %s \\mathrm{C}_{%s}^{%s} = %s \\cdot %s! + %s \\cdot \\dfrac{%s!}{(%s-%s)!} + %s \\cdot \\dfrac{%s!}{%s!(%s-%s)!} = %s$.' % (
                latex(a), latex(n1), latex(b), latex(n2), latex(k2), latex(c), latex(n3), latex(k3),
                latex(a), latex(n1), latex(b), latex(n2), latex(n2), latex(k2), latex(c), latex(n3), latex(k3), latex(n3), latex(k3), latex(kq)
            ))

            # Đáp án ngắn
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq))

            # Xuất câu trắc nghiệm và xử lý định dạng chuỗi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')

            return content

