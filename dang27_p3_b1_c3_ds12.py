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


def bt_dang27_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến cấu trúc
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # P0: Số lượng vi khuẩn ban đầu
                p0 = random.choice([200, 300, 400, 500, 600, 800])
                # diff: Số lượng tăng thêm sau 1 ngày (để k đẹp, nên chọn bội của 2/3 nếu muốn k nguyên, 
                # nhưng ở đây ta tính trực tiếp hệ số (2/3)*k = p1 - p0)
                diff = random.choice([50, 100, 150, 200, 250])
                p1 = p0 + diff

                # t_target: Số ngày cần tính sau đó
                t_target = random.choice([3, 4, 5, 6, 7, 8, 9])

                # Tính toán logic:
                # P'(t) = k*sqrt(t) => P(t) = (2/3)*k*t^(3/2) + C
                # P(0) = p0 => C = p0
                # P(1) = (2/3)*k + p0 = p1 => (2/3)*k = p1 - p0 = diff
                # => k = 1.5 * diff
                k_val = int(1.5 * diff)
                hiso_truoc_can = int(diff) # Đây là (2/3)*k

                # Kết quả P(t_target) = diff * sqrt(t_target^3) + p0
                kq_float = diff * math.pow(t_target, 1.5) + p0
                kq_num = int(Decimal(str(kq_float)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # B4: Điều chỉnh các phương án sai
                # Tạo các đáp án nhiễu quanh kết quả đúng
                da_dung = '$%s$' % kq_num

                s = set()
                while len(s) < 3:
                    sai = kq_num + random.choice([-100, -50, 50, 100, -20, 20, -1, 1]) + randint(-5, 5)
                    if sai != kq_num and sai > 0:
                        s.add('$%s$' % sai)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # B2: Viết lại bài toán theo mẫu code python
                # Câu hỏi
                noidungcauhoi = (r'''Một quần thể vi khuẩn ban đầu gồm $%s$ vi khuẩn, sau đó bắt đầu tăng trưởng. Gọi $P(t)$ là số lượng vi khuẩn của quần thể đó tại thời điểm $t$, trong đó $t$ tính theo ngày ($0 \le t \le 10$). Tốc độ tăng trưởng của quần thể vi khuẩn đó cho bởi hàm số $P'(t) = k\sqrt{t}$, trong đó $k$ là hằng số. Sau $1$ ngày, số lượng vi khuẩn của quần thể đó đã tăng lên thành $%s$ vi khuẩn. Số lượng vi khuẩn của quần thể đó sau $%s$ ngày bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                 % (latex(p0), latex(p1), latex(t_target)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))

                # Trộn đáp án
                list_ans = [da_d, das1, das2, das3]
                random.shuffle(list_ans)

                # Nội dung lời giải
                loigiai = (r'''Ta có $P(t) = \int P'(t) \text{d}t = \int k\sqrt{t} \text{d}t = \frac{2}{3}k\sqrt{t^3} + C$. \\
                             Tại thời điểm ban đầu ($t=0$): $P(0) = \frac{2}{3}k\sqrt{0^3} + C = %s \Rightarrow C = %s$. \\
                             Sau 1 ngày ($t=1$): $P(1) = \frac{2}{3}k\sqrt{1^3} + %s = %s \Rightarrow \frac{2}{3}k = %s \Rightarrow k = %s$. \\
                             Vậy số lượng vi khuẩn được biểu diễn bởi hàm số $P(t) = %s\sqrt{t^3} + %s$. \\
                             Số lượng vi khuẩn của quần thể đó sau $%s$ ngày là: \\
                             $P(%s) = %s\sqrt{%s^3} + %s \approx %s$ (con).'''
                           % (latex(p0), latex(p0), 
                              latex(p0), latex(p1), latex(diff), latex(k_val),
                              latex(hiso_truoc_can), latex(p0),
                              latex(t_target), latex(t_target), latex(hiso_truoc_can), latex(t_target), latex(p0), latex(kq_num)))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_num))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

