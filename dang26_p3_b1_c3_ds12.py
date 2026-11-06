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


def bt_dang26_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # a(t) = k * cos(t)
                k = random.randint(2, 9) 
                # Vận tốc ban đầu v(0) = v0
                v0_val = random.choice([1.5, 2.5, 3.5, 4.5, 5.0])
                v0_str = str(v0_val).replace('.', ',')


                kq_num = 0
                kq = str(kq_num)

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                # Tạo các giá trị sai dựa trên k và v0
                s_vals = [k, -k, float(v0_val), k/2, -k/2, 1]
                # Lọc bỏ giá trị 0 nếu lỡ có trong danh sách sai
                s_vals = [x for x in s_vals if x != 0]
                random.shuffle(s_vals)

                du = ['$%s$ m/s$^2$' % kq]
                da = random.choice(du)

                s = []
                for val in s_vals[:3]:
                    val_str = str(val).replace('.', ',')
                    s.append('$%s$ m/s$^2$' % val_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # B2: Viết lại bài toán theo mẫu code python
                # Câu hỏi
                noidungcauhoi = (r'''Một vật chuyển động với gia tốc được cho bởi hàm số $a(t) = %s \cos t \text{ (m/s}^2\text{)}$. Lúc bắt đầu chuyển động vật có vận tốc $%s \text{ m/s}$. Gia tốc của vật tại thời điểm vận tốc đạt giá trị lớn nhất trong $\pi \text{ (s)}$ đầu tiên bằng bao nhiêu?'''
                                 % (latex(k), v0_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Vận tốc của vật được biểu diễn bởi hàm số $v(t) = \int a(t) \text{d}t = \int %s \cos t \text{d}t = %s \sin t + C$. \\
                             Khi bắt đầu chuyển động, vật có vận tốc $%s \text{ m/s}$ nên ta có: \\
                             $v(0) = %s \Leftrightarrow %s \sin 0 + C = %s \Leftrightarrow C = %s$. \\
                             Suy ra $v(t) = %s \sin t + %s$. \\
                             Trên đoạn $[0; \pi]$, hàm số $\sin t$ đạt giá trị lớn nhất tại $t = \frac{\pi}{2}$. \\
                             Khi đó, gia tốc của vật tại thời điểm $t = \frac{\pi}{2}$ là: \\
                             $a\left(\frac{\pi}{2}\right) = %s \cos\left(\frac{\pi}{2}\right) = 0 \text{ (m/s}^2\text{)}$.'''
                           % (latex(k), latex(k), v0_str, v0_str, latex(k), v0_str, v0_str, latex(k), v0_str, latex(k)))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(0))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

