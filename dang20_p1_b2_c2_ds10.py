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


def bt_dang20_p1_b2_c2_ds10(self):
            # Định nghĩa hàm
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số tiền thưởng (nghìn đồng), ví dụ từ 400 đến 800 nghìn, chia hết cho 100
                tong_tien = randint(4, 8) * 100 

                # Random giá kem Merino (nghìn đồng), từ 10 đến 14
                gia_merino = randint(10, 14)

                # Random giá kem TH (nghìn đồng), từ 15 to 18
                gia_th = randint(15, 18)

                # Đảm bảo giá hai loại kem và tổng tiền tối giản tạo ra các số nguyên đẹp
                # Tìm ước chung lớn nhất của gia_merino, gia_th, tong_tien để rút gọn bất phương trình tiền
                ucln = math.gcd(math.gcd(gia_merino, gia_th), tong_tien)

                # Hệ số sau khi rút gọn cho bất phương trình tiền: a*x + b*y <= c
                a = int(gia_merino / ucln)
                b = int(gia_th / ucln)
                c = int(tong_tien / ucln)

                # Random số lượng kem tối đa chứa được trong tủ lạnh, từ 25 đến 40
                max_kem = randint(25, 40)

                # Đáp án đúng (Hệ bất phương trình đúng định dạng LaTeX)
                # Vì viết trong chuỗi hệ thống và quy định dấu \\, ta dùng cấu trúc dạng hệ \begin{cases} ... \end{cases}
                da_dung = '\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le %s \\\\ %sx + %sy \\le %s \\end{cases}' % (latex(max_kem), latex(a), latex(b), latex(c))

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (da_dung)]
                da = random.choice(du)

                # Tạo các phương án sai (bẫy về dấu >, <, >= hoặc sai hệ số)
                s = [
                    '$\\begin{cases} x > 0 \\\\ y > 0 \\\\ x + y < %s \\\\ %sx + %sy < %s \\end{cases}$' % (latex(max_kem), latex(a), latex(b), latex(c)),
                    '$\\begin{cases} x > 0 \\\\ y > 0 \\\\ x + y > %s \\\\ %sx + %sy > %s \\end{cases}$' % (latex(max_kem), latex(a), latex(b), latex(c)),
                    '$\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\ge %s \\\\ %sx + %sy \\ge %s \\end{cases}$' % (latex(max_kem), latex(a), latex(b), latex(c)),
                    '$\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le %s \\\\ %sx + %sy \\ge %s \\end{cases}$' % (latex(max_kem), latex(a), latex(b), latex(c)),
                    '$\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y > %s \\\\ %sx + %sy \\le %s \\end{cases}$' % (latex(max_kem), latex(a), latex(b), latex(c))
                ]

                # Lấy ngẫu nhiên các đáp án sai và đảm bảo không trùng nhau
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Bạn Minh đạt được danh hiệu Học sinh giỏi nên được mẹ thưởng cho $%s$ nghìn đồng để mua kem. Minh đến siêu thị dự định mua hai hãng kem Merino và TH. Giá của mỗi chiếc kem Merino là $%s$ nghìn đồng một chiếc, giá của một chiếc kem TH là $%s$ nghìn đồng. Do tủ lạnh đã chứa nhiều đồ nên không gian ngăn bảo quản chỉ có thể chứa tối đa $%s$ chiếc kem. Gọi $x, y$ lần lượt là số kem loại Merino và TH mà Minh có thể mua. Hệ bất phương trình biểu thị các điều kiện ràng buộc của bài toán theo $x, y$ là'''
                                 % (latex(tong_tien), latex(gia_merino), latex(gia_th), latex(max_kem)))

                # Các đáp án mang cấu trúc True/False của đề bài
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $x, y$ lần lượt là số kem loại Merino và TH mà Minh có thể mua ($x, y \\ge 0; x, y \\in \\mathbb{N}$).\\\\
                           Do số kem có thể chứa trong tủ lạnh là $%s$ chiếc nên ta có bất phương trình: $x + y \\le %s$.\\\\
                           Số tiền mua kem không vượt quá $%s$ nghìn nên ta có bất phương trình:\\\\
                           $%sx + %sy \\le %s \\Leftrightarrow %sx + %sy \\le %s$.\\\\
                           Vậy ta có hệ sau:\\\\
                           $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le %s \\\\ %sx + %sy \\le %s \\end{cases}$'''
                           % (latex(max_kem), latex(max_kem), latex(tong_tien),
                              latex(gia_merino), latex(gia_th), latex(tong_tien), latex(a), latex(b), latex(c),
                              latex(max_kem), latex(a), latex(b), latex(c)))

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

