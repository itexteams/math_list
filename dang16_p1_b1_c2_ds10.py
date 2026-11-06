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


def bt_dang16_p1_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số tiền tổng cộng (nghìn đồng) và giá tiền 2 loại vở (đồng)
                # Đảm bảo g2 > g1 để thuật toán tìm số vở lớn nhất ưu tiên loại I
                g1 = randint(3, 5) * 1000 # Giá vở loại I: 3000, 4000, 5000
                g2 = g1 + randint(1, 3) * 1000 # Giá vở loại II lớn hơn loại I

                # Random tổng số tiền sao cho đủ mua mỗi loại ít nhất 1 quyển và không quá lớn
                T = randint(20, 40) # Tổng số tiền (nghìn đồng)
                tong_tien_dong = T * 1000

                # Rút gọn hệ số để đưa vào bất phương trình ax + by <= c
                a = g1 // 1000
                b = g2 // 1000
                c = T

                # Tìm tập nghiệm (x, y) nguyên dương sao cho ax + by <= c và x + y đạt Max
                tap_nghiem = []
                max_vở = 0

                for y_val in range(1, c // b + 1):
                    for x_val in range(1, (c - b * y_val) // a + 1):
                        if a * x_val + b * y_val <= c:
                            tap_nghiem.append((x_val, y_val))
                            if (x_val + y_val) > max_vở:
                                max_vở = x_val + y_val

                # Lọc ra các bộ nghiệm cho số vở lớn nhất để viết vào bảng nghiệm lời giải
                cac_bo_max = [cap for cap in tap_nghiem if cap[0] + cap[1] == max_vở]

                # Tạo chuỗi dòng x và dòng y cho bảng nghiệm trong lời giải (lấy tối đa 3 cặp nghiệm tiêu biểu)
                hien_thi_nghiem = tap_nghiem[:3] if len(tap_nghiem) > 3 else tap_nghiem
                str_x = ""
                str_y = ""
                for cap in hien_thi_nghiem:
                    str_x += " & %s" % (cap[0])
                    str_y += " & %s" % (cap[1])

                kq4 = max_vở

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(latex(kq4))]
                da = random.choice(du)

                s = ['$%s$'%(latex(kq4+1)),
                     '$%s$'%(latex(kq4+2)),
                     '$%s$'%(latex(kq4+3)),
                     '$%s$'%(latex(kq4-1)) if kq4-1 > 2 else '$%s$'%(latex(kq4+4)),
                     '$%s$'%(latex(kq4-2)) if kq4-2 > 2 else '$%s$'%(latex(kq4+5)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Bạn Lan có $%s$ nghìn đồng để đi mua vở. Vở loại I có giá $%s$ đồng một cuốn, vở loại II có giá $%s$ đồng một cuốn. Hỏi bạn Lan có thể mua nhiều nhất bao nhiêu quyển vở sao cho bạn có cả hai loại vở?'''
                                 %(latex(T), latex(g1), latex(g2)))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Gọi số vở Loại I, Loại II bạn Lan có thể mua lần lượt là $x, y$ (quyển), $x, y \\in \\mathbb{N}^*$.\\\\
                         Theo đề bài ta có $%sx + %sy \\le %s$.\\\\
                         Bảng nghiệm thỏa mãn:\\\\
                         \\begin{tabular}{|c|%s|}\\hline
                         $x$ %s \\\\\\hline
                         $y$ %s \\\\\\hline
                         \\end{tabular}\\\\
                         Vậy bạn Lan có thể mua nhiều nhất $%s$ quyển vở.'''
                         %(latex(a), latex(b), latex(c),
                           "c|".join(["" for _ in range(len(hien_thi_nghiem) + 1)]),
                           str_x, str_y, latex(kq4)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

