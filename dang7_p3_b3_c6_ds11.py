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


def bt_dang7_p3_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết lập số lượng bóng
                # Tổng số bóng cố định là 10 để n(Omega_1) = 45 giống trong ảnh
                tong_bong = 10
                n_omega_1 = math.comb(tong_bong, 2)
                n_omega_tong = n_omega_1**2

                # Chọn ngẫu nhiên số bóng xanh (x) và vàng (y)
                # Để C(x,2) và C(y,2) ra số nguyên đẹp, ta chọn x trong khoảng [3, 5]
                x = randint(3, 5)
                y = tong_bong - x

                n_x = math.comb(x, 2)
                n_y = math.comb(y, 2)

                # Xác suất chọn 2 bóng xanh và 2 bóng vàng trong 1 lần thử
                p_x_1 = Rational(n_x, n_omega_1)
                p_y_1 = Rational(n_y, n_omega_1)

                # Biến cố A: chọn được 4 quả bóng màu vàng (tức là mỗi lần đều được 2 quả vàng)
                # Xác suất P(A)
                p_a = p_y_1**2

                # Số kết quả thuận lợi n(A)
                kq_val = n_y**2
                kq = str(kq_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = kq_val + randint(-50, 50)
                    if sai != kq_val and sai > 0:
                        s.add('$%s$'%(latex(sai)))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong một hộp đựng $%s$ quả bóng gồm màu xanh và màu vàng. Các quả bóng có cùng kích thước và khối lượng. Chọn ngẫu nhiên $2$ quả bóng, xem màu rồi trả vào hộp. Lặp lại phép thử trên $2$ lần. Xác suất để chọn được $2$ quả bóng màu xanh là $%s$ và xác suất chọn được $2$ quả bóng màu vàng là $%s$. Số kết quả thuận lợi cho biến cố chọn được $4$ quả bóng màu vàng bằng bao nhiêu?'''
                                 %(latex(tong_bong), latex(p_x_1), latex(p_y_1)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Ta có $n\\left(\\Omega\\right) = C_{%s}^{2} \\cdot C_{%s}^{2} = %s \\cdot %s = %s$. \\\\
                            Gọi $A$ là biến cố chọn được $4$ quả bóng màu vàng. \\\\
                            Gọi $A_1$ là biến cố lần thứ nhất chọn được $2$ quả bóng màu vàng. \\\\
                            Gọi $A_2$ là biến cố lần thứ hai chọn được $2$ quả bóng màu vàng. \\\\
                            Khi đó, $A = A_1 A_2$ và $A_1, A_2$ là hai biến cố độc lập nhau. \\\\
                            Do đó, $P\\left(A\\right) = P\\left(A_1\\right) \\cdot P\\left(A_2\\right) = %s \\cdot %s = %s$. \\\\
                            Mà $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} \\Rightarrow n\\left(A\\right) = P\\left(A\\right) \\cdot n\\left(\\Omega\\right) = %s \\cdot %s = %s$.'''
                           %(latex(tong_bong), latex(tong_bong), latex(n_omega_1), latex(n_omega_1), latex(n_omega_tong),
                             latex(p_y_1), latex(p_y_1), latex(p_a),
                             latex(p_a), latex(n_omega_tong), latex(kq_val)))
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_val))  
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

