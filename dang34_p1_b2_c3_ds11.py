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


def bt_dang34_p1_b2_c3_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Khởi tạo độ rộng khoảng ngẫu nhiên (ví dụ 10, 15, 20)
        step = random.choice([10, 15, 20])

        # Tạo 5 khoảng liên tiếp bắt đầu từ 0
        intervals = []
        for i in range(5):
            intervals.append(f"[{i*step};{(i+1)*step})")

        # Tạo số lượng học sinh ngẫu nhiên cho 5 nhóm
        # Để đảm bảo Q1 rơi vào nhóm thích hợp (nhóm 2 hoặc 3), ta điều chỉnh phân phối
        c1 = random.randint(3, 8)
        c2 = random.randint(7, 12)
        c3 = random.randint(10, 15)
        c4 = random.randint(8, 12)
        c5 = random.randint(4, 8)

        parts = [c1, c2, c3, c4, c5]
        n = sum(parts)

        # Tìm tứ phân vị thứ nhất (Q1)
        # Vì n có thể chẵn hoặc lẻ, ta tính vị trí phần tử Q1
        # Dãy gồm n phần tử, nửa đầu có n_half phần tử
        n_half = n // 2

        # Q1 là trung vị của nửa đầu
        # Vị trí của Q1 trong dãy đã sắp xếp
        if n_half % 2 == 0:
            # Nếu nửa đầu chẵn, Q1 là trung bình cộng của 2 phần tử ở giữa
            q1_pos_str = f"\\frac{{x_{{{n_half // 2}}} + x_{{{n_half // 2 + 1}}}}}{{2}}"
            target_pos = n_half / 2
        else:
            # Nếu nửa đầu lẻ, Q1 là phần tử ở chính giữa
            q1_pos_idx = (n_half + 1) // 2
            q1_pos_str = f"x_{{{q1_pos_idx}}}"
            target_pos = q1_pos_idx

        # Tìm nhóm chứa phần tử thứ target_pos
        cf = 0
        q1_group_index = -1

        for i, count in enumerate(parts):
            cf += count
            if cf >= target_pos:
                q1_group_index = i
                break

        # Nội dung câu hỏi
        noidungcauhoi = ('''Khảo sát thời gian tập thể dục trong ngày của một số học sinh khối 11 thu được mẫu số liệu ghép nhóm sau:
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|c|}
        \\hline
        Thời gian (phút) & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        Số học sinh & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        Nhóm chứa tứ phân vị thứ nhất là'''
                         %(intervals[0], intervals[1], intervals[2], intervals[3], intervals[4],
                           latex(c1), latex(c2), latex(c3), latex(c4), latex(c5)
                         ))

        # Đáp án đúng
        kq_dung = intervals[q1_group_index]
        da = f"${kq_dung}$"

        # Tạo đáp án sai bằng cách lấy các khoảng khác
        sai_intervals = intervals.copy()
        sai_intervals.pop(q1_group_index)

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
        # Chuỗi tổng n
        sum_str = " + ".join([str(c) for c in parts])

        loigiai=('''Ta có cỡ mẫu là $n = %s = %s$.\\\\
        Gọi $x_1, x_2, \\dots, x_{%s}$ là thời gian tập thể dục trong ngày của $%s$ học sinh khối 11 và giả sử dãy này đã sắp xếp theo thứ tự tăng dần.\\\\
        Khi đó tứ phân vị thứ nhất $Q_1$ là trung vị của dãy gồm $%s$ số liệu đầu nên $Q_1 = %s$. Do phần tử này thuộc nhóm $%s$ nên nhóm này chứa $Q_1$.'''
                 %(sum_str, latex(n), latex(n), latex(n), latex(n_half), q1_pos_str, kq_dung
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

