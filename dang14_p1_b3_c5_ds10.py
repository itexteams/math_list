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


def bt_dang14_p1_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                n = random.randint(4, 9)  # Số mũ n
                a = random.randint(2, 6)  # Hệ số của x
                b_val = random.choice([-5, -4, -3, -2, 2, 3, 4, 5]) # Hệ số tự do (có âm có dương)

                # Chuẩn bị hiển thị b trong LaTeX
                if b_val < 0:
                    b_tex = '\\left( %s \\right)' % (latex(b_val))
                    b_display = latex(b_val)
                else:
                    b_tex = latex(b_val)
                    b_display = latex(b_val)

                # Số hạng tổng quát đúng: C_n^k * (ax)^{n-k} * b^k = C_n^k * a^{n-k} * b^k * x^{n-k}
                da_dung = 'C_{%s}^k %s^{%s-k} %s^k .x^{%s-k}' % (latex(n), latex(a), latex(n), b_tex, latex(n))

                # Bước 4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                # Sai kiểu 1: Đảo số mũ n-k và k cho a và b
                sai1 = 'C_{%s}^k %s^k %s^{%s-k} .x^{%s-k}' % (latex(n), latex(a), b_tex, latex(n), latex(n))

                # Sai kiểu 2: Mất dấu âm của b (nếu b âm) hoặc đảo số mũ của x
                sai2 = 'C_{%s}^k %s^{%s-k} %s^k .x^{%s-k}' % (latex(n), latex(a), latex(n), latex(abs(b_val)), latex(n))

                # Sai kiểu 3: Đảo toàn bộ số mũ
                sai3 = 'C_{%s}^k %s^k %s^{%s-k} .x^k' % (latex(n), latex(a), b_tex, latex(n))

                # Câu hỏi
                # Biểu thức khai triển: (ax + b)^n
                if b_val > 0:
                    bieu_thuc = '\\left( %sx + %s \\right)^{%s}' % (latex(a), latex(b_val), latex(n))
                else:
                    bieu_thuc = '\\left( %sx %s \\right)^{%s}' % (latex(a), latex(b_val), latex(n))

                noidungcauhoi = ('''Trong khai triển nhị thức Niu-tơn của $%s$, số hạng tổng quát của khai triển là'''
                                 % (bieu_thuc))

                # Các đáp án
                da_d = ('\\True $%s$' % (da_dung))
                da_s1 = '$%s$' % (sai1)
                da_s2 = '$%s$' % (sai2)
                da_s3 = '$%s$' % (sai3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # T_{k+1} = C_n^k (ax)^{n-k} b^k
                loigiai = ('''Số hạng tổng quát của khai triển $%s$ là $C_{%s}^k \\left( %sx \\right)^{%s-k} \\left( %s \\right)^k = C_{%s}^k %s^{%s-k} \\left( %s \\right)^k .x^{%s-k}$.'''
                           % (bieu_thuc, latex(n), latex(a), latex(n), latex(b_val), latex(n), latex(a), latex(n), latex(b_val), latex(n)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

