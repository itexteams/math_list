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


def bt_dang43_p1_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (giữ nguyên logic mẫu)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # nm: số học sinh nam, nf: số học sinh nữ
                # kt: tổng số học sinh chọn, kf: số học sinh nữ chọn
                nm = randint(12, 18) # Mẫu là 15
                nf = randint(18, 25) # Mẫu là 20
                kt = randint(4, 6)   # Mẫu là 5
                kf = randint(2, kt - 1) # Mẫu là 3
                kn = kt - kf         # Mẫu là 2 (số nam cần chọn)

                # Tính toán kết quả bằng công thức tổ hợp
                cach_chon_nu = binomial(nf, kf)
                cach_chon_nam = binomial(nm, kn)
                kq_val = cach_chon_nu * cach_chon_nam

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                kq = int(kq_val)
                s = set()
                while len(s) < 3:
                    # Tạo sai số bằng cách thay đổi nhẹ các giá trị hoặc hoán vị chữ số
                    sai_so = random.choice([100, 200, 500, 1000, -100, -200, -500])
                    phuong_an_sai = kq + sai_so
                    if phuong_an_sai > 0 and phuong_an_sai != kq:
                        s.add('$%s$' % latex(phuong_an_sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi (B2 - Viết lại y hệt bài toán theo mẫu)
                noidungcauhoi = ('''Một lớp có $%s$ học sinh nam và $%s$ học sinh nữ. Có bao nhiêu cách chọn $%s$ bạn học sinh sao cho trong đó có đúng $%s$ học sinh nữ?'''
                                 %(latex(nm), latex(nf), latex(kt), latex(kf)))

                # Các đáp án
                da_d = ('\\True $%s$' % latex(kq))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2 - Viết chi tiết đầy đủ)
                loigiai = ('''Số cách chọn $%s$ học sinh nữ từ $%s$ học sinh nữ là: $C_{%s}^{%s} = %s$ cách. \\\\
                             Vì cần chọn tổng cộng $%s$ học sinh nên số học sinh nam cần chọn là $%s - %s = %s$ học sinh. \\\\
                             Số cách chọn $%s$ học sinh nam từ $%s$ học sinh nam là: $C_{%s}^{%s} = %s$ cách. \\\\
                             Số cách chọn $%s$ bạn thỏa mãn yêu cầu bài toán là: $%s \\cdot %s = %s$ cách.'''
                           %(latex(kf), latex(nf), latex(nf), latex(kf), latex(cach_chon_nu),
                             latex(kt), latex(kt), latex(kf), latex(kn),
                             latex(kn), latex(nm), latex(nm), latex(kn), latex(cach_chon_nam),
                             latex(kt), latex(cach_chon_nu), latex(cach_chon_nam), latex(kq)
                           ))

            # Xuất câu trắc nghiệm (Giữ nguyên cấu trúc format)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

