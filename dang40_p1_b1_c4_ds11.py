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


def bt_dang40_p1_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM THAM SỐ ĐỀ BÀI ---
                # Đề bài dạng: n * (sqrt(n^2 + a) - sqrt(n^2 - b))
                # Chọn a và b là số nguyên dương ngẫu nhiên từ 1 đến 9
                a = randint(1, 9) 
                b = randint(1, 9)

                # Tính toán kết quả đúng
                # Tử số sau khi liên hợp: (n^2 + a) - (n^2 - b) = a + b
                tu_so = a + b
                # Giới hạn mẫu số luôn tiến tới sqrt(1) + sqrt(1) = 2
                kq_fraction = Rational(tu_so, 2)

                # --- BƯỚC 2: TẠO ĐÁP ÁN NHIỄU (DISTRACTORS) ---
                kq = latex(kq_fraction) # Đáp án đúng

                # Nhiễu 1: Quên chia cho 2 (chỉ lấy a + b)
                kq_sai1 = latex(tu_so)

                # Nhiễu 2: Sai dấu (lấy a - b) chia 2
                val_sai2 = Rational(abs(a - b), 2)
                kq_sai2 = latex(val_sai2)

                # Nhiễu 3: Một giá trị ngẫu nhiên khác (cộng thêm 1 vào tử số)
                val_sai3 = Rational(tu_so + 1, 2)
                kq_sai3 = latex(val_sai3)

                # Đảm bảo các đáp án không trùng nhau (xử lý trường hợp đặc biệt)
                ds_dap_an = {kq, kq_sai1, kq_sai2, kq_sai3}
                while len(ds_dap_an) < 4:
                    temp_val = Rational(tu_so + randint(2, 10), 2)
                    ds_dap_an.add(latex(temp_val))

                # Chuyển set về list để xử lý hiển thị
                list_da_temp = list(ds_dap_an)
                # Loại bỏ đáp án đúng ra khỏi danh sách nhiễu để chọn
                if kq in list_da_temp: list_da_temp.remove(kq)

                das1 = list_da_temp[0]
                das2 = list_da_temp[1]
                das3 = list_da_temp[2]

                # --- BƯỚC 3: SOẠN THẢO NỘI DUNG ---

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Giới hạn $I = \\lim_{n \\to +\\infty} \\left[ n \\left( \\sqrt{n^2 + %s} - \\sqrt{n^2 - %s} \\right) \\right]$ bằng'
                    % (a, b)
                )

                # Các đáp án
                da_d = ('\\True $' + str(kq) + '$')
                da_s1 = ('$' + str(das1) + '$')
                da_s2 = ('$' + str(das2) + '$')
                da_s3 = ('$' + str(das3) + '$')

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (LaTeX)
                # Xây dựng từng bước giải chi tiết giống hình ảnh
                loigiai = (
                    'Ta có: \\\\'
                    '$I = \\lim_{n \\to +\\infty} \\left[ n \\left( \\sqrt{n^2 + %s} - \\sqrt{n^2 - %s} \\right) \\right] '
                    '= \\lim_{n \\to +\\infty} \\dfrac{n \\left[ (n^2 + %s) - (n^2 - %s) \\right]}{\\sqrt{n^2 + %s} + \\sqrt{n^2 - %s}}$ \\\\'
                    '   $= \\lim_{n \\to +\\infty} \\dfrac{%s n}{\\sqrt{n^2 + %s} + \\sqrt{n^2 - %s}}$ \\\\'
                    '   $= \\lim_{n \\to +\\infty} \\dfrac{%s}{\\sqrt{1 + \\frac{%s}{n^2}} + \\sqrt{1 - \\frac{%s}{n^2}}}$ \\\\'
                    '   $= \\dfrac{%s}{1 + 1} = %s.$'
                    % (
                        a, b,            # Đề bài
                        a, b, a, b,      # Bước nhân liên hợp
                        tu_so, a, b,     # Rút gọn tử số
                        tu_so, a, b,     # Chia n
                        tu_so, kq        # Kết quả cuối
                    )
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

