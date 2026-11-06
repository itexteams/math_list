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


def bt_dang35_p4_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng (giữ cấu trúc lisdang của mẫu)
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các thông số bài toán
                n = randint(7, 9)       # Tổng số người khách (ví dụ từ 7 đến 9)
                k = randint(2, 4)       # Số người cùng đến quầy thứ nhất
                m = 3                   # Số quầy (giữ cố định theo đề bài)

                # Tính toán các giá trị
                n_omega = m**n          # Số phần tử không gian mẫu
                c_n_k = math.comb(n, k) # Tổ hợp chọn k người từ n người
                ways_remaining = (m - 1)**(n - k) # Cách chọn cho những người còn lại
                n_A = c_n_k * ways_remaining      # Số phần tử của biến cố A

                # Tính xác suất tối giản
                p_A = frac(n_A, n_omega)

                # Đáp án đúng
                da_dung = "\\frac{" + str(n_A) + "}{" + str(n_omega) + "}"

                # Bước 4: Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s = []
                # Sai lầm 1: Quên giai đoạn 2 (chỉ tính C_n^k / 3^n)
                s1_val = frac(c_n_k, n_omega)
                s.append("\\frac{" + str(c_n_k) + "}{" + str(n_omega) + "}")

                # Sai lầm 2: Tính nhầm số người còn lại (ví dụ n-k-1)
                s2_val_num = c_n_k * (m - 1)**(n - k - 1)
                s.append("\\frac{" + str(s2_val_num) + "}{" + str(n_omega) + "}")

                # Sai lầm 3: Nhầm số quầy ở mẫu (ví dụ 2^n thay vì 3^n)
                s3_val_den = 2**n
                s.append("\\frac{" + str(n_A) + "}{" + str(s3_val_den) + "}")

                # Sai lầm 4: Một số phân số ngẫu nhiên gần giống
                s.append("\\frac{" + str(randint(10, 50)) + "}{" + str(randint(51, 100)) + "}")

                # Lọc bỏ nếu có phần tử nào trùng với đáp án đúng (đề phòng random)
                s = [item for item in s if item != da_dung]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Có $%s$ người khách bước ngẫu nhiên vào một cửa hàng có $%s$ quầy. Tính xác suất để $%s$ người cùng đến quầy thứ nhất.'''
                                 %(latex(n), latex(m), latex(k)))

                # Các đáp án
                da_d = ('\\True $' + str(da_dung) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết, không viết tắt, dùng \left( \right))
                loigiai = ('''Không gian mẫu là số cách xếp $%s$ người khách vào $%s$ quầy. \\\\
            Vì mỗi khách có $%s$ cách chọn quầy nên có $%s^{%s}$ khả năng xảy ra. \\\\
            Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = %s^{%s} = %s$. \\\\
            Gọi $A$ là biến cố "Có $%s$ người cùng đến quầy thứ nhất, $%s$ người còn lại đến quầy thứ hai hoặc thứ ba". \\\\
            Để tìm số phần tử của $A$, ta chia làm hai giai đoạn như sau: \\\\
            - Giai đoạn thứ nhất: Chọn $%s$ người khách trong $%s$ người khách và cho đến quầy thứ nhất: có $C_{%s}^{%s}$ cách. \\\\
            - Giai đoạn thứ hai: Còn lại $%s$ người khách xếp vào $%s$ quầy. Mỗi người khách có $%s$ cách chọn quầy. Suy ra có $%s^{%s}$ cách xếp. \\\\
            Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = C_{%s}^{%s} \\cdot %s^{%s} = %s \\cdot %s = %s$. \\\\
            Vậy xác suất cần tính $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s}$.'''
                           %(latex(n), latex(m), 
                             latex(m), latex(m), latex(n), 
                             latex(m), latex(n), latex(n_omega),
                             latex(k), latex(n-k),
                             latex(k), latex(n), latex(n), latex(k),
                             latex(n-k), latex(m-1), latex(m-1), latex(m-1), latex(n-k),
                             latex(n), latex(k), latex(m-1), latex(n-k), latex(c_n_k), latex(ways_remaining), latex(n_A),
                             latex(n_A), latex(n_omega)
                             ))

            # Xuất câu trắc nghiệm đúng cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

