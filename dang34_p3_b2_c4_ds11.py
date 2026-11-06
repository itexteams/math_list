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


def bt_dang34_p3_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo các thông số ngẫu nhiên
            h = random.randint(20, 60) # Chiều cao vách đá
            a = random.randint(4, 6)   # Hệ số trong công thức s(t) = a*t^2

            # 1. Tính toán thời điểm chạm đất t0
            t0_val = math.sqrt(h/a)
            t0_rounded = round(t0_val, 4)

            # 2. Tính vận tốc tại thời điểm t0: v(t) = s'(t) = 2*a*t
            v_val = 2 * a * t0_val

            # 3. Làm tròn kết quả đến hàng phần chục
            kq_decimal = Decimal(str(v_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq_str = str(kq_decimal).replace('.', ',')

            # 4. Tạo các đáp án nhiễu
            wrong_1 = Decimal(str(v_val + random.uniform(2, 5))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            wrong_2 = Decimal(str(v_val - random.uniform(2, 5))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            wrong_3 = Decimal(str(v_val + random.uniform(6, 10))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

            da_d = '\\True $' + kq_str + '$'
            da_s1 = '$' + str(wrong_1).replace('.', ',') + '$'
            da_s2 = '$' + str(wrong_2).replace('.', ',') + '$'
            da_s3 = '$' + str(wrong_3).replace('.', ',') + '$'

            # Trộn đáp án
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Nội dung câu hỏi (Sử dụng .format)
            noidungcauhoi = ('''Giả sử khoảng cách từ đỉnh của vách đá đến mặt đất là ${0} \\text{{ m}}$. Một hòn đá rơi từ đỉnh của vách đá xuống đất, sau khoảng thời gian $t$ giây, khoảng cách của nó so với đỉnh của vách đá là $s(t) = {1}t^2$. Vận tốc của hòn đá tại thời điểm hòn đá chạm xuống đất bằng bao nhiêu? (làm tròn đến hàng phần chục và đơn vị là $\\text{{m/s}}$).'''
                             .format(h, a))

            # Nội dung lời giải (Sử dụng .format, lưu ý dùng {{ }} để hiển thị dấu { } của LaTeX)
            loigiai = ('''Hòn đá sẽ chạm đất khi và chỉ khi $s(t) = {0}t^2 = {1} \\Leftrightarrow t^2 = {2} \\Leftrightarrow t = \\sqrt{{{2}}} \\approx {3} \\text{{ (s)}}$.\\\\
            Tại thời điểm hòn đá chạm xuống đất, vận tốc của hòn đá là:\\\\
            $\\lim_{{t \\to \\sqrt{{{2}}}}} \\frac{{s(t) - s(\\sqrt{{{2}}})}}{{t - \\sqrt{{{2}}}}} = \\lim_{{t \\to \\sqrt{{{2}}}}} \\frac{{{0}t^2 - {0} \\cdot (\\sqrt{{{2}}})^2}}{{t - \\sqrt{{{2}}}}} = \\lim_{{t \\to \\sqrt{{{2}}}}} {4}(t + \\sqrt{{{2}}}) = {5}\\sqrt{{{2}}} \\approx {6} \\text{{ (m/s)}}$.'''
                       .format(a, h, h/a, t0_rounded, a, 2*a, kq_str))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+ '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

