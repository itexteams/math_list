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


def bt_dang23_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- CÁC THAM SỐ RANDOM CỦA BÀI TOÁN CẤP SỐ CỘNG ---
                n = randint(12, 25)           # Số hàng ghế
                u1 = randint(15, 30)          # Số ghế hàng thứ nhất
                d = randint(1, 3)             # Công sai (số ghế hơn hàng trước)
                # Giá vé (nghìn đồng), chọn số chia hết cho 5
                gia_ve_nghin = random.choice([x for x in range(50, 151) if x % 5 == 0]) 
                gia_ve = gia_ve_nghin * 1000  # Giá vé (đồng)

                # --- TÍNH TOÁN KẾT QUẢ ---
                # 1. Tính tổng số ghế (S_n)
                # Sn = n/2 * (2*u1 + (n-1)*d)
                tong_so_ghe = (n / 2) * (2 * u1 + (n - 1) * d) 
                # 2. Tính tổng số tiền thu được
                tong_tien = tong_so_ghe * gia_ve 

                # Kết quả tính theo triệu đồng (chính xác)
                kq_trieu_exact = tong_tien / 1000000

                # LÀM TRÒN KẾT QUẢ ĐÚNG (theo yêu cầu đề bài: 1 chữ số thập phân)
                kq_decimal = Decimal(kq_trieu_exact).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.',',') # Format: 35,4

                # Chuẩn bị đáp án đúng
                da = '$%s$' % (kq_str)

                # TẠO CÁC ĐÁP ÁN SAI (Lấy kết quả tính theo triệu đồng làm tham chiếu)
                kq_round = round(kq_trieu_exact, 0) # Lấy phần nguyên để tạo đáp án gần nhau

                # Tạo danh sách các giá trị sai
                s_values = [kq_round + 1, kq_round + 2, kq_round - 1, kq_round - 2]
                # Loại bỏ các giá trị trùng lặp nếu có (ví dụ: kq_round = 35)
                s_values = list(set(s_values)) 

                s = []
                for val in s_values:
                    # Làm tròn các đáp án sai đến 1 chữ số thập phân (để đồng nhất với đáp án đúng)
                    val_decimal = Decimal(val).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    s.append('$%s$'%(str(val_decimal).replace('.',',')))


                # Chọn ngẫu nhiên 3 đáp án sai
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một rạp hát có $%s$ hàng ghế. Hàng thứ nhất có $%s$ ghế, số ghế ở các hàng sau hơn số ghế ngay trước đó $%s$ ghế. Cho biết rạp hát đã bán hết vé với giá mỗi vé là $%s$ nghìn đồng. Tổng số tiền vé thu được của rạp hát bằng bao nhiêu triệu đồng? (làm tròn kết quả đến hàng đơn vị).'''
                                %(latex(n), latex(u1), latex(d), latex(gia_ve_nghin)
                                ))

                # Các đáp án
                da_d = ('\\True ' + str(da) + ' \\text{ (triệu đồng)}') # Đáp án đúng
                da_s1 = str(das1) + ' \\text{ (triệu đồng)}'
                da_s2 = str(das2) + ' \\text{ (triệu đồng)}'
                da_s3 = str(das3) + ' \\text{ (triệu đồng)}'

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Gọi $u_n$ là số ghế ở hàng thứ $n$. \\\\
            Khi đó, dãy số $(u_n)$ tạo thành cấp số cộng với $u_1 = %s$ và công sai $d = %s$. \\\\
            Tổng số ghế có trong rạp hát là $S_{%s}$: \\\\
            $S_{%s} = \\frac{%s[2\\cdot %s+(%s-1)\\cdot %s]}{2} = %s \\text{ (ghế)}$
            Tổng số tiền vé thu được là \\\\
            $\\text{Tổng tiền} = %s \\cdot %s \\text{ (đồng)} = %s \\text{ (triệu đồng)} \\approx %s \\text{ (triệu đồng.)}$'''

                        %(latex(u1), latex(d),
                          latex(n), latex(n), latex(n), latex(u1), latex(n), latex(d), latex(round(tong_so_ghe,0)).replace('.0',''),
                          latex(round(tong_so_ghe,0)).replace('.0',''), latex(gia_ve), latex(round(kq_trieu_exact,1)).replace('.',','), kq_str
                        ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
            return content 

