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


def bt_dang29_p3_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1 & B3: Nghiên cứu và thiết lập thông số ngẫu nhiên
                # v0: vận tốc ban đầu (m/s)
                # a_val: độ lớn gia tốc chậm dần đều (m/s^2)

                # Chọn v0 từ 10 đến 30 (bội số của 2 để kết quả thường đẹp)
                v0 = random.choice([10, 12, 14, 16, 18, 20, 24, 30])

                # Tìm các ước số của v0 để thời gian dừng t = v0/a là số nguyên
                uoc = [i for i in range(2, 7) if v0 % i == 0]
                a_val = random.choice(uoc)

                # Thời gian từ lúc phanh đến khi dừng hẳn (v = 0)
                t_dung = int(v0 / a_val)

                # Hàm vận tốc v(t) = -a*t + v0
                v_func = -a_val * t + v0

                # Tính quãng đường bằng tích phân: S = tích phân từ 0 đến t_dung của v(t)
                S_val = integrate(v_func, (t, 0, t_dung))

                # Đáp án đúng
                kq = S_val
                da_dung = '$%s$' % (latex(kq))

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = []
                # Tạo các giá trị sai quanh đáp án đúng
                candidates = [kq + 2, kq + 5, kq + 10, kq - 2, kq - 5, kq / 2, kq * 2]
                for c in candidates:
                    if c > 0 and c != kq:
                        s.append('$%s$' % (latex(c)))

                # Lấy ngẫu nhiên 3 đáp án sai từ danh sách
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # B2: Viết lại nội dung câu hỏi (sử dụng LaTeX)
                noidungcauhoi = ('''Một ô tô đang chạy với vận tốc $%s$ m/s thì người lái xe đạp phanh, thời điểm đó ô tô chuyển động chậm dần đều với vận tốc $v(t) = -%st + %s$ (m/s), trong đó $t$ là khoảng thời gian tính bằng giây kể từ lúc đạp phanh. Từ lúc đạp phanh đến khi dừng hẳn ô tô còn di chuyển được số mét là'''
                                 %(latex(v0), latex(a_val), latex(v0)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Nguyên hàm của -at + v0 là -(a/2)t^2 + v0t
                nguyen_ham = integrate(v_func, t)

                loigiai=('''Thời gian ô tô chuyển động từ lúc đạp phanh cho đến khi dừng hẳn:\\\\
                         $v(t) = 0 \\Leftrightarrow -%st + %s = 0 \\Leftrightarrow t = %s$. \\\\
                           Quảng đường mà ô tô di chuyển từ lúc đạp phanh đến khi dừng hẳn là: \\\\
                               $S = \\int_{0}^{%s} (-%st + %s) \\text{d}t$
                           $= \\left( \\left. %s \\right) \\right|_{0}^{%s} = %s$ (m).'''
                         %(latex(a_val), latex(v0), latex(t_dung),
                           latex(t_dung), latex(a_val), latex(v0),
                           latex(nguyen_ham), latex(t_dung), latex(kq)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

