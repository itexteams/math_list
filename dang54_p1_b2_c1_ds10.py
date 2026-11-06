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


def bt_dang54_p1_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các vùng trong biểu đồ Venn để đảm bảo tính chính xác về mặt toán học
                a3 = randint(1, 2)       # Số ngày có cả 3 yếu tố: mưa, lạnh, gió
                a_rw = randint(2, 4)     # Số ngày chỉ có mưa và gió
                a_rc = randint(2, 4)     # Số ngày chỉ có mưa và lạnh
                a_wc = randint(2, 4)     # Số ngày chỉ có gió và lạnh
                a_r = randint(2, 5)      # Số ngày chỉ có mưa
                a_w = randint(2, 5)      # Số ngày chỉ có gió
                a_c = randint(2, 5)      # Số ngày chỉ có lạnh

                # Tính toán các số liệu đưa vào đề bài
                nM = a_r + a_rw + a_rc + a3     # Tổng số ngày mưa
                nG = a_w + a_rw + a_wc + a3     # Tổng số ngày có gió
                nL = a_c + a_rc + a_wc + a3     # Tổng số ngày lạnh
                nMG = a_rw + a3                 # Số ngày mưa và gió
                nML = a_rc + a3                 # Số ngày mưa và lạnh
                nLG = a_wc + a3                 # Số ngày lạnh và có gió
                nMGL = a3                       # Số ngày mưa, lạnh và có gió

                # Kết quả câu hỏi: Số ngày thời tiết xấu (hợp của cả 3 tập hợp)
                kq = nM + nG + nL - nMG - nML - nLG + nMGL

                # Đáp án trắc nghiệm đúng
                da = '$%s$' % (latex(kq))

                # Tạo danh sách các phương án sai không trùng với đáp án đúng
                s_wrong = []
                # Phương án sai 1: Tổng tất cả các ngày đơn lẻ (quên trừ giao nhau)
                w1 = nM + nG + nL
                if w1 != kq:
                    s_wrong.append(w1)

                # Phương án sai 2: Trừ các giao đôi nhưng quên cộng lại giao ba
                w2 = nM + nG + nL - nMG - nML - nLG
                if w2 != kq and w2 not in s_wrong:
                    s_wrong.append(w2)

                # Bổ sung các phương án sai ngẫu nhiên khác quanh kết quả đúng
                for offset in [2, 3, 5, -2, -3, -4]:
                    w = kq + offset
                    if w > 0 and w != kq and w not in s_wrong:
                        s_wrong.append(w)

                # Chuyển đổi các phương án sai thành định dạng LaTeX
                s = ['$%s$' % (latex(val)) for val in s_wrong[:4]]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Trong một khoảng thời gian nhất định, tại một địa phương, Đài khí tượng thủy văn đã thống kê được:\\\\
            Số ngày mưa: $%s$ ngày; Số ngày có gió: $%s$ ngày; Số ngày lạnh: $%s$ ngày; Số ngày mưa và gió: $%s$ ngày; Số ngày mưa và lạnh: $%s$ ngày; Số ngày lạnh và có gió: $%s$ ngày; Số ngày mưa, lạnh và có gió: $%s$ ngày. Số ngày thời tiết xấu là'''
                                 % (latex(nM), latex(nG), latex(nL), latex(nMG), latex(nML), latex(nLG), latex(nMGL)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $M$, $G$, $L$ lần lượt là tập hợp các ngày mưa, ngày có gió và ngày lạnh.\\\\
            Theo giả thiết của bài toán, ta có các số liệu sau:\\\\
            $|M| = %s$, $|G| = %s$, $|L| = %s$.\\\\
            $|M \\cap G| = %s$, $|M \\cap L| = %s$, $|L \\cap G| = %s$.\\\\
            $|M \\cap G \\cap L| = %s$.\\\\
            Số ngày có thời tiết xấu (ngày có ít nhất một trong ba hiện tượng thời tiết trên) chính là số phần tử của tập hợp $M \\cup G \\cup L$.\\\\
            Áp dụng công thức bao hàm - loại trừ đối với ba tập hợp, ta có:\\\\
            $|M \\cup G \\cup L| = |M| + |G| + |L| - |M \\cap G| - |M \\cap L| - |L \\cap G| + |M \\cap G \\cap L|$\\\\
            Thay các giá trị số vào công thức, ta được:\\\\
            $|M \\cup G \\cup L| = %s + %s + %s - %s - %s - %s + %s = %s$.\\\\
            Vậy có tất cả $%s$ ngày thời tiết xấu.'''
                           % (latex(nM), latex(nG), latex(nL), latex(nMG), latex(nML), latex(nLG), latex(nMGL),
                              latex(nM), latex(nG), latex(nL), latex(nMG), latex(nML), latex(nLG), latex(nMGL), latex(kq), latex(kq)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ \
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

