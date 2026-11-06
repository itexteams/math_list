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


def bt_dang51_p4_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random bài toán
                # Chọn số học sinh nữ từ 5 đến 7, nam từ 6 đến 8 để đảm bảo số cách chọn phong phú
                nu = randint(5, 7)
                nam = randint(6, 8)
                chon = 5
                tong_hs = nu + nam

                # Tính toán các giá trị tổ hợp
                # Tổng số cách chọn k học sinh bất kỳ: C(tong, k)
                c_tong = math.comb(tong_hs, chon)
                # Số cách chọn toàn nữ: C(nu, k)
                c_nu = math.comb(nu, chon)
                # Số cách chọn toàn nam: C(nam, k)
                c_nam = math.comb(nam, chon)

                # Kết quả bài toán: Tổng - (Toàn nữ + Toàn nam)
                kq_chinh_thuc = c_tong - (c_nu + c_nam)

                # Đáp án đúng
                da = '$%s$' % (latex(kq_chinh_thuc))

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Tạo các phương án nhiễu như: tổng cách chọn, chỉ trừ nam, hoặc sai lệch đơn vị
                    nhieu = random.choice([
                        c_tong, 
                        c_tong - c_nu, 
                        c_tong - c_nam, 
                        kq_chinh_thuc + randint(1, 10), 
                        kq_chinh_thuc - randint(1, 10)
                    ])
                    if nhieu != kq_chinh_thuc:
                        s.add('$%s$' % (latex(nhieu)))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Một tổ có $%s$ học sinh nữ và $%s$ học sinh nam. Tìm số cách chọn ngẫu nhiên $%s$ học sinh của tổ trong đó có cả học sinh nam và học sinh nữ.'''
                                 %(latex(nu), latex(nam), latex(chon)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Tổng số học sinh của tổ là $%s + %s = %s$ học sinh.\\\\
                             Chọn $%s$ học sinh bất kỳ từ tổ $%s$ học sinh có số cách chọn là $C_{%s}^{%s} = %s$.\\\\
                             Số cách chọn $%s$ học sinh mà chỉ toàn học sinh nữ là $C_{%s}^{%s} = %s$.\\\\
                             Số cách chọn $%s$ học sinh mà chỉ toàn học sinh nam là $C_{%s}^{%s} = %s$.\\\\
                             Số cách chọn ngẫu nhiên $%s$ học sinh của tổ trong đó có cả học sinh nam và học sinh nữ là\\\\
                             $C_{%s}^{%s} - \\left( C_{%s}^{%s} + C_{%s}^{%s} \\right) = %s - \\left( %s + %s \\right) = %s$.'''
                           %(latex(nu), latex(nam), latex(tong_hs),
                             latex(chon), latex(tong_hs), latex(tong_hs), latex(chon), latex(c_tong),
                             latex(chon), latex(nu), latex(chon), latex(c_nu),
                             latex(chon), latex(nam), latex(chon), latex(c_nam),
                             latex(chon),
                             latex(tong_hs), latex(chon), latex(nu), latex(chon), latex(nam), latex(chon),
                             latex(c_tong), latex(c_nu), latex(c_nam), latex(kq_chinh_thuc)
                            ))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

