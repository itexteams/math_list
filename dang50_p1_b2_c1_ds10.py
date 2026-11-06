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


def bt_dang50_p1_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các giá trị ngẫu nhiên cho bài toán
                # N: tổng số học sinh, L: giỏi Văn, I: giỏi cả hai, O: không giỏi môn nào
                N = randint(40, 50)
                L = randint(10, 15)
                I = randint(2, 5)
                O = randint(12, 18)

                # Tính toán số học sinh giỏi toán a
                # Công thức: N = (L + a - I) + O => a = N - O - L + I
                a_val = N - O - L + I

                # Tạo đáp án đúng là một khoảng chứa a_val
                # Ví dụ: a = 20, khoảng đúng (18; 24)
                low_d = a_val - randint(2, 3)
                high_d = a_val + randint(3, 5)
                da = "\\left( %s; %s \\right)" % (latex(low_d), latex(high_d))

                # Tạo các đáp án sai không chứa a_val
                # S1: Khoảng nằm hoàn toàn bên trái
                s1 = "\\left( %s; %s \\right)" % (latex(randint(1, 5)), latex(a_val - randint(6, 8)))

                # S2: Khoảng có a_val là biên (ngoặc tròn nên không chứa a_val)
                s2 = "\\left( %s; %s \\right)" % (latex(a_val), latex(a_val + randint(8, 12)))

                # S3: Khoảng nằm hoàn toàn bên phải
                s3 = "\\left( %s; %s \\right)" % (latex(a_val + randint(1, 3)), latex(a_val + randint(15, 20)))

                # Đảm bảo các phương án không trùng lặp
                da_s_list = list(set([s1, s2, s3]))
                while len(da_s_list) < 3:
                    new_s = "\\left( %s; %s \\right)" % (latex(randint(1, 30)), latex(randint(31, 60)))
                    if new_s != da:
                        da_s_list.append(new_s)

                das1, das2, das3 = da_s_list

                # Câu hỏi
                noidungcauhoi = ('''Lớp $10A$ có $%s$ học sinh, trong đó có $%s$ học sinh giỏi văn, $a$ học sinh giỏi toán, có $%s$ học sinh giỏi văn và giỏi toán, $%s$ học sinh không giỏi văn và không giỏi toán. Mệnh đề nào sau đây đúng?'''
                                 %(latex(N), latex(L), latex(I), latex(O)))

                # Các đáp án
                da_d = ('\\True $a \\in ' + str(da) + '$')
                da_s1 = ('$a \\in ' + str(das1) + '$')
                da_s2 = ('$a \\in ' + str(das2) + '$')
                da_s3 = ('$a \\in ' + str(das3) + '$')

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Gọi $A$ là tập hợp các học sinh giỏi văn, $B$ là tập hợp các học sinh giỏi toán. \\\\
                         Theo giả thiết, ta có: \\\\
                         Số học sinh giỏi ít nhất một trong hai môn Văn hoặc Toán là: \\\\
                         $n\\left( A \\cup B \\right) = %s - %s = %s$ (học sinh). \\\\
                         Mặt khác, theo công thức số phần tử của hợp hai tập hợp: \\\\
                         $n\\left( A \\cup B \\right) = n\\left( A \\right) + n\\left( B \\right) - n\\left( A \\cap B \\right)$. \\\\
                         Thay các số liệu vào ta được: \\\\
                         $%s = %s + a - %s \\Leftrightarrow %s = a + %s \\Leftrightarrow a = %s$. \\\\
                         Đối chiếu với các phương án, ta thấy $%s \\in %s$.'''
                         %(latex(N), latex(O), latex(N-O),
                           latex(N-O), latex(L), latex(I), latex(N-O), latex(L-I), latex(a_val),
                           latex(a_val), str(da)
                         ))

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

