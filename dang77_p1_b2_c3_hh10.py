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


def bt_dang77_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Thiết lập các hệ số cho d2: ax + by + c2 = 0
                # Ở đây d2: 3x - 4y = 0
                a = 3
                b = -4
                c2 = 0

                # Bước 2: Thiết lập d1 song song với d2 bằng cách nhân hệ số k=2
                # d1: 6x - 8y - c1 = 0
                k = 2
                a1 = k * a
                b1 = k * b
                # Ngẫu nhiên số c1 (thường chọn số lẻ để kết quả là số thập phân)
                c1_val = random.choice([101, 103, 107, 109, 113, 121, 131])
                # Trong phương trình d1: a1*x + b1*y + c1 = 0 => 6x - 8y - c1_val = 0
                c1 = -c1_val 

                # Bước 3: Lấy 1 điểm M trên đường thẳng d1
                # Để đơn giản, cho y = 0 => x = -c1 / a1 = c1_val / 6
                xM = Rational(c1_val, a1)
                yM = 0

                # Bước 4: Tính khoảng cách từ M đến d2: 3x - 4y = 0
                # Tử số: |a*xM + b*yM + c2| = |3 * (c1_val/6) - 4*0| = c1_val / 2
                tu_so_val = abs(a * xM + b * yM + c2)
                # Mẫu số: sqrt(a^2 + b^2) = sqrt(3^2 + 4^2) = 5
                mau_so_val = int(math.sqrt(a**2 + b**2))

                kq_numeric = float(tu_so_val / mau_so_val)
                kq_str = str(kq_numeric).replace('.', ',')

                # Các phương án trắc nghiệm
                da_dung = '$' + kq_str + '$'
                s1 = '$' + str(c1_val / 100).replace('.', ',') + '$'
                s2 = '$' + str(c1_val) + '$'
                s3 = '$' + '\\sqrt{' + str(c1_val) + '}' + '$'

                # Câu hỏi
                noidungcauhoi = (
                    'Khoảng cách giữa hai đường thẳng song song '
                    '$d_1 : %sx %sy %s = 0$ và $d_2 : %sx %sy = 0$ bằng'
                    % (latex(a1), latex(b1), latex(c1), latex(a), latex(b))
                )

                # Lời giải chi tiết theo yêu cầu mới
                loigiai = (
                    'Lấy điểm $M\\left( %s; %s \\right)$ thuộc đường thẳng $d_1$. \\\\'
                    'Khoảng cách giữa hai đường thẳng song song $d_1$ và $d_2$ bằng khoảng cách từ điểm $M$ đến đường thẳng $d_2$. \\\\'
                    'Ta có: $d(d_1; d_2) = d(M; d_2) = \\frac{|%s \\cdot %s %s \\cdot %s|}{\\sqrt{(%s)^2 + (%s)^2}} '
                    '= \\frac{|%s - 0|}{%s} = \\frac{%s}{%s} = %s$.'
                    % (latex(xM), latex(yM), 
                       latex(a), latex(xM), latex(b), latex(yM),
                       latex(a), latex(b),
                       latex(tu_so_val), latex(mau_so_val), 
                       latex(tu_so_val), latex(mau_so_val), kq_str)
                )

                # Đưa các đáp án vào danh sách và xáo trộn
                da_d = '\\True ' + da_dung
                list_ans = [da_d, s1, s2, s3]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content 

