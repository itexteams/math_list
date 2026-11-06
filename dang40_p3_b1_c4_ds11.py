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


def bt_dang40_p3_b1_c4_ds11(self):
            # Khai báo biến
            # --- KHỞI TẠO BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random lượng bột lớp đầu tiên (u1) từ 50 đến 400, bước nhảy 50
                u1 = random.randrange(50, 450, 50)

                # Random phần trăm giảm (p) để bài toán đa dạng
                # Chọn các giá trị để kết quả thường là số nguyên hoặc thập phân đẹp
                p_percent = random.choice([10, 20, 25, 40, 50])
                p_decimal = Rational(p_percent, 100)

                # Tính công bội q = 1 - p
                q = 1 - p_decimal

                # Tính tổng S = u1 / (1 - q)
                # 1 - q chính bằng p_decimal
                kq_val = u1 / p_decimal

                # Định dạng đáp án
                kq = latex(kq_val)

                # Tạo các đáp án nhiễu
                s = [
                    '$%s$' % latex(kq_val + 50),
                    '$%s$' % latex(kq_val - 50),
                    '$%s$' % latex(kq_val + 100),
                    '$%s$' % latex(kq_val * 2),
                    '$%s$' % latex(u1 * 10),
                    '$%s$' % latex(kq_val + 20),
                ]

                # Chọn ngẫu nhiên đáp án đúng và các đáp án sai
                da_dung = '$%s$' % kq
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Bạn đang chuẩn bị làm một chiếc bánh nhiều lớp. Để phủ đều các lớp bánh, bạn sử dụng một loại bột mịn. Lượng bột phủ cho lớp bánh đầu tiên là $%s$ g. Ở mỗi lớp tiếp theo, lượng bột cần thiết sẽ giảm đi $%s\\%%$ so với lớp trước đó do diện tích cần phủ giảm dần. Tổng lượng bột bạn cần sử dụng nếu bạn muốn phủ vô hạn lớp bánh theo quy tắc này bằng bao nhiêu?'''
                                 % (latex(u1), latex(p_percent)))

                # Các đáp án theo format \True
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn thứ tự đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Lượng bột cần cho lớp đầu tiên: $u_1 = %s$ g. \\\\
                             Do mỗi lớp tiếp theo lượng bột cần giảm đi $%s\\%%$ nên ta có công bội: $q = 1 - %s = %s$. \\\\
                             Khối lượng bột ở từng lớp lập thành một cấp số nhân lùi vô hạn với $u_1 = %s$ và $q = %s$. \\\\
                             Tổng lượng bột cần dùng cho các lớp bánh là tổng của một cấp số nhân lùi vô hạn: \\\\
                             $S = \\frac{u_1}{1 - q} = \\frac{%s}{1 - %s} = %s$. \\\\
                             Vậy, tổng lượng bột cần để phủ vô hạn lớp bánh là $%s$ g.'''
                           % (latex(u1), latex(p_percent), latex(p_decimal), latex(q), 
                              latex(u1), latex(q), 
                              latex(u1), latex(q), latex(kq_val), latex(kq_val)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))
            # Xuất nội dung theo định dạng ex
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

