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


def bt_dang27_p1_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến và thiết lập bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Random các thông số bài toán
                # Giả sử hàm số y = ln(-x^2 + mx + am + b) trên khoảng (alpha, beta)
                alpha = random.randint(0, 2)
                beta = alpha + random.randint(1, 2)
                a = random.randint(1, 4)
                b = random.randint(1, 5)

                # Thiết lập hàm f(x) = x^2 - mx - am - b
                # f(alpha) <= 0 <=> alpha^2 - m*alpha - a*m - b <= 0 
                #              <=> m*(alpha + a) >= alpha^2 - b
                #              <=> m >= (alpha^2 - b) / (alpha + a)

                val1 = Rational(alpha**2 - b, alpha + a)
                val2 = Rational(beta**2 - b, beta + a)

                # Giá trị m cuối cùng là max của 2 giá trị trên
                m_threshold = max(val1, val2)

                # Đáp án đúng
                kq = "m \\ge " + latex(m_threshold)
                da_d = '\\True $' + kq + '$'

                # B4: Điều chỉnh các phương án sai (nhiễu logic)
                # Tránh trùng lặp bằng cách sử dụng set
                s_options = set()

                # Các kiểu nhiễu: đổi dấu bất đẳng thức, dùng nhầm ngưỡng val1 hoặc val2, cộng trừ đơn vị
                wrong_logic = [
                    "m > " + latex(m_threshold),
                    "m \\le " + latex(m_threshold),
                    "m < " + latex(m_threshold),
                    "m \\ge " + latex(min(val1, val2) - 1),
                    "m \\ge " + latex(m_threshold + 1),
                    "m \\le " + latex(m_threshold + Rational(1, 2))
                ]

                for item in wrong_logic:
                    if item != kq:
                        s_options.add('$' + item + '$')

                list_s = list(s_options)
                random.shuffle(list_s)

                da_s1 = list_s[0]
                da_s2 = list_s[1]
                da_s3 = list_s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Giá trị của $m$ để hàm số $y = \ln(-x^2 + mx + %sm + %s)$ xác định với mọi $x \in (%s; %s)$ là'''
                                 % (latex(a), latex(b), latex(alpha), latex(beta)))

                # Nội dung lời giải (B2: Viết lại y hệt cấu trúc mẫu)
                loigiai = (r'''Hàm số xác định với mọi $x \in (%s; %s)$ khi $-x^2 + mx + %sm + %s > 0, \forall x \in (%s; %s)$. \\
                             $\Leftrightarrow f(x) = x^2 - mx - %sm - %s < 0, \forall x \in (%s; %s)$. \\
                             $\Rightarrow f(x) = 0$ có 2 nghiệm thỏa mãn $x_1 \le %s < %s \le x_2$. \\
                             $\Rightarrow \begin{cases} f(%s) \le 0 \\ f(%s) \le 0 \end{cases} 
                             \Leftrightarrow \begin{cases} %s - m(%s) - %sm - %s \le 0 \\ %s - m(%s) - %sm - %s \le 0 \end{cases}$ \\
                             $\Leftrightarrow \begin{cases} m \ge %s \\ m \ge %s \end{cases} \Leftrightarrow m \ge %s$.'''
                           % (latex(alpha), latex(beta), latex(a), latex(b), latex(alpha), latex(beta),
                              latex(a), latex(b), latex(alpha), latex(beta),
                              latex(alpha), latex(beta),
                              latex(alpha), latex(beta),
                              latex(alpha**2), latex(alpha), latex(a), latex(b),
                              latex(beta**2), latex(beta), latex(a), latex(b),
                              latex(val1), latex(val2), latex(m_threshold)
                             ))

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_all = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_all)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_all[0]) + '}\n'
                       '{' + str(list_all[1]) + '}\n'
                       '{' + str(list_all[2]) + '}\n'
                       '{' + str(list_all[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

