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


def bt_dang8_p4_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Bước 1: Khởi tạo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tọa độ điểm M(xm; ym)
                xm = randint(-10, 10)
                ym = randint(-10, 10)
                # Tránh trường hợp xm = 0 để lời giải biến đổi t nhìn rõ ràng hơn
                if xm == 0: xm = 5 

                # Vectơ chỉ phương của Ox là (1; 0)
                ux = 1
                uy = 0

                # Đáp án đúng: d có dạng {x = xm + t, y = ym} 
                # Hoặc dạng đơn giản hơn thường thấy trong trắc nghiệm là {x = t, y = ym}
                da_dung = "\\begin{cases} x = t \\\\ y = %s \\end{cases}" % (latex(ym))

                # Các phương án nhiễu
                s = [
                    "\\begin{cases} x = 1 + %st \\\\ y = %st \\end{cases}" % (latex(xm), latex(ym)), # Tỉ lệ từ tọa độ
                    "\\begin{cases} x = %s \\\\ y = %s + t \\end{cases}" % (latex(xm), latex(ym)), # Song song Oy
                    "\\begin{cases} x = %s + t \\\\ y = %s \\end{cases}" % (latex(ym), latex(xm)), # Tráo đổi x, y
                    "\\begin{cases} x = %s \\\\ y = t \\end{cases}" % (latex(ym)),
                    "\\begin{cases} x = %s + t \\\\ y = 0 \\end{cases}" % (latex(xm)),
                ]

                # Lọc bỏ nếu trùng với đáp án đúng (đề phòng ym ngẫu nhiên rơi vào các giá trị đặc biệt)
                s = [i for i in s if i != da_dung]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ("Lập phương trình tham số của đường thẳng $d$ đi qua điểm $M(%s;%s)$ và song song với trục $Ox$."
                                 % (latex(xm), latex(ym)))

                # Các đáp án
                da_d = ('\\True $' + str(da_dung) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo hình ảnh
                # d song song Ox nên nhận u_Ox = (1; 0) làm VCP
                loigiai = ("Trục $Ox$ có vectơ chỉ phương là $\\vec{u}_{Ox} = (1;0)$. \\\\"
                           "Vì đường thẳng $d \\parallel Ox$ nên $d$ nhận $\\vec{u}_{Ox} = (1;0)$ làm vectơ chỉ phương $\\vec{u}_d = (1;0)$. \\\\"
                           "Phương trình tham số của đường thẳng $d$ đi qua $M(%s;%s)$ có vectơ chỉ phương $\\vec{u}_d = (1;0)$ là: \\\\"
                           "$d: \\begin{cases} x = %s + t \\\\ y = %s \\end{cases}$. \\\\"
                           "Với $t = %s$, ta chọn được điểm $A(0; %s) \\in d$. \\\\"
                           "Khi đó phương trình đường thẳng $d$ có thể viết lại dưới dạng: $d: \\begin{cases} x = t \\\\ y = %s \\end{cases}$."
                           % (latex(xm), latex(ym), latex(xm), latex(ym), latex(-xm), latex(ym), latex(ym)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

