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


def bt_dang13_p1_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số: x + a*sqrt(x + b) + m = 0
                # Để đảm bảo hoành độ đỉnh -a/2 < 0, ta chọn a > 0
                b = random.randint(1, 10)
                a = random.randint(2, 6)

                # Tính toán tọa độ đỉnh cụ thể
                t_I_val = Rational(-a, 2)
                # f(t) = t^2 + at - b
                y_I_val = t_I_val**2 + a*t_I_val - b

                # Đáp án đúng: -m < -b <=> m > b
                da_dung = '$m > %s$' % (latex(b))

                # Các phương án sai
                s = [
                    '$m < %s$' % (latex(b)),
                    '$m > %s$' % (latex(-b)),
                    '$m \\le %s$' % (latex(b)),
                    '$m < %s$' % (latex(-b)),
                    '$m \\ge %s$' % (latex(b)),
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Giá trị của $m$ để phương trình $x + %s\\sqrt{x + %s} + m = 0$ vô nghiệm là'
                                 % (latex(a), latex(b)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải xét tam thức bậc hai với tọa độ đỉnh đã tính toán
                loigiai = ('''Điều kiện xác định: $x \\ge -%s$. \\\\
                             Đặt $t = \\sqrt{x + %s}$, điều kiện $t \\ge 0$. \\\\
                             Ta có $t^2 = x + %s \\Rightarrow x = t^2 - %s$. \\\\
                             Khi đó phương trình trở thành: \\\\
                             $(t^2 - %s) + %st + m = 0 \\Leftrightarrow t^2 + %st - %s = -m \\quad (2)$. \\\\
                             Phương trình ban đầu vô nghiệm khi và chỉ khi phương trình (2) không có nghiệm $t \\in [0; +\\infty)$. \\\\
                             Xét hàm số bậc hai $f(t) = t^2 + %st - %s$ có hệ số $a = 1 > 0$, tọa độ đỉnh $I(%s; %s)$. \\\\
                             Vì hoành độ đỉnh $t_I = %s < 0$ nên hàm số $f(t)$ đồng biến trên khoảng $[0; +\\infty)$. \\\\
                             Bảng biến thiên của hàm số $f(t)$ trên $[0; +\\infty)$: \\\\
                             \\begin{center}
                             \\begin{tikzpicture}
                                \\tkzTabInit[lgt=1.2,espcl=2.5]{$t$/0.7, $f(t)$/2}{0, $+\\infty$}
                                \\tkzTabVar{-/ $%s$, +/ $+\\infty$}
                             \\end{tikzpicture}
                             \\end{center}
                             Dựa vào bảng biến thiên, để phương trình (2) vô nghiệm thì đường thẳng $y = -m$ phải nằm dưới giá trị nhỏ nhất của hàm số trên nửa khoảng $[0; +\\infty)$. \\\\
                             Suy ra $-m < %s \\Leftrightarrow m > %s$. \\\\
                             Vậy $m > %s$ là các giá trị cần tìm.'''
                           % (latex(b), latex(b), latex(b), latex(b),
                              latex(b), latex(a), latex(a), latex(b), 
                              latex(a), latex(b), 
                              latex(t_I_val), latex(y_I_val),
                              latex(t_I_val),
                              latex(-b), 
                              latex(-b), latex(b), latex(b)
                             ))

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

