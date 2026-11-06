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


def bt_dang10_p2_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Định dạng số phẩy của Việt Nam, đảm bảo luôn có 1 chữ số thập phân
            def format_num(num):
                res = f"{num:.1f}"
                return res.replace('.', ',')

            ######################################################################## Xử lý Data Random ########################

            # Random điểm trung bình mục tiêu
            mu_vals = [7.5, 8.0, 8.5]
            mu = random.choice(mu_vals)
            M = int(mu * 10) # Xử lý trên số nguyên để tránh sai số dấu phẩy động
            max_dev = min(M, 100 - M) # Giới hạn độ lệch để điểm luôn nằm trong [0, 10]

            # Sinh sai số cho bộ dữ liệu có khoảng biến thiên LỚN (học lệch)
            v_shifts = []
            for _ in range(4):
                v = random.randint(8, max_dev)
                v_shifts.extend([v, -v])
            random.shuffle(v_shifts)
            data_wide_int = [M + s for s in v_shifts]

            # Sinh sai số cho bộ dữ liệu có khoảng biến thiên NHỎ (học đều)
            u_shifts = []
            for _ in range(4):
                u = random.randint(1, 4)
                u_shifts.extend([u, -u])
            random.shuffle(u_shifts)
            data_narrow_int = [M + s for s in u_shifts]

            # Tráo ngẫu nhiên bộ dữ liệu cho An và Bình
            if random.choice([True, False]):
                data_A_int = data_wide_int
                data_B_int = data_narrow_int
            else:
                data_A_int = data_narrow_int
                data_B_int = data_wide_int

            # Chuyển về dạng điểm thập phân
            data_A = [x / 10.0 for x in data_A_int]
            data_B = [x / 10.0 for x in data_B_int]

            # Tính khoảng biến thiên
            R_A = (max(data_A_int) - min(data_A_int)) / 10.0
            R_B = (max(data_B_int) - min(data_B_int)) / 10.0

            # Nội dung câu hỏi
            noidungcauhoi = f'''Điểm trung bình môn học kì của hai bạn An và Bình được cho như bảng sau
            \\begin{{center}}
            \\begin{{tabular}}{{|l|c|c|c|c|c|c|c|c|}}
            \\hline
            & Toán & Vật lí & Hóa học & Ngữ văn & Lịch sử & Địa lí & Tin học & Tiếng Anh \\\\
            \\hline
            An & {format_num(data_A[0])} & {format_num(data_A[1])} & {format_num(data_A[2])} & {format_num(data_A[3])} & {format_num(data_A[4])} & {format_num(data_A[5])} & {format_num(data_A[6])} & {format_num(data_A[7])} \\\\
            \\hline
            Bình & {format_num(data_B[0])} & {format_num(data_B[1])} & {format_num(data_B[2])} & {format_num(data_B[3])} & {format_num(data_B[4])} & {format_num(data_B[5])} & {format_num(data_B[6])} & {format_num(data_B[7])} \\\\
            \\hline
            \\end{{tabular}}
            \\end{{center}}'''

            ######################################################################## Nhận biết ############################################

            list_a = [
                f'\\True Điểm trung bình môn học kì của hai bạn đều là {format_num(mu)}',
                f'Điểm trung bình môn học kì của hai bạn đều là {format_num(mu + random.choice([-0.5, 0.5]))}'
            ]
            sol_a = f'Điểm trung bình môn học kì của hai bạn đều là {format_num(mu)}.'

            ######################################################################## Thông hiểu ############################################

            list_b = [
                f'\\True Khoảng biến thiên điểm của bạn An là $R_1 = {format_num(R_A)}$',
                f'Khoảng biến thiên điểm của bạn An là $R_1 = {format_num(R_B)}$' # Bẫy lấy R của Bình
            ]
            sol_b = f'''Đối với bạn An: điểm môn thấp nhất, cao nhất tương ứng là {format_num(min(data_A))}; {format_num(max(data_A))}.\\\\
            Do đó khoảng biến thiên là $R_1 = {format_num(max(data_A))} - {format_num(min(data_A))} = {format_num(R_A)}$.'''

            list_c = [
                f'\\True Khoảng biến thiên điểm của bạn Bình là $R_2 = {format_num(R_B)}$',
                f'Khoảng biến thiên điểm của bạn Bình là $R_2 = {format_num(R_A)}$' # Bẫy lấy R của An
            ]
            sol_c = f'''Đối với bạn Bình: điểm môn thấp nhất, cao nhất tương ứng là {format_num(min(data_B))}; {format_num(max(data_B))}.\\\\
            Do đó khoảng biến thiên là $R_2 = {format_num(max(data_B))} - {format_num(min(data_B))} = {format_num(R_B)}$.'''

            ######################################################################## Vận dụng ############################################

            if R_A < R_B:
                list_d = [
                    '\\True Bạn An học đều hơn bạn Bình',
                    'Bạn Bình học đều hơn bạn An'
                ]
                sol_d = f'Do $R_1 < R_2$ nên ta nói bạn An học đều hơn bạn Bình.'
            else:
                list_d = [
                    'Bạn An học đều hơn bạn Bình',
                    '\\True Bạn Bình học đều hơn bạn An'
                ]
                sol_d = f'Do $R_1 > R_2$ nên ta nói bạn Bình học đều hơn bạn An.'

            ######################################################################## Xáo trộn và in kết quả ###############################

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                da_a = random.choice(list_a)
                da_b = random.choice(list_b)
                da_c = random.choice(list_c)
                da_d = random.choice(list_d)
                answers = [da_a, da_b, da_c, da_d]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
                '{'+str(da_a)+'}\n'
                '{'+str(da_b)+'}\n'
                '{'+str(da_c)+'}\n'
                '{'+str(da_d)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(sol_a)+'\n'
                '\\item '+str(sol_b)+'\n'
                '\\item '+str(sol_c)+'\n'
                '\\item '+str(sol_d)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

