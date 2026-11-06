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


def bt_dang17_p4_b1_c5_ds10(self):
            # Khai báo biến
            # B1 & B3: Nghiên cứu đề bài và thiết lập các biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tên các lớp ngẫu nhiên
                ten_lop1 = random.choice(['11A', '11A1', '10A', '11C', '12A'])
                ten_lop2 = random.choice(['12B', '12B2', '12C', '11B', '10B'])
                if ten_lop1 == ten_lop2:
                    ten_lop2 = '12D'

                # Số lượng học sinh ngẫu nhiên
                n1 = randint(20, 45) # Số học sinh lớp 1
                n2 = randint(15, 35) # Số học sinh lớp 2

                # Kết quả đúng theo quy tắc cộng
                kq = n1 + n2

                # B4: Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s = set()
                # Các phương án sai thường gặp: lấy hiệu, lấy tích, hoặc giữ nguyên 1 số
                phuong_an_sai_tiem_nang = [abs(n1 - n2), n1 * n2, n1, n2, kq + 5, kq - 2]

                for val in phuong_an_sai_tiem_nang:
                    if val != kq and val > 0:
                        s.add(val)

                # Chuyển set thành list và lấy 3 phương án
                list_sai = list(s)
                random.shuffle(list_sai)

                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # B2: Viết lại nội dung câu hỏi (sử dụng %s)
                noidungcauhoi = ('''Một trường THPT được cử một học sinh đi dự trại hè toàn quốc. Nhà trường quyết định chọn một học sinh tiên tiến lớp $%s$ hoặc lớp $%s$. Tính số cách chọn, nếu biết rằng lớp $%s$ có $%s$ học sinh tiên tiến và lớp $%s$ có $%s$ học sinh tiên tiến.'''
                                 % (ten_lop1, ten_lop2, ten_lop1, latex(n1), ten_lop2, latex(n2)))

                # Các đáp án
                da_d = ('\\True ' + str(latex(kq)))
                da_s1 = str(latex(das1))
                da_s2 = str(latex(das2))
                da_s3 = str(latex(das3))

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết không viết tắt
                loigiai = ('''Nếu chọn một học sinh lớp $%s$ có $%s$ cách. \\\\
                             Nếu chọn một học sinh lớp $%s$ có $%s$ cách. \\\\
                             Theo quy tắc cộng, ta có $%s + %s = %s$ cách chọn.'''
                           % (ten_lop1, latex(n1), ten_lop2, latex(n2), latex(n1), latex(n2), latex(kq)))

            # Xuất câu trắc nghiệm (B2 - Phần content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

