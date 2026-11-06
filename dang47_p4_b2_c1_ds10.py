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


def bt_dang47_p4_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random dữ liệu
                # n_total: Tổng số học sinh lớp 10A
                # n_a: Số bạn tham gia Nhiếp ảnh
                # n_b: Số bạn tham gia Hội họa
                # Giả định mọi học sinh đều tham gia ít nhất 1 CLB

                n_total = randint(45, 60)
                # Đảm bảo n_a và n_b đủ lớn để phần giao không bị âm hoặc bằng 0
                n_a = randint(n_total // 2 + 5, n_total - 10)
                n_b = randint(n_total - n_a + 5, n_total - 5)

                # Đáp án đúng (Số bạn tham gia cả hai)
                kq_val = n_a + n_b - n_total
                kq = str(kq_val)

                # Các đáp án trắc nghiệm
                da_d = ('\\True $%s$' % (kq))

                # Tạo danh sách các phương án sai không trùng với đáp án đúng
                s_list = []
                while len(s_list) < 3:
                    sai = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    if sai > 0 and str(sai) != kq and str(sai) not in s_list:
                        s_list.append(str(sai))

                da_s1 = '$%s$' % (s_list[0])
                da_s2 = '$%s$' % (s_list[1])
                da_s3 = '$%s$' % (s_list[2])

                # Câu hỏi
                noidungcauhoi = ('''Trong $%s$ học sinh của lớp $10A$, có $%s$ bạn tham gia câu lạc bộ Nhiếp ảnh, có $%s$ bạn tham gia câu lạc bộ Hội họa. Tìm số học sinh tham gia cả hai câu lạc bộ Nhiếp ảnh và Hội họa.'''
                                 %(latex(n_total), latex(n_a), latex(n_b)))

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Nội dung lời giải
                loigiai = ('''Gọi $A$ là tập hợp các học sinh tham gia câu lạc bộ Nhiếp ảnh, $B$ là tập hợp các học sinh tham gia câu lạc bộ Hội họa. \\\\
                             Theo giả thiết, ta có: $n\\left(A\\right) = %s$, $n\\left(B\\right) = %s$. \\\\
                             Giả sử mọi học sinh trong lớp đều tham gia ít nhất một trong hai câu lạc bộ, khi đó số học sinh của lớp chính là số phần tử của tập hợp $A \\cup B$, tức là $n\\left(A \\cup B\\right) = %s$. \\\\
                             Số học sinh tham gia cả hai câu lạc bộ là số phần tử của tập hợp $A \\cap B$, được tính theo công thức: \\\\
                             $n\\left(A \\cap B\\right) = n\\left(A\\right) + n\\left(B\\right) - n\\left(A \\cup B\\right)$. \\\\
                             Thay số vào ta được: \\\\
                             $n\\left(A \\cap B\\right) = %s + %s - %s = %s$. \\\\
                             Vậy có $%s$ bạn tham gia cả hai câu lạc bộ.'''
                           %(latex(n_a), latex(n_b), latex(n_total),
                             latex(n_a), latex(n_b), latex(n_total), latex(kq_val), latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

