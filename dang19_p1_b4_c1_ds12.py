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


def bt_dang19_p1_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tọa độ điểm cực đại (x1, y1) và cực tiểu (x2, y2)
                x1 = random.randint(-3, 1)
                x2 = x1 + random.randint(1, 4)
                y1 = random.randint(1, 5)
                y2 = y1 - random.randint(2, 7)

                # Tính tọa độ điểm đối xứng (điểm uốn I)
                xI = Rational(x1 + x2, 2)
                yI = Rational(y1 + y2, 2)

                # Hàm hỗ trợ định dạng tọa độ để xử lý phân số
                def toado(hx, hy):
                    lx = latex(hx)
                    ly = latex(hy)
                    if '\\frac' in lx or '\\frac' in ly:
                        return 'I\\left(%s; %s\\right)' % (lx, ly)
                    else:
                        return 'I(%s; %s)' % (lx, ly)

                # Các đáp án trắc nghiệm
                da = toado(xI, yI)

                # Tạo các phương án nhiễu
                das1 = toado(x1, y1) # Cực đại
                das2 = toado(x2, y2) # Cực tiểu

                if yI != 0:
                    das3 = toado(xI, -yI) # Đảo dấu tung độ
                elif xI != 0:
                    das3 = toado(-xI, yI) # Đảo dấu hoành độ
                else:
                    das3 = toado(y1, x1) # Đảo tọa độ

                # Đảm bảo các phương án không trùng nhau
                while das3 == da or das3 == das1 or das3 == das2:
                    das3 = toado(xI + 1, yI - 1)
                    break

                # Vẽ bảng biến thiên bằng TikZ (tkz-tab) - Đã bỏ nocadre để tạo khung
                bbt = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[lgt=1.2,espcl=2.5]
            {$x$ /0.7, $f'(x)$ /0.7, $f(x)$ /2}
            {$-\\infty$, $%s$, $%s$, $+\\infty$}
            \\tkzTabLine{ ,+, 0, -, 0, +, }
            \\tkzTabVar{-/ $-\\infty$, +/ $%s$, -/ $%s$, +/ $+\\infty$}
            \\end{tikzpicture}
            \\end{center}''' % (latex(x1), latex(x2), latex(y1), latex(y2)))

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = ax^3 + bx^2 + cx + d$ có bảng biến thiên như sau:
            %s
            Tọa độ điểm đối xứng $I$ của đồ thị hàm số trên là:''' % (bbt))

                # Các đáp án
                da_d = ('\\True $%s$' % str(da))
                da_s1 = '$%s$' % str(das1)
                da_s2 = '$%s$' % str(das2)
                da_s3 = '$%s$' % str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Đồ thị hàm số bậc ba nhận điểm uốn làm tâm đối xứng.\\\\
            Điểm uốn $I$ là trung điểm của đoạn thẳng nối hai điểm cực trị của đồ thị hàm số.\\\\
            Từ bảng biến thiên, đồ thị hàm số có điểm cực đại là $A(%s; %s)$ và điểm cực tiểu là $B(%s; %s)$.\\\\
            Tọa độ điểm đối xứng $I$ là:
            $$\\begin{cases} x_I = \\frac{x_A + x_B}{2} = \\frac{%s + %s}{2} = %s \\\\ y_I = \\frac{y_A + y_B}{2} = \\frac{%s + %s}{2} = %s \\end{cases}$$
            Vậy tọa độ tâm đối xứng là $%s$.''' % 
                (latex(x1), latex(y1), latex(x2), latex(y2), 
                 latex(x1), latex(x2), latex(xI), 
                 latex(y1), latex(y2), latex(yI), 
                 str(da)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

