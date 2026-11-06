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


def bt_dang27_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến và thiết lập bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Random bài toán bằng cách thay đổi các hệ số a và b trong sqrt(a + b*cosx)
                # Trong đề gốc: a = 2, b = 1
                a = random.randint(1, 5)
                b = random.randint(1, 5)

                # Thiết lập biểu thức toán học
                f_x = sqrt(a + b*cos(x))
                f_x_squared = a + b*cos(x)
                nguyen_ham = a*x + b*sin(x)

                # Tính toán kết quả đúng: V = pi * [ax + b*sinx] từ 0 đến pi/2
                # V = pi * (a*pi/2 + b*1) = (a*pi^2)/2 + b*pi
                ket_qua_bieu_thuc = pi * (a * pi / 2 + b)
                da_dung = '$%s$' % latex(ket_qua_bieu_thuc)

                # B4: Tạo các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai_options = [
                        pi * (a * pi + b),           # Sai hệ số pi/2
                        a * pi / 2 + b,              # Thiếu pi ngoài cùng
                        pi * (a * pi / 2 - b),       # Sai dấu
                        pi * (b * pi / 2 + a),       # Đổi chỗ a và b
                        pi**2 * (a + b),             # Công thức sai hoàn toàn
                        pi * (a * pi / 4 + b)        # Sai cận
                    ]
                    chosen = latex(random.choice(sai_options))
                    if chosen != latex(ket_qua_bieu_thuc):
                        s.add('$%s$' % chosen)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                noidungcauhoi = (r'''Cho hình phẳng $D$ giới hạn bởi đường cong $y = \sqrt{%s + %s \cos x}$, trục hoành và các đường thẳng $x = 0, x = \frac{\pi}{2}$. Tính thể tích khối tròn xoay tạo thành khi $D$ quay quanh trục hoành.'''
                                 % (latex(a), ('' if b == 1 else latex(b))))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết lại y hệt cấu trúc lời giải trong ảnh)
                # dx được thay bằng \text{d}x theo yêu cầu
                loigiai = (r'''Thể tích khối tròn xoay được tính theo công thức: \\
                             $V = \pi \int_{0}^{\frac{\pi}{2}} \left( \sqrt{%s + %s \cos x} \right)^2 \text{d}x = \pi \int_{0}^{\frac{\pi}{2}} (%s + %s \cos x) \text{d}x$ \\
                             $= \pi (%s + %s \sin x) \Big|_{0}^{\frac{\pi}{2}} = %s$.'''
                           % (latex(a), ('' if b == 1 else latex(b)), 
                              latex(a), ('' if b == 1 else latex(b)),
                              latex(a*x), ('' if b == 1 else latex(b)),
                              latex(ket_qua_bieu_thuc)
                             ))

            # Xuất câu trắc nghiệm theo mẫu content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

