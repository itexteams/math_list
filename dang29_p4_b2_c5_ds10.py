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


def bt_dang29_p4_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Random số đỉnh của đa giác từ 5 đến 15
                n = random.randint(5, 15)

                # Từ điển tên gọi đa giác tương ứng với số đỉnh
                dict_ten = {
                    5: 'ngũ giác', 6: 'lục giác', 7: 'thất giác', 8: 'bát giác', 
                    9: 'cửu giác', 10: 'thập giác', 11: 'thập nhất giác', 12: 'thập nhị giác'
                }
                ten_da_giac = dict_ten.get(n, str(n) + '-giác')

                # Tạo nhãn các đỉnh (Ví dụ: ABCDEF...)
                chu_cai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                nhan_dinh = chu_cai[:n]

                # Đáp án đúng là chỉnh hợp chập 2 của n: A_n^2
                kq_dung = '$A_{%s}^2$' % (latex(n))

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                # Các phương án nhiễu thường gặp trong bài toán này
                s = [
                    '$C_{%s}^2$' % (latex(n)),
                    '$P_{%s}$' % (latex(n)),
                    '$%s$' % (latex(n * (n-1))), # Giá trị cụ thể của A_n^2
                    '$%s$' % (latex(n**2)),
                    '$%s$' % (latex(2*n)),
                    '$A_{%s}^2 + %s$' % (latex(n), latex(random.randint(1, 5)))
                ]

                # Loại bỏ phương án nếu tình cờ trùng với giá trị latex của kq_dung
                if kq_dung in s:
                    s.remove(kq_dung)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Tìm số vectơ khác $\\vec{0}$ có điểm đầu, điểm cuối là hai trong $%s$ đỉnh của %s $%s$.'''
                                 % (latex(n), ten_da_giac, nhan_dinh))

                # Các đáp án
                da_d = ('\\True ' + str(kq_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B1 & B7: Viết chi tiết, đầy đủ)
                loigiai = ('''Mỗi vectơ khác $\\vec{0}$ được xác định bởi một cặp điểm đầu và điểm cuối phân biệt.\\\\
                             Để tạo thành một vectơ khác $\\vec{0}$ từ các đỉnh của %s $%s$, ta cần chọn ra $2$ đỉnh trong số $%s$ đỉnh và sắp xếp thứ tự của chúng (đỉnh nào là điểm đầu, đỉnh nào là điểm cuối).\\\\
                             Số cách chọn và sắp xếp như vậy là số chỉnh hợp chập $2$ của $%s$ phần tử.\\\\
                             Vậy số vectơ thỏa mãn yêu cầu bài toán là $A_{%s}^2$.'''
                           % (ten_da_giac, nhan_dinh, latex(n), latex(n), latex(n)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

