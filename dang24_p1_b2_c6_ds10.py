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


def bt_dang24_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Dạng 2: Hai số có chữ số hàng chục giống nhau
            lisdang = ['don_vi', 'hang_chuc']
            dang = random.choice(lisdang)

            # Khai báo số các số tự nhiên có 2 chữ số (từ 10 đến 99)
            n_S = 90
            # Tính n(Omega) = C(90, 2)
            n_Omega = int(binomial(n_S, 2)) 

            if dang == 'don_vi':
                ten_vi_tri = "đơn vị"
                # Có 10 cách chọn chữ số hàng đơn vị giống nhau (0, 1, ..., 9)
                # Với mỗi chữ số hàng đơn vị đó, ta chọn 2 chữ số hàng chục khác nhau từ {1, 2, ..., 9}
                # Số cách chọn: 10 * C(9, 2) = 10 * 36 = 360
                n_A = 10 * int(binomial(9, 2))
                mo_ta_chon_hang = "Có 10 cách chọn chữ số hàng đơn vị (chọn từ các số $\\left\\{0;1;2;3;4;5;6;7;8;9\\right\\}$)."
                mo_ta_chon_con_lai = "Có $C_9^2$ cách chọn hai chữ số hàng chục khác nhau (chọn từ các số $\\left\\{1;2;3;4;5;6;7;8;9\\right\\}$)."
            else:
                ten_vi_tri = "hàng chục"
                # Có 9 cách chọn chữ số hàng chục giống nhau (1, 2, ..., 9)
                # Với mỗi chữ số hàng chục đó, ta chọn 2 chữ số hàng đơn vị khác nhau từ {0, 1, ..., 9}
                # Số cách chọn: 9 * C(10, 2) = 9 * 45 = 405
                n_A = 9 * int(binomial(10, 2))
                mo_ta_chon_hang = "Có 9 cách chọn chữ số hàng chục (chọn từ các số $\\left\\{1;2;3;4;5;6;7;8;9\\right\\}$)."
                mo_ta_chon_con_lai = "Có $C_{10}^2$ cách chọn hai chữ số hàng đơn vị khác nhau (chọn từ các số $\\left\\{0;1;2;3;4;5;6;7;8;9\\right\\}$)."

            # Tính xác suất và rút gọn phân số
            prob = Rational(n_A, n_Omega)
            da_dung = "\\True $\\frac{%s}{%s}$" % (prob.p, prob.q)

            # B4- Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            s = []
            while len(s) < 3:
                # Tạo các tử số ngẫu nhiên gần với tử số đúng để làm nhiễu
                sai_p = random.randint(max(1, prob.p - 50), prob.p + 50)
                # Đảm bảo mẫu số giống nhau, tử số khác nhau và phân số không bằng đáp án đúng
                if sai_p != prob.p and Rational(sai_p, n_Omega) != prob:
                    item = "$\\frac{%s}{%s}$" % (sai_p, n_Omega)
                    if item not in s:
                        s.append(item)

            list_ans = [da_dung, s[0], s[1], s[2]]
            random.shuffle(list_ans)

            # B2- Viết nội dung bài toán
            noidungcauhoi = ("Gọi $S$ là tập hợp các số tự nhiên có hai chữ số. Chọn ngẫu nhiên đồng thời hai số từ tập hợp $S$. Xác suất để hai số được chọn có chữ số hàng %s giống nhau bằng" % ten_vi_tri)

            # Viết lời giải chi tiết (Không viết tắt, định dạng latex đúng yêu cầu)
            loigiai = ("Số phần tử của tập $S$ là: $9 \\cdot 10 = 90$. \\\\"
                       "Không gian mẫu là chọn ngẫu nhiên 2 số từ tập $S$. \\\\"
                       "Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{90}^2 = %s$. \\\\"
                       "Gọi $X$ là biến cố \"số được chọn có chữ số hàng %s giống nhau\". Ta mô tả không gian của biến cố $X$ như sau: \\\\"
                       "+ %s \\\\"
                       "+ %s \\\\"
                       "Suy ra số phần tử của biến cố $X$ là $n\\left(A\\right) = %s$. \\\\"
                       "Vậy xác suất cần tính là $P\\left(X\\right) = \\frac{%s}{%s} = \\frac{%s}{%s}$." 
                       % (n_Omega, ten_vi_tri, mo_ta_chon_hang, mo_ta_chon_con_lai, n_A, n_A, n_Omega, prob.p, prob.q))

            # Xuất câu trắc nghiệm (Content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

