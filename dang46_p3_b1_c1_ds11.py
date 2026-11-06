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


def bt_dang46_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài kim phút r_phut (ví dụ từ 4,0m đến 4,8m) và kim giờ r_gio (ví dụ từ 2,5m đến 3,0m)
                # Ta biểu diễn dưới dạng phân số Rational để tính toán chính xác hệ số pi trước khi làm tròn
                r_phut_val = random.choice([4.0, 4.2, 4.3, 4.5, 4.6, 4.8])
                r_gio_val = random.choice([2.5, 2.6, 2.7, 2.74, 2.8, 3.0])

                r_phut = Rational(str(r_phut_val))
                r_gio = Rational(str(r_gio_val))

                # Chuỗi hiển thị số thập phân dùng dấu phẩy cho đề bài và lời giải
                r_phut_str = str(float(r_phut)).replace('.', ',')
                r_gio_str = str(float(r_gio)).replace('.', ',')

                # Random thời gian số phút (ví dụ: 20, 30, 40, 45, 50 phút)
                t_phut = random.choice([20, 30, 40, 45, 50])

                # Tỉ lệ thời gian trôi qua so với 1 giờ (60 phút)
                he_so_t = Rational(t_phut, 60)
                he_so_t_str = '%s/%s' % (he_so_t.p, he_so_t.q) if he_so_t.q != 1 else '%s' % he_so_t.p

                # Tính góc quét trong thời gian t_phut (đơn vị rad)
                # Kim phút: quét 2*pi trong 1 giờ
                goc_phut = he_so_t * 2
                # Kim giờ: quét pi/6 trong 1 giờ
                goc_gio = he_so_t * Rational(1, 6)

                # Tổng độ dài hai cung tròn: l = r_phut * goc_phut + r_gio * goc_gio
                tong_heso_pi = r_phut * goc_phut + r_gio * goc_gio

                # Tính giá trị xấp xỉ làm tròn đến hàng đơn vị
                val_approx = float(tong_heso_pi * math.pi)
                kq_num = Decimal(str(val_approx)).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
                kq = str(kq_num)

                # Các đáp án trắc nghiệm
                du = ['$%s$ m' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai xung quanh đáp án đúng không được trùng nhau
                s_set = set()
                while len(s_set) < 3:
                    sai_val = int(kq_num) + random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
                    if sai_val > 0 and sai_val != int(kq_num):
                        s_set.add('$%s$ m' % (sai_val))

                s_list = list(s_set)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Tháp đồng hồ của cung điện Westminster hay thường gọi là Big Ben là một cấu trúc tháp đồng hồ ở mặt Đông-Bắc của công trình Nhà quốc hội ở Westminster, thủ đô London, nước Anh. Mỗi mặt của chiếc đồng hồ được đặt vào trong một khối đá hình vuông có cạnh là $7$ m. Kim phút của đồng hồ dài $%s$ m, được chế tạo bằng đồng, trong khi chiếc kim giờ dài $%s$ m và được chế tạo bằng hợp kim chuyên dùng để đúc súng. Hỏi trong thời gian $%s$ phút, tổng độ dài của hai cung tròn được vạch nên bởi đầu kim giờ và kim phút bằng bao nhiêu mét? (làm tròn đến hàng đơn vị)'''
                                 % (r_phut_str, r_gio_str, latex(t_phut)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Trong một giờ, kim phút quét một góc $2\\pi$ (rad), kim giờ quét một góc $\\frac{2\\pi}{12} = \\frac{\\pi}{6}$ (rad) nên trong thời gian $%s$ phút kim phút quét một góc $\\frac{%s}{%s} \\cdot 2\\pi = \\frac{%s\\pi}{%s}$ (rad), kim giờ quét một góc $\\frac{%s}{%s} \\cdot \\frac{\\pi}{6} = \\frac{\\pi}{%s}$ (rad). \\\\
                           Khi đó tổng độ dài của hai cung tròn được vạch nên bởi đầu kim giờ và kim phút là \\\\
                           $l = %s \\cdot \\frac{%s\\pi}{%s} + %s \\cdot \\frac{\\pi}{%s} = \\frac{%s}{%s}\\pi \\approx %s$ (m). \\\\
                           Trả lời: $%s$ (m).'''
                           % (latex(t_phut), latex(he_so_t.p), latex(he_so_t.q), latex(goc_phut.p), latex(goc_phut.q),
                              latex(he_so_t.p), latex(he_so_t.q), latex(goc_gio.q),
                              r_phut_str, latex(goc_phut.p), latex(goc_phut.q), r_gio_str, latex(goc_gio.q),
                              latex(tong_heso_pi.p), latex(tong_heso_pi.q), latex(kq), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

