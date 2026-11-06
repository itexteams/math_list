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


def bt_dang48_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Số lượng chữ số có thể chọn (từ 0 đến n-1)
                # Mặc định là 10 (từ 0 đến 9) nhưng có thể random nhẹ để tạo bài toán mới
                n_digits = 10 

                # Số phần tử của không gian mẫu (chọn 2 chữ số khác nhau có tính thứ tự)
                # n(Omega) = A(n, 2) = n * (n - 1)
                omega = n_digits * (n_digits - 1)

                # Đáp án đúng
                kq = Rational(1, omega)
                da = '$%s$' % (latex(kq))

                # Tạo các phương án sai
                s = [
                    '$%s$' % (latex(Rational(1, n_digits * n_digits))),  # Quên điều kiện khác nhau (1/100)
                    '$%s$' % (latex(Rational(1, math.comb(n_digits, 2)))), # Không tính thứ tự (1/45)
                    '$%s$' % (latex(Rational(1, (n_digits - 1) * (n_digits - 1)))), # 1/81
                    '$%s$' % (latex(Rational(1, 49))),
                    '$%s$' % (latex(Rational(1, 98))),
                    '$%s$' % (latex(Rational(1, 50)))
                ]

                # Loại bỏ đáp án đúng nếu lỡ trùng trong danh sách sai
                if da in s:
                    s.remove(da)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Bạn Nam muốn gọi điện cho cô chủ nhiệm nhưng quên mất hai chữ số cuối của số điện thoại, bạn chỉ nhớ rằng hai chữ số đó khác nhau. Vì có chuyện gấp nên bạn bấm ngẫu nhiên hai chữ số bất kì trong các số từ $0$ đến $9$. Xác suất để bạn gọi đúng số của cô trong lần gọi đầu tiên bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).''')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                h1=1/omega
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')

                # Nội dung lời giải chi tiết
                loigiai = ('''Số các chữ số từ $0$ đến $9$ là $%s$ chữ số. \\\\
                             Vì hai chữ số cuối của số điện thoại là khác nhau, nên việc chọn ngẫu nhiên hai chữ số (có tính thứ tự) tương ứng với việc chọn một chỉnh hợp chập $2$ của $%s$ phần tử. \\\\
                             Số phần tử của không gian mẫu là: \\\\
                             $n\\left(\\Omega\\right) = A_{%s}^2 = %s \\cdot %s = %s$. \\\\
                             Gọi $A$ là biến cố: "Nam gọi đúng số điện thoại của cô chủ nhiệm". \\\\
                             Vì trong các cặp số có thể bấm, chỉ có duy nhất một cặp số tương ứng với số điện thoại đúng của cô, nên số kết quả thuận lợi cho biến cố $A$ là: \\\\
                             $n\\left(A\\right) = 1$. \\\\
                             Xác suất để bạn Nam gọi đúng số của cô trong lần gọi đầu tiên là: \\\\
                             $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{1}{%s} \\approx %s$.'''
                           % (latex(n_digits), latex(n_digits), latex(n_digits), 
                              latex(n_digits), latex(n_digits - 1), latex(omega), 
                              latex(omega), kqz
                             ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

