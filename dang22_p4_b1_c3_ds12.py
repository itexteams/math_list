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


def bt_dang22_p4_b1_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':

                A = random.randint(4, 10) # Thời gian chạm đất (đáp án đúng)
                B = random.randint(1, 3)  # Nghiệm âm để tạo h0 và v0

                # Tính toán các thông số vật lý
                g_half = 4.9
                v0 = round(g_half * (A - B), 2)
                h0 = round(g_half * A * B, 1)

                # Kết quả đúng
                kq = A

                # Các đáp án trắc nghiệm
                du = ['$%s$ giây'%(kq)]
                da = random.choice(du)

                # Tạo danh sách các phương án nhiễu không trùng với đáp án đúng
                s_vals = set()
                while len(s_vals) < 3:
                    sai = random.randint(max(1, A-4), A+5)
                    if sai != A:
                        s_vals.add(sai)

                s = []
                for val in s_vals:
                    s.append('$%s$ giây'%(val))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một quả bóng được ném lên từ độ cao $%s$ m với vận tốc được tính bởi công thức $v(t) = -9,8t + %s$ (m/s). Tính thời gian kể từ khi ném lên thì quả bóng chạm đất.'''
                                 %(latex(h0).replace('.', ','), latex(v0).replace('.', ',')))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $h(t)$ là độ cao của quả bóng tại thời điểm $t$ ($h(t)$ tính theo mét, $t$ tính theo giây). \\\\
                             Khi đó, ta có: $h(t) = \\int (-9,8t + %s) \\text{d}t = -4,9t^2 + %s t + C$. \\\\
                             Mà quả bóng được ném lên từ độ cao $%s$ m tức là tại thời điểm $t=0$ thì $h=%s$ hay $h(0)=%s$. Suy ra $C=%s$. \\\\
                             Vậy công thức tính độ cao $h(t)$ của quả bóng theo thời gian $t$ là: \\\\
                             $h(t) = -4,9t^2 + %s t + %s$. \\\\
                             Khi quả bóng chạm đất thì $h(t)=0$. Ta có: $-4,9t^2 + %s t + %s = 0$. \\\\
                             Giải phương trình ta được $t=%s; t=%s$. Mà $t>0$ nên $t=%s$. \\\\
                             Vậy sau $%s$ giây kể từ khi được ném lên thì quả bóng chạm đất.'''
                           %(latex(v0).replace('.', ','), latex(v0).replace('.', ','), 
                             latex(h0).replace('.', ','), latex(h0).replace('.', ','), latex(h0).replace('.', ','), latex(h0).replace('.', ','),
                             latex(v0).replace('.', ','), latex(h0).replace('.', ','),
                             latex(v0).replace('.', ','), latex(h0).replace('.', ','),
                             latex(-B), latex(A), latex(A), latex(A)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

