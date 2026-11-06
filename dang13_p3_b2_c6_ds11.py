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


def bt_dang13_p3_b2_c6_ds11(self):
            # Khai báo biến
            # Bước 1: Khai báo biến và chọn dạng bài (ở đây có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn xác suất Chiến thắng (p1) và Công thắng (p2)
                # Đảm bảo tổng p1 + p2 < 1 để có xác suất hòa
                p1_val = random.choice([0.2, 0.3, 0.4])
                p2_val = random.choice([0.2, 0.3, 0.4, 0.5])

                # Kiểm tra điều kiện để bài toán hợp lý (tổng không quá 0.9 để p_tie >= 0.1)
                while p1_val + p2_val >= 1.0:
                    p1_val = random.choice([0.2, 0.3])
                    p2_val = random.choice([0.3, 0.4])

                p1 = Decimal(str(p1_val))
                p2 = Decimal(str(p2_val))

                # Tính toán các giá trị trung gian
                p_tie = Decimal('1') - p1 - p2
                p_win = p1 + p2
                kq_val = p_tie * p_win

                # Định dạng hiển thị dấu phẩy cho số thập phân
                p1_s = str(p1).replace('.', ',')
                p2_s = str(p2).replace('.', ',')
                p_tie_s = str(p_tie).replace('.', ',')
                p_win_s = str(p_win).replace('.', ',')

                # Kết quả cuối cùng làm tròn đến hàng phần trăm
                kq_final = kq_val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq_final).replace('.', ',')

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                du = ['$%s$' % (kq)]
                da = du[0]

                s = set()
                while len(s) < 3:
                    # Các phương án nhiễu thường gặp: tính nhầm p_tie, p_win hoặc quên nhân
                    fake_vals = [
                        p_tie, 
                        p_win, 
                        p_tie * p_tie,
                        p_win * p_win,
                        (p1 * p2).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
                        Decimal(str(round(random.uniform(0.1, 0.5), 2)))
                    ]
                    f_val = random.choice(fake_vals)
                    f_str = '$%s$' % (str(f_val).replace('.', ','))
                    if f_str != da:
                        s.add(f_str)

                list_fake = list(s)
                das1 = list_fake[0]
                das2 = list_fake[1]
                das3 = list_fake[2]

                # Câu hỏi (B2: Viết lại y hệt cấu trúc đề bài)
                noidungcauhoi = ('''Hai bạn Chiến và Công cùng chơi cờ với nhau. Trong một ván cờ, xác suất Chiến thắng Công là $%s$ và xác suất để Công thắng Chiến là $%s$. Hai bạn dừng chơi khi có người thắng, người thua. Xác suất để hai bạn dừng chơi sau hai ván cờ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm).'''
                                 % (p1_s, p2_s))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết chi tiết giống nội dung trong ảnh)
                loigiai = ('''Gọi $A$ là biến cố: "Chiến thắng Công trong ván cờ", $B$ là biến cố: "Công thắng Chiến trong ván cờ" và $C$: "Công và Chiến hòa nhau trong ván cờ".\\\\
            Dễ thấy $A, B, C$ là các biến cố xung khắc.\\\\
            Theo giả thiết thì ván đấu thứ nhất hai bạn hòa nhau, ván đấu thứ hai sẽ có thắng thua.\\\\
            Xét ván thứ nhất: $P\\left( C \\right) = 1 - P\\left( A \\right) - P\\left( B \\right) = 1 - %s - %s = %s$.\\\\
            Xét ván thứ hai: $P\\left( A \\cup B \\right) = P\\left( A \\right) + P\\left( B \\right) = %s + %s = %s$.\\\\
            Xác suất để hai bạn dừng chơi sau hai ván đấu là $P = %s \\cdot %s = %s$.'''
                           % (p1_s, p2_s, p_tie_s, p1_s, p2_s, p_win_s, p_tie_s, p_win_s, kq))
                dapan=' \\shortans[0]{$%s$} '%(kq)
            # Xuất câu trắc nghiệm (Đúng cấu trúc mẫu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

