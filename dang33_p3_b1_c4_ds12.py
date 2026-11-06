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


def bt_dang33_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':


                n_A = 24 + 6 + 12 # = 42

                # Biến cố B: Cấp số nhân từ các bộ trên. Chỉ có bộ {1; 2; 4} lập được CSN:
                # Trình tự {1; 2; 4} (q=2): 2 * 2 * 1 = 4 cách.
                # Trình tự {4; 2; 1} (q=1/2): 1 * 2 * 2 = 4 cách.
                n_AB = 4 + 4 # = 8

                # Tính xác suất P(B|A) = 8/42 = 4/21
                xs_chinh_xac = float(n_AB) / n_A # ~ 0.190476...

                # Làm tròn đến hàng phần chục theo yêu cầu đề bài (0.2)
                kq3 = Decimal(str(xs_chinh_xac)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.',',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên không trùng phương án đúng
                s = []
                for i in [0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
                    val_str = str(i).replace('.',',')
                    if val_str != kq:
                        s.append('$%s$' % val_str)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một con xúc xắc cân đối đồng chất được thiết kế đặc biệt, trên sáu mặt của nó ghi các số $1,1,2,2,3,4$. Tiến hành tung con xúc xắc này ba lần liên tiếp. Biết rằng tổng các số thu được sau ba lần tung bằng $7$. Xác suất để kết quả của ba lần tung theo đúng thứ tự đó lập thành một cấp số nhân (Kết quả làm tròn đến hàng phần chục) là''')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $A$ là biến cố: "Tổng số chấm thu được sau $3$ lần tung bằng $7$".\\\\
            Bộ $\\{1; 2; 4\\}$ có $3!=6$ hoán vị và mỗi hoán vị có số cách xuất hiện là $2 \\cdot 2 \\cdot 1 = 4$ cách nên số cách cho bộ này là: $6 \\cdot 4 = 24$ cách.\\\\
            Bộ $\\{1; 3; 3\\}$ có $\\frac{3!}{2!} = 3$ hoán vị và mỗi hoán vị có số cách xuất hiện là $2 \\cdot 1 \\cdot 1 = 2$ cách nên số cách cho bộ này là: $3 \\cdot 2 = 6$ cách.\\\\
            Bộ $\\{2; 2; 3\\}$ có $\\frac{3!}{2!} = 3$ hoán vị và mỗi hoán vị có số cách xuất hiện là $2 \\cdot 2 \\cdot 1 = 4$ cách nên số cách cho bộ này là: $3 \\cdot 4 = 12$ cách.\\\\
            Vậy tổng số khả năng để biến cố $A$ xảy ra là: $24 + 6 + 12 = 42$ cách.\\\\
            Gọi $B$ là biến cố: "Kết quả ba lần tung theo thứ tự lập thành một cấp số nhân".\\\\
            Với ba bộ ở trên, chỉ có bộ $\\{1; 2; 4\\}$ tạo thành cấp số nhân và tạo ra hai hoán vị.\\\\
            Trình tự $\\{1; 2; 4\\}$ với công bội $q = 2$ có $2 \\cdot 2 \\cdot 1 = 4$ cách.\\\\
            Trình tự $\\{4; 2; 1\\}$ với công bội $q = \\frac{1}{2}$ có $1 \\cdot 2 \\cdot 2 = 4$ cách.\\\\
            Vậy số cách để kết quả vừa có tổng bằng $7$ vừa là cấp số nhân là: $n(A \\cap B) = 4 + 4 = 8$ cách.\\\\
            Vậy xác suất cần tìm là: $P(B | A) = \\frac{n(A \\cap B)}{n(A)} = \\frac{8}{42} = \\frac{4}{21} \\approx %s$.'''
                           %(kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

