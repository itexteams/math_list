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


def bt_dang21_p4_b1_c5_ds10(self):
            # Khai báo biến
            # q: số cái quần, a: số cái áo, c: số chiếc cà vạt
            q = randint(3, 7)
            a = randint(5, 10)
            c = randint(2, 6)

            # Tính toán kết quả
            kq_dung = q * a * c

            # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
            s_list = []

            # Sai lầm 1: Dùng quy tắc cộng thay vì quy tắc nhân
            sai_cong = q + a + c
            if sai_cong != kq_dung:
                s_list.append(sai_cong)

            # Sai lầm 2: Chỉ nhân 2 loại đồ vật
            sai_nhan_2 = q * a
            if sai_nhan_2 != kq_dung and sai_nhan_2 not in s_list:
                s_list.append(sai_nhan_2)

            # Các phương án ngẫu nhiên khác để đủ 3 phương án sai
            while len(s_list) < 3:
                ngaunhien = kq_dung + random.choice([-5, -2, 2, 5, 10, 12])
                if ngaunhien > 0 and ngaunhien != kq_dung and ngaunhien not in s_list:
                    s_list.append(ngaunhien)

            # Trộn danh sách phương án sai
            random.shuffle(s_list)

            # Các đáp án trắc nghiệm (định dạng Latex, thay dấu . thành , nếu có số thập phân)
            da = '$%s$' % (latex(kq_dung))
            da = da.replace('.', ',')

            das1 = '$%s$' % (latex(s_list[0]))
            das1 = das1.replace('.', ',')

            das2 = '$%s$' % (latex(s_list[1]))
            das2 = das2.replace('.', ',')

            das3 = '$%s$' % (latex(s_list[2]))
            das3 = das3.replace('.', ',')

            # B2: Viết lại đề bài và lời giải theo mẫu (truyền %s)
            noidungcauhoi = ('''Một người có $%s$ cái quần, $%s$ cái áo, $%s$ chiếc cà vạt. Để chọn mỗi thứ một món hãy tính số cách chọn bộ \"quần-áo-cà vạt\" khác nhau.'''
                             % (latex(q), latex(a), latex(c)))

            # Các đáp án để đưa vào danh sách shuffle
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết không viết tắt, sử dụng quy tắc nhân
            loigiai = ('''Để chọn một bộ \"quần-áo-cà vạt\", ta có:\\\\
                         Có $%s$ cách chọn quần.\\\\
                         Có $%s$ cách chọn áo.\\\\
                         Có $%s$ cách chọn cà vạt.\\\\
                         Vậy theo quy tắc nhân ta có $%s \\\\times %s \\\\times %s = %s$ cách.'''
                       % (latex(q), latex(a), latex(c), latex(q), latex(a), latex(c), latex(kq_dung)))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

