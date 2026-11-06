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


def bt_dang38_p3_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khởi tạo các thông số ngẫu nhiên
                v = randint(10, 30)          # Tốc độ bơm (l/phút)
                he_so = randint(10, 50)      # Hệ số để V0 chia hết cho v cho đẹp số
                V0 = v * he_so               # Lượng nước ngọt ban đầu (l)
                c = randint(15, 60)          # Nồng độ muối bơm vào (g/l)

                # 2. Tính toán các giá trị trung gian cho lời giải
                # Nồng độ C(t) = (c * v * t) / (V0 + v * t)
                # Rút gọn phân số cho giống mẫu: C(t) = (c * t) / (V0/v + t)
                k = V0 // v  # k = 40 trong ví dụ mẫu

                # Đáp án đúng
                kq = c
                da_d = ('\\True $%s$' % (latex(kq)))

                # 3. Tạo các đáp án nhiễu
                s = [
                    '$%s$' % (latex(kq + 5)),
                    '$%s$' % (latex(kq - 5 if kq > 5 else kq + 10)),
                    '$%s$' % (latex(kq * 2)),
                    '$%s$' % (latex(0)),
                    '$%s$' % (latex(v)),
                    '$%s$' % (latex(k))
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # 4. Nội dung câu hỏi
                noidungcauhoi = ('''Một cái hồ chứa $%s l$ nước ngọt. Người ta bơm nước biển có nồng độ muối $%s g/l$ vào hồ với tốc độ $%s l/$ phút. Nồng độ muối trong hồ khi $t$ dần về dương vô cùng (đơn vị g/l) bằng bao nhiêu?'''
                                 % (latex(V0), latex(c), latex(v)))

                # 5. Nội dung lời giải
                loigiai = ('''Sau $t$ phút bơm nước vào hồ thì lượng nước là $%s + %st$ $(l)$ và lượng muối có được là $%s \\cdot %st$ $(g)$. \\\\
                             Nồng độ muối của nước là: $C(t) = \\frac{%s \\cdot %st}{%s + %st} = \\frac{%s t}{%s + t}$ $(g/l)$. \\\\
                             Khi $t$ dần về dương vô cùng, ta có: \\\\
                             $\\lim_{t \\to +\\infty} C(t) = \\lim_{t \\to +\\infty} \\frac{%s t}{%s + t} = \\lim_{t \\to +\\infty} \\frac{%s t}{t \\left( \\frac{%s}{t} + 1 \\right)} = \\lim_{t \\to +\\infty} \\frac{%s}{\\frac{%s}{t} + 1} = %s$ $(g/l)$.'''
                           % (latex(V0), latex(v), latex(c), latex(v),
                              latex(c), latex(v), latex(V0), latex(v), latex(c), latex(k),
                              latex(c), latex(k), latex(c), latex(k), latex(c), latex(k), latex(kq)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # 6. Xuất câu trắc nghiệm theo định dạng yêu cầu
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)


            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

