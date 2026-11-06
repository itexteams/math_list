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


def bt_dang31_p1_b2_c3_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Sinh ngẫu nhiên tần số cho các nhóm
                n1 = randint(15, 30)
                n2 = randint(25, 40)
                n3 = randint(20, 35)
                n4 = randint(10, 25)
                n5 = randint(5, 15)

                # Tổng tần số
                N = n1 + n2 + n3 + n4 + n5

                # Giá trị đại diện của từng nhóm: [0;2), [2;4), [4;6), [6;8), [8;10)
                x1, x2, x3, x4, x5 = 1, 3, 5, 7, 9

                # Tính tổng x_i * n_i và giá trị trung bình
                tong = x1*n1 + x2*n2 + x3*n3 + x4*n4 + x5*n5
                kq_float = tong / N

                # Làm tròn đến hàng phần mười (1 chữ số thập phân)
                kq3 = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')
                kq_val = float(kq3)

                # Đáp án đúng
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai không trùng với đáp án đúng
                s_set = set()
                offsets = [0.5, -0.5, 0.7, -0.7, 1.2, -1.2, 1.5, -1.5, 0.3, -0.3, 0.8, -0.8]
                for off in offsets:
                    val = round(kq_val + off, 1)
                    if val > 0 and val != kq_val:
                        s_set.add('$%s$' % (str(val).replace('.', ',')))

                s = list(s_set)
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Sau khi khảo sát tổng số giờ xem truyền hình (đơn vị: giờ) của $%s$ gia đình trong hai ngày nghỉ cuối tuần, người ta thu được mẫu số liệu ghép nhóm như sau:
            \\begin{center}
            \\begin{tabular}{|c|c|c|c|c|c|}
            \\hline
            \\textbf{Số giờ xem truyền hình} & $[0; 2)$ & $[2; 4)$ & $[4; 6)$ & $[6; 8)$ & $[8; 10)$ \\\\
            \\hline
            \\textbf{Tần số} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Giá trị trung bình của mẫu số liệu ghép nhóm đó bằng (làm tròn kết quả đến hàng phần mười)'''
                                 % (latex(N), latex(n1), latex(n2), latex(n3), latex(n4), latex(n5)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Giá trị đại diện của các nhóm lần lượt là $x_1 = 1$, $x_2 = 3$, $x_3 = 5$, $x_4 = 7$, $x_5 = 9$.\\\\
            Tổng số gia đình được khảo sát là $N = %s + %s + %s + %s + %s = %s$.\\\\
            Giá trị trung bình của mẫu số liệu ghép nhóm là:\\\\
            $\\bar{x} = \\frac{1 \\cdot %s + 3 \\cdot %s + 5 \\cdot %s + 7 \\cdot %s + 9 \\cdot %s}{%s} = \\frac{%s}{%s} \\approx %s$.'''
                           % (latex(n1), latex(n2), latex(n3), latex(n4), latex(n5), latex(N),
                              latex(n1), latex(n2), latex(n3), latex(n4), latex(n5), latex(N),
                              latex(tong), latex(N), kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

