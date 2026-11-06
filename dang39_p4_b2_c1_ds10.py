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


def bt_dang39_p4_b2_c1_ds10(self):
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
                    A_end = 5 # Khôi phục lại biến A_end

                    # Kết quả mong muốn
                    # Điều kiện để A, B khác rỗng và A giao B rỗng
                    # m-b1 < A_end -> m < A_end + b1
                    # b2 < 2020 - a1*m -> a1*m < 2020-b2 -> m < (2020-b2)/a1

                    # A \ B = rỗng <=> A con B
                    # m-b1 >= b2 -> m >= b1 + b2
                    # A_end < 2020 - a1*m -> a1*m < 2020 - A_end -> m < (2020 - A_end)/a1

                    # Để bài toán có đáp án nguyên, cần có khoảng giá trị cho m
                    m_start = b1 + b2
                    m_end_A = A_end + b1
                    m_end_B = Rational(2020 - A_end, a1)

                    # Chọn giá trị m_end nhỏ hơn
                    if m_end_A < m_end_B:
                        kq_end = m_end_A
                    else:
                        kq_end = m_end_B

                    # Lấy giá trị nguyên nhỏ nhất từ kq_end
                    if isinstance(kq_end, Rational):
                        kq_end_int = int(kq_end)
                    else:
                        kq_end_int = kq_end

                    # Kiểm tra điều kiện có đáp án
                    if m_start < kq_end_int:
                        # Chọn giá trị ngẫu nhiên trong khoảng đó
                        kq = random.randint(m_start, kq_end_int - 1)
                        break

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(latex(kq))]
                da = random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                      '$%s$'%(latex(kq+2)),
                      '$%s$'%(latex(kq+3)),
                      '$%s$'%(latex(kq-1)),
                      '$%s$'%(latex(kq-2)),
                      '$%s$'%(latex(kq-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho hai tập hợp $A=(m-%s; %s]$ và $B=(%s; %s - %sm)$. Tìm số giá trị nguyên của $m$ để $A \\setminus B = \\emptyset$.'''
                                 %(latex(b1), latex(A_end), latex(b2), latex(2020), latex(a1)
                                 ))
                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Để $A$ và $B$ là hai tập hợp khác rỗng thì \\\\
                         $\\heva{& m-%s < %s \\\\& %s < %s - %sm } \\Leftrightarrow \\heva{& m<%s \\\\& m < %s/%s } \\Leftrightarrow m < %s.$ \\\\
                         Để $A \\setminus B = \\emptyset$ thì $A \\subset B$. Ta có điều kiện: \\\\
                         $\\heva{& m-%s \\ge %s \\\\& %s < %s - %sm } \\Leftrightarrow \\heva{& m \\ge %s \\\\& m < %s/%s } \\Leftrightarrow m \\ge %s.$ \\\\
                         Kết hợp các điều kiện, ta có $%s \\le m < %s$. \\\\
                         Vậy có $%s$ giá trị nguyên của $m$ thỏa mãn.'''
                         %(latex(b1), latex(A_end), latex(b2), latex(2020), latex(a1),
                           latex(A_end+b1), latex(2020-b2), latex(a1), latex(A_end+b1),
                           latex(b1), latex(b2), latex(A_end), latex(2020), latex(a1),
                           latex(b1+b2), latex(2020-A_end), latex(a1), latex(b1+b2),
                           latex(m_start), latex(kq_end_int), latex(kq)
                         ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

