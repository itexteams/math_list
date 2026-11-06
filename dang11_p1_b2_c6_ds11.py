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


def bt_dang11_p1_b2_c6_ds11(self):
            # Khai báo biến
            # Hộp B: w2 (trắng), r2 (đỏ), x2 (xanh)

            w1 = random.randint(3, 8)
            r1 = random.randint(3, 8)
            x1 = random.randint(3, 8)

            w2 = random.randint(3, 8)
            r2 = random.randint(3, 8)
            x2 = random.randint(3, 8)

            # Tổng số bi mỗi hộp
            t1 = w1 + r1 + x1
            t2 = w2 + r2 + x2

            # Xác suất từng trường hợp (dùng Rational để giữ phân số tối giản)
            pa1 = Rational(w1 * w2, t1 * t2)
            pa2 = Rational(r1 * r2, t1 * t2)
            pa3 = Rational(x1 * x2, t1 * t2)

            # Xác suất tổng (đáp án đúng)
            kq = pa1 + pa2 + pa3

            # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
            s = set()
            while len(s) < 3:
                # Tạo các giá trị sai quanh đáp án đúng hoặc đảo ngược tử mẫu
                fake_num = kq.p + random.randint(-10, 10)
                fake_den = kq.q + random.randint(-5, 5)
                if fake_num > 0 and fake_num < fake_den:
                    wrong_val = Rational(fake_num, fake_den)
                    if wrong_val != kq:
                        s.add('$%s$' % latex(wrong_val))

            das1, das2, das3 = list(s)

            # Câu hỏi
            noidungcauhoi = (
                'Hộp $A$ có $%s$ viên bi trắng, $%s$ viên bi đỏ và $%s$ viên bi xanh. '
                'Hộp $B$ có $%s$ viên bi trắng, $%s$ viên bi đỏ và $%s$ viên bi xanh. '
                'Lấy ngẫu nhiên mỗi hộp một viên bi. Xác suất để hai viên bi được lấy ra có cùng màu là'
                % (latex(w1), latex(r1), latex(x1), latex(w2), latex(r2), latex(x2))
            )

            # Đáp án
            da_d = '\\True $%s$' % latex(kq)
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Bước 2: Viết lại lời giải chi tiết theo mẫu
            loigiai = (
                'Gọi biến cố $A$: “Hai viên bi được lấy ra có cùng màu”.\\\\ '
                '$A_1$: “Hai viên bi lấy ra màu trắng”. Lúc đó: $P\\left(A_1\\right) = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = %s$.\\\\ '
                '$A_2$: “Hai viên bi lấy ra màu đỏ”. Lúc đó: $P\\left(A_2\\right) = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = %s$.\\\\ '
                '$A_3$: “Hai viên bi lấy ra màu xanh”. Lúc đó: $P\\left(A_3\\right) = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = %s$.\\\\ '
                'Lúc đó: $A = A_1 \\cup A_2 \\cup A_3$ và $A_1, A_2, A_3$ là các biến cố xung khắc nên:\\\\ '
                '$P\\left(A\\right) = P\\left(A_1\\right) + P\\left(A_2\\right) + P\\left(A_3\\right) = %s$.'
                % (
                    latex(w1), latex(t1), latex(w2), latex(t2), latex(pa1),
                    latex(r1), latex(t1), latex(r2), latex(t2), latex(pa2),
                    latex(x1), latex(t1), latex(x2), latex(t2), latex(pa3),
                    latex(kq)
                )
            )

            # Xuất nội dung theo cấu trúc yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

