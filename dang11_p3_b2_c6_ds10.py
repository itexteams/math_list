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


def bt_dang11_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Random số lần gieo đồng tiền (từ 3 đến 6 lần để bài toán hợp lý)
                n = random.randint(3, 5) 

                # Tính toán các giá trị
                omega_size = 2**n

                # Đáp án đúng luôn là 1/2^n
                kq = Rational(1, omega_size)
                da = '$%s$' % latex(kq)

                # B4: Tạo các phương án sai (không trùng với đáp án đúng)
                s = []
                # Phương án n/2^n
                s_val1 = Rational(n, omega_size)
                if s_val1 != kq:
                    s.append('$%s$' % latex(s_val1))

                # Phương án 2/2^n
                s_val2 = Rational(2, omega_size)
                if s_val2 != kq:
                    s.append('$%s$' % latex(s_val2))

                # Phương án (n+2)/2^n
                s_val3 = Rational(n + 2, omega_size)
                if s_val3 != kq:
                    s.append('$%s$' % latex(s_val3))

                # Bổ sung thêm phương án nếu thiếu
                while len(s) < 3:
                    rand_num = random.randint(3, 10)
                    s_val_extra = Rational(rand_num, omega_size)
                    s_str = '$%s$' % latex(s_val_extra)
                    if s_str != da and s_str not in s:
                        s.append(s_str)

                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # B2: Viết nội dung câu hỏi
                # Chuyển số n sang chữ tiếng Việt tương ứng (tùy chọn, ở đây dùng số cho gọn)
                dict_chu = {3: 'ba', 4: 'bốn', 5: 'năm', 6: 'sáu'}
                n_chu = dict_chu.get(n, str(n))

                noidungcauhoi = ('Gieo một đồng tiền cân đối và đồng chất %s lần. Xác suất để cả %s lần xuất hiện mặt sấp bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                                 % (n_chu, n_chu))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B1 & B2)
                # Tạo chuỗi 2.2.2...2
                phep_tinh_omega = " . ".join(["2"] * n)
                h1=1/omega_size
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')
                loigiai = ('Số phần tử của không gian mẫu là $|\\Omega| = %s = %s$. \\\\'
                           'Gọi $A$ là biến cố: "Cả %s lần gieo xuất hiện mặt sấp". \\\\'
                           'Khi đó chỉ có duy nhất một kết quả thuận lợi cho biến cố $A$ là $\\left( S; S; \\dots; S \\right)$, suy ra $|\\Omega_A| = 1$. \\\\'
                           'Vậy xác suất cần tính là $P\\left( A \\right) = \\frac{|\\Omega_A|}{|\\Omega|} = \\frac{1}{%s} \\approx %s$.'
                           % (phep_tinh_omega, latex(omega_size), n_chu, latex(omega_size), kqz))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r, sử dụng \left( \right))
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

