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


def bt_dang31_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Cố định số phần tử (12 tháng)
                n = 12

                # Sinh ngẫu nhiên số xe bán được mỗi tháng (ví dụ từ 20 đến 60 xe)
                list_num = [random.randint(20, 60) for _ in range(n)]

                # --- TẠO BẢNG LATEX CHO ĐỀ BÀI ---
                # Dòng 1: Tháng từ 1 đến 12
                row_thang = " & ".join(map(str, range(1, 13)))
                # Dòng 2: Số xe tương ứng
                row_soxe = " & ".join(map(str, list_num))

                table_latex = (
                    "\\begin{center}\n"
                    "\\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}\n"
                    "\\hline\n"
                    f"Tháng & {row_thang} \\\\\n"
                    "\\hline\n"
                    f"Số xe & {row_soxe} \\\\\n"
                    "\\hline\n"
                    "\\end{tabular}\n"
                    "\\end{center}"
                )

                # Sắp xếp mảng số liệu theo thứ tự không giảm
                sorted_num = sorted(list_num)
                sorted_str = "; ".join(map(str, sorted_num))

                # --- TÍNH TOÁN Q1 CHO n=12 ---
                # Nửa dữ liệu bên trái Q2 gồm 6 phần tử đầu tiên
                left_half = sorted_num[:6]
                left_str = "; ".join(map(str, left_half))

                # Q1 là trung bình cộng của 2 phần tử chính giữa nửa trái (vị trí index 2 và 3)
                val1 = left_half[2]
                val2 = left_half[3]
                q1 = (val1 + val2) / 2

                # Định dạng Q1 (đổi dấu . thành ,)
                q1_str = str(int(q1)) if q1.is_integer() else str(q1).replace('.', ',')

                # Đáp án đúng
                da_str = f"{q1_str}"

                # --- TẠO CÁC ĐÁP ÁN NHIỄU ---
                options = set()
                while len(options) < 3:
                    # Nhiễu là các giá trị xung quanh Q1, có thể là số nguyên hoặc có phẩy 5
                    fake_q1 = q1 + random.choice([-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2])
                    if fake_q1 > 0:
                        fake_str = str(int(fake_q1)) if fake_q1.is_integer() else str(fake_q1).replace('.', ',')
                        if fake_str != da_str:
                            options.add(fake_str)

                options_list = list(options)
                random.shuffle(options_list)

                das1 = options_list[0]
                das2 = options_list[1]
                das3 = options_list[2]

                # Câu hỏi
                # Bổ sung năm ngẫu nhiên cho tự nhiên
                nam = random.randint(2020, 2024)
                noidungcauhoi = f"Số xe ô tô của một cửa hàng bán được mỗi tháng trong năm {nam} được ghi lại ở bảng sau: \n{table_latex}\n Tứ phân vị $Q_1$ của bảng số liệu là"

                # Định dạng đáp án
                da_d = '\\True $' + da_str + '$'
                da_s1 = '$' + das1 + '$'
                da_s2 = '$' + das2 + '$'
                da_s3 = '$' + das3 + '$'

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"Sắp xếp số liệu theo thứ tự không giảm ta được: \n"
                           f"$${sorted_str}$$ \n"
                           f"Mẫu số liệu có $n=12$ là số chẵn. Nửa số liệu bên trái $Q_2$ gồm $6$ giá trị: \n"
                           f"${left_str}$\\\\ \n"
                           f"Tứ phân vị $Q_1$ là trung vị của nửa số liệu bên trái. Do đó: \n"
                           f"$$Q_1 = ({val1} + {val2}) : 2 = {q1_str}$$.")

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

