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


def bt_dang17_p4_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tham số a để tạo biểu thức (sqrt(x-a^2) +/- a)^2
                # Trong ảnh gốc a = 1
                a = randint(1, 6)
                a2 = a*a
                two_a = 2*a

                # Đáp án đúng là m = 2*a
                kq_val = two_a

                # Các đáp án trắc nghiệm
                da_text = '$m = %s$' % (latex(kq_val))

                # Tạo danh sách các phương án nhiễu (không trùng với đáp án đúng)
                s = [
                    '$m = %s$' % (latex(a)),
                    '$m = %s$' % (latex(a2)),
                    '$m = %s$' % (latex(a + 1)),
                    '$m = 0$',
                    '$m = %s$' % (latex(two_a + 2)),
                    '$m = %s$' % (latex(two_a - 1 if two_a > 1 else 5))
                ]

                # Lọc bỏ nếu lỡ trùng với đáp án đúng
                s = [item for item in s if item != da_text]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Biểu thức: sqrt(x - 2*a*sqrt(x-a2)) + sqrt(x + 2*a*sqrt(x-a2)) = m
                noidungcauhoi = ('''Phương trình $\\sqrt{x - %s\\sqrt{x - %s}} + \\sqrt{x + %s\\sqrt{x - %s}} = m$ có vô số nghiệm. Tìm giá trị của $m$.'''
                                 % (latex(two_a), latex(a2), latex(two_a), latex(a2)))

                # Các đáp án
                da_d = ('\\True ' + str(da_text))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Tập xác định: $x \\ge %s$. \\\\
                             Ta có: \\\\
                             $x - %s\\sqrt{x - %s} = (x - %s) - 2\\sqrt{x - %s} \\cdot %s + %s = (\\sqrt{x - %s} - %s)^2$. \\\\
                             $x + %s\\sqrt{x - %s} = (x - %s) + 2\\sqrt{x - %s} \\cdot %s + %s = (\\sqrt{x - %s} + %s)^2$. \\\\
                             Phương trình đã cho tương đương với: \\\\
                             $\\left| \\sqrt{x - %s} - %s \\right| + \\left| \\sqrt{x - %s} + %s \\right| = m$. \\\\
                             Xét hàm số $f(x) = \\left| \\sqrt{x - %s} - %s \\right| + \\left| \\sqrt{x - %s} + %s \\right|$. \\\\
                             Với $x \\in [%s; %s]$, ta có $0 \\le \\sqrt{x - %s} \\le %s$, khi đó: \\\\
                             $f(x) = %s - \\sqrt{x - %s} + \\sqrt{x - %s} + %s = %s$. \\\\
                             Để phương trình $f(x) = m$ có vô số nghiệm thì $m = %s$.'''
                           % (latex(a2),
                              latex(two_a), latex(a2), latex(a2), latex(a2), latex(a), latex(a2), latex(a2), latex(a),
                              latex(two_a), latex(a2), latex(a2), latex(a2), latex(a), latex(a2), latex(a2), latex(a),
                              latex(a2), latex(a), latex(a2), latex(a),
                              latex(a2), latex(a), latex(a2), latex(a),
                              latex(a2), latex(2*a2), latex(a2), latex(a),
                              latex(a), latex(a2), latex(a2), latex(a), latex(two_a),
                              latex(two_a)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

