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


def bt_dang16_p1_b3_c3_ds10(self):
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
                # Số lượng ngày khảo sát
                n = 10

                # B3: Random 10 giá trị nhiệt độ
                data = [random.randint(20, 40) for _ in range(n)]

                # Xáo trộn mẫu số liệu để tạo đề bài ngẫu nhiên
                random.shuffle(data)
                data_str = " \\hspace{0.5cm} ".join(map(str, data))

                # Sắp xếp số liệu để giải
                sorted_data = sorted(data)
                sorted_data_str = " \\hspace{0.5cm} ".join(map(str, sorted_data))

                # B2: Tính toán Q1, Q2, Q3
                # Mẫu có 10 giá trị:
                # Q2 là trung bình cộng vị trí 5 và 6 (index 4 và 5)
                q2_val = (sorted_data[4] + sorted_data[5]) / 2
                # Nửa trái có 5 giá trị, Q1 là giá trị chính giữa (index 2)
                q1_val = sorted_data[2]
                # Nửa phải có 5 giá trị, Q3 là giá trị chính giữa (index 7)
                q3_val = sorted_data[7]

                kq = q3_val - q1_val

                # Chuẩn hóa định dạng
                q1_str = format_num(q1_val)
                q2_str = format_num(q2_val)
                q3_str = format_num(q3_val)
                kq_str = format_num(kq)

                # Các đáp án trắc nghiệm
                du = ['$\\Delta_Q=%s$'%(kq_str)]
                da = random.choice(du)

                # Sinh các đáp án nhiễu
                s = ['$\\Delta_Q=%s$'%(format_num(kq + 1)),
                     '$\\Delta_Q=%s$'%(format_num(kq - 1)),
                     '$\\Delta_Q=%s$'%(format_num(kq + 2)),
                     '$\\Delta_Q=%s$'%(format_num(kq - 2)),
                     '$\\Delta_Q=%s$'%(format_num(kq + 3)),
                     '$\\Delta_Q=%s$'%(format_num(kq - 3))]

                # Lọc bỏ các đáp án trùng với đáp án đúng
                s = list(set(s) - set(du))
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Có thể đổi tên thành phố ngẫu nhiên để đề đa dạng hơn
                thanhpho = random.choice(["Thanh Hóa", "Nghệ An", "Hà Nội", "Hải Phòng", "Đà Nẵng"])

                noidungcauhoi = ('''Nhiệt độ của thành phố %s ghi nhận trong 10 ngày qua lần lượt là:
            \\begin{center}
            %s
            \\end{center}
            Khoảng tứ phân vị của mẫu số liệu bằng''' 
                                 % (thanhpho, data_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuẩn bị text cho nửa trái, nửa phải
                nua_trai_str = "; ".join(map(str, sorted_data[:5]))
                nua_phai_str = "; ".join(map(str, sorted_data[5:]))

                # Nội dung lời giải
                loigiai = ('''Ta sắp xếp mẫu số liệu theo thứ tự không giảm:\\\\
            %s\\\\
            Mẫu số liệu gồm 10 giá trị nên số trung vị là $Q_2 = (%s + %s) : 2 = %s$\\\\
            Nửa số liệu bên trái là %s gồm 5 giá trị, số chính giữa là $%s$\\\\
            Khi đó $Q_1 = %s$\\\\
            Nửa số liệu bên phải là %s gồm 5 giá trị, số chính giữa là $%s$\\\\
            Khi đó $Q_3 = %s$\\\\
            Khoảng tứ phân vị của mẫu số liệu bằng: $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$'''
                           % (sorted_data_str, 
                              sorted_data[4], sorted_data[5], q2_str,
                              nua_trai_str, q1_str, q1_str,
                              nua_phai_str, q3_str, q3_str,
                              q3_str, q1_str, kq_str))

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

