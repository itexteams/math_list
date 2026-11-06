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


def bt_dang34_p1_b2_c3_ds10(self):
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Cố định số phần tử là 10 (10 địa phương)
                n = 10

                # Sinh ngẫu nhiên 10 điểm trung bình (từ 6.50 đến 8.50)
                list_num = [random.randint(650, 850) / 100 for _ in range(n)]

                # Biểu đồ hiển thị từ cao xuống thấp
                list_num_desc = sorted(list_num, reverse=True)
                # Chuyển đổi trực tiếp bằng List Comprehension
                original_str = " \\quad ".join([str(x).replace('.', ',') for x in list_num_desc])

                # Sắp xếp mảng số liệu theo thứ tự tăng dần
                sorted_num = sorted(list_num)
                sorted_str = " \\quad ".join([str(x).replace('.', ',') for x in sorted_num])

                # --- TÍNH TOÁN CÁC TỨ PHÂN VỊ CHO n=10 ---
                val2_1 = sorted_num[4]
                val2_2 = sorted_num[5]
                q2 = (val2_1 + val2_2) / 2

                left_half = sorted_num[:5]  
                right_half = sorted_num[5:] 

                q1 = left_half[2]
                q3 = right_half[2]

                # Chuỗi đáp án đúng, xử lý dấu phẩy trực tiếp
                da_str = f"Q_1 = {str(q1).replace('.', ',')}, Q_2 = {str(q2).replace('.', ',')}, Q_3 = {str(q3).replace('.', ',')}"

                # --- TẠO CÁC ĐÁP ÁN NHIỄU ---
                options = set()
                while len(options) < 3:
                    # Thêm round(..., 2) để làm tròn 2 chữ số thập phân, tránh sinh ra các số quá dài do lỗi float của Python
                    f_q1_val = round(q1 + random.choice([-0.05, -0.04, -0.02, 0.02, 0.04, 0.05]), 2)
                    f_q2_val = round(q2 + random.choice([-0.05, -0.04, -0.02, 0.02, 0.04, 0.05]), 2)
                    f_q3_val = round(q3 + random.choice([-0.05, -0.04, -0.02, 0.02, 0.04, 0.05]), 2)

                    # Xử lý dấu phẩy cho các phương án nhiễu
                    opt = f"Q_1 = {str(f_q1_val).replace('.', ',')}, Q_2 = {str(f_q2_val).replace('.', ',')}, Q_3 = {str(f_q3_val).replace('.', ',')}"
                    if opt != da_str:
                        options.add(opt)

                options_list = list(options)
                random.shuffle(options_list)

                das1 = options_list[0]
                das2 = options_list[1]
                das3 = options_list[2]

                # Câu hỏi
                nam_thi = random.randint(2023, 2026)
                noidungcauhoi = (f"Trong kỳ thi tốt nghiệp THPT năm {nam_thi}, 10 địa phương có điểm trung bình môn Toán cao nhất cả nước lần lượt là: \n"
                                 f"$${original_str}$$ \n"
                                 f"Tứ phân vị trong mẫu số liệu thống kê trên là")

                # Định dạng các đáp án trắc nghiệm
                da_d = '\\True $' + da_str + '$'
                da_s1 = '$' + das1 + '$'
                da_s2 = '$' + das2 + '$'
                da_s3 = '$' + das3 + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                left_str = " \\quad ".join([str(x).replace('.', ',') for x in left_half])
                right_str = " \\quad ".join([str(x).replace('.', ',') for x in right_half])

                loigiai = (f"Mẫu số liệu trên được sắp xếp theo thứ tự tăng dần như sau:\\\\ \n"
                           f"${sorted_str}$\\\\ \n"
                           f"Số trung vị trong mẫu số liệu trên là $\\frac{{{str(val2_1).replace('.', ',')} + {str(val2_2).replace('.', ',')}}}{{2}} = {str(q2).replace('.', ',')}$.\\\\ \n"
                           f"Trung vị của dãy ${left_str}$ là ${str(q1).replace('.', ',')}$\\\\ \n"
                           f"Trung vị của dãy ${right_str}$ là ${str(q3).replace('.', ',')}$\\\\ \n"
                           f"Vậy ${da_str}$.")

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

