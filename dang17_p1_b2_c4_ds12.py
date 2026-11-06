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


def bt_dang17_p1_b2_c4_ds12(self):
            # Khai báo biến
            # Ta chọn ngẫu nhiên để tạo đa dạng
            p_b = Decimal(str(random.choice([0.6, 0.7, 0.8])))
            p_a_given_b = Decimal(str(random.choice([0.6, 0.7])))
            p_a_given_not_b = Decimal(str(random.choice([0.3, 0.4, 0.45])))

            # Tính toán các giá trị
            p_not_b = 1 - p_b
            p_a = (p_b * p_a_given_b) + (p_not_b * p_a_given_not_b)
            kq_value = (p_b * p_a_given_b) / p_a

            # Làm tròn kết quả để hiển thị (lấy 2 chữ số thập phân)
            kq_display = kq_value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kq_str = str(kq_display).replace('.', ',')

            # Tạo các đáp án nhiễu (distractors)
            # Đảm bảo không trùng với đáp án đúng
            distractors = set()
            while len(distractors) < 3:
                offset = Decimal(str(random.randint(5, 20))) / 100
                if random.choice([True, False]):
                    wrong = kq_value + offset
                else:
                    wrong = kq_value - offset

                # Không để giá trị âm hoặc > 1
                if 0 < wrong < 1:
                    wrong_str = str(wrong.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if wrong_str != kq_str:
                        distractors.add(wrong_str)

            list_distractors = list(distractors)

            # Chuẩn bị nội dung câu hỏi
            noidungcauhoi = ('''Cho hai biến cố $A$ và $B$, với $P(B)=%s$, $P(A|B)=%s$, $P(A|\\overline{B})=%s$. Giá trị $P(B|A)$ bằng'''
                             %(str(p_b).replace('.', ','), 
                               str(p_a_given_b).replace('.', ','), 
                               str(p_a_given_not_b).replace('.', ',')
                              ))

            # Chuẩn bị lời giải chi tiết
            loigiai = ('''Theo công thức xác suất toàn phần:\\\\
                         $P(A) = P(B) \\cdot P(A|B) + P(\\overline{B}) \\cdot P(A|\\overline{B}) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\
                         Theo công thức Bayes:\\\\
                         $P(B|A) = \\frac{P(B) \\cdot P(A|B)}{P(A)} = \\frac{%s \\cdot %s}{%s} = %s$.'''
                       %(str(p_b).replace('.', ','), str(p_a_given_b).replace('.', ','), 
                         str(p_not_b).replace('.', ','), str(p_a_given_not_b).replace('.', ','), 
                         str(p_a).replace('.', ','),
                         str(p_b).replace('.', ','), str(p_a_given_b).replace('.', ','), 
                         str(p_a).replace('.', ','), kq_str
                        ))

            # Các đáp án
            da_d = ('\\True ' + kq_str)
            list_1 = [da_d, list_distractors[0], list_distractors[1], list_distractors[2]]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

