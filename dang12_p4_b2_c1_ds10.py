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


def bt_dang12_p4_b2_c1_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thay đổi các giá trị để tạo bài toán ngẫu nhiên
                tong_hs = random.randint(30, 50)
                hs_khong_chon = random.randint(5, 20)

                # Đảm bảo các giá trị không âm và có ý nghĩa
                n_A = random.randint(5, 15)
                n_B = random.randint(5, 15)
                n_C = random.randint(5, 15)

                n_AB = random.randint(1, min(n_A, n_B) - 1)
                n_BC = random.randint(1, min(n_B, n_C) - 1)
                n_AC = random.randint(1, min(n_A, n_C) - 1)

                n_union = tong_hs - hs_khong_chon
                n_ABC = n_union - (n_A + n_B + n_C) + (n_AB + n_BC + n_AC)

                # Điều chỉnh lại các giá trị nếu kq không hợp lý
                if n_ABC < 0:
                    n_ABC = random.randint(1, 3)
                    n_union = n_A + n_B + n_C - (n_AB + n_BC + n_AC) + n_ABC
                    tong_hs = n_union + hs_khong_chon

                kq = n_ABC
                kq_str = str(kq)


                # Câu hỏi
                noidungcauhoi = ('''Một lớp có $%s$ học sinh. Trong một đợt khảo sát, giáo viên chủ nhiệm đưa ra ba nhóm ngành cho học sinh lựa chọn: Giáo dục, Y tế và Công nghệ thông tin. Có $%s$ học sinh không chọn nhóm ngành nào trong ba nhóm trên. 
                Kết quả khảo sát như sau: có $%s$ học sinh chọn Giáo dục, $%s$ học sinh chọn Y tế, $%s$ học sinh chọn Công nghệ thông tin. Ngoài ra, có $%s$ học sinh chọn cả hai nhóm Giáo dục và Y tế; $%s$ học sinh chọn cả hai nhóm Y tế và Công nghệ thông tin; $%s$ học sinh chọn cả hai nhóm Giáo dục và Công nghệ thông tin. Hỏi có bao nhiêu học sinh chọn cả ba nhóm ngành?'''
                                 %(latex(tong_hs), latex(hs_khong_chon), 
                                   latex(n_A), latex(n_B), latex(n_C),
                                   latex(n_AB), latex(n_BC), latex(n_AC)
                                 ))


                # Nội dung lời giải
                loigiai=('''Gọi $A,B,C$ lần lượt là tập hợp học sinh chọn nhóm ngành Giáo dục, Y tế, Công nghệ thông tin. \\\\
                Số học sinh chọn ít nhất một trong ba nhóm ngành là: $%s - %s = %s$. \\\\
                Theo nguyên lý bao hàm và loại trừ cho ba tập hợp, ta có công thức: \\\\
                $n(A \\cap B \\cap C) = n(A \\cup B \\cup C) - n(A) - n(B) - n(C) + n(A \\cap B) + n(B \\cap C) + n(A \\cap C)$. \\\\
                Thay số vào, ta được: \\\\
                $n(A \\cap B \\cap C) = %s - %s - %s - %s + %s + %s + %s = %s$.'''
                         %(latex(tong_hs), latex(hs_khong_chon), latex(n_union),
                           latex(n_union), latex(n_A), latex(n_B), latex(n_C),
                           latex(n_AB), latex(n_BC), latex(n_AC), latex(kq)
                         ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')  
            return content 

