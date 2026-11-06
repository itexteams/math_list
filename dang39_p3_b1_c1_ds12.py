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


def bt_dang39_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết lập các trường hợp dữ liệu ngẫu nhiên phù hợp với bài toán thực tế
                case = random.choice([1, 2, 3, 4])
                if case == 1:
                    V0, m0, cin = 10, 2, 1.5
                    B_str = "0,0013"
                    B_val = 0.0013
                elif case == 2:
                    V0, m0, cin = 10, 5, 2.0
                    B_str = "0,0015"
                    B_val = 0.0015
                elif case == 3:
                    V0, m0, cin = 10, 3, 1.8
                    B_str = "0,0015"
                    B_val = 0.0015
                else:
                    V0, m0, cin = 10, 4, 2.2
                    B_str = "0,0018"
                    B_val = 0.0018

                # Tính toán giá trị cực đại chính xác
                u_cube = cin / (4 * B_val)
                u_max = u_cube ** (1/3)
                max_val = cin * u_max - B_val * (u_max ** 4)

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân) theo quy định định dạng dấu phẩy
                max_val_dec = Decimal(str(max_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(max_val_dec).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Tạo danh sách các phương án nhiễu không trùng lặp
                s = set()
                for diff in [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 1.2, -1.2]:
                    val = float(max_val_dec) + diff
                    if val > 0:
                        val_dec = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                        val_str = str(val_dec).replace('.', ',')
                        if val_str != kq:
                            s.add('$%s$' % val_str)

                s_list = list(s)
                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Chuyển đổi định dạng số để hiển thị trong đề bài
                cin_str = str(cin).replace('.', ',')
                m0_str = str(m0).replace('.', ',')

                # Câu hỏi
                noidungcauhoi = ('''Một bể ban đầu chứa $%s$ gal dung dịch muối với $%s$ lb muối. Dung dịch vào có nồng độ $%s$ lb/gal chảy vào với tốc độ $3$ gal/phút, và hỗn hợp trong bể chảy ra với tốc độ $4$ gal/phút. Người ta cho biết lượng muối trong bể sau $t$ phút là $x$ (pound), với: $x = f(t) = %s(10-t) - %s(10-t)^4$, $0 \\le t \\le 10$. Hỏi lượng muối tối đa có thể có trong bể tại một thời điểm nào đó là bao nhiêu lb? (làm tròn kết quả đến hàng phần trăm)'''
                                 %(latex(V0), latex(m0), cin_str, cin_str, B_str
                                 ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Tính toán các thông số trung gian cho lời giải chi tiết
                u3_str = str(round(u_cube, 2)).replace('.', ',')
                u_str = str(round(u_max, 3)).replace('.', ',')
                g_der_b = str(4 * B_val).replace('.', ',')

                # Nội dung lời giải
                loigiai=('''Xét hàm số biểu thị lượng muối trong bể sau $t$ phút là $f(t) = %s(10-t) - %s(10-t)^4$ với $t \\in [0; 10]$. \\\\
                         Đặt $u = 10-t$. Vì $0 \\le t \\le 10$ nên $u \\in [0; 10]$. \\\\
                         Hàm số trở thành: $g(u) = %su - %su^4$ trên đoạn $[0; 10]$. \\\\
                         Ta có đạo hàm: $g'(u) = %s - %su^3$. \\\\
                         Cho $g'(u) = 0 \\Leftrightarrow %s - %su^3 = 0 \\Leftrightarrow u^3 = %s \\Leftrightarrow u \\approx %s \\in [0; 10]$. \\\\
                         Ta thấy $g'(u)$ đổi dấu từ dương sang âm khi đi qua điểm $u \\approx %s$ nên hàm số đạt giá trị lớn nhất tại điểm này. \\\\
                         Giá trị lớn nhất của lượng muối trong bể là: \\\\
                         $\\max_{[0; 10]} g(u) = g(%s) = %s \\cdot %s - %s \\cdot (%s)^4 \\approx %s$ lb. \\\\
                         Vậy lượng muối tối đa có thể có trong bể xấp xỉ $%s$ lb.'''
                         %(cin_str, B_str,
                           cin_str, B_str,
                           cin_str, g_der_b,
                           cin_str, g_der_b, u3_str, u_str,
                           u_str,
                           u_str, cin_str, u_str, B_str, u_str, kq,
                           kq
                         ))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content  

