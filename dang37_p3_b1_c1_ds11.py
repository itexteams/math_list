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


def bt_dang37_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random đường kính bánh xe d (mm), thường từ 550mm đến 750mm, chia hết cho 10 hoặc 20
                d = random.choice([600, 640, 660, 680, 700, 720])
                R_mm = Rational(d, 2)

                # Random số vòng quay n và số giây t_giay sao cho n/t_giay không quá phức tạp
                # Ví dụ mẫu: 11 vòng trong 5 giây
                n_vong = random.choice([9, 11, 13, 15, 17])
                t_giay = random.choice([4, 5, 6])

                # Vận tốc quay (vòng/giây)
                v_quay = Rational(n_vong, t_giay)

                # Số vòng trong 1 phút (60 giây)
                tong_vong = 60 * v_quay

                # Quãng đường đi được l = alpha * R 
                # Một vòng tương ứng góc quay 2*pi (rad)
                # alpha = tong_vong * 2 * pi
                alpha_chia_pi = tong_vong * 2

                # l_mm = alpha_chia_pi * pi * R_mm = alpha_chia_pi * R_mm * pi
                l_mm_heso = alpha_chia_pi * R_mm

                # Đổi sang mét: chia cho 1000
                l_m_exact = Rational(l_mm_heso, 1000) * pi

                # Tính toán giá trị xấp xỉ làm tròn đến hàng đơn vị theo yêu cầu mới nhất ở cuối bài
                val_m = float(l_m_exact)
                kq_dec = Decimal(str(val_m)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec) 

                # Các đáp án trắc nghiệm công thức hóa
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai xung quanh kết quả đúng (làm tròn đến hàng đơn vị)
                s = []
                val_int = int(kq_dec)
                phi_sai = [val_int + 20, val_int - 20, val_int + 50, val_int - 50, val_int + 150, val_int - 150]
                for v_sai in phi_sai:
                    if v_sai > 0 and ('$%s m$' % v_sai) != da and ('$%s m$' % v_sai) not in s:
                        s.append('$%s m$' % v_sai)

                # Trộn chọn phương án sai
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một người đi xe đạp với vận tốc không đổi, biết rằng bánh xe đạp có đường kính là $%s$ mm và quay được $%s$ vòng trong $%s$ giây. Độ dài quãng đường mà người đi xe đã đi được trong $1$ phút gần nhất với giá trị nào dưới đây?'''
                                 % (latex(d), latex(n_vong), latex(t_giay)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải hoàn chỉnh theo từng bước ảnh mẫu
                loigiai = ('''Ta có $1$ phút $= 60$ giây. \\\\
                             Vì người đi xe đạp với vận tốc không đổi và bánh xe đạp quay được $%s$ vòng trong $%s$ giây nên vận tốc của xe đạp là: $%s : %s = \\frac{%s}{%s}$ (vòng/giây). \\\\
                             Số vòng mà bánh xe quay trong $1$ phút là: $60 \\cdot \\frac{%s}{%s} = %s$ vòng. \\\\
                             Quãng đường mà người đi xe đạp đi được trong $1$ phút là \\\\
                             $l = \\alpha R = %s \\cdot 2\\pi \\cdot \\frac{%s}{2} = %s\\pi$ (mm) $\\approx %s$m.'''
                           % (latex(n_vong), latex(t_giay), latex(n_vong), latex(t_giay), latex(n_vong), latex(t_giay),
                              latex(n_vong), latex(t_giay), latex(tong_vong),
                              latex(tong_vong), latex(d), latex(l_mm_heso), kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

