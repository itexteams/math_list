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


def bt_dang60_p4_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random các giá trị của bài toán
                # Số câu khó (nk), trung bình (ntb), dễ (nd)
                nk = randint(4, 6)
                ntb = randint(8, 12)
                nd = randint(14, 18)
                tong_cau = nk + ntb + nd

                # Tính toán các trường hợp (TH) theo logic đề bài:
                # Chọn 5 câu sao cho đủ 3 loại và số câu dễ >= 2
                # TH1: 2 dễ, 2 trung bình, 1 khó
                c1_d = binomial(nd, 2)
                c1_tb = binomial(ntb, 2)
                c1_k = binomial(nk, 1)
                kq_th1 = c1_d * c1_tb * c1_k

                # TH2: 2 dễ, 1 trung bình, 2 khó
                c2_d = binomial(nd, 2)
                c2_tb = binomial(ntb, 1)
                c2_k = binomial(nk, 2)
                kq_th2 = c2_d * c2_tb * c2_k

                # TH3: 3 dễ, 1 trung bình, 1 khó
                c3_d = binomial(nd, 3)
                c3_tb = binomial(ntb, 1)
                c3_k = binomial(nk, 1)
                kq_th3 = c3_d * c3_tb * c3_k

                # Tổng kết quả
                kq_cuoi = kq_th1 + kq_th2 + kq_th3

                # Đáp án đúng
                da = kq_cuoi

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = kq_cuoi + randint(-10, 10) * 100 + randint(1, 99)
                    if sai != kq_cuoi and sai > 0:
                        s.add(str(sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Thầy A có $%s$ câu hỏi khác nhau gồm $%s$ câu khó, $%s$ câu trung bình và $%s$ câu dễ. Từ $%s$ câu hỏi đó hãy tìm số đề kiểm tra được lập biết mỗi đề gồm $5$ câu hỏi khác nhau, sao cho trong mỗi đề nhất thiết phải có đủ cả $3$ câu và số câu dễ không ít hơn $2$.'''
                                 %(latex(tong_cau), latex(nk), latex(ntb), latex(nd), latex(tong_cau)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Để chọn đề kiểm tra gồm $5$ câu hỏi có đủ $3$ loại và số câu dễ không ít hơn $2$, ta có các trường hợp sau: \\\\
                         TH1: Trong $5$ câu có $2$ câu dễ, $2$ câu trung bình và $1$ câu khó, có: $C_{%s}^{2} \\cdot C_{%s}^{2} \\cdot C_{%s}^{1} = %s$ đề. \\\\
                         TH2: Trong $5$ câu có $2$ câu dễ, $1$ câu trung bình và $2$ câu khó, có: $C_{%s}^{2} \\cdot C_{%s}^{1} \\cdot C_{%s}^{2} = %s$ đề. \\\\
                         TH3: Trong $5$ câu có $3$ câu dễ, $1$ câu trung bình và $1$ câu khó, có: $C_{%s}^{3} \\cdot C_{%s}^{1} \\cdot C_{%s}^{1} = %s$ đề. \\\\
                         Vậy tất cả có số đề là: $%s + %s + %s = %s$ đề.'''
                         %(latex(nd), latex(ntb), latex(nk), latex(kq_th1),
                           latex(nd), latex(ntb), latex(nk), latex(kq_th2),
                           latex(nd), latex(ntb), latex(nk), latex(kq_th3),
                           latex(kq_th1), latex(kq_th2), latex(kq_th3), latex(kq_cuoi)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

