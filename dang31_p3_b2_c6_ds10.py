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


def bt_dang31_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Chúng ta sẽ random số lượng bì thư và tem (n)
            n = random.randint(3, 5) 
            k = n - 1 # Số bì thư cần khớp (theo đề là 2 trong 3, nên ta dùng n-1 trong n)

            # Tính toán các giá trị
            n_omega = math.factorial(n)
            n_A = 1
            probability = Rational(n_A, n_omega)

            # B4: Điều chỉnh các phương án sai không được trùng đáp án đúng
            da_dung = '$%s$' % (latex(probability))

            # Tạo danh sách phương án sai
            list_s = []
            possible_denominators = [2, 3, 4, 6, 8, 12, 24, 60, 120]
            while len(list_s) < 3:
                num = random.randint(1, 5)
                den = random.choice(possible_denominators)
                if den > num: # Đảm bảo xác suất < 1
                    ps = Rational(num, den)
                    ps_latex = '$%s$' % (latex(ps))
                    if ps_latex != da_dung and ps_latex not in list_s:
                        list_s.append(ps_latex)

            das1, das2, das3 = list_s

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có $%s$ bì thư giống nhau lần lượt được đánh số thứ tự từ $1$ đến $%s$ và $%s$ con tem giống nhau lần lượt đánh số thứ tự từ $1$ đến $%s$. Dán $%s$ con tem đó vào $%s$ bì thư sao cho không có bì thư nào không có tem. Xác suất để lấy ra được $%s$ bì thư trong $%s$ bì thư trên sao cho mỗi bì thư đều có số thứ tự giống với số thứ tự con tem đã dán vào nó bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                             % (latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(k), latex(n)))

            h1=probability
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.', ',')
            # Nội dung lời giải
            loigiai = ('''Không gian mẫu là số cách dán $%s$ con tem trên $%s$ bì thư. Tức là hoán vị của $%s$ con tem trên $%s$ bì thư. Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = %s! = %s$. \\\\
                      Gọi $A$ là biến cố "$%s$ bì thư lấy ra có số thứ tự giống với số thứ tự con tem đã dán vào nó". Thế thì bì thư còn lại cũng có số thứ tự giống với số thứ tự con tem đã dán vào nó (vì chỉ còn một vị trí và một con tem duy nhất). \\\\
                      Trường hợp này có một cách duy nhất (tất cả các bì thư đều dán đúng tem của nó). Suy ra số phần tử của $A$ là $n\\left(A\\right) = 1$. \\\\
                      Vậy xác suất cần tính $P\\left(A\\right) = \\frac{1}{%s} = %s \\approx %s$.'''
                       % (latex(n), latex(n), latex(n), latex(n), latex(n), latex(n_omega), 
                          latex(k), latex(n_omega), da_dung.replace('$', ''),kqz))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Các đáp án
            da_d = ('\\True ' + str(da_dung))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo đúng format mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

