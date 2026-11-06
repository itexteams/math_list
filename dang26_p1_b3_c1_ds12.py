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


def bt_dang26_p1_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random x0 (vị trí tiệm cận đứng)
                x0 = randint(-4, 4)
                # Random x1, x2 (hoành độ các điểm cực trị, đảm bảo x1 < x0 < x2)
                x1 = x0 - randint(1, 3)
                x2 = x0 + randint(1, 3)

                # Random y1, y2 (tung độ các điểm cực trị, đồ thị dạng này thường có y1 < y2)
                y1 = randint(-5, 2)
                y2 = y1 + randint(2, 6)

                str_x0 = latex(x0)
                str_x1 = latex(x1)
                str_x2 = latex(x2)
                str_y1 = latex(y1)
                str_y2 = latex(y2)

                # Các đáp án trắc nghiệm
                da = '$x = %s$' % (str_x0)

                # Tạo tập hợp các phương án nhiễu
                s = [
                    '$x = %s$' % (str_x1),
                    '$x = %s$' % (str_x2),
                    '$y = %s$' % (str_x0),
                    '$y = %s$' % (str_y1),
                    '$y = %s$' % (str_y2)
                ]

                # Lọc đáp án trùng
                s = list(set(s))
                if da in s:
                    s.remove(da)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Code TikZ vẽ Bảng biến thiên
                bang_bien_thien = ('''\\begin{center}
            \\begin{tikzpicture}[line width=1pt]
            \\draw (0,2.4) -- (12,2.4);
            \\draw (0,1.6) -- (12,1.6);
            \\draw (1,0) -- (1,3.2);
            \\node at (0.5, 2.8) {$x$};
            \\node at (0.5, 2.0) {$y'$};
            \\node at (0.5, 0.8) {$y$};
            \\node at (1.5, 2.8) {$-\\infty$};
            \\node at (3.5, 2.8) {$%s$};
            \\node at (6.0, 2.8) {$%s$};
            \\node at (8.5, 2.8) {$%s$};
            \\node at (11.0, 2.8) {$+\\infty$};
            \\node at (2.5, 2.0) {$+$};
            \\node at (3.5, 2.0) {$0$};
            \\node at (4.75, 2.0) {$-$};
            \\node at (7.25, 2.0) {$-$};
            \\node at (8.5, 2.0) {$0$};
            \\node at (9.75, 2.0) {$+$};
            \\draw (5.9, 0) -- (5.9, 2.4);
            \\draw (6.1, 0) -- (6.1, 2.4);
            \\node at (1.5, 0.3) {$-\\infty$};
            \\node at (3.5, 1.3) {$%s$};
            \\node at (5.5, 0.3) {$-\\infty$};
            \\node at (6.5, 1.3) {$+\\infty$};
            \\node at (8.5, 0.3) {$%s$};
            \\node at (11.0, 1.3) {$+\\infty$};
            \\draw[->] (1.8, 0.4) -- (3.2, 1.2);
            \\draw[->] (3.8, 1.2) -- (5.2, 0.4);
            \\draw[->] (6.8, 1.2) -- (8.2, 0.4);
            \\draw[->] (8.8, 0.4) -- (10.5, 1.2);
            \\end{tikzpicture}
            \\end{center}''' % (str_x1, str_x0, str_x2, str_y1, str_y2))

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=\\frac{ax^2+bx+c}{mx+n}$ ($a \\neq 0, m \\neq 0$) với $a,b,c,m,n$ là các số thực và có bảng biến thiên như sau:
            %s
            Tiệm cận đứng của đồ thị hàm số đã cho là''' % (bang_bien_thien))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Từ bảng biến thiên, ta có $\\lim\\limits_{x \\to %s^-} y = -\\infty$ và $\\lim\\limits_{x \\to %s^+} y = +\\infty$. \\\\
            Do đó, đường thẳng $x = %s$ là tiệm cận đứng của đồ thị hàm số.''' % (str_x0, str_x0, str_x0))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

