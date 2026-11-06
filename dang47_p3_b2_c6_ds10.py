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


def bt_dang47_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random số lượng bi
                nx = randint(4, 8) # Số bi xanh
                nt = randint(3, 6) # Số bi trắng
                tong = nx + nt     # Tổng số bi
                tong_con_lai = tong - 1

                # Tính toán kết quả
                # Xác suất lần 1: nx/tong
                # Xác suất lần 2: nt/(tong-1)
                tuso = nx * nt
                mauso = tong * tong_con_lai
                kq_phan_so = Rational(tuso, mauso)

                # Đáp án đúng
                da = '$%s$' % (latex(kq_phan_so))

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                # Sai lầm 1: Lấy mẫu số là tong*tong (có hoàn lại)
                sai1 = Rational(nx * nt, tong * tong)
                # Sai lầm 2: Lấy cùng màu xanh cả 2 lần
                sai2 = Rational(nx * (nx - 1), tong * tong_con_lai)
                # Sai lầm 3: Lấy cùng màu trắng cả 2 lần
                sai3 = Rational(nt * (nt - 1), tong * tong_con_lai)
                # Sai lầm 4: Tổng các bi chia cho số cách chọn
                sai4 = Rational(nx + nt, tong * tong_con_lai)

                list_sai = [sai1, sai2, sai3, sai4]
                for i in list_sai:
                    val = '$%s$' % (latex(i))
                    if val != da and val not in s:
                        s.append(val)

                # Bổ sung nếu thiếu phương án do trùng lặp
                while len(s) < 3:
                    fake = Rational(randint(1, 10), randint(11, 40))
                    val_fake = '$%s$' % (latex(fake))
                    if val_fake != da and val_fake not in s:
                        s.append(val_fake)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Bước 2: Viết lại nội dung câu hỏi
                noidungcauhoi = ('''Một hộp có $%s$ viên bi xanh và $%s$ viên bi trắng. Lấy ngẫu nhiên hai lần, mỗi lần một viên bi. Xác suất để lần thứ nhất lấy được viên bi xanh, lần thứ hai lấy được viên bi trắng bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                %(latex(nx), latex(nt)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                h1=kq_phan_so
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')
                # Nội dung lời giải chi tiết (Không viết tắt, dùng \left \right)
                loigiai = ('''Tổng số viên bi trong hộp là $%s + %s = %s$ viên bi. \\\\
                             Xác suất lần thứ nhất lấy được viên bi xanh là $\\frac{C_{%s}^1}{C_{%s}^1} = \\frac{%s}{%s}$. \\\\
                             Sau khi lấy một viên bi xanh ở lần thứ nhất, trong hộp còn lại $%s$ viên bi, trong đó có $%s$ viên bi trắng. \\\\
                             Xác suất lần thứ hai lấy được viên bi trắng là $\\frac{C_{%s}^1}{C_{%s}^1} = \\frac{%s}{%s}$. \\\\
                             Vậy xác suất để lần thứ nhất lấy được viên bi xanh, lần thứ hai lấy được viên bi trắng là:
                             $$\\frac{C_{%s}^1}{C_{%s}^1} \\cdot \\frac{C_{%s}^1}{C_{%s}^1} = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = %s \\approx %s. $$'''
                          %(latex(nx), latex(nt), latex(tong),
                            latex(nx), latex(tong), latex(nx), latex(tong),
                            latex(tong_con_lai), latex(nt),
                            latex(nt), latex(tong_con_lai), latex(nt), latex(tong_con_lai),
                            latex(nx), latex(tong), latex(nt), latex(tong_con_lai),
                            latex(nx), latex(tong), latex(nt), latex(tong_con_lai),
                            latex(kq_phan_so), kqz))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))
            # Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

