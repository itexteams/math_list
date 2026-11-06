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


def bt_dang8_p3_b1_c6_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # n1: số bóng hộp 1, n2: số bóng hộp 2, s_min: tổng tối thiểu
                n1 = random.randint(5, 9)
                n2 = random.randint(4, 7)
                s_min = random.randint(5, 8)

                # Tính số kết quả có thể xảy ra
                total = n1 * n2

                # Tìm các kết quả thuận lợi cho biến cố đối (Tổng < s_min)
                bad_pairs = []
                for i in range(1, n1 + 1):
                    for j in range(1, n2 + 1):
                        if i + j < s_min:
                            bad_pairs.append("\\left(" + str(i) + "; " + str(j) + "\\right)")

                num_bad = len(bad_pairs)
                ans = total - num_bad

                # Đáp án đúng
                kq = str(ans)
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    # Tạo các phương án nhiễu xung quanh đáp án đúng
                    sai = ans + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    if sai > 0 and str(sai) != kq:
                        s_set.add('$%s$'%(str(sai)))

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Hộp thứ nhất chứa $%s$ quả bóng được đánh số từ $1$ đến $%s$. Hộp thứ hai chứa $%s$ quả bóng được đánh số từ $1$ đến $%s$. Chọn ngẫu nhiên mỗi hộp $1$ quả bóng. Kết quả thuận lợi cho biến cố "Tổng các số ghi trên hai quả bóng không nhỏ hơn $%s$" bằng bao nhiêu?'''
                                 %(latex(n1), latex(n1), latex(n2), latex(n2), latex(s_min)
                                 ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                pairs_str = ", ".join(bad_pairs)
                loigiai = ('''Số kết quả có thể xảy ra của phép thử là $%s \\cdot %s = %s$. \\\\
                             Biến cố đối của biến cố "Tổng các số ghi trên hai quả bóng không nhỏ hơn $%s$" là biến cố "Tổng các số ghi trên hai quả bóng nhỏ hơn $%s$". \\\\
                             Các kết quả thuận lợi cho biến cố "Tổng các số ghi trên hai quả bóng nhỏ hơn $%s$" bao gồm các cặp số sau: \\\\ $%s$. \\\\
                             Số kết quả thuận lợi cho biến cố "Tổng các số ghi trên hai quả bóng nhỏ hơn $%s$" là $%s$. \\\\
                             Vậy số kết quả thuận lợi cho biến cố "Tổng các số ghi trên hai quả bóng không nhỏ hơn $%s$" là $%s - %s = %s$.'''
                           %(latex(n1), latex(n2), latex(total), 
                             latex(s_min), latex(s_min), 
                             latex(s_min), pairs_str, 
                             latex(s_min), latex(num_bad), 
                             latex(s_min), latex(total), latex(num_bad), latex(ans)
                           ))
                dapan=' \\shortans[0]{$%s$} '%(latex(ans))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

