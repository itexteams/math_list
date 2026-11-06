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


def bt_dang45_p4_b2_c4_ds10(self):
            # Khai báo biến
            # --- BƯỚC 1 & 2: KHAI BÁO BIẾN VÀ RANDOM ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random giá trị m là đáp án đúng (m > 0 để có GTNN)
                # Ta chọn m sao cho -4m - 2 là một số nguyên để đề bài đẹp
                m_val = random.randint(1, 5) 

                # Tính giá trị nhỏ nhất tương ứng: y_min = -4m - 2
                y_min = -4 * m_val - 2


                kq = m_val
                da = '$m = %s$' % latex(kq)

                # --- BƯỚC 4: TẠO CÁC PHƯƠNG ÁN SAI (KHÔNG TRÙNG ĐÁP ÁN ĐÚNG) ---
                s = []
                while len(s) < 3:
                    sai = random.randint(-5, 10)
                    if sai != kq and sai != 0: # m khác 0 theo điều kiện đề bài
                        val_sai = '$m = %s$' % latex(sai)
                        if val_sai not in s:
                            s.append(val_sai)

                das1, das2, das3 = s

                # --- NỘI DUNG CÂU HỎI ---
                # Biểu thức hàm số: m x^2 - 2m x - (3m + 2)
                noidungcauhoi = (r'''Cho hàm số $y = %sx^2 - %sx - %s$ ($m \neq 0$). Tìm giá trị của $m$ để hàm số có giá trị nhỏ nhất bằng $%s$.'''
                                 % (latex(m_val), latex(2*m_val), latex(3*m_val + 2), latex(y_min)))

                # --- NỘI DUNG LỜI GIẢI (Chi tiết theo ảnh) ---
                loigiai = (r'''Ta có các hệ số $a = m, b = -2m, c = -3m - 2$. \\
                           Tung độ đỉnh của parabol là: \\
                           $y = -\frac{\Delta}{4a} = -\frac{(-2m)^2 - 4 \cdot m \cdot (-3m - 2)}{4m} = \frac{-(4m^2 + 12m^2 + 8m)}{4m} = -4m - 2$. \\
                           Để hàm số có giá trị nhỏ nhất bằng $%s$ thì: \\
                           $\begin{cases} a > 0 \\ -\frac{\Delta}{4a} = %s \end{cases} \Leftrightarrow \begin{cases} m > 0 \\ -4m - 2 = %s \end{cases} \Leftrightarrow \begin{cases} m > 0 \\ -4m = %s \end{cases} \Leftrightarrow m = %s$. \\
                           Vậy $m = %s$ thỏa mãn yêu cầu bài toán.'''
                           % (latex(y_min), latex(y_min), latex(y_min), latex(y_min + 2), latex(kq), latex(kq)))

                # --- XUẤT NỘI DUNG ---
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

