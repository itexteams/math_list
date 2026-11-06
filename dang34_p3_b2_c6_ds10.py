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


def bt_dang34_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng hành khách và số toa tàu (từ 4 đến 5)
                n_khach = randint(4, 5)
                n_toa = n_khach 

                # Tính không gian mẫu: mỗi hành khách có n_toa cách chọn
                n_omega = n_toa**n_khach

                # Biến cố A: 1 toa có (n_khach - 1) người, 1 toa có 1 người, còn lại trống.
                # Bước 1: Chọn (n_khach - 1) người từ n_khach người
                c1 = math.comb(n_khach, n_khach - 1)
                # Bước 2: Chọn 1 toa trong n_toa toa cho nhóm người này
                c2 = n_toa
                # Bước 3: Chọn 1 toa trong (n_toa - 1) toa còn lại cho 1 người còn lại
                c3 = n_toa - 1

                n_a = c1 * c2 * c3

                # Tính xác suất
                p_a = Rational(n_a, n_omega)

                # Đáp án đúng
                da = '$%s$' % (latex(p_a))

                # Tạo các đáp án sai
                s = []
                s.append('$%s$' % (latex(Rational(n_a + 2, n_omega))))
                s.append('$%s$' % (latex(Rational(c1 * c2, n_omega))))
                s.append('$%s$' % (latex(Rational(1, n_toa))))
                s.append('$%s$' % (latex(Rational(3, n_toa**2))))

                s = [i for i in s if i != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Có $%s$ hành khách bước lên một đoàn tàu gồm $%s$ toa. Mỗi hành khách độc lập với nhau và chọn ngẫu nhiên một toa. Xác suất để $1$ toa có $%s$ người, $1$ toa có $1$ người, các toa còn lại không có ai bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 % (latex(n_khach), latex(n_toa), latex(n_khach - 1)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                h1=p_a
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')
                # Nội dung lời giải chi tiết
                loigiai = ('''Vì mỗi hành khách có $%s$ cách chọn toa nên có $%s^{%s}$ cách xếp. \\\\
                             Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = %s^{%s} = %s$. \\\\
                             Gọi $A$ là biến cố "1 toa có $%s$ người, 1 toa có 1 người, các toa còn lại không có ai". \\\\
                             Để tìm số phần tử của $A$, ta chia làm hai giai đoạn như sau: \\\\
                             - Giai đoạn 1: Chọn $%s$ hành khách trong $%s$ hành khách. Chọn 1 toa trong $%s$ toa và xếp lên toa đó $%s$ hành khách vừa chọn. Suy ra có $C_{%s}^{%s} \\cdot C_{%s}^{1}$ cách. \\\\
                             - Giai đoạn 2: Chọn 1 toa trong $%s$ toa còn lại và xếp lên toa đó một hành khách còn lại. Suy ra có $C_{%s}^{1}$ cách. \\\\
                             Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = C_{%s}^{%s} \\cdot C_{%s}^{1} \\cdot C_{%s}^{1} = %s \\cdot %s \\cdot %s = %s$. \\\\
                             Vậy xác suất cần tính là $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = %s \\approx %s$.'''
                           % (latex(n_toa), latex(n_toa), latex(n_khach), 
                              latex(n_toa), latex(n_khach), latex(n_omega),
                              latex(n_khach - 1), 
                              latex(n_khach - 1), latex(n_khach), latex(n_toa), latex(n_khach - 1),
                              latex(n_khach), latex(n_khach - 1), latex(n_toa),
                              latex(n_toa - 1), latex(n_toa - 1),
                              latex(n_khach), latex(n_khach - 1), latex(n_toa), latex(n_toa - 1),
                              latex(c1), latex(c2), latex(c3), latex(n_a),
                              latex(n_a), latex(n_omega), latex(p_a),kqz
                             ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

