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


def bt_dang26_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 🎲 Random hóa tham số
                t = random.choice([5, 10, 20]) # Cạnh viên gạch (cm)

                # Random số viên gạch u1 và un (u1 > un và đảm bảo đủ chỗ cho ít nhất 5 hàng)
                u1 = randint(20, 40) # Số viên gạch hàng đáy lớn (u1)
                un = randint(5, u1 - 5) # Số viên gạch hàng đáy nhỏ (un)

                # Công sai: -1 (ít hơn 1 viên) hoặc -2 (ít hơn 2 viên)
                d = random.choice([-1, -2]) 

                # Đảm bảo số hàng n là số nguyên dương
                if (un - u1) % d != 0:
                    un = u1 + d * randint(5, 15)
                    # Nếu un vẫn âm sau khi tính toán, đảm bảo un > 0
                    while un <= 0:
                        un = u1 + d * randint(5, 15)

                # Tính toán A và B từ u1, un, t
                A = u1 * t # Chiều rộng đáy lớn (cm)
                B = un * t # Chiều rộng đáy nhỏ (cm)

                # 💡 Tính toán kết quả
                n = int((un - u1)/d + 1) # Số hàng
                kq = int(n*(u1 + un)/2) # Tổng số viên gạch

                # Kết quả
                kq_str = str(kq)

                # ✅ Đáp án đúng
                du = ['$%s$'%(kq_str)]
                da = random.choice(du)

                # ❌ Tạo các đáp án nhiễu (sai)
                s = []
                # Thêm các đáp án nhiễu dựa trên kết quả
                s.append('$%s$'%(kq + d * 3))
                s.append('$%s$'%(kq - d * 3))
                s.append('$%s$'%(kq + d * 2))
                s.append('$%s$'%(kq - d * 2))

                # Thêm các đáp án nhiễu ngẫu nhiên khác để đảm bảo tính đa dạng
                for _ in range(3):
                    nhiu = randint(kq - 10, kq + 10)
                    if nhiu != kq:
                        s.append('$%s$'%(nhiu))

                # Loại bỏ các đáp án trùng lặp và đảm bảo có đủ 3 đáp án nhiễu
                s = list(set(s))

                # Chọn ngẫu nhiên 3 đáp án nhiễu
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # ❓ Câu hỏi
                # Lấy giá trị tuyệt đối cho d trong câu hỏi
                noidungcauhoi = ('''Một bức tường trang trí có dạng hình thang, rộng $%s\\text{ m}$ ở đáy và rộng $%s\\text{ m}$ ở đỉnh. Các viên gạch hình vuông kích thước $%s\\text{ cm}\\times %s\\text{ cm}$ phải đặt sao cho mỗi hàng ở phía trên chứa ít hơn $%s$ viên so với hàng ở ngay phía dưới đó. Hỏi cần bao nhiêu viên gạch hình vuông như vậy để ốp hết bức tường đó?'''
                                  %(latex(Rational(A,100)),latex(Rational(B,100)),latex(t),latex(t),latex(abs(d))
                                  ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # ✍️ Nội dung lời giải
                loigiai=('''Đổi đơn vị: $%s\\text{ m} = %s\\text{ cm}$; $%s\\text{ m} = %s\\text{ cm}$. \\\\
                          Số viên gạch ở hàng đầu tiên (ứng với đáy lớn) là: $u_1 = \\frac{%s}{%s} = %s$ (viên). \\\\
                          Số viên gạch ở hàng trên cùng (ứng với đáy nhỏ) là: $u_n = \\frac{%s}{%s} = %s$ (viên). \\\\
                          Vì mỗi hàng ở phía trên chứa ít hơn $|%s|$ viên so với hàng ở ngay phía dưới đó nên ta thu được cấp số cộng có công sai $d = %s$. \\\\
                          Áp dụng công thức số hạng tổng quát: $u_n = u_1 + (n-1)d$ để tìm số hàng $n$: \\\\
                          $%s = %s + (n-1)(%s) \\Rightarrow n = %s$. \\\
                          Vậy số viên gạch hình vuông cần thiết để ốp hết bức tường đó là: \\\\
                          $S_{%s} = \\frac{(u_1 + u_n)n}{2} = \\frac{(%s + %s)%s}{2} = %s$ (viên gạch).'''

                        %(latex(A/100),latex(A),latex(B/100),latex(B),
                          latex(A),latex(t),latex(u1),
                          latex(B),latex(t),latex(un),
                          latex(d),latex(d),
                          latex(un),latex(u1),latex(d),latex(n),
                          latex(n),latex(u1),latex(un),latex(n),latex(kq)
                        ))
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(kq))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

