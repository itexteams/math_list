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


def bt_dang21_p1_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            # Hàm hỗ trợ định dạng số
            def format_num(num):
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            if dang=='1':
                # B3: Random các dữ kiện ngữ cảnh
                year_1 = random.randint(2019, 2023)
                year_2 = year_1 + 1
                name = random.choice(["An", "Bình", "Cường", "Dũng", "Hoa", "Mai"])

                # Lượng điện giảm mỗi tháng
                c = random.randint(5, 30)

                # B2: Tạo mẫu số liệu 12 tháng năm thứ 1
                n = 12
                data_1 = [random.randint(120, 250) for _ in range(n)]

                # Xáo trộn số liệu năm 1 để hiện thị lên đề
                random.shuffle(data_1)
                data_1_str_de = " \\hspace{0.3cm} ".join(map(str, data_1))

                # Số liệu năm 1 đã sắp xếp để tính toán
                sorted_1 = sorted(data_1)
                sorted_1_str = " \\hspace{0.3cm} ".join(map(str, sorted_1))

                # Số liệu năm 2 (giảm đi c)
                sorted_2 = [val - c for val in sorted_1]
                sorted_2_str = " \\hspace{0.3cm} ".join(map(str, sorted_2))

                # Các đại lượng năm 1
                # n=12 (chẵn) -> Nửa trái 6 phần tử, nửa phải 6 phần tử
                q2_1_val = (sorted_1[5] + sorted_1[6]) / 2
                q1_1_val = (sorted_1[2] + sorted_1[3]) / 2
                q3_1_val = (sorted_1[8] + sorted_1[9]) / 2
                delta_1 = q3_1_val - q1_1_val

                # Các đại lượng năm 2
                q2_2_val = (sorted_2[5] + sorted_2[6]) / 2
                q1_2_val = (sorted_2[2] + sorted_2[3]) / 2
                q3_2_val = (sorted_2[8] + sorted_2[9]) / 2
                delta_2 = q3_2_val - q1_2_val

                # Các đáp án trắc nghiệm
                du = ['$\\Delta_Q = \\Delta\'_Q$']
                da = random.choice(du)

                # Các đáp án nhiễu theo hằng số giảm c
                s = ['$\\Delta\'_Q = \\Delta_Q - %s$' % c,
                     '$\\Delta_Q = \\Delta\'_Q - %s$' % c,
                     '$\\Delta\'_Q = \\Delta_Q - %s$' % (2 * c),
                     '$\\Delta\'_Q = \\Delta_Q + %s$' % c]

                # Lọc đáp án
                s = list(set(s) - set(du))
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Mẫu số liệu cho biết lượng điện tiêu thụ (đơn vị $kw$) hàng tháng của gia đình bạn %s trong năm %s như sau:
            \\begin{center}
            %s
            \\end{center}
            Trong năm %s nhà bạn %s giảm mức tiêu thụ điện mỗi tháng là $%skw$. Gọi $\\Delta_Q; \\Delta'_Q$ lần lượt là khoảng tứ phân vị của mẫu số liệu tiêu thụ điện năm %s và năm %s. Đẳng thức nào sau đây là đúng?''' 
                                 % (name, year_1, data_1_str_de, year_2, name, c, year_1, year_2))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuẩn bị string nửa trái, nửa phải cho lời giải
                left_1_str = "; ".join(map(str, sorted_1[:6]))
                right_1_str = "; ".join(map(str, sorted_1[6:]))
                left_2_str = "; ".join(map(str, sorted_2[:6]))
                right_2_str = "; ".join(map(str, sorted_2[6:]))

                # Nội dung lời giải
                loigiai = ('''+) Sắp xếp mẫu số liệu năm %s theo thứ tự không giảm:\\\\
            %s\\\\
            Mẫu số liệu gồm 12 giá trị nên số trung vị là $Q_2 = (%s + %s) : 2 = %s$\\\\
            Nửa số liệu bên trái là %s gồm 6 giá trị\\\\
            Khi đó $Q_1 = (%s + %s) : 2 = %s$\\\\
            Nửa số liệu bên phải là %s gồm 6 giá trị\\\\
            Khi đó $Q_3 = (%s + %s) : 2 = %s$\\\\
            Khoảng tứ phân vị của mẫu số liệu bằng: $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$\\\\
            +) Sắp xếp mẫu số liệu năm %s theo thứ tự không giảm:\\\\
            %s\\\\
            Mẫu số liệu gồm 12 giá trị nên số trung vị là $Q'_2 = (%s + %s) : 2 = %s$\\\\
            Nửa số liệu bên trái là %s gồm 6 giá trị\\\\
            Khi đó $Q'_1 = (%s + %s) : 2 = %s$\\\\
            Nửa số liệu bên phải là %s gồm 6 giá trị\\\\
            Khi đó $Q'_3 = (%s + %s) : 2 = %s$\\\\
            Khoảng tứ phân vị của mẫu số liệu bằng: $\\Delta'_Q = Q'_3 - Q'_1 = %s - %s = %s$\\\\
            Vậy $\\Delta_Q = \\Delta'_Q$.'''
                           % (year_1, sorted_1_str, 
                              sorted_1[5], sorted_1[6], format_num(q2_1_val),
                              left_1_str, sorted_1[2], sorted_1[3], format_num(q1_1_val),
                              right_1_str, sorted_1[8], sorted_1[9], format_num(q3_1_val),
                              format_num(q3_1_val), format_num(q1_1_val), format_num(delta_1),
                              year_2, sorted_2_str,
                              sorted_2[5], sorted_2[6], format_num(q2_2_val),
                              left_2_str, sorted_2[2], sorted_2[3], format_num(q1_2_val),
                              right_2_str, sorted_2[8], sorted_2[9], format_num(q3_2_val),
                              format_num(q3_2_val), format_num(q1_2_val), format_num(delta_2)))

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

