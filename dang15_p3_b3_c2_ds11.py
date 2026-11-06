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


def bt_dang15_p3_b3_c2_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Random các tham số
                # Nhiệt độ ban đầu (T0) - Chọn ngẫu nhiên nhiệt độ ban đầu trong khoảng 20 đến 30 độ C
                T0 = random.randint(20, 30) 
                # Phần trăm giảm mỗi giờ (p%) - chọn ngẫu nhiên 10%, 15%, 20%, 25%, 30%
                p = random.choice([10, 15, 20, 25, 30]) 
                # Thời gian (số giờ) (t_gio) - chọn ngẫu nhiên 5 đến 8 giờ
                t_gio = random.randint(5, 8) 

                # 2. Tính toán kết quả
                # Công bội q (tỷ lệ còn lại sau mỗi giờ)
                q = 1 - p/100 
                # Nhiệt độ sau t_gio là T_t = T0 * q^t_gio
                kq_chinhxac = T0 * (q)**t_gio

                # Làm tròn kết quả về 1 chữ số thập phân (đáp án chính xác)
                kq3 = Decimal(float(kq_chinhxac)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq3).replace('.',',')
                kq = '$%s$'%(kq_str) # Đáp án chính xác (chuẩn LaTeX)
                kq_round = round(kq_chinhxac, 1) # Đáp án làm tròn để tạo phương án sai

                # 3. Tạo các đáp án trắc nghiệm sai
                # Tạo danh sách các giá trị sai
                s = [round(kq_round + 1.0, 1),
                     round(kq_round + 0.5, 1),
                     round(kq_round - 1.0, 1),
                     round(kq_round - 0.5, 1),
                    ]
                # Chuyển sang định dạng LaTeX và lọc bỏ các đáp án trùng hoặc không hợp lệ (ví dụ <= 0)
                s_latex = []
                for val in s:
                    if val > 0 and abs(val - kq_round) > 0.05: # Loại trừ giá trị quá gần đáp án đúng
                        s_latex.append('$%s$'%(latex(val)).replace('.',','))

                # Đảm bảo có đủ 3 đáp án sai (nếu không đủ, dùng các giá trị mặc định)
                s_latex = list(set(s_latex))
                while len(s_latex) < 3:
                    if ('$%s$'%(latex(round(kq_round + 2.0, 1))).replace('.',',') not in s_latex):
                        s_latex.append('$%s$'%(latex(round(kq_round + 2.0, 1))).replace('.',','))
                    elif ('$%s$'%(latex(round(kq_round - 2.0, 1))).replace('.',',') not in s_latex):
                        s_latex.append('$%s$'%(latex(round(kq_round - 2.0, 1))).replace('.',','))
                    s_latex = list(set(s_latex))
                    if len(s_latex) >= 3:
                        break

                da_s1 = s_latex.pop(random.randrange(len(s_latex)))
                da_s2 = s_latex.pop(random.randrange(len(s_latex)))
                da_s3 = s_latex.pop(random.randrange(len(s_latex)))

                # 4. Câu hỏi
                noidungcauhoi = ('''Một khay nước có nhiệt độ $%s^\\circ C$ được đặt vào ngăn đá của tủ lạnh. Biết sau mỗi giờ, nhiệt độ của nước giảm $%s \\%%$. Nhiệt độ của khay nước đó sau $%s$ giờ theo đơn vị độ $C$ là bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 %(latex(T0), latex(p), latex(t_gio)))

                # 5. Các đáp án
                da_d = ('\\True ' +str(kq))
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # 6. Nội dung lời giải
                loigiai=('''Gọi $T_n$ là nhiệt độ của khay nước sau $n$ giờ ($n \\in \\mathbb{N}^*$). \\\\
                         Nhiệt độ giảm $%s \\%%$ mỗi giờ, nên nhiệt độ còn lại là $100 \\%% - %s \\%% = %s \\%% = %s$. \\\\
                         Nhiệt độ ban đầu là $T_0 = %s^\\circ C$. \\\\
                         Dãy nhiệt độ sau mỗi giờ tạo thành một cấp số nhân với công bội $q = %s$. \\\\
                         Công thức tổng quát: $T_n = T_0 \\cdot q^n = %s \\cdot (%s)^n$ (độ $C$). \\\\
                         Nhiệt độ của khay nước đó sau $%s$ giờ là: \\\\
                         $T_{%s} = %s \\cdot (%s)^{%s} \\approx %s^\\circ C$.'''
                         %(latex(p), latex(p), latex(100-p), latex(q),
                           latex(T0),
                           latex(q),
                           latex(T0), latex(q),
                           latex(t_gio),
                           latex(t_gio), latex(T0), latex(q), latex(t_gio), kq))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))  

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')               
            return content 

