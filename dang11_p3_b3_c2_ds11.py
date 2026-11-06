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


def bt_dang11_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            # Hàm thay thế dấu thập phân từ . sang , và loại bỏ .0
            def format_latex_number(value):
                # Dùng str() để đảm bảo xử lý được Decimal, float hoặc int
                return str(value).replace('.', ',').replace(',0', '')

            if dang=='1':
                # --- RANDOM DỮ LIỆU ---
                # Số tiền gửi hàng tháng (a) - random từ 200 đến 1000 nghìn, bước 100
                a_nghin = random.randrange(200, 1001, 100)
                a = a_nghin / 1000.0  # Chuyển sang triệu đồng

                # Lãi suất hàng tháng (r_percent) - random từ 0.3% đến 1.0%
                r_percent_list = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
                r_percent = random.choice(r_percent_list) 
                r = r_percent / 100.0  # Lãi suất (dạng thập phân)

                # Số lần gửi (n) - random số tháng, bước 12 (số năm) từ 10 đến 20 năm
                n = random.randrange(120, 241, 12) 

                # Tuổi con khi bắt đầu gửi
                tuoi_bat_dau = random.randrange(1, 6) 

                # --- TÍNH TOÁN KẾT QUẢ ---
                # Công thức tích lũy: u_n = a * ((1+r)**n - 1) / r
                u_n = a * ((1 + r)**n - 1) / r

                # Tính tuổi con gái
                thang_thanh_nam = n / 12
                tuoi_con = tuoi_bat_dau + thang_thanh_nam

                # Tính kết quả: làm tròn số tiền tích lũy đến 2 chữ số thập phân (triệu đồng)
                # Dùng cho phần lời giải
                kq_tien = Decimal(float(u_n)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                # Đã có .replace('.',',') ở trên (Dòng 66)
                kq_tien_str = str(kq_tien).replace('.',',') 

                # Kết quả cần tìm: Tuổi con gái
                kq = str(int(tuoi_con))

                # --- CÁC ĐÁP ÁN TRẮC NGHIỆM ---
                # Đáp án đúng: tuổi con gái (số nguyên)
                da = kq 

                # Các đáp án sai: tuổi +1, +2, -1, -2
                s = [str(int(tuoi_con) + 1),
                     str(int(tuoi_con) + 2),
                     str(int(tuoi_con) - 1),
                     str(int(tuoi_con) - 2)
                    ]

                # Đảm bảo các đáp án sai không âm
                s = [d for d in s if int(d) > 0 and d != da] # Đảm bảo đáp án sai khác đáp án đúng

                # Chọn 3 đáp án sai ngẫu nhiên
                if len(s) < 3: # Xử lý nếu không đủ 3 đáp án sai hợp lệ
                    temp_set = {str(i) for i in range(1, int(tuoi_con) + 5)} - {da}
                    s = random.sample(list(temp_set), 3)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = (f'''Để tích lũy tiền cho việc học đại học của con gái, cô Hoa quyết định hàng tháng bỏ ${latex(a_nghin).replace('.', ',')}$ nghìn đồng vào tài khoản tiết kiệm, được trả lãi ${latex(r_percent).replace('.', ',')}$ phần trăm cộng dồn hàng tháng. Cô ấy sẽ tích lũy được một khoản tiền vào thời điểm gửi khoản tiền thứ ${latex(n).replace('.', ',')}$. Lúc này con gái cô Hoa bao nhiêu tuổi? (làm tròn kết quả đến hàng đơn vị).'''
                                 )

                # Các đáp án (lấy kết quả là tuổi con gái)
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Sử dụng f-string và format_latex_number)

                a_latex = latex(a).replace('.', ',')
                r_percent_latex = latex(r_percent).replace('.', ',')
                r_latex = latex(r).replace('.', ',')
                n_latex = latex(n).replace('.', ',')
                tuoi_bat_dau_latex = latex(tuoi_bat_dau).replace('.', ',')
                thang_thanh_nam_latex = latex(thang_thanh_nam).replace('.', ',')
                tuoi_con_latex = latex(tuoi_con).replace('.', ',')

                loigiai=(f'''Gọi số tiền gửi hàng tháng là $a = {a_latex}$ (triệu đồng), lãi suất hàng tháng $r = {r_percent_latex}\\% = {r_latex}$. Số lần gửi $n={n_latex}$.\\\\
                             Ta áp dụng công thức tính tổng số tiền tích lũy sau $n$ lần gửi (Lãi suất kép, gửi định kỳ):\\\\
                             $$u_n = a \\cdot \\frac{{(1+r)^n - 1}}{{r}}$$\\\\
                             Vào thời điểm gửi khoản tiền thứ ${n_latex}$, cô ấy sẽ tích lũy được: \\\\
                             $$u_{{{n_latex}}} = {a_latex} \\cdot \\frac{{(1+{r_latex})^{n_latex} - 1}}{{{r_latex}}} \\approx {kq_tien_str} \\text{{ (triệu đồng)}}$$\\\\
                             Khi đó, tuổi của con gái cô Hoa là: ${tuoi_bat_dau_latex} + \\frac{{{n_latex}}}{{12}} = {tuoi_bat_dau_latex} + {thang_thanh_nam_latex} = {tuoi_con_latex}$ (tuổi).
                             ''')
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(tuoi_con_latex))                

            # Xuất câu trắc nghiệm
            # Loại bỏ .0 cho các số nguyên sau khi đã chuyển sang dấu phẩy.
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ noidungcauhoi.replace(',0$', '$')+str(dapan)+
                '\\loigiai{'+str(loigiai).replace(',0$', '$')+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

