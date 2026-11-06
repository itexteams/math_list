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


def bt_dang36_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tham số k để tạo bài toán (Với bản gốc: k = 15 -> a = 45, b = 30)
                # Đặt a = 3k và khoảng khảo sát là [0; 2k] để đảm bảo tính thực tế của số ca nhiễm (luôn tăng)
                k = random.choice([10, 12, 14, 15, 16, 18, 20])
                a = 3 * k
                b = 2 * k

                # Các giá trị tính toán dùng cho lời giải
                a2 = 2 * a
                vk = 3 * k * k # Giá trị lớn nhất của V(t)
                vb = 0         # V(b) luôn bằng 0

                # Đáp án đúng
                kq = k

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Các phương án nhiễu
                s = ['$%s$'%(kq+1),
                     '$%s$'%(kq+2),
                     '$%s$'%(kq+3),
                     '$%s$'%(kq-1),
                     '$%s$'%(kq-2),
                     '$%s$'%(kq-3),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Sau khi phát hiện một bệnh dịch, các chuyên gia y tế ước tính số người nhiễm bệnh kể từ ngày xuất hiện bệnh nhân đầu tiên đến ngày thứ $t$ là $N(t) = %st^2 - t^3$, $0 \\le t \\le %s$ (người). Nếu xem $N'(t)$ là tốc độ truyền bệnh (người/ ngày) tại thời điểm $t$ thì tốc độ truyền bệnh lớn nhất sẽ vào ngày thứ bao nhiêu?'''
                                 %(latex(a), latex(b)
                                 ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Ta có số người nhiễm bệnh là $N(t) = %st^2 - t^3$ với $t \\in [0; %s]$. \\\\
                         Tốc độ truyền bệnh tại thời điểm $t$ là $V(t) = N'(t) = %st - 3t^2$. \\\\
                         Bài toán yêu cầu tìm giá trị lớn nhất của $V(t)$ trên đoạn $[0; %s]$. \\\\
                         Ta có đạo hàm $V'(t) = %s - 6t$. \\\\
                         Cho $V'(t) = 0 \\Leftrightarrow %s - 6t = 0 \\Leftrightarrow t = %s \\in [0; %s]$. \\\\
                         Ta tính các giá trị: $V(0) = 0$, $V(%s) = %s$, $V(%s) = %s$. \\\\
                         Suy ra $\\max_{[0; %s]} V(t) = V(%s) = %s$. \\\\
                         Vậy tốc độ truyền bệnh lớn nhất sẽ vào ngày thứ $%s$.'''
                         %(latex(a), latex(b),
                           latex(a2),
                           latex(b),
                           latex(a2),
                           latex(a2), latex(k), latex(b),
                           latex(k), latex(vk), latex(b), latex(vb),
                           latex(b), latex(k), latex(vk),
                           latex(k)
                         ))
            dapan='\\shortans[0]{$%s$}\n'%(latex(k))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content  

