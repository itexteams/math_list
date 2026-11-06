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


def bt_dang20_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn k sao cho biểu thức có dạng x^2 - kx + m
                k = randint(1, 5) 
                # Đảm bảo delta < 0 để x^2 - kx + m luôn dương: k^2 - 4m < 0 => m > k^2/4
                m_min = math.floor(k**2 / 4) + 1
                m = randint(m_min, m_min + 5)

                # Biểu thức dưới căn
                f_trong = x**2 - k*x + m
                # Hàm số đầy đủ
                ham_so = sqrt(x + sqrt(f_trong))

                # Đáp án đúng luôn là R theo logic thiết lập
                da_dung = r'$\mathbb{R}$'

                # B4: Điều chỉnh các phương án sai
                s = [
                    r'$[0; +\infty)$',
                    r'$(-\infty; %s]$'%latex(m),
                    r'$\mathbb{R} \setminus \{0\}$',
                    r'$[%s; +\infty)$'%latex(Rational(m, k) if k != 0 else 0),
                    r'$(0; +\infty)$',
                    r'$\varnothing$'
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Tìm tập xác định của hàm số $y = %s$.'''
                                 %(latex(ham_so)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B2: Viết lại lời giải theo mẫu code python
                # Tính toán các bước bổ trợ cho lời giải
                # x^2 - kx + m = (x - k/2)^2 + (m - k^2/4)
                pk2 = Rational(k, 2)
                phan_du = m - Rational(k**2, 4)

                loigiai = ('''Hàm số xác định khi $\\begin{cases} %s \\geq 0 \\\\ x + \\sqrt{%s} \\geq 0 \\end{cases}$ \\\\
                           $\\Leftrightarrow \\begin{cases} \\left( x - %s \\right)^2 + %s \\geq 0 \\\\ \\sqrt{%s} \\geq -x \\end{cases} \\Leftrightarrow \\sqrt{%s} \\geq -x$ (*) \\\\
                           Giải (*): \\\\
                           TH1: $-x < 0 \\Leftrightarrow x > 0$. Khi đó (*) luôn đúng vì $\\sqrt{A} \\geq 0 > B$. \\\\
                           TH2: $-x \\geq 0 \\Leftrightarrow x \\leq 0$. \\\\
                           Khi đó (*) $\\Leftrightarrow %s \\geq (-x)^2 \\Leftrightarrow %s \\geq x^2 \\Leftrightarrow -%sx + %s \\geq 0 \\Leftrightarrow x \\leq %s$. \\\\
                           Kết hợp điều kiện $x \\leq 0$, ta được $x \\leq 0$. \\\\
                           Hợp hai trường hợp ta được $x \\in \\mathbb{R}$. \\\\
                           Vậy tập xác định của hàm số là $D = \\mathbb{R}$.'''
                           %(latex(f_trong), latex(f_trong),
                             latex(pk2), latex(phan_du), latex(f_trong),
                             latex(f_trong),
                             latex(f_trong), latex(f_trong), latex(k), latex(m), latex(Rational(m, k))
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

