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


def bt_dang64_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số nguyên a trong khoảng [2, 5] cho hàm f(x) = 1/(x-a) + 3sin^2(x)
                # Random số nguyên b trong khoảng [1, 4] cho hàm g(x) = sin(sqrt(b-x))
                a = random.randint(2, 5)
                b = random.randint(1, 4)

                # Định nghĩa chuỗi hiển thị toán học cho các hàm số
                fx_str = 'f(x) = \\frac{1}{x-%s} + 3\\sin^2 x' % (latex(a))
                gx_str = 'g(x) = \\sin \\sqrt{%s-x}' % (latex(b))

                # Các giá trị dùng trong lời giải chi tiết
                am_a = -a

                # Câu hỏi sử dụng %s đúng cấu trúc mẫu
                noidungcauhoi = ('''Cho hai hàm số $%s$ và $%s$. Kết luận nào sau đây đúng về tính chẵn lẻ của hai hàm số này?'''
                                 % (str(fx_str), str(gx_str)))

                # Phương án trả lời trắc nghiệm không thêm dấu chấm ở cuối
                da = 'Cả hai hàm số $f(x);g(x)$ đều là hàm số không chẵn không lẻ'
                da_d = ('\\True ' + str(da))

                das1 = 'Hai hàm số $f(x);g(x)$ là hai hàm số lẻ'
                das2 = 'Hàm số $f(x)$ là hàm số chẵn; hàm số $g(x)$ là hàm số lẻ'
                das3 = 'Hàm số $f(x)$ là hàm số lẻ; hàm số $g(x)$ là hàm số không chẵn không lẻ'

                # Đưa các đáp án vào 1 danh sách trộn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết, đầy đủ từng bước theo mẫu bằng định dạng %s
                loigiai = ('''Chọn D. \\\\
                           $a$, Xét hàm số $%s$ có tập xác định là $D = \\mathbb{R} \\setminus \\{%s\\}$. \\\\
                           Ta có $x = %s \\in D$ nhưng $-x = %s \\notin D$ nên $D$ không có tính đối xứng. Do đó ta có kết luận hàm số $f(x)$ không chẵn không lẻ. \\\\
                           $b$, Xét hàm số $%s$ có tập xác định là $D_2 = (-\\infty; %s]$. Dễ thấy $D_2$ không phải là tập đối xứng nên ta kết luận hàm số $g(x)$ không chẵn không lẻ. \\\\
                           Vậy chọn D.'''
                           % (str(fx_str), latex(a), latex(am_a), latex(a), str(gx_str), latex(b)))

            # Xuất câu trắc nghiệm đúng định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

