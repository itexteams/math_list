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


def bt_dang19_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Tạo ngẫu nhiên tâm I(a, b) và bán kính R^2 (k2)
                a = random.randint(-5, 5)
                b = random.randint(-5, 5)

                # Để điểm A nguyên, ta chọn vector IA = (u, v) trước
                # Sau đó R^2 = u^2 + v^2
                u = random.choice([x for x in range(-5, 5) if x != 0])
                v = random.choice([x for x in range(-5, 5) if x != 0])

                k2 = u**2 + v**2
                R_val = sp.sqrt(k2)

                # Tọa độ điểm A thuộc đường tròn: A = I + IA
                xA = a + u
                yA = b + v

                # Thiết lập các biểu thức Sympy để xử lý dấu tự động
                x, y = symbols('x y')

                # Phương trình đường tròn (C)
                vt_trai = (x - a)**2 + (y - b)**2
                pt_tron = latex(vt_trai) + " = " + str(k2)

                # Vector pháp tuyến n = IA = (u, v)
                # Phương trình tiếp tuyến: u(x - xA) + v(y - yA) = 0 <=> ux + vy + (-u*xA - v*yA) = 0
                c_tt = -u*xA - v*yA
                pt_tiep_tuyen = sp.Eq(u*x + v*y + c_tt, 0)
                pt_tt_latex = latex(pt_tiep_tuyen).replace('=', ' = ')

                # Tạo đáp án đúng
                da = "$%s$" % pt_tt_latex

                # Tạo các đáp án nhiễu (thay đổi hệ số tự do hoặc đổi dấu vector pháp tuyến)
                s = [
                    "$%s = 0$" % latex(u*x + v*y + c_tt + random.randint(1, 5)),
                    "$%s = 0$" % latex(u*x + v*y + c_tt - random.randint(1, 5)),
                    "$%s = 0$" % latex(v*x + u*y + c_tt),
                    "$%s = 0$" % latex(u*x - v*y + (u*xA - v*yA)),
                    "$%s = 0$" % latex(-u*x + v*y + (u*xA + v*yA))
                ]

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Câu hỏi
                noidungcauhoi = (r"Trong mặt phẳng tọa độ $Oxy$, cho đường tròn $(C) \colon %s$. "
                                 r"Phương trình tiếp tuyến của đường tròn $(C)$ tại điểm $A(%s; %s)$ là"
                                 % (pt_tron, latex(xA), latex(yA)))

                # Các đáp án
                da_d = r'\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r"Đường tròn $(C)$ có tâm $I(%s; %s)$ và bán kính $R = %s$. \\ "
                           r"Do $A$ thuộc $(C)$ nên tiếp tuyến $\Delta$ qua $A$ và nhận $\vec{IA} = (%s; %s)$ làm vector pháp tuyến. \\ "
                           r"Vậy phương trình $\Delta \colon %s$."
                           % (latex(a), latex(b), latex(R_val), 
                              latex(u), latex(v), 
                              pt_tt_latex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

