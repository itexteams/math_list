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


def bt_dang14_p4_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo danh sách dạng
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1-Nghiên cứu đề bài: M là trung điểm AB, A thuộc Ox, B thuộc Oy
                # Chọn tọa độ M(xm, ym) ngẫu nhiên
                xm = randint(1, 10)
                ym = randint(-10, 10)
                while ym == 0: # Tránh trường hợp M nằm trên trục hoành
                    ym = randint(-10, 10)

                # Tính tọa độ A(a, 0) và B(0, b)
                # Vì M là trung điểm AB: xm = (a+0)/2 => a = 2*xm; ym = (0+b)/2 => b = 2*ym
                a = 2 * xm
                b = 2 * ym

                # Phương trình đoạn chắn: x/a + y/b = 1
                # Chuyển sang phương trình tổng quát: b*x + a*y - a*b = 0
                # Rút gọn phương trình
                u = b # Hệ số x
                v = a # Hệ số y
                w = -a*b # Hệ số tự do

                common = math.gcd(math.gcd(u, v), w)
                # Đảm bảo hệ số x dương để nhìn đẹp hơn
                if u < 0:
                    common = -abs(common)
                else:
                    common = abs(common)

                u1, v1, w1 = u//common, v//common, w//common

                # Tạo phương trình tổng quát bằng sympy để hiển thị đẹp
                pt_tong_quat = Eq(u1*x + v1*y + w1, 0)
                da_dung = '$%s$' % latex(pt_tong_quat)

                # B4-Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = set()
                # Sai lầm 1: Quên nhân 2 (lấy tọa độ M làm tọa độ chắn)
                u_s1, v_s1, w_s1 = ym, xm, -xm*ym
                c1 = math.gcd(math.gcd(u_s1, v_s1), w_s1)
                s.add('$%s = 0$' % latex((ym//c1)*x + (xm//c1)*y + (-xm*ym//c1)))

                # Sai lầm 2: Nhầm tọa độ A thuộc Oy, B thuộc Ox (Hoán vị xm, ym)
                u_s2, v_s2, w_s2 = a, b, -a*b
                c2 = math.gcd(math.gcd(u_s2, v_s2), w_s2)
                s.add('$%s = 0$' % latex((a//c2)*x + (b//c2)*y + (-a*b//c2)))

                # Sai lầm 3: Sai dấu hệ số tự do
                s.add('$%s = 0$' % latex(u1*x + v1*y - w1))

                # Sai lầm 4: Sai dấu một trong hai hệ số biến
                s.add('$%s = 0$' % latex(u1*x - v1*y + w1))

                # Đảm bảo không trùng với đáp án đúng
                if da_dung in s:
                    s.remove(da_dung)

                # Chuyển set thành list và lấy 3 đáp án sai
                list_s = list(s)
                random.shuffle(list_s)
                das1 = list_s[0]
                das2 = list_s[1]
                das3 = list_s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Một đường thẳng đi qua điểm $M(%s;%s)$ cắt trục $Ox$ và $Oy$ lần lượt tại $A$ và $B$ sao cho $M$ là trung điểm của $AB$. Lập phương trình tổng quát của đường thẳng đó.'''
                                 %(latex(xm), latex(ym)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B2-Viết lại y hệt bài toán gồm đề bài và lời giải chi tiết
                loigiai = ('''Giả sử $A=(a;0), B=(0;b)$. Vì $M(%s;%s)$ là trung điểm của $AB$ nên \\\\
                             $\\begin{cases} %s = \\dfrac{a+0}{2} \\\\ %s = \\dfrac{0+b}{2} \\end{cases} \\Rightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$ \\\\
                             Phương trình của đường thẳng đi qua $A, B$ là $\\dfrac{x}{%s} + \\dfrac{y}{%s} = 1$ hay $%s$.'''
                           %(latex(xm), latex(ym), latex(xm), latex(ym), latex(a), latex(b), 
                             latex(a), latex(b), latex(pt_tong_quat)
                            ))

            # Xuất câu trắc nghiệm - Không dùng tiền tố r (raw string)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

