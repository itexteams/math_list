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


def bt_dang62_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Ta chọn m_root là nghiệm nguyên để bài toán đẹp (m = 2 hoặc m = -2 trong hình)
                # Ở đây ta sẽ random m_root từ -5 đến 5
                m_root = random.randint(-5, 5)

                # Để có m = ± m_root, ta cần biểu thức m^2 - C = 1 => C = m_root^2 - 1
                c_val = m_root**2 - 1

                # Để m_root thỏa mãn m > -2 (trong hình là m > -k), ta tính toán điều kiện Delta
                # Delta' = (m+1)^2 - (m^2 - c_val) = m^2 + 2m + 1 - m^2 + c_val = 2m + 1 + c_val
                # 2m + 1 + c_val > 0 => m > -(1 + c_val)/2
                limit = -(1 + c_val) / 2

                # Tạo đáp án đúng
                # Trong bài mẫu: m = 2 (chọn giá trị dương)
                kq_val = abs(m_root)
                if kq_val <= limit: # Đảm bảo kq_val thỏa mãn điều kiện Delta
                    kq_val = math.ceil(limit + 1)

                da = '$m = %s$' % latex(kq_val)

                # B4: Điều chỉnh phương án sai không trùng đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    sai = random.randint(-10, 10)
                    option = '$m = %s$' % latex(sai)
                    if sai != kq_val:
                        s_set.add(option)

                list_sai = list(s_set)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                noidungcauhoi = (r'''Tìm giá trị của $m$ để Parabol $(P): y = x^2 - 2(m+1)x + m^2 - %s$ cắt trục hoành tại $2$ điểm phân biệt có hoành độ $x_1, x_2$ sao cho $x_1 \cdot x_2 = 1$.'''
                                 % (latex(c_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết theo ảnh)
                loigiai = (r'''Phương trình hoành độ giao điểm của $(P)$ với trục hoành: $x^2 - 2(m+1)x + m^2 - %s = 0 \quad (1)$. \\
                             Parabol $(P)$ cắt trục hoành tại $2$ điểm phân biệt có hoành độ $x_1, x_2$ sao cho $x_1 \cdot x_2 = 1$ \\
                             $\Leftrightarrow (1)$ có $2$ nghiệm phân biệt $x_1, x_2$ thỏa mãn $x_1 \cdot x_2 = 1$ \\
                             $\Leftrightarrow \begin{cases} \Delta' = (m+1)^2 - (m^2 - %s) > 0 \\ m^2 - %s = 1 \end{cases} 
                             \Leftrightarrow \begin{cases} 2m + %s > 0 \\ m^2 = %s \end{cases} 
                             \Leftrightarrow \begin{cases} m > %s \\ m = \pm %s \end{cases} 
                             \Leftrightarrow m = %s$.'''
                           % (latex(c_val), latex(c_val), latex(c_val), latex(1 + c_val), 
                              latex(1 + c_val), latex(limit), latex(int(math.sqrt(1 + c_val))), latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

