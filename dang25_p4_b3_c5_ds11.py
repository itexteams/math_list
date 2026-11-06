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


def bt_dang25_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Bước 1 & 3: Nghiên cứu đề bài và thiết lập các biến số ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số tiền gửi (từ 50 đến 500 triệu, bước nhảy 50)
                tien_gui = random.choice([50, 100, 150, 200, 250, 300, 400, 500])

                # Random lãi suất mỗi quý (từ 1.2% đến 2.5%)
                lai_suat_val = random.choice([1.2, 1.5, 1.8, 2.0, 2.2, 2.5])
                r = lai_suat_val / 100

                # Tính toán kết quả
                # Khoản 1 gửi 1 năm (4 quý)
                T1_val = tien_gui * (1 + r)**4
                # Khoản 2 gửi sau 6 tháng, tức là còn lại 6 tháng (2 quý)
                T2_val = tien_gui * (1 + r)**2

                tong_tien = T1_val + T2_val

                # Làm tròn kết quả đến 2 chữ số thập phân (theo phong cách Việt Nam dùng dấu phẩy)
                kq_decimal = Decimal(str(tong_tien)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
                da_dung = '$%s$' % (kq_str)

                s = []
                # Tạo các sai số ngẫu nhiên để làm đáp án nhiễu
                sai_so = [-10.15, -5.22, 5.12, 10.45, 15.33, -15.21, 2.5, -2.5]
                for ss in sai_so:
                    val_sai = float(kq_decimal) + ss
                    val_sai_str = str(Decimal(str(val_sai)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    s.append('$%s$' % val_sai_str)

                # Loại bỏ trùng lặp nếu có và chọn ra 3 đáp án sai
                s = list(set(s))
                if da_dung in s: s.remove(da_dung)
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Bước 2: Viết lại nội dung câu hỏi dựa trên mẫu
                noidungcauhoi = ('''Một người lần đầu gửi vào ngân hàng $%s$ triệu đồng theo thể thức lãi kép (tức là tiền lãi của kỳ trước được cộng vào vốn của kỳ kế tiếp) với kì hạn $3$ tháng, lãi suất $%s\\%%$ một quý. Sau đúng $6$ tháng, người đó gửi thêm $%s$ triệu đồng với kỳ hạn và lãi suất như trước đó. Tổng số tiền người đó nhận được sau $1$ năm gửi tiền vào ngân hàng gần bằng với kết quả nào sau đây? Biết rằng trong suốt thời gian gửi tiền lãi suất ngân hàng không thay đổi và người đó không rút tiền ra.'''
                                 % (latex(tien_gui), latex(lai_suat_val), latex(tien_gui)))

                da_d = '\\True ' + da_dung
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                T1_str = str(Decimal(str(T1_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                T2_str = str(Decimal(str(T2_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

                loigiai = ('''Ta có: $r = %s\\%% = %s$. \\\\
                             Số tiền $%s$ triệu đồng gửi lần đầu thì sau $1$ năm ($4$ quý) nhận được cả vốn lẫn lãi là: \\\\
                             $T_1 = %s(1 + %s)^4 \\approx %s$ triệu đồng. \\\\
                             Số tiền $%s$ triệu đồng gửi lần thứ hai thì sau $6$ tháng ($2$ quý) nhận được cả vốn lẫn lãi là: \\\\
                             $T_2 = %s(1 + %s)^2 \\approx %s$ triệu đồng. \\\\
                             Vậy tổng số tiền nhận được là: $T = T_1 + T_2 \\approx %s$ triệu đồng.'''
                           % (latex(lai_suat_val), latex(r), 
                              latex(tien_gui), latex(tien_gui), latex(r), T1_str,
                              latex(tien_gui), latex(tien_gui), latex(r), T2_str,
                              kq_str))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

