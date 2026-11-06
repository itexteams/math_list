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


def bt_dang62_p4_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Sinh dữ liệu bài toán bằng phương pháp đi ngược từ nghiệm để đảm bảo luôn có nghiệm nguyên dương hợp lý
                x3 = randint(1, 3)    # Số học sinh chỉ ủng hộ 1 tờ 20.000đ
                x23 = randint(1, 4)   # Số học sinh ủng hộ 2 tờ (10.000đ và 20.000đ)
                k = 2                # Tỉ lệ gấp hai lần (giữ cố định để câu văn tự nhiên)

                x2 = k * x3 + (k - 1) * x23  # Số học sinh chỉ ủng hộ 1 tờ 10.000đ (Đây là đáp án đúng)
                x1 = x2 + x3                # Số học sinh chỉ ủng hộ 1 tờ 5.000đ

                m = randint(1, 3)           # Số học sinh chênh lệch ở điều kiện (3)
                N = 2 * x1 + x2 + x3 + x23 - m  # Tổng số học sinh lớp 12A tham gia ủng hộ

                # Đáp án đúng
                da = '$%s$' % (latex(x2))

                # Tạo danh sách các phương án sai không trùng với đáp án đúng và là số dương
                s_candidates = [x2 + 1, x2 + 2, x2 + 6, x2 + 9, x2 - 1, x2 - 2, x2 + 3]
                s = []
                for val in s_candidates:
                    if val > 0 and val != x2 and val not in s:
                        s.append('$%s$' % (latex(val)))

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong đợt quyên góp ủng hộ đồng bào bị lũ lụt, có $%s$ học sinh lớp 12A đã tham gia ủng hộ, mỗi học sinh ủng hộ nhiều nhất 2 tờ tiền khác nhau trong ba loại tờ tiền mệnh giá 5.000 đồng, 10.000 đồng và 20.000 đồng. Biết rằng số học sinh đã tham gia ủng hộ thỏa mãn đồng thời ba kết quả sau:\\\\
            (1) Số học sinh chỉ ủng hộ một tờ 5.000 đồng bằng tổng số học sinh chỉ ủng hộ một tờ 10.000 đồng và số học sinh chỉ ủng hộ một tờ 20.000 đồng.\\\\
            (2) Trong số học sinh không ủng hộ tờ 5.000 đồng thì số học sinh có ủng hộ tờ 10.000 đồng nhiều gấp %s lần số học sinh có ủng hộ tờ 20.000 đồng.\\\\
            (3) Số học sinh chỉ ủng hộ một tờ 5.000 đồng nhiều hơn số học sinh ủng hộ tờ 5.000 đồng và một tờ khác là $%s$ học sinh.\\\\
            Tìm số học sinh lớp 12A chỉ ủng hộ một tờ 10.000 đồng.'''
                                 %(latex(N), latex(k), latex(m)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai=('''Gọi $x_1, x_2, x_3$ lần lượt là số học sinh chỉ ủng hộ một tờ 5.000 đồng, 10.000 đồng, và 20.000 đồng.\\\\
            Gọi $x_{12}, x_{23}, x_{13}$ lần lượt là số học sinh ủng hộ hai tờ loại (5.000 đồng và 10.000 đồng), (10.000 đồng và 20.000 đồng), (5.000 đồng và 20.000 đồng).\\\\
            Theo giả thiết bài ra, tổng số học sinh tham gia là $N = %s$, ta có phương trình:\\\\
            $x_1 + x_2 + x_3 + x_{12} + x_{23} + x_{13} = %s$ (1)\\\\
            Từ kết quả (1), ta có mối liên hệ: $x_1 = x_2 + x_3$ (2)\\\\
            Từ kết quả (2), trong số học sinh không ủng hộ tờ 5.000 đồng (bao gồm các nhóm học sinh ứng với $x_2, x_3, x_{23}$), số học sinh có ủng hộ tờ 10.000 đồng nhiều gấp $%s$ lần số học sinh có ủng hộ tờ 20.000 đồng, ta có:\\\\
            $x_2 + x_{23} = %s(x_3 + x_{23}) \\implies x_{23} = x_2 - %sx_3$ (3)\\\\
            Từ kết quả (3), ta có phương trình: $x_1 - (x_{12} + x_{13}) = %s \\implies x_{12} + x_{13} = x_1 - %s$ (4)\\\\
            Thay (4) vào phương trình tổng số học sinh (1) ta được:\\\\
            $x_1 + x_2 + x_3 + x_{23} + (x_1 - %s) = %s \\implies 2x_1 + x_2 + x_3 + x_{23} = %s$\\\\
            Tiếp tục thay phương trình (2) vào biểu thức trên ta thu được:\\\\
            $2(x_2 + x_3) + x_2 + x_3 + x_{23} = %s \\implies 3x_2 + 3x_3 + x_{23} = %s$\\\\
            Thay tiếp phương trình (3) vào để triệt tiêu biến $x_{23}$:\\\\
            $3x_2 + 3x_3 + (x_2 - %sx_3) = %s \\implies 4x_2 + x_3 = %s$\\\\
            Do $x_2, x_3, x_{23}$ bắt buộc phải là các số nguyên không âm, kết hợp với điều kiện từ (3) là $x_{23} = x_2 - %sx_3 \\ge 0 \\implies x_2 \\ge %sx_3$.\\\\
            Từ hệ điều kiện trên, ta biện luận và tìm được bộ nghiệm nguyên duy nhất thỏa mãn là: $x_2 = %s, x_3 = %s, x_{23} = %s$.\\\\
            Vậy số học sinh lớp 12A chỉ ủng hộ một tờ 10.000 đồng là %s học sinh.'''
                         %(latex(N), latex(N), latex(k), latex(k), latex(k), latex(m), latex(m), 
                           latex(m), latex(N), latex(N + m), latex(N + m), latex(N + m), 
                           latex(k), latex(N + m), latex(N + m), latex(k), latex(k),
                           latex(x2), latex(x3), latex(x23), latex(x2)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

