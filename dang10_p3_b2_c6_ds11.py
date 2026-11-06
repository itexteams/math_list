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


def bt_dang10_p3_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # pX: % hâm mộ đội X, pY: % hâm mộ đội Y, pXY: % hâm mộ cả hai
                # Đảm bảo pXY < pX và pXY < pY và (pX + pY - pXY) < 100
                pX = random.randint(20, 35)
                pY = random.randint(36, 50)
                pXY = random.randint(5, 15)

                # Tính toán xác suất
                probA = Rational(pX, 100)
                probB = Rational(pY, 100)
                probAB = Rational(pXY, 100)

                # P(A U B) = P(A) + P(B) - P(AB)
                probAUB = probA + probB - probAB

                # Xác suất không hâm mộ đội nào: 1 - P(A U B)
                kq_val = 1 - probAUB

                # Định dạng kết quả số thập phân với dấu phẩy
                def format_vn(val):
                    return str(float(val)).replace('.', ',')

                kq_str = format_vn(kq_val)

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                # Tạo danh sách đáp án nhiễu xung quanh đáp án đúng
                s = []
                offsets = [-0.1, 0.1, -0.05, 0.05, 0.15, -0.15]
                for offset in offsets:
                    sai = round(float(kq_val) + offset, 2)
                    if sai > 0 and sai < 1 and sai != float(kq_val):
                        s.append('$%s$' % (str(sai).replace('.', ',')))

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                da_d = '\\True $%s$' % (kq_str)

                # Câu hỏi
                noidungcauhoi = ('''Người ta thăm dò một số lượng người hâm mộ bóng đá tại một thành phố, nơi có hai đội bóng đá $X$ và $Y$ cùng thi đấu giải vô địch quốc gia. Biết rằng số lượng người hâm mộ đội bóng đá $X$ là $%s\\%%$, số lượng người hâm mộ đội bóng đá $Y$ là $%s\\%%$, trong số đó có $%s\\%%$ người nói rằng họ hâm mộ cả hai đội bóng trên. Chọn ngẫu nhiên một người hâm mộ trong số những người được hỏi, xác suất để chọn được người không hâm mộ đội nào trong hai đội bóng đá $X$ và $Y$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 %(latex(pX), latex(pY), latex(pXY)))

                # Nội dung lời giải chi tiết (Bước 2: Viết lại y hệt cấu trúc ảnh)
                loigiai = ('''Gọi $A$ là biến cố: "Chọn được một người hâm mộ đội bóng đá $X$", gọi $B$ là biến cố: "Chọn được một người hâm mộ đội bóng đá $Y$". \\\\
            Khi đó $P\\left(A\\right)=\\frac{%s}{100}=%s, P\\left(B\\right)=\\frac{%s}{100}=%s, P\\left(AB\\right)=\\frac{%s}{100}=%s$. \\\\
            Suy ra: $P\\left(A \\cup B\\right)=P\\left(A\\right)+P\\left(B\\right)-P\\left(AB\\right)=%s+%s-%s=%s$. \\\\
            Xác suất để chọn được người không hâm mộ đội nào trong hai đội bóng đá $X$ và $Y$ là: \\\\
            $P\\left(\\overline{A \\cup B}\\right)=1-P\\left(A \\cup B\\right)=1-%s=%s$.'''
                           %(latex(pX), format_vn(probA), 
                             latex(pY), format_vn(probB), 
                             latex(pXY), format_vn(probAB),
                             format_vn(probA), format_vn(probB), format_vn(probAB), format_vn(probAUB),
                             format_vn(probAUB), kq_str))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)
                dapan=' \\shortans[0]{$%s$} '%(kq_str)
            # Xuất câu trắc nghiệm (Không dùng raw string r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

