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


def bt_dang29_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tập các điểm số từ 0 đến 10
                scores = list(range(11))

                # Sinh tần số ngẫu nhiên dạng phân phối chuẩn (hình chuông) cho thực tế
                freqs = [
                    random.randint(0, 3),   # Điểm 0
                    random.randint(0, 5),   # Điểm 1
                    random.randint(2, 8),   # Điểm 2
                    random.randint(4, 12),  # Điểm 3
                    random.randint(8, 20),  # Điểm 4
                    random.randint(15, 30), # Điểm 5
                    random.randint(15, 30), # Điểm 6
                    random.randint(15, 30), # Điểm 7
                    random.randint(8, 20),  # Điểm 8
                    random.randint(2, 12),  # Điểm 9
                    random.randint(0, 4)    # Điểm 10
                ]

                # Đảm bảo luôn có 1 mốt duy nhất (không bị trùng tần số cao nhất)
                max_freq = max(freqs)
                if freqs.count(max_freq) > 1:
                    # Nếu có nhiều điểm cùng tần số cao nhất, cộng thêm 1 vào một điểm ngẫu nhiên trong số đó
                    idx_to_boost = freqs.index(max_freq)
                    freqs[idx_to_boost] += random.randint(1, 3)
                    max_freq = freqs[idx_to_boost]

                # Tính tổng số học sinh N
                N = sum(freqs)

                # Xác định Mốt (M0)
                mode_score = scores[freqs.index(max_freq)]

                # --- TẠO BẢNG LATEX ---
                row_diem = " & ".join(map(str, scores))
                row_tanso = " & ".join(map(str, freqs))

                table_latex = (
                    "\\begin{center}\n"
                    "\\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}\n"
                    "\\hline\n"
                    f"Điểm & {row_diem} & \\\\\n"
                    "\\hline\n"
                    f"Tần số & {row_tanso} & $N={N}$ \\\\\n"
                    "\\hline\n"
                    "\\end{tabular}\n"
                    "\\end{center}"
                )

                # --- ĐÁP ÁN ĐÚNG ---
                da_str = str(mode_score)

                # --- TẠO CÁC ĐÁP ÁN NHIỄU ---
                options = set()
                while len(options) < 3:
                    # Nhiễu là các điểm số lân cận hoặc các điểm số khác trong thang điểm 10
                    fake_mode = random.choice([4, 5, 6, 7, 8, 9])
                    if fake_mode != mode_score:
                        options.add(str(fake_mode))

                options_list = list(options)
                random.shuffle(options_list)

                das1 = options_list[0]
                das2 = options_list[1]
                das3 = options_list[2]

                # Câu hỏi
                noidungcauhoi = (f"Để khảo sát kết quả thi tuyển sinh môn Toán trong kì thi tuyển sinh đại học năm vừa qua "
                                 f"của trường A, người điều tra chọn một mẫu gồm ${N}$ học sinh tham gia kì thi tuyển sinh đó. "
                                 f"Điểm môn Toán (thang điểm 10) của các học sinh này được cho ở bảng phân bố tần số sau đây:\n"
                                 f"{table_latex}\n"
                                 f"Mốt của mẫu số liệu là")

                # Định dạng đáp án
                da_d = '\\True $' + da_str + '$'
                da_s1 = '$' + das1 + '$'
                da_s2 = '$' + das2 + '$'
                da_s3 = '$' + das3 + '$'

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"Nhìn vào bảng tần số ta thấy giá trị ${mode_score}$ có tần số lớn nhất nên $M_0 = {mode_score}$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

