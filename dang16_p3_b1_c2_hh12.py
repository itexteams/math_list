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


def bt_dang16_p3_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1 & 3: Thiết lập thông số và Random bài toán
                # Để đảm bảo có vùng phủ sóng trên Oxy, khoảng cách từ A đến Oxy (h = |zA|) phải nhỏ hơn R
                zA = randint(1, 5)
                xA = randint(-5, 5)
                yA = randint(-5, 5)
                # Bán kính R của máy phát phải lớn hơn khoảng cách zA
                R = zA + randint(1, 4)

                h = abs(zA)
                r_binh_phuong = R**2 - h**2
                kq_sym = sqrt(r_binh_phuong)

                # Đáp án đúng
                da = '$' + latex(kq_sym) + '$'

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s_list = []
                # Sai lầm 1: Tính nhầm thành cộng (Pitago ngược)
                val1 = sqrt(R**2 + h**2)
                s_list.append('$' + latex(val1) + '$')

                # Sai lầm 2: Lấy luôn bán kính R ban đầu
                s_list.append('$' + latex(R) + '$')

                # Sai lầm 3: Lấy khoảng cách h
                s_list.append('$' + latex(h) + '$')

                # Sai lầm 4: Một giá trị ngẫu nhiên khác
                s_list.append('$' + latex(sqrt(abs(R**2 - 2*h))) + '$')

                # Lọc trùng và loại đáp án đúng nếu lỡ trùng
                s_list = list(set(s_list))
                if da in s_list:
                    s_list.remove(da)

                # Đảm bảo đủ 3 đáp án sai
                while len(s_list) < 3:
                    temp_val = randint(2, 10)
                    temp_str = '$' + latex(sqrt(temp_val)) + '$'
                    if temp_str != da and temp_str not in s_list:
                        s_list.append(temp_str)

                das1 = random.choice(s_list)
                s_list.remove(das1)
                das2 = random.choice(s_list)
                s_list.remove(das2)
                das3 = random.choice(s_list)

                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, một máy phát sóng đặt tại vị trí $A(%s; %s; %s)$ và có bán kính phủ sóng là $%s$. Bán kính vùng phủ sóng trên mặt phẳng $(Oxy)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                                 %(latex(xA), latex(yA), latex(zA), latex(R)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Nội dung lời giải chi tiết (không viết tắt)
                h1=kq_sym
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                loigiai = ('Ta có khoảng cách từ điểm $A(%s; %s; %s)$ đến mặt phẳng $(Oxy)$ là $h = d(A, (Oxy)) = |z_A| = %s$. \\\\'
                           'Bán kính đường tròn là giao tuyến của mặt cầu tâm $A$, bán kính bằng $R = %s$ với mặt phẳng $(Oxy)$ được tính theo công thức: \\\\'
                           '$r = \\sqrt{R^2 - h^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s} = %s$. \\\\'
                           'Vậy bán kính vùng phủ sóng trên mặt phẳng $(Oxy)$ bằng $%s \\approx %s$.'
                           %(latex(xA), latex(yA), latex(zA), latex(h), 
                             latex(R), 
                             latex(R), latex(h), latex(r_binh_phuong), latex(kq_sym),
                             latex(kq_sym), str(kqz)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kqz).replace('.', ','))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

