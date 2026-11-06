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


def bt_dang48_p4_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1 & B3: Nghiên cứu đề bài và thiết lập random
                # Tổng số học sinh
                S = randint(100, 150)
                # Số học sinh nói tiếng Anh (n1) và tiếng Pháp (n2)
                n1 = randint(60, 85)
                n2 = randint(40, 55)
                # Đảm bảo số học sinh nói cả hai (n12) sao cho n1 + n2 - n12 <= S
                min_n12 = max(10, n1 + n2 - S + 5)
                max_n12 = min(n1, n2) - 10
                n12 = randint(min_n12, max_n12)

                # Tính toán kết quả
                # Số học sinh nói ít nhất 1 thứ tiếng: n_union = n1 + n2 - n12
                n_union = n1 + n2 - n12
                # Số học sinh không nói thứ tiếng nào: kq = S - n_union
                kq_val = S - n_union

                da = '$%s$' % (latex(kq_val))

                # B4: Điều chỉnh các phương án sai
                s_list = []
                while len(s_list) < 3:
                    sai = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    if sai > 0 and sai != kq_val and sai not in s_list:
                        s_list.append(sai)

                das1 = '$%s$' % (latex(s_list[0]))
                das2 = '$%s$' % (latex(s_list[1]))
                das3 = '$%s$' % (latex(s_list[2]))

                # Câu hỏi
                noidungcauhoi = ('''Trong $%s$ học sinh khối 10 có $%s$ học sinh nói được tiếng Anh, $%s$ học sinh nói được tiếng Pháp và $%s$ học sinh nói được cả hai thứ tiếng. Tìm số học sinh không nói được thứ tiếng nào.'''
                                 %(latex(S), latex(n1), latex(n2), latex(n12)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $A$ là tập hợp các học sinh nói được tiếng Anh. \\\\
                             Gọi $B$ là tập hợp các học sinh nói được tiếng Pháp. \\\\
                             Theo giả thiết, ta có $n\\left(A\\right)=%s$, $n\\left(B\\right)=%s$ và $n\\left(A \\cap B\\right)=%s$. \\\\
                             Số học sinh nói được ít nhất một trong hai thứ tiếng Anh hoặc Pháp là \\\\
                             $n\\left(A \\cup B\\right) = n\\left(A\\right) + n\\left(B\\right) - n\\left(A \\cap B\\right) = %s + %s - %s = %s$ (học sinh). \\\\
                             Số học sinh không nói được thứ tiếng nào trong hai thứ tiếng trên là \\\\
                             $%s - %s = %s$ (học sinh).'''
                           %(latex(n1), latex(n2), latex(n12),
                             latex(n1), latex(n2), latex(n12), latex(n_union),
                             latex(S), latex(n_union), latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

