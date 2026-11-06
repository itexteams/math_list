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


def bt_dang12_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khởi tạo biến ký hiệu
            x = symbols('x')

            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Random các hệ số a, b cho f'(x) = a*cos(x) + b*sin(x)
                # Trong đề mẫu: a=5, b=-1
                a = randint(2, 10)
                b = randint(-10, -1) 
                f_prime = a*cos(x) + b*sin(x)

                # 2. Chọn điểm x0 và giá trị y0: f(x0) = y0
                # Để giống mẫu, ta chọn x0 = pi/2
                x0 = pi/2
                y0 = randint(-5, 5)

                # 3. Tính toán lời giải
                # Nguyên hàm F(x) chưa có C
                F_x = integrate(f_prime, x) 

                # Tính C: F(x0) + C = y0 => C = y0 - F(x0)
                val_at_x0 = F_x.subs(x, x0)
                C_val = y0 - val_at_x0

                # Hàm số cuối cùng
                f_final = F_x + C_val

                # 4. Tạo đáp án đúng và các đáp án sai
                kq_dung = '$f(x) = %s$' % latex(f_final)

                # Tạo danh sách đáp án sai bằng cách thay đổi hằng số C
                s = set()
                while len(s) < 3:
                    sai_C = C_val + randint(-5, 5)
                    if sai_C != C_val:
                        f_sai = F_x + sai_C
                        s.add('$f(x) = %s$' % latex(f_sai))

                list_sai = list(s)

                # 5. Soạn nội dung câu hỏi
                noidungcauhoi = ('Tìm hàm số $f(x)$, biết rằng $f\'(x) = %s$ và $f\\left(\\frac{\\pi}{2}\\right) = %s$' 
                                 % (latex(f_prime), latex(y0)))

                # 6. Soạn nội dung lời giải
                loigiai = ('Ta có $f(x) = \\int f\'(x) \\text{d}x = \\int (%s) dx = %s + C$. \\\\'
                           'Theo giả thiết $f\\left(\\frac{\\pi}{2}\\right) = %s \\Rightarrow %s + C = %s \\Rightarrow C = %s$. \\\\'
                           r'Vậy $f(x) = %s$.'
                           % (latex(f_prime), latex(F_x), 
                              latex(y0), latex(val_at_x0), latex(y0), latex(C_val),
                              latex(f_final)))

                # 7. Sắp xếp đáp án
                da_d = '\\True ' + kq_dung
                list_1 = [da_d, list_sai[0], list_sai[1], list_sai[2]]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

