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


def bt_dang42_p1_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # tong: tổng số học sinh lớp (từ 30 đến 50)
                tong = randint(35, 50)
                # khong_thich: số học sinh không thích môn nào (từ 3 đến 10)
                khong_thich = randint(3, 8)
                # thich_it_nhat_mot: số học sinh thích ít nhất Văn hoặc Toán
                thich_it_nhat_mot = tong - khong_thich

                # van: số học sinh thích Văn
                van = randint(15, thich_it_nhat_mot - 5)
                # toan: số học sinh thích Toán (đảm bảo tổng van + toan > thich_it_nhat_mot để có giao nhau)
                toan = randint(thich_it_nhat_mot - van + 2, thich_it_nhat_mot - 2)

                # Kết quả: số học sinh thích cả hai môn
                kq_val = van + toan - thich_it_nhat_mot
                kq = latex(kq_val)

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                # Tạo danh sách các số gần đáp án đúng để làm nhiễu
                s_nhieu = []
                while len(s_nhieu) < 3:
                    sai = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    if sai > 0 and sai != kq_val and sai not in s_nhieu:
                        s_nhieu.append(sai)

                # Các đáp án trắc nghiệm
                da_d = ('\\True ' + '$%s$ học sinh' % (kq))
                da_s1 = '$%s$ học sinh' % (latex(s_nhieu[0]))
                da_s2 = '$%s$ học sinh' % (latex(s_nhieu[1]))
                da_s3 = '$%s$ học sinh' % (latex(s_nhieu[2]))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Câu hỏi
                noidungcauhoi = ('''Trong lớp 10A có $%s$ học sinh. Trong đó có $%s$ học sinh thích môn Văn, $%s$ em thích môn Toán, $%s$ em không thích môn nào. Số học sinh thích cả hai môn là'''
                                 %(latex(tong), latex(van), latex(toan), latex(khong_thich)))

                # Nội dung lời giải (Viết chi tiết theo từng bước)
                loigiai=('''Gọi $A$ là tập hợp các học sinh thích môn Văn, $B$ là tập hợp các học sinh thích môn Toán. \\\\
                             Số học sinh thích ít nhất một trong hai môn (Văn hoặc Toán) là: \\\\
                             $%s - %s = %s$ học sinh. \\\\
                             Theo công thức số phần tử của hợp hai tập hợp, ta có: \\\\
                             $n\\left(A \\cup B\\right) = n\\left(A\\right) + n\\left(B\\right) - n\\left(A \\cap B\\right)$. \\\\
                             Số học sinh thích cả hai môn Văn và Toán tương ứng với số phần tử của tập hợp $A \\cap B$: \\\\
                             $n\\left(A \\cap B\\right) = n\\left(A\\right) + n\\left(B\\right) - n\\left(A \\cup B\\right) = %s + %s - %s = %s$ học sinh.'''
                         %(latex(tong), latex(khong_thich), latex(thich_it_nhat_mot),
                           latex(van), latex(toan), latex(thich_it_nhat_mot), latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

