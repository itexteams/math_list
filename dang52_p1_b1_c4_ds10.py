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


def bt_dang52_p1_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khởi tạo các giá trị ngẫu nhiên để bài toán luôn có nghiệm đẹp
                # Hàm số có dạng: y = sqrt(x - 2m + k1)/(x - m) + (3x - 1)/sqrt(-x + m + k2)
                # Xác định trên khoảng (p; q)
                k1 = random.randint(2, 4) # Trong ảnh là 3
                k2 = random.randint(4, 6) # Trong ảnh là 5
                p = 0
                q = 1

                # 2. Tính toán các điều kiện biên cho m
                # Điều kiện 1: x >= 2m - k1. Để (p,q) thỏa mãn thì 2m - k1 <= p => m <= (p+k1)/2
                m_max1 = Rational(p + k1, 2)

                # Điều kiện 2: x < m + k2. Để (p,q) thỏa mãn thì m + k2 >= q => m >= q - k2
                m_min = q - k2

                # Điều kiện 3: x != m. Để (p,q) thỏa mãn thì m không thuộc (p, q) => m <= p hoặc m >= q

                # 3. Tổng hợp tập nghiệm đúng
                # m thuộc [m_min, m_max1] AND (m <= p OR m >= q)
                # Kết quả: [m_min, p] U [q, m_max1]

                kq_chuan = r"m \in [%s; %s] \cup \left[ %s; %s \right]" % (latex(m_min), latex(p), latex(q), latex(m_max1))
                da = '$%s$' % kq_chuan

                # 4. Tạo các phương án sai (nhiễu)
                s = [
                    '$m \\in (%s; %s) \\cup (%s; %s)$' % (latex(m_min), latex(p), latex(q), latex(m_max1)),
                    '$m \\in [%s; %s] \\cup [%s; %s]$' % (latex(m_min - 1), latex(p), latex(q), latex(m_max1)),
                    '$m \\in [%s; %s]$' % (latex(m_min), latex(m_max1)),
                    '$m \\in [%s; %s] \\cup [%s; %s]$' % (latex(m_min), latex(p - 1), latex(q + 1), latex(m_max1)),
                    '$m \\in (-\\infty; %s] \\cup [%s; +\\infty)$' % (latex(p), latex(q)),
                ]

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # 5. Nội dung câu hỏi
                noidungcauhoi = (r'''Tất cả các giá trị của tham số $m$ để hàm số $y = \frac{\sqrt{x - 2m + %s}}{x - m} + \frac{3x - 1}{\sqrt{-x + m + %s}}$ xác định trên khoảng $(%s;%s)$ là'''
                                 % (latex(k1), latex(k2), latex(p), latex(q)))

                # 6. Nội dung lời giải (Viết y hệt cấu trúc trong ảnh)
                loigiai = (r'''Điều kiện xác định của hàm số là: $\begin{cases} x - 2m + %s \ge 0 \\ x - m \neq 0 \\ -x + m + %s > 0 \end{cases} \Leftrightarrow \begin{cases} x \ge 2m - %s \\ x \neq m \\ x < m + %s \end{cases}$. \\
            TH1. $2m - %s \ge m + %s \Leftrightarrow m \ge %s \Rightarrow$ tập xác định của hàm số là: $D = \varnothing \Rightarrow m \ge %s$ loại. \\
            TH2. $2m - %s < m + %s \Leftrightarrow m < %s \Rightarrow$ TXĐ của hàm số là: $D = [2m - %s; m + %s) \setminus \{m\}$. \\
            Để hàm số xác định trên khoảng $(%s; %s)$ thì $(%s; %s) \subset D$. \\
            $\Rightarrow \begin{cases} 2m - %s \le %s \\ m + %s \ge %s \\ \left[ \begin{aligned} m \le %s \\ m \ge %s \end{aligned} \right. \end{cases} \Leftrightarrow \begin{cases} m \le %s \\ m \ge %s \\ \left[ \begin{aligned} m \le %s \\ m \ge %s \end{aligned} \right. \end{cases} \Rightarrow \left[ \begin{aligned} %s \le m \le %s \\ %s \le m \le %s \end{aligned} \right.$. \\
            Suy ra $%s$.'''
                           % (latex(k1), latex(k2), latex(k1), latex(k2), 
                              latex(k1), latex(k2), latex(k1+k2), latex(k1+k2),
                              latex(k1), latex(k2), latex(k1+k2), latex(k1), latex(k2),
                              latex(p), latex(q), latex(p), latex(q),
                              latex(k1), latex(p), latex(k2), latex(q), latex(p), latex(q),
                              latex(m_max1), latex(m_min), latex(p), latex(q),
                              latex(m_min), latex(p), latex(q), latex(m_max1),
                              da[1:-1])) # Bỏ dấu $ ở hai đầu da để đưa vào lời giải

                # Đưa các đáp án vào danh sách
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

