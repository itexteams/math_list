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


def bt_dang23_p3_b1_c5_ds10(self):
            # Khai báo biến
            # B3: Suy nghĩ tìm cách random bài toán
            # Random số lượng hoa mỗi loại
            n1 = randint(4, 8)  # Số hoa hồng trắng
            n2 = randint(5, 9)  # Số hoa hồng đỏ
            n3 = randint(6, 10) # Số hoa hồng vàng

            # Tính toán đáp án đúng
            kq = n1 * n2 * n3

            # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            # Tạo danh sách các phương án sai tiềm năng
            s_list = [
                n1 + n2 + n3,             # Quy tắc cộng (sai lầm phổ biến)
                (n1 * n2 * n3) - 10,      # Sai số
                (n1 * n2 * n3) + 30,      # Sai số
                n1 * n2 + n3,             # Tính toán sai quy tắc
                (n1 + n2) * n3,           # Tính toán sai quy tắc
                n1 * n2 * n3 // 2         # Chia đôi ngẫu nhiên
            ]

            # Lọc các giá trị trùng với kq và loại bỏ trùng lặp trong s_list
            s_list = list(set([x for x in s_list if x != kq]))
            random.shuffle(s_list)

            # Lấy 3 đáp án sai
            das1 = s_list[0]
            das2 = s_list[1]
            das3 = s_list[2]

            # Câu hỏi
            noidungcauhoi = ('''Một bó hoa có $%s$ hoa hồng trắng, $%s$ hoa hồng đỏ và $%s$ hoa hồng vàng. Số cách chọn lấy ba bông hoa có đủ cả ba màu bằng bao nhiêu?'''
                             %(latex(n1), latex(n2), latex(n3)))

            # Các đáp án
            da_d = ('\\True $%s$' % (latex(kq)))
            da_s1 = ('$%s$' % (latex(das1)))
            da_s2 = ('$%s$' % (latex(das2)))
            da_s3 = ('$%s$' % (latex(das3)))

            # Đưa các đáp án vào danh sách và xáo trộn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # B2: Viết lại lời giải chi tiết theo mẫu
            loigiai = ('''Để chọn ba bông hoa có đủ cả ba màu, ta có:\\\\
                         Có $%s$ cách chọn hoa hồng trắng.\\\\
                         Có $%s$ cách chọn hoa hồng đỏ.\\\\
                         Có $%s$ cách chọn hoa hồng vàng.\\\\
                         Vậy theo quy tắc nhân ta có $%s \\times %s \\times %s = %s$ cách.'''
                       %(latex(n1), latex(n2), latex(n3), latex(n1), latex(n2), latex(n3), latex(kq)))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm (Không dùng raw string r, dùng %s)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

