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


def bt_dang45_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số vòng và số giây sao cho phép chia số vòng / số giây ra số đẹp (ví dụ: 30 vòng trong 8 giây -> 3.75)
                # Ta chọn cặp số (vong, giay) sao cho số vòng/giây là số hữu tỉ gọn
                cap_so = random.choice([(30, 8), (20, 8), (25, 4), (15, 4), (40, 8), (18, 6)])
                vong = cap_so[0]
                giay = cap_so[1]

                # Số vòng trong 1 giây (dưới dạng phân số và số thập phân)
                vong_1s_frac = Rational(vong, giay)
                vong_1s_float = float(vong_1s_frac)
                vong_1s_str = str(vong_1s_float).replace('.', ',')

                # Số vòng trong 1 phút (60 giây)
                vong_1p = vong_1s_frac * 60

                # Số đo góc quay sau 1 phút (tính bằng radian: số vòng * 2pi)
                goc_rad = vong_1p * 2

                # Bán kính bánh xe r (đơn vị cm), random từ 30 đến 40 cm
                r_cm = random.choice([30, 32, 35, 36, 38, 40])
                r_m_frac = Rational(r_cm, 100)
                r_m_float = float(r_m_frac)
                r_m_str = str(r_m_float).replace('.', ',')

                # Tính độ dài quãng đường chính xác theo mét trước khi nhân pi
                quang_duong_heso = goc_rad * r_m_frac

                # Tính giá trị xấp xỉ làm tròn đến hàng đơn vị theo yêu cầu đề bài
                val_approx = float(quang_duong_heso * math.pi)
                kq_num = Decimal(str(val_approx)).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
                kq = str(kq_num)

                # Giá trị mẫu trước khi làm tròn để hiển thị trong lời giải (lấy 1 chữ số thập phân như mẫu gốc)
                val_mau = Decimal(str(val_approx)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                val_mau_str = str(val_mau).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$ m' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai xung quanh đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    sai_val = int(kq_num) + random.choice([-50, -30, -15, 15, 30, 50, 75])
                    if sai_val > 0 and sai_val != int(kq_num):
                        s_set.add('$%s$ m' % (sai_val))

                s_list = list(s_set)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong chặng đua nước rút, bánh xe của một vận động viên đua xe đạp quay được $%s$ vòng trong $%s$ giây. Chọn chiều quay của bánh xe là chiều dương. Xét van $V$ của bánh xe. Biết rằng bán kính của bánh xe là $%s$ cm. Độ dài quãng đường mà vận động viên đua xe đạp đã đi được trong $1$ phút là bao nhiêu mét? (Kết quả làm tròn đến hàng đơn vị).'''
                                 % (latex(vong), latex(giay), latex(r_cm)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Sau $1$ giây, van $V$ của bánh xe quay được $\\frac{%s}{%s} = %s$ (vòng). \\\\
                           Sau $1$ phút, van $V$ của bánh xe quay được $%s \\cdot 60 = %s$ (vòng). \\\\
                           Suy ra sau $1$ phút, van $V$ của bánh xe quay được một góc có số đo là $%s \\cdot 2\\pi = %s\\pi$. \\\\
                           Mỗi góc ở tâm với số đo $1$ rad chắn một cung có độ dài bằng bán kính bánh xe $r = %s$ m. \\\\
                           Do đó độ dài quãng đường mà vận động viên đua xe đạp đã đi được trong $1$ phút là \\\\
                           $%s\\pi \\cdot %s \\approx %s$ m $\\approx %s$ m.'''
                           % (latex(vong), latex(giay), vong_1s_str,
                              vong_1s_str, latex(vong_1p),
                              latex(vong_1p), latex(goc_rad),
                              r_m_str,
                              latex(goc_rad), r_m_str, val_mau_str, latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

