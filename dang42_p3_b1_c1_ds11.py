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


def bt_dang42_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random thời điểm xuất phát (Ví dụ xuất phát từ m giờ, 2 kim trùng nhau sẵn)
                # Để giữ nguyên bài toán gốc chuẩn xác nhất và dễ mở rộng, ta chọn m = 12
                m = 12 

                # Tính toán các giá trị phân số bằng SymPy để giữ độ chính xác hình thức LaTeX
                v_kim_phut = 1 # 1 vòng/giờ
                v_kim_gio = Rational(1, 12) # 1/12 vòng/giờ
                hieu_v = v_kim_phut - v_kim_gio # 11/12 vòng/giờ

                # Thời gian từ lúc 12 giờ đến khi gặp nhau lần đầu tiên là 12/11 giờ
                t_gap = Rational(12, 11) 

                # Góc quay theo chiều dương hình học (vòng lượng giác) tính bằng radian
                # Vì kim đồng hồ quay theo chiều âm nên kết quả sẽ mang dấu trừ
                goc_duong = t_gap * 2 * pi # 24*pi/11
                goc_am = -goc_duong

                # Tính giá trị thập phân làm tròn đến hàng phần chục của đáp án đúng
                kq_float = float(goc_am.evalf())
                kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Đáp án đúng dạng số thập phân
                da = '$%s$' % (kq_str)

                # Tạo các phương án sai nhiễu dạng số thập phân làm tròn đến hàng phần chục
                s = [
                    '$%s$' % (str(Decimal(str(float(goc_duong.evalf()))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')), # Sai dấu (6,9)
                    '$%s$' % (str(Decimal(str(float((-Rational(13, 16)*pi).evalf()))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$' % (str(Decimal(str(float((-Rational(12, 11)*pi).evalf()))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$' % (str(Decimal(str(float((-Rational(26, 11)*pi).evalf()))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$' % (str(Decimal(str(float((-Rational(23, 11)*pi).evalf()))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')),
                    '$%s$' % ('-3,4'),
                    '$%s$' % ('-5,5')
                ]

                # Loại bỏ trùng lặp và loại bỏ phần tử trùng với đáp án đúng nếu có
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Lúc $%s$ giờ, kim giờ và kim phút của một chiếc đồng hồ trùng nhau. Hỏi từ lúc đó đến khi hai kim trùng nhau lần đầu tiên, kim phút quay được một góc lượng giác bao nhiêu radian? (kết quả làm tròn đến hàng phần chục).'''
                                 % (latex(m)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Định dạng LaTeX cho các bước trung gian
                goc_duong_latex = latex(goc_duong)
                goc_am_latex = latex(goc_am)

                # Nội dung lời giải chi tiết từng bước chuyển sang dạng thập phân ở kết quả cuối cùng
                loigiai = ('''Lúc $%s$ giờ, hai kim đồng hồ cùng chỉ vào số $%s$. Vì kim phút đi nhanh hơn kim giờ nên kim phút đi hết một vòng mà hai kim vẫn chưa gặp nhau.\\\\
            Hiệu vận tốc của hai kim là: $%s - \\frac{1}{12} = \\frac{11}{12}$ (vòng đồng hồ/giờ).\\\\
            Kể từ lúc $1$ giờ, thời gian để kim phút đuổi kịp kim giờ là: $\\frac{1}{12} : \\frac{11}{12} = \\frac{1}{11}$ (giờ).\\\\
            Kể từ lúc $%s$ giờ, thời gian để hai kim chập nhau lần đầu tiên là: $1 + \\frac{1}{11} = %s$ (giờ).\\\\
            Trong $1$ giờ kim phút quay được một vòng $\\Rightarrow$ Kim phút quay được $2\\pi$ (radian).\\\\
            Trong $%s$ giờ kim phút quay được là: $%s \\cdot 2\\pi = %s$ (radian).\\\\
            Do cùng chiều kim đồng hồ là chiều âm $\\Rightarrow$ Kim phút quay được là: $%s \\approx %s$ (radian).'''
                           % (latex(m), latex(m), latex(v_kim_phut), latex(m), latex(t_gap), latex(t_gap), latex(t_gap), goc_duong_latex, goc_am_latex, kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

