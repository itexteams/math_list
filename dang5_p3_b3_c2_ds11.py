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


def bt_dang5_p3_b3_c2_ds11(self):
            # Khai báo biến
            # --- KHAI BÁO BIẾN CHO BÀI TOÁN BUNGEE (RANDOM) ---
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các hằng số
                a1 = randint(10, 150)       # Quãng đường rơi ban đầu (m)
                q_ptram = randint(60, 90)   # Tỉ lệ so với lần trước (%) (60% đến 90%)
                n = randint(5, 15)          # Số lần kéo lên và rơi xuống

                # Chuyển tỉ lệ sang số thập phân
                q = Rational(q_ptram, 100)
                q_float = float(q)

                # Tính tổng n số hạng đầu của CSN: Sn = a1 * (1 - q^n) / (1 - q)
                mau = 1 - q
                tu = a1 * (1 - q**n)
                kq_chinhxac = tu / mau

                # Làm tròn kết quả đến 1 chữ số thập phân
                kq_decimal = Decimal(float(kq_chinhxac)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq_lamtron_str = str(kq_decimal).replace('.',',')
                kq_lamtron_float = float(kq_decimal) # Giá trị làm tròn

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_lamtron_str), # Đáp án đúng
                      ]
                da = random.choice(du)

                # Tạo các đáp án sai gần đáp án đúng
                # (Đảm bảo các đáp án sai khác nhau và khác đáp án đúng)
                s = []
                while len(s) < 3:
                    # Tạo ngẫu nhiên một sai số (ví dụ: -2, -1.5, -1, 1, 1.5, 2, ...)
                    delta = random.choice([-2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2])
                    dap_an_sai = round(kq_lamtron_float + delta, 1)

                    # Chuyển sang chuỗi định dạng LaTeX và thay '.' bằng ','
                    das_str = '$%s$'%(latex(dap_an_sai)).replace('.',',')

                    if das_str not in s and das_str != da:
                        s.append(das_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một người nhảy bungee (một trò chơi mạo hiểm mà người chơi nhảy từ nơi có địa thế cao xuống với dây đai an toàn buộc xung quanh người) từ một cây cầu và căng sợi dây dài $%s$ m. Sau mỗi lần rơi xuống, người nhảy được kéo lên một quãng đường có độ dài bằng $%s$$\\%%$ so với lần rơi trước đó và lại bị rơi xuống đúng bằng quãng đường vừa được kéo lên. Tổng quãng đường người đó rơi xuống sau $%s$ lần rơi bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                 %(latex(a1),latex(q_ptram),latex(n)
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
                loigiai=('''Quãng đường rơi lần đầu là $a_1 = %s$ m.\\\\
                          Quãng đường kéo lên và rơi xuống sau mỗi lần bằng $q = %s$$\\%%$ $= %s$ lần quãng đường rơi trước đó.\\\\
                          Dãy các quãng đường rơi tạo thành một Cấp số nhân với số hạng đầu $a_1 = %s$ và công bội $q = %s$.\\\\
                          Tổng quãng đường người đó rơi xuống sau $%s$ lần rơi được tính theo công thức tổng của $%s$ số hạng đầu của cấp số nhân:
                          $$S_{%s} = a_1 \\cdot \\frac{1 - q^{%s}}{1 - q}$$
                          $$S_{%s} = %s \\cdot \\frac{1 - (%s)^{%s}}{1 - %s} \\approx %s \\text{ (m)}.$$ '''
                         %(latex(a1),latex(q_ptram),latex(q),
                           latex(a1),latex(q),
                           latex(n),latex(n),
                           latex(n),latex(n),
                           latex(n),latex(a1),latex(q),latex(n),latex(q),
                           kq_lamtron_str
                         ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_lamtron_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

