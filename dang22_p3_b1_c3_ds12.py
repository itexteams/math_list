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


def bt_dang22_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                H = random.randint(100, 500)       # Độ cao từ 100m đến 500m
                v0 = round(random.uniform(10.0, 40.0), 2)  # Vận tốc đầu có phần thập phân
                g = random.choice([9.8, 9.81])     # Chọn hằng số g phổ biến

                # Giải phương trình bậc hai: -(g/2)t^2 + v0*t + H = 0
                # t = [ -v0 - sqrt(v0^2 - 4*(-g/2)*H) ] / [ 2*(-g/2) ]
                # t = [ v0 + sqrt(v0^2 + 2*g*H) ] / g (nghiệm dương)
                t_val = (v0 + math.sqrt(v0**2 + 2*g*H)) / g

                # Làm tròn đến hàng đơn vị theo yêu cầu đề bài
                kq_decimal = Decimal(str(t_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq_int = int(kq_decimal)

                # Đáp án đúng
                da = '$%s$ (s)' % kq_int

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                s_wrong = set()
                while len(s_wrong) < 3:
                    sai_offset = random.choice([-5, -3, -2, 2, 4, 6, 8])
                    sai_val = kq_int + sai_offset
                    if sai_val > 0 and sai_val != kq_int:
                        s_wrong.add('$%s$ (s)' % sai_val)

                list_wrong = list(s_wrong)
                das1, das2, das3 = list_wrong[0], list_wrong[1], list_wrong[2]

                # Câu hỏi (B2: Viết lại y hệt bài toán theo mẫu)
                v0_str = str(v0).replace('.', ',')
                g_str = str(g).replace('.', ',')

                noidungcauhoi = (r'''Một vật được ném lên từ độ cao $%s m$ với vận tốc được cho bởi công thức $v(t) = -%s t + %s$ (m/s). Gọi $h(t)$ m là độ cao của vật tại thời điểm $t$ giây. Sau bao lâu kể từ khi bắt đầu được ném lên thì vật đó chạm đất (làm tròn kết quả đến hàng đơn vị của giây)?'''
                                 % (H, g_str, v0_str))

                # Nội dung lời giải (Trình bày logic tìm nguyên hàm và giải phương trình bậc hai)
                g_half_str = str(round(g/2, 2)).replace('.', ',')

                loigiai = (r'''Ta có $h(t) = \int v(t) \text{d}t = \int (-%s t + %s) \text{d} t = -\frac{%s}{2}t^2 + %st + C = -%s t^2 + %st + C$. \\
                             Vì vật được ném lên từ độ cao $%s m$ nên $h(0) = %s$. Suy ra $C = %s$. \\
                             Vậy $h(t) = -%s t^2 + %st + %s$. Khi vật bắt đầu chạm đất ứng với $h(t) = 0$. \\
                             Nên ta có $-%s t^2 + %st + %s = 0 \Leftrightarrow t \approx %s$ hoặc $t \approx %s$. \\
                             Do $t > 0$ nên $t \approx %s$ (s).'''
                           % (g_str, v0_str, g_str, v0_str, g_half_str, v0_str,
                              H, H, H,
                              g_half_str, v0_str, H,
                              g_half_str, v0_str, H, kq_int, round((v0 - math.sqrt(v0**2 + 2*g*H)) / g, 1),
                              kq_int))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_int))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                da_d = '\\True ' + str(da)
                list_ans = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

