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


def bt_dang24_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn các giá trị để tính toán (loại bỏ tham số a)
                pairs = [
                    (13.5, 6.2), (12.4, 5.8), (10.2, 7.5), (15.6, 4.3), 
                    (20.5, 3.5), (8.4, 9.2), (11.5, 6.6)
                ]
                # n1 đóng vai trò diện tích đáy B, n2 đóng vai trò chiều cao h
                B_val, h_val = random.choice(pairs)

                # Tính thể tích V = B * h
                V_calc = B_val * h_val
                V_final = round(float(V_calc), 1)

                # Đáp án đúng
                da = '$V = %s$' % str(V_final).replace('.', ',')

                # Bước 4: Điều chỉnh các phương án sai (làm tròn hàng phần chục)
                s = []
                # Phương án sai 1: Nhầm sang công thức khối chóp (chia 3)
                s1 = '$V = %s$' % str(round(V_calc / 3, 1)).replace('.', ',')
                if s1 != da: s.append(s1)

                # Phương án sai 2: Nhầm lẫn phép cộng thay vì phép nhân
                s2 = '$V = %s$' % str(round(B_val + h_val, 1)).replace('.', ',')
                if s2 != da: s.append(s2)

                # Phương án sai 3: Nhầm hệ số (ví dụ nhân đôi)
                s3 = '$V = %s$' % str(round(V_calc * 2, 1)).replace('.', ',')
                if s3 != da: s.append(s3)

                # Phương án sai 4: Nhầm sang hiệu
                s4 = '$V = %s$' % str(round(abs(B_val - h_val), 1)).replace('.', ',')
                if s4 != da: s.append(s4)

                # Đảm bảo lấy đủ 3 đáp án sai khác nhau và khác đáp án đúng
                s = list(set(s)) # Loại bỏ trùng lặp
                if da in s: s.remove(da)
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (Sử dụng số thực, thay dấu . thành dấu , theo chuẩn VN nếu cần)
                B_str = str(B_val).replace('.', ',')
                h_str = str(h_val).replace('.', ',')

                noidungcauhoi = ('''Cho khối lăng trụ có diện tích đáy bằng $%s$, khoảng cách giữa hai đáy của lăng trụ bằng $%s$. Thể tích $V$ của khối lăng trụ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (B_str, h_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Thể tích khối lăng trụ được tính theo công thức: $V = B \\cdot h$. \\\\
                              Thay số ta có: $V = %s \\cdot %s \\approx %s$.'''
                           % (B_str, h_str, str(V_final).replace('.', ',')))

                # Trong mã gốc kqz chưa định nghĩa, tôi giả định kqz là kết quả cuối cùng
                kqz_str = str(V_final).replace('.', ',')
                dapan = '\\shortans[0]{$%s$}\n' % kqz_str
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

