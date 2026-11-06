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


def bt_dang19_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các số a, b, c tương ứng với các điểm cực trị sao cho a < b < c
                a = random.randint(-5, -1)
                b = random.randint(a + 1, 2)
                c = random.randint(b + 2, 6)

                # Sinh một số d thuộc [a; c] nhưng khác a, b, c để làm phương án nhiễu
                tap_d = [x for x in range(a, c + 1) if x not in (a, b, c)]
                if not tap_d:
                    d = 0
                else:
                    d = random.choice(tap_d)

                # Bước 4: Điều chỉnh các đáp án trắc nghiệm (đảm bảo không trùng nhau)
                # Đáp án đúng: Do f'(x) >= 0 trên [a; c] nên hàm số đồng biến, max đạt tại c
                da = '\\max_{[%s;%s]} f(x) = f(%s)' % (a, c, c)

                # Các đáp án sai
                das1 = '\\max_{[%s;%s]} f(x) = f(%s)' % (a, c, a)
                das2 = '\\max_{[%s;%s]} f(x) = f(%s)' % (a, c, b)
                das3 = '\\max_{[%s;%s]} f(x) = f(%s)' % (a, c, d)

                # Tạo bảng xét dấu đạo hàm bằng môi trường tkz-tab (thay thế cho hình ảnh)
                bang_bien_thien = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[nocadre=false,lgt=1.5,espcl=2.5]{$x$ / 1, $f'(x)$ / 1}{$-\\infty$, $%s$, $%s$, $%s$, $+\\infty$}
            \\tkzTabLine{ , -, 0, +, 0, +, 0, -, }
            \\end{tikzpicture}
            \\end{center}''' % (a, b, c))

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = f(x)$ xác định, liên tục trên $\\mathbb{R}$ và có bảng xét dấu đạo hàm như sau:
            %s
            Giá trị lớn nhất của hàm số $f(x)$ trên đoạn $[%s;%s]$ là''' % (bang_bien_thien, a, c))

                # Thêm định dạng LaTeX và trộn các đáp án
                da_d = ('\\True $%s$' % str(da))
                da_s1 = '$%s$' % str(das1)
                da_s2 = '$%s$' % str(das2) 
                da_s3 = '$%s$' % str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Dựa vào bảng xét dấu, ta thấy $f'(x) \\ge 0$ với mọi $x \\in [%s; %s]$ và $f'(x) = 0$ tại $x = %s$. \\\\
            Suy ra hàm số $y = f(x)$ đồng biến trên đoạn $[%s; %s]$. \\\\
            Vì vậy, giá trị lớn nhất của hàm số trên đoạn $[%s; %s]$ đạt được tại điểm cuối của đoạn. \\\\
            Do đó, $\\max_{[%s;%s]} f(x) = f(%s)$.''' % (a, c, b, a, c, a, c, a, c, c))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{\n' + str(loigiai) + '\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

