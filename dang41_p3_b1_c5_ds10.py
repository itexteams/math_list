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


def bt_dang41_p3_b1_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn 5 chữ số khác 0 ngẫu nhiên từ 1-9, sau đó thêm số 0
                all_nonzero = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                selected_nonzero = random.sample(all_nonzero, 5)
                digits = [0] + selected_nonzero
                digits.sort() # Sắp xếp để hiển thị đẹp mắt: 0, 1, 2...

                # Chọn một chữ số khác 0 để làm "cặp bài trùng" với số 0
                special_digit = random.choice(selected_nonzero)

                # Chuyển danh sách chữ số thành chuỗi để đưa vào đề bài
                digits_str = ", ".join(map(str, digits))

                # B1 & B2: Tính toán dựa trên logic đề bài
                # Tổng số các số có 6 chữ số khác nhau: 6! - 5! (vì chữ số đầu khác 0)
                total_nums = factorial(6) - factorial(5)

                # Số các số có 0 và special_digit đứng cạnh nhau: 2*5! - 4!
                # Giải thích: Coi (0, special_digit) là 1 khối. Có 2! cách xếp trong khối. 
                # Có 5! cách xếp khối này với 4 số còn lại.
                # Trừ đi trường hợp số 0 đứng đầu: khối là (0, special_digit) và đứng vị trí đầu tiên -> còn 4! cách.
                adj_nums = 2 * factorial(5) - factorial(4)

                # Đáp án đúng: Hiệu của hai giá trị trên
                result = total_nums - adj_nums

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                # Sử dụng các giá trị trung gian làm nhiễu
                da = result

                wrong_options = set()
                # Các nhiễu logic: tổng số, số trường hợp cạnh nhau, hoặc các giá trị ngẫu nhiên hợp lý
                potential_wrongs = [int(total_nums), int(adj_nums), 120, 216, 480, 504, 360]

                for w in potential_wrongs:
                    if w != da:
                        wrong_options.add(w)

                # Nếu chưa đủ 3 đáp án sai, tạo thêm
                while len(wrong_options) < 3:
                    random_wrong = da + random.randint(-50, 50)
                    if random_wrong != da and random_wrong > 0:
                        wrong_options.add(random_wrong)

                selected_wrongs = random.sample(list(wrong_options), 3)

                # Gán vào biến theo mẫu
                da_str = "$%s$" % latex(da)
                das1 = "$%s$" % latex(selected_wrongs[0])
                das2 = "$%s$" % latex(selected_wrongs[1])
                das3 = "$%s$" % latex(selected_wrongs[2])

                # Câu hỏi
                noidungcauhoi = ('''Từ các chữ số $%s$ có thể lập được bao nhiêu số tự nhiên gồm $6$ chữ số đôi một khác nhau trong đó hai chữ số $0$ và $%s$ không đứng cạnh nhau?'''
                                 %(digits_str, latex(special_digit)))

                # Các đáp án
                da_d = ('\\True ' + str(da_str))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết, không viết tắt, sử dụng \left( \right))
                loigiai=('''Số các số có $6$ chữ số được lập từ các chữ số $%s$ là $6! - 5!$. \\\\
                           Số các số có chữ số $0$ và $%s$ đứng cạnh nhau là: $2 \\cdot 5! - 4!$. \\\\
                           Số các số có chữ số $0$ và $%s$ không đứng cạnh nhau là: $6! - 5! - \\left( 2 \\cdot 5! - 4! \\right) = %s$.'''
                         %(digits_str, latex(special_digit), latex(special_digit), latex(da)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(da))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

