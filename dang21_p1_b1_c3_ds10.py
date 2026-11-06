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


def bt_dang21_p1_b1_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1', '2', '3']
            dang=random.choice(lisdang)

            if dang=='1':
                # Dạng 1: Diện tích hình chữ nhật (Giống ảnh gốc)
                name = random.choice(["Châu", "An", "Bình", "Cường", "Mai"])
                obj = random.choice(["tấm nhôm", "mảnh bìa", "miếng gỗ", "tấm kính"])
                a = random.randint(15, 25)
                b = random.randint(a + 2, 35)
                err = random.choice([0.01, 0.02, 0.05])

                # Tính toán
                S0 = a * b
                delta_S = a * err + b * err + err**2
                length_interval = 2 * delta_S
                kq = round(length_interval, 1) # Làm tròn đến hàng phần chục

                err_str = str(err).replace('.', ',')
                delta_S_str = str(round(delta_S, 4)).replace('.', ',')
                S0_str = str(S0).replace('.', ',')
                kq_str = str(kq).replace('.', ',')

                noidungcauhoi = ('''Trong giờ thực hành hình học, bạn %s đã thực hiện việc đo đạc tính diện tích của một %s hình chữ nhật với hai cạnh đo được lần lượt là $%s \\pm %s \\, \\text{mm}$ và $%s \\pm %s \\, \\text{mm}$. Giá trị đúng của diện tích thuộc đoạn có độ dài bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục).'''
                                 %(name, obj, a, err_str, b, err_str))

                loigiai = ('''Ta biểu diễn chiều rộng và chiều dài của hình chữ nhật là $%s + d_1$ và $%s + d_2$, \\\\
                           Trong đó $-%s \\le d_1 \\le %s; -%s \\le d_2 \\le %s$. \\\\
                           Khi đó, ta có: $(%s + d_1)(%s + d_2) = %s + %s d_2 + %s d_1 + d_1d_2$. \\\\
                           Vì $-%s \\le d_1, d_2 \\le %s$ nên $|%s d_2 + %s d_1 + d_1d_2| \\le %s \\cdot %s + %s \\cdot %s + %s \\cdot %s = %s$. \\\\
                           Vậy giá trị đúng của diện tích thuộc đoạn $[%s - %s; %s + %s]$. \\\\
                           Khi đó độ dài của đoạn này là $%s + %s - (%s - %s) = %s \\approx %s$'''
                           %(a, b, 
                             err_str, err_str, err_str, err_str, 
                             a, b, S0, a, b, 
                             err_str, err_str, a, b, a, err_str, b, err_str, err_str, err_str, delta_S_str,
                             S0, delta_S_str, S0, delta_S_str,
                             S0, delta_S_str, S0, delta_S_str, str(round(length_interval, 4)).replace('.', ','), kq_str))

            elif dang=='2':
                # Dạng 2: Chu vi hình chữ nhật
                name = random.choice(["Hùng", "Lan", "Nga", "Tuấn", "Minh"])
                obj = random.choice(["khu vườn", "sân trường", "mặt bàn", "bức tranh"])
                a = random.randint(15, 25)
                b = random.randint(a + 2, 35)
                err = random.choice([0.01, 0.02, 0.05])

                # Tính toán: P = 2(a+d1 + b+d2) = 2(a+b) + 2(d1+d2)
                P0 = 2 * (a + b)
                delta_P = 2 * (err + err)
                length_interval = 2 * delta_P
                kq = round(length_interval, 1)

                err_str = str(err).replace('.', ',')
                delta_P_str = str(round(delta_P, 4)).replace('.', ',')
                kq_str = str(kq).replace('.', ',')

                noidungcauhoi = ('''Trong giờ thực hành hình học, bạn %s đã thực hiện việc đo đạc tính chu vi của một %s hình chữ nhật với hai cạnh đo được lần lượt là $%s \\pm %s \\, \\text{m}$ và $%s \\pm %s \\, \\text{m}$. Giá trị đúng của chu vi thuộc đoạn có độ dài bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục).'''
                                 %(name, obj, a, err_str, b, err_str))

                loigiai = ('''Ta biểu diễn chiều rộng và chiều dài của hình chữ nhật là $%s + d_1$ và $%s + d_2$, \\\\
                           Trong đó $-%s \\le d_1 \\le %s; -%s \\le d_2 \\le %s$. \\\\
                           Khi đó, chu vi là: $2(%s + d_1 + %s + d_2) = %s + 2(d_1 + d_2)$. \\\\
                           Vì $-%s \\le d_1, d_2 \\le %s$ nên $|2(d_1 + d_2)| \\le 2(%s + %s) = %s$. \\\\
                           Vậy giá trị đúng của chu vi thuộc đoạn $[%s - %s; %s + %s]$. \\\\
                           Khi đó độ dài của đoạn này là $%s + %s - (%s - %s) = %s \\approx %s$'''
                           %(a, b, 
                             err_str, err_str, err_str, err_str, 
                             a, b, P0, 
                             err_str, err_str, err_str, err_str, delta_P_str,
                             P0, delta_P_str, P0, delta_P_str,
                             P0, delta_P_str, P0, delta_P_str, str(round(length_interval, 4)).replace('.', ','), kq_str))

            elif dang=='3':
                # Dạng 3: Diện tích hình vuông
                name = random.choice(["Đức", "Trang", "Phong", "Hương", "Thành"])
                obj = random.choice(["viên gạch", "mặt ghế", "tấm thảm"])
                a = random.randint(20, 40)
                err = random.choice([0.01, 0.02, 0.05])

                # Tính toán: S = (a+d)^2 = a^2 + 2ad + d^2
                S0 = a**2
                delta_S = 2 * a * err + err**2
                length_interval = 2 * delta_S
                kq = round(length_interval, 1)

                err_str = str(err).replace('.', ',')
                delta_S_str = str(round(delta_S, 4)).replace('.', ',')
                kq_str = str(kq).replace('.', ',')

                noidungcauhoi = ('''Trong giờ thực hành hình học, bạn %s đã thực hiện việc đo đạc tính diện tích của một %s hình vuông với cạnh đo được là $%s \\pm %s \\, \\text{cm}$. Giá trị đúng của diện tích thuộc đoạn có độ dài bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục).'''
                                 %(name, obj, a, err_str))

                loigiai = ('''Ta biểu diễn cạnh của hình vuông là $%s + d$, trong đó $-%s \\le d \\le %s$. \\\\
                           Khi đó, diện tích là: $(%s + d)^2 = %s + %s d + d^2$. \\\\
                           Vì $-%s \\le d \\le %s$ nên $|%s d + d^2| \\le %s \\cdot %s + %s^2 = %s$. \\\\
                           Vậy giá trị đúng của diện tích thuộc đoạn $[%s - %s; %s + %s]$. \\\\
                           Khi đó độ dài của đoạn này là $%s + %s - (%s - %s) = %s \\approx %s$'''
                           %(a, err_str, err_str, 
                             a, S0, 2*a, 
                             err_str, err_str, 2*a, 2*a, err_str, err_str, delta_S_str,
                             S0, delta_S_str, S0, delta_S_str,
                             S0, delta_S_str, S0, delta_S_str, str(round(length_interval, 4)).replace('.', ','), kq_str))

            # Tạo đáp án đúng và nhiễu
            du = ['$%s$'%(kq_str)]
            da = random.choice(du)

            s = [
                 '$%s$' % str(round(kq + 0.1, 1)).replace('.', ','),
                 '$%s$' % str(round(kq - 0.1, 1)).replace('.', ','),
                 '$%s$' % str(round(kq / 2.0, 1)).replace('.', ','),  # Quên nhân 2
                 '$%s$' % str(round(kq + 0.2, 1)).replace('.', ',')
                ]

            s = list(set(s))
            if da in s:
                s.remove(da)

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Xử lý hiển thị dấu: + - thành - và - - thành +
            noidungcauhoi = noidungcauhoi.replace('+ -', '-').replace('- -', '+')
            loigiai = loigiai.replace('+ -', '-').replace('- -', '+')

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

