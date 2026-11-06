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


def bt_dang33_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo danh sách dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                A = random.randint(5, 15)  
                k = random.choice([0.1, 0.2, 0.3, 0.4, 0.5]) 
                B = random.randint(2, 10)  
                T = random.randint(5, 15)  

                # Tính toán các giá trị trung gian
                he_so = A / k
                he_so_hien_thi = int(he_so) if he_so == int(he_so) else round(he_so, 2)
                C = B - he_so
                C_round = round(C, 2)

                # Tính kết quả cuối cùng
                ket_qua_chua_tron = he_so * math.exp(k * T) + C
                kq_tron = int(Decimal(ket_qua_chua_tron).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # --- Chuyển đổi dấu chấm thành dấu phẩy cho hiển thị ---
                k_str = str(k).replace('.', ',')
                he_so_str = str(he_so_hien_thi).replace('.', ',')
                # Xử lý riêng cho C để đẹp về dấu
                dau_C = '+' if C_round >= 0 else '-'
                C_abs_str = str(abs(C_round)).replace('.', ',')
                C_full_str = f"{dau_C} {C_abs_str}"

                # --- B4: Điều chỉnh các phương án sai ---
                da_dung = f"${kq_tron}$"
                s = set()
                while len(s) < 3:
                    nhieu = kq_tron + random.choice([-20, -10, 5, 10, 15, 20, 35, 50])
                    if nhieu != kq_tron and nhieu > 0:
                        s.add(f"${nhieu}$")

                list_sai = list(s)

                # --- B2: Viết lại nội dung bài toán ---
                noidungcauhoi = (
                    f"Trong một dịch cúm, tốc độ tăng số trường hợp mắc bệnh của một thành phố được ước lượng bởi "
                    f"$N'(t) = {A} \\cdot e^{{{k_str}t}}$ (trường hợp/ngày) trong đó $N(t)$ là số trường hợp mắc bệnh sau thời gian $t$ ngày kể từ khi bắt đầu dịch. "
                    f"Biết rằng thời điểm bắt đầu dịch có ${B}$ trường hợp mắc bệnh. Ước lượng số trường hợp mắc bệnh của thành phố sau ${T}$ ngày dịch bắt đầu bằng bao nhiêu? "
                    f"(làm tròn kết quả đến hàng đơn vị)."
                )

                da_d = '\\True ' + da_dung
                list_1 = [da_d, list_sai[0], list_sai[1], list_sai[2]]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (
                    f"Ta có $N(t) = \\int N'(t) dt = \\int {A} \\cdot e^{{{k_str}t}} dt = \\frac{{{A}}}{{{k_str}}} e^{{{k_str}t}} + C = {he_so_str} \\cdot e^{{{k_str}t}} + C$.\\\\\n"
                    f"Theo giả thiết, $N(0) = {B}$ suy ra ${he_so_str} + C = {B} \\Rightarrow C = {str(C_round).replace('.', ',')}$.\\\\\n"
                    f"Vậy $N(t) = {he_so_str} \\cdot e^{{{k_str}t}} {C_full_str}$.\\\\\n"
                    f"Số trường hợp mắc bệnh sau ${T}$ ngày là:\\\\\n"
                    f"$N({T}) = {he_so_str} \\cdot e^{{{k_str} \\cdot {T}}} {C_full_str} \\approx {kq_tron}$ (trường hợp)."
                )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_tron))

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

