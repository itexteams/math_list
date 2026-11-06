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


def bt_dang16_p3_b2_c1_ds10(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Khởi tạo các số ngẫu nhiên cho bài toán
        while True:
            # Giá trị cho phép toán trong tập B
            a1 = random.randint(10, 100)
            b1 = random.randint(1, 10)
            b2 = random.randint(1, 10)
            A_end = 5 

            # Các cận của m
            m_start = b1 + b2
            m_end_A = A_end + b1
            m_end_B = Rational(2020 - A_end, a1)

            # Chọn cận trên nhỏ hơn
            if m_end_A < m_end_B:
                kq_end = m_end_A
            else:
                kq_end = m_end_B

            # Tìm giá trị nguyên M lớn nhất thỏa mãn m < kq_end
            kq_end_float = float(kq_end)
            if kq_end_float == int(kq_end_float):
                max_m = int(kq_end_float) - 1
            else:
                max_m = math.floor(kq_end_float)

            # Kiểm tra điều kiện tồn tại ít nhất 1 nghiệm nguyên
            if m_start <= max_m:
                # SỬA LẠI: Biến kq phải là "số lượng" giá trị nguyên thay vì random
                kq = max_m - m_start + 1 
                break

        # Câu hỏi
        noidungcauhoi = ('''Cho hai tập hợp $A=(m-%s; %s]$ và $B=(%s; %s - %sm)$. Có bao nhiêu giá trị nguyên của $m$ để $A \\setminus B = \\emptyset$?'''
                         %(latex(b1), latex(A_end), latex(b2), latex(2020), latex(a1)
                         ))

        # Nội dung lời giải (Đã sửa lại logic hiển thị hệ phương trình và phân số)
        loigiai=('''Để $A$ và $B$ là hai tập hợp khác rỗng thì \\\\
                 $\\heva{& m-%s < %s \\\\& %s < %s - %sm } \\Leftrightarrow \\heva{& m < %s \\\\& m < %s } \\Leftrightarrow m < %s.$ \\\\
                 Để $A \\setminus B = \\emptyset$ thì $A \\subset B$. Ta có điều kiện: \\\\
                 $\\heva{& m-%s \\ge %s \\\\& %s < %s - %sm } \\Leftrightarrow \\heva{& m \\ge %s \\\\& m < %s }$ \\\\
                 Kết hợp các điều kiện, ta có $%s \\le m < %s$. \\\\
                 Vậy có $%s$ giá trị nguyên của $m$ thỏa mãn.'''
                 %(latex(b1), latex(A_end), latex(b2), latex(2020), latex(a1),
                   latex(A_end+b1), latex(Rational(2020-b2, a1)), latex(min(A_end+b1, Rational(2020-b2, a1))),
                   latex(b1), latex(b2), latex(A_end), latex(2020), latex(a1),
                   latex(b1+b2), latex(Rational(2020-A_end, a1)),
                   latex(m_start), latex(kq_end), latex(kq)
                 ))

        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

        # Xuất câu trắc nghiệm
        content = ('\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
            '\\loigiai{ \n'
            +str(loigiai)+'}\n'
            '\\end{ex}\n \\end{minipage} \n\n')
        return content

