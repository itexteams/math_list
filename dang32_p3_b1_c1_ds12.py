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


def bt_dang32_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':


                a_val = 0.000001

                # Random x0 (đáp án) và x1 (nghiệm âm)
                # Chọn sao cho b, c dễ nhìn
                pairs = [
                    (1000, -1000/3), # x0=1000, x1=-333.3 -> b = 1.5*10^-6 * 2000/3 = 10^-3 => b = 0.001. c = -3*10^-6 * 1000 * (-1000/3) = 1 => P(x) = -0.000001x^3 + 0.001x^2 + x
                    (1500, -500), # b = 1.5*10^-6 * 1000 = 0.0015. c = -3*10^-6 * 1500 * (-500) = 2.25
                    (2000, -1000), # b = 1.5*10^-6 * 1000 = 0.0015. c = -3*10^-6 * 2000 * (-1000) = 6
                    (1666.6666666666667, -1000), # Bài gốc: b = 0.001, c = 5. x0 = 5000/3. 
                ]

                # Chọn cấu hình giống bài gốc nhưng đổi c
                # P'(x) = -0.000003 x^2 + 0.002 x + c_val = 0
                # Đặt c_val = 1, 2, 3, 4, 5, 6, 7
                c_val = random.choice([2, 3, 4, 5, 6, 8, 9])

                b_val = 0.001
                a_val = 0.000001
                d_val = random.choice([300, 400, 500, 600, 800])
                x_max = 2000

                # Phương trình đạo hàm: -0.000003 x^2 + 0.002 x + c_val = 0
                # Delta' = 0.001^2 - (-0.000003) * c_val = 0.000001 + 0.000003 * c_val
                # x = (-0.001 - sqrt(Delta')) / (-0.000003)

                delta_phay = 0.000001 + 0.000003 * c_val
                sqrt_delta_phay = math.sqrt(delta_phay)
                x_ans = (-0.001 - sqrt_delta_phay) / (-0.000003)

                kq = int(round(x_ans))

                a_str = "0,000001"
                b_str = "0,001"
                a3_str = "0,000003"
                b2_str = "0,002"

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Tạo các phương án sai
                s = ['$%s$'%(latex(kq + 10)),
                     '$%s$'%(latex(kq - 10)),
                     '$%s$'%(latex(kq + 100)),
                     '$%s$'%(latex(kq - 100)),
                     '$%s$'%(latex(kq + 50)),
                     '$%s$'%(latex(kq - 50)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Lợi nhuận tổng hàng ngày (tính theo đô la) mà một công ty thu được từ việc sản xuất và bán $x$ đĩa DVD có thể ghi lại được cho bởi hàm lợi nhuận:\\\\
            $P(x) = -%sx^3 + %sx^2 + %sx - %s; \\quad 0 \\le x \\le %s$\\\\
            Mức sản xuất $x$ để lợi nhuận hàng ngày đạt cực đại bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị)'''
                                 %(a_str, b_str, c_val, d_val, x_max))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có hàm lợi nhuận $P(x) = -%sx^3 + %sx^2 + %sx - %s$ với $0 \\le x \\le %s$.\\\\
                             Đạo hàm: $P'(x) = -%sx^2 + %sx + %s$.\\\\
                             Cho $P'(x) = 0 \\Leftrightarrow -%sx^2 + %sx + %s = 0$.\\\\
                             Giải phương trình trên, ta được nghiệm dương là $x \\approx %s$.\\\\
                             Ta có $P''(x) = -0,000006x + %s$. Tại $x = %s$, $P''(%s) < 0$ nên hàm số đạt cực đại tại $x \\approx %s$.\\\\
                             Vậy mức sản xuất để lợi nhuận đạt cực đại là khoảng $%s$ đĩa DVD.'''
                             %(a_str, b_str, c_val, d_val, x_max,
                               a3_str, b2_str, c_val,
                               a3_str, b2_str, c_val,
                               kq,
                               b2_str, kq, kq, kq,
                               kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

