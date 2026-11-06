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


def bt_dang46_p1_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn 3 chữ số khác nhau từ 1 đến 9 cho khối đặc biệt
                digits = random.sample(range(1, 10), 3)
                n1, n2, n3 = digits[0], digits[1], digits[2]

                # Logic tính toán theo bài toán gốc (6 chữ số)
                # TH1: Chữ số a khác 0. Có 6 cách chọn a (bỏ 0 và 3 chữ số đã chọn)
                # Có A(6, 2) cách chọn 2 chữ số còn lại. Có 4 vị trí chèn khối và 2 cách đảo khối.
                c1 = 6 * (factorial(6)/factorial(6-2)) * 4 * 2

                # TH2: Chữ số a bằng 0. Có 1 cách chọn a.
                # Có A(6, 2) cách chọn 2 chữ số còn lại. Khối phải đứng trước a để số có 6 chữ số.
                c2 = 1 * (factorial(6)/factorial(6-2)) * 1 * 2

                kq_int = int(c1 + c2)
                kq = str(kq_int)

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s_vals = [
                    kq_int + 120,
                    kq_int - 120,
                    int(kq_int / 2),
                    kq_int + 240,
                    kq_int - 60,
                    1200,
                    1800
                ]
                # Lọc bỏ giá trị trùng với đáp án đúng
                s_vals = [v for v in s_vals if v != kq_int and v > 0]
                random.shuffle(s_vals)

                # Các đáp án trắc nghiệm
                da_d = ('\\True $%s$' % (kq))
                da_s1 = '$%s$' % (s_vals[0])
                da_s2 = '$%s$' % (s_vals[1])
                da_s3 = '$%s$' % (s_vals[2])

                # Câu hỏi
                noidungcauhoi = ('''Có bao nhiêu số tự nhiên có sáu chữ số khác nhau từng đôi một, trong đó chữ số $%s$ đứng liền giữa hai chữ số $%s$ và $%s$?'''
                                 % (latex(n2), latex(n1), latex(n3)))

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết theo mẫu ảnh)
                loigiai = ('''Chữ số $%s$ đứng liền giữa hai chữ số $%s$ và $%s$ nên ta có thể có khối $%s%s%s$ hoặc $%s%s%s$.\\\\
                            Gọi số cần tìm có dạng được tạo bởi việc chèn khối trên vào một bộ 3 chữ số khác.\\\\
                            Giả sử ta chọn 3 chữ số còn lại là $\\overline{abc}$ từ tập các chữ số còn lại (sau khi đã lấy ra $%s, %s, %s$).\\\\
                            TH1: $a \\neq 0$. Số cách chọn $a$ là $6$ (loại chữ số $0$ và các chữ số $%s, %s, %s$), số cách chọn $b$ và $c$ là $A_6^2$.\\\\
                            Sau đó chèn khối $%s%s%s$ hoặc $%s%s%s$ vào $4$ vị trí xen kẽ giữa các chữ số $a, b, c$ (bao gồm cả vị trí sau $c$) nên có $6 \\cdot A_6^2 \\cdot 4 \\cdot 2 = %s$ cách.\\\\
                            TH2: $a = 0$. Số cách chọn $a$ là $1$, số cách chọn $b$ và $c$ là $A_6^2$.\\\\
                            Để số tạo thành là số có 6 chữ số, khối $%s%s%s$ hoặc $%s%s%s$ phải chèn vào duy nhất $1$ vị trí trước $a$ nên có $1 \\cdot A_6^2 \\cdot 1 \\cdot 2 = %s$ cách.\\\\
                            Vậy có $%s + %s = %s$ số thỏa mãn yêu cầu đề bài.'''
                           % (latex(n2), latex(n1), latex(n3), latex(n1), latex(n2), latex(n3), latex(n3), latex(n2), latex(n1),
                              latex(n1), latex(n2), latex(n3),
                              latex(n1), latex(n2), latex(n3),
                              latex(n1), latex(n2), latex(n3), latex(n3), latex(n2), latex(n1),
                              latex(int(c1)),
                              latex(n1), latex(n2), latex(n3), latex(n3), latex(n2), latex(n1),
                              latex(int(c2)),
                              latex(int(c1)), latex(int(c2)), latex(kq_int)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

