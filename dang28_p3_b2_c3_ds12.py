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


def bt_dang28_p3_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # I = integrate( (a*x - b*m^2), (x, 0, 1) )
                # I = a/2 - b*m^2
                # Điều kiện: I + c > 0  => a/2 - b*m^2 + c > 0 => b*m^2 < a/2 + c

                a = random.randint(1, 5) * 2 # Chọn a chẵn để a/2 nguyên (giống số 4 trong đề)
                b = random.randint(1, 3)     # Hệ số của m^2
                c = random.randint(2, 10)    # Số thực cộng thêm vào I

                # Tính toán giá trị I theo m
                # I = a/2 - b*m^2
                tuso_i = a // 2

                # Giải bất phương trình: -b*m^2 + (tuso_i + c) > 0
                # m^2 < (tuso_i + c) / b
                limit_sq = (tuso_i + c) / b
                limit = math.sqrt(limit_sq)

                # Tìm các giá trị m nguyên
                m_nguyen = []
                # Quét trong khoảng rộng để tìm m nguyên thỏa mãn m^2 < limit_sq
                for m_val in range(-10, 11):
                    if m_val**2 < limit_sq:
                        m_nguyen.append(m_val)

                # Đáp án đúng
                kq = len(m_nguyen)
                da = '$%s$' % kq

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng và > 0)
                s = set()
                while len(s) < 3:
                    sai = kq + random.choice([-2, -1, 1, 2, 3])
                    if sai > 0 and sai != kq:
                        s.add('$%s$' % sai)

                list_s = list(s)
                das1, das2, das3 = list_s[0], list_s[1], list_s[2]

                # Câu hỏi
                noidungcauhoi = (r'Cho $I = \int_{0}^{1} (%sx - %sm^2) \, \text{d}x$. Có bao nhiêu giá trị nguyên của $m$ để $I + %s > 0$?'
                                 % (latex(a), latex(b), latex(c)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết lại y hệt logic hình ảnh)
                loigiai = (r'''Theo định nghĩa tích phân ta có $I = \int_{0}^{1} (%sx - %sm^2) \, \text{d}x = \left( %sx^2 - %sm^2x \right) \bigg|_0^1 = %s - %sm^2$. \\
                             Khi đó $I + %s > 0 \Leftrightarrow %s - %sm^2 + %s > 0 \Leftrightarrow -%sm^2 + %s > 0 \Leftrightarrow m^2 < %s \Leftrightarrow %s < m < %s$. \\
                             Mà $m$ là số nguyên nên $m \in \{%s\}$. \\
                             Vậy có $%s$ giá trị nguyên của $m$ thỏa mãn yêu cầu.'''
                           % (latex(a), latex(b), latex(Rational(a, 2)), latex(b), latex(tuso_i), latex(b),
                              latex(c), latex(tuso_i), latex(b), latex(c), latex(b), latex(tuso_i + c),
                              latex(Rational(tuso_i + c, b)), 
                              latex(-round(limit, 2)).replace('.',','), latex(round(limit, 2)).replace('.',','),
                              "; ".join(map(str, m_nguyen)), kq
                             ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

