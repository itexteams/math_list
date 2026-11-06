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


def bt_dang21_p1_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (Dạng 1: Phương trình bậc 2 kết hợp căn thức)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các hệ số ngẫu nhiên để bài toán luôn có nghiệm và đẹp
                # Phương trình dạng: a*x^2 - 2*a*x + m + sqrt(-x^2 + 2x) = k
                # Đặt t = sqrt(-x^2 + 2x) => t^2 = -x^2 + 2x => x^2 - 2x = -t^2
                # Phương trình trở thành: a*(-t^2) + m + t = k  => m = a*t^2 - t + k

                a = randint(2, 4) # Hệ số a dương để parabol hướng lên
                k = randint(-2, 2)

                # Biểu thức trong căn: -x^2 + 2x = -(x-1)^2 + 1. Do đó t thuộc [0, 1]
                # Hàm số f(t) = a*t^2 - t + k
                # Tọa độ đỉnh t_v = 1/(2a). Vì a >= 2 nên 0 < t_v <= 1/4, thuộc [0, 1]

                t_v = Rational(1, 2*a)
                f_0 = k
                f_1 = a - 1 + k
                f_tv = a * (t_v**2) - t_v + k # Giá trị cực tiểu f(1/2a) = k - 1/(4a)

                # Tập giá trị là [f_tv, max(f_0, f_1)]
                # Vì a >= 2 nên a-1 > 0 => f_1 > f_0. Vậy Max là f_1.
                val_min = f_tv
                val_max = f_1
                val_mid = f_0 # Giá trị tại biên t=0 để tạo phương án nhiễu

                # Chuyển sang định dạng LaTeX
                str_min = latex(val_min)
                str_max = latex(val_max)
                str_mid = latex(val_mid)

                # Đáp án đúng
                da_dung = '$%s \\le m \\le %s$' % (str_min, str_max)

                # Tạo các phương án sai (đảm bảo không trùng đáp án đúng)
                s = [
                    '$%s \\le m \\le %s$' % (latex(0), latex(Rational(1, 4))),
                    '$%s \\le m$' % (str_mid),
                    '$%s \\le m \\le %s$' % (str_min, str_mid),
                    '$%s \\le m < %s$' % (str_min, str_max),
                    '$m \\le %s$' % (str_max),
                    '$%s < m < %s$' % (str_min, str_max)
                ]

                # Loại bỏ phương án nếu lỡ trùng với đáp án đúng
                if da_dung in s:
                    s.remove(da_dung)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                # Biểu thức x: a*x^2 - 2*a*x tương ứng với 2*x^2 - 4x khi a=2
                noidungcauhoi = ('''Giá trị của tham số $m$ để phương trình $%sx^2 - %sx + m + \\sqrt{-x^2 + 2x} = %s$ có nghiệm là'''
                                 % (latex(a), latex(2*a), latex(k)))

                # Đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Lời giải chi tiết với Bảng biến thiên TikZ
                # f(t) = a*t^2 - t + k. t_v = 1/(2a). f(0)=k, f(t_v), f(1)=a-1+k
                loigiai = ('''Đưa phương trình về dạng: $m = -%sx^2 + %sx - \\sqrt{-x^2 + 2x} + %s$. \\\\
                            Điều kiện xác định: $-x^2 + 2x \\ge 0 \\Leftrightarrow 0 \\le x \\le 2$. \\\\
                            Đặt $t = \\sqrt{-x^2 + 2x}$. Xét hàm số $g(x) = -x^2 + 2x$ trên $[0; 2]$, ta có $g(x) = -(x-1)^2 + 1 \\le 1$. \\\\
                            Vì $g(x) \\ge 0$ nên $t \\in [0; 1]$. \\\\
                            Khi đó $t^2 = -x^2 + 2x \\Rightarrow %st^2 = -%sx^2 + %sx$. \\\\
                            Phương trình trở thành: $%st^2 - t + %s = m$. \\\\
                            Xét hàm số $f(t) = %st^2 - t + %s$ trên đoạn $[0; 1]$. \\\\
                            Đây là hàm số bậc hai có hệ số $a = %s > 0$ nên bề lõm hướng lên trên. \\\\
                            Đỉnh của parabol có hoành độ $t = \\frac{1}{2 \\cdot %s} = %s \\in [0; 1]$. \\\\
                            Ta có: $f(0) = %s$; $f(1) = %s$; $f\\left(%s\\right) = %s$. \\\\
                            Bảng biến thiên: \\\\
                            \\begin{center}
                            \\begin{tikzpicture}
                                \\tkzTabInit[lgt=1.2,espcl=2.5]{$t$/1,$f(t)$/2}{0,$%s$,1}
                                \\tkzTabVar{+/ $%s$ , -/ $%s$ , +/ $%s$ }
                            \\end{tikzpicture}
                            \\end{center}
                            Dựa vào bảng biến thiên, để phương trình có nghiệm thì $m$ phải thuộc tập giá trị của $f(t)$ trên $[0; 1]$. \\\\
                            Vậy $%s \\le m \\le %s$.'''
                           % (latex(a), latex(2*a), latex(k),
                              latex(a), latex(a), latex(2*a),
                              latex(a), latex(k), 
                              latex(a), latex(k),
                              latex(a), latex(a), str_min if t_v == val_min else latex(t_v),
                              str_mid, str_max, latex(t_v), str_min,
                              latex(t_v), str_mid, str_min, str_max,
                              str_min, str_max))

            # Xuất câu trắc nghiệm đúng cấu trúc
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

