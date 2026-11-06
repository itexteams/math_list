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


def bt_dang17_p1_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo ngẫu nhiên giá tiền hoa hồng, hoa ly và doanh thu tối thiểu
                # Giá hoa hồng từ 50000 đến 100000 (bước 10000)
                gia_hong = randint(5, 10) * 10000
                # Giá hoa ly từ 110000 đến 150000 (bước 10000)
                gia_ly = randint(11, 15) * 10000

                # Doanh thu tối thiểu (triệu đồng), chọn từ 20 đến 40 triệu
                doanh_thu_trieu = randint(20, 40)
                doanh_thu_dong = doanh_thu_trieu * 1000000

                # Rút gọn hệ số của bất phương trình: gia_hong * x + gia_ly * y >= doanh_thu_dong
                # Tìm ước chung lớn nhất để tối giản hệ số
                ucln = math.gcd(math.gcd(gia_hong, gia_ly), doanh_thu_dong)

                a = gia_hong // ucln
                b = gia_ly // ucln
                c = doanh_thu_dong // ucln

                # Đáp án đúng
                da_dung = '$%sx + %sy \\ge %s$' % (latex(a), latex(b), latex(c))

                # Tạo các phương án sai ngẫu nhiên và đảm bảo không trùng với đáp án đúng
                s = []
                # Phương án đổi dấu bất đẳng thức
                s.append('$%sx + %sy > %s$' % (latex(a), latex(b), latex(c)))
                s.append('$%sx + %sy \\le %s$' % (latex(a), latex(b), latex(c)))
                # Phương án đảo vị trí hệ số x và y
                if a != b:
                    s.append('$%sx + %sy \\ge %s$' % (latex(b), latex(a), latex(c)))
                    s.append('$%sx + %sy \\le %s$' % (latex(b), latex(a), latex(c)))

                # Điền thêm một số phương án nhiễu khác nếu chưa đủ 5 phương án để chọn ngẫu nhiên
                s.append('$%sx + %sy \\ge %s$' % (latex(a), latex(b), latex(c + 50)))
                s.append('$%sx + %sy \\ge %s$' % (latex(a), latex(b), latex(abs(c - 50))))

                # Lọc bỏ phần tử trùng với đáp án đúng (nếu có)
                s = [item for item in s if item != da_dung]

                # Chọn ra 3 đáp án sai phân biệt
                s_distinct = list(set(s))
                random.shuffle(s_distinct)

                das1 = s_distinct[0]
                das2 = s_distinct[1]
                das3 = s_distinct[2]

                # Câu hỏi
                noidungcauhoi = ('''Ông Minh trồng hai loại hoa gồm hoa hồng và hoa ly để bán vào dịp Tết Nguyên Đán. Hoa hồng có giá $%s$ đồng/chậu và hoa ly có giá $%s$ đồng/chậu. Ông Minh tính toán rằng, để không phải bù lỗ thì số tiền bán hoa thu được phải đạt tối thiểu $%s$ triệu đồng. Gọi $x$ và $y$ lần lượt là số chậu hoa hồng và hoa ly bán được. Hỏi $x$ và $y$ thỏa mãn điều kiện nào dưới đây thì ông Minh không phải bù lỗ.'''
                                 % (latex(gia_hong), latex(gia_ly), latex(doanh_thu_trieu)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $x$ và $y$ lần lượt là số chậu hoa hồng và hoa ly bán được. Điều kiện $x, y \\in \\mathbb{N}$.\\\\
                             Khi đó số tiền bán hoa thu được là $%sx + %sy$ (đồng).\\\\
                             Để không phải bù lỗ thì số tiền bán hoa thu được phải đạt tối thiểu $%s$ đồng nên\\\\
                             $\\quad %sx + %sy \\ge %s$\\\\
                             $\\Leftrightarrow %sx + %sy \\ge %s$.'''
                           % (latex(gia_hong), latex(gia_ly), latex(doanh_thu_dong),
                              latex(gia_hong), latex(gia_ly), latex(doanh_thu_dong),
                              latex(a), latex(b), latex(c)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

