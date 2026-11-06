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


def bt_dang15_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- RANDOM THAM SỐ CẤP SỐ CỘNG ---

                # 1. Số bậc (n): Kết quả cần tìm. Chọn từ 8 đến 15.
                n = randint(8, 15)       
                # 2. Công sai (d): Phải là số âm (chiều dài giảm dần). Chọn từ -5 đến -2.
                d = randint(-5, -2)      

                # 3. Số hạng đầu (u1): Chiều dài bậc dưới cùng. Lặp cho đến khi bậc cuối cùng (un) > 0.
                while True:
                    u1 = randint(40, 70) # Chiều dài bậc đầu tiên (cm)
                    un = u1 + (n-1)*d    # Chiều dài bậc cuối cùng (cm)
                    if un > 0 and un < u1 - 5: # Đảm bảo bậc cuối không quá gần bậc đầu
                        break

                kq = n # Kết quả là số bậc

                # --- TẠO ĐÁP ÁN TRẮC NGHIỆM ---

                # Đáp án đúng
                da = '$%s$'%(latex(kq))

                # Các đáp án sai
                s = ['$%s$'%(latex(kq+1)),
                     '$%s$'%(latex(kq+2)),
                     '$%s$'%(latex(kq+3)),
                     '$%s$'%(latex(kq-1)),
                     '$%s$'%(latex(kq-2)),
                     '$%s$'%(latex(kq-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---

                # Câu hỏi
                noidungcauhoi = ('''Một người muốn mua một thanh gỗ đủ để cắt ra làm các thanh ngang của một cái thang. Biết rằng chiều dài các thanh ngang của cái thang đó (từ bậc dưới cùng) lần lượt là $%s \\text{ cm}, %s \\text{ cm}, %s \\text{ cm},\\dots,%s \\text{ cm}$. \\\\
                                 Cái thang đó có bao nhiêu bậc?'''
                                 %(latex(u1), latex(u1+d), latex(u1+2*d), latex(un)
                                 ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai=('''Chiều dài các thanh ngang là dãy cấp số cộng có số hạng đầu là $u_1 = %s$, công sai là $d = %s$. \\\\
                             Số hạng tổng quát là $u_n = u_1 + (n-1)d = %s %s(n-1)$.\\\\
                             Chiều dài thanh cuối cùng là $u_n = %s$. Ta có phương trình: \\\\
                             $%s = %s + %s(n-1) \\Leftrightarrow %s(n-1) = %s - %s \\Leftrightarrow %s(n-1) = %s \\Leftrightarrow n-1 = %s \\Leftrightarrow n = %s$. \\\\
                             Vậy cái thang có $\\mathbf{%s}$ bậc.'''
                             %(latex(u1), latex(d),
                               latex(u1), latex(d),
                               latex(un),
                               latex(un), latex(u1), latex(d), latex(d), latex(un), latex(u1), latex(d), latex(un-u1), latex(int((un-u1)/d)), latex(kq),
                               latex(kq)
                             ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
            return content 

