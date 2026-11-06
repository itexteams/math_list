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


def bt_dang30_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn v0 và gia tốc a sao cho thời điểm dừng lại hoặc quay về là số nguyên
                v0 = random.choice([4, 6, 8, 10, 12, 15, 20])
                a_coeff = random.choice([0.2, 0.4, 0.5, 0.8, 1.0])

                # Tính hệ số của t^2 trong nguyên hàm (a/2)
                hiso_t2 = Rational(str(a_coeff)) / 2

                # Tọa độ x(t) = v0*t - (a/2)*t^2. Vật về gốc tọa độ khi x(t) = 0
                # => t = 2*v0 / a
                kq_num = int(2 * v0 / a_coeff)

                # Định dạng hiển thị số thập phân dùng dấu phẩy cho tiếng Việt
                v0_str = str(v0).replace('.', ',')
                a_str = str(a_coeff).replace('.', ',')
                hiso_t2_str = str(float(hiso_t2)).replace('.', ',')

                # Đáp án đúng
                da = '$%s$ giây' % (kq_num)

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s = [
                    '$%s$ giây' % (kq_num + 5),
                    '$%s$ giây' % (kq_num - 5 if kq_num > 5 else kq_num + 10),
                    '$%s$ giây' % (int(v0 / a_coeff)), # Đây là thời điểm v=0 (dừng lại)
                    '$%s$ giây' % (kq_num * 2),
                    '$%s$ giây' % (v0),
                    '$20$ giây',
                    '$30$ giây'
                ]
                # Loại bỏ giá trị nếu lỡ trùng với đáp án đúng trong danh sách nhiễu
                s = [item for item in s if item != da]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # B2: Viết lại bài toán theo mẫu code python
                # Câu hỏi
                noidungcauhoi = ('''Một vật chuyển động thẳng dọc theo một đường thẳng (có gắn trục tọa độ $Ox$ với độ dài đơn vị bằng $1$ m). Biết rằng vật xuất phát từ vị trí ban đầu là gốc tọa độ và chuyển động với vận tốc $v(t) = %s - %st$ (m/s), trong đó $t$ là thời gian tính theo giây ($t \\ge 0$). Hỏi tại thời điểm nào thì vật đi qua gốc tọa độ (không tính thời điểm ban đầu)?'''
                                 % (v0_str, a_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tọa độ của vật tại thời điểm $t$ là: \\\\
                             $x(t) = \\int v(t)dt = \\int (%s - %st)dt = %st - %st^2 + C$. \\\\
                             Ban đầu vật ở gốc tọa độ nên $x(0) = 0 \\Rightarrow C = 0$. \\\\
                             Suy ra $x(t) = %st - %st^2$ với $t \\ge 0$. \\\\
                             Vật đi qua gốc tọa độ khi $x(t) = 0 \\Leftrightarrow %st - %st^2 = 0 \\Leftrightarrow t(%s - %st) = 0$. \\\\
                             $\\Leftrightarrow t = 0$ hoặc $t = %s$. \\\\
                             Vậy vật đi qua gốc tọa độ tại thời điểm $t = %s$ giây (không tính thời điểm ban đầu).'''
                           % (v0_str, a_str, v0_str, hiso_t2_str,
                              v0_str, hiso_t2_str,
                              v0_str, hiso_t2_str, v0_str, hiso_t2_str,
                              kq_num, kq_num))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_num))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content            

