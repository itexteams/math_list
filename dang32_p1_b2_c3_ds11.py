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


def bt_dang32_p1_b2_c3_ds11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Khởi tạo các khoảng tuổi thọ và số lượng ngẫu nhiên
        start_age = random.randint(10, 15)

        # Tạo 5 khoảng liên tiếp
        intervals = []
        for i in range(5):
            intervals.append(f"[{start_age+i};{start_age+i+1})")

        # Tạo số lượng ngẫu nhiên cho từng nhóm sao cho tổng bằng 20 hoặc một số n cụ thể
        n = random.choice([20, 24, 28]) 

        # Chia nhỏ n thành 5 phần
        parts = []
        remaining = n
        for i in range(4):
            # Đảm bảo mỗi nhóm có ít nhất 1 con và không quá nhiều
            max_val = min(remaining - (4 - i), int(n * 0.4)) 
            val = random.randint(1, max_val)
            parts.append(val)
            remaining -= val
        parts.append(remaining)

        c1, c2, c3, c4, c5 = parts

        # Tìm tứ phân vị thứ nhất (Q1)
        # Vị trí Q1 là n/4
        q1_pos = n / 4

        # Tính tần số tích lũy để tìm nhóm chứa Q1
        cf = 0
        q1_group_index = -1
        cf_prev = 0

        for i, count in enumerate(parts):
            cf_prev = cf
            cf += count
            if cf >= q1_pos:
                q1_group_index = i
                break

        # Tạo chuỗi giải thích
        if q1_group_index == 0:
            explain_ineq = f"{q1_pos} \\le {cf}"
        elif q1_group_index == 1:
            explain_ineq = f"{c1} < {q1_pos} \\le {c1} + {c2}"
        elif q1_group_index == 2:
            explain_ineq = f"{c1} + {c2} < {q1_pos} \\le {c1} + {c2} + {c3}"
        elif q1_group_index == 3:
            explain_ineq = f"{c1} + {c2} + {c3} < {q1_pos} \\le {c1} + {c2} + {c3} + {c4}"
        else:
            explain_ineq = f"{c1} + {c2} + {c3} + {c4} < {q1_pos} \\le {c1} + {c2} + {c3} + {c4} + {c5}"


        # Câu hỏi
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
        Nhóm chứa tứ phân vị thứ nhất là'''
                         %(latex(n), 
                           intervals[0], intervals[1], intervals[2], intervals[3], intervals[4],
                           latex(c1), latex(c2), latex(c3), latex(c4), latex(c5)
                         ))

        # Đáp án đúng
        kq_dung = intervals[q1_group_index]
        da = f"${kq_dung}$"

        # Tạo các đáp án sai bằng cách lấy các khoảng khác
        sai_intervals = intervals.copy()
        sai_intervals.pop(q1_group_index)

        # Chọn ngẫu nhiên 3 đáp án sai từ 4 khoảng còn lại
        s = random.sample(sai_intervals, 3)

        das1 = f"${s[0]}$"
        das2 = f"${s[1]}$"
        das3 = f"${s[2]}$"


        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai=('''Ta có: $\\frac{n}{4} = \\frac{%s}{4} = %s$ và $%s$ nên tứ phân vị thứ nhất của mẫu số liệu thuộc nhóm $%s$'''
                 %(latex(n), latex(q1_pos), explain_ineq, kq_dung
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

