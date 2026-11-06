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


def bt_dang34_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo các biến và hằng số
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các thông số cho bài toán
                # F'(m) = A / (B*m + 1)
                # Chọn A là bội của B để hệ số nguyên hàm đẹp
                B = random.randint(2, 5)
                A = B * random.randint(20, 80) 

                P0 = random.randint(30, 100) # Số bệnh nhân ngày đầu (m=0)
                m_target = random.randint(7, 15) # Ngày cần tính (ví dụ ngày thứ 10)

                # Bước 2: Tính toán lời giải
                # F(m) = tích phân(A/(Bm+1)) = (A/B) * ln(Bm+1) + C
                coeff = A // B

                # Tính giá trị tại m_target: F(m) = coeff * ln(B*m + 1) + P0
                val_target = coeff * math.log(B * m_target + 1) + P0

                # Làm tròn đến hàng đơn vị
                kq_final = int(Decimal(str(val_target)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                da_dung = '$%s$' % kq_final

                # Bước 3: Tạo các phương án nhiễu (số nguyên, không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Tạo các số nguyên quanh đáp án đúng trong khoảng +/- 50 đơn vị
                    sai_so = random.choice([-20, -15, -10, -5, 5, 10, 15, 20, 25, 30])
                    val_sai = kq_final + sai_so
                    if val_sai > 0 and str(val_sai) != str(kq_final):
                        s.add('$%s$' % val_sai)

                list_sai = list(s)
                random.shuffle(list_sai)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Khi nghiên cứu dịch sốt xuất huyết ở một địa phương, các chuyên gia y tế ước tính rằng tại ngày thứ $m$ có $F(m)$ người mắc bệnh (sau khi đã làm tròn đến chữ số hàng đơn vị). Biết rằng tốc độ lan truyền bệnh là $F'(m) = \\frac{%s}{%sm + 1}$ và ngày đầu tiên ($m=0$) người ta phát hiện ra $%s$ bệnh nhân. Số người mắc bệnh ở ngày thứ $%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                % (latex(A), latex(B), latex(P0), latex(m_target)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_ans = [da_d, das1, das2, das3]
                random.shuffle(list_ans)

                # Nội dung lời giải
                loigiai = ('''Từ giả thiết ta có: \\\\
                             $F(m) = \\int F'(m) \\text{d}m = \\int \\frac{%s}{%sm+1} \\text{d}m = %s \\ln|%sm+1| + C$. \\\\
                             Tại ngày đầu tiên $m=0$, ta có $F(0) = %s$. \\\\
                             Thay vào công thức: $%s \\ln|%s \\cdot 0 + 1| + C = %s \\Rightarrow C = %s$. \\\\
                             Vậy $F(m) = %s \\ln|%sm+1| + %s$. \\\\
                             Số người mắc bệnh ở ngày thứ $%s$ là: \\\\
                             $F(%s) = %s \\ln|%s \\cdot %s + 1| + %s \\approx %s$ người.'''
                           % (latex(A), latex(B), latex(coeff), latex(B),
                              latex(P0), latex(coeff), latex(B), latex(P0), latex(P0),
                              latex(coeff), latex(B), latex(P0),
                              latex(m_target), latex(m_target), latex(coeff), latex(B), latex(m_target), latex(P0), kq_final))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_final))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

