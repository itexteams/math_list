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


def bt_dang39_p3_b1_c5_ds10(self):
            # Khai báo biến
            # Bài toán gốc: n nam, n nữ. Số cách xếp xen kẽ là: 2 * n! * n!
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng học sinh mỗi bên từ 2 đến 5 để con số không quá lớn
                n = random.randint(3, 5)

                # Tính toán các giá trị
                fact_n = math.factorial(n)
                kq_val = 2 * (fact_n**2)

                # Đáp án đúng
                kq = str(kq_val).replace('.', ',')

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    # Tạo các phương án sai dựa trên các lỗi thường gặp
                    sai1 = fact_n**2 # Quên nhân 2 trường hợp
                    sai2 = math.factorial(2 * n) # Hoán vị tất cả không xen kẽ
                    sai3 = 2 * fact_n # Quên bình phương factorial
                    sai4 = fact_n * (n**2)
                    sai5 = kq_val + random.randint(2, 10)
                    sai6 = kq_val // 2 if kq_val % 2 == 0 else kq_val + 5

                    candidates = [sai1, sai2, sai3, sai4, sai5, sai6]
                    val = random.choice(candidates)
                    if val != kq_val:
                        s.add(val)

                list_sai = list(s)
                das1 = str(list_sai[0]).replace('.', ',')
                das2 = str(list_sai[1]).replace('.', ',')
                das3 = str(list_sai[2]).replace('.', ',')

                # Bước 2: Viết lại nội dung câu hỏi (sử dụng %s)
                noidungcauhoi = ('''Có bao nhiêu cách sắp xếp $%s$ nữ sinh, $%s$ nam sinh thành một hàng dọc sao cho các bạn nam và nữ ngồi xen kẽ?'''
                                 % (latex(n), latex(n)))

                # Nội dung lời giải chi tiết (không viết tắt, sử dụng \left( \right))
                # Tạo chuỗi n! dưới dạng n.(n-1)...1 để giống ảnh mẫu
                chuoi_gt = ".".join([str(i) for i in range(n, 0, -1)])

                loigiai = ('''Có $2$ cách chọn vị trí cho $%s$ nam và $%s$ nữ ngồi xen kẽ (Trường hợp 1: Nam đứng đầu hàng, Trường hợp 2: Nữ đứng đầu hàng).\\\\
                             Xếp $%s$ nam sinh vào các vị trí cố định có: $%s = %s$ cách xếp.\\\\
                             Xếp $%s$ nữ sinh vào các vị trí cố định còn lại có: $%s = %s$ cách xếp.\\\\
                             Vậy tổng số cách sắp xếp thỏa mãn yêu cầu bài toán là: $2 \\cdot \\left( %s \\right)^{2} = %s$ cách xếp.'''
                           % (latex(n), latex(n), 
                              latex(n), chuoi_gt, latex(fact_n),
                              latex(n), chuoi_gt, latex(fact_n),
                              latex(fact_n), latex(kq_val)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))

                # Các đáp án
                da_d = ('\\True $%s$' % (kq))
                da_s1 = '$%s$' % (das1)
                da_s2 = '$%s$' % (das2)
                da_s3 = '$%s$' % (das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm (Không dùng tiền tố r, đúng cấu trúc minipage)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

