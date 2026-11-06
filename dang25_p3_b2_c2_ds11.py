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


def bt_dang25_p3_b2_c2_ds11(self):
            # Khai báo biến
            # 1. Random tham số: u1, d, n
            u1 = random.randint(25, 45) # Số ghế hàng đầu
            d = random.randint(1, 4)    # Công sai (lượng tăng thêm mỗi hàng)
            n = random.randint(18, 35)  # Số hàng ghế

            # 2. Tính toán kết quả (Tổng S_n)
            # Công thức: S_n = n/2 * (2*u1 + (n-1)*d)
            kq = (n / 2) * (2 * u1 + (n - 1) * d)
            da_dung = int(kq)

            # 3. Tạo đáp án trắc nghiệm
            da = f'${latex(da_dung)}$'

            # Tạo các đáp án nhiễu (dễ dàng kiểm soát để không trùng)
            # Lấy các giá trị gần kq và là số nguyên
            da_sai = []
            # Sai lệch +- d*2, +- d*3...
            da_sai.append(da_dung + d * random.randint(2, 4))
            da_sai.append(da_dung - d * random.randint(2, 4))
            da_sai.append(da_dung + d * random.randint(1, 2) + random.randint(1, 2)) # Một số nhiễu "lẻ" hơn

            # Đảm bảo 3 đáp án nhiễu khác nhau và khác đáp án đúng
            da_sai_set = set(da_sai)
            while len(da_sai_set) < 3:
                da_sai_set.add(da_dung + random.choice([-1, 1]) * random.randint(3, 7))

            list_da_sai = [f'${latex(s)}$' for s in list(da_sai_set)[:3]]

            # Lấy 3 đáp án sai
            das1, das2, das3 = list_da_sai

            # 4. Nội dung câu hỏi và lời giải

            # Hàng thứ hai và hàng thứ ba
            u2 = u1 + d
            u3 = u1 + 2 * d

            noidungcauhoi = (f'''Một hội trường lớn có ${latex(u1)}$ ghế ở hàng đầu tiên, ${latex(u2)}$ ghế ở hàng thứ hai, ${latex(u3)}$ ghế ở hàng thứ ba và cứ tiếp tục theo quy luật như vậy. Có tất cả ${latex(n)}$ hàng ghế. Hỏi hội trường đó có bao nhiêu ghế?''')

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = (f'''Gọi $u_n$ là số ghế ở hàng thứ $n$. \\\\
            Dãy số $(u_n)$ lập thành cấp số cộng có số hạng đầu $u_1 = {latex(u1)}$ và công sai $d = u_2 - u_1 = {latex(u2)} - {latex(u1)} = {latex(d)}$.\\\\
            Số hàng ghế là $n = {latex(n)}$.\\\\
            Tổng số ghế của hội trường với ${latex(n)}$ hàng ghế là: \\\\
            Sử dụng công thức tổng cấp số cộng $S_n = \\frac{{n}}{{2}}[2u_1 + (n-1)d]$.\\\\
            $$\\text{{S}}_{{ {latex(n)} }} = \\frac{{ {latex(n)} }}{{2}}[2 \\cdot {latex(u1)} + ({latex(n)} - 1) \\cdot {latex(d)}]$$
            $$\\text{{S}}_{{ {latex(n)} }} = \\frac{{ {latex(n)} }}{{2}}( {latex(2*u1)} + {latex((n-1)*d)} ) = {latex(da_dung)} \\text{{ (ghế)}}.$$''')
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(da_dung))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

