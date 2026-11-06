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


def bt_dang20_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1, B2, B3: Phân tích, viết lại và ngẫu nhiên hóa
                N = 30 # Giữ nguyên cỡ mẫu 30 lớp học để bảng chia 2 dòng x 15 cột đẹp mắt

                # Sinh ngẫu nhiên số học sinh của 30 lớp (ví dụ từ 35 đến 55 học sinh)
                # Sử dụng random.choices để có sự lặp lại (nhiều lớp có cùng sĩ số)
                base_sizes = list(range(35, 53))
                data = sorted(random.choices(base_sizes, k=N))

                # Tách dữ liệu thành 2 dòng để hiển thị bảng
                row1 = data[:15]
                row2 = data[15:]

                # Tính toán vị trí trung vị (N = 30 là số chẵn)
                pos1 = N // 2
                pos2 = N // 2 + 1
                val1 = data[pos1 - 1]
                val2 = data[pos2 - 1]

                Me = (val1 + val2) / 2

                # Xử lý định dạng dấu phẩy và kiểm tra số nguyên (Fix lỗi is_integer)
                if float(Me).is_integer():
                    Me = int(Me)
                    Me_str = str(Me)
                else:
                    Me_str = str(Me).replace('.', ',')

                # Đáp án đúng
                da = f"${Me_str}$"

                # Sinh các đáp án nhiễu
                distractors = set()
                # Ưu tiên lấy luôn 2 giá trị val1 và val2 làm nhiễu nếu chúng khác đáp án đúng
                if str(val1) != Me_str: distractors.add(f"${val1}$")
                if str(val2) != Me_str: distractors.add(f"${val2}$")

                while len(distractors) < 3:
                    delta = random.choice([-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2])
                    fake_Me = Me + delta

                    # Đảm bảo định dạng nhiễu khớp chuẩn
                    if float(fake_Me).is_integer():
                        fake_Me_str = str(int(fake_Me))
                    else:
                        fake_Me_str = str(fake_Me).replace('.', ',')

                    fake_ans = f"${fake_Me_str}$"
                    if fake_ans != da:
                        distractors.add(fake_ans)

                distractors = list(distractors)
                das1 = distractors[0]
                das2 = distractors[1]
                das3 = distractors[2]

                # Tạo bảng LaTeX (2 dòng x 15 cột)
                col_format = "|" + "c|" * 15
                table_str = f"\\begin{{center}}\n\\begin{{tabular}}{{{col_format}}}\n\\hline\n"
                table_str += " & ".join(map(str, row1)) + " \\\\\n\\hline\n"
                table_str += " & ".join(map(str, row2)) + " \\\\\n\\hline\n\\end{tabular}\n\\end{center}"

                # Câu hỏi
                noidungcauhoi = (f"Điều tra số học sinh của ${N}$ lớp học, ta được bảng số liệu như sau:\n"
                                 f"{table_str}\n"
                                 f"Số trung vị của bảng nói trên là")

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                if val1 == val2:
                    loigiai_calc = f"M_e = {Me_str}"
                else:
                    loigiai_calc = f"M_e = \\frac{{{val1} + {val2}}}{{2}} = {Me_str}"

                loigiai = (f"Ta có: $N = {N}$ là số chẵn. Số liệu thứ {pos1} và thứ {pos2} lần lượt là: ${val1}$ và ${val2}$. Vậy số trung vị là:\\\\\n"
                           f"${loigiai_calc}$ (Học sinh).")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

