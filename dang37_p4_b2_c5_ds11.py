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


def bt_dang37_p4_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (theo mẫu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                a = random.choice([2, 3, 4, 5, 6, 10]) # Cơ số a

                # Đáp án đúng
                kq = 1
                da_d = '\\True $%s$' % latex(kq)

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s_list = [
                    '$0$', 
                    '$2$', 
                    '$%s$' % latex(Rational(1, 2)), 
                    '$-1$', 
                    '$%s$' % latex(a),
                    '$\\frac{3}{2}$'
                ]
                random.shuffle(s_list)

                # Lấy 3 đáp án sai khác với đáp án đúng (trong trường hợp kq lọt vào list s)
                selected_s = []
                for item in s_list:
                    if item != '$1$' and len(selected_s) < 3:
                        selected_s.append(item)

                da_s1, da_s2, da_s3 = selected_s

                # B2: Viết lại nội dung câu hỏi
                noidungcauhoi = (
                    '''Cho hàm số $f(x) = \\frac{1}{2} \\log_{%s} \\left( \\frac{%sx}{1-x} \\right)$ và hai số thực $m, n$ thuộc khoảng $(0;1)$ sao cho $m + n = 1$. Tính $f(m) + f(n)$.'''
                    % (latex(a), latex(a))
                )

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (
                    '''$f(m) + f(n) = \\frac{1}{2} \\log_{%s} \\left( \\frac{%sm}{1-m} \\right) + \\frac{1}{2} \\log_{%s} \\left( \\frac{%sn}{1-n} \\right)$ \\\\
                    $= \\frac{1}{2} \\left[ \\log_{%s} \\left( \\frac{%sm}{1-m} \\right) + \\log_{%s} \\left( \\frac{%sn}{1-n} \\right) \\right]$ \\\\
                    $= \\frac{1}{2} \\log_{%s} \\left( \\frac{%sm \\cdot %sn}{(1-m)(1-n)} \\right)$ \\\\
                    $= \\frac{1}{2} \\log_{%s} \\left( \\frac{%smn}{1 - (m+n) + mn} \\right)$. \\\\
                    Vì $m+n=1$ nên $(1-m)(1-n) = 1 - 1 + mn = mn$. \\\\
                    Vậy $f(m) + f(n) = \\frac{1}{2} \\log_{%s} \\left( \\frac{%smn}{mn} \\right) = \\frac{1}{2} \\log_{%s} (%s) = \\frac{1}{2} \\cdot 2 = 1$.'''
                    % (latex(a), latex(a), latex(a), latex(a), 
                       latex(a), latex(a), latex(a), latex(a), 
                       latex(a), latex(a), latex(a),
                       latex(a), latex(a**2),
                       latex(a), latex(a**2),
                       latex(a), latex(a**2))
                )

            # Xuất câu trắc nghiệm theo mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

