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


def bt_dang27_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bài toán biến đổi sin^6(x) + cos^6(x) = a + b*sin^2(2x)
                # Ta có a = 1, b = -3/4
                val_a = Rational(1, 1)
                val_b = Rational(-3, 4)

                # Chọn ngẫu nhiên hệ số cho biểu thức T = k1*a + k2*b
                # Để ra kết quả đẹp, chọn k2 là bội của 4
                k1 = random.randint(2, 5)
                k2 = random.choice([4, 8, 12])

                val_T = k1 * val_a + k2 * val_b

                # Đáp án đúng
                da = '$T = %s$' % (latex(val_T))

                # Các đáp án sai ngẫu nhiên không trùng với đáp án đúng
                s = [
                    '$T = %s$' % (latex(k1 * val_a - k2 * val_b)),
                    '$T = %s$' % (latex(k1 + k2)),
                    '$T = %s$' % (latex(-k1)),
                    '$T = %s$' % (latex(val_T + 2)),
                    '$T = %s$' % (latex(val_T - 5)),
                    '$T = 1$'
                ]
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Biết rằng $\\sin^6 x + \\cos^6 x = a + b \\sin^2 2x$, với $a,b$ là các số thực. Tính $T = %sa + %sb$.'''
                                 % (latex(k1), latex(k2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết bám sát cấu trúc ảnh gốc
                loigiai = ('''Ta có $\\sin^6 x + \\cos^6 x = \\left(\\sin^2 x + \\cos^2 x\\right)^3 - 3 \\sin^2 x \\cos^2 x \\left(\\sin^2 x + \\cos^2 x\\right)$ \\\\
            = $1 - 3 \\sin^2 x \\cos^2 x = 1 - \\frac{3}{4} \\sin^2 2x$. \\\\
            Vậy $a = 1, b = -\\frac{3}{4}$. Do đó $T = %s \\cdot 1 + %s \\cdot \\left(-\\frac{3}{4}\\right) = %s$.'''
                           % (latex(k1), latex(k2), latex(val_T)))

            elif dang == '2':
                # Bài toán biến đổi sin^4(x) + cos^4(x) = a + b*sin^2(2x)
                # Ta có a = 1, b = -1/2
                val_a = Rational(1, 1)
                val_b = Rational(-1, 2)

                # Chọn ngẫu nhiên hệ số cho biểu thức T = k1*a + k2*b
                # Để ra kết quả đẹp, chọn k2 là bội của 2
                k1 = random.randint(2, 5)
                k2 = random.choice([2, 4, 6, 8])

                val_T = k1 * val_a + k2 * val_b

                # Đáp án đúng
                da = '$T = %s$' % (latex(val_T))

                # Các đáp án sai ngẫu nhiên không trùng với đáp án đúng
                s = [
                    '$T = %s$' % (latex(k1 * val_a - k2 * val_b)),
                    '$T = %s$' % (latex(k1 + k2)),
                    '$T = %s$' % (latex(-k1)),
                    '$T = %s$' % (latex(val_T + 3)),
                    '$T = %s$' % (latex(val_T - 4)),
                    '$T = 0$'
                ]
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Biết rằng $\\sin^4 x + \\cos^4 x = a + b \\sin^2 2x$, với $a,b$ là các số thực. Tính $T = %sa + %sb$.'''
                                 % (latex(k1), latex(k2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết bám sát cấu trúc ảnh gốc
                loigiai = ('''Ta có $\\sin^4 x + \\cos^4 x = \\left(\\sin^2 x + \\cos^2 x\\right)^2 - 2 \\sin^2 x \\cos^2 x$ \\\\
            = $1 - 2 \\sin^2 x \\cos^2 x = 1 - \\frac{1}{2} \\sin^2 2x$. \\\\
            Vậy $a = 1, b = -\\frac{1}{2}$. Do đó $T = %s \\cdot 1 + %s \\cdot \\left(-\\frac{1}{2}\\right) = %s$.'''
                           % (latex(k1), latex(k2), latex(val_T)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

