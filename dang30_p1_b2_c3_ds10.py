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


def bt_dang30_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- TẠO SỐ LIỆU ---
                # Sinh ngẫu nhiên giá trị khối lượng bắt đầu và bước nhảy (ví dụ bắt đầu từ 20-30g, bước nhảy 2-5g)
                start_mass = random.randint(20, 30)
                step = random.choice([2, 5])

                # Tạo danh sách 6 giá trị khối lượng
                masses = [start_mass + i * step for i in range(6)]

                # Tạo danh sách 6 tần số ngẫu nhiên
                freqs = [random.randint(2, 8) for _ in range(6)]

                # Chỉ định một vị trí làm mốt (tránh nằm ở đầu hoặc cuối quá lộ liễu, chọn từ index 1 đến 4)
                mode_idx = random.randint(1, 4)
                # Gán tần số lớn nhất cho vị trí này
                freqs[mode_idx] = random.randint(10, 18)

                # Đảm bảo tần số này là lớn nhất và duy nhất
                max_freq = freqs[mode_idx]
                while freqs.count(max_freq) > 1:
                    freqs[mode_idx] += 1
                    max_freq = freqs[mode_idx]

                mode_val = masses[mode_idx]

                # Tổng số quả trứng (N)
                N = sum(freqs)

                # --- TẠO BẢNG LATEX DỌC ---
                table_rows = ""
                for m, f in zip(masses, freqs):
                    table_rows += f"        {m} & {f} \\\\\n"

                table_latex = (
                    "\\begin{center}\n"
                    "\\begin{tabular}{|c|c|}\n"
                    "\\hline\n"
                    "Khối lượng (g) & Tần số \\\\\n"
                    "\\hline\n"
                    f"{table_rows}"
                    "\\hline\n"
                    f"Cộng & {N} \\\\\n"
                    "\\hline\n"
                    "\\end{tabular}\n"
                    "\\end{center}"
                )

                # --- TẠO ĐÁP ÁN ---
                da_str = str(mode_val)

                options = set()
                # Thêm giá trị tần số lớn nhất vào làm nhiễu (học sinh rất hay nhầm mốt là tần số)
                options.add(str(max_freq))

                # Thêm các khối lượng khác làm nhiễu
                while len(options) < 3:
                    fake_mode = random.choice(masses)
                    if str(fake_mode) != da_str:
                        options.add(str(fake_mode))

                options_list = list(options)
                random.shuffle(options_list)

                das1 = options_list[0]
                das2 = options_list[1]
                das3 = options_list[2]

                # Câu hỏi
                noidungcauhoi = (f"Cho bảng phân bố tần số khối lượng {N} quả trứng gà của một rổ trứng gà:\n"
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

                # Nội dung lời giải (Bám sát ảnh)
                loigiai = (f"Nhìn vào bảng tần số ta thấy giá trị ${mode_val}(g)$ có tần số lớn nhất nên $M_0 = {mode_val}$.")

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

