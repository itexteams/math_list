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


def bt_dang39_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            def fmt(n):
                if n == int(n):
                    return str(int(n))
                return str(round(n, 2)).replace('.', ',')

            if dang=='1':
                # Random 20 giá trị (bội số của 10 từ 0 đến 350)
                data = [random.randint(0, 35) * 10 for _ in range(20)]

                # Chia thành 2 dòng cho bảng
                row1 = " & ".join(map(str, data[:10]))
                row2 = " & ".join(map(str, data[10:]))

                # Sắp xếp để tìm tứ phân vị
                data_sorted = sorted(data)
                str_sorted = " \\quad ".join(map(str, data_sorted))

                # Tính Q2
                q2_1, q2_2 = data_sorted[9], data_sorted[10]
                q2 = (q2_1 + q2_2) / 2

                # Tính Q1 (nửa đầu có 10 phần tử: index 0 đến 9)
                q1_1, q1_2 = data_sorted[4], data_sorted[5]
                q1 = (q1_1 + q1_2) / 2
                str_half_1 = " \\quad ".join(map(str, data_sorted[:10]))

                # Tính Q3 (nửa sau có 10 phần tử: index 10 đến 19)
                q3_1, q3_2 = data_sorted[14], data_sorted[15]
                q3 = (q3_1 + q3_2) / 2
                str_half_2 = " \\quad ".join(map(str, data_sorted[10:]))

                # Tổng các tứ phân vị
                sum_q = q1 + q2 + q3

                # Kết quả đúng
                kq = fmt(sum_q)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các đáp án nhiễu
                s = [
                    '$%s$'%(fmt(sum_q + 5)),
                    '$%s$'%(fmt(sum_q - 5)),
                    '$%s$'%(fmt(sum_q + 10)),
                    '$%s$'%(fmt(sum_q - 10)),
                    '$%s$'%(fmt(sum_q + 15)),
                    '$%s$'%(fmt(sum_q - 15)),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Hàm lượng Natri (đơn vị miligam, $1mg=0,001g$) trong $100g$ một số loại ngũ cốc được cho như sau:
            \\begin{center}
            \\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|}
            \\hline
            %s \\\\
            \\hline
            %s \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Tổng các tứ phân vị bằng'''
                                 %(row1, row2))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Sắp xếp các giá trị này theo thứ tự không giảm: \\\\
            %s \\\\
            Vì cỡ mẫu là $n=20$, là số chẵn, nên giá trị của tứ phân vị thứ hai là 
            $$Q_2 = (%s + %s) : 2 = %s$$
            Tứ phân vị thứ nhất là trung vị của nửa số liệu bên trái $Q_2$: \\\\
            %s \\\\
            Do đó: $Q_1 = (%s + %s) : 2 = %s$. \\\\
            Tứ phân vị thứ ba là trung vị của nửa số liệu bên phải $Q_2$: \\\\
            %s \\\\
            Do đó: $Q_3 = (%s + %s) : 2 = %s$. \\\\
            Khi đó tính tổng các tứ phân vị bằng $ %s + %s + %s = %s $.'''
                           %(str_sorted, q2_1, q2_2, fmt(q2), str_half_1, q1_1, q1_2, fmt(q1), str_half_2, q3_1, q3_2, fmt(q3), fmt(q1), fmt(q2), fmt(q3), kq))

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

