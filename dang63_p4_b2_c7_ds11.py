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


def bt_dang63_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bài toán: y = (x + a) / (x + b*m) đồng biến trên (-inf; c)
                # y' = (b*m - a) / (x + b*m)^2
                # Đồ thị đồng biến và không bị gián đoạn trên khoảng (-inf; c) khi:
                # 1. b*m - a > 0  => m > a/b
                # 2. -b*m >= c    => m <= -c/b

                # Random các tham số để đảm bảo có nghiệm nguyên
                found = False
                while not found:
                    a = random.randint(1, 10)
                    b = random.randint(2, 6)
                    c = random.randint(-20, -5)

                    lower_bound = a / b
                    upper_bound = -c / b

                    # Tìm danh sách các số nguyên m trong (a/b; -c/b]
                    m_values = [m for m in range(math.floor(lower_bound) - 2, math.ceil(upper_bound) + 3) 
                                if m > lower_bound and m <= upper_bound]

                    # Chỉ lấy bài toán nếu có từ 1 đến 5 giá trị nguyên để làm trắc nghiệm đẹp
                    if 1 <= len(m_values) <= 5:
                        found = True

                count_m = len(m_values)

                # Các đáp án trắc nghiệm
                da_dung = str(count_m)

                # Tạo các đáp án nhiễu
                s = set()
                s.add(str(count_m + 1))
                s.add(str(max(0, count_m - 1)))
                if count_m > 2:
                    s.add(str(count_m - 2))
                else:
                    s.add(str(count_m + 2))
                s.add("vô số")

                # Đảm bảo đủ 3 đáp án sai
                list_s = list(s)
                random.shuffle(list_s)
                das1 = list_s[0]
                das2 = list_s[1]
                das3 = list_s[2]

                # Câu hỏi
                noidungcauhoi = (r'Tìm số giá trị nguyên của $m$ để hàm số $y = \frac{x+%s}{x+%sm}$ có đạo hàm dương trên khoảng $(-\infty;%s)$.'
                                 % (latex(a), latex(b), latex(c)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Tập xác định: $D = \mathbb{R} \setminus \{-%sm\}$. \\
                             Ta có $y' = \frac{%sm - %s}{(x + %sm)^2}$. \\
                             Để hàm số có đạo hàm dương trên khoảng $(-\infty; %s)$, điều kiện là: \\
                             $\begin{cases} %sm - %s > 0 \\ -%sm \geq %s \end{cases} \Leftrightarrow \begin{cases} m > \frac{%s}{%s} \\ m \leq \frac{%s}{%s} \end{cases} \Leftrightarrow %s < m \leq %s$. \\
                             Vì $m \in \mathbb{Z} \Rightarrow m \in \{%s\}$. \\
                             Vậy có $%s$ giá trị nguyên của $m$ thỏa mãn yêu cầu bài toán.'''
                           % (latex(b), latex(b), latex(a), latex(b), latex(c),
                              latex(b), latex(a), latex(b), latex(c),
                              latex(a), latex(b), latex(-c), latex(b),
                              latex(Rational(a, b)), latex(Rational(-c, b)),
                              ", ".join(map(str, m_values)), str(count_m)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

