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


def bt_dang7_p3_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến Sympy
            t = symbols('t')

            # B1: Nghiên cứu đề bài và B3: Random bài toán
            # Để t_giai là số nguyên dương, ta chọn t_giai trước
            t_giai = random.randint(1, 4) 
            # Chọn các hệ số A, B cho v(t) = At + Bt^2
            A = random.randint(2, 10)
            B = random.randint(2, 6)

            # Vận tốc tại thời điểm cần tìm
            v_t_val = A * t_giai + B * (t_giai**2)

            # Hàm vận tốc v(t)
            v_func = A*t + B*t**2
            # Hàm gia tốc a(t) = v'(t)
            a_func = A + 2*B*t

            # Tính toán kết quả gia tốc đúng
            kq_dung = A + 2*B*t_giai

            # B4: Điều chỉnh phương án sai không trùng đáp án đúng
            s = []
            while len(s) < 3:
                offset = random.choice([-3, -2, -1, 1, 2, 3, 5, 10])
                sai = kq_dung + offset
                if sai > 0 and sai != kq_dung and sai not in s:
                    s.append(sai)

            # Định dạng LaTeX và số thập phân (dấu phẩy)
            da = '$%s$' % (str(kq_dung).replace('.', ','))
            das1 = '$%s$' % (str(s[0]).replace('.', ','))
            das2 = '$%s$' % (str(s[1]).replace('.', ','))
            das3 = '$%s$' % (str(s[2]).replace('.', ','))

            # B2: Viết lại nội dung đề bài và lời giải theo mẫu %s
            # Yêu cầu: Không dùng raw string, dấu ( ) thành \left( \right)
            noidungcauhoi = ('Vận tốc của một chất điểm chuyển động được biểu thị bởi công thức $v\\left(t\\right) = %st + %st^2$, trong đó $t > 0$, $t$ tính bằng giây và $v\\left(t\\right)$ tính bằng mét/giây. Gia tốc của chất điểm tại thời điểm mà vận tốc chuyển động là $%s$ mét/giây bằng bao nhiêu?'
                             % (latex(A), latex(B), latex(v_t_val)))

            # Lời giải chi tiết
            loigiai = ('Ta tính được $v\'\\left(t\\right) = %s + %st$.\\\\'
                       'Ta có $v\\left(t\\right) = %s \\Leftrightarrow %st + %st^2 = %s \\Leftrightarrow t = %s \\left(t > 0\\right)$.\\\\'
                       'Gia tốc của chất điểm $a\\left(t\\right) = v\'\\left(t\\right) = %s + %st \\longrightarrow a\\left(%s\\right) = v\'\\left(%s\\right) = %s + %s \\cdot %s = %s$ m/s$^2$.'
                       % (latex(A), latex(2*B),
                          latex(v_t_val), latex(A), latex(B), latex(v_t_val), latex(t_giai),
                          latex(A), latex(2*B), latex(t_giai), latex(t_giai), latex(A), latex(2*B), latex(t_giai), latex(kq_dung)))
            dapan='\\shortans[0]{$%s$}\n'%(kq_dung)
            # Các đáp án
            da_d = '\\True ' + str(da)
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa vào danh sách và shuffle
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

