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


def bt_dang35_p4_b1_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Tìm cách random bài toán
                # Chọn n là số phần tử của tập A (từ 7 đến 9 để số không quá lớn hoặc quá nhỏ)
                n = random.randint(7, 9)
                tap_A = list(range(1, n + 1))

                # Xác định các chữ số lẻ trong tập A
                odd_digits = [i for i in tap_A if i % 2 != 0]
                # Điều kiện: lẻ và không chia hết cho 5 (loại số 5)
                valid_d = [i for i in odd_digits if i != 5]

                count_d = len(valid_d) # Số cách chọn chữ số tận cùng
                fact_remaining = math.factorial(n - 1) # Cách xếp các chữ số còn lại

                # Đáp án đúng
                ket_qua = count_d * fact_remaining

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                # Tạo danh sách các phương án sai dựa trên các lỗi logic phổ biến
                s_list = [
                    (count_d + 1) * fact_remaining,             # Chọn thừa 1 chữ số tận cùng
                    len(odd_digits) * fact_remaining,           # Quên điều kiện không chia hết cho 5
                    count_d * math.factorial(n - 2),            # Tính sai giai thừa
                    ket_qua + random.randint(10, 100),          # Số ngẫu nhiên
                    ket_qua - random.randint(10, 100),          # Số ngẫu nhiên
                    (count_d - 1) * fact_remaining if count_d > 1 else ket_qua + 500
                ]

                # Loại bỏ các giá trị trùng với đáp án đúng hoặc trùng nhau
                s_list = list(set([x for x in s_list if x != ket_qua]))
                random.shuffle(s_list)

                # Gán các đáp án
                da = '$%s$' % (latex(ket_qua))
                das1 = '$%s$' % (latex(s_list[0]))
                das2 = '$%s$' % (latex(s_list[1]))
                das3 = '$%s$' % (latex(s_list[2]))

                # Câu hỏi
                # Chuyển đổi tập A sang định dạng chuỗi LaTeX {1, 2, ..., n}
                str_A = '{' + ', '.join(map(str, tap_A)) + '}'

                noidungcauhoi = ('''Cho tập $A = %s$. Từ tập $A$ tìm số các số gồm $%s$ chữ số đôi một khác nhau sao cho các số này lẻ và không chia hết cho $5$.'''
                                 % (str_A, latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B2: Viết lại y hệt và không viết tắt)
                # Chuẩn bị chuỗi liệt kê cho lời giải
                str_odd_digits = ', '.join(map(str, odd_digits))
                str_valid_d = ', '.join(map(str, valid_d))

                loigiai = ('''Gọi số cần tìm có dạng $x = \\overline{a_1a_2...a_{%s}}$ với các chữ số đôi một khác nhau thuộc tập $A$. \\\\
                             Vì $x$ là số lẻ và không chia hết cho $5$ nên chữ số tận cùng $a_{%s}$ phải là số lẻ và khác $5$. \\\\
                             Các chữ số lẻ trong tập $A$ là $\\left\\{ %s \\right\\}$. Loại đi chữ số $5$, ta còn các chữ số $\\left\\{ %s \\right\\}$ để chọn cho $a_{%s}$. \\\\
                             Do đó, chữ số $a_{%s}$ có $%s$ cách chọn. \\\\
                             Sau khi chọn $a_{%s}$, ta còn $%s$ chữ số trong tập $A$ để xếp vào $%s$ vị trí còn lại. \\\\
                             Số cách chọn và sắp xếp các chữ số còn lại là: $%s! = %s$ cách. \\\\
                             Vậy số các số thỏa mãn yêu cầu bài toán là: $%s \\cdot %s = %s$ số.'''
                           % (latex(n), latex(n), 
                              str_odd_digits, str_valid_d, latex(n),
                              latex(n), latex(count_d),
                              latex(n), latex(n-1), latex(n-1),
                              latex(n-1), latex(fact_remaining),
                              latex(count_d), latex(fact_remaining), latex(ket_qua)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

