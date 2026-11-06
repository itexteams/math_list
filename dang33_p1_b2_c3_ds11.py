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


def bt_dang33_p1_b2_c3_ds11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Khởi tạo độ tuổi bắt đầu ngẫu nhiên
        start_age = random.randint(10, 15)

        # Tạo 5 khoảng liên tiếp
        intervals = []
        for i in range(5):
            intervals.append(f"[{start_age+i};{start_age+i+1})")

        # Tổng số cá thể (n)
        n = random.choice([20, 24, 28, 32, 40]) 

        # Chia ngẫu nhiên n thành 5 nhóm sao cho tổng bằng n
        parts = []
        remaining = n
        for i in range(4):
            # Đảm bảo phân bổ hợp lý, không dồn hết vào 1 nhóm
            max_val = min(remaining - (4 - i), int(n * 0.4)) 
            val = random.randint(1, max_val)
            parts.append(val)
            remaining -= val
        parts.append(remaining)

        c1, c2, c3, c4, c5 = parts

        # Vị trí tứ phân vị thứ 3 (Q3) là 3n/4
        q3_pos = (3 * n) / 4

        # Tính tần số tích lũy để tìm nhóm chứa Q3
        cf = 0
        q3_group_index = -1

        for i, count in enumerate(parts):
            cf += count
            if cf >= q3_pos:
                q3_group_index = i
                break

        # Tạo chuỗi giải thích cho bất đẳng thức
        if q3_group_index == 0:
            explain_ineq = f"{q3_pos} \\le {cf}"
        elif q3_group_index == 1:
            explain_ineq = f"{c1} < {q3_pos} \\le {c1} + {c2}"
        elif q3_group_index == 2:
            explain_ineq = f"{c1} + {c2} < {q3_pos} \\le {c1} + {c2} + {c3}"
        elif q3_group_index == 3:
            explain_ineq = f"{c1} + {c2} + {c3} < {q3_pos} \\le {c1} + {c2} + {c3} + {c4}"
        else:
            explain_ineq = f"{c1} + {c2} + {c3} + {c4} < {q3_pos} \\le {c1} + {c2} + {c3} + {c4} + {c5}"

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một vườn thú ghi lại tuổi thọ (đơn vị: năm) của $%s$ con hổ và thu được kết quả như sau:
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|c|}
        \\hline
        Tuổi thọ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        Số con hổ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        Nhóm chứa tứ phân vị thứ ba là'''
                         %(latex(n), 
                           intervals[0], intervals[1], intervals[2], intervals[3], intervals[4],
                           latex(c1), latex(c2), latex(c3), latex(c4), latex(c5)
                         ))

        # Đáp án đúng
        kq_dung = intervals[q3_group_index]
        da = f"${kq_dung}$"

        # Tạo đáp án sai
        sai_intervals = intervals.copy()
        sai_intervals.pop(q3_group_index)

        s = random.sample(sai_intervals, 3)

        das1 = f"${s[0]}$"
        das2 = f"${s[1]}$"
        das3 = f"${s[2]}$"

        # Gán đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)

        # Lời giải
        if int(q3_pos) == q3_pos:
            q3_pos_str = str(int(q3_pos))
        else:
            q3_pos_str = str(q3_pos)

        loigiai=('''Ta có: $\\frac{3 \\cdot %s}{4} = %s$ và $%s$ nên tứ phân vị thứ ba thuộc nhóm $%s$'''
                 %(latex(n), q3_pos_str, explain_ineq, kq_dung
                 ))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

