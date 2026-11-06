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


def bt_dang20_p1_b3_c5_ds11(self):
            # Khai báo biến
            # Danh sách các cơ số cho hàm nghịch biến (0 < a < 1)
            list_giam = [
                {'tex': r'\left( \frac{e}{4} \right)', 'val': math.e/4},
                {'tex': r'\left( \frac{1}{2} \right)', 'val': 0.5},
                {'tex': r'\left( \frac{\pi}{4} \right)', 'val': math.pi/4},
                {'tex': r'\left( \frac{2}{3} \right)', 'val': 2/3},
                {'tex': r'\left( \frac{\sqrt{2}}{2} \right)', 'val': math.sqrt(2)/2},
                {'tex': r'0,5', 'val': 0.5}
            ]

            # Danh sách các cơ số cho hàm đồng biến (a > 1)
            list_tang = [
                {'tex': r'\left( \frac{4}{e} \right)', 'val': 4/math.e},
                {'tex': r'\pi', 'val': math.pi},
                {'tex': r'\left( \sqrt{3} \right)', 'val': math.sqrt(3)},
                {'tex': r'2', 'val': 2},
                {'tex': r'\left( \frac{3}{2} \right)', 'val': 1.5},
                {'tex': r'e', 'val': math.e},
                {'tex': r'\left( \frac{\pi}{3} \right)', 'val': math.pi/3}
            ]

            # Chọn ngẫu nhiên 1 đáp án đúng
            true_choice = random.choice(list_giam)

            # BƯỚC 4: CHỌN 3 ĐÁP ÁN SAI KHÔNG TRÙNG ĐÁP ÁN ĐÚNG
            # Lấy ngẫu nhiên 3 phần tử từ list_tang (đảm bảo không trùng nhau)
            wrong_choices = random.sample(list_tang, k=3)

            # Nội dung câu hỏi
            noidungcauhoi = "Trong các hàm số sau, hàm số nào nghịch biến trên $\\mathbb{R}$?"

            # Các phương án
            da_d = r'\True $y = ' + true_choice['tex'] + r'^x$'
            da_s1 = r'$y = ' + wrong_choices[0]['tex'] + r'^x$'
            da_s2 = r'$y = ' + wrong_choices[1]['tex'] + r'^x$'
            da_s3 = r'$y = ' + wrong_choices[2]['tex'] + r'^x$'

            # Trộn đáp án
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # BƯỚC 2: VIẾT LẠI LỜI GIẢI THEO MẪU
            loigiai = (r"Hàm số mũ $y = a^x$ với $0 < a < 1$ nghịch biến trên $\mathbb{R}$. \\ "
                       r"Xét hàm số $y = " + true_choice['tex'] + r"^x$, ta có cơ số $a = " + true_choice['tex'] + r"$. \\ "
                       r"Vì $0 < a < 1$ nên hàm số $y = " + true_choice['tex'] + r"^x$ nghịch biến trên $\mathbb{R}$.")

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

