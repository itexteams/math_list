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


def bt_dang25_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                v0 = random.randint(100, 200)
                # Gia tốc trọng trường g (thường là 9.8 hoặc 10, ở đây lấy 9.8 theo đề bài mẫu)
                g = 9.8
                g_half = 4.9 # g/2

                # Tính toán thời điểm đạt độ cao cực đại: v(t) = 0 => t = v0 / g
                t_max = v0 / g
                t_max_round = round(t_max, 1)

                # Tính độ cao cực đại: h = v0*t - 0.5*g*t^2
                # Hoặc công thức nhanh: h = v0^2 / (2g)
                h_max_val = (v0**2) / (19.6)

                # Làm tròn kết quả đến chữ số thập phân thứ nhất
                kq_decimal = Decimal(str(h_max_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                # Tạo các đáp án nhiễu bằng cách cộng/trừ ngẫu nhiên hoặc sai lệch công thức
                sai_1 = float(kq_decimal) + random.choice([10.5, 20.2, 15.7])
                sai_2 = float(kq_decimal) - random.choice([12.3, 8.4, 25.1])
                sai_3 = v0 * t_max_round # Sai do quên chia 2 ở phần gia tốc

                # Đảm bảo không trùng
                s_nhieu = set()
                while len(s_nhieu) < 3:
                    val = float(kq_decimal) + random.uniform(-100, 100)
                    val_round = round(val, 1)
                    if val_round != float(kq_decimal):
                        s_nhieu.add(val_round)

                list_sai = [str(x).replace('.', ',') for x in s_nhieu]

                # Câu hỏi (B2: Viết lại y hệt bài toán)
                noidungcauhoi = ('''Một viên đạn được bắn thẳng đứng lên trên từ mặt đất. Giả sử tại thời điểm $t$ giây (coi $t=0$ là thời điểm viên đạn được bắn lên), vận tốc của nó được cho bởi $v(t)=%s-9,8t$(m/s). Tìm độ cao của viên đạn (tính từ mặt đất) khi nó đạt độ cao lớn nhất (làm tròn kết quả đến chữ số thập phân thứ nhất).'''
                                 %(latex(v0)))

                # Các đáp án
                da_d = ('\\True $%s$ m' % kq_str)
                da_s1 = '$%s$ m' % list_sai[0]
                da_s2 = '$%s$ m' % list_sai[1]
                da_s3 = '$%s$ m' % list_sai[2]

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Nội dung lời giải
                loigiai = ('''Từ ý nghĩa cơ học của đạo hàm, ta đã biết độ cao $h(t)$ của viên đạn (tính từ mặt đất) tại thời điểm $t$ thỏa mãn $h'(t)=v(t)$ nên $h(t)$ là nguyên hàm của hàm vận tốc $v(t)$.\\\\
                             Ta có $\\int v(t) \\text{d}t = \\int (%s-9,8t) \\text{d}t = %st-4,9t^2+C$.\\\\
                             Do đó $h(t)=%st-4,9t^2+C$. Từ giả thiết $h(0)=0$ suy ra $C=0$ và $h(t)=%st-4,9t^2$ (m).\\\\
                             Khi viên đạn đạt độ cao cực đại thì $v(t)=%s-9,8t=0$. Từ đó ta có $t=t_m \\approx %s$ (giây).\\\\
                             Độ cao cực đại của viên đạn là $h_{\\max}=h(t_m) \\approx %s \\cdot %s - 4,9 \\cdot %s^2 \\approx %s$ (m).'''
                           %(latex(v0), latex(v0), latex(v0), latex(v0), 
                             latex(v0), latex(round(t_max, 1)), 
                             latex(v0), latex(round(t_max, 1)), latex(round(t_max, 1)), kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

