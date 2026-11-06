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


def bt_dang10_p3_b4_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các khoảng cách cận nhật (d1) và viễn nhật (d2)
                d1 = randint(140, 150)
                d2 = randint(151, 160)

                # Tính toán các đại lượng a, c và kết quả
                a_val = (d1 + d2) / 2
                c_val = (d2 - d1) / 2
                ans_val = c_val**2

                # Hàm xử lý định dạng số: đổi dấu chấm thành phẩy và bỏ đuôi ,0 nếu là số nguyên
                def format_num(num):
                    s = str(num).replace('.', ',')
                    if s.endswith(',0'):
                        s = s[:-2]
                    return s

                kq = format_num(ans_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không bị trùng với đáp án đúng và luôn dương)
                wrong_offsets = [1, 2, 3, 1.25, 2.25, -1, -2, -1.25, 0.75, 2.5]
                s_list = []
                for offset in wrong_offsets:
                    w_val = ans_val + offset
                    if w_val > 0 and w_val != ans_val:
                        s_list.append('$%s$' % format_num(w_val))

                # Lọc trùng và lấy ngẫu nhiên 3 phương án sai
                s_list = list(set(s_list))
                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Giả sử quỹ đạo của Trái Đất là một đường elip $(E)$ với mặt trời nằm tại tiêu điểm $F_1$. Gọi $F_2$ là tiêu điểm còn lại của elip (điểm đối xứng với mặt trời qua tâm quỹ đạo). Xét đại lượng $P$ là tích khoảng cách từ trái đất đến hai tiêu điểm là $F_1$ và $F_2$ tại một thời điểm bất kỳ. Hãy tìm sự chênh lệch giữa giá trị lớn nhất và giá trị nhỏ nhất của $P$ trong suốt một chu kỳ quay (Biết khoảng cách cận nhật là $%s$ triệu kilomet và viễn nhật là $%s$ triệu kilomet)'''
                                 %(d1, d2))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý định dạng chuỗi số cho phần lời giải
                a_str = format_num(a_val)
                c_str = format_num(c_val)

                # Nội dung lời giải
                loigiai=('''Phương trình chính tắc của $(E): \\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ với $a > b > 0$. \\\\
                Theo đề bài: $\\begin{cases} MF_{1\\min} = a - c = %s \\\\ MF_{1\\max} = a + c = %s \\end{cases}$ (triệu kilomet) nên $\\begin{cases} a = %s \\\\ c = %s \\end{cases}$. \\\\
                Đại lượng cần xét $P = MF_1 \\cdot MF_2 = x \\cdot y$ thì $\\begin{cases} x + y = 2a \\\\ P = x \\cdot y \\end{cases}$. \\\\
                Sử dụng tính chất:
                \\begin{itemize}
                    \\item Tích của hai số có tổng không đổi sẽ lớn nhất khi hai số đó bằng nhau ($x = y$).
                    \\item Tích của hai số có tổng không đổi sẽ nhỏ nhất khi độ chênh lệch giữa hai số đó là lớn nhất.
                \\end{itemize}
                Giá trị lớn nhất xảy ra khi $MF_1 = MF_2 = a \\Rightarrow P_{\\max} = a \\cdot a = a^2$. \\\\
                Mặt khác, giá trị nhỏ nhất xảy ra khi hiệu $|MF_1 - MF_2|$ lớn nhất thì khi đó $MF_1 = a - c$ và $MF_2 = a + c$. \\\\
                Khi đó $P_{\\min} = (a - c)(a + c) = a^2 - c^2$. \\\\
                Vậy sự chênh lệch giữa giá trị lớn nhất và giá trị nhỏ nhất là: \\\\
                $\\Delta P = a^2 - (a^2 - c^2) = c^2 = %s^2 = %s$.'''
                         %(d1, d2, a_str, c_str, c_str, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

