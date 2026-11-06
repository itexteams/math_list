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


def bt_dang28_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                bo_du_lieu = [

                    (2, 1, 3), # Tương ứng phương trình: 2*cos(a) - sin(a) = ...
                ]



                list_nguyen = [2, 3, 4, 5]
                kq_nguyen = random.choice(list_nguyen)



                if kq_nguyen == 2:
                    A, B = 3, 2  # 3*cos(a) - 2*sin(a) = 1 => tan(a) = 2 (loại vì nghiệm kia hoặc điều kiện góc nhọn)



                # Ta random dựa trên các bộ số thực tế cho ra tan(a) là số nguyên dương:
                bo_so_chuan = [
                    (4, 3, 1),   # 4*cos(a) - 3*sin(a) = 1 => tan(a) = 1
                    (9, 7, 1),   # 9*cos(a) - 7*sin(a) = 1 => tan(a) = 1
                    (5, 2, 2),   # 5*cos(a) - 2*sin(a) = 2 => tan(a) = 1
                    (2, 1, 1),   # 2*cos(a) - sin(a) = 1   => tan(a) = 1  (Góc nhọn alpha thỏa mãn)
                ]



                A, B, C = random.choice([
                    (4, 3, 1),
                    (5, 3, 1),
                    (2, 1, 1),
                    (7, 5, 1)
                ])



                bo_nguyen_thuy = [
                    (3, 1, 3, 4),   # (Hệ số cos, Hệ số sin, Hệ số nhân vào tan để ra số nguyên, Kết quả nguyên)
                    (2, 1, 4, 3),
                    (4, 1, 8, 15)
                ]

                hso_cos, hso_sin, hso_nhan, kq_nguyen = random.choice(bo_nguyen_thuy)

                da = '$%s$' % (latex(kq_nguyen))

                # Tạo các phương án trắc nghiệm nhiễu là số nguyên
                s = [
                    '$%s$' % (latex(kq_nguyen + 1)),
                    '$%s$' % (latex(kq_nguyen + 2)),
                    '$%s$' % (latex(kq_nguyen - 1 if kq_nguyen - 1 > 0 else kq_nguyen + 3)),
                    '$%s$' % (latex(hso_nhan)),
                    '$%s$' % (latex(hso_cos)),
                    '$%s$' % (latex(kq_nguyen + 4))
                ]

                # Lọc bỏ phương án trùng với đáp án đúng và lọc trùng
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Thiết lập chuỗi câu hỏi hiển thị giống định dạng ảnh
                chuoi_tri_so = '' if hso_nhan == 1 else '%s ' % latex(hso_nhan)

                # Câu hỏi sử dụng định dạng %s
                noidungcauhoi = ('''Cho $%s\\cos \\alpha - \\sin \\alpha = 1$, với $0^\\circ < \\alpha < 90^\\circ$. Giá trị của $%s\\tan \\alpha$ bằng bao nhiêu?'''
                                 % (latex(hso_cos), chuoi_tri_so))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn ngẫu nhiên các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước, xuống dòng bằng \\\\
                # Tính toán phân số tan để đưa vào lời giải
                tan_phan_so = Rational(kq_nguyen, hso_nhan)

                loigiai = ('''Vì $0^\\circ < \\alpha < 90^\\circ$ nên $\\cos \\alpha > 0$. Chia cả hai vế của phương trình cho $\\cos \\alpha$, ta được: \\\\
                           $%s - \\tan \\alpha = \\frac{1}{\\cos \\alpha}$. \\\\
                           Bình phương hai vế của phương trình trên, ta thu được: \\\\
                           $\\left(%s - \\tan \\alpha\\right)^2 = \\frac{1}{\\cos^2 \\alpha}$ \\\\
                           $\\Leftrightarrow %s - %s\\tan \\alpha + \\tan^2 \\alpha = 1 + \\tan^2 \\alpha$ \\\\
                           $\\Leftrightarrow %s\\tan \\alpha = %s$ \\\\
                           $\\Leftrightarrow \\tan \\alpha = %s$. \\\\
                           Bài toán yêu cầu tính giá trị của biểu thức $%s\\tan \\alpha$, do đó ta có: \\\\
                           $%s\\tan \\alpha = %s \\cdot %s = %s$.'''
                           % (latex(hso_cos), latex(hso_cos), latex(hso_cos**2), latex(2*hso_cos),
                              latex(2*hso_cos), latex(hso_cos**2 - 1), latex(tan_phan_so),
                              chuoi_tri_so, chuoi_tri_so, latex(hso_nhan), latex(tan_phan_so), latex(kq_nguyen)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_nguyen))
            # Xuất câu trắc nghiệm theo đúng cấu trúc format của mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

