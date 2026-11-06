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


def bt_dang23_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các giá trị số thực
                # Chọn các số n1, n2 ngẫu nhiên để tạo ra số thập phân
                n1 = random.uniform(2, 10)
                n2 = random.uniform(2, 10)

                # Tính toán giá trị số (làm tròn đến hàng phần chục)
                B_val = round(n1, 1)
                h_val = round(n2, 1)

                # Tính thể tích V = B * h
                V_calc = B_val * h_val
                V_final = round(V_calc, 1)

                # Đáp án đúng
                da = '$V = %s$' % str(V_final).replace('.', ',')

                # Bước 4: Điều chỉnh các phương án sai
                s = []
                # Phương án sai 1: Nhầm sang công thức khối chóp (chia 3)
                s1_val = round(V_final / 3, 1)
                s1 = '$V = %s$' % str(s1_val).replace('.', ',')
                if s1 != da: s.append(s1)

                # Phương án sai 2: Nhầm hệ số (nhân 2 hoặc 1.5)
                s2_val = round(V_final * 2, 1)
                s2 = '$V = %s$' % str(s2_val).replace('.', ',')
                if s2 != da: s.append(s2)

                # Phương án sai 3: Nhầm phép tính (cộng thay vì nhân)
                s3_val = round(B_val + h_val, 1)
                s3 = '$V = %s$' % str(s3_val).replace('.', ',')
                if s3 != da: s.append(s3)

                # Phương án sai 4: Giá trị ngẫu nhiên khác
                s4_val = round(V_final - 1.5, 1)
                s4 = '$V = %s$' % str(s4_val).replace('.', ',')
                if s4 != da: s.append(s4)

                # Đảm bảo lấy đủ 3 đáp án sai khác nhau và khác đáp án đúng
                s = list(set(s)) 
                while len(s) < 3: # Phòng trường hợp trùng lặp ngẫu nhiên
                    extra_val = round(V_final + random.uniform(1, 5), 1)
                    s.append('$V = %s$' % str(extra_val).replace('.', ','))
                    s = list(set(s))

                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Chuyển dấu chấm thành dấu phẩy theo chuẩn Việt Nam nếu cần
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
                V_res_str = str(V_final).replace('.', ',')
                loigiai = ('''Thể tích khối lăng trụ được tính theo công thức: $V = B \\cdot h$. \\\\
                              Thay số ta có: $V = %s \\cdot %s = %s$.'''
                           % (B_str, h_str, V_res_str))

                dapan = '\\shortans[0]{$%s$}\n' % (V_res_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

