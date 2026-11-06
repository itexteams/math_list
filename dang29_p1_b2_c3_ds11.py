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


def bt_dang29_p1_b2_c3_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Khởi tạo cấu trúc nhóm
                start_val = 10
                step = 10
                num_groups = 6

                # Sinh ngẫu nhiên tổng số học sinh n (số chẵn)
                n = randint(20, 35) * 2  # n chạy từ 40 đến 50
                pos = n // 2             # Vị trí n/2

                # Vòng lặp đảm bảo 2 giá trị trung vị (vị trí pos và pos+1) cùng thuộc 1 nhóm
                while True:
                    frequencies = [0] * num_groups
                    remaining = n
                    for i in range(num_groups - 1):
                        max_alloc = min(remaining - (num_groups - 1 - i) * 2, int(n * 0.4))
                        frequencies[i] = randint(3, max(4, max_alloc))
                        remaining -= frequencies[i]
                    frequencies[-1] = remaining

                    # Kiểm tra để tránh vị trí ranh giới giữa 2 nhóm
                    cf = 0
                    has_exact_half = False
                    for f in frequencies:
                        cf += f
                        if cf == pos:
                            has_exact_half = True
                            break

                    if not has_exact_half:
                        break

                # 2. Xác định nhóm chứa trung vị
                cf = 0        
                median_group_idx = 0
                for i in range(num_groups):
                    cf += frequencies[i]
                    if cf >= pos and median_group_idx == 0:
                        median_group_idx = i

                # 3. Tạo danh sách chuỗi các nhóm
                groups_str = []
                for i in range(num_groups):
                    low = start_val + i * step
                    high = low + step
                    groups_str.append(f"[{low};{high})")

                table_header = " & ".join([f"\\text{{{g}}}" for g in groups_str])
                table_freq = " & ".join([str(f) for f in frequencies])

                # Đáp án đúng
                da = f"${groups_str[median_group_idx]}$"

                # Các đáp án sai
                wrong_options = []
                for i in range(num_groups):
                    if i != median_group_idx:
                        wrong_options.append(f"${groups_str[i]}$")

                s = random.sample(wrong_options, 3)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = (
                    f"Khảo sát thời gian (đơn vị: phút) học trực tuyến trong một ngày của ${n}$ học sinh, "
                    f"người ta thu được mẫu số liệu ghép nhóm như sau:\n"
                    f"\\begin{{center}}\n"
                    f"\\begin{{tabular}}{{|l|c|c|c|c|c|c|}}\n"
                    f"\\hline\n"
                    f"Thời gian học trực tuyến & {table_header} \\\\\n"
                    f"\\hline\n"
                    f"Số học sinh & {table_freq} \\\\\n"
                    f"\\hline\n"
                    f"\\end{{tabular}}\n"
                    f"\\end{{center}}\n"
                    f"Trung vị của mẫu số liệu trên thuộc nhóm nào sau đây?"
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lập luận lời giải SIÊU ĐƠN GIẢN (Cộng dồn trực tiếp, không dùng từ "tần số tích lũy")
                text_dem_buoc = ""
                tong_cong = 0
                for i in range(median_group_idx + 1):
                    if i == 0:
                        text_dem_buoc += f"Nhóm {groups_str[i]} có {frequencies[0]} học sinh."
                        tong_cong = frequencies[0]
                    else:
                        text_dem_buoc += f"\\\\ \nCộng tiếp nhóm {groups_str[i]}: tổng số học sinh là ${tong_cong} + {frequencies[i]} = {tong_cong + frequencies[i]}$."
                        tong_cong += frequencies[i]

                loigiai = (
                    f"Tổng số học sinh là $n = {n}$. Do $n$ là số chẵn nên trung vị sẽ là trung bình cộng của hai giá trị ở vị trí thứ ${pos}$ và thứ ${pos+1}$.\\\\ \n"
                    f"Ta đếm số lượng học sinh từ nhóm đầu tiên trở đi:\\\\ \n"
                    f"{text_dem_buoc}\\\\ \n"
                    f"Nhận thấy đến nhóm {groups_str[median_group_idx]} thì tổng số học sinh đếm được đạt đến ${tong_cong}$, đã bao gồm cả hai vị trí thứ ${pos}$ và ${pos+1}$.\\\\ \n"
                    f"Do đó, hai giá trị trung tâm này đều nằm trọn trong nhóm {da}.\\\\ \n"
                    f"Vậy nhóm chứa trung vị là nhóm {da}."
                )

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

