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


def bt_dang22_p4_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các góc để tạo ra nhiều câu hỏi khác nhau nhưng vẫn giữ cấu trúc giá trị đẹp
                A = random.choice([30, 150])
                B = random.choice([45, 135])
                C = random.choice([60, 120])

                # Tính toán kết quả chính xác bằng sympy
                val_A = sin(A * pi / 180)
                val_B = cos(B * pi / 180)
                val_C = sin(C * pi / 180)

                correct_val = simplify(sqrt(3) * val_A + val_B - val_C)
                da = latex(correct_val)

                # Hàm bọc ngoặc cho số âm để hiển thị lời giải chuẩn
                def wrap_paren(val_latex):
                    if val_latex.startswith('-'):
                        return '\\left(' + val_latex + '\\right)'
                    return val_latex

                str_val_A = latex(val_A)
                str_val_B = latex(val_B)
                str_val_C = latex(val_C)

                step1_A = wrap_paren(str_val_A)
                step1_B = wrap_paren(str_val_B)
                step1_C = wrap_paren(str_val_C)

                # Tạo danh sách các phương án sai (đảm bảo không trùng với đáp án đúng)
                wrong_vals = [
                    sqrt(2)/2, -sqrt(2)/2, sqrt(2), -sqrt(2), 0, 1, -1, sqrt(3)/2, -sqrt(3)/2, Rational(1,2), Rational(-1,2)
                ]

                s_list = []
                for wv in wrong_vals:
                    if simplify(wv - correct_val) != 0:
                        s_list.append(latex(wv))

                # Loại bỏ các phần tử trùng lặp và trộn ngẫu nhiên
                s_list = list(set(s_list))
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = ('Tính giá trị của biểu thức $P = \\sqrt{3} \\sin %s^\\circ + \\cos %s^\\circ - \\sin %s^\\circ$.'
                                 % (A, B, C))

                # Các đáp án (Không có dấu chấm ở cuối)
                da_d = ('\\True $%s$' % (da))
                da_s1 = ('$%s$' % (das1))
                da_s2 = ('$%s$' % (das2))
                da_s3 = ('$%s$' % (das3))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Ta có $P = \\sqrt{3} \\sin %s^\\circ + \\cos %s^\\circ - \\sin %s^\\circ$. \\\\ \n'
                           '$\\Rightarrow P = \\sqrt{3} \\cdot %s + %s - %s$. \\\\ \n'
                           '$\\Rightarrow P = %s$.' % (
                               A, B, C,
                               step1_A, step1_B, step1_C,
                               da
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

