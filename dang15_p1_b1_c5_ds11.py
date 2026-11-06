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


def bt_dang15_p1_b1_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            a = symbols('a')

            # Danh sách dạng bài
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dạng 1: Giống hệt hình ảnh mẫu
                m = 5
                p = 1
                n = 3
            else:
                # Dạng 2: Random bài toán mới
                # Chọn mẫu số n từ 2 đến 6
                n = randint(2, 9)
                # Chọn tổng số mũ k (để kết quả là số nguyên cho đẹp giống mẫu)
                k = randint(1, 9)
                tong_tu = n * k
                # Tách tổng tử số thành 2 phần m và p
                m = randint(1, tong_tu - 1)
                p = tong_tu - m

            # Tính toán giá trị
            mu1 = Rational(m, n)
            mu2 = Rational(p, n)
            tong_mu = mu1 + mu2
            ket_qua = a**tong_mu

            # Đáp án đúng
            da_dung = '$%s$' % latex(ket_qua)

            # Các đáp án nhiễu (sai lầm phổ biến)
            s = [
                '$%s$' % latex(a**(mu1 * mu2)),                # Sai: Nhân hai số mũ
                '$%s$' % latex(a**(mu1 - mu2)),                # Sai: Trừ hai số mũ
                '$%s$' % latex(a**(Rational(m + p, 2 * n))),   # Sai: Cộng cả tử và mẫu số mũ
                '$%s$' % latex(a**(Rational(m, p))),           # Sai: Lấy tử chia tử
                '$%s$' % latex(a**(mu1 + 2)),                  # Sai: Cộng nhầm số nguyên
            ]

            # Trộn và lấy 3 đáp án sai
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # Gán nhãn đáp án đúng
            da_d = ('\\True ' + str(da_dung))

            # Đưa vào danh sách chọn ngẫu nhiên vị trí
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Câu hỏi
            noidungcauhoi = (r'Với $a$ là số thực dương tùy ý, biểu thức $a^{%s} \cdot a^{%s}$ là' 
                             % (latex(mu1), latex(mu2)))

            # Nội dung lời giải
            loigiai = (r'Ta có $a^{%s} \cdot a^{%s} = a^{%s + %s} = %s$.' 
                       % (latex(mu1), latex(mu2), latex(mu1), latex(mu2), latex(ket_qua)))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
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

