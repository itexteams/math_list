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


def bt_dang33_p1_b1_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1 & 3: Nghiên cứu đề bài và tìm cách random
                # n: số học sinh, m: số thầy giáo
                # Điều kiện để mỗi thầy giáo ngồi giữa 2 học sinh: m <= n - 1
                n = random.randint(6, 8)
                m = random.randint(2, 4)

                # Tính toán kết quả
                # Số cách xếp n học sinh: n!
                cach_hs = math.factorial(n)
                # Số khoảng trống giữa n học sinh: n - 1
                khoang_trong = n - 1
                # Số cách chọn m khoảng trống và xếp m thầy giáo vào: A(khoang_trong, m)
                # nPr = n! / (n-r)!
                cach_gv = math.factorial(khoang_trong) // math.factorial(khoang_trong - m)

                kq_num = cach_hs * cach_gv

                # Tạo danh sách tên thầy giáo A, B, C...
                list_ten = ["A", "B", "C", "D", "E", "F"]
                ten_gv = ", ".join(list_ten[:m])

                # Bước 4: Điều chỉnh các phương án sai
                kq = str(kq_num)

                s_set = set()
                while len(s_set) < 3:
                    # Tạo các phương án sai dựa trên các lỗi logic phổ biến
                    # Sai lầm 1: Dùng tổ hợp thay vì chỉnh hợp
                    sai1 = cach_hs * (math.factorial(khoang_trong) // (math.factorial(m) * math.factorial(khoang_trong - m)))
                    # Sai lầm 2: Tính cả 2 đầu (n+1 khoảng trống)
                    cach_gv_sai = math.factorial(n + 1) // math.factorial(n + 1 - m)
                    sai2 = cach_hs * cach_gv_sai
                    # Sai lầm 3: Hoán vị đơn giản hoặc số ngẫu nhiên gần đáp án
                    sai3 = kq_num // 10 if kq_num > 1000 else kq_num + 100
                    sai4 = (n + m) * 100 # Một con số giả định

                    candidates = [sai1, sai2, sai3, sai4]
                    val = random.choice(candidates)
                    if val != kq_num and val > 0:
                        s_set.add(f'${val}$')

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Bước 2: Viết lại y hệt cấu trúc đề bài trong ảnh
                noidungcauhoi = ('''Có $%s$ học sinh và $%s$ thầy giáo $%s$. Số cách xếp chỗ $%s$ người đó ngồi trên một hàng ngang có $%s$ chỗ sao cho mỗi thầy giáo ngồi giữa hai học sinh là'''
                                 %(latex(n), latex(m), ten_gv, latex(n + m), latex(n + m)))

                # Các đáp án
                da_d = ('\\True ' + '$%s$' % (kq))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết, không viết tắt, dùng \left \right)
                # Sử dụng ký hiệu Chỉnh hợp A_n^k theo kiểu truyền thống VN
                loigiai = ('''Sắp xếp $%s$ học sinh thành một hàng ngang, có $%s!$ cách sắp xếp. \\\\
                           Giữa $%s$ học sinh có $%s$ khoảng trống (không tính hai đầu hàng), ta chọn $%s$ khoảng trống và đưa $%s$ giáo viên vào đó (mỗi giáo viên vào một khoảng trống) để thỏa mãn yêu cầu mỗi giáo viên ngồi giữa hai học sinh. \\\\
                           Số cách chọn và sắp xếp $%s$ giáo viên vào $%s$ khoảng trống là chỉnh hợp chập $%s$ của $%s$ phần tử, ký hiệu là $A_{%s}^{%s}$ cách. \\\\
                           Vậy tất cả có: $%s! \\cdot A_{%s}^{%s} = %s$ cách.'''
                           %(latex(n), latex(n), 
                             latex(n), latex(khoang_trong), latex(m), latex(m),
                             latex(m), latex(khoang_trong), latex(m), latex(khoang_trong), 
                             latex(khoang_trong), latex(m),
                             latex(n), latex(khoang_trong), latex(m), latex(kq_num)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

