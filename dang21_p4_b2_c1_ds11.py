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


def bt_dang21_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập tham số ngẫu nhiên logic
                # Giả sử tan(beta/2) = k * tan(alpha/2). Trong đề gốc k = 4.
                # Ta chọn ngẫu nhiên k nguyên dương từ 2 đến 6 (loại bỏ k=1 để tử số không triệt tiêu)
                k = randint(2, 6)


                c1 = k - 1 # Hệ số của sin(alpha) ở tử và cos(alpha) ở mẫu
                c2 = k + 1 # Hệ số tự do dưới mẫu

                # Định dạng chuỗi LaTeX cho phương án đúng
                da_dung_str = '\\frac{%s\\sin \\alpha}{%s - %s\\cos \\alpha}' % (latex(c1), latex(c2), latex(c1))
                da = '$%s$' % da_dung_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Điều chỉnh tập hợp các phương án nhiễu không trùng đáp án đúng
                s_set = set()
                nhiieu_list = [
                    '\\frac{%s\\sin \\alpha}{%s + %s\\cos \\alpha}' % (latex(c1), latex(c2), latex(c1)),
                    '\\frac{%s\\cos \\alpha}{%s - %s\\cos \\alpha}' % (latex(c1), latex(c2), latex(c1)),
                    '\\frac{%s\\cos \\alpha}{%s + %s\\cos \\alpha}' % (latex(c1), latex(c2), latex(c1)),
                    '\\frac{%s\\sin \\alpha}{%s - %s\\sin \\alpha}' % (latex(c1), latex(c2), latex(c1))
                ]

                for item in nhiieu_list:
                    p_an = '$%s$' % item
                    if p_an != da:
                        s_set.add(p_an)

                list_sai = list(s_set)
                random.shuffle(list_sai)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\tan \\frac{\\beta}{2} = %s\\tan \\frac{\\alpha}{2}$. Tính $\\tan \\frac{\\beta - \\alpha}{2}$.'''
                                 % latex(k))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Trình bày lời giải chi tiết rõ ràng từng bước bám sát nội dung gốc
                loigiai = ('''Ta có: \\\\
            $\\tan \\frac{\\beta - \\alpha}{2} = \\frac{\\tan \\frac{\\beta}{2} - \\tan \\frac{\\alpha}{2}}{1 + \\tan \\frac{\\beta}{2} \\cdot \\tan \\frac{\\alpha}{2}} = \\frac{%s\\tan \\frac{\\alpha}{2}}{1 + %s\\tan^2 \\frac{\\alpha}{2}}$ \\\\
            = $\\frac{%s\\sin \\frac{\\alpha}{2} \\cdot \\cos \\frac{\\alpha}{2}}{1 + %s\\sin^2 \\frac{\\alpha}{2}} = \\frac{%s\\sin \\alpha}{%s - %s\\cos \\alpha}$.'''
                           % (latex(c1), latex(k), latex(c1), latex(c1), latex(c1), latex(c2), latex(c1)))

            # Xuất câu trắc nghiệm định dạng minipage TeX theo đúng khuôn mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

